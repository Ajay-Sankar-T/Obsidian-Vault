"""Heat Transfer (ME3101): every number quoted in the concept notes is recomputed here and the figures are drawn.
   python ht_core.py  -> prints the numbers, writes ../assets/HT-*.png.  Fluid properties from CoolProp (1 atm)."""
import os
from math import pi, sqrt, log, exp, tanh, sinh, cosh, tan, sin, cos
import numpy as np
from scipy.optimize import brentq
import CoolProp.CoolProp as CP
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
SIG = 5.670374419e-8
G = 9.81
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})


def props(fluid, T, P=101325.0):
    return dict(rho=CP.PropsSI("D", "T", T, "P", P, fluid), mu=CP.PropsSI("V", "T", T, "P", P, fluid), k=CP.PropsSI("L", "T", T, "P", P, fluid),
                cp=CP.PropsSI("C", "T", T, "P", P, fluid), Pr=CP.PropsSI("Prandtl", "T", T, "P", P, fluid))


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ================================================================ conduction
def wall():
    A, Ti, To, hi, ho = 10.0, 22.0, -5.0, 8.0, 25.0
    layers = [("brick", 0.20, 0.7), ("insulation", 0.05, 0.04), ("plaster", 0.02, 0.8)]
    R = [1 / (hi * A)] + [L / (k * A) for _, L, k in layers] + [1 / (ho * A)]
    Rt = sum(R)
    Q = (Ti - To) / Rt
    T = [Ti]
    for r in R:
        T.append(T[-1] - Q * r)
    return dict(R=R, Rt=Rt, Q=Q, U=1 / (A * Rt), T=T, names=["inside air film"] + [n for n, _, _ in layers] + ["outside air film"])


def pipe_insulation():
    r1, k, h, Ti, Tinf = 0.010, 0.15, 10.0, 100.0, 20.0
    qprime = lambda r2: 2 * pi * (Ti - Tinf) / (log(r2 / r1) / k + 1 / (h * r2))
    rcr = k / h
    r_be = brentq(lambda r: qprime(r) - qprime(r1), rcr * 1.001, 0.5)
    return dict(r1=r1, rcr=rcr, q1=qprime(r1), qcr=qprime(rcr), q50=qprime(0.05), r_break=r_be, f=qprime)


def fin():
    D, L, k, h, Tb, Tinf = 0.005, 0.05, 200.0, 25.0, 100.0, 25.0
    P, Ac = pi * D, pi * D ** 2 / 4
    m = sqrt(h * P / (k * Ac))
    M = sqrt(h * P * k * Ac) * (Tb - Tinf)
    mL = m * L
    q_ins = M * tanh(mL)
    q_inf = M
    c = h / (m * k)
    q_conv = M * (sinh(mL) + c * cosh(mL)) / (cosh(mL) + c * sinh(mL))
    eta = tanh(mL) / mL
    q_max = h * P * L * (Tb - Tinf)
    eff = q_ins / (h * Ac * (Tb - Tinf))
    Lc = L + D / 4
    q_corr = M * tanh(m * Lc)
    return dict(m=m, M=M, mL=mL, q_ins=q_ins, q_inf=q_inf, q_conv=q_conv, eta=eta, q_max=q_max, eff=eff, q_corr=q_corr, params=(D, L, k, h, Tb, Tinf, P, Ac))


def lumped():
    d, rho, c, k, h, T0, Tinf = 0.025, 7800.0, 480.0, 45.0, 100.0, 500.0, 25.0
    Lc = d / 6
    Bi = h * Lc / k
    tau = rho * c * Lc / h
    t_to_100 = -tau * log((100 - Tinf) / (T0 - Tinf))
    return dict(Lc=Lc, Bi=Bi, tau=tau, t100=t_to_100)


def slab_one_term(Bi):
    z = brentq(lambda x: x * tan(x) - Bi, 1e-6, pi / 2 - 1e-9)
    C1 = 4 * sin(z) / (2 * z + sin(2 * z))
    return z, C1


def slab_exact(Bi, Fo, nterms=60):
    s = 0.0
    for n in range(nterms):
        lo, hi = n * pi + 1e-9, n * pi + pi / 2 - 1e-9
        z = brentq(lambda x: x * tan(x) - Bi, lo, hi)
        C = 4 * sin(z) / (2 * z + sin(2 * z))
        s += C * exp(-z * z * Fo)
    return s


# ================================================================ convection
def flat_plate_air():
    p = props("Air", 300.0)
    nu = p["mu"] / p["rho"]
    u, L = 5.0, 1.0
    Re = u * L / nu
    Nu = 0.664 * sqrt(Re) * p["Pr"] ** (1 / 3)
    h = Nu * p["k"] / L
    Re_x_crit = 5e5
    xc = Re_x_crit * nu / u
    Nu_mixed = lambda Re_: (0.037 * Re_ ** 0.8 - 871) * p["Pr"] ** (1 / 3)
    uu = 25.0
    Re2 = uu * 2.0 / nu
    return dict(p=p, nu=nu, Re=Re, Nu=Nu, h=h, xc=xc, delta_L=5 * L / sqrt(Re), Re_mixed=Re2, Nu_mixed=Nu_mixed(Re2), h_mixed=Nu_mixed(Re2) * p["k"] / 2.0)


def pipe_water():
    p = props("Water", 300.0)
    D, V = 0.02, 1.0
    Re = p["rho"] * V * D / p["mu"]
    f = (0.79 * log(Re) - 1.64) ** -2
    Nu_DB = 0.023 * Re ** 0.8 * p["Pr"] ** 0.4
    Nu_G = (f / 8) * (Re - 1000) * p["Pr"] / (1 + 12.7 * sqrt(f / 8) * (p["Pr"] ** (2 / 3) - 1))
    return dict(p=p, Re=Re, f=f, Nu_DB=Nu_DB, Nu_G=Nu_G, h_DB=Nu_DB * p["k"] / D, h_G=Nu_G * p["k"] / D, lam=3.66 * p["k"] / D)


def churchill_chu(Ra, Pr):
    return (0.825 + 0.387 * Ra ** (1 / 6) / (1 + (0.492 / Pr) ** (9 / 16)) ** (8 / 27)) ** 2


def vertical_plate_air():
    Ts, Tinf, L = 353.15, 293.15, 0.5
    Tf = (Ts + Tinf) / 2
    p = props("Air", Tf)
    nu = p["mu"] / p["rho"]; alpha = p["k"] / (p["rho"] * p["cp"]); beta = 1 / Tf
    Ra = G * beta * (Ts - Tinf) * L ** 3 / (nu * alpha)
    Nu = churchill_chu(Ra, p["Pr"])
    h = Nu * p["k"] / L
    return dict(Tf=Tf, nu=nu, alpha=alpha, Pr=p["Pr"], Ra=Ra, Nu=Nu, h=h, q=h * (Ts - Tinf), Gr=Ra / p["Pr"])


def boiling_condensing():
    out = {}
    rho_l = CP.PropsSI("D", "P", 101325, "Q", 0, "Water"); rho_v = CP.PropsSI("D", "P", 101325, "Q", 1, "Water")
    hfg = CP.PropsSI("H", "P", 101325, "Q", 1, "Water") - CP.PropsSI("H", "P", 101325, "Q", 0, "Water")
    sig = CP.PropsSI("surface_tension", "P", 101325, "Q", 0, "Water")
    qmax = 0.131 * sqrt(rho_v) * hfg * (sig * G * (rho_l - rho_v)) ** 0.25
    out.update(rho_l=rho_l, rho_v=rho_v, hfg=hfg, sigma=sig, q_chf=qmax)
    mu_l = CP.PropsSI("V", "P", 101325, "Q", 0, "Water"); cp_l = CP.PropsSI("C", "P", 101325, "Q", 0, "Water"); Pr_l = CP.PropsSI("Prandtl", "P", 101325, "Q", 0, "Water")
    Csf, nexp = 0.013, 1.0
    rohsenow = lambda dT: mu_l * hfg * sqrt(G * (rho_l - rho_v) / sig) * (cp_l * dT / (Csf * hfg * Pr_l ** nexp)) ** 3
    out["rohsenow10"] = rohsenow(10.0)
    out["dT_chf"] = brentq(lambda dT: rohsenow(dT) - qmax, 1, 60)
    out["rohsenow"] = rohsenow
    # film condensation, vertical plate L=1 m, Tsat=100C, Ts=80C
    Tsat, Ts, L = 373.15, 353.15, 1.0
    Tf = (Tsat + Ts) / 2
    rl = CP.PropsSI("D", "T", Tf, "Q", 0, "Water"); mu = CP.PropsSI("V", "T", Tf, "Q", 0, "Water"); k = CP.PropsSI("L", "T", Tf, "Q", 0, "Water"); cp = CP.PropsSI("C", "T", Tf, "Q", 0, "Water")
    hfg_p = hfg + 0.68 * cp * (Tsat - Ts)
    h = 0.943 * (G * rl * (rl - rho_v) * k ** 3 * hfg_p / (mu * L * (Tsat - Ts))) ** 0.25
    mdot = h * L * (Tsat - Ts) / hfg_p          # per unit width
    Regam = 4 * mdot / mu
    out.update(h_cond=h, hfg_p=hfg_p, mdot=mdot, Re_film=Regam, q_cond=h * (Tsat - Ts))
    return out


# ================================================================ radiation
def two_plates():
    e1, e2, T1, T2 = 0.8, 0.6, 500.0, 300.0
    q = SIG * (T1 ** 4 - T2 ** 4) / (1 / e1 + 1 / e2 - 1)
    e3 = 0.1
    qs = SIG * (T1 ** 4 - T2 ** 4) / ((1 / e1 + 1 / e3 - 1) + (1 / e3 + 1 / e2 - 1))
    Ts = ((T1 ** 4 + T2 ** 4) / 2) ** 0.25 if e3 else 0
    # shield temperature when both shield faces have the same emissivity
    T3 = ((T1 ** 4 * (1 / e3 + 1 / e2 - 1) + T2 ** 4 * (1 / e1 + 1 / e3 - 1)) / ((1 / e1 + 1 / e3 - 1) + (1 / e3 + 1 / e2 - 1))) ** 0.25
    return dict(q=q, q_shield=qs, reduction=1 - qs / q, T_shield=T3, black=SIG * (T1 ** 4 - T2 ** 4))


def enclosure3():
    """infinitely long equilateral duct, side 1 m: surface 1 hot (600 K, eps .8), surface 2 cold (400 K, eps .5), surface 3 adiabatic (re-radiating)."""
    F = np.array([[0, .5, .5], [.5, 0, .5], [.5, .5, 0]])
    eps = np.array([0.8, 0.5, 0.9])
    A = np.ones(3)
    T = [600.0, 400.0, None]
    Eb = [SIG * t ** 4 if t else None for t in T]
    # unknowns: J1, J2, J3 ; surfaces 1,2: (Eb - J)/((1-e)/e) = sum F (J_i - J_j)   ; surface 3 adiabatic: sum F (J3 - Jj) = 0
    M = np.zeros((3, 3)); b = np.zeros(3)
    for i in (0, 1):
        r = (1 - eps[i]) / eps[i]
        M[i, i] = 1 / r + sum(F[i, j] for j in range(3) if j != i)
        for j in range(3):
            if j != i:
                M[i, j] = -F[i, j]
        b[i] = Eb[i] / r
    M[2] = [-F[2, 0], -F[2, 1], sum(F[2, j] for j in (0, 1))]
    J = np.linalg.solve(M, b)
    q1 = (Eb[0] - J[0]) / ((1 - eps[0]) / eps[0])          # W/m2 net leaving surface 1
    q2 = (Eb[1] - J[1]) / ((1 - eps[1]) / eps[1])
    T3 = (J[2] / SIG) ** 0.25
    q_two = SIG * (600 ** 4 - 400 ** 4) / ((1 - .8) / .8 + 1 / .5 + (1 - .5) / .5 + 0)   # no re-radiating surface, view factor... (for contrast)
    return dict(J=J, q1=q1, q2=q2, T3=T3, sum=q1 + q2, F12=0.5)


# ================================================================ heat exchangers
def hx_example():
    ch, cc = 2.0 * 2100.0, 2.5 * 4180.0
    Thi, Tho, Tci = 120.0, 70.0, 20.0
    Q = ch * (Thi - Tho)
    Tco = Tci + Q / cc
    d1c, d2c = Thi - Tco, Tho - Tci
    lmtd_c = (d1c - d2c) / log(d1c / d2c)
    d1p, d2p = Thi - Tci, Tho - Tco
    lmtd_p = (d1p - d2p) / log(d1p / d2p)
    U = 400.0
    Ac, Ap = Q / (U * lmtd_c), Q / (U * lmtd_p)
    Cmin, Cmax = min(ch, cc), max(ch, cc)
    Cr = Cmin / Cmax
    NTU = U * Ac / Cmin
    eps_counter = lambda N, c: N / (1 + N) if abs(c - 1) < 1e-9 else (1 - exp(-N * (1 - c))) / (1 - c * exp(-N * (1 - c)))
    eps_parallel = lambda N, c: (1 - exp(-N * (1 + c))) / (1 + c)
    return dict(Q=Q, Tco=Tco, lmtd_c=lmtd_c, lmtd_p=lmtd_p, Ac=Ac, Ap=Ap, Cr=Cr, NTU=NTU, eps=Q / (Cmin * (Thi - Tci)), eps_check=eps_counter(NTU, Cr),
                eps_counter=eps_counter, eps_parallel=eps_parallel, Cmin=Cmin, Thi=Thi, Tho=Tho, Tci=Tci, ch=ch, cc=cc)


# ================================================================ figures
def fig_conduction(w, pi_):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    x = [0]
    th = [0.0, 0.2, 0.05, 0.02]
    names = ["film", "brick", "insulation", "plaster", "film"]
    # temperature profile through the wall (films drawn with fixed width)
    xs = [0, 0.06, 0.06 + 0.2, 0.06 + 0.25, 0.06 + 0.27, 0.06 + 0.27 + 0.06]
    for i in range(5):
        a.plot([xs[i], xs[i + 1]], [w["T"][i], w["T"][i + 1]], color=[GREY, ORANGE, BLUE, PURPLE, GREY][i], lw=3)
    for i, nm in enumerate(["air", "brick", "insulation", "plaster", "air"]):
        a.axvspan(xs[i], xs[i + 1], color=[GREY, ORANGE, BLUE, PURPLE, GREY][i], alpha=.10)
        a.text((xs[i] + xs[i + 1]) / 2, 24, nm, ha="center", fontsize=8.5)
    a.set_ylim(-8, 27); a.set_xlabel("through the wall (films not to scale)"); a.set_ylabel("temperature (°C)"); a.set_xticks([])
    a.set_title("insulation takes %.0f %% of the resistance, so %.0f %% of the drop" % (100 * w["R"][2] / w["Rt"], 100 * (w["T"][2] - w["T"][3]) / (w["T"][0] - w["T"][-1])), fontsize=9.5)
    r2 = np.linspace(pi_["r1"], 0.08, 300)
    b.plot(r2 * 1000, [pi_["f"](r) for r in r2], color=BLUE, lw=2.4)
    b.axvline(pi_["rcr"] * 1000, color=RED, ls="--"); b.text(pi_["rcr"] * 1000 + 1, 41.5, "r_cr = k/h = %.0f mm" % (pi_["rcr"] * 1000), color=RED, fontsize=9)
    b.axhline(pi_["q1"], color=GREY, ls=":"); b.text(40, pi_["q1"] + .6, "bare pipe: %.1f W/m" % pi_["q1"], color=GREY, fontsize=9)
    b.plot([pi_["r_break"] * 1000], [pi_["q1"]], "o", color=GREEN); b.annotate("break-even r = %.0f mm" % (pi_["r_break"] * 1000), (pi_["r_break"] * 1000, pi_["q1"]), (45, 46), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("outer radius of insulation r₂ (mm), pipe r₁ = 10 mm"); b.set_ylabel("heat loss per metre (W/m)"); b.set_title("thin insulation on a small pipe increases the loss", fontsize=9.5)
    fig.suptitle("Steady conduction", fontsize=11)
    save(fig, "HT-1-conduction.png")


def fig_fins(f):
    D, L, k, h, Tb, Tinf, P, Ac = f["params"]
    m = f["m"]
    x = np.linspace(0, L, 200)
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    th_inf = np.exp(-m * x)
    th_ins = np.cosh(m * (L - x)) / cosh(m * L)
    c = h / (m * k)
    th_conv = (np.cosh(m * (L - x)) + c * np.sinh(m * (L - x))) / (cosh(m * L) + c * sinh(m * L))
    a.plot(x * 1000, th_ins, color=BLUE, lw=2.4, label="insulated tip")
    a.plot(x * 1000, th_conv, color=ORANGE, lw=2.4, ls="--", label="convecting tip")
    a.plot(x * 1000, th_inf, color=GREEN, lw=2, ls=":", label="infinitely long fin")
    a.set_xlabel("distance from the base x (mm)"); a.set_ylabel("θ / θ_b"); a.legend(fontsize=9); a.set_title("pin fin D = 5 mm, L = 50 mm, k = 200, h = 25 (mL = %.1f)" % f["mL"], fontsize=9.5)
    mL = np.linspace(0.01, 4, 300)
    b.plot(mL, np.tanh(mL) / mL, color=BLUE, lw=2.4); b.axvline(f["mL"], color=RED, ls="--"); b.plot([f["mL"]], [f["eta"]], "o", color=RED)
    b.annotate("η = %.3f" % f["eta"], (f["mL"], f["eta"]), (1.0, .95), arrowprops=dict(arrowstyle="->", color=GREY))
    b.set_xlabel("mL"); b.set_ylabel("fin efficiency η = tanh(mL)/mL"); b.set_title("beyond mL ≈ 2 the tip does almost nothing", fontsize=9.5); b.set_ylim(0, 1.05)
    fig.suptitle("Extended surfaces", fontsize=11)
    save(fig, "HT-2-fins.png")


def fig_transient():
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    Fo = np.linspace(0.01, 3, 200)
    for Bi, col in ((0.1, GREEN), (1.0, BLUE), (10.0, RED)):
        a.semilogy(Fo, [slab_exact(Bi, f) for f in Fo], color=col, lw=2.2, label="Bi = %g" % Bi)
        z, C = slab_one_term(Bi)
        a.semilogy(Fo[Fo > .2], C * np.exp(-z * z * Fo[Fo > .2]), color=col, lw=1, ls=":")
    a.set_ylim(1e-3, 1.2); a.set_xlabel("Fourier number αt/L²"); a.set_ylabel("centre θ / θ₀"); a.legend(fontsize=9); a.set_title("slab, thickness 2L: exact series (solid) and one term (dotted)", fontsize=9.5)
    lp = lumped()
    t = np.linspace(0, 700, 200)
    b.plot(t, 25 + 475 * np.exp(-t / lp["tau"]), color=BLUE, lw=2.4)
    b.axvline(lp["tau"], color=GREY, ls="--"); b.text(lp["tau"] + 8, 400, "τ = %.0f s\n(63 %% of the drop)" % lp["tau"], fontsize=9)
    b.plot([lp["t100"]], [100], "o", color=RED); b.annotate("100 °C at %.0f s" % lp["t100"], (lp["t100"], 100), (330, 220), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("time (s)"); b.set_ylabel("temperature (°C)"); b.set_title("lumped steel ball, d = 25 mm, h = 100: Bi = %.4f" % lp["Bi"], fontsize=9.5)
    fig.suptitle("Transient conduction", fontsize=11)
    save(fig, "HT-3-transient.png")


def fig_convection(fp, vp):
    fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))
    p = fp["p"]; nu = fp["nu"]
    x = np.linspace(0.01, 1.5, 400)
    u = 5.0
    Rex = u * x / nu
    hx = np.where(Rex < 5e5, 0.332 * np.sqrt(Rex) * p["Pr"] ** (1 / 3) * p["k"] / x, 0.0296 * Rex ** 0.8 * p["Pr"] ** (1 / 3) * p["k"] / x)
    a.plot(x, hx, color=BLUE, lw=2.4); a.set_xlabel("distance from the leading edge x (m)"); a.set_ylabel("local h (W/m²K)"); a.set_ylim(0, 60)
    a.set_title("air at 5 m/s: h falls as x^(-1/2) while laminar", fontsize=9.5)
    delta = 5 * x / np.sqrt(np.maximum(Rex, 1)); a2 = a.twinx(); a2.plot(x, delta * 1000, color=ORANGE, ls="--"); a2.set_ylabel("δ (mm)", color=ORANGE); a2.grid(False)
    Re = np.logspace(3.3, 6, 100)
    pw = props("Water", 300.0)
    f = (0.79 * np.log(Re) - 1.64) ** -2
    b.loglog(Re, 0.023 * Re ** 0.8 * pw["Pr"] ** 0.4, color=BLUE, lw=2.2, label="Dittus–Boelter (heating)")
    b.loglog(Re, (f / 8) * (Re - 1000) * pw["Pr"] / (1 + 12.7 * np.sqrt(f / 8) * (pw["Pr"] ** (2 / 3) - 1)), color=RED, lw=2, ls="--", label="Gnielinski")
    b.axhline(3.66, color=GREEN, ls=":"); b.text(2.2e3, 4.2, "laminar, constant T_w: 3.66", color=GREEN, fontsize=9)
    b.axvline(2300, color=GREY, ls=":"); b.set_xlabel("Re = ρVD/μ"); b.set_ylabel("Nu"); b.legend(fontsize=8.5, loc="upper left"); b.set_title("water in a tube (Pr = %.1f)" % pw["Pr"], fontsize=9.5)
    Ra = np.logspace(3, 12, 200)
    c.loglog(Ra, [churchill_chu(r, 0.71) for r in Ra], color=BLUE, lw=2.4)
    c.loglog(Ra, 0.59 * Ra ** 0.25, color=GREEN, ls=":", label="laminar 0.59 Ra^(1/4)"); c.loglog(Ra, 0.1 * Ra ** (1 / 3), color=RED, ls=":", label="turbulent 0.1 Ra^(1/3)")
    c.axvline(1e9, color=GREY, ls=":"); c.text(1.3e9, 3, "transition", fontsize=8.5, color=GREY)
    c.plot([vp["Ra"]], [vp["Nu"]], "o", color=ORANGE); c.annotate("0.5 m plate, ΔT = 60 K\nRa = %.1e, Nu = %.0f" % (vp["Ra"], vp["Nu"]), (vp["Ra"], vp["Nu"]), (2e3, 100), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    c.set_xlabel("Ra = gβΔT L³/(να)"); c.set_ylabel("Nu"); c.legend(fontsize=8.5, loc="lower right"); c.set_title("vertical plate, Churchill–Chu (Pr = 0.71)", fontsize=9.5)
    fig.suptitle("Convection: three correlations to know", fontsize=11)
    save(fig, "HT-4-convection.png")


def fig_boiling(bc):
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    dT = np.linspace(2, bc["dT_chf"], 80)
    ax.loglog(dT, [bc["rohsenow"](d) / 1e6 for d in dT], color=BLUE, lw=2.6, label="nucleate boiling (Rohsenow)")
    ax.plot([bc["dT_chf"]], [bc["q_chf"] / 1e6], "o", color=RED, ms=8); ax.annotate("critical heat flux %.2f MW/m²\nat ΔT ≈ %.0f K (Zuber)" % (bc["q_chf"] / 1e6, bc["dT_chf"]), (bc["dT_chf"], bc["q_chf"] / 1e6), (3, 1.4), fontsize=9, arrowprops=dict(arrowstyle="->", color=GREY))
    dT2 = np.linspace(bc["dT_chf"], 1000, 40)
    ax.loglog(dT2, np.interp(np.log(dT2), np.log([bc["dT_chf"], 150, 1000]), [bc["q_chf"] / 1e6, 0.03, 0.9]), color=GREY, ls="--", label="transition and film boiling (sketch)")
    ax.axvspan(2, 5, color="#e2e8f0", alpha=.6); ax.text(2.2, 0.0015, "free\nconvection", fontsize=8.5)
    ax.set_xlabel("excess temperature ΔT_e = T_s − T_sat (K)"); ax.set_ylabel("heat flux (MW/m²)"); ax.set_ylim(1e-3, 3); ax.legend(fontsize=9, loc="lower right")
    ax.set_title("Water at 1 atm: pool boiling curve (nucleate branch computed; the dashed part is schematic)", fontsize=9.5)
    save(fig, "HT-5-boiling.png")


def fig_radiation(tp, e3):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    # shield effect: net flux vs number of shields (equal emissivity eps everywhere 0.8,0.6 ends; shield 0.1)
    n = np.arange(0, 7)
    e1, e2, es = 0.8, 0.6, 0.1
    q = [SIG * (500 ** 4 - 300 ** 4) / (1 / e1 + 1 / e2 - 1 + k * (2 / es - 1)) for k in n]
    a.bar(n, q, color=BLUE); [a.text(k, v + 25, "%.0f" % v, ha="center", fontsize=9) for k, v in zip(n, q)]
    a.set_xlabel("number of shields (ε = 0.1 both sides)"); a.set_ylabel("net flux between plates (W/m²)"); a.set_title("500 K and 300 K plates (ε = 0.8, 0.6): one shield cuts the flux %.0f %%" % (100 * tp["reduction"]), fontsize=9.5)
    # equilateral duct network
    b.set_aspect("equal"); b.axis("off")
    P = np.array([[0, 0], [1, 0], [.5, np.sqrt(3) / 2]])
    names = ["1: 600 K\nε = 0.8", "2: 400 K\nε = 0.5", "3: adiabatic\nT = %.0f K" % e3["T3"]]
    cols = [RED, BLUE, GREY]
    for i in range(3):
        j = (i + 1) % 3
        b.plot([P[i, 0], P[j, 0]], [P[i, 1], P[j, 1]], color=cols[[0, 2, 1][i]], lw=5)
    b.text(.5, -.1, "surface 1 (bottom)", ha="center", color=RED); b.text(.82, .5, "surface 2", color=BLUE, rotation=-60, ha="center"); b.text(.18, .5, "surface 3\n(re-radiating)", color=GREY, ha="center", rotation=60)
    b.text(.5, .28, "F₁₂ = F₁₃ = F₂₃ = 0.5\nq₁ = %.0f W/m² out\nq₂ = %.0f W/m² in\nT₃ = %.0f K" % (e3["q1"], -e3["q2"], e3["T3"]), ha="center", fontsize=9.5)
    b.set_title("long equilateral duct: radiosity solution", fontsize=9.5)
    fig.suptitle("Radiation exchange", fontsize=11)
    save(fig, "HT-6-radiation.png")


def fig_hx(h):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    N = np.linspace(0, 5, 200)
    for Cr, col in ((0.0, GREEN), (0.5, ORANGE), (1.0, RED)):
        a.plot(N, [h["eps_counter"](n, Cr) for n in N], color=col, lw=2.2, label="counterflow, Cr = %.1f" % Cr)
        if Cr > 0:
            a.plot(N, [h["eps_parallel"](n, Cr) for n in N], color=col, lw=1.4, ls="--")
    a.plot([h["NTU"]], [h["eps"]], "ko"); a.annotate("worked example\nNTU = %.2f, ε = %.2f, Cr = %.2f" % (h["NTU"], h["eps"], h["Cr"]), (h["NTU"], h["eps"]), (2.3, 0.28), fontsize=9, arrowprops=dict(arrowstyle="->", color=GREY))
    a.set_xlabel("NTU = UA/C_min"); a.set_ylabel("effectiveness ε"); a.legend(fontsize=8.5, loc="lower right"); a.set_ylim(0, 1.02); a.set_title("solid: counterflow; dashed: parallel flow", fontsize=9.5)
    x = np.linspace(0, 1, 100)
    Q = h["Q"]
    Th = h["Thi"] - (h["Thi"] - h["Tho"]) * x
    Tc_counter = h["Tco"] - (h["Tco"] - h["Tci"]) * x          # cold flows the other way
    b.plot(x, Th, color=RED, lw=2.4, label="hot oil 120 → 70 °C")
    b.plot(x, Tc_counter, color=BLUE, lw=2.4, label="water, counterflow (leaves at %.1f °C)" % h["Tco"])
    Tc_par = h["Tci"] + (h["Tco"] - h["Tci"]) * x
    b.plot(x, Tc_par, color=BLUE, lw=1.6, ls="--", label="water, parallel flow")
    b.set_xlabel("position along the exchanger (fraction)"); b.set_ylabel("temperature (°C)"); b.legend(fontsize=8.5); b.set_title("counterflow keeps ΔT up: LMTD %.1f vs %.1f K" % (h["lmtd_c"], h["lmtd_p"]), fontsize=9.5)
    fig.suptitle("Heat exchangers", fontsize=11)
    save(fig, "HT-7-exchangers.png")


if __name__ == "__main__":
    w, pp, f, lp = wall(), pipe_insulation(), fin(), lumped()
    print("--- wall"); print({k: (np.round(v, 4) if not isinstance(v, list) else [round(x, 4) for x in v]) for k, v in w.items() if k != "names"})
    print("--- pipe insulation", {k: round(v, 5) for k, v in pp.items() if k != "f"})
    print("--- fin", {k: (round(v, 5) if not isinstance(v, tuple) else v) for k, v in f.items()})
    print("--- lumped", {k: round(v, 5) for k, v in lp.items()})
    for Bi in (0.1, 1.0, 10.0):
        z, C = slab_one_term(Bi)
        Fo10 = log(C / 0.1) / z ** 2
        print(f"--- slab Bi={Bi}: zeta1={z:.4f} C1={C:.4f}  Fo for theta0=0.1 (one term): {Fo10:.3f}  exact at that Fo: {slab_exact(Bi, Fo10):.4f}")
    fp, pw, vp, bc = flat_plate_air(), pipe_water(), vertical_plate_air(), boiling_condensing()
    print("--- flat plate air", {k: (round(v, 5) if not isinstance(v, dict) else {a: round(b, 5) for a, b in v.items()}) for k, v in fp.items()})
    print("--- pipe water", {k: (round(v, 4) if not isinstance(v, dict) else {a: round(b, 5) for a, b in v.items()}) for k, v in pw.items()})
    print("--- vertical plate", {k: round(v, 5) for k, v in vp.items()})
    print("--- boiling/condensing", {k: (round(v, 5) if not callable(v) else "fn") for k, v in bc.items()})
    tp, e3, hx = two_plates(), enclosure3(), hx_example()
    print("--- two plates", {k: round(v, 4) for k, v in tp.items()})
    print("--- enclosure3", {k: (np.round(v, 3) if hasattr(v, "__len__") else round(v, 4)) for k, v in e3.items()})
    print("--- hx", {k: (round(v, 4) if not callable(v) else "fn") for k, v in hx.items()})
    fig_conduction(w, pp); fig_fins(f); fig_transient(); fig_convection(fp, vp); fig_boiling(bc); fig_radiation(tp, e3); fig_hx(hx)
