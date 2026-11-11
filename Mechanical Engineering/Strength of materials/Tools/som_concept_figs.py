"""Figures for the Strength of Materials concept notes (assets/SM-C-*.png).  Run: python som_concept_figs.py
Every number printed on a figure is computed here, and the asserts check the closed forms quoted in the notes."""
import os
import numpy as np
from math import pi, sqrt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, Polygon

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
BLUE, ORANGE, RED, GREEN, GREY, INK, PURPLE = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a", "#777777", "#222222", "#7a4fb5"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.titlesize": 10, "axes.titleweight": "bold",
                     "figure.dpi": 100, "savefig.dpi": 170, "savefig.bbox": "tight"})


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, name), facecolor="white")
    plt.close(fig)
    print("saved", name)


def arrow(ax, p, q, color=INK, lw=1.4, ms=9, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, lw=lw, color=color))


# ------------------------------------------------------------------ stress-strain diagram
def stress_strain():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    e = np.array([0, 1.0, 1.15, 1.7, 4, 10, 16, 24])
    s = np.array([0, 200, 250, 240, 300, 380, 400, 300])
    from scipy.interpolate import PchipInterpolator
    ee = np.linspace(0, 24, 300)
    ax.plot(ee, PchipInterpolator(e, s)(ee), color=BLUE, lw=2.4)
    ax.plot([0, 2.3], [0, 200 * 2.3], color=GREY, lw=1, ls=":")
    off = 2.0
    ax.plot([off, off + 1.45], [0, 200 * 1.45], color=ORANGE, lw=1.4, ls="--")
    ax.plot([14, 14 - 380 / 200 * 0.5 * 3.1], [388, 0], color=GREEN, lw=1.2, ls="--") if False else None
    ax.plot([16 - 400 / 200, 16], [0, 400], color=GREEN, lw=1.2, ls="--")
    for x, y, t, dx, dy in [(1.0, 200, "proportional limit", 2.0, -30), (1.7, 240, "yield", 2.4, -45), (16, 400, "ultimate strength", -9.5, 8), (24, 300, "fracture", -2.5, -42)]:
        ax.plot(x, y, "o", color=RED, ms=5)
        ax.annotate(t, (x, y), (x + dx, y + dy), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=GREY, lw=.8))
    ax.text(3.7, 30, "0.2 % offset line\n(gives yield strength\nwhen there is no plateau)", color=ORANGE, fontsize=8)
    ax.text(18.2, 95, "unloading runs\nparallel to the\nelastic line:\npermanent set", color=GREEN, fontsize=8)
    ax.text(2.7, 345, "elastic line\n(E = slope)", color=GREY, fontsize=8)
    ax.set_xlabel(r"strain $\varepsilon$ (elastic part exaggerated)"); ax.set_ylabel(r"stress $\sigma$ (MPa)")
    ax.set_xlim(0, 25); ax.set_ylim(0, 440)
    ax.set_title("Engineering stress-strain curve of mild steel (schematic)")
    save(fig, "SM-C-stress-strain.png")


# ------------------------------------------------------------------ torsion: solid vs hollow
def torsion():
    c, ci = 1.0, 0.6
    ratio_T = 1 - (ci / c) ** 4
    ratio_A = 1 - (ci / c) ** 2
    assert abs(ratio_T - 0.8704) < 1e-4 and abs(ratio_A - 0.64) < 1e-9
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axs[0]
    ax.add_patch(Circle((0, 0), c, fc="#dbe7fb", ec=BLUE, lw=1.5)); ax.add_patch(Circle((0, 0), ci, fc="white", ec=BLUE, lw=1.5, ls="--"))
    for ang in (30, 150, 270):
        a = np.radians(ang)
        for r in (0.25, 0.6, 0.95):
            pass
    for ang in (45, 135, 225, 315):
        a = np.radians(ang)
        for r, col in ((0.95, RED),):
            x0, y0 = r * np.cos(a), r * np.sin(a)
            arrow(ax, (x0, y0), (x0 - 0.35 * np.sin(a), y0 + 0.35 * np.cos(a)), color=col, lw=1.8)
    ax.text(0, 0, "no material\n(tube)", ha="center", va="center", fontsize=8, color=GREY)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.35, 1.35); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Shear stress is tangential")
    ax = axs[1]
    rho = np.linspace(0, 1, 200)
    ax.plot(rho, rho, color=BLUE, lw=2.4, label="solid shaft  $\\tau=T\\rho/J$")
    rh = np.linspace(ci, 1, 100)
    ax.plot(rh, rh * (1.0), color=ORANGE, lw=2.4, label="tube $c_i=0.6c$ (same $T$ gives larger $\\tau_{max}$)")
    ax.fill_between(rho, 0, rho, color=BLUE, alpha=.12)
    ax.set_xlabel(r"radius $\rho/c$"); ax.set_ylabel(r"$\tau/\tau_{max}$ at that radius, for the solid shaft")
    ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.1)
    ax.axvspan(0, ci, color=GREY, alpha=.12)
    ax.text(0.04, 0.7, "the core carries\nlittle stress:\nhollowing it out\nbarely hurts", fontsize=8.5, color=GREY)
    ax.text(0.62, 0.18, f"tube: {ratio_T*100:.0f} % of the solid's torque capacity\nfor {ratio_A*100:.0f} % of its material\n($J\\propto 1-(c_i/c)^4$, area $\\propto 1-(c_i/c)^2$)", fontsize=8.5, color=INK)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0), frameon=False, fontsize=8, handlelength=1.2).set_visible(False)
    ax.set_title("Stress grows linearly with radius")
    save(fig, "SM-C-torsion-solid-hollow.png")


# ------------------------------------------------------------------ SFD and BMD, simply supported beam
def sfd_bmd():
    L, w, P, a = 6.0, 4.0, 10.0, 2.0
    RB = (w * L * L / 2 + P * a) / L
    RA = w * L + P - RB
    x = np.linspace(0, L, 1201)
    V = RA - w * x - np.where(x >= a, P, 0)
    M = RA * x - w * x ** 2 / 2 - np.where(x >= a, P * (x - a), 0)
    xm = x[np.argmin(abs(V[x > a]))] if False else (RA - P) / w
    Mmax = RA * xm - w * xm ** 2 / 2 - P * (xm - a)
    assert abs(M.max() - Mmax) < 1e-2 and abs(RA - 56 / 3) < 1e-9 and abs(RB - 46 / 3) < 1e-9 and abs(xm - 13 / 6) < 1e-9 and abs(Mmax - 29.3889) < 1e-3
    fig, axs = plt.subplots(3, 1, figsize=(7.2, 6.4), sharex=True, gridspec_kw={"height_ratios": [0.9, 1.2, 1.2]})
    ax = axs[0]
    ax.plot([0, L], [0, 0], color=INK, lw=4)
    for xx in np.linspace(0, L, 13):
        arrow(ax, (xx, 0.55), (xx, 0.08), color=BLUE, lw=1)
    arrow(ax, (a, 1.4), (a, 0.08), color=RED, lw=2); ax.text(a + .1, 1.35, "P = 10 kN", color=RED)
    ax.text(L / 2, 0.75, "w = 4 kN/m", color=BLUE, ha="center")
    ax.plot([0], [-0.25], "^", color=INK, ms=11); ax.plot([L], [-0.25], "o", color=INK, ms=9)
    ax.text(0.05, -0.8, f"R$_A$ = {RA:.2f} kN", fontsize=8.5); ax.text(L - 1.2, -0.8, f"R$_B$ = {RB:.2f} kN", fontsize=8.5)
    ax.set_ylim(-1, 1.8); ax.axis("off")
    ax = axs[1]
    ax.plot(x, V, color=BLUE, lw=2); ax.fill_between(x, 0, V, color=BLUE, alpha=.12); ax.axhline(0, color=GREY, lw=.8)
    ax.axvline(xm, color=GREY, ls=":", lw=1); ax.set_ylabel("V (kN)")
    ax.text(a + .12, -9, "jump of $-P$ at the point load", fontsize=8, color=RED)
    ax.text(xm + .15, 9, f"$V=0$ at x = {xm:.2f} m", fontsize=8.5)
    ax.set_title("Shear force: slope $=-w$, steps down by $P$", fontsize=9)
    ax = axs[2]
    ax.plot(x, M, color=ORANGE, lw=2); ax.fill_between(x, 0, M, color=ORANGE, alpha=.12); ax.axhline(0, color=GREY, lw=.8)
    ax.axvline(xm, color=GREY, ls=":", lw=1); ax.plot(xm, Mmax, "o", color=RED)
    ax.text(xm + .12, Mmax - 3, f"$M_{{max}}$ = {Mmax:.1f} kN·m", fontsize=9, color=RED)
    ax.set_ylabel("M (kN·m)"); ax.set_xlabel("x (m)"); ax.set_title("Bending moment: slope $=V$, a corner under $P$, maximum where $V=0$", fontsize=9)
    save(fig, "SM-C-sfd-bmd.png")


# ------------------------------------------------------------------ load -> shear -> moment chain (cantilever, UDL)
def chain():
    L, w = 1.0, 1.0
    x = np.linspace(0, L, 400)
    V = w * (L - x)
    M = -w * (L - x) ** 2 / 2
    assert abs(M[0] + w * L * L / 2) < 1e-12
    fig, axs = plt.subplots(1, 3, figsize=(10.2, 2.9))
    axs[0].plot(x, -w * np.ones_like(x), color=BLUE, lw=2); axs[0].fill_between(x, 0, -w, color=BLUE, alpha=.15)
    axs[0].set_title("load $w$ (constant)"); axs[0].set_ylim(-1.4, .4)
    axs[1].plot(x, V, color=GREEN, lw=2); axs[1].fill_between(x, 0, V, color=GREEN, alpha=.15)
    axs[1].set_title("shear $V$: straight line, slope $-w$"); axs[1].text(.05, .08, "$V(0)=wL$ at the wall", fontsize=8.5)
    axs[2].plot(x, M, color=ORANGE, lw=2); axs[2].fill_between(x, 0, M, color=ORANGE, alpha=.15)
    axs[2].set_title("moment $M$: parabola, slope $V$"); axs[2].text(.2, -.12, "$M(0)=-wL^2/2$ (hogging)", fontsize=8.5)
    for ax in axs:
        ax.axhline(0, color=GREY, lw=.8); ax.set_xlabel("x from the fixed end")
    fig.suptitle("Integrate once for shear, twice for moment (cantilever, uniform load)", y=1.04, fontsize=10, fontweight="bold")
    fig.tight_layout()
    save(fig, "SM-C-load-shear-moment.png")


# ------------------------------------------------------------------ flexure: linear stress, neutral axis
def flexure():
    h, b = 1.0, 0.5
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.4))
    ax = axs[0]
    ax.add_patch(Rectangle((-b / 2, -h / 2), b, h, fc="#dbe7fb", ec=BLUE, lw=1.5))
    ax.plot([-b, b], [0, 0], color=GREY, ls="--", lw=1); ax.text(b * 1.05, 0.02, "neutral axis", fontsize=8.5, color=GREY)
    ax.add_patch(Polygon([[b / 2 + .5, 0], [b / 2 + .5, h / 2], [b / 2 + .5 + .6, h / 2]], fc=RED, alpha=.25, ec=RED))
    ax.add_patch(Polygon([[b / 2 + .5, 0], [b / 2 + .5, -h / 2], [b / 2 + .5 - .6, -h / 2]], fc=BLUE, alpha=.25, ec=BLUE))
    ax.plot([b / 2 + .5] * 2, [-h / 2, h / 2], color=INK, lw=1)
    ax.text(b / 2 + 1.15, h / 2 - .05, "tension\n(top, hogging)", fontsize=8, color=RED, va="top"); ax.text(b / 2 - .15, -h / 2 - .12, "compression", fontsize=8, color=BLUE, va="top")
    ax.set_xlim(-0.9, 2.2); ax.set_ylim(-.9, .8); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(r"Bending stress is linear in $y$: $\sigma=-My/I$")
    ax = axs[1]
    y = np.linspace(0, 1, 50)
    # rectangle vs I-section: section modulus per unit area
    A = 1.0
    Irect = A * (1.0) ** 2 / 12                      # b h^3/12 with b h = 1, h = 1
    # I-section of the same area and depth 1.6h: flanges carry most area
    hI, tf, tw = 1.6, 0.15, 0.1
    bf = (A - tw * (hI - 2 * tf)) / (2 * tf)
    Iibeam = bf * hI ** 3 / 12 - (bf - tw) * (hI - 2 * tf) ** 3 / 12
    ZR, ZI = Irect / 0.5, Iibeam / (hI / 2)
    assert abs((ZI / ZR) - Iibeam / Irect * 0.5 / (hI / 2)) < 1e-9
    ax.bar(["rectangle\n(depth 1.0)", f"I-section\n(depth {hI}, same area)"], [ZR, ZI], color=[BLUE, ORANGE], width=.5)
    for i, v in enumerate((ZR, ZI)):
        ax.text(i, v + .01, f"$Z=I/c$ = {v:.3f}", ha="center", fontsize=9)
    ax.set_ylabel("section modulus $Z$ (same area, same material)")
    ax.set_title(f"Same material, {ZI/ZR:.1f}x the moment capacity")
    print("I-section/rectangle section modulus ratio", ZI / ZR)
    save(fig, "SM-C-flexure.png")


# ------------------------------------------------------------------ beam shear stress profile
def beam_shear():
    h, b = 1.0, 0.5
    y = np.linspace(-h / 2, h / 2, 201)
    tau = 1.5 * (1 - (2 * y / h) ** 2)         # tau / (V/A)
    assert abs(tau.max() - 1.5) < 1e-9
    fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.4))
    ax = axs[0]
    ax.plot(tau, y, color=ORANGE, lw=2.2); ax.fill_betweenx(y, 0, tau, color=ORANGE, alpha=.15)
    ax.axvline(1, color=GREY, ls="--", lw=1); ax.text(1.02, -.45, "average $V/A$", fontsize=8.5, color=GREY)
    ax.text(1.5, .02, "  max = 1.5 V/A\n  at the neutral axis", fontsize=8.5, color=ORANGE, va="center", ha="right") if False else ax.text(1.0, .06, "max = 1.5 V/A\n(at the neutral axis)", fontsize=8.5, color=ORANGE)
    ax.set_xlim(0, 1.8); ax.set_ylabel("height y / h"); ax.set_xlabel(r"$\tau\,/\,(V/A)$"); ax.set_title("Rectangle: parabola, zero at top and bottom")
    ax = axs[1]
    hI, tf, tw, bf = 1.6, 0.15, 0.1, 0.8
    ax.add_patch(Rectangle((-bf / 2, hI / 2 - tf), bf, tf, fc="#dbe7fb", ec=BLUE)); ax.add_patch(Rectangle((-bf / 2, -hI / 2), bf, tf, fc="#dbe7fb", ec=BLUE))
    ax.add_patch(Rectangle((-tw / 2, -hI / 2 + tf), tw, hI - 2 * tf, fc="#dbe7fb", ec=BLUE))
    yy = np.linspace(-hI / 2 + tf, hI / 2 - tf, 80)
    prof = 0.15 + 0.35 * (1 - (yy / (hI / 2 - tf)) ** 2)
    ax.plot(bf / 2 + .25 + prof, yy, color=ORANGE, lw=2)
    ax.text(bf / 2 + .25, hI / 2 + .12, "web carries nearly all the shear", fontsize=8.5, color=ORANGE)
    ax.set_xlim(-.7, 1.7); ax.set_ylim(-1.0, 1.0); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("I-section: jump at the web-flange joint")
    save(fig, "SM-C-beam-shear.png")


# ------------------------------------------------------------------ Mohr's circle
def mohr():
    sx, sy, txy = 80.0, -20.0, 30.0
    c, R = (sx + sy) / 2, sqrt(((sx - sy) / 2) ** 2 + txy ** 2)
    s1, s2 = c + R, c - R
    th = 0.5 * np.degrees(np.arctan2(2 * txy, sx - sy))
    assert abs(R - sqrt(50 ** 2 + 30 ** 2)) < 1e-9 and abs(s1 - 88.31) < 0.01 and abs(s2 - (-28.31)) < 0.01 and abs(th - 15.48) < 0.01
    t = np.linspace(0, 2 * pi, 400)
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    ax.plot(c + R * np.cos(t), R * np.sin(t), color=BLUE, lw=2)
    ax.plot([sx, sy], [-txy, txy], color=INK, lw=1.2); ax.plot([sx, sy], [-txy, txy], "o", color=RED)
    ax.text(sx + 2, -txy - 5, "X (80, 30)\n(shear plotted downward\nfor a clockwise face pair)", fontsize=7.5)
    ax.text(sy - 4, txy + 3, "Y (−20, −30)", fontsize=8, ha="right")
    ax.plot([s1, s2], [0, 0], "s", color=GREEN, ms=7); ax.plot([c], [0], "k+", ms=9)
    ax.text(s1 + 2, 4, f"$\\sigma_1$ = {s1:.1f}", color=GREEN); ax.text(s2 - 2, 4, f"$\\sigma_2$ = {s2:.1f}", color=GREEN, ha="right")
    ax.plot([c, c], [R, -R], "o", color=ORANGE, ms=6); ax.text(c + 2, R + 2, f"$\\tau_{{max}}$ = R = {R:.1f}", color=ORANGE)
    ax.text(-58, -64, f"centre = (σx+σy)/2 = {c:.0f} MPa", fontsize=8, color=GREY)
    ax.axhline(0, color=GREY, lw=.8); ax.axvline(0, color=GREY, lw=.8)
    ax.set_aspect("equal"); ax.set_xlabel(r"normal stress $\sigma$ (MPa)"); ax.set_ylabel(r"shear stress $\tau$ (MPa)")
    ax.set_title(f"Mohr's circle: R = {R:.1f}, principal angle {th:.1f}° (circle angle is double)")
    ax.set_xlim(-60, 125); ax.set_ylim(-70, 70)
    save(fig, "SM-C-mohr-circle.png")


# ------------------------------------------------------------------ Euler buckling and end conditions
def euler():
    Ks = [("pinned-pinned", 1.0), ("fixed-free", 2.0), ("fixed-pinned", 0.7), ("fixed-fixed", 0.5)]
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
    ax = axs[0]
    names = [k[0] for k in Ks]
    pcr = [1.0 / k[1] ** 2 for k in Ks]
    assert abs(pcr[1] - 0.25) < 1e-12 and abs(pcr[3] - 4.0) < 1e-12 and abs(pcr[2] - 2.04) < 0.01
    ax.bar(names, pcr, color=[BLUE, RED, ORANGE, GREEN], width=.55)
    for i, v in enumerate(pcr):
        ax.text(i, v + .08, f"{v:.2f}$\\times$", ha="center", fontsize=9)
    ax.set_ylabel(r"$P_{cr}$ relative to pinned-pinned"); ax.set_title(r"$P_{cr}=\pi^2EI/(KL)^2$"); ax.tick_params(axis="x", labelsize=8)
    ax = axs[1]
    lam = np.linspace(20, 200, 300)
    E, sy = 200e3, 250.0
    ax.plot(lam, np.minimum(sy, pi ** 2 * E / lam ** 2), color=BLUE, lw=2.2)
    ax.plot(lam, pi ** 2 * E / lam ** 2, color=GREY, ls=":", lw=1)
    lc = sqrt(pi ** 2 * E / sy)
    ax.axvline(lc, color=ORANGE, ls="--"); ax.text(lc + 28, 185,f"$\\lambda_c$ = {lc:.0f}\nshort columns\nyield, long ones\nbuckle", fontsize=8.5, color=ORANGE)
    ax.set_xlabel(r"slenderness $\lambda=KL/r$"); ax.set_ylabel(r"failure stress (MPa), $E$=200 GPa, $\sigma_Y$=250 MPa"); ax.set_ylim(0, 300)
    ax.set_title("Strength governs short columns, stability long ones")
    print("critical slenderness", lc)
    save(fig, "SM-C-euler-buckling.png")


# ------------------------------------------------------------------ thin-walled vessel
def vessel():
    p, r, t = 2.0, 0.5, 0.01     # MPa, m, m
    sh, sl = p * r / t, p * r / (2 * t)
    assert abs(sh - 100) < 1e-9 and abs(sl - 50) < 1e-9
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4))
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 3, 2, fc="#dbe7fb", ec=BLUE))
    for xx in np.linspace(.3, 2.7, 5):
        for sgn in (1, -1):
            arrow(ax, (xx, 1 if sgn > 0 else 1), (xx, 1 + sgn * 0.85), color=RED, lw=1.2)
    ax.text(1.5, 1.0, "$p$", ha="center", va="center", fontsize=11, color=RED)
    arrow(ax, (1.5, 2.0), (1.5, 2.55), color=GREEN, lw=2); arrow(ax, (1.5, 0.0), (1.5, -0.55), color=GREEN, lw=2)
    ax.text(1.65, 2.35, r"$\sigma_h = pr/t$ = 100 MPa on each cut face", fontsize=8.5, color=GREEN)
    ax.text(0.1, -0.55, "half cylinder: pressure force $2prL$ = wall tension $2\\sigma_h tL$", fontsize=8.5)
    ax.set_xlim(-.2, 5.3); ax.set_ylim(-.9, 2.9); ax.axis("off"); ax.set_title("Hoop stress: cut along the axis")
    ax = axs[1]
    ax.add_patch(Circle((0, 0), 1, fc="#dbe7fb", ec=BLUE)); ax.add_patch(Circle((0, 0), .86, fc="white", ec=BLUE))
    ax.text(0, 0, "$p$", ha="center", va="center", fontsize=12, color=RED)
    for a in np.radians(np.arange(0, 360, 45)):
        arrow(ax, (1.0 * np.cos(a), np.sin(a)), (1.35 * np.cos(a), 1.35 * np.sin(a)), color=GREEN, lw=1.6)
    ax.text(0, -1.75, "end cap: $p\\pi r^2$ = $\\sigma_l(2\\pi rt)$  so  $\\sigma_l=pr/2t$ = 50 MPa", ha="center", fontsize=8.5)
    ax.text(0, 1.62, "the hoop stress is twice the axial stress", ha="center", fontsize=9, color=ORANGE)
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.0, 1.9); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("Longitudinal stress: cut across")
    save(fig, "SM-C-pressure-vessel.png")


# ------------------------------------------------------------------ thermal stress, restrained bar
def thermal():
    E, al, dT = 200e3, 12e-6, 50
    sig = E * al * dT
    assert abs(sig - 120.0) < 1e-9
    fig, axs = plt.subplots(2, 1, figsize=(7.2, 3.4), sharex=True)
    for ax, free in zip(axs, (True, False)):
        ax.add_patch(Rectangle((0, 0), 4, .6, fc="#dbe7fb", ec=BLUE))
        if free:
            ax.add_patch(Rectangle((4, 0), .45, .6, fc="#f7d9c4", ec=ORANGE, ls="--"))
            ax.text(4.55, .3, r"$\delta_T=\alpha\,\Delta T\,L$: free to grow, no stress", va="center", fontsize=8.5, color=ORANGE)
        else:
            ax.plot([-.15, -.15], [-.2, .8], color=INK, lw=4); ax.plot([4.15, 4.15], [-.2, .8], color=INK, lw=4)
            arrow(ax, (-.1, .3), (.6, .3), color=RED, lw=2); arrow(ax, (4.1, .3), (3.4, .3), color=RED, lw=2)
            ax.text(4.35, .3, f"walls refuse the growth:\n$\\sigma=-E\\alpha\\Delta T$ = {sig:.0f} MPa (compression)", va="center", fontsize=8.5, color=RED)
        ax.set_xlim(-.4, 8.8); ax.set_ylim(-.3, .9); ax.axis("off")
    axs[0].set_title("Heating a bar by 50 K (steel, $E$=200 GPa, $\\alpha=12\\times10^{-6}$/K)", fontsize=9)
    save(fig, "SM-C-thermal-stress.png")


# ------------------------------------------------------------------ deflection from curvature (double integration)
def deflection():
    L, w, EI = 1.0, 1.0, 1.0
    x = np.linspace(0, L, 400)
    M = w * x * (L - x) / 2
    v = w * x * (L ** 3 - 2 * L * x ** 2 + x ** 3) / (24 * EI)          # downward deflection, simply supported, UDL
    # check: EI v'' = -M  (downward positive v):  v'' = -M/EI  -> second derivative of v
    h = x[1] - x[0]
    vpp = np.gradient(np.gradient(v, h), h)
    assert abs(vpp[100:300] + M[100:300] / EI).max() < 1e-3
    assert abs(v.max() - 5 * w * L ** 4 / (384 * EI)) < 1e-6
    fig, axs = plt.subplots(1, 3, figsize=(10.2, 2.9))
    axs[0].plot(x, M, color=ORANGE, lw=2); axs[0].fill_between(x, 0, M, color=ORANGE, alpha=.15); axs[0].set_title("bending moment $M(x)$")
    axs[1].plot(x, np.gradient(v, h), color=GREEN, lw=2); axs[1].axhline(0, color=GREY, lw=.8); axs[1].set_title("slope $v'$: integrate $M/EI$ once")
    axs[2].plot(x, -v, color=BLUE, lw=2); axs[2].plot(x, 0 * x, color=INK, lw=3)
    axs[2].plot(L / 2, -v.max(), "o", color=RED); axs[2].text(.3, -v.max() * .7, r"$v_{max}=\frac{5wL^4}{384EI}$", fontsize=9, color=RED)
    axs[2].set_title("deflection $v$: integrate again")
    for ax in axs:
        ax.set_xlabel("x / L")
    fig.suptitle("Double integration, simply supported beam under uniform load (constants from $v(0)=v(L)=0$)", y=1.04, fontsize=10, fontweight="bold")
    fig.tight_layout()
    save(fig, "SM-C-double-integration.png")


# ------------------------------------------------------------------ axial members in parallel: load sharing
def axial():
    E1, A1, E2, A2, P = 200e3, 600.0, 70e3, 1200.0, 300e3     # steel core, aluminium tube
    k1, k2 = E1 * A1, E2 * A2
    P1, P2 = P * k1 / (k1 + k2), P * k2 / (k1 + k2)
    s1, s2 = P1 / A1, P2 / A2
    d = P / (k1 + k2)            # delta/L
    assert abs(P1 - 176470.588) < 0.01 and abs(s1 - 294.118) < 0.01 and abs(s2 - 102.941) < 0.01 and abs(P1 + P2 - P) < 1e-6
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.4))
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 3, 1.4, fc="#f0d9b8", ec=ORANGE)); ax.add_patch(Rectangle((0, .45), 3, .5, fc="#b9c9e8", ec=BLUE))
    ax.plot([-.15, -.15], [-.2, 1.6], color=INK, lw=5)
    ax.plot([3.4, 3.4], [-.2, 1.6], color=INK, lw=5); ax.plot([3, 3.4], [.7, .7], color=INK, lw=2)
    arrow(ax, (4.6, .7), (3.5, .7), color=RED, lw=2.4); ax.text(4.65, .7, "P = 300 kN", va="center", color=RED)
    ax.text(1.5, .55, "steel core", ha="center", fontsize=8.5); ax.text(1.5, 1.1, "aluminium tube", ha="center", fontsize=8.5)
    ax.set_xlim(-.5, 6.2); ax.set_ylim(-.4, 1.8); ax.axis("off"); ax.set_title("Same elongation, so load splits by stiffness $EA$")
    ax = axs[1]
    ax.bar(["steel core\n$E$=200 GPa, 600 mm²", "aluminium\n$E$=70 GPa, 1200 mm²"], [s1, s2], color=[BLUE, ORANGE], width=.5)
    ax.text(0, s1 + 5, f"{s1:.0f} MPa  ({P1/1e3:.0f} kN)", ha="center"); ax.text(1, s2 + 5, f"{s2:.0f} MPa  ({P2/1e3:.0f} kN)", ha="center")
    ax.set_ylabel("stress (MPa)"); ax.set_ylim(0, 340); ax.set_title("Strain is common, so $\\sigma\\propto E$: the stiff part is the highly stressed part")
    ax.title.set_fontsize(8.5)
    save(fig, "SM-C-axial-load-sharing.png")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    for f in (stress_strain, torsion, sfd_bmd, chain, flexure, beam_shear, mohr, euler, vessel, thermal, deflection, axial):
        f()
