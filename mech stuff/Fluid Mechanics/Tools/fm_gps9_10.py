"""GPS 9 & 10 (viscous flow, AM2530): every number quoted in
   '10 Viscous Flow and Exact Solutions/Viscous Flow - Solved Problems' is recomputed here and the figures are drawn.
   Run `python fm_gps9_10.py` (figures go to ../assets/FM-V*.png)."""
import os
from math import log10, sqrt, pi, log
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G = 9.81
RHO, MU, NU, PV, PATM = 998.0, 1.01e-3, 1.01e-6, 2.34e3, 101.3e3          # data sheet, water 20 C
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})


def colebrook(Re, ed):
    if Re < 2300:
        return 64. / Re
    return brentq(lambda f: 1 / sqrt(f) + 2.0 * log10(ed / 3.7 + 2.51 / (Re * sqrt(f))), 0.005, 0.2)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(ASSETS, name), dpi=150)
    plt.close(fig)


# ============================================================ 1  parallel-plate flow chamber
def p1():
    r = {}
    h, w, L, rho, mu, tw = 0.25e-3, 10e-3, 40e-3, 1000.0, 0.80e-3, 1.2
    Q = tw * w * h ** 2 / (6 * mu)
    V = Q / (w * h)
    r.update(Q=Q, Q_mLmin=Q * 6e7, V=V, umax=1.5 * V, dpdx=-12 * mu * Q / (w * h ** 3), Re=rho * V * h / mu)
    r["dp"] = -r["dpdx"] * L
    r["dpdx_check"] = -2 * tw / h
    for hh in (0.23e-3, 0.25e-3, 0.27e-3):
        r["tau_%g" % (hh * 1e3)] = 6 * mu * Q / (w * hh ** 2)
    return r


# ============================================================ 2  lava
def p2():
    r = {}
    rho, h, th, us = 2700.0, 2.0, np.radians(5), 1.5
    mu = rho * G * np.sin(th) * h ** 2 / (2 * us)
    V = 2 * us / 3
    q = V * h
    r.update(mu=mu, V=V, q=q, Re=rho * V * h / mu, tau_bed=rho * G * h * np.sin(th))
    mu2 = 10 * mu
    h2 = (3 * mu2 * q / (rho * G * np.sin(th))) ** (1 / 3)
    r.update(h2=h2, us2=1.5 * q / h2, tau_bed2=rho * G * h2 * np.sin(th), ratio=h2 / h, us2_check=rho * G * np.sin(th) * h2 ** 2 / (2 * mu2), Re2=rho * (q / h2) * h2 / mu2)
    return r


# ============================================================ 3  stagnation-point flow
def p3():
    r = {}
    rho, nu, B = 970.0, 1.0e-3, 25.0
    mu = rho * nu
    x, y = 10e-3, 4e-3
    r.update(mu=mu, vis_xx=2 * mu * B * y, vis_yy=-2 * mu * B * y, tau_xy=mu * B * x, tau_wall=mu * B * x, omega_z=-B * x,
             ell01=(0.1 * nu / B) ** (1 / 3), Re_P=B * (np.hypot(x, y)) ** 3 / nu, dp_scale=mu * B * 10e-3)
    return r


# ============================================================ 4  wire coating
def p4():
    r = {}
    a, R, L, U, rho, mu = 0.5e-3, 0.6e-3, 20e-3, 2.0, 1100.0, 0.50
    ln = log(R / a)
    tau = mu * U / (a * ln)
    F = tau * 2 * pi * a * L
    Q = pi * U * ((R ** 2 - a ** 2) / (2 * ln) - a ** 2)
    ab = sqrt((R ** 2 - a ** 2) / (2 * ln))
    h = R - a
    tauC = mu * U / h
    FC = tauC * 2 * pi * a * L
    QC = pi * a * U * h
    t_exact_from_Q = sqrt(a ** 2 + Q / (pi * U)) - a
    r.update(ln=ln, tau=tau, F=F, Q=Q, Q_mLs=Q * 1e6, t=ab - a, t_check=t_exact_from_Q, tauC=tauC, FC=FC, QC=QC, tC=h / 2,
             tC_exact_circle=(-a + sqrt(a ** 2 + a * h)) , Re=rho * (U / 2) * h / mu, dF=(FC - F) / F, dQ=(QC - Q) / Q, dt=(h / 2 - (ab - a)) / (ab - a))
    return r


# ============================================================ 5  dashpot
def p5():
    r = {}
    D, L, rho, mu, h, F = 40e-3, 30e-3, 880.0, 0.15, 0.30e-3, 250.0
    A = pi * D ** 2 / 4
    dp = F / A
    U = dp * h ** 3 / (3 * mu * L * (D + 2 * h))
    c = F / U
    Vbar = A * U / (pi * D * h)
    Re = rho * Vbar * h / mu
    h2 = 1.2 * h
    ratio = (D + 2 * h2) / (D + 2 * h) * (h / h2) ** 3
    # direct check: flow through gap from the profile
    Qgap = pi * D * (dp * h ** 3 / (12 * mu * L) - U * h / 2)
    r.update(A=A, dp=dp, U=U, c=c, Vbar=Vbar, Re=Re, red=Re * h / L, ratio=ratio, Qgap=Qgap, AU=A * U, hD=h / D,
             u_mid=dp / (2 * mu * L) * h ** 2 / 4 - U / 2)
    return r


# ============================================================ 6  syringe
def p6():
    r = {}
    rho, mu, Db, L, F = 1000.0, 0.015, 8.66e-3, 16e-3, 15.0
    Ab = pi * Db ** 2 / 4
    dp = F / Ab
    r["dp"] = dp
    ds = (0.16e-3, 0.21e-3, 0.26e-3, 0.34e-3)
    rows = []
    for d in ds:
        Q = pi * d ** 4 * dp / (128 * mu * L)
        V = Q / (pi * d ** 2 / 4)
        rows.append(dict(d=d, Q=Q, t=1e-6 / Q, V=V, Vmax=2 * V, tau=dp * d / (4 * L), Re=rho * V * d / mu, KE=0.5 * rho * V ** 2, KE2=rho * V ** 2, frac=0.5 * rho * V ** 2 / dp, frac2=rho * V ** 2 / dp,
                         Le=0.06 * (rho * V * d / mu) * d, t_cold=2 * 1e-6 / Q))
    r["rows"] = rows
    r["Ab"] = Ab
    r["tau_8muVd"] = 8 * mu * rows[1]["V"] / ds[1]
    return r


# ============================================================ 7  siphon
D7, EPS7 = 0.05, 0.046e-3
ED7 = EPS7 / D7
A7 = pi * D7 ** 2 / 4


def siphon_V(H):
    """outlet H m below the surface, total length 20 + (H - 6)"""
    Ltot = 20.0 + (H - 6.0)
    def res(V):
        f = colebrook(V * D7 / NU, ED7)
        return V ** 2 / (2 * G) * (1 + 0.8 + 2 * 0.9 + f * Ltot / D7) - H
    V = brentq(res, 0.1, 40)
    return V, colebrook(V * D7 / NU, ED7)


def crest_head(V, f):
    """(patm - p)/rho g at the end of the crest"""
    vh = V ** 2 / (2 * G)
    loss = (0.8 + 2 * 0.9 + f * 8.0 / D7) * vh
    return 4.5, vh, loss


def p7():
    r = {}
    V, f = siphon_V(6.0)
    Q = V * A7
    c1, c2, c3 = crest_head(V, f)
    tot = c1 + c2 + c3
    pabs = PATM - RHO * G * tot
    r.update(V=V, f=f, Q=Q, Re=V * D7 / NU, vh=c2, hl_c=c3, tot=tot, p_abs=pabs, fr=(c1 / tot, c2 / tot, c3 / tot), margin=pabs / PV,
             head_lim=(PATM - PV) / (RHO * G))
    # (d) cavitation limit
    lim = (PATM - PV) / (RHO * G)
    def res(Hh):
        Vv, ff = siphon_V(Hh)
        a, b, c = crest_head(Vv, ff)
        return a + b + c - lim
    Hc = brentq(res, 6.0, 40.0)
    Vc, fc = siphon_V(Hc)
    r.update(Hc=Hc, Vc=Vc, Qc=Vc * A7, fc=fc, Lc=20 + Hc - 6, Rec=Vc * D7 / NU)
    # variations the designer could use (rounded inlet, no change else)
    def tot_with(K_ent, H=6.0):
        Ltot = 20.0 + (H - 6.0)
        res2 = lambda V: V ** 2 / (2 * G) * (1 + K_ent + 1.8 + colebrook(V * D7 / NU, ED7) * Ltot / D7) - H
        Vv = brentq(res2, .1, 40)
        ff = colebrook(Vv * D7 / NU, ED7)
        vh = Vv ** 2 / (2 * G)
        return Vv, 4.5 + vh + (K_ent + 1.8 + ff * 8.0 / D7) * vh
    r["rounded_inlet"] = tot_with(0.04)
    return r


# ============================================================ 8  pump system
def p8():
    r = {}
    L, D, Q, dz = 60.0, 0.05, 4e-3, 12.0
    SK = 0.5 + 2.0 + 4 * 0.9 + 0.2 + 1.0
    out = {}
    for name, D_, Qb in (("single 50", 0.05, Q), ("parallel 2x50", 0.05, Q / 2), ("single 65", 0.065, Q)):
        A = pi * D_ ** 2 / 4
        V = Qb / A
        Re = V * D_ / NU
        f = colebrook(Re, EPS7 / D_)
        vh = V ** 2 / (2 * G)
        fric = f * L / D_ * vh
        minor = SK * vh
        out[name] = dict(V=V, Re=Re, f=f, vh=vh, fric=fric, minor=minor, hp=dz + fric + minor, LD=L / D_, ed=EPS7 / D_)
    r["SK"] = SK
    r["cases"] = out
    return r


# ============================================================ figures
def fig1(a):
    h, w, mu = 0.25e-3, 10e-3, 0.80e-3
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
    y = np.linspace(0, h, 200)
    dpdx = a["dpdx"]
    u = dpdx / (2 * mu) * (y ** 2 - h * y)
    ax1.plot(u * 1e3, y * 1e3, color=BLUE, lw=2.4)
    ax1.fill_betweenx(y * 1e3, 0, u * 1e3, color=BLUE, alpha=.12)
    ax1.axvline(a["V"] * 1e3, color=GREEN, ls="--"); ax1.text(a["V"] * 1e3 + 1, .03, "mean %.1f mm/s" % (a["V"] * 1e3), color=GREEN, fontsize=8)
    ax1.plot([a["umax"] * 1e3], [h / 2 * 1e3], "o", color=RED); ax1.text(a["umax"] * 1e3 - 2, h / 2 * 1e3 + .012, "max %.1f mm/s" % (a["umax"] * 1e3), color=RED, ha="right", fontsize=8)
    ax1.set_xlabel("u (mm/s)"); ax1.set_ylabel("y (mm)  [cells at y = 0]"); ax1.set_title("parabolic profile, τ_w = 1.2 Pa at the cell layer", fontsize=10)
    hh = np.linspace(0.20e-3, 0.30e-3, 100)
    Q = a["Q"]
    ax2.plot(hh * 1e3, 6 * mu * Q / (w * hh ** 2), color=ORANGE, lw=2.4)
    for g in (0.23e-3, 0.25e-3, 0.27e-3):
        t = 6 * mu * Q / (w * g ** 2)
        ax2.plot([g * 1e3], [t], "o", color=RED if g != 0.25e-3 else GREEN)
        ax2.annotate("%.2f Pa" % t, (g * 1e3, t), (g * 1e3 + .004, t + .05), fontsize=9)
    ax2.axvspan(0.23, 0.27, color=GREY, alpha=.1)
    ax2.set_xlabel("gap h (mm)"); ax2.set_ylabel("wall shear stress (Pa)"); ax2.set_title("fixed Q: τ_w ∝ 1/h², so ±8 % in h is −14 % / +18 % in τ_w", fontsize=10)
    fig.suptitle("GPS 9&10 · 1 Parallel-plate flow chamber", fontsize=11)
    save(fig, "FM-V1-chamber.png")


def fig2(a):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
    rho, th, mu = 2700.0, np.radians(5), a["mu"]
    for h, m, col, lab in ((2.0, mu, BLUE, "hot: μ = %.0f Pa·s" % mu), (a["h2"], 10 * mu, RED, "cooled: 10μ")):
        y = np.linspace(0, h, 200)
        u = rho * G * np.sin(th) / (2 * m) * (2 * h * y - y ** 2)
        ax1.plot(u, y, color=col, lw=2.4, label=lab + ", h = %.2f m" % h)
        ax1.plot([u[-1]], [h], "o", color=col)
        ax2.plot(rho * G * np.sin(th) * (h - y) / 1e3, y, color=col, lw=2.4)
    ax1.set_xlabel("u (m/s)"); ax1.set_ylabel("y from the bed (m)"); ax1.legend(fontsize=8, loc="lower right"); ax1.set_title("same flow rate q = 2.0 m²/s: deeper and slower", fontsize=10)
    ax2.set_xlabel("shear stress τ (kPa)"); ax2.set_title("τ = ρg(h − y) sinθ: linear, zero at the free surface", fontsize=10)
    ax2.text(a["tau_bed"] / 1e3 + .2, 0.08, "%.2f kPa" % (a["tau_bed"] / 1e3), color=BLUE, ha="left", fontsize=9)
    ax2.text(a["tau_bed2"] / 1e3 - .2, 0.4, "%.2f kPa" % (a["tau_bed2"] / 1e3), color=RED, ha="right", fontsize=9)
    fig.suptitle("GPS 9&10 · 2 Lava flow down a 5° slope", fontsize=11)
    save(fig, "FM-V2-lava.png")


def fig3(a):
    B, nu = 25.0, 1.0e-3
    fig, ax = plt.subplots(figsize=(8, 4.8))
    x = np.linspace(-0.03, 0.03, 300); y = np.linspace(0, 0.02, 200)
    X, Y = np.meshgrid(x, y)
    U, V = B * X * Y, -0.5 * B * Y ** 2
    ax.streamplot(X * 1e3, Y * 1e3, U, V, color=BLUE, density=1.5, linewidth=1.0, arrowsize=1.1)
    ell = a["ell01"] * 1e3
    t = np.linspace(0, pi, 100)
    ax.plot(ell * np.cos(t), ell * np.sin(t), color=RED, lw=2)
    ax.text(0, ell * 0.55, "Re = Bℓ³/ν < 0.1\nℓ < %.1f mm" % ell, color=RED, ha="center", fontsize=9, bbox=dict(fc="white", ec="none", alpha=.85))
    ax.plot([10], [4], "o", color=ORANGE, ms=8); ax.text(10.8, 4.4, "P", color=ORANGE, fontsize=11, weight="bold")
    ax.axhline(0, color="k", lw=3)
    ax.annotate("", (10, 0.0), (0, 0.0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.5))
    ax.text(5, -1.4, "τ_w = μBx = 0.2425 Pa at x = 10 mm", color=GREEN, ha="center", fontsize=8.5)
    ax.set_xlim(-30, 30); ax.set_ylim(-3, 20); ax.set_xlabel("x (mm)"); ax.set_ylabel("y (mm)")
    ax.set_title("GPS 9&10 · 3 Stagnation-point flow: streamlines xy² = const, and the creeping-flow zone", fontsize=10)
    save(fig, "FM-V3-stagnation.png")


def fig4(a):
    aa, R, U = 0.5, 0.6, 2.0
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    r = np.linspace(aa, R, 200)
    ax.plot(U * np.log(R / r) / log(R / aa), r, color=BLUE, lw=2.6, label="exact: ln(R/r) / ln(R/a)")
    ax.plot(U * (R - r) / (R - aa), r, color=ORANGE, lw=1.8, ls="--", label="plane Couette: 1 − y/h")
    ax.set_xlabel("u (m/s)"); ax.set_ylabel("r (mm)")
    ax.axhspan(0.0, aa, color=GREY, alpha=.3, xmax=1)
    ax.text(1.0, 0.49, "wire (moves at U)", ha="center", va="top", fontsize=8)
    ax.set_ylim(0.44, 0.62); ax.legend(fontsize=9, loc="upper right")
    ax.set_title("GPS 9&10 · 4 Wire coating: the gap is thin enough that Couette is within a few percent", fontsize=10)
    save(fig, "FM-V4-wire.png")


def fig5(a):
    D, L, mu, h, F = 40e-3, 30e-3, 0.15, 0.30e-3, 250.0
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
    y = np.linspace(0, h, 300)
    u = a["dp"] / (2 * mu * L) * (h * y - y ** 2) - a["U"] * y / h
    ax1.plot(u, y * 1e3, color=BLUE, lw=2.4)
    ax1.axvline(0, color="k", lw=.8)
    ax1.set_xlabel("u (m/s), up positive"); ax1.set_ylabel("y (mm)  [0 = cylinder wall, 0.3 = piston]")
    ax1.annotate("piston face moves down\nat U = %.1f mm/s" % (a["U"] * 1e3), (-a["U"], h * 1e3), (0.12, 0.27), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    ax1.set_title("Poiseuille (pressure) + Couette (moving piston)", fontsize=10)
    hh = np.linspace(0.2e-3, 0.5e-3, 200)
    c = 3 * mu * L * (pi * D ** 2 / 4) * (D + 2 * hh) / hh ** 3
    ax2.semilogy(hh * 1e3, c, color=ORANGE, lw=2.4)
    for g, col in ((0.30e-3, GREEN), (0.36e-3, RED)):
        cg = 3 * mu * L * (pi * D ** 2 / 4) * (D + 2 * g) / g ** 3
        ax2.plot([g * 1e3], [cg], "o", color=col); ax2.annotate("%.0f N·s/m" % cg, (g * 1e3, cg), (g * 1e3 + .01, cg * 1.5), fontsize=9)
    ax2.set_xlabel("radial clearance h (mm)"); ax2.set_ylabel("damping coefficient c (N·s/m)"); ax2.set_title("c ∝ (D + 2h)/h³: wear of 20 % cuts it by 42 %", fontsize=10)
    fig.suptitle("GPS 9&10 · 5 Dashpot", fontsize=11)
    save(fig, "FM-V5-dashpot.png")


def fig6(a):
    rows = a["rows"]
    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    d = np.array([r["d"] for r in rows]) * 1e3
    t = np.array([r["t"] for r in rows]); tc = np.array([r["t_cold"] for r in rows])
    w = 0.012
    ax.bar(d - w / 2 * 1.1, t, w, color=BLUE, label="room temperature"); ax.bar(d + w / 2 * 1.1, tc, w, color=PURPLE, label="from the fridge (2 μ)")
    ax.set_yscale("log"); ax.axhline(10, color=RED, ls="--"); ax.text(0.335, 11, "10 s limit", color=RED, ha="right", fontsize=9)
    for x, v in zip(d, t):
        ax.text(x - w * .6, v * 1.1, "%.1f" % v, ha="center", fontsize=8, color=BLUE)
    for x, v in zip(d, tc):
        ax.text(x + w * .6, v * 1.1, "%.1f" % v, ha="center", fontsize=8, color=PURPLE)
    ax.set_xticks(d); ax.set_xticklabels(["%.2f\n(30 G)" % d[0], "%.2f\n(27 G)" % d[1], "%.2f\n(25 G)" % d[2], "%.2f\n(23 G)" % d[3]])
    ax.set_xlabel("needle inside diameter (mm)"); ax.set_ylabel("time to inject 1.0 mL (s)"); ax.legend(fontsize=9)
    ax.set_title("GPS 9&10 · 6 Syringe: time ∝ μ/d⁴", fontsize=10.5)
    save(fig, "FM-V6-syringe.png")


def fig7(a):
    V, f = a["V"], a["f"]
    vh = V ** 2 / (2 * G)
    fr = f * 1.0 / D7 * vh                      # friction head per metre of pipe
    s1 = 7.0                                    # sketch geometry: rising leg 7 m, crest 1 m, down-leg 12 m
    s = np.array([0, s1, 8.0, 20.0])
    z = np.array([-1.0, 4.5, 4.5, -6.0])
    # energy line
    el = [0.0, ]
    el.append(-0.8 * vh)                                          # after inlet
    segs = [(0, s1), (s1, 8.0), (8.0, 20.0)]
    S, E = [0.0, 0.0], [0.0, -0.8 * vh]
    cur = -0.8 * vh
    for (a_, b_), elbow in zip(segs, (0.9, 0.9, 0.0)):
        cur -= fr * (b_ - a_)
        S += [b_, b_] ; E += [cur, cur - elbow * vh]
        cur -= elbow * vh
    S, E = np.array(S[:-1] if False else S), np.array(E)
    fig, ax = plt.subplots(figsize=(10, 4.9))
    ax.axhline(0, color=BLUE, lw=1, ls=":"); ax.text(20.3, 0.05, "reservoir level", color=BLUE, fontsize=8)
    ax.plot(s, z, color="#555", lw=6, alpha=.45, solid_capstyle="round", label="pipe")
    ax.plot(S, E, color=RED, lw=2.2, label="energy line (EGL)")
    ax.plot(S, E - vh, color=GREEN, lw=2.2, label="hydraulic grade line (HGL) = EGL − V²/2g")
    lim = 4.5 - (PATM - PV) / (RHO * G)
    ax.plot([6, 9.5], [lim, lim], color=ORANGE, ls="--", lw=2)
    ax.text(9.8, lim - .05, "HGL must stay above this at the crest\n(below it the water boils): %.2f m" % lim, color=ORANGE, fontsize=8, va="center")
    ax.plot([8], [-a["tot"] + 4.5], "o", color=GREEN)
    ax.annotate("HGL at the crest end: %.2f m below the surface\n(pressure %.2f m below atmospheric)" % (a["tot"] - 4.5, a["tot"]), (8, -a["tot"] + 4.5), (0.2, -7.4), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("jet KE\nV²/2g = %.2f m" % vh, (20, -6 + vh / 2), (17.0, -2.6), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.set_xlim(-1, 22); ax.set_ylim(-9, 6.5); ax.set_xlabel("distance along the pipe (m, schematic)"); ax.set_ylabel("height above the reservoir surface (m)")
    ax.legend(fontsize=8, loc="upper right"); ax.set_title("GPS 9&10 · 7(e) Siphon: grade lines for Q = %.1f L/s (not to scale)" % (a["Q"] * 1e3), fontsize=10)
    save(fig, "FM-V7a-siphon-grade-lines.png")


def fig7b(a):
    H = np.linspace(4, 14, 80)
    pabs, Q = [], []
    for h in H:
        V, f = siphon_V(h)
        c1, c2, c3 = crest_head(V, f)
        pabs.append((PATM - RHO * G * (c1 + c2 + c3)) / 1e3); Q.append(V * A7 * 1e3)
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(H, pabs, color=BLUE, lw=2.4)
    ax.axhline(PV / 1e3, color=RED, ls="--"); ax.text(4.2, PV / 1e3 - 4.2, "vapour pressure 2.34 kPa", color=RED, fontsize=9)
    ax.plot([a["Hc"]], [PV / 1e3], "o", color=RED); ax.annotate("outlet %.1f m below the surface\nQ = %.1f L/s" % (a["Hc"], a["Qc"] * 1e3), (a["Hc"], PV / 1e3), (9.0, 16), fontsize=9, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.plot([6], [a["p_abs"] / 1e3], "o", color=GREEN); ax.annotate("as built: %.1f kPa" % (a["p_abs"] / 1e3), (6, a["p_abs"] / 1e3), (6.6, 27), fontsize=9, arrowprops=dict(arrowstyle="->", color=GREY))
    ax2 = ax.twinx(); ax2.plot(H, Q, color=ORANGE, lw=1.8, ls="-."); ax2.set_ylabel("flow rate (L/s)", color=ORANGE); ax2.grid(False)
    ax.set_xlabel("depth of the outlet below the reservoir surface (m)"); ax.set_ylabel("absolute pressure at the end of the crest (kPa)")
    ax.set_title("GPS 9&10 · 7(d) How deep can the outlet go?", fontsize=10.5)
    save(fig, "FM-V7b-siphon-depth.png")


def fig8(a):
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    names = list(a["cases"].keys()); cols = ["#4a5568", ORANGE, GREEN]
    labs = ["one 50 mm pipe", "two 50 mm in parallel", "one 65 mm pipe"]
    for i, n in enumerate(names):
        c = a["cases"][n]
        ax.bar(i, 12, color="#cbd5e0", edgecolor="k", lw=.5)
        ax.bar(i, c["fric"], bottom=12, color=BLUE)
        ax.bar(i, c["minor"], bottom=12 + c["fric"], color=ORANGE)
        ax.text(i, 12 + c["fric"] + c["minor"] + .3, "%.1f m" % c["hp"], ha="center", fontsize=10, weight="bold")
        ax.text(i, 6, "static 12", ha="center", fontsize=9)
        ax.text(i, 12 + c["fric"] / 2, "friction\n%.1f" % c["fric"] if c["fric"] > 1.6 else "", ha="center", va="center", fontsize=8, color="white")
        ax.text(i, 12 + c["fric"] + c["minor"] / 2, "minor %.1f" % c["minor"] if c["minor"] > .9 else "", ha="center", va="center", fontsize=8)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs); ax.set_ylabel("pump head h_p (m)"); ax.set_ylim(0, 22)
    ax.set_title("GPS 9&10 · 8 The 12 m lift is untouchable; only the losses can shrink", fontsize=10.5)
    save(fig, "FM-V8-pump-head.png")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    a1, a2, a3, a4, a5, a6, a7, a8 = p1(), p2(), p3(), p4(), p5(), p6(), p7(), p8()
    for name, d in (("P1", a1), ("P2", a2), ("P3", a3), ("P4", a4), ("P5", a5), ("P7", a7)):
        print("---", name)
        for k, v in d.items():
            print(f"  {k:16s} {v}")
    print("--- P6")
    print("  dp", a6["dp"], "Ab", a6["Ab"], "tau_8muVd", a6["tau_8muVd"])
    for r in a6["rows"]:
        print("  ", {k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()})
    print("--- P8  sum K =", a8["SK"])
    for n, c in a8["cases"].items():
        print("  ", n, {k: round(v, 4) for k, v in c.items()})
    fig1(a1); fig2(a2); fig3(a3); fig4(a4); fig5(a5); fig6(a6); fig7(a7); fig7b(a7); fig8(a8)
