"""AM2540 lab figures (beam deflection, buckling, tensile, torsion). Output: ../assets/AML-*.png
All specimen sizes below are ILLUSTRATIVE (the manuals tell you to measure your own); they only make the plots and sample calculations concrete."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets")); os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, GREEN, RED, PURPLE, GREY, TEAL = "#2b6cb0", "#dd6b20", "#2f855a", "#c53030", "#6b46c1", "#718096", "#2c7a7b"
plt.rcParams.update({"figure.dpi": 150, "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": "#e2e8f0",
                     "axes.axisbelow": True, "legend.frameon": False, "axes.prop_cycle": matplotlib.cycler(color=[BLUE, ORANGE, GREEN, RED, PURPLE, TEAL])})
g = 9.81


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, "AML-%s.png" % name), bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote AML-%s.png" % name)


def beam_defl(P, a, L, E, I, x):
    """simply supported beam, point load P at distance a from the left support; deflection at x (positive down)"""
    b = L - a; y = np.empty_like(x)
    left = x <= a
    y[left] = P * b * x[left] * (L ** 2 - b ** 2 - x[left] ** 2) / (6 * L * E * I)
    xr = x[~left]
    y[~left] = P * b * xr * (L ** 2 - b ** 2 - xr ** 2) / (6 * L * E * I) + P * (xr - a) ** 3 / (6 * E * I)
    return y


def beam_figs():
    L, bw, t = 400.0, 25.0, 6.0; I = bw * t ** 3 / 12
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9))
    x = np.linspace(0, L, 400); E = 70e3
    for aa, c, lab in ((L / 2, BLUE, "load at L/2"), (L / 4, ORANGE, "load at L/4"), (3 * L / 4, GREEN, "load at 3L/4")):
        y = beam_defl(24.5, aa, L, E, I, x); a.plot(x, y, color=c, lw=2.4, label=lab); a.plot([aa], [beam_defl(24.5, aa, L, E, I, np.array([aa]))[0]], "o", color=c)
    a.invert_yaxis(); a.set_xlabel("position x along the span (mm)"); a.set_ylabel("deflection (mm, down)"); a.legend(fontsize=8.5); a.set_title("Deflected shape, aluminium, P = 24.5 N")
    Ps = np.linspace(0, 24.5, 6)
    for Em, c, lab in ((70e3, BLUE, "aluminium  E = 70 GPa"), (210e3, ORANGE, "mild steel  E = 210 GPa")):
        d = Ps * L ** 3 / (48 * Em * I); b.plot(Ps / g * 1000, d, "o-", color=c, lw=2.2, label=lab)
    b.set_xlabel("hanger load (g)"); b.set_ylabel("midspan deflection (mm)"); b.legend(fontsize=8.5); b.set_title("Midspan deflection: slope L³/(48EI)")
    save(fig, "beam-deflection")
    k_al = 48 * 70e3 * I / L ** 3; k_st = 48 * 210e3 * I / L ** 3
    print("beam: I =", I, "mm^4; midspan stiffness Al, steel (N/mm):", round(k_al, 2), round(k_st, 2), " delta at 24.5 N:", round(24.5 / k_al, 3), round(24.5 / k_st, 3))
    print("beam: peak of off-centre (a=L/4) deflection location x/L ~", round(x[np.argmax(beam_defl(24.5, L / 4, L, 70e3, I, x))] / L, 3), "(theory sqrt((L^2-b^2)/3)/L =", round(np.sqrt((1 - .75 ** 2) / 3), 3), ")")


def buckling_fig():
    d, bb, E = 3.0, 25.0, 210e3; Imin = bb * d ** 3 / 12; A = bb * d; sy = 250.0
    L = np.linspace(80, 600, 300)
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    for K, c, lab in ((1.0, BLUE, "pinned-pinned  (Le = L)"), (1 / np.sqrt(2), GREEN, "pinned-fixed  (Le = L/√2)"), (0.5, ORANGE, "fixed-fixed  (Le = L/2)")):
        P = np.pi ** 2 * E * Imin / (K * L) ** 2; ax.plot(L, np.minimum(P, sy * A), color=c, lw=2.4, label=lab)
    ax.axhline(sy * A, color=RED, ls="--", lw=1.4); ax.text(110, sy * A + 300, "yield load σ_y·A: short struts squash instead of buckling", color=RED, fontsize=8.5)
    ax.set_ylim(0, 22000); ax.set_xlabel("strut length L (mm)"); ax.set_ylabel("critical load (N)"); ax.legend(fontsize=9, loc="upper right", bbox_to_anchor=(1, .8))
    ax.set_title("Euler load, 25 × 3 mm steel strip (weak axis, I = b d³/12)")
    save(fig, "buckling-vs-length")
    print("buckling: Imin =", Imin, "mm^4;  Pcr(L=400) pinned-pinned, pinned-fixed:", round(np.pi ** 2 * E * Imin / 400 ** 2, 1), round(np.pi ** 2 * E * Imin / (400 / np.sqrt(2)) ** 2, 1),
          " ratio:", round(2, 3), " crossover L pinned-pinned where Pcr=sigma_y A:", round(np.sqrt(np.pi ** 2 * E * Imin / (sy * A)), 1), "mm")


def tensile_fig():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.1), gridspec_kw={"width_ratios": [1.25, 1]})
    E = 210e3; sy, uts = 250.0, 400.0
    e1 = np.linspace(0, sy / E, 40); e2 = np.linspace(sy / E, 0.02, 40); e3 = np.linspace(0.02, 0.16, 120); e4 = np.linspace(0.16, 0.26, 60)
    s1 = E * e1; s2 = np.full_like(e2, sy); s3 = sy + (uts - sy) * (1 - np.exp(-(e3 - 0.02) / 0.04)) / (1 - np.exp(-0.14 / 0.04)); s4 = uts - (uts - 300) * ((e4 - 0.16) / 0.10) ** 1.5
    e = np.concatenate([e1, e2, e3, e4]); s = np.concatenate([s1, s2, s3, s4]); a.plot(e, s, color=BLUE, lw=2.6, label="engineering stress–strain")
    et = np.log(1 + e); st = s * (1 + e); m = e <= 0.16; a.plot(np.log(1 + e[m]), (s * (1 + e))[m], color=ORANGE, lw=2.4, ls="--", label="true stress–strain (valid to necking)")
    pass; 
    a.plot([sy / E], [sy], "o", color=RED); a.annotate("yield (σ_y)", (sy / E, sy), (0.03, 130), arrowprops=dict(arrowstyle="->", color=RED), fontsize=8.5, color=RED)
    a.plot([0.16], [uts], "o", color=RED); a.annotate("UTS: highest engineering\nstress; necking starts", (0.16, uts), (0.005, 505), arrowprops=dict(arrowstyle="->", color=RED), fontsize=8.5, color=RED)
    a.plot([0.26], [300], "x", color=RED, ms=9); a.annotate("fracture", (0.26, 300), (0.20, 345), arrowprops=dict(arrowstyle="->", color=RED), fontsize=8.5, color=RED)
    a.set_xlabel("strain (mm/mm)"); a.set_ylabel("stress (MPa)"); a.legend(fontsize=8, loc="upper right"); a.set_xlim(0, .3); a.set_ylim(0, 560)
    a.set_title("Mild steel (schematic): what to read from the curve")
    ins = a.inset_axes([0.42, 0.10, 0.5, 0.36]); ins.plot([0, sy / E], [0, sy], color=BLUE, lw=2.2); ins.plot([sy / E, 0.006], [sy, sy], color=BLUE, lw=2.2)
    ins.plot([0.002, 0.002 + 250 / E], [0, 250], color=GREEN, lw=1.8); ins.set_xlim(0, 0.006); ins.set_ylim(0, 300); ins.set_title("zoom on the elastic region", fontsize=8)
    ins.text(0.0022, 40, "0.2% offset line", color=GREEN, fontsize=7.5); ins.text(0.0001, 200, "slope E", color=BLUE, fontsize=7.5); ins.tick_params(labelsize=7)
    for E_, sy_, uts_, ef, c, lab in ((210e3, 250, 400, .25, BLUE, "mild steel"), (70e3, 190, 280, .12, GREEN, "aluminium alloy"), (3.0e3, 45, 55, .5, ORANGE, "PVC")):
        ey = sy_ / E_; ee = np.linspace(0, ef, 500); u = np.clip((ee - ey) / (0.6 * ef - ey), 0, 1)
        s_ = np.where(ee < ey, E_ * ee, sy_ + (uts_ - sy_) * np.sin(np.pi / 2 * u)); s_ = np.where(ee > 0.6 * ef, uts_ - (uts_ - 0.8 * uts_) * ((ee - 0.6 * ef) / (0.4 * ef)) ** 2, s_)
        b.plot(ee, s_, color=c, lw=2.3, label=lab); b.plot([ef], [s_[-1]], "x", color=c, ms=8)
    b.set_xlim(0, .55); b.set_ylim(0, 450); b.set_xlabel("strain"); b.set_ylabel("stress (MPa)"); b.legend(fontsize=8.5); b.set_title("ES6 kit materials (schematic)")
    save(fig, "tensile-curves")
    print("tensile: 0.2% offset yield for E=210 GPa elastic-perfectly-plastic: sigma_y =", sy)


def torsion_fig():
    r, L, arm = 2.5, 300.0, 50.0; J = np.pi * r ** 4 / 2
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9))
    m = np.arange(0, 600, 100); T = m / 1000 * g * arm; Gs = {"steel": 79.6e3, "brass": 38e3, "aluminium": 25.5e3}
    for (name, G), c in zip(Gs.items(), (BLUE, ORANGE, GREEN)):
        phi = np.degrees(T * L / (G * J)); a.plot(T / 1000, phi, "o-", color=c, lw=2.2, label="%s  G = %.1f GPa" % (name, G / 1e3))
    a.set_xlabel("torque T (N·m)"); a.set_ylabel("twist angle (degrees)"); a.legend(fontsize=8.5); a.set_title("Twist vs torque: slope = L/(GJ)")
    Ls = np.linspace(100, 400, 50)
    for (name, G), c in zip(Gs.items(), (BLUE, ORANGE, GREEN)):
        b.plot(Ls, np.degrees(0.245e3 * Ls / (G * J)), color=c, lw=2.2, label=name)
    b.set_xlabel("shaft length L (mm), at fixed torque 0.245 N·m"); b.set_ylabel("twist angle (degrees)"); b.legend(fontsize=8.5); b.set_title("Twist is proportional to length")
    save(fig, "torsion-twist")
    print("torsion: J =", round(J, 2), "mm^4; T(500 g, arm 50 mm) =", round(.5 * g * arm / 1000, 4), "N·m; twist deg steel/brass/Al:", [round(float(np.degrees(0.245e3 * L / (G * J))), 3) for G in Gs.values()])
    print("G/E check: E=210, nu=0.3 -> G =", round(210 / (2 * 1.3), 1), "GPa (steel quoted 79.6);  Al: E=70, nu=0.33 ->", round(70 / (2 * 1.33), 1), "(quoted 25.5)")


if __name__ == "__main__":
    beam_figs(); buckling_fig(); tensile_fig(); torsion_fig()
