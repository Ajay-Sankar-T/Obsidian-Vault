"""Tutorial 3 and Tutorial 4 figures -> Problems/Tutorial 3 - AC Circuit Analysis/assets and
Problems/Tutorial 4 - Resonance, Filter and Three-Phase Circuits/assets.   Run:  python ee_figs_t3_t4.py"""
import os
import math
import cmath
import numpy as np
from matplotlib.patches import Rectangle
from ee_draw import *

HERE = os.path.dirname(os.path.abspath(__file__))
P3 = os.path.join(HERE, "..", "Problems", "Tutorial 3 - AC Circuit Analysis", "assets")
P4 = os.path.join(HERE, "..", "Problems", "Tutorial 4 - Resonance, Filter and Three-Phase Circuits", "assets")
os.makedirs(P3, exist_ok=True); os.makedirs(P4, exist_ok=True)


def zbox(ax, p1, p2, lab="", side=1, body=1.5, h=0.42):
    L = float(np.hypot(p2[0] - p1[0], p2[1] - p1[1])); ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
    px, py = -uy, ux
    a = (L - body) / 2
    s = (p1[0] + ux * a, p1[1] + uy * a); e = (p1[0] + ux * (a + body), p1[1] + uy * (a + body))
    wire(ax, p1, s); wire(ax, e, p2)
    c = ((s[0] + e[0]) / 2, (s[1] + e[1]) / 2)
    pts = [(s[0] + px * h, s[1] + py * h), (e[0] + px * h, e[1] + py * h), (e[0] - px * h, e[1] - py * h), (s[0] - px * h, s[1] - py * h), (s[0] + px * h, s[1] + py * h)]
    wire(ax, *pts)
    if lab:
        ax.text(c[0] + px * (h + 0.35) * side, c[1] + py * (h + 0.35) * side, lab, ha="center", va="center", fontsize=9)


def mk(path, xl, yl, title, draw, size):
    f, ax = plt.subplots(figsize=size); draw(ax); finish(ax, xl, yl, title); save(f, path)


def phasors(ax, items, lim, title="", rings=()):
    """items: (label, magnitude, angle_deg, colour); drawn from the origin"""
    for r in rings:
        th = np.linspace(0, 2 * np.pi, 200); ax.plot(r * np.cos(th), r * np.sin(th), color="#cccccc", lw=0.8, ls="--")
    ax.axhline(0, color="#999999", lw=0.8); ax.axvline(0, color="#999999", lw=0.8)
    for lab, m, a, c in items:
        x, y = m * math.cos(math.radians(a)), m * math.sin(math.radians(a))
        ax.annotate("", xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=1.8))
        ax.text(x * 1.07 + (0.02 * lim if x >= 0 else -0.02 * lim), y * 1.07, lab, color=c, fontsize=9, ha="left" if x >= 0 else "right", va="center")
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal"); ax.grid(alpha=0.2); ax.set_title(title, fontsize=10)


# ----------------------------------------------------------------- Tutorial 3
def t3_q1_q2():
    f, axs = plt.subplots(1, 3, figsize=(12, 3.0))
    t = np.linspace(0, 2, 801)
    sq = np.where((t % 1) < 0.5, 1, -1); uni = np.where((t % 1) < 0.5, 1, 0)
    axs[0].plot(t, sq, color=BLUE, lw=2); axs[0].set_title("(a) square, ±$I_m$:  avg 0, rms $I_m$"); axs[0].set_ylim(-1.4, 1.4)
    axs[1].plot(t, uni, color=ORANGE, lw=2); axs[1].axhline(0.5, color=GREY, ls="--"); axs[1].set_title("(b) unipolar: avg $I_m/2$, rms $I_m/\\sqrt{2}$"); axs[1].set_ylim(-0.4, 1.4)
    tt = np.linspace(0, 6, 1201); v = np.piecewise(tt, [(tt % 3) < 1, ((tt % 3) >= 1) & ((tt % 3) < 2), (tt % 3) >= 2], [0, 10, 20])
    axs[2].plot(tt, v, color=GREEN, lw=2); axs[2].axhline(10, color=GREY, ls="--"); axs[2].axhline(12.909, color=RED, ls=":"); axs[2].set_title("Q2: avg 10 V, rms 12.91 V"); axs[2].set_ylim(-3, 25)
    for a in axs: a.set_xlabel("t (units of T, or s)"); a.grid(alpha=0.3)
    save(f, os.path.join(P3, "T3-Q1-Q2-waveforms.png"))


def t3_q4_q6_q7():
    f, axs = plt.subplots(1, 3, figsize=(13, 4.2))
    phasors(axs[0], [("V = 120.2∠0°", 120.2, 0, BLUE), ("I (leads 30°)", 100, 30, ORANGE), ("$V_R$ = 104.1∠30°", 104.1, 30, GREEN), ("$V_{XC}$ = 60.1∠−60°", 60.1, -60, RED)], 175, "Q4: RC series, current leads 30°")
    i1 = 10 * cmath.exp(-1j * math.radians(45)); i2 = 20 * cmath.exp(1j * math.radians(30)); i3 = 5 * cmath.exp(1j * math.radians(60)); it = i1 + i2 + i3
    phasors(axs[1], [("$I_1$ 10∠−45°", 10, -45, BLUE), ("$I_2$ 20∠30°", 20, 30, GREEN), ("$I_3$ 5∠60°", 5, 60, ORANGE), ("$I$ = 27.85∠15.1°", abs(it), math.degrees(cmath.phase(it)), RED)], 40, "Q6: branch currents, V reference")
    I = 2.1213; Vm = 106.07
    phasors(axs[2], [("V 106∠0°", 106.07, 0, BLUE), ("I 2.12∠−36.9° (×50)", I * 50, -36.87, ORANGE), ("$V_R$ 84.9∠−36.9°", 84.85, -36.87, GREEN), ("$V_L$ 275.8∠53.1°", 275.8, 53.13, RED), ("$V_C$ 212.1∠−126.9°", 212.1, -126.87, "#8844aa")], 380, "Q7: series RLC, $V_L$ and $V_C$ exceed $V$")
    save(f, os.path.join(P3, "T3-Q4-Q6-Q7-phasors.png"))


def t3_q8():
    f, ax = plt.subplots(figsize=(5.8, 4.4))
    ax.annotate("", xy=(180, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2)); ax.text(70, -22, "P = 180 W", color=GREEN)
    ax.annotate("", xy=(180, 585), xytext=(180, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2)); ax.text(190, 300, "$Q_L$ = +585 VAr", color=RED)
    ax.annotate("", xy=(180, 135), xytext=(180, 585), arrowprops=dict(arrowstyle="-|>", color="#8844aa", lw=2)); ax.text(190, 430, "$Q_C$ = −450 VAr", color="#8844aa")
    ax.annotate("", xy=(180, 135), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2)); ax.text(20, 95, "S = 180 + j135\n|S| = 225 VA, pf 0.8 lag", color=BLUE, fontsize=9)
    ax.set_xlim(-30, 380); ax.set_ylim(-60, 640); ax.set_xlabel("P (W)"); ax.set_ylabel("Q (VAr)"); ax.grid(alpha=0.3); ax.set_title("Q8: the capacitor cancels most of the inductor's Q")
    save(f, os.path.join(P3, "T3-Q8-power-triangle.png"))


def t3_circuits():
    def q9(ax):
        wire(ax, (0, 0), (8, 0)); vsrc(ax, (0, 0), (0, 3), "$\\bar V_1$ = 100∠0° V", plus=2, side=-1, ac=True); wire(ax, (0, 3), (0.8, 3))
        zbox(ax, (0.8, 3), (3.4, 3), "$Z_1$ = 6 + j8 Ω"); dot(ax, 4.4, 3); zbox(ax, (3.4, 3), (4.4, 3), "", body=0.01); wire(ax, (3.4, 3), (4.4, 3))
        zbox(ax, (4.4, 3), (7.0, 3), "$Z_2$ = 6 − j8 Ω"); wire(ax, (7.0, 3), (7.6, 3)); vsrc(ax, (7.6, 0), (7.6, 3), "$\\bar V_2$ = 100∠−60° V", plus=2, side=1, ac=True)
        zbox(ax, (4.4, 3), (4.4, 0), "$Z_3$ = j10 Ω", side=1, body=1.4); node(ax, 4.4, 3, "N", dy=0.25, c=RED)
        arrow(ax, (4.0, 2.4), (4.0, 1.5), "$\\bar I_3$", side=-1)
    def q10(ax):
        wire(ax, (0, 0), (9, 0)); vsrc(ax, (0, 0), (0, 3), "e(t) = 141 sin 400t", plus=2, side=1, ac=True); wire(ax, (0, 3), (0.5, 3))
        res(ax, (0.5, 3), (2.6, 3), "$R_1$ = 3 Ω"); zbox(ax, (2.6, 3), (4.8, 3), "X", body=1.0); node(ax, 5.4, 3, "a", c=RED); wire(ax, (4.8, 3), (5.4, 3))
        wire(ax, (5.4, 3), (9, 3)); dot(ax, 6.5, 3); res(ax, (6.5, 3), (6.5, 1.7), "$R_2$ = 100 Ω", side=1); cap(ax, (6.5, 1.7), (6.5, 0), "25 µF", side=1)
        dot(ax, 8.5, 3); ind(ax, (8.5, 3), (8.5, 0), "0.1 H", side=1); node(ax, 5.4, 0, "b", dy=-0.55, c=RED)
    def q11(ax):
        wire(ax, (0, 0), (9, 0)); vsrc(ax, (0, 0), (0, 3), "$\\bar V_1$ = 10∠0° V", plus=2, side=-1, ac=True); wire(ax, (0, 3), (0.5, 3))
        zbox(ax, (0.5, 3), (3.5, 3), "$Z_1$ = 1 + j1 Ω"); wire(ax, (3.5, 3), (4.5, 3)); node(ax, 4.5, 3, "a", c=RED)
        zbox(ax, (4.5, 3), (4.5, 0), "$Z_3$ = 1 + j2 Ω", side=1, body=1.4); node(ax, 4.5, 0, "b", dy=-0.55, c=RED)
        zbox(ax, (4.5, 3), (7.5, 3), "$Z_2$ = 1 − j1 Ω"); wire(ax, (7.5, 3), (8.2, 3)); vsrc(ax, (8.2, 0), (8.2, 3), "$\\bar V_2$ = 10∠−60° V", plus=2, side=1, ac=True)
        for x, n in ((2.0, "$\\bar I_1$"), (6.3, "$\\bar I_2$")):
            ax.add_patch(FancyArrowPatch((x + 0.6, 1.1), (x - 0.6, 1.1), connectionstyle="arc3,rad=-1.0", arrowstyle="-|>", mutation_scale=11, color=ORANGE, lw=1.5)); ax.text(x, 1.45, n, ha="center", color=ORANGE)
    mk(os.path.join(P3, "T3-Q9-circuit.png"), (-4.6, 11.8), (-0.6, 3.9), "Q9: one unknown node N", q9, (9.0, 2.9))
    mk(os.path.join(P3, "T3-Q10-circuit.png"), (-4.0, 9.8), (-0.9, 3.9), "Q10: find X so that the source current is in phase", q10, (7.8, 3.0))
    mk(os.path.join(P3, "T3-Q11-circuit.png"), (-4.0, 13.0), (-0.9, 3.9), "Q11/Q12: two sources, shared branch $Z_3$", q11, (9.4, 3.0))


def t3_q12():
    f, ax = plt.subplots(figsize=(6.2, 3.5))
    R3 = np.linspace(0.05, 6, 400); Zth = 1.0; Vth = 13.66
    P = (Vth / np.abs(Zth + R3)) ** 2 * R3
    ax.plot(R3, P, color=BLUE, lw=2); ax.plot([1], [46.65], "o", color=RED); ax.annotate("$Z_3$ = 1 Ω: $P_{max}$ = 46.65 W", (1, 46.65), xytext=(2, 44), fontsize=9)
    ax.set_xlabel("$R_3$ (Ω), with $X_3=0$"); ax.set_ylabel("power in $Z_3$ (W)"); ax.set_title("Q12: maximum power when $Z_3=Z_{th}^*=1$ Ω"); ax.grid(alpha=0.3)
    save(f, os.path.join(P3, "T3-Q12-power-curve.png"))


# ----------------------------------------------------------------- Tutorial 4
def t4_resonance():
    f, axs = plt.subplots(1, 3, figsize=(13, 3.6))
    w = np.linspace(200, 3000, 1500); R, L, C = 10, 0.01, 100e-6
    Z = R + 1j * (w * L - 1 / (w * C)); I = 1 / np.abs(Z)
    axs[0].plot(w, I, color=BLUE, lw=2); axs[0].axhline(0.1 / math.sqrt(2), color=GREY, ls="--"); axs[0].plot([618.03, 1618.03], [0.0707] * 2, "o", color=RED)
    axs[0].axvline(1000, color=GREY, ls=":"); axs[0].set_title("Q1: series, $Q=1$: current vs ω"); axs[0].set_xlabel("ω (rad/s)"); axs[0].set_ylabel("|I| per volt")
    axs[0].annotate("ω₁ = 618", (618, 0.0707), xytext=(250, 0.04), fontsize=9); axs[0].annotate("ω₂ = 1618", (1618, 0.0707), xytext=(1700, 0.045), fontsize=9)
    wl = np.logspace(0, 6.5, 1500); R, L, C = 10, 1, 1e-6
    Y = 1 / R + 1 / (1j * wl * L) + 1j * wl * C; V = 1 / np.abs(Y)
    axs[1].semilogx(wl, V, color=ORANGE, lw=2); axs[1].axhline(10 / math.sqrt(2), color=GREY, ls="--"); axs[1].axvline(1000, color=GREY, ls=":")
    axs[1].set_title("Q2: parallel, $Q=0.01$: |V| for 1 A"); axs[1].set_xlabel("ω (rad/s, log)"); axs[1].set_ylabel("|V| (V)"); axs[1].annotate("flat top: BW ≈ 10⁵ rad/s", (30, 9.2), fontsize=9)
    wq = np.linspace(17000, 23000, 800); Rr, Ll, Cc = 100, 0.25, 1e-8
    Zq = Rr + 1j * (wq * Ll - 1 / (wq * Cc)); Vc = (10 / np.abs(Zq)) / (wq * Cc)
    axs[2].plot(wq, Vc, color=GREEN, lw=2); axs[2].axvline(20000, color=GREY, ls=":"); axs[2].plot([20000], [500], "o", color=RED); axs[2].annotate("500 V = Q × 10 V", (20000, 500), xytext=(20300, 480), fontsize=9)
    axs[2].set_title("Q3: $Q=50$, BW = 400 rad/s"); axs[2].set_xlabel("ω (rad/s)"); axs[2].set_ylabel("$|V_C|$ (V)")
    for a in axs: a.grid(alpha=0.3)
    save(f, os.path.join(P4, "T4-Q1-Q2-Q3-resonance.png"))


def t4_filters():
    f, axs = plt.subplots(2, 2, figsize=(11, 6.6))
    fr = np.logspace(1, 6, 800)
    lp = 1 / np.sqrt(1 + (fr / 1000) ** 2); axs[0, 0].semilogx(fr, 20 * np.log10(lp), color=BLUE, lw=2); axs[0, 0].axhline(-3.01, color=GREY, ls="--"); axs[0, 0].axvline(1000, color=RED, ls=":")
    axs[0, 0].set_title("Q4: RC low-pass, $f_c$=1 kHz (R = 100 Ω, C = 1.6 µF)"); axs[0, 0].set_ylim(-45, 3)
    hp = (fr / 20000) / np.sqrt(1 + (fr / 20000) ** 2); axs[0, 1].semilogx(fr, 20 * np.log10(hp), color=ORANGE, lw=2); axs[0, 1].axhline(-3.01, color=GREY, ls="--"); axs[0, 1].axvline(20000, color=RED, ls=":")
    axs[0, 1].set_title("Q5: RC high-pass, $f_c$=20 kHz (R = 1 kΩ, C = 7.95 nF)"); axs[0, 1].set_ylim(-45, 3)
    w = np.logspace(1, 5, 1000); L, C, R = 1, 1e-6, 1000
    H = R / (R + 1j * w * L + 1 / (1j * w * C)); axs[1, 0].semilogx(w, 20 * np.log10(np.abs(H)), color=GREEN, lw=2); axs[1, 0].axhline(-3.01, color=GREY, ls="--")
    for x in (618.03, 1000, 1618.03): axs[1, 0].axvline(x, color=RED, ls=":")
    axs[1, 0].set_title("Q6: series L-C then R: band-pass, $\\omega_0$=1000, BW=1000"); axs[1, 0].set_ylim(-45, 3)
    fw = np.logspace(1, 4, 1000); w7 = 2 * np.pi * fw; L7, C7, R7 = 791.6e-6, 200e-6, 4000
    Zp = 1 / (1 / (1j * w7 * L7) + 1j * w7 * C7); H7 = R7 / (R7 + Zp); axs[1, 1].semilogx(fw, 20 * np.log10(np.abs(H7) + 1e-12), color=RED, lw=2); axs[1, 1].axvline(400, color=GREY, ls=":")
    axs[1, 1].set_title("Q7: parallel LC in series with the load: notch at 400 Hz"); axs[1, 1].set_ylim(-60, 3)
    for a, xl in zip(axs.ravel(), ("f (Hz)", "f (Hz)", "ω (rad/s)", "f (Hz)")): a.set_xlabel(xl); a.set_ylabel("|H| (dB)"); a.grid(alpha=0.3, which="both")
    save(f, os.path.join(P4, "T4-Q4-Q7-filters.png"))
    def q6c(ax):
        ind(ax, (0, 3), (2.4, 3), "L = 1 H"); cap(ax, (2.4, 3), (4.8, 3), "C = 1 µF"); wire(ax, (4.8, 3), (6, 3)); res(ax, (6, 3), (6, 0), "R = 1 kΩ", side=1)
        wire(ax, (0, 0), (6, 0)); node(ax, 0, 3, None); node(ax, 0, 0, None); ax.text(-0.5, 1.5, "$V_i$", ha="right", color=BLUE); ax.text(6.8, 1.5, "$V_0$", color=BLUE)
        ax.annotate("", xy=(-0.2, 2.9), xytext=(-0.2, 0.1), arrowprops=dict(arrowstyle="-|>", color=BLUE)); ax.annotate("", xy=(6.5, 2.9), xytext=(6.5, 0.1), arrowprops=dict(arrowstyle="-|>", color=BLUE))
    def q7c(ax):
        wire(ax, (0, 3), (1, 3)); wire(ax, (1, 3), (1, 4.2)); cap(ax, (1, 4.2), (4, 4.2), "C = 200 µF", side=1); wire(ax, (4, 4.2), (4, 3)); wire(ax, (1, 3), (1, 1.8)); ind(ax, (1, 1.8), (4, 1.8), "L", side=-1); wire(ax, (4, 1.8), (4, 3))
        dot(ax, 1, 3); dot(ax, 4, 3); wire(ax, (4, 3), (5.5, 3)); dot(ax, 5.5, 3); res(ax, (5.5, 3), (5.5, 0), "R = 4 kΩ", side=1); wire(ax, (0, 0), (5.5, 0))
        node(ax, 0, 3, "$V_{in}$", dx=0.1); node(ax, 6.5, 3, "$V_{out}$", dx=0.0); wire(ax, (5.5, 3), (6.5, 3))
    mk(os.path.join(P4, "T4-Q6-circuit.png"), (-1.5, 7.5), (-0.6, 4.0), "Q6: band-pass (series LC, output across R)", q6c, (6.2, 2.7))
    mk(os.path.join(P4, "T4-Q7-circuit.png"), (-1.5, 7.8), (-0.6, 5.4), "Q7: band-reject (parallel LC in the signal path)", q7c, (6.2, 3.6))


def t4_q8():
    f, ax = plt.subplots(figsize=(6.6, 3.6)); fm = np.linspace(96, 104, 2000); Q = 251.2
    x = fm / 100; H = 1 / np.sqrt(1 + Q ** 2 * (x - 1 / x) ** 2)
    ax.plot(fm, 20 * np.log10(H), color=BLUE, lw=2); ax.axhline(-20, color=GREY, ls="--")
    for fx in (98, 102): ax.plot([fx], [-20], "o", color=RED)
    ax.annotate("102 MHz: exactly −20 dB", (102, -20), xytext=(100.3, -33), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("98 MHz: −19.2 dB (needs only Q = 246)", (98, -20), xytext=(96.2, -6), arrowprops=dict(arrowstyle="->"), fontsize=9) if False else None
    ax.set_xlabel("f (MHz)"); ax.set_ylabel("|H| (dB)"); ax.set_title("Q8: series-RLC band-pass at 100 MHz, Q = 251.2"); ax.grid(alpha=0.3); ax.set_ylim(-45, 2)
    save(f, os.path.join(P4, "T4-Q8-selectivity.png"))


def t4_three_phase():
    f, axs = plt.subplots(1, 3, figsize=(13, 4.4))
    r3 = math.sqrt(3)
    # Q9 delta: line voltages 220 (abc), phase currents 10, line currents 17.32
    items = [("$V_{ab}$ 220∠0°", 220, 0, BLUE), ("$V_{bc}$ 220∠−120°", 220, -120, GREEN), ("$V_{ca}$ 220∠120°", 220, 120, ORANGE)]
    items += [("$I_{ab}$ 10∠−30° (×10)", 100, -30, "#8844aa"), ("$I_a$ 17.32∠−60° (×10)", 173.2, -60, RED)]
    phasors(axs[0], items, 330, "Q9: delta load, $V_{ab}$ taken as reference", rings=(220,))
    # Q10: phase currents 8.8 and line currents 15.24
    Iph = 8.8; ang = -53.13
    items = [("$I_{ab}$ 8.8∠−53.1°", Iph, ang, "#8844aa"), ("$I_{bc}$ 8.8∠−173.1°", Iph, ang - 120, "#8844aa"), ("$I_{ca}$ 8.8∠66.9°", Iph, ang + 120, "#8844aa")]
    for k, n in enumerate("abc"):
        items.append((f"$I_{n}$ 15.24∠{ang - 30 - 120 * k:.1f}°".replace("-", "−") if True else "", Iph * r3, ang - 30 - 120 * k, RED))
    phasors(axs[1], items, 26, "Q10: phase currents (purple) and line currents (red)")
    items = [("$V_{an}$ 20∠30°", 20, 30, BLUE), ("$V_{bn}$ 20∠−90°", 20, -90, GREEN), ("$V_{cn}$ 20∠150°", 20, 150, ORANGE), ("$V_{ac}=V_{an}-V_{cn}$ 34.64∠0°", 34.64, 0, RED), ("$I_a$ 5∠−30° (×4)", 20, -30, "#8844aa")]
    phasors(axs[2], items, 55, "Q12: star load, line-to-neutral and line voltages")
    save(f, os.path.join(P4, "T4-Q9-Q10-Q12-phasors.png"))


if __name__ == "__main__":
    t3_q1_q2(); t3_q4_q6_q7(); t3_q8(); t3_circuits(); t3_q12()
    t4_resonance(); t4_filters(); t4_q8(); t4_three_phase()
    print("T3/T4 figures written")
