"""Materials and Design (ME2200): numbers and figures for the concept notes.
   python mat_core.py -> prints every quoted number, writes ../assets/MAT-*.png"""
import os
from math import pi, sqrt, log, log10, exp, cos, sin, radians, degrees, acos
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})
NA = 6.02214076e23


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ------------------------------------------------------------ crystals
def crystals():
    r = {}
    r["apf"] = dict(SC=pi / 6, BCC=pi * sqrt(3) / 8, FCC=pi / (3 * sqrt(2)), HCP=pi / (3 * sqrt(2)))
    rho = lambda n, A, a_nm: n * A * 1e-3 / (NA * (a_nm * 1e-9) ** 3) / 1e3        # g/cm3
    r["rho_Cu"] = rho(4, 63.55, 0.3615)
    r["rho_Fe"] = rho(2, 55.85, 0.2866)
    r["rho_Al"] = rho(4, 26.98, 0.4050)
    a = 1.0
    r["FCC_110_linear"] = 2 / (a * sqrt(2))     # atoms per length along [110]  (units 1/a)
    r["FCC_111_planar"] = 2 / (sqrt(3) * a ** 2 / 2 * 2 / 2 * 2) if False else 2 / (sqrt(3) / 2 * (sqrt(2) * a) ** 2 / 1 * 0.5 * 2) if False else 4 / (sqrt(3) * a ** 2)  # atoms per (111) triangle-based area, per a^2
    r["FCC_100_planar"] = 2 / a ** 2
    r["BCC_110_planar"] = 2 / (sqrt(2) * a ** 2)
    return r


def cube_edges(ax):
    for s, e in (((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (0, 1, 0)), ((0, 0, 0), (0, 0, 1)), ((1, 1, 1), (0, 1, 1)), ((1, 1, 1), (1, 0, 1)), ((1, 1, 1), (1, 1, 0)),
                 ((1, 0, 0), (1, 1, 0)), ((1, 0, 0), (1, 0, 1)), ((0, 1, 0), (1, 1, 0)), ((0, 1, 0), (0, 1, 1)), ((0, 0, 1), (1, 0, 1)), ((0, 0, 1), (0, 1, 1))):
        ax.plot(*zip(s, e), color="#555", lw=1)


def fig_crystals(c):
    fig = plt.figure(figsize=(12.5, 4.4))
    corners = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    face = [(.5, .5, 0), (.5, .5, 1), (.5, 0, .5), (.5, 1, .5), (0, .5, .5), (1, .5, .5)]
    for idx, (nm, extra, col) in enumerate((("Simple cubic: 1 atom, CN 6", [], GREY), ("BCC: 2 atoms, CN 8", [(.5, .5, .5)], ORANGE), ("FCC: 4 atoms, CN 12", face, BLUE))):
        ax = fig.add_subplot(1, 4, idx + 1, projection="3d"); cube_edges(ax)
        pts = np.array(corners)
        ax.scatter(*pts.T, s=120, color=GREY, edgecolor="k", depthshade=False)
        if extra:
            e = np.array(extra); ax.scatter(*e.T, s=120, color=col, edgecolor="k", depthshade=False)
        ax.set_axis_off(); ax.set_title(nm, fontsize=9.5)
    ax = fig.add_subplot(1, 4, 4)
    names = ["SC", "BCC", "FCC", "HCP"]; vals = [c["apf"][k] for k in names]
    ax.bar(names, vals, color=[GREY, ORANGE, BLUE, BLUE]); [ax.text(i, v + .01, "%.3f" % v, ha="center") for i, v in enumerate(vals)]
    ax.set_ylim(0, .85); ax.set_ylabel("atomic packing factor"); ax.set_title("how full the cell is", fontsize=9.5)
    fig.suptitle("Metallic crystal structures", fontsize=11)
    save(fig, "MAT-1-crystals.png")


# ------------------------------------------------------------ slip, Hall-Petch
def slip():
    r = {}
    r["schmid_sigma"] = 0.48 / (cos(radians(60)) * cos(radians(35)))
    hp = lambda d_um: 70 + 0.6 / sqrt(d_um * 1e-6)
    r["hp"] = {d: hp(d) for d in (100, 10, 1)}
    G, b = 48e9, 0.256e-9
    r["taylor"] = {rho: 0.5 * G * b * sqrt(rho) / 1e6 for rho in (1e12, 1e14, 1e15)}
    return r


def fig_slip(s):
    fig, (a, b, c) = plt.subplots(1, 3, figsize=(13, 4.2))
    phi = np.linspace(0, 90, 200)
    a.plot(phi, np.cos(np.radians(phi)) * np.cos(np.radians(90 - phi)), color=BLUE, lw=2.4, label="λ = 90° − φ")
    a.axhline(0.5, color=RED, ls="--"); a.text(5, .51, "maximum 0.5 at φ = λ = 45°", color=RED, fontsize=9)
    a.set_xlabel("angle φ between load axis and slip-plane normal (deg)"); a.set_ylabel("Schmid factor cosφ cosλ"); a.set_title("a crystal yields when τ_R = σ cosφ cosλ reaches the CRSS", fontsize=9.5)
    d = np.logspace(-0.3, 2.3, 100)
    b.loglog(d, 70 + 0.6 / np.sqrt(d * 1e-6), color=BLUE, lw=2.4)
    for dd, v in s["hp"].items():
        b.plot([dd], [v], "o", color=RED); b.text(dd * 1.1, v * 1.05, "%d µm: %.0f MPa" % (dd, v), fontsize=9)
    b.set_xlabel("grain size d (µm)"); b.set_ylabel("yield strength (MPa)"); b.set_title("Hall–Petch: σ_y = σ₀ + k d^(-1/2) (σ₀ = 70 MPa, k = 0.6 MPa√m)", fontsize=9.5)
    rho = np.logspace(10, 16, 100)
    c.loglog(rho, 0.5 * 48e9 * 0.256e-9 * np.sqrt(rho) / 1e6, color=GREEN, lw=2.4)
    for r_, v in s["taylor"].items():
        c.plot([r_], [v], "o", color=RED); c.text(r_ * 1.2, v * .8, "%.0f MPa" % v, fontsize=9)
    c.set_xlabel("dislocation density ρ (m⁻²)"); c.set_ylabel("Δσ = αGb√ρ (MPa)"); c.set_title("work hardening: more dislocations, more strength (copper, α = 0.5)", fontsize=9.5)
    fig.suptitle("Slip and strengthening", fontsize=11)
    save(fig, "MAT-2-slip.png")


# ------------------------------------------------------------ tensile test
def tensile():
    K, n = 900.0, 0.2
    r = dict(K=K, n=n)
    r["eps_neck"] = n
    r["sig_T_neck"] = K * n ** n
    r["UTS_eng"] = r["sig_T_neck"] / exp(n)
    r["e_neck"] = exp(n) - 1
    sy, E = 350.0, 200e3
    r["resilience"] = sy ** 2 / (2 * E)
    F, D, dd = 3000.0, 10.0, 4.0
    r["HB"] = 2 * F / (pi * D * (D - sqrt(D ** 2 - dd ** 2)))
    r["UTS_from_HB"] = 3.45 * r["HB"]
    r["HV"] = 1.8544 * 30 / 0.45 ** 2 if False else 1.8544 * 30 / (0.45 ** 2)
    return r


def fig_tensile(t):
    K, n, E, sy = t["K"], t["n"], 200e3, 350.0
    eps = np.linspace(0, 0.45, 500)
    sig_T = np.minimum(E * eps, K * eps ** n)          # elastic line until it meets the power law (yield about 233 MPa)
    Kp = K
    Kp_neck = K * n ** n
    e = np.exp(eps) - 1
    sig_E = sig_T / (1 + e)
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    ee = np.linspace(0, 0.6, 500)
    # engineering curve is only defined up to fracture; draw until e=0.5
    mask = e < 0.6
    a.plot(e[mask], sig_E[mask], color=BLUE, lw=2.4, label="engineering")
    a.plot(np.exp(eps[mask]) - 1, sig_T[mask], color=RED, lw=2, ls="--", label="true (up to fracture, assuming uniform)")
    ineck = int(np.argmax(sig_E))
    a.plot([e[ineck]], [sig_E[ineck]], "o", color=ORANGE, ms=8); a.annotate("UTS: necking starts\ne = %.3f, σ = %.0f MPa" % (e[ineck], sig_E[ineck]), (e[ineck], sig_E[ineck]), (0.3, 360), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("strain"); a.set_ylabel("stress (MPa)"); a.legend(fontsize=9, loc="lower right"); a.set_title("after necking the engineering stress falls while the true stress keeps rising", fontsize=9.5)
    # Considere construction: dsigma/deps vs sigma
    sig = np.linspace(0, 1300, 300)
    b.plot(eps, sig_T, color=RED, lw=2.4, label="σ_T = Kε^n")
    dsig = np.gradient(sig_T, eps)
    b.plot(eps, dsig, color=GREEN, lw=2.2, label="slope dσ_T/dε_T")
    b.axvline(n, color=GREY, ls=":"); b.plot([n], [Kp * n ** n], "o", color=ORANGE, ms=8); b.annotate("necking where slope = σ_T\nε = n = %.2f, σ_T = %.0f MPa" % (n, Kp_neck), (n, Kp_neck), (0.23, 200), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlim(0, 0.45); b.set_ylim(0, 1400); b.set_xlabel("true strain"); b.set_ylabel("MPa"); b.legend(fontsize=9); b.set_title("Considère criterion: neck when work hardening can no longer keep up", fontsize=9.5)
    fig.suptitle("Tensile test", fontsize=11)
    save(fig, "MAT-3-tensile.png")
    return Kp, Kp_neck


# ------------------------------------------------------------ static failure
def failure():
    sx, sy_, txy = 100.0, -60.0, 40.0
    Sy, Sut, Suc = 300.0, 200.0, 700.0
    avg, R = (sx + sy_) / 2, sqrt(((sx - sy_) / 2) ** 2 + txy ** 2)
    s1, s2 = avg + R, avg - R
    n_tresca = Sy / (s1 - s2)
    vm = sqrt(s1 ** 2 - s1 * s2 + s2 ** 2)
    n_vm = Sy / vm
    n_cm = 1 / (s1 / Sut - s2 / Suc)
    n_mns = min(Sut / s1, -Suc / s2)
    return dict(s1=s1, s2=s2, tau_max=R, n_tresca=n_tresca, vm=vm, n_vm=n_vm, n_cm=n_cm, n_mns=n_mns, Sy=Sy, Sut=Sut, Suc=Suc)


def fig_failure(f):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 5))
    Sy = f["Sy"]
    th = np.linspace(0, 2 * pi, 400)
    # von Mises ellipse (plane stress): s1^2 - s1 s2 + s2^2 = Sy^2
    # parametrise with rotated axes: u=(s1+s2)/sqrt2, v=(s1-s2)/sqrt2 ; u^2/ (2 Sy^2) ... use polar solve
    s1v = []; s2v = []
    for t in th:
        c, s = cos(t), sin(t)
        k = Sy / sqrt(c * c - c * s + s * s)
        s1v.append(k * c); s2v.append(k * s)
    a.plot(s1v, s2v, color=BLUE, lw=2.4, label="von Mises")
    hexa = [(Sy, Sy), (0, Sy), (-Sy, 0), (-Sy, -Sy), (0, -Sy), (Sy, 0), (Sy, Sy)]
    a.plot(*zip(*hexa), color=GREEN, lw=2.2, ls="--", label="Tresca (max shear)")
    a.plot([f["s1"]], [f["s2"]], "o", color=ORANGE, ms=9); a.annotate("σ₁ = %.0f, σ₂ = %.0f MPa" % (f["s1"], f["s2"]), (f["s1"], f["s2"]), (110, -240), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.axhline(0, color="k", lw=.7); a.axvline(0, color="k", lw=.7)
    a.set_aspect("equal"); a.set_xlim(-400, 400); a.set_ylim(-400, 400); a.set_xlabel("σ₁ (MPa)"); a.set_ylabel("σ₂ (MPa)"); a.legend(fontsize=9, loc="upper left"); a.set_title("ductile: yield loci (Sy = 300 MPa), plane stress", fontsize=9.5)
    Sut, Suc = f["Sut"], f["Suc"]
    sq = [(Sut, Sut), (-Suc, Sut), (-Suc, -Suc), (Sut, -Suc), (Sut, Sut)]
    b.plot(*zip(*sq), color=GREEN, lw=2.2, ls="--", label="maximum normal stress")
    cm = [(Sut, 0), (0, Sut), (-Suc, Sut), (-Suc, 0), (0, -Suc), (Sut, -Suc), (Sut, 0)]
    cm = [(Sut, 0), (Sut, Sut * 0 + 0)]
    pts = [(0, Sut), (Sut, 0), (Sut, -Suc * 0 - 0)]
    cmL = [(Sut, 0), (0, -Suc), (-Suc, -Suc), (-Suc, 0), (0, Sut), (Sut, Sut)]
    # Coulomb-Mohr (plane stress): quadrant I square-ish corner, quadrants II/IV straight lines joining Sut and -Suc
    cmloc = [(Sut, Sut), (Sut, 0), (0, -Suc), (-Suc, -Suc), (-Suc, 0), (0, Sut), (Sut, Sut)]
    b.plot(*zip(*cmloc), color=BLUE, lw=2.4, label="Coulomb–Mohr")
    b.plot([f["s1"]], [f["s2"]], "o", color=ORANGE, ms=9)
    b.axhline(0, color="k", lw=.7); b.axvline(0, color="k", lw=.7)
    b.set_xlim(-800, 300); b.set_ylim(-800, 300); b.set_aspect("equal"); b.set_xlabel("σ₁ (MPa)"); b.set_ylabel("σ₂ (MPa)"); b.legend(fontsize=9, loc="lower left"); b.set_title("brittle (cast iron S_ut = 200, S_uc = 700 MPa)", fontsize=9.5)
    fig.suptitle("Static failure theories: the safe region is inside the curve", fontsize=11)
    save(fig, "MAT-4-failure.png")


# ------------------------------------------------------------ fracture
def fracture():
    Y = 1.12
    out = dict(Y=Y)
    sig, a = 300.0, 2e-3
    out["K"] = Y * sig * sqrt(pi * a)
    out["ac_Al7075"] = (24 / (Y * sig)) ** 2 / pi
    out["ac_4340"] = (50 / (Y * sig)) ** 2 / pi
    out["sigma_f_glass"] = sqrt(2 * 70e9 * 1.0 / (pi * 1e-6)) / 1e6
    out["B_min_4340"] = 2.5 * (50 / 1500) ** 2
    out["B_min_Al"] = 2.5 * (24 / 500) ** 2
    out["sig_f_Al_2mm"] = 24 / (Y * sqrt(pi * a))
    out["sig_f_4340_2mm"] = 50 / (Y * sqrt(pi * a))
    return out


def fig_fracture(f):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    aa = np.logspace(-4.5, -1, 200)
    for sig, col in ((100, GREEN), (200, BLUE), (300, ORANGE)):
        a.loglog(aa * 1000, 1.12 * sig * np.sqrt(pi * aa), color=col, lw=2, label="σ = %d MPa" % sig)
    for Kc, nm, col in ((24, "Al 7075-T6, K_Ic = 24", PURPLE), (50, "4340 steel, K_Ic = 50", RED)):
        a.axhline(Kc, color=col, ls="--"); a.text(0.04, Kc * 1.04, nm, color=col, fontsize=9)
    a.set_xlabel("crack length a (mm)"); a.set_ylabel("K_I = Yσ√(πa) (MPa√m)"); a.legend(fontsize=9, loc="lower right"); a.set_ylim(1, 300); a.set_title("a crack grows unstable when K_I reaches K_Ic", fontsize=9.5)
    s = np.logspace(1.5, 3.2, 200)
    for Kc, nm, col in ((24, "Al 7075-T6", PURPLE), (50, "4340 steel", RED), (4, "alumina", GREY), (0.7, "glass", GREEN)):
        b.loglog(s, (Kc / (1.12 * s)) ** 2 / pi * 1000, color=col, lw=2, label=nm)
    b.set_xlabel("stress σ (MPa)"); b.set_ylabel("critical crack length a_c (mm)"); b.legend(fontsize=9); b.set_title("tougher material, longer tolerable crack", fontsize=9.5)
    fig.suptitle("Fracture mechanics", fontsize=11)
    save(fig, "MAT-5-fracture.png")


# ------------------------------------------------------------ fatigue
def fatigue():
    Sut, f = 800.0, 0.9
    ka = 4.51 * Sut ** -0.265
    kb, ke = 0.85, 0.814
    Se = ka * kb * ke * 0.5 * Sut
    a_ = (f * Sut) ** 2 / Se
    b_ = -log10(f * Sut / Se) / 3
    N_at = lambda s: (s / a_) ** (1 / b_)
    sa, sm = 150.0, 100.0
    n_g = 1 / (sa / Se + sm / Sut)
    n_ger = 0.5 * (Sut / sm) ** 2 * (sa / Se) * (-1 + sqrt(1 + (2 * sm * Se / (Sut * sa)) ** 2))
    sar = sa / (1 - sm / Sut)
    return dict(ka=ka, Se=Se, a=a_, b=b_, N300=N_at(300.0), n_goodman=n_g, n_gerber=n_ger, sar=sar, N_sar=N_at(sar), N_at=N_at, Sut=Sut, f=f)


def fig_fatigue(f):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    N = np.logspace(3, 7, 200)
    S = np.where(N < 1e6, f["a"] * N ** f["b"], f["Se"])
    a.loglog(N, S, color=BLUE, lw=2.6)
    a.axhline(f["Se"], color=GREEN, ls=":"); a.text(2e3, f["Se"] * .93, "Se = %.0f MPa" % f["Se"], color=GREEN, fontsize=9)
    a.axhline(0.9 * f["Sut"], color=GREY, ls=":"); a.text(2e3, 0.9 * f["Sut"] * 1.02, "0.9 S_ut at 10³ cycles", color=GREY, fontsize=9)
    a.plot([f["N300"]], [300], "o", color=ORANGE); a.annotate("σ_a = 300 MPa: N = %.1e" % f["N300"], (f["N300"], 300), (2e5, 500), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("cycles to failure N"); a.set_ylabel("stress amplitude (MPa)"); a.set_ylim(100, 900); a.set_title("S–N line for S_ut = 800 MPa after Marin factors", fontsize=9.5)
    Sut, Se = f["Sut"], f["Se"]
    sm = np.linspace(0, Sut, 200)
    b.plot(sm, Se * (1 - sm / Sut), color=BLUE, lw=2.4, label="Goodman")
    b.plot(sm, Se * (1 - (sm / Sut) ** 2), color=GREEN, lw=1.8, ls="--", label="Gerber")
    b.plot([0, 640], [640, 0], color=RED, ls="-.", label="Soderberg-like yield line (Sy = 640)")
    b.plot([100], [150], "o", color=ORANGE, ms=9); b.annotate("σ_a = 150, σ_m = 100\nGoodman n = %.2f" % f["n_goodman"], (100, 150), (250, 150), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.fill_between(sm, 0, Se * (1 - sm / Sut), color=BLUE, alpha=.08)
    b.set_xlim(0, 850); b.set_ylim(0, 300); b.set_xlabel("mean stress σ_m (MPa)"); b.set_ylabel("alternating stress σ_a (MPa)"); b.legend(fontsize=9); b.set_title("modified Goodman diagram", fontsize=9.5)
    fig.suptitle("Fatigue: stress-life", fontsize=11)
    save(fig, "MAT-6-fatigue.png")


# ------------------------------------------------------------ Paris
def paris():
    C, m, Y, dsig, ai, Kc = 1e-11, 3.0, 1.12, 200.0, 0.5e-3, 50.0
    ac = (Kc / (Y * dsig)) ** 2 / pi
    p = 1 - m / 2
    Nf = (ac ** p - ai ** p) / (C * Y ** m * dsig ** m * pi ** (m / 2) * p)
    # numerical integration check
    a = ai; N = 0.0
    da = 1e-6
    while a < ac:
        dK = Y * dsig * sqrt(pi * a)
        N += da / (C * dK ** m)
        a += da
    N5 = None
    ai2 = 1e-3
    Nf2 = (ac ** p - ai2 ** p) / (C * Y ** m * dsig ** m * pi ** (m / 2) * p)
    return dict(ac=ac, Nf=Nf, Nnum=N, Nf_ai1mm=Nf2, dK_i=Y * dsig * sqrt(pi * ai), dK_c=Y * dsig * sqrt(pi * ac), C=C, m=m, Y=Y, dsig=dsig, ai=ai, Kc=Kc)


def fig_paris(p):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    dK = np.logspace(0.4, 1.7, 100)
    a.loglog(dK, p["C"] * dK ** 3, color=BLUE, lw=2.6, label="region II: da/dN = C ΔK^m")
    dK1 = np.logspace(0.4, 0.85, 20); a.loglog(dK1, p["C"] * dK1 ** 3 * (1 - (6.5 / dK1) ** 3 * 0) * np.exp(-((dK1 - 7) / 1.5) ** 2 * 0), color=BLUE, lw=0)
    a.axvline(6, color=GREY, ls=":"); a.text(2.7, 5e-9, "threshold\nΔK_th (I)", fontsize=9, color=GREY)
    a.axvline(40, color=RED, ls=":"); a.text(41, 2e-7, "K_max → K_Ic\n(III)", fontsize=9, color=RED)
    a.set_xlabel("ΔK (MPa√m)"); a.set_ylabel("crack growth per cycle da/dN (m/cycle)"); a.legend(fontsize=9, loc="upper left"); a.set_title("three regimes; the straight region is the Paris law", fontsize=9.5)
    aa = np.linspace(p["ai"], p["ac"], 400); p_ = 1 - p["m"] / 2
    Nn = (aa ** p_ - p["ai"] ** p_) / (p["C"] * p["Y"] ** 3 * p["dsig"] ** 3 * pi ** 1.5 * p_)
    b.plot(Nn / 1e3, aa * 1000, color=BLUE, lw=2.6)
    b.plot([p["Nf"] / 1e3], [p["ac"] * 1000], "o", color=RED); b.annotate("fracture at a_c = %.1f mm\nafter %.0f 000 cycles" % (p["ac"] * 1000, p["Nf"] / 1e3), (p["Nf"] / 1e3, p["ac"] * 1000), (p["Nf"] / 2e3, 6), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("cycles N (thousands)"); b.set_ylabel("crack length a (mm)"); b.set_title("Δσ = 200 MPa, a_i = 0.5 mm: slow, then fast", fontsize=9.5)
    fig.suptitle("Fatigue crack growth", fontsize=11)
    save(fig, "MAT-7-paris.png")


# ------------------------------------------------------------ phase diagrams
def phases():
    r = {}
    r["Wa_PbSn"] = (99 - 40) / (99 - 11)
    r["Wb_PbSn"] = 1 - r["Wa_PbSn"]
    Ceu, Calpha, Cbeta = 61.9, 19.2, 97.5
    r["eutectic_hypo_30"] = dict(proeut=(Ceu - 30) / (Ceu - Calpha), eut=(30 - Calpha) / (Ceu - Calpha))
    r["alpha_in_eut"] = (Cbeta - Ceu) / (Cbeta - Calpha)
    r["fe_04"] = dict(proeut_ferrite=(0.76 - 0.40) / (0.76 - 0.022), pearlite=(0.40 - 0.022) / (0.76 - 0.022), cementite_total=(0.40 - 0.022) / (6.70 - 0.022))
    r["fe_10"] = dict(proeut_cementite=(1.0 - 0.76) / (6.70 - 0.76), pearlite=(6.70 - 1.0) / (6.70 - 0.76))
    r["pearlite_cementite"] = (0.76 - 0.022) / (6.70 - 0.022)
    return r


def fig_phases(p):
    fig, (a, b) = plt.subplots(1, 2, figsize=(12.5, 5))
    # Pb-Sn
    liq1 = [(0, 327), (61.9, 183)]; liq2 = [(100, 232), (61.9, 183)]
    sol_a = [(0, 327), (19.2, 183)]; sol_b = [(100, 232), (97.5, 183)]
    solv_a = [(19.2, 183), (11, 150), (6, 100), (2, 20)]; solv_b = [(97.5, 183), (99, 150), (99.5, 100), (100, 20)]
    for ln in (liq1, liq2, sol_a, sol_b, solv_a, solv_b):
        a.plot(*zip(*ln), color=BLUE, lw=2.2)
    a.plot([19.2, 97.5], [183, 183], color=RED, lw=2.2)
    a.text(30, 270, "L", fontsize=14); a.text(5, 150, "α", fontsize=14); a.text(88, 100, "β", fontsize=14); a.text(30, 100, "α + β", fontsize=12); a.text(55, 215, "α + L", fontsize=9, rotation=-25); a.text(80, 220, "β + L", fontsize=9)
    a.plot([61.9], [183], "o", color=RED); a.annotate("eutectic 61.9 wt% Sn, 183 °C", (61.9, 183), (35, 20), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.plot([11, 40, 99], [150, 150, 150], "o--", color=ORANGE); a.text(40, 155, "40 wt%% Sn at 150 °C:\nWα = %.2f, Wβ = %.2f" % (p["Wa_PbSn"], p["Wb_PbSn"]), fontsize=8.5, color=ORANGE)
    a.set_xlim(0, 100); a.set_ylim(0, 340); a.set_xlabel("wt% Sn"); a.set_ylabel("temperature (°C)"); a.set_title("Pb–Sn: simple eutectic system", fontsize=10)
    # Fe-Fe3C (simplified, no delta/peritectic region)
    lines = {"liquidus AC": [(0, 1538), (4.30, 1147)], "liquidus CD": [(4.30, 1147), (6.67, 1227)], "solidus AE": [(0, 1538), (2.14, 1147)], "eutectic": [(2.14, 1147), (6.67, 1147)],
             "A3 GS": [(0, 912), (0.76, 727)], "Acm SE": [(0.76, 727), (2.14, 1147)], "GP": [(0, 912), (0.022, 727)], "eutectoid": [(0.022, 727), (6.67, 727)], "solvus ferrite": [(0.022, 727), (0.0, 400)],
             "cementite": [(6.67, 0), (6.67, 1227)]}
    for nm, ln in lines.items():
        b.plot(*zip(*ln), color=BLUE if nm not in ("eutectic", "eutectoid") else RED, lw=2.2)
    b.text(1.5, 1400, "L", fontsize=13); b.text(0.9, 1000, "γ (austenite)", fontsize=10); b.text(0.15, 800, "α+γ", fontsize=8, rotation=0); b.text(0.02, 500, "α (ferrite)", fontsize=9, rotation=90)
    b.text(1.3, 600, "α + Fe₃C", fontsize=10); b.text(3.0, 900, "γ + Fe₃C", fontsize=10); b.text(4.2, 1250, "L + Fe₃C", fontsize=9)
    for x, y, t in ((0.76, 727, "eutectoid\n0.76 wt% C, 727 °C"), (4.30, 1147, "eutectic\n4.30 wt% C, 1147 °C")):
        b.plot([x], [y], "o", color=RED); b.annotate(t, (x, y), (x + .3, y - 330), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREY))
    b.set_xlim(0, 6.9); b.set_ylim(300, 1600); b.set_xlabel("wt% C"); b.set_ylabel("temperature (°C)"); b.set_title("Fe–Fe₃C (simplified: peritectic corner omitted)", fontsize=10)
    fig.suptitle("Binary phase diagrams", fontsize=11)
    save(fig, "MAT-8-phases.png")


# ------------------------------------------------------------ TTT
def ttt_curves():
    T = np.linspace(230, 720, 200)
    # schematic C-curve for a eutectoid steel: nose near 540 C at about 1 s (start) and 10 s (finish)
    def start(T):
        return 10 ** (0.0 + 3.0 * ((np.maximum(T, 1) - 540) / 180) ** 2 * (T > 540) + 1.6 * ((540 - T) / 300) ** 2 * (T <= 540))
    t_s = start(T); t_f = t_s * 10 ** (1.0 + 0.8 * (T > 540) * (T - 540) / 180)
    return T, t_s, t_f


def fig_ttt():
    T, ts, tf = ttt_curves()
    fig, ax = plt.subplots(figsize=(8.2, 5.4))
    ax.set_xscale("log")
    ax.plot(ts, T, color=BLUE, lw=2.4); ax.plot(tf, T, color=BLUE, lw=2.4, ls="--")
    ax.axhline(727, color=RED); ax.text(0.15, 735, "A₁ = 727 °C", color=RED, fontsize=9)
    ax.axhline(220, color=GREEN); ax.text(0.15, 226, "Ms ≈ 220 °C (martensite starts)", color=GREEN, fontsize=9)
    ax.axhline(130, color=GREEN, ls=":"); ax.text(0.15, 136, "M50 ≈ 130 °C", color=GREEN, fontsize=8)
    ax.text(1e4, 630, "coarse pearlite", fontsize=9); ax.text(25, 610, "fine pearlite", fontsize=9, ha="center"); ax.text(30, 430, "upper bainite", fontsize=9); ax.text(80, 255, "lower bainite", fontsize=9)
    ax.text(0.15, 90, "martensite (+ retained austenite)", fontsize=9); ax.text(1.5, 765, "austenite", fontsize=10)
    paths = {"quench": ([0.2, 0.2], [800, 20], RED), "austemper": ([0.2, 0.3, 1e4], [800, 330, 330], ORANGE), "isothermal anneal": ([0.2, 0.4, 3e4], [800, 680, 680], PURPLE)}
    for nm, (x, y, c) in paths.items():
        ax.plot(x, y, color=c, lw=1.6)
    ax.annotate("quench → martensite", (0.2, 40), (1.5, 40), color=RED, fontsize=9, arrowprops=dict(arrowstyle="->", color=RED))
    ax.annotate("austemper: hold 330 °C → bainite", (3e2, 330), (1.2e3, 345), color=ORANGE, fontsize=9)
    ax.annotate("isothermal anneal 680 °C → coarse pearlite", (3e3, 680), (4e2, 748), color=PURPLE, fontsize=9)
    ax.set_xlim(0.1, 1e6); ax.set_ylim(0, 800); ax.set_xlabel("time (s), log scale"); ax.set_ylabel("temperature (°C)")
    ax.set_title("Schematic TTT diagram, eutectoid steel (0.77 wt% C): solid = start, dashed = finish", fontsize=9.5)
    save(fig, "MAT-9-ttt.png")


if __name__ == "__main__":
    c = crystals(); print("--- crystals", {k: (v if not isinstance(v, dict) else {a: round(b, 4) for a, b in v.items()}) for k, v in c.items()})
    s = slip(); print("--- slip", s)
    t = tensile(); print("--- tensile", t)
    f = failure(); print("--- failure", f)
    fr = fracture(); print("--- fracture", fr)
    fa = fatigue(); print("--- fatigue", {k: v for k, v in fa.items() if k != "N_at"})
    pa = paris(); print("--- paris", pa)
    ph = phases(); print("--- phases", ph)
    fig_crystals(c); fig_slip(s); print("--- Kp", fig_tensile(t)); fig_failure(f); fig_fracture(fr); fig_fatigue(fa); fig_paris(pa); fig_phases(ph); fig_ttt()
