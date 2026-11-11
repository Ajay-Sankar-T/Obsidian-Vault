"""Figures for the Strength of Materials formula bank and question bank (assets/SM-FB-*.png and SM-QB-*.png).
Run: python sm_bank_figs.py   (numbers come from sm_bank_core.py)"""
import os
import numpy as np
from math import pi, sqrt, sin, cos, radians, degrees, atan2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon, Arc
import sm_bank_core as C

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, RED, GREEN, GREY, INK = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a", "#777777", "#222222"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.titlesize": 10, "axes.titleweight": "bold",
                     "figure.dpi": 100, "savefig.dpi": 170, "savefig.bbox": "tight", "axes.grid": False})


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, name), facecolor="white")
    plt.close(fig)
    print("saved", name)


def arrow(ax, p, q, color=INK, lw=1.4, style="-|>", ms=9, **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, lw=lw, color=color, **kw))


# ====================================================================================== FB-1 stress-strain
def fb_stress_strain():
    """Schematic: elastic strain is exaggerated so that every feature is visible."""
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.1), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axs[0]
    xp, xy1, xy2, xh, xu, xf = 1.0, 1.15, 1.7, 4.0, 16.0, 24.0
    sp, syu, syl, su, sf = 200.0, 250.0, 235.0, 400.0, 300.0
    e1 = np.linspace(0, xp, 20)
    e2 = np.linspace(xp, xy1, 10)
    e3 = np.linspace(xy1, xy2, 10)
    e4 = np.linspace(xy2, xh, 20)
    e5 = np.linspace(xh, xu, 200)
    e6 = np.linspace(xu, xf, 100)
    ex = np.concatenate([e1, e2, e3, e4, e5, e6])
    sx = np.concatenate([sp * e1 / xp,
                         sp + (syu - sp) * (e2 - xp) / (xy1 - xp),
                         syu - (syu - syl) * (e3 - xy1) / (xy2 - xy1),
                         np.full_like(e4, syl),
                         syl + (su - syl) * (1 - (1 - (e5 - xh) / (xu - xh)) ** 2.2),
                         su - (su - sf) * ((e6 - xu) / (xf - xu)) ** 1.7])
    ax.plot(ex, sx, color=BLUE, lw=2.2, zorder=3)
    m = ex <= xu
    ax.plot(ex[m], sx[m] * (1 + 0.45 * ex[m] / 100 * 6), color=GREY, lw=1.2, ls="--")
    ax.text(10.5, 452, "true stress (rises to fracture)", color=GREY, fontsize=8, ha="center")
    # offset line
    off_x = np.linspace(0.45, 1.5, 10)
    ax.plot(off_x, sp / xp * (off_x - 0.45), color=RED, lw=1, ls=":")
    pts = [(xp, sp, "A  proportional limit", (3.6, 80)),
           (xy1, syu, "B  upper yield", (4.2, 285)),
           (3.0, syl, "lower yield, plateau", (6.5, 160)),
           (xu, su, "C  ultimate  $S_u=P_{max}/A_0$", (8.0, 430)),
           (xf, sf, "D  fracture", (19.2, 205))]
    for x, y, lab, tp in pts:
        ax.plot([x], [y], "o", color=INK, ms=4.5, zorder=5)
        ax.annotate(lab, (x, y), xytext=tp, fontsize=8.5, arrowprops=dict(arrowstyle="-", lw=0.7, color=GREY))
    ax.annotate("necking starts: load\nfalls on the original area", (19, 385), xytext=(18.3, 330), fontsize=8.2, color=ORANGE, ha="left",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9))
    ax.annotate("0.2 % offset line,\nparallel to $E$", (1.35, 180), xytext=(4.0, 20), fontsize=8.2, color=RED, arrowprops=dict(arrowstyle="->", color=RED, lw=0.9))
    # unloading from the strain-hardening region
    xu0 = 11.0
    yu0 = float(np.interp(xu0, ex, sx))
    ax.plot([xu0, xu0 - yu0 / sp * xp], [yu0, 0], color=GREEN, lw=1.3)
    ax.annotate("unload $\\parallel E$: permanent\nset remains", (xu0 - yu0 / sp * xp + 0.15, 0), xytext=(13.0, 25), fontsize=8.2, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=0.9))
    ax.set_xlabel("engineering strain $e$ (schematic: elastic part exaggerated)")
    ax.set_ylabel("engineering stress $S$ (MPa)")
    ax.set_title("Mild steel, engineering curve")
    ax.set_xlim(0, 26)
    ax.set_ylim(0, 480)
    ax = axs[1]
    eb = np.linspace(0, 1, 100)
    ax.plot(eb, 300 * (eb - 0.25 * eb**2) / 0.75, color=ORANGE, lw=2.2)
    ax.plot([1], [300], "x", color=RED, ms=9, mew=2.2)
    ax.text(0.93, 232, "fracture:\nno yield,\nno neck", color=RED, fontsize=8.5, ha="right")
    ax.text(0.03, 450, "stays nearly linear;\nweak in tension, strong\nin compression", fontsize=8.5, color=GREY, va="top")
    ax.set_title("Brittle (cast iron, glass)")
    ax.set_xlabel("engineering strain $e$ (schematic)")
    ax.set_xlim(0, 1.1)
    ax.set_ylim(0, 480)
    ax.set_yticks([])
    save(fig, "SM-FB-1-stress-strain.png")


# ====================================================================================== FB-2 Mohr's circle
def fb_mohr():
    sx, sy, txy = 80.0, -40.0, 30.0
    c, R, s1, s2, thp = C.principal(sx, sy, txy)
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    t = np.linspace(0, 2 * pi, 400)
    ax.plot(c + R * np.cos(t), R * np.sin(t), color=BLUE, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(0, color=GREY, lw=0.8)
    # plot with tau positive downward convention (clockwise-shear-positive plotted down): use y = -tau
    X, Y = (sx, -txy), (sy, txy)
    ax.plot([X[0], Y[0]], [X[1], Y[1]], "o-", color=RED, lw=1.6)
    ax.annotate("X  ($\\sigma_x$, $\\tau_{xy}$)", X, xytext=(X[0] + 3, X[1] - 12), color=RED, fontsize=9)
    ax.annotate("Y  ($\\sigma_y$, $-\\tau_{xy}$)", Y, xytext=(Y[0] - 36, Y[1] + 6), color=RED, fontsize=9)
    ax.plot([c], [0], "k+", ms=9)
    ax.annotate("centre $C=\\frac{\\sigma_x+\\sigma_y}{2}$", (c, 0), xytext=(c - 28, -26), fontsize=9)
    for sv, lab, dy in [(s1, "$\\sigma_1$", 8), (s2, "$\\sigma_2$", 8)]:
        ax.plot([sv], [0], "s", color=GREEN, ms=6)
        ax.text(sv, dy, lab, color=GREEN, ha="center", fontsize=11)
    ax.plot([c, c], [-R, R], ":", color=ORANGE)
    ax.text(c + 2, R + 4, "$\\tau_{max}=R$", color=ORANGE, fontsize=10)
    ax.plot([c], [R], "o", color=ORANGE, ms=5)
    ax.plot([c], [-R], "o", color=ORANGE, ms=5)
    # 2 theta_p arc from CX to the sigma_1 axis
    ang = degrees(atan2(X[1], X[0] - c))
    ax.add_patch(Arc((c, 0), 2 * 27, 2 * 27, theta1=ang, theta2=0, color=INK, lw=1.2))
    ax.text(c + 31, -10, "$2\\theta_p$", fontsize=10)
    ax.text(c + R * 0.55, -R * 0.93, "$R=\\sqrt{(\\frac{\\sigma_x-\\sigma_y}{2})^2+\\tau_{xy}^2}$", fontsize=9, color=BLUE)
    ax.set_aspect("equal")
    ax.set_xlabel("normal stress $\\sigma$ (MPa)")
    ax.set_ylabel("shear stress $\\tau$ (MPa), clockwise-positive plotted down")
    ax.invert_yaxis()
    ax.set_title("Mohr's circle for $\\sigma_x=80,\\ \\sigma_y=-40,\\ \\tau_{xy}=30$ MPa")
    ax.set_xlim(-65, 105)
    save(fig, "SM-FB-2-mohr-circle.png")


# ====================================================================================== FB-3 beam cases
def fb_beam_cases():
    fig, axs = plt.subplots(3, 4, figsize=(11, 6.2), gridspec_kw={"height_ratios": [1.0, 1, 1]})
    L = 1.0
    x = np.linspace(0, L, 400)
    titles = ["Simply supported,\ncentral load $P$", "Simply supported,\nUDL $w$", "Cantilever,\ntip load $P$", "Cantilever,\nUDL $w$"]
    Vs = [np.where(x < 0.5, 0.5, -0.5), 0.5 - x, np.ones_like(x) * 1.0, 1.0 - x]
    Ms = [np.where(x < 0.5, 0.5 * x, 0.5 * (1 - x)), 0.5 * x - x**2 / 2, -(1 - x), -(1 - x)**2 / 2]
    Vlab = [("$P/2$", "$-P/2$"), ("$wL/2$", "$-wL/2$"), ("$P$", ""), ("$wL$", "")]
    Mlab = ["$M_{max}=PL/4$", "$M_{max}=wL^2/8$", "$M_{max}=PL$ (at wall)", "$M_{max}=wL^2/2$ (at wall)"]
    defl = ["$\\delta_{max}=\\dfrac{PL^3}{48EI}$\n$\\theta_{end}=\\dfrac{PL^2}{16EI}$", "$\\delta_{max}=\\dfrac{5wL^4}{384EI}$\n$\\theta_{end}=\\dfrac{wL^3}{24EI}$",
            "$\\delta_{tip}=\\dfrac{PL^3}{3EI}$\n$\\theta_{tip}=\\dfrac{PL^2}{2EI}$", "$\\delta_{tip}=\\dfrac{wL^4}{8EI}$\n$\\theta_{tip}=\\dfrac{wL^3}{6EI}$"]
    for j in range(4):
        ax = axs[0, j]
        ax.set_xlim(-0.15, 1.15)
        ax.set_ylim(-0.55, 0.9)
        ax.axis("off")
        ax.set_title(titles[j], fontsize=9)
        ax.plot([0, 1], [0, 0], color=INK, lw=5, solid_capstyle="butt")
        if j < 2:
            ax.add_patch(Polygon([[0, -0.0], [-0.06, -0.14], [0.06, -0.14]], color=GREY))
            ax.add_patch(Circle((1, -0.07), 0.05, color=GREY))
        else:
            ax.add_patch(Rectangle((-0.08, -0.2), 0.08, 0.4, color=GREY, hatch="///", fill=False))
        if j == 0:
            arrow(ax, (0.5, 0.65), (0.5, 0.06), RED, lw=2)
            ax.text(0.53, 0.55, "$P$", color=RED, fontsize=11)
        elif j == 1 or j == 3:
            for xx in np.linspace(0.04, 0.96, 9):
                arrow(ax, (xx, 0.38), (xx, 0.06), RED, lw=1, ms=7)
            ax.plot([0.04, 0.96], [0.38, 0.38], color=RED, lw=1)
            ax.text(0.5, 0.45, "$w$", color=RED, ha="center", fontsize=11)
        else:
            arrow(ax, (1, 0.65), (1, 0.06), RED, lw=2)
            ax.text(0.93, 0.55, "$P$", color=RED, fontsize=11)
        ax.annotate("", (0, -0.35), (1, -0.35), arrowprops=dict(arrowstyle="<->", lw=0.8))
        ax.text(0.5, -0.5, "$L$", ha="center")
        ax = axs[1, j]
        ax.fill_between(x, Vs[j], 0, color=BLUE, alpha=0.25)
        ax.plot(x, Vs[j], color=BLUE, lw=1.6)
        ax.axhline(0, color=GREY, lw=0.8)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylim(-0.75, 1.25)
        if j == 0:
            ax.text(0.04, 0.55, Vlab[j][0], color=BLUE); ax.text(0.7, -0.68, Vlab[j][1], color=BLUE)
        elif j == 1:
            ax.text(0.04, 0.55, Vlab[j][0], color=BLUE); ax.text(0.7, -0.68, Vlab[j][1], color=BLUE)
        else:
            ax.text(0.05, 1.07, Vlab[j][0], color=BLUE)
        if j == 0:
            ax.set_ylabel("shear $V$", rotation=0, ha="right", va="center", color=BLUE)
        ax = axs[2, j]
        ax.fill_between(x, Ms[j], 0, color=ORANGE, alpha=0.25)
        ax.plot(x, Ms[j], color=ORANGE, lw=1.6)
        ax.axhline(0, color=GREY, lw=0.8)
        ax.set_xticks([])
        ax.set_yticks([])
        if j < 2:
            ax.set_ylim(-0.08, 0.34)
            ax.text(0.5, 0.29 if j == 0 else 0.15, Mlab[j], ha="center", color=ORANGE, fontsize=8)
        else:
            ax.set_ylim(-1.15 if j == 2 else -0.7, 0.1)
            ax.text(0.45, -0.42 if j == 2 else -0.28, Mlab[j], ha="center", color=ORANGE, fontsize=8)
        ax.set_xlabel(defl[j], fontsize=8.5, labelpad=6)
        if j == 0:
            ax.set_ylabel("moment $M$", rotation=0, ha="right", va="center", color=ORANGE)
    fig.suptitle("Four standard beams: load, shear force, bending moment (sagging positive) and deflection", fontsize=10, fontweight="bold", y=1.0)
    fig.tight_layout()
    save(fig, "SM-FB-3-beam-cases.png")


# ====================================================================================== FB-4 columns
def fb_columns():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axs[0]
    ax.axis("off")
    ax.set_xlim(0, 8)
    ax.set_ylim(-1.3, 4.1)
    y = np.linspace(0, 3, 100)
    shapes = [
        ("pinned–\npinned\n$K=1$", 0.8, lambda y: 0.22 * np.sin(pi * y / 3), "pin", "pin"),
        ("fixed–\nfree\n$K=2$", 2.7, lambda y: 0.30 * (1 - np.cos(pi * y / 6)), "fix", "free"),
        ("fixed–\npinned\n$K\\approx0.7$", 4.6, lambda y: 0.2 * (np.sin(4.4934 * y / 3) / np.sin(4.4934) * -1 + y / 3 * 1) * 1.0, "fix", "pin"),
        ("fixed–\nfixed\n$K=0.5$", 6.5, lambda y: 0.16 * (1 - np.cos(2 * pi * y / 3)) / 2, "fix", "fix"),
    ]
    for lab, x0, f, a, b in shapes:
        if "pinned" in lab and lab.startswith("fixed"):
            kk = 4.4934 / 3
            xs = 0.34 * (np.sin(kk * y) / kk - y * np.cos(4.4934) / 1.0 * 1.0 / 1.0 * 0 ) * 0
            # exact shape: v = (sin(kx) - kx cos(kL)... ) use standard: v ~ sin(kx) - kx*cos(kL)... scaled
            kL = 4.4934
            v = (np.sin(kk * y) - kk * y * np.cos(kL) * 0 - (np.sin(kL) / 3) * y)
            v = v / np.max(abs(v)) * 0.26
            ax.plot(x0 + v, y, color=BLUE, lw=2)
        else:
            ax.plot(x0 + f(y), y, color=BLUE, lw=2)
        ax.plot([x0, x0], [0, 3], color=GREY, lw=0.8, ls=":")
        ax.text(x0, -0.35, lab, ha="center", va="top", fontsize=8.5)
        # supports
        if a == "pin":
            ax.add_patch(Polygon([[x0, 0], [x0 - 0.16, -0.22], [x0 + 0.16, -0.22]], color=GREY))
        else:
            ax.add_patch(Rectangle((x0 - 0.22, -0.16), 0.44, 0.16, color=GREY, hatch="///", fill=False))
        if b == "pin":
            ax.add_patch(Polygon([[x0, 3], [x0 - 0.16, 3.22], [x0 + 0.16, 3.22]], color=GREY))
        elif b == "fix":
            ax.add_patch(Rectangle((x0 - 0.22, 3.0), 0.44, 0.16, color=GREY, hatch="///", fill=False))
        arrow(ax, (x0 - 0.0, 3.95), (x0, 3.5), RED, lw=1.6, ms=8) if b != "free" else arrow(ax, (x0 + 0.3, 3.95), (x0 + 0.3, 3.35), RED, lw=1.6, ms=8)
    ax.set_title("Buckled shapes and effective-length factors", fontsize=9.5)
    ax = axs[1]
    E, sY = 200e3, 250.0
    lam = np.linspace(20, 250, 400)
    euler = pi**2 * E / lam**2
    lc = pi * sqrt(2 * E / sY)
    john = sY * (1 - sY * lam**2 / (4 * pi**2 * E))
    ax.plot(lam[lam >= lc], euler[lam >= lc], color=BLUE, lw=2.2, label="Euler  $\\pi^2E/\\lambda^2$")
    ax.plot(lam[lam < lc], euler[lam < lc], color=BLUE, lw=1.0, ls="--")
    ax.plot(lam[lam <= lc], john[lam <= lc], color=ORANGE, lw=2.2, label="Johnson parabola")
    ax.axhline(sY, color=RED, lw=1, ls=":")
    ax.text(24, sY + 6, "$\\sigma_Y$", color=RED, ha="left")
    ax.axvline(lc, color=GREY, lw=0.8, ls=":")
    ax.text(lc + 2, 300, f"$\\lambda_c=\\pi\\sqrt{{2E/\\sigma_Y}}={lc:.0f}$\n(where $\\sigma_{{cr}}=\\sigma_Y/2$)", fontsize=8.5)
    ax.set_ylim(0, 340)
    ax.set_xlim(20, 250)
    ax.set_xlabel("slenderness ratio  $\\lambda=KL/r$")
    ax.set_ylabel("critical stress (MPa)")
    ax.set_title("Column curve, steel $E=200$ GPa, $\\sigma_Y=250$ MPa", fontsize=9.5)
    ax.annotate("short: crushes", (45, 240), xytext=(28, 150), fontsize=8.5, color=GREY, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.annotate("intermediate:\nyield and buckling interact", (100, 170), xytext=(92, 40), fontsize=8.5, color=ORANGE, arrowprops=dict(arrowstyle="->", color=ORANGE))
    ax.annotate("slender: elastic buckling", (180, 61), xytext=(150, 120), fontsize=8.5, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE))
    ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1, 0.74))
    save(fig, "SM-FB-4-columns.png")


# ====================================================================================== FP failure planes
def fp_failure_planes():
    fig, axs = plt.subplots(2, 3, figsize=(10.5, 6.6))
    for a in axs.flat:
        a.set_xlim(-1.7, 1.7)
        a.set_ylim(-2.7, 2.7)
        a.set_aspect("equal")
        a.axis("off")
    # --- tension, ductile: cup and cone (mating surface is a U with 45 degree lips)
    ax = axs[0, 0]
    ax.set_title("Tension, ductile: cup and cone", fontsize=9.5)
    U = [(-0.30, 0.15), (-0.15, 0.0), (0.15, 0.0), (0.30, 0.15)]
    bot = [(-0.45, -2.0), (-0.45, -1.2), (-0.30, 0.15)] + U[1:3] + [(0.30, 0.15), (0.45, -1.2), (0.45, -2.0)]
    ax.add_patch(Polygon(bot, closed=True, fill=False, ec=INK, lw=1.6))
    g = 0.4
    top = [(-0.45, 2.0), (-0.45, 1.2 + g), (-0.30, 0.15 + g)] + [(x, y + g) for x, y in U[1:3]] + [(0.30, 0.15 + g), (0.45, 1.2 + g), (0.45, 2.0)]
    ax.add_patch(Polygon(top, closed=True, fill=False, ec=INK, lw=1.6))
    arrow(ax, (0, 2.0), (0, 2.55), RED, lw=2)
    arrow(ax, (0, -2.0), (0, -2.55), RED, lw=2)
    ax.plot([0.55, 0.9], [-0.05, 0.3], color=ORANGE, lw=1.6)
    ax.text(0.95, 0.3, "$45^\\circ$ lips\n(shear)", color=ORANGE, fontsize=8.5, va="center")
    ax.text(-0.15, 0.2, "flat centre", fontsize=8, ha="right", va="center", color=GREY)
    ax.text(0, -2.62, "", fontsize=1)
    ax.text(0, -2.75, "centre cracks flat (normal stress),\nrim tears at $45^\\circ$ (maximum shear)", ha="center", fontsize=8.2, va="top")
    # --- tension, brittle
    ax = axs[0, 1]
    ax.set_title("Tension, brittle: flat, $90^\\circ$ to the axis", fontsize=9.5)
    ax.add_patch(Polygon([(-0.45, 2.0), (-0.45, 0.10), (0.45, 0.16), (0.45, 2.0)], closed=True, fill=False, ec=INK, lw=1.6))
    ax.add_patch(Polygon([(-0.45, -2.0), (-0.45, -0.10), (0.45, -0.16), (0.45, -2.0)], closed=True, fill=False, ec=INK, lw=1.6))
    arrow(ax, (0, 2.0), (0, 2.55), RED, lw=2)
    arrow(ax, (0, -2.0), (0, -2.55), RED, lw=2)
    ax.text(0, -2.75, "plane of maximum normal stress;\nno necking, no shear lips", ha="center", fontsize=8.2, va="top")
    # --- torsion, ductile
    ax = axs[0, 2]
    ax.set_title("Torsion, ductile: cross-section plane", fontsize=9.5)
    ax.add_patch(Rectangle((-0.45, -2.0), 0.9, 1.95, fill=False, lw=1.6, ec=INK))
    ax.add_patch(Rectangle((-0.45, 0.05), 0.9, 1.95, fill=False, lw=1.6, ec=INK))
    ax.plot([-0.45, 0.45], [0, 0], color=RED, lw=0.0)
    arrow(ax, (0.95, 1.5), (0.95, 0.7), ORANGE, ms=9, connectionstyle="arc3,rad=-0.5")
    arrow(ax, (0.95, -1.5), (0.95, -0.7), ORANGE, ms=9, connectionstyle="arc3,rad=0.5")
    ax.text(0, 0.0, "", fontsize=1)
    ax.text(0, -2.75, "maximum shear acts on the cross-section;\nflat, smooth, rotated face", ha="center", fontsize=8.2, va="top")
    # --- torsion, brittle (45 degree helical crack)
    ax = axs[1, 0]
    ax.set_title("Torsion, brittle: $45^\\circ$ helix", fontsize=9.5)
    ax.add_patch(Rectangle((-0.45, -2.0), 0.9, 4.0, fill=False, lw=1.6, ec=INK))
    ax.plot([-0.45, 0.45], [-1.0, -0.1], color=RED, lw=2.2)
    ax.plot([-0.45, 0.45], [0.1, 1.0], color=RED, lw=0.0)
    ax.plot([0.45, 0.45], [-0.1, 0.1], color=RED, lw=0.0)
    ax.plot([-0.45, 0.45], [-0.1, 0.8], color=RED, lw=0.0)
    ax.annotate("crack $\\perp$ $\\sigma_1$", (0.45, -0.55), xytext=(0.8, -0.1), fontsize=8.5, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    arrow(ax, (-0.95, 1.5), (-0.95, 0.7), ORANGE, ms=9, connectionstyle="arc3,rad=0.5")
    arrow(ax, (-0.95, -1.5), (-0.95, -0.7), ORANGE, ms=9, connectionstyle="arc3,rad=-0.5")
    ax.text(0, -2.75, "maximum tensile stress is at $45^\\circ$ to the axis;\nbrittle solids are weak in tension", ha="center", fontsize=8.2, va="top")
    # --- 3-point bending, ductile
    ax = axs[1, 1]
    ax.set_title("3-point bending, ductile: bends", fontsize=9.5)
    xs = np.linspace(-1.5, 1.5, 100)
    sag = 0.35 * (1 - (xs / 1.5) ** 2)
    ax.fill_between(xs, -0.2 - sag, 0.22 - sag, color="#ddd", edgecolor=INK, lw=1.4)
    ax.add_patch(Polygon([[-1.45, -0.2], [-1.58, -0.45], [-1.32, -0.45]], color=GREY))
    ax.add_patch(Polygon([[1.45, -0.2], [1.58, -0.45], [1.32, -0.45]], color=GREY))
    arrow(ax, (0, 1.2), (0, 0.3), RED, lw=2)
    ax.text(0.1, 0.9, "$P$", color=RED)
    ax.text(0, -2.75, "yields at the load line and arches;\nno fracture until a plastic hinge forms", ha="center", fontsize=8.2, va="top")
    # --- 3-point bending, brittle
    ax = axs[1, 2]
    ax.set_title("3-point bending, brittle: cracks", fontsize=9.5)
    ax.add_patch(Rectangle((-1.5, -0.3), 3.0, 0.6, fill=False, lw=1.6, ec=INK))
    ax.add_patch(Polygon([[-1.3, -0.3], [-1.43, -0.55], [-1.17, -0.55]], color=GREY))
    ax.add_patch(Polygon([[1.3, -0.3], [1.43, -0.55], [1.17, -0.55]], color=GREY))
    arrow(ax, (0, 1.2), (0, 0.4), RED, lw=2)
    ax.plot([0.0, 0.04, -0.04, 0.02], [-0.3, -0.12, 0.05, 0.22], color=RED, lw=2.2)
    ax.text(0.15, -0.95, "tension face", color=RED, fontsize=8.5)
    ax.text(0, -2.75, "$\\sigma_{max}=3PL/2bh^2$ at the bottom of mid-span:\nvertical crack, $\\perp$ to the axis", ha="center", fontsize=8.2, va="top")
    fig.tight_layout()
    save(fig, "SM-FP-failure-planes.png")


# ====================================================================================== QB figures
def qb1_n1_n2():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.2), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axs[0]
    ax.axis("off")
    ax.set_xlim(-0.6, 8.2)
    ax.set_ylim(-1.5, 1.8)
    ax.add_patch(Rectangle((-0.5, -1.0), 0.5, 2.0, color=GREY, hatch="///", fill=False))
    ax.add_patch(Rectangle((0, -0.5), 4.0, 1.0, color="#cfe0f7", ec=INK, lw=1.4))
    ax.add_patch(Rectangle((4.0, -0.31), 3.0, 0.62, color="#f8dcb8", ec=INK, lw=1.4))
    ax.text(2.0, 0, "A  steel\nØ40, 800 mm", ha="center", va="center", fontsize=8.5)
    ax.text(5.5, 0, "aluminium\nØ25, 600", ha="center", va="center", fontsize=8.5)
    ax.plot([4.0, 4.0], [0.5, 1.2], color=RED, lw=1)
    arrow(ax, (4.0, 1.2), (5.3, 1.2), RED, lw=2)
    ax.text(5.4, 1.15, "100 kN", color=RED)
    arrow(ax, (7.9, 0), (7.0, 0), RED, lw=2)
    ax.text(7.3, 0.2, "60 kN", color=RED)
    ax.text(4.0, -0.7, "B", ha="center")
    ax.text(7.0, -0.55, "C", ha="center")
    ax.set_title("Q1: stepped bar (steel AB, aluminium BC)", fontsize=9.5)
    ax = axs[1]
    ax.axis("off")
    ax.set_xlim(-0.4, 3.6)
    ax.set_ylim(-0.9, 2.5)
    ax.plot([-0.2, 3.4], [2.2, 2.2], color=GREY, lw=3)
    ax.add_patch(Rectangle((0, 0.55), 3, 0.18, color=INK))
    ax.plot([0, 0], [0.6, 0.0], color=INK)
    ax.add_patch(Circle((0, 0.64), 0.07, color="white", ec=INK, zorder=5))
    for xx, c_, lab in [(1, BLUE, "steel Ø6, 2 m"), (2, ORANGE, "aluminium Ø8, 1.5 m")]:
        ax.plot([xx, xx], [2.2, 0.73], color=c_, lw=2)
        ax.text(xx + 0.05, 1.5, lab, rotation=90, ha="left", va="center", fontsize=8, color=c_)
    arrow(ax, (3, 0.55), (3, -0.1), RED, lw=2)
    ax.text(3.05, -0.35, "$P=8$ kN", color=RED)
    for xx, lab in [(0, "A"), (1, "1 m"), (2, "2 m"), (3, "3 m")]:
        ax.text(xx + (0.18 if xx == 3 else 0), 0.3, lab, ha="center", fontsize=8)
    ax.set_title("Q2: rigid bar on two wires", fontsize=9.5)
    save(fig, "SM-QB-1-setups.png")


def qb2_beams():
    # N1 and N2 SFD/BMD
    x, V, M, RA, RB = C.beam_ss(8.0, [('w', 0, 8, 10.0), ('P', 3.0, 20.0)], 4001)
    fig, axs = plt.subplots(3, 1, figsize=(8.2, 6.2), gridspec_kw={"height_ratios": [0.9, 1, 1]}, sharex=True)
    ax = axs[0]
    ax.axis("off")
    ax.set_ylim(-0.7, 1.0)
    ax.plot([0, 8], [0, 0], color=INK, lw=5)
    ax.add_patch(Polygon([[0, 0], [-0.15, -0.3], [0.15, -0.3]], color=GREY))
    ax.add_patch(Circle((8, -0.15), 0.12, color=GREY))
    for xx in np.linspace(0.2, 7.8, 17):
        arrow(ax, (xx, 0.38), (xx, 0.06), BLUE, lw=0.9, ms=6)
    ax.plot([0.2, 7.8], [0.38, 0.38], color=BLUE, lw=1)
    ax.text(5.5, 0.5, "10 kN/m", color=BLUE)
    arrow(ax, (3, 0.95), (3, 0.08), RED, lw=2)
    ax.text(3.1, 0.75, "20 kN", color=RED)
    arrow(ax, (0, -0.8), (0, -0.35), GREEN, lw=1.5)
    arrow(ax, (8, -0.8), (8, -0.35), GREEN, lw=1.5)
    ax.text(0.12, -0.7, f"$R_A$={RA:.1f}", color=GREEN, fontsize=8.5)
    ax.text(7.0, -0.7, f"$R_B$={RB:.1f}", color=GREEN, fontsize=8.5)
    ax = axs[1]
    ax.fill_between(x, V, 0, color=BLUE, alpha=0.25)
    ax.plot(x, V, color=BLUE, lw=1.6)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_ylabel("V (kN)")
    ax.set_ylim(-62, 68)
    for xx, yy, t in [(0.08, 52.5, "52.5"), (2.55, 22.5, "22.5"), (3.08, 2.5, "2.5")]:
        ax.text(xx, yy + 4, t, fontsize=8)
    ax.text(7.35, -44, "−47.5", fontsize=8)
    ax.plot([3.25], [0], "ko", ms=4)
    ax.text(3.35, -12, "V=0 at 3.25 m", fontsize=8)
    ax = axs[2]
    ax.fill_between(x, M, 0, color=ORANGE, alpha=0.25)
    ax.plot(x, M, color=ORANGE, lw=1.6)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_ylabel("M (kN·m)")
    ax.plot([3.25], [112.8], "ko", ms=4)
    ax.text(3.45, 108, "$M_{max}$ = 112.8 at 3.25 m", fontsize=8.5)
    ax.plot([3], [112.5], "o", color=INK, ms=3)
    ax.set_xlabel("x (m)")
    ax.set_ylim(0, 135)
    fig.suptitle("Q1: simply supported beam, UDL + point load", fontsize=10, fontweight="bold")
    fig.tight_layout()
    save(fig, "SM-QB-2a-sfd-bmd.png")
    # N2 overhang
    r = C.p2_n2()
    RA_, RC_ = r["RA"], r["RC"]
    xs = np.linspace(0, 8, 4001)
    V2 = np.where(xs <= 6, RA_ - 12 * xs, 18.0 * np.ones_like(xs))
    V2 = np.where(xs <= 6, RA_ - 12 * xs, RA_ + RC_ - 72.0)
    M2 = np.where(xs <= 6, RA_ * xs - 6 * xs**2, -18.0 * (8 - xs))
    fig, axs = plt.subplots(3, 1, figsize=(8.2, 6.2), gridspec_kw={"height_ratios": [0.9, 1, 1]}, sharex=True)
    ax = axs[0]
    ax.axis("off")
    ax.set_ylim(-0.7, 1.0)
    ax.plot([0, 8], [0, 0], color=INK, lw=5)
    ax.add_patch(Polygon([[0, 0], [-0.15, -0.3], [0.15, -0.3]], color=GREY))
    ax.add_patch(Circle((6, -0.15), 0.12, color=GREY))
    for xx in np.linspace(0.2, 5.8, 13):
        arrow(ax, (xx, 0.38), (xx, 0.06), BLUE, lw=0.9, ms=6)
    ax.plot([0.2, 5.8], [0.38, 0.38], color=BLUE, lw=1)
    ax.text(2.2, 0.5, "12 kN/m", color=BLUE)
    arrow(ax, (8, 0.95), (8, 0.08), RED, lw=2)
    ax.text(7.1, 0.75, "18 kN", color=RED)
    ax.text(0, -0.65, "A", ha="center")
    ax.text(6, -0.65, "C", ha="center")
    ax.text(8, -0.4, "D", ha="center")
    ax.text(1.0, -0.55, f"$R_A$={RA_:.0f} kN", color=GREEN, fontsize=8.5)
    ax.text(6.2, -0.55, f"$R_C$={RC_:.0f} kN", color=GREEN, fontsize=8.5)
    ax = axs[1]
    ax.fill_between(xs, V2, 0, color=BLUE, alpha=0.25)
    ax.plot(xs, V2, color=BLUE, lw=1.6)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_ylabel("V (kN)")
    ax.set_ylim(-55, 40)
    ax.text(0.1, 31, "+30", fontsize=8)
    ax.text(5.35, -41, "−42", fontsize=8)
    ax.text(6.2, 20, "+18", fontsize=8)
    ax = axs[2]
    ax.fill_between(xs, M2, 0, color=ORANGE, alpha=0.25)
    ax.plot(xs, M2, color=ORANGE, lw=1.6)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_ylabel("M (kN·m)")
    ax.plot([2.5], [37.5], "ko", ms=4)
    ax.text(2.7, 36, "+37.5 at 2.5 m", fontsize=8.5)
    ax.plot([5], [0], "ro", ms=5)
    ax.annotate("contraflexion at x = 5 m", (5, 0), xytext=(3.4, -22), fontsize=8.5, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    ax.plot([6], [-36], "ko", ms=4)
    ax.text(6.15, -40, "−36 at C", fontsize=8.5)
    ax.set_xlabel("x (m)")
    ax.set_ylim(-50, 50)
    fig.suptitle("Q2: overhanging beam, contraflexion point", fontsize=10, fontweight="bold")
    fig.tight_layout()
    save(fig, "SM-QB-2b-overhang.png")


def qb2_sections():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.9), gridspec_kw={"width_ratios": [1, 1, 1.15]})
    # T-section stresses
    r = C.p2_n3()
    ax = axs[0]
    bf, tf, bw, hw = 120.0, 20.0, 20.0, 100.0
    ax.add_patch(Rectangle((-bf / 2, hw), bf, tf, color="#cfe0f7", ec=INK))
    ax.add_patch(Rectangle((-bw / 2, 0), bw, hw, color="#cfe0f7", ec=INK))
    yb = r["ybar"]
    ax.axhline(yb, color=RED, lw=1, ls="--")
    ax.text(62, yb + 3, f"NA, $\\bar y$={yb:.1f}", color=RED, fontsize=8.5)
    s = 0.4
    ax.fill([-110, -110 + r["s_top"] * s, -110 + r["s_top"] * s, -110][:0] or [-110, -110, -110 + r["s_top"] * s], [yb, hw + tf, hw + tf], alpha=0)
    # linear stress profile at left
    ytop, ybot = hw + tf, 0
    xs0 = -95
    ax.plot([xs0, xs0 + r["s_top"] * 0.5, xs0 + r["s_bot"] * 0.5 * (ytop - yb) / (yb) * 0 + 0], [ytop, ytop, ytop], alpha=0)
    ax.plot([xs0, xs0 + r["s_top"] * 0.5], [yb, ytop], color=BLUE, lw=0)
    ax.fill([xs0, xs0 + r["s_top"] * 0.5, xs0], [yb, ytop, ytop], color=BLUE, alpha=0.3)
    ax.fill([xs0, xs0 + r["s_bot"] * 0.5, xs0], [yb, 0, 0], color=RED, alpha=0.3)
    ax.plot([xs0, xs0 + r["s_top"] * 0.5], [ytop, ytop], color=BLUE, lw=1.2)
    ax.plot([xs0, xs0 + r["s_bot"] * 0.5], [0, 0], color=RED, lw=1.2)
    ax.plot([xs0, xs0], [0, ytop], color=GREY, lw=0.8)
    ax.text(xs0 + r["s_top"] * 0.5 - 4, ytop + 4, f"{r['s_top']:.1f} (C)", fontsize=8, color=BLUE, ha="right")
    ax.text(xs0 + r["s_bot"] * 0.5 + 2, 4, f"+{r['s_bot']:.1f} (T)", fontsize=8, color=RED)
    ax.set_xlim(-130, 100)
    ax.set_ylim(-10, 140)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Q3: T-section, $M=8$ kN·m sagging (MPa)", fontsize=9)
    # I-section shear
    r4 = C.p2_n4()
    ax = axs[1]
    bf, tf, tw, hw = 100.0, 12.0, 10.0, 150.0
    H = hw + 2 * tf
    ax.add_patch(Rectangle((-bf / 2, hw / 2), bf, tf, color="#cfe0f7", ec=INK))
    ax.add_patch(Rectangle((-bf / 2, -hw / 2 - tf), bf, tf, color="#cfe0f7", ec=INK))
    ax.add_patch(Rectangle((-tw / 2, -hw / 2), tw, hw, color="#cfe0f7", ec=INK))
    y = np.linspace(-hw / 2, hw / 2, 200)
    Qf = r4["Qflange"]
    I = r4["I"]
    Qy = Qf + tw * ((hw / 2)**2 - y**2) / 2
    tau = 60e3 * Qy / (I * tw)
    k = 1.0
    ax.plot(60 + tau * k, y, color=ORANGE, lw=2)
    ax.plot([60, 60], [-hw / 2, hw / 2], color=GREY, lw=0.8)
    ax.fill_betweenx(y, 60, 60 + tau * k, color=ORANGE, alpha=0.25)
    # flange portion (small)
    tf_j = r4["tau_j_fl"]
    for sgn in (1, -1):
        yy = sgn * hw / 2
        ax.plot([60, 60 + tf_j * k], [yy, yy], color=ORANGE, lw=1.4)
    ax.text(60 + tau.max() * k + 2, 0, f"{r4['tau_na']:.1f}", color=ORANGE, fontsize=8.5, va="center")
    ax.text(60 + r4["tau_j_web"] * k + 3, hw / 2 - 5, f"{r4['tau_j_web']:.1f}", color=ORANGE, fontsize=8.5)
    ax.text(60 + 0.5, hw / 2 + 12, f"{r4['tau_j_fl']:.2f}", color=ORANGE, fontsize=8.5)
    ax.set_xlim(-70, 150)
    ax.set_ylim(-95, 95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Q4: I-section, $V=60$ kN: $\\tau$ (MPa)", fontsize=9)
    # eccentric column
    r8 = C.p2_n8()
    ax = axs[2]
    b, h = 150.0, 200.0
    ax.add_patch(Rectangle((-h / 2, -b / 2), h, b, color="#cfe0f7", ec=INK))
    ax.plot([40], [0], "o", color=RED, ms=6)
    ax.text(40, 10, "P, e=40", color=RED, fontsize=8.5, ha="center")
    yna = r8["y_na"]
    ax.plot([yna, yna], [-b / 2 - 8, b / 2 + 8], color=GREEN, lw=1.4, ls="--")
    ax.text(yna + 3, -b / 2 - 22, "NA", color=GREEN, fontsize=8.5)
    ax.fill_betweenx([-b / 2, b / 2], yna, h / 2, color=RED, alpha=0.25)
    ax.text(88, 0, "tension\n16.7 mm", fontsize=8, ha="center", color=RED, va="center")
    ax.text(-30, -b / 2 - 22, "compression", fontsize=8.5, color=BLUE)
    ax.set_xlim(-130, 130)
    ax.set_ylim(-110, 100)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Q8: eccentric load beyond the kern ($e>h/6$)", fontsize=9)
    fig.tight_layout()
    save(fig, "SM-QB-2c-sections.png")


def qb3_mohr():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.2))
    # N1
    sx, sy, txy = 80.0, -40.0, 30.0
    c, R, s1, s2, thp = C.principal(sx, sy, txy)
    ax = axs[0]
    t = np.linspace(0, 2 * pi, 400)
    ax.plot(c + R * np.cos(t), R * np.sin(t), color=BLUE, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(0, color=GREY, lw=0.8)
    ax.plot([sx, sy], [-txy, txy], "o-", color=RED, lw=1.4)
    ax.text(sx + 2, -txy - 9, "X (80, 30)", color=RED, fontsize=8.5)
    ax.text(sy - 5, txy + 12, "Y (−40, −30)", color=RED, fontsize=8.5, ha="center")
    sn, sn90, tn = C.transform(sx, sy, txy, 30)
    # plane at 30 deg ccw: point is at angle 60 deg on circle from X (ccw rotates +2 theta, plotted with tau down -> clockwise on screen? we compute from numbers)
    ax.plot([sn], [-tn], "s", color=ORANGE, ms=7)
    ax.plot([sn90], [tn], "s", color=ORANGE, ms=7)
    ax.plot([sn, sn90], [-tn, tn], "--", color=ORANGE)
    ax.text(sn + 2, -tn + 12, f"30°: ({sn:.1f}, {tn:.1f})", color=ORANGE, fontsize=8.5)
    ax.text(sn90 - 2, tn - 8, f"120°: ({sn90:.1f}, {-tn:.1f})", color=ORANGE, fontsize=8.5, ha="center")
    ax.plot([s1, s2], [0, 0], "s", color=GREEN, ms=6)
    ax.text(s1, 9, f"$\\sigma_1$={s1:.1f}", color=GREEN, ha="center", fontsize=9)
    ax.text(s2, 9, f"$\\sigma_2$={s2:.1f}", color=GREEN, ha="center", fontsize=9)
    ax.plot([c, c], [-R, R], ":", color=GREY)
    ax.text(c + 2, R + 6, f"$\\tau_{{max}}$={R:.1f}", fontsize=9, color=INK)
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.set_xlim(-70, 110)
    ax.set_xlabel("$\\sigma$ (MPa)")
    ax.set_ylabel("$\\tau$ (MPa), clockwise-positive downwards")
    ax.set_title("Q1: plane stress state, circle", fontsize=9.5)
    # rosette strain circle (micro)
    r = C.p3_n3()
    ax = axs[1]
    c_, R_ = r["c"] * 1e6, r["R"] * 1e6
    ex, ey, g = r["ex"] * 1e6, r["ey"] * 1e6, r["gxy"] * 1e6
    ax.plot(c_ + R_ * np.cos(t), R_ * np.sin(t), color=BLUE, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(0, color=GREY, lw=0.8)
    ax.plot([ex, ey], [-g / 2, g / 2], "o-", color=RED, lw=1.4)
    ax.text(ex + 15, -g / 2 - 40, f"X ({ex:.0f}, {g/2:.0f})", color=RED, fontsize=8.5)
    ax.text(ey + 20, g / 2 + 70, f"Y ({ey:.0f}, {-g/2:.0f})", color=RED, fontsize=8.5, ha="left")
    ax.plot([c_ + R_, c_ - R_], [0, 0], "s", color=GREEN, ms=6)
    ax.text(c_ + R_, 40, f"$\\varepsilon_1$={c_+R_:.0f}", color=GREEN, ha="center", fontsize=9)
    ax.text(c_ - R_, 40, f"$\\varepsilon_2$={c_-R_:.0f}", color=GREEN, ha="center", fontsize=9)
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.set_xlim(-300, 780)
    ax.set_xlabel("$\\varepsilon$ ($\\mu\\varepsilon$)")
    ax.set_ylabel("$\\gamma/2$ ($\\mu\\varepsilon$)")
    ax.set_title("Q3: strain circle from a 0°/45°/90° rosette", fontsize=9.5)
    fig.tight_layout()
    save(fig, "SM-QB-3-mohr.png")


def qb4_curves():
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.7))
    # N3 overhang
    P, L, a, EI = 20.0, 4.0, 1.5, 12000.0
    M0 = P * a
    xs = np.linspace(0, L + a, 2000)
    M = np.where(xs <= L, -M0 * xs / L, -P * (L + a - xs))
    th = np.concatenate([[0], np.cumsum((M[1:] + M[:-1]) / 2 * np.diff(xs))]) / EI
    v = np.concatenate([[0], np.cumsum((th[1:] + th[:-1]) / 2 * np.diff(xs))])
    iL = np.argmin(abs(xs - L))
    v = v - v[iL] * xs / L
    ax = axs[0]
    ax.plot(xs, -v * 1e3, color=BLUE, lw=2)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.plot([0, L], [0, 0], "^", color=GREY, ms=8)
    ax.plot([L + a], [-v[-1] * 1e3], "o", color=RED)
    ax.text(L + a - 0.15, -v[-1] * 1e3 - 0.6, f"{-v[-1]*1e3:.2f} mm down", ha="right", va="bottom", fontsize=8.5, color=RED)
    ax.annotate("2.50 mm up at mid-span", (2.0, -2.5), xytext=(1.0, 2.2), fontsize=8.5, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE))
    ax.set_ylabel("deflection (mm, down positive)")
    ax.set_xlabel("x (m)")
    ax.invert_yaxis()
    ax.set_title("Q3: overhang, 20 kN at the tip", fontsize=9.5)
    # N5 Macaulay
    r = C.p4_n5()
    RA = r["RA"]
    L, EI = 8.0, 40000.0
    xs = np.linspace(0, L, 1600)
    C1 = r["C1"]
    vm = np.array([(RA * x**3 / 6 - 30 * max(x - 3, 0)**3 / 6 - 10 * max(x - 5, 0)**4 / 24 + C1 * x) / EI for x in xs])
    ax = axs[1]
    ax.plot(xs, -vm * 1e3, color=BLUE, lw=2)
    ax.plot([0, L], [0, 0], "^", color=GREY, ms=8)
    ax.invert_yaxis()
    ax.plot([r["xmax"]], [-r["vmax"]], "o", color=RED)
    ax.text(r["xmax"] - 0.2, -r["vmax"] - 1.5, f"max {-r['vmax']:.2f} mm\nat x = {r['xmax']:.2f} m", ha="center", va="bottom", fontsize=8.5, color=RED)
    ax.axvline(3, color=GREY, lw=0.6, ls=":")
    ax.axvspan(5, 8, color=ORANGE, alpha=0.12)
    ax.set_xlabel("x (m)")
    ax.set_title("Q5: 30 kN at 3 m, UDL on 5–8 m", fontsize=9.5)
    # secant
    r = C.p4_n10()
    E, b, h, Lc, e = 200e3, 100.0, 60.0, 2400.0, 6.0
    A, I = b * h, b * h**3 / 12
    r2 = I / A
    c = h / 2
    Pe = pi**2 * E * I / Lc**2
    P = np.linspace(1e3, 0.99 * Pe, 500)
    smax = P / A * (1 + e * c / r2 / np.cos(Lc / (2 * sqrt(r2)) * np.sqrt(P / (E * A))))
    lin = P / A * (1 + e * c / r2)
    ax = axs[2]
    ax.plot(P / 1e3, smax, color=BLUE, lw=2, label="secant (with deflection)")
    ax.plot(P / 1e3, lin, color=GREY, lw=1.2, ls="--", label="$P/A\\,(1+ec/r^2)$ only")
    ax.axhline(250, color=RED, lw=1, ls=":")
    ax.text(5, 258, "$\\sigma_Y=250$", color=RED, fontsize=8.5)
    ax.plot([r["P_secant"]], [250], "o", color=RED)
    ax.annotate(f"{r['P_secant']:.0f} kN", (r["P_secant"], 250), xytext=(r["P_secant"] - 160, 170), fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    ax.axvline(Pe / 1e3, color=GREEN, lw=1, ls=":")
    ax.text(Pe / 1e3 - 6, 40, f"$P_E$={Pe/1e3:.0f}", color=GREEN, fontsize=8.5, ha="right", rotation=90)
    ax.set_ylim(0, 420)
    ax.set_xlabel("axial load P (kN)")
    ax.set_ylabel("max stress (MPa)")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_title("Q10: eccentric column, secant formula", fontsize=9.5)
    fig.tight_layout()
    save(fig, "SM-QB-4-curves.png")


if __name__ == "__main__":
    fb_stress_strain()
    fb_mohr()
    fb_beam_cases()
    fb_columns()
    fp_failure_planes()
    qb1_n1_n2()
    qb2_beams()
    qb2_sections()
    qb3_mohr()
    qb4_curves()
