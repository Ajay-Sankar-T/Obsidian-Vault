"""Introduction to Machine Design (ME3203): numbers and figures for the concept notes.
   python md_core.py -> prints every quoted number, writes ../assets/MD-*.png"""
import os
from math import pi, sqrt, log, tan, radians, cos, sin
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ============================================================ shaft
def marin(Sut, d_mm, reliability=0.99, surface="machined"):
    a, b = {"machined": (4.51, -0.265), "ground": (1.58, -0.085), "hot rolled": (57.7, -0.718)}[surface]
    ka = a * Sut ** b
    kb = 1.24 * d_mm ** -0.107 if 2.79 <= d_mm <= 51 else 1.51 * d_mm ** -0.157
    kc = kd = 1.0
    ke = {0.5: 1.0, 0.9: 0.897, 0.95: 0.868, 0.99: 0.814, 0.999: 0.753}[reliability]
    return ka, kb, kc, kd, ke


def shaft():
    P, n_rpm, Dg, L = 15e3, 1000.0, 0.120, 0.300
    T = P / (n_rpm * 2 * pi / 60)
    Ft = T / (Dg / 2); Fr = Ft * tan(radians(20)); F = sqrt(Ft ** 2 + Fr ** 2)
    M = F * L / 4
    Sut, Sy = 630.0, 530.0
    Kf, Kfs, nsf = 1.6, 1.4, 2.0
    d = 35.0
    for _ in range(30):
        ka, kb, kc, kd, ke = marin(Sut, d)
        Se = ka * kb * kc * kd * ke * 0.5 * Sut
        dnew = ((16 * nsf / pi) * ((2 * Kf * M) / (Se * 1e6) + sqrt(3) * Kfs * T / (Sut * 1e6))) ** (1 / 3) * 1000
        if abs(dnew - d) < 1e-6:
            break
        d = dnew
    d_std = 36.0
    ka, kb, *_ = marin(Sut, d_std)
    Se_std = marin(Sut, d_std)[0] * marin(Sut, d_std)[1] * marin(Sut, d_std)[4] * 0.5 * Sut
    sa = 32 * Kf * M / (pi * (d_std / 1000) ** 3) / 1e6
    tm = 16 * Kfs * T / (pi * (d_std / 1000) ** 3) / 1e6
    sm_vm = sqrt(3) * tm
    n_f = 1 / (sa / Se_std + sm_vm / Sut)
    n_y = Sy / (sa + sm_vm)       # first-cycle yielding (conservative)
    n_y_vm = Sy / sqrt((sa) ** 2 + 3 * tm ** 2)
    return dict(T=T, Ft=Ft, Fr=Fr, F=F, M=M, Se=Se, ka=ka, kb=kb, d=d, d_std=d_std, Se_std=Se_std, sa=sa, tm=tm, sm_vm=sm_vm, n_f=n_f, n_y=n_y, n_y_vm=n_y_vm, Sut=Sut, Sy=Sy)


def fig_shaft(s):
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    Sut, Sy, Se = s["Sut"], s["Sy"], s["Se_std"]
    sm = np.linspace(0, Sut, 200)
    ax.plot(sm, Se * (1 - sm / Sut), color=BLUE, lw=2.6, label="Goodman line")
    ax.plot(sm, Se * (1 - (sm / Sut) ** 2), color=GREEN, lw=1.6, ls="--", label="Gerber parabola")
    ax.plot([0, Sy], [Sy, 0], color=RED, lw=1.8, ls="-.", label="yield (Langer) line")
    ax.fill_between(sm, 0, Se * (1 - sm / Sut), color=BLUE, alpha=.08)
    ax.plot([s["sm_vm"]], [s["sa"]], "o", color=ORANGE, ms=9); ax.annotate("design point\n(σ'm = %.0f, σ'a = %.0f MPa)" % (s["sm_vm"], s["sa"]), (s["sm_vm"], s["sa"]), (230, 175), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    k = s["n_f"]; ax.plot([s["sm_vm"] * k], [s["sa"] * k], "x", color=PURPLE, ms=9); ax.text(s["sm_vm"] * k + 12, s["sa"] * k + 8, "same load ×%.2f touches the line" % k, color=PURPLE, fontsize=8.5)
    ax.set_xlim(0, Sut * 1.03); ax.set_ylim(0, Sy * 1.05)
    ax.set_xlabel("mean stress σ'ₘ (MPa)"); ax.set_ylabel("alternating stress σ'ₐ (MPa)"); ax.legend(fontsize=9)
    ax.set_title("Ø36 shaft: Se = %.0f MPa, Sut = %.0f, Sy = %.0f: fatigue safe, n = %.2f" % (Se, Sut, Sy, s["n_f"]), fontsize=10)
    save(fig, "MD-1-shaft-goodman.png")


# ============================================================ keys and flange couplings
def key():
    d, T = 0.040, 143.2
    b, t = 0.012, 0.008
    Sy = 300e6
    Ssy = 0.577 * Sy
    n = 2.0
    F = T / (d / 2)
    L_shear = F * n / (b * Ssy)
    L_bear = 2 * F * n / (t * Sy)
    L_equal = pi * d / 2
    Lc = 0.040
    tau = F / (b * Lc); sig = 2 * F / (t * Lc)
    nb, Dp, tau_b = 4, 0.100, 40e6
    db = sqrt(8 * T / (pi * nb * tau_b * Dp))
    return dict(F=F, L_shear=L_shear, L_bear=L_bear, L_equal=L_equal, tau=tau, sig=sig, n_shear=Ssy / tau, n_bear=Sy / sig, db=db, Ssy=Ssy)


def fig_key(k):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    a.set_aspect("equal"); a.axis("off"); a.set_xlim(-30, 30); a.set_ylim(-28, 28)
    a.add_patch(Circle((0, 0), 20, fc="#e2e8f0", ec="k", lw=2))
    a.add_patch(Rectangle((-6, 14), 12, 8, fc=ORANGE, ec="k", lw=1.5, alpha=.9))
    a.add_patch(Circle((0, 0), 28, fill=False, ec=GREY, lw=1, ls="--"))
    a.annotate("", (-18, 0), (-18, 14), arrowprops=dict(arrowstyle="<->", color=RED)); a.text(-26, 6, "T", color=RED, fontsize=12)
    a.annotate("shear plane\n(area b·L)", (0, 18), (14, 25), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.annotate("bearing area\n(t/2)·L", (6, 17), (14, 9), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.text(0, -5, "Ø40", ha="center", fontsize=11); a.text(0, -25, "key 12 × 8: F = T/(d/2) = %.0f N" % k["F"], ha="center", fontsize=9)
    a.set_title("force on the key: shear across b·L, crushing on t/2·L", fontsize=9.5)
    L = np.linspace(5, 60, 100) / 1000
    b.plot(L * 1000, 143.2 / (0.020 * 0.012 * L) / 1e6 * 0 + (k["F"] / (0.012 * L)) / 1e6, color=BLUE, lw=2.4, label="shear stress τ = F/(bL)")
    b.plot(L * 1000, (2 * k["F"] / (0.008 * L)) / 1e6, color=ORANGE, lw=2.4, label="crushing σc = 2F/(tL)")
    b.axhline(k["Ssy"] / 2e6, color=BLUE, ls=":"); b.text(40, k["Ssy"] / 2e6 + 4, "Ssy/n = %.0f MPa" % (k["Ssy"] / 2e6), color=BLUE, fontsize=9)
    b.axhline(150, color=ORANGE, ls=":"); b.text(40, 154, "Sy/n = 150 MPa", color=ORANGE, fontsize=9)
    b.axvline(k["L_bear"] * 1000, color=GREY, ls="--"); b.text(k["L_bear"] * 1000 + .5, 250, "L ≥ %.1f mm\n(crushing governs)" % (k["L_bear"] * 1000), fontsize=9)
    b.set_ylim(0, 300); b.set_xlabel("key length L (mm)"); b.set_ylabel("stress (MPa)"); b.legend(fontsize=9); b.set_title("T = 143 N·m on a Ø40 shaft", fontsize=9.5)
    fig.suptitle("Keys", fontsize=11)
    save(fig, "MD-2-key.png")


# ============================================================ bearings
def bearings():
    C, Fr, n = 32e3, 4e3, 1000.0
    L10 = (C / Fr) ** 3
    L10h = L10 * 1e6 / (60 * n)
    a1 = {90: 1.0, 95: 0.64, 96: 0.55, 97: 0.47, 98: 0.37, 99: 0.25}
    Fr2 = 2 * Fr
    d, L, c, mu, N, W = 0.050, 0.050, 0.00005, 0.03, 1500 / 60, 2000.0
    Pm = W / (d * L)
    f = 2 * pi ** 2 * (mu * N / Pm) * (d / 2 / c)
    S = (d / 2 / c) ** 2 * (mu * N / Pm)
    Tq = f * W * d / 2
    pw = Tq * 2 * pi * N
    return dict(L10=L10, L10h=L10h, L10h_90=L10h * 1.0, L10h_99=L10h * 0.25, L10_double=(C / Fr2) ** 3, Pm=Pm, f=f, S=S, Tq=Tq, pw=pw)


def fig_bearings(b):
    fig, (a, c) = plt.subplots(1, 2, figsize=(11, 4.2))
    x = np.linspace(0.1, 1.0, 200)
    r = np.linspace(0.15, 1.2, 100)
    cp_ = np.linspace(1, 8, 200)
    a.semilogy(cp_, cp_ ** 3, color=BLUE, lw=2.4, label="ball bearing, p = 3"); a.semilogy(cp_, cp_ ** (10 / 3), color=GREEN, lw=2, ls="--", label="roller bearing, p = 10/3")
    a.set_xlim(1, 8); a.set_ylim(1, 1e4)
    a.axvline(8, color=GREY)
    a.set_xlabel("C / P (rating over equivalent load)"); a.set_ylabel("L10 (million revolutions)")
    a.plot([8], [512], "o", color=RED); a.annotate("C/P = 8: L10 = 512 Mrev\n= 8530 h at 1000 rpm", (8, 512), (3.3, 2500), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.legend(fontsize=9, loc="lower right"); a.set_title("double the load and the life falls 8 times", fontsize=9.5)
    z = np.logspace(-8, -4.5, 300)               # mu N / P  (dimensionless)
    cr = 500.0
    pet = 2 * pi ** 2 * z * cr
    c.loglog(z, pet, color=BLUE, lw=2.4, label="hydrodynamic (Petroff): f = 2π²(μN/P)(r/c)")
    c.loglog(z, 0.12 / (1 + (z / 2e-8) ** 1.2) + pet, color=ORANGE, lw=2, ls="--", label="with boundary and mixed lubrication (sketch)")
    z0 = b["S"] / cr ** 2
    c.plot([z0], [b["f"]], "o", color=RED, ms=8)
    c.annotate("example: f = %.4f, S = %.2f" % (b["f"], b["S"]), (z0, b["f"]), (3e-8, 0.35), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    c.set_xlabel("μN/P (dimensionless)"); c.set_ylabel("friction coefficient f"); c.legend(fontsize=8.5, loc="upper left"); c.set_ylim(3e-3, 1)
    c.set_title("Stribeck curve: friction is lowest in the full-film regime", fontsize=9.5)
    fig.suptitle("Bearings", fontsize=11)
    save(fig, "MD-3-bearings.png")


# ============================================================ spur gears
LEWIS = {12: .245, 13: .261, 14: .277, 15: .290, 16: .296, 17: .303, 18: .309, 19: .314, 20: .322, 21: .328, 22: .331, 24: .337, 26: .346, 28: .353, 30: .359, 34: .371, 38: .384, 43: .397, 50: .409, 60: .422, 75: .435, 100: .447, 150: .460, 300: .472, 400: .480}


def gears():
    N1, N2, m, bw, P, n = 20, 40, 4e-3, 40e-3, 7.5e3, 1450.0
    d1, d2 = N1 * m, N2 * m
    V = pi * d1 * n / 60
    Wt = P / V
    Kv = (6.1 + V) / 6.1
    Y1 = LEWIS[20]
    sig = Kv * Wt / (bw * m * Y1)
    phi = radians(20)
    rho1, rho2 = d1 / 2 * sin(phi), d2 / 2 * sin(phi)
    E, nu = 207e9, 0.3
    Fn = Wt / cos(phi)
    sH = sqrt(Fn / (pi * bw) * (1 / rho1 + 1 / rho2) / (2 * (1 - nu ** 2) / E))
    return dict(d1=d1, d2=d2, V=V, Wt=Wt, Kv=Kv, Y=Y1, sig=sig, Fn=Fn, rho1=rho1, rho2=rho2, sH=sH, T1=Wt * d1 / 2, a=(d1 + d2) / 2)


def fig_gears(g):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    N = np.array(sorted(LEWIS)); Y = np.array([LEWIS[k] for k in N])
    a.semilogx(N, Y, "o-", color=BLUE, lw=2); a.axhline(0.485, color=GREY, ls=":"); a.text(13, 0.488, "rack: 0.485", fontsize=9, color=GREY)
    a.plot([20], [LEWIS[20]], "o", color=RED, ms=9); a.annotate("N = 20: Y = 0.322", (20, .322), (40, .28), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("number of teeth N"); a.set_ylabel("Lewis form factor Y (20° full depth)"); a.set_title("fewer teeth, thinner root, weaker tooth", fontsize=9.5)
    V = np.linspace(0, 20, 100)
    b.plot(V, (6.1 + V) / 6.1, color=BLUE, lw=2.4, label="cut or milled gears: (6.1+V)/6.1")
    b.plot(V, (3.05 + V) / 3.05, color=ORANGE, lw=2, ls="--", label="cast gears: (3.05+V)/3.05")
    b.plot([g["V"]], [g["Kv"]], "o", color=RED, ms=8); b.annotate("V = %.1f m/s: Kv = %.2f" % (g["V"], g["Kv"]), (g["V"], g["Kv"]), (9, 1.3), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("pitch-line velocity V (m/s)"); b.set_ylabel("velocity factor Kv"); b.legend(fontsize=9); b.set_title("faster teeth meet harder: Kv multiplies the load", fontsize=9.5)
    fig.suptitle("Spur gear strength", fontsize=11)
    save(fig, "MD-4-gears.png")


# ============================================================ springs
def spring():
    d, D, Na, G, Fmax = 4e-3, 30e-3, 8.0, 79.3e9, 250.0
    C = D / d
    Kw = (4 * C - 1) / (4 * C - 4) + 0.615 / C
    tau = Kw * 8 * Fmax * D / (pi * d ** 3)
    k = G * d ** 4 / (8 * D ** 3 * Na)
    Sut = 2211 / (d * 1000) ** 0.145
    Ssy = 0.45 * Sut
    Ssu = 0.67 * Sut
    Fmin = 100.0
    Fa, Fm = (Fmax - Fmin) / 2, (Fmax + Fmin) / 2
    ta, tm = Kw * 8 * Fa * D / (pi * d ** 3), Kw * 8 * Fm * D / (pi * d ** 3)
    Ssa, Ssm = 241e6, 379e6
    Sse = Ssa / (1 - Ssm / Ssu / 1e6) if False else Ssa / (1 - (Ssm / (Ssu * 1e6)))
    nf = 1 / (ta / Sse + tm / (Ssu * 1e6))
    Lfree_solid = (Na + 2) * d
    return dict(C=C, Kw=Kw, tau=tau / 1e6, k=k, delta=Fmax / k, Sut=Sut, Ssy=Ssy, Ssu=Ssu, n_static=Ssy * 1e6 / tau, ta=ta / 1e6, tm=tm / 1e6, Sse=Sse / 1e6, nf=nf, solid=Lfree_solid)


def fig_spring(s):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    C = np.linspace(3, 14, 200)
    a.plot(C, (4 * C - 1) / (4 * C - 4) + 0.615 / C, color=BLUE, lw=2.4, label="Wahl factor Kw")
    a.plot(C, 1 + 0.5 / C, color=GREEN, lw=1.8, ls="--", label="direct-shear factor Ks = 1 + 0.5/C")
    a.plot([s["C"]], [s["Kw"]], "o", color=RED); a.annotate("C = 7.5: Kw = %.3f" % s["Kw"], (s["C"], s["Kw"]), (9, 1.45), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("spring index C = D/d"); a.set_ylabel("stress correction factor"); a.legend(fontsize=9); a.set_title("tight coils (small C) raise the inner-fibre shear stress", fontsize=9.5)
    x = np.linspace(0, 30, 50)
    k = s["k"] / 1000
    b.plot(x, k * x, color=BLUE, lw=2.4, label="one spring: k = %.1f N/mm" % k)
    b.plot(x, 2 * k * x, color=GREEN, lw=1.8, ls="--", label="two in parallel: 2k")
    b.plot(x, k / 2 * x, color=ORANGE, lw=1.8, ls="--", label="two in series: k/2")
    b.set_xlabel("deflection (mm)"); b.set_ylabel("force (N)"); b.legend(fontsize=9); b.set_title("springs combine like conductances", fontsize=9.5)
    fig.suptitle("Helical springs", fontsize=11)
    save(fig, "MD-5-springs.png")


# ============================================================ bolted joints
def bolt():
    d, At, E = 12.0, 84.3, 207e3         # mm, mm2, MPa
    Ad = pi * d ** 2 / 4
    ld, lt = 20.0, 20.0
    kb = Ad * At * E / (Ad * lt + At * ld)
    l = 40.0
    km = 0.5774 * pi * E * d / (2 * log(5 * (0.5774 * l + 0.5 * d) / (0.5774 * l + 2.5 * d)))
    C = kb / (kb + km)
    Sp, Sut, Se = 600.0, 800.0, 129.0
    Fi = 0.75 * Sp * At
    P = 15e3
    Fb = Fi + C * P
    Fm_ = Fi - (1 - C) * P
    n_p = Sp * At / Fb
    n_L = (Sp * At - Fi) / (C * P)
    n_0 = Fi / ((1 - C) * P)
    sa = C * P / (2 * At)
    si = Fi / At
    sm = sa + si
    n_f = Se * (Sut - si) / (Sut * sa + Se * (sm - si))
    return dict(kb=kb, km=km, C=C, Fi=Fi, Fb=Fb, Fm=Fm_, n_p=n_p, n_L=n_L, n_0=n_0, sa=sa, sm=sm, si=si, n_f=n_f, Sp=Sp, At=At, P=P, sep=Fi / (1 - C))


def fig_bolt(b):
    fig, (a, c) = plt.subplots(1, 2, figsize=(11, 4.4))
    kb, km, Fi, P, C = b["kb"] / 1e3, b["km"] / 1e3, b["Fi"] / 1e3, b["P"] / 1e3, b["C"]
    xb = np.linspace(0, 0.05, 50); xm = np.linspace(0, 0.0, 2)
    a.plot([0, Fi / kb], [0, Fi], color=BLUE, lw=2.4, label="bolt (soft spring)")
    a.plot([0, -Fi / km], [0, Fi], color=ORANGE, lw=2.4, label="members (stiff spring)")
    dxb = C * P / kb
    a.plot([Fi / kb, Fi / kb + dxb], [Fi, Fi + C * P], color=BLUE, lw=2.4, ls="--")
    a.plot([-Fi / km, -Fi / km + (1 - C) * P / km], [Fi, Fi - (1 - C) * P], color=ORANGE, lw=2.4, ls="--")
    a.annotate("", (Fi / kb + dxb, Fi + C * P), (Fi / kb + dxb, Fi), arrowprops=dict(arrowstyle="->", color=BLUE)); a.text(Fi / kb + dxb + 0.002, Fi + 1, "bolt gains\nC·P = %.1f kN" % (C * P), color=BLUE, fontsize=9)
    a.text(-0.0155, 12, "members lose\n(1−C)P = %.1f kN" % ((1 - C) * P), color=ORANGE, fontsize=9, ha="left")
    a.axhline(Fi, color=GREY, ls=":"); a.text(0.0005, Fi + 1, "preload Fi = %.1f kN" % Fi, fontsize=9, color=GREY)
    a.set_xlim(-0.022, 0.1); a.set_xlabel("elongation of bolt (right) / compression of members (left), mm"); a.set_ylabel("force (kN)"); a.legend(fontsize=9, loc="lower right"); a.set_title("joint diagram: external load P = 15 kN", fontsize=9.5)
    Pv = np.linspace(0, 60, 200)
    Fbv = b["Fi"] / 1e3 + C * Pv
    Fmv = np.maximum(b["Fi"] / 1e3 - (1 - C) * Pv, 0)
    c.plot(Pv, Fbv, color=BLUE, lw=2.4, label="bolt force"); c.plot(Pv, Fmv, color=ORANGE, lw=2.4, label="clamp force")
    c.axvline(b["sep"] / 1e3, color=RED, ls="--"); c.text(b["sep"] / 1e3 + .8, 8, "joint separates\nat P₀ = %.0f kN" % (b["sep"] / 1e3), color=RED, fontsize=9)
    c.axhline(b["Sp"] * b["At"] / 1e3, color=GREY, ls=":"); c.text(1, b["Sp"] * b["At"] / 1e3 + .6, "proof load Sp·At = %.1f kN" % (b["Sp"] * b["At"] / 1e3), fontsize=9, color=GREY)
    c.set_xlabel("external load per bolt P (kN)"); c.set_ylabel("force (kN)"); c.legend(fontsize=9, loc="center right"); c.set_title("a tight bolt barely feels the load until the joint opens", fontsize=9.5)
    fig.suptitle("Bolted joint M12 × 1.75, grade 8.8", fontsize=11)
    save(fig, "MD-6-bolt.png")


if __name__ == "__main__":
    s, k, b_, g, sp, bt = shaft(), key(), bearings(), gears(), spring(), bolt()
    for name, d in (("shaft", s), ("key", k), ("bearings", b_), ("gears", g), ("spring", sp), ("bolt", bt)):
        print("---", name)
        for kk, v in d.items():
            print(f"  {kk:10s} {v:.5g}" if isinstance(v, (int, float)) else f"  {kk:10s} {v}")
    fig_shaft(s); fig_key(k); fig_bearings(b_); fig_gears(g); fig_spring(sp); fig_bolt(bt)
