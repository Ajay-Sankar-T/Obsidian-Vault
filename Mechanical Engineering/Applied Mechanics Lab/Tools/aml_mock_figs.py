"""Figures for the lab theory notes and mock papers (assets/AML-*.png).   Run: python aml_mock_figs.py"""
import os
import numpy as np
from math import pi, sqrt, sin, cos, tan, radians, degrees, atan
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon, Arc

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, RED, GREEN, GREY, INK = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a", "#777777", "#222222"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.titlesize": 10, "axes.titleweight": "bold",
                     "savefig.dpi": 170, "savefig.bbox": "tight"})


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, name), facecolor="white")
    plt.close(fig)
    print("saved", name)


def arrow(ax, p, q, color=INK, lw=1.4, ms=9, **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color, **kw))


# ------------------------------------------------------------------ Wheatstone bridge variants
def bridges():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.9))
    T, B, L, R = (0, 1), (0, -1), (-1, 0), (1, 0)
    arms = {"R1": (T, L), "R2": (L, B), "R3": (B, R), "R4": (R, T)}

    def draw(ax, title, roles, out, note):
        ax.set_xlim(-1.9, 1.9)
        ax.set_ylim(-1.95, 1.7)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=9.5)
        for nm, (p, q) in arms.items():
            role = roles.get(nm, ("fixed", GREY, ""))
            kind, col, lab = role
            mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
            ax.plot([p[0], q[0]], [p[1], q[1]], color=col, lw=2.2 if kind == "fixed" else 3.4, solid_capstyle="round")
            ox, oy = (1 if mx > 0 else -1), (1 if my > 0 else -1)
            ax.text(mx + 0.17 * ox, my + 0.17 * oy, nm, ha="center", va="center", fontsize=8.5, color=col, fontweight="bold")
            if lab:
                ax.text(mx + 0.62 * ox, my + 0.42 * oy, lab, ha="center", va="center", fontsize=7.8, color=col)
        for (x, y), nm in [(T, "+V"), (B, "0 V")]:
            ax.plot([x], [y], "o", color=INK, ms=5)
            ax.text(x, y + (0.15 if y > 0 else -0.28), nm, ha="center", fontsize=8.5)
        for (x, y), nm in [(L, "$V_a$"), (R, "$V_b$")]:
            ax.plot([x], [y], "o", color=INK, ms=5)
            ax.text(x + (-0.16 if x < 0 else 0.16), y, nm, ha="center", va="center", fontsize=9)
        ax.annotate("", (1.0, 0.0), (-1.0, 0.0), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1, ls="--"))
        ax.text(0, 0.1, out, ha="center", fontsize=8.6, color=GREEN)
        ax.text(0, -1.78, note, ha="center", fontsize=8.2, va="top")

    gauge_t = ("active", RED, "tension\n$+\\varepsilon$")
    gauge_c = ("active", BLUE, "compression\n$-\\varepsilon$")
    dummy = ("dummy", ORANGE, "dummy\n(no strain)")
    draw(axs[0], "Quarter bridge + dummy", {"R1": gauge_t, "R2": dummy},
         "$V_o=\\dfrac{V_{ex}GF\\,\\varepsilon}{4}$", "dummy in the adjacent arm: $\\Delta R_T$ cancels")
    draw(axs[1], "Half bridge (bending)", {"R1": gauge_t, "R2": gauge_c},
         "$V_o=\\dfrac{V_{ex}GF\\,\\varepsilon}{2}$", "top and bottom gauges: twice the signal, $\\Delta R_T$ cancels")
    draw(axs[2], "Full bridge", {"R1": gauge_t, "R2": gauge_c, "R3": gauge_t, "R4": gauge_c},
         "$V_o=V_{ex}GF\\,\\varepsilon$", "four active gauges: most sensitive (load cells)")
    fig.tight_layout()
    save(fig, "AML-bridge-configs.png")


# ------------------------------------------------------------------ mirror and scale
def mirror_optics():
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    phi = radians(9.0)
    D = 6.0
    ax.set_xlim(-1.6, 7.4)
    ax.set_ylim(-1.7, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    # shaft end and mirror
    ax.add_patch(Rectangle((-1.5, -0.25), 1.5, 0.5, color="#cfe0f7", ec=INK))
    ax.text(-0.75, 0, "shaft", ha="center", va="center", fontsize=8.5)
    L = 0.8
    ax.plot([0.0 - L * sin(0) , 0.0], [0, 0], color=INK, lw=0)
    mx = np.array([-sin(phi), cos(phi)]) * L
    ax.plot([-mx[0], mx[0]], [-mx[1], mx[1]], color=INK, lw=4)
    ax.plot([0, 0], [-L, L], color=GREY, lw=1, ls=":")
    ax.text(0.1, -L - 0.2, "mirror after twist $\\phi$", fontsize=8.5)
    # incident ray
    ax.plot([-1.5, 0], [0.0, 0.0], color=RED, lw=0)    # shaft hides it; draw incident from below instead
    ax.plot([2.4, 0.0], [-1.2 * 0 + 0, 0], color=RED, lw=0)
    ax.annotate("", (0, 0), (3.2, 0), arrowprops=dict(arrowstyle="<|-", color=RED, lw=1.5))
    ax.text(3.3, 0.08, "incident ray\n(fixed direction)", color=RED, fontsize=8.5)
    # reflected ray at 2 phi
    ang = 2 * phi
    xe, ye = D * cos(ang), D * sin(ang)
    ax.annotate("", (xe, ye), (0, 0), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5))
    ax.plot([3.2, 3.2 + 0.001], [0, 0], alpha=0)
    # undeflected reference (zero twist): reflected straight back along the incident line
    ax.plot([0, D], [0, 0], color=GREY, lw=1, ls="--")
    # scale
    ax.plot([D, D], [-1.2, 2.0], color=INK, lw=2)
    for yy in np.linspace(-1.0, 1.9, 16):
        ax.plot([D - 0.08, D], [yy, yy], color=INK, lw=0.8)
    ax.text(D + 0.1, 1.9, "scale", fontsize=8.5)
    ax.annotate("", (D + 0.35, 0), (D + 0.35, ye), arrowprops=dict(arrowstyle="<->", lw=1))
    ax.text(D + 0.45, ye / 2, "$s$", fontsize=11, va="center")
    # angle arcs
    ax.add_patch(Arc((0, 0), 3.0, 3.0, theta1=0, theta2=degrees(ang), color=ORANGE, lw=1.2))
    ax.text(1.75, 0.35, "$2\\phi$", color=ORANGE, fontsize=11)
    ax.annotate("", (0, -1.5), (D, -1.5), arrowprops=dict(arrowstyle="<->", lw=1))
    ax.text(D / 2, -1.3, "$D$", ha="center", va="bottom", fontsize=11)
    ax.text(3.2, 2.2, "$\\tan2\\phi=\\dfrac{s}{D}\\ \\Rightarrow\\ \\phi=\\dfrac{1}{2}\\,\\mathrm{atan}\\,\\dfrac{s}{D}\\approx\\dfrac{s}{2D}$", fontsize=10, ha="center", va="top")
    save(fig, "AML-mirror-twist.png")


# ------------------------------------------------------------------ photoelastic fringes
def disk_field(P, D, t, X, Y):
    R = D / 2
    r1 = X**2 + (R - Y) ** 2
    r2 = X**2 + (R + Y) ** 2
    k = 2 * P / (pi * t)
    sx = -k * (X**2 * (R - Y) / r1**2 + X**2 * (R + Y) / r2**2 - 1 / D)
    sy = -k * ((R - Y) ** 3 / r1**2 + (R + Y) ** 3 / r2**2 - 1 / D)
    txy = k * (X * (R - Y) ** 2 / r1**2 - X * (R + Y) ** 2 / r2**2)
    d = np.sqrt(((sx - sy) / 2) ** 2 + txy**2) * 2        # sigma1 - sigma2
    return d


def photoelastic():
    D, t = 40.0, 6.0
    fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.9), gridspec_kw={"width_ratios": [1, 1, 1.1]})
    n = 700
    xs = np.linspace(-D / 2, D / 2, n)
    X, Y = np.meshgrid(xs, xs)
    mask = X**2 + Y**2 <= (D / 2) ** 2 * 0.997
    for ax, f, P, title in [(axs[0], 8.0, 50.0, "polycarbonate, $f_\\sigma=8$, $P=50$ N"), (axs[1], 0.2, 50.0, "polyurethane, $f_\\sigma=0.2$, $P=50$ N")]:
        d = disk_field(P, D, t, X, Y)
        N = d * t / f
        I = np.sin(pi * N) ** 2
        I = np.where(mask, I, np.nan)
        ax.imshow(I, cmap="gray", extent=(-D / 2, D / 2, -D / 2, D / 2), origin="lower", vmin=0, vmax=1)
        ax.set_title(title, fontsize=9)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        Nc = 8 * P / (pi * D * f)
        ax.text(0, -D / 2 - 2.5, f"centre fringe order $N_c=8P/(\\pi Df_\\sigma)={Nc:.2f}$", ha="center", va="top", fontsize=8.5)

    # beam in pure bending: fringe order linear in y
    ax = axs[2]
    h, Lb = 20.0, 60.0
    xs = np.linspace(0, Lb, 500)
    ys = np.linspace(-h / 2, h / 2, 400)
    X, Y = np.meshgrid(xs, ys)
    Nmax = 6.0
    N = Nmax * np.abs(Y) / (h / 2)
    I = np.sin(pi * N) ** 2
    ax.imshow(I, cmap="gray", extent=(0, Lb, -h / 2, h / 2), origin="lower", vmin=0, vmax=1, aspect="equal")
    ax.axhline(0, color=GREEN, lw=1, ls="--")
    ax.text(Lb + 1.5, 0, "neutral axis\n$N=0$", color=GREEN, fontsize=8.5, va="center")
    ax.text(Lb + 1.5, h / 2 - 1, "$N=6$", fontsize=8.5, va="top")
    ax.text(Lb + 1.5, -h / 2 + 1, "$N=6$", fontsize=8.5, va="bottom")
    ax.set_xlim(0, Lb + 22)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("pure bending: fringes parallel to the axis", fontsize=9)
    ax.text(Lb / 2, -h / 2 - 2, "$N$ is proportional to the distance from the neutral axis", ha="center", va="top", fontsize=8.5)
    save(fig, "AML-photoelastic-fringes.png")


# ------------------------------------------------------------------ deflection helpers
def beam_deflection(M_func, xs, EI, supports):
    """integrate EI v'' = M(x) (v upward) with v=0 at the two supports."""
    M = np.array([M_func(x) for x in xs])
    th = np.concatenate([[0], np.cumsum((M[1:] + M[:-1]) / 2 * np.diff(xs))]) / EI
    v = np.concatenate([[0], np.cumsum((th[1:] + th[:-1]) / 2 * np.diff(xs))])
    i1, i2 = [np.argmin(abs(xs - s)) for s in supports]
    c1 = -(v[i2] - v[i1]) / (xs[i2] - xs[i1])
    v = v + c1 * xs
    c0 = -v[i1]
    return v + c0


def real_q13():
    EI = 70e3 * 25 * 6**3 / 12
    L, W = 400.0, 24.5
    w_true = 2700 * (25 * 6e-6) * 9.81 / 1000
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.7))
    # (a) weightless overhang
    for ax, l_, wscale, title in [(axs[0], 100.0, 0.0, "weightless overhang"), (axs[1], 100.0, 40.0, "with its own weight (exaggerated $\\times$40)")]:
        w = w_true * wscale
        xs = np.linspace(-l_, L + l_, 2501)

        def M(x, l_=l_, w=w):
            # origin at left support; overhang to the left (x<0) and right (x>L)
            RA = RB = W / 2 + w * (L + 2 * l_) / 2
            if x < 0:
                return -w * x**2 / 2
            if x <= L:
                return RA * x - w * (x + l_) ** 2 / 2 + w * l_ * 0 - W * max(x - L / 2, 0) + 0
            return -w * (L + l_ - x) ** 2 / 2
        # exact: M for x in span = RA x - w (x + l)^2/2 + w l (x + l/2)... recompute with simple statics below
        def M2(x, l_=l_, w=w):
            RA = W / 2 + w * (L + 2 * l_) / 2
            if x < 0:
                return -w * x**2 / 2
            if x <= L:
                Mx = RA * x - W * max(x - L / 2, 0) - w * (x + l_) ** 2 / 2 + w * l_ * 0
                # take moment of loads to the left of the section: overhang weight w*l at distance (x + l/2), span weight w*x at x/2
                Mx = RA * x - W * max(x - L / 2, 0) - w * l_ * (x + l_ / 2) - w * x * x / 2
                return Mx
            return -w * (L + l_ - x) ** 2 / 2
        v = beam_deflection(M2, xs, EI, (0.0, L))
        # l = 0 curve
        xs0 = np.linspace(0, L, 1001)
        M0 = lambda x, w=w: (W / 2 + w * L / 2) * x - W * max(x - L / 2, 0) - w * x * x / 2
        v0 = beam_deflection(M0, xs0, EI, (0.0, L))
        ax.plot(xs0, v0, color=GREY, lw=1.6, ls="--", label="$l=0$")
        ax.plot(xs, v, color=BLUE, lw=2, label="$l=100$ mm")
        ax.axhline(0, color=GREY, lw=0.6)
        ax.plot([0, L], [0, 0], "^", color=INK, ms=8)
        arrow(ax, (L / 2, max(v.max(), 0) + 0.8 + (1.3 if wscale == 0 else 0)), (L / 2, v0[500] + 0.2), RED, lw=1.8, ms=8)
        ax.text(L / 2 + 8, v.max() * 0 + 0.6 + (1.3 if wscale == 0 else 0), "$W$", color=RED)
        ax.set_title(title, fontsize=9.5)
        ax.set_xlabel("x (mm), supports at 0 and 400")
        ax.set_ylabel("deflection (mm, up positive)")
        ax.legend(frameon=False, loc="upper left")
        ax.set_ylim(min(v0.min(), v.min()) * 1.25, 2.4)
        print("   mid v0 %.4f  mid v %.4f  tip %.4f" % (v0[500], v[np.argmin(abs(xs - L / 2))], v[-1]))
    fig.tight_layout()
    save(fig, "AML-real-q13-overhang.png")


def mock_overhangs():
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.9))
    # Mock 1 Q13: supports 600 apart, overhang 200 each side, P at both tips, EI Al 25x6
    EI = 70e3 * 25 * 6**3 / 12
    P, L, a = 50.0, 600.0, 200.0
    xs = np.linspace(-a, L + a, 2001)
    M = lambda x: -P * (-x) if x < 0 else (-P * a if x <= L else -P * (x - L - 0 if False else (L + a - x)))
    def Mf(x):
        if x < 0:
            return -P * (-x)
        if x <= L:
            return -P * a
        return -P * (x - L)
    # for x>L the moment from the right overhang is -P (L+a-x)
    def Mf2(x):
        if x < 0:
            return -P * (a + x)
        if x <= L:
            return -P * a
        return -P * (L + a - x)
    v = beam_deflection(Mf2, xs, EI, (0.0, L))
    ax = axs[0]
    ax.plot(xs, v, color=BLUE, lw=2)
    ax.plot([0, L], [0, 0], "^", color=INK, ms=8)
    ax.axhline(0, color=GREY, lw=0.6)
    ax.axvspan(0, L, color=ORANGE, alpha=0.1)
    ax.text(L / 2, -9, "pure bending: $M=-Pa$ constant,\ncircular arc", ha="center", fontsize=8.5, color=ORANGE)
    for xx in (-a, L + a):
        arrow(ax, (xx, 8), (xx, 1.5), RED, lw=1.8, ms=8)
    ax.text(-a, 9, "$P$", color=RED, ha="center")
    ax.text(L + a, 9, "$P$", color=RED, ha="center")
    ax.annotate(f"{v[np.argmin(abs(xs - L / 2))]:.1f} mm up", (L / 2, v[np.argmin(abs(xs - L / 2))]), xytext=(L / 2, v[np.argmin(abs(xs - L / 2))] + 5), fontsize=8.5, ha="center",
                arrowprops=dict(arrowstyle="-", color=GREY))
    ax.annotate(f"{-v[0]:.1f} mm down", (-a, v[0]), xytext=(-a + 30, v[0] + 4), fontsize=8.5, color=RED, ha="left")
    ax.set_title("Mock 1, Q13: loads on both overhangs", fontsize=9.5)
    ax.set_xlabel("x (mm)")
    ax.set_ylabel("deflection (mm, up positive)")
    ax.set_ylim(-26, 14)
    print("   mock1 q13: mid", v[np.argmin(abs(xs - L / 2))], "tip", v[0])
    # Mock 3 Q13: span L=0.8 m, overhang a=0.2 m, P at the centre and P at the tip
    EI = 70e3 * 25 * 6**3 / 12
    L, a, P = 800.0, 200.0, 50.0
    xs = np.linspace(0, L + a, 2001)
    RA = P / 2 - P * a / L
    def Mg(x):
        if x <= L:
            return RA * x - P * max(x - L / 2, 0)
        return -P * (L + a - x)
    v = beam_deflection(Mg, xs, EI, (0.0, L))
    M = np.array([Mg(x) for x in xs])
    xc = xs[np.where(np.diff(np.sign(M[xs <= L])) != 0)[0]][0] if np.any(np.diff(np.sign(M[xs <= L])) != 0) else None
    ax = axs[1]
    ax.plot(xs, v, color=BLUE, lw=2)
    ax.plot([0, L], [0, 0], "^", color=INK, ms=8)
    ax.axhline(0, color=GREY, lw=0.6)
    xc_exact = (P * L / 2) / (P - RA)
    ax.axvline(xc_exact, color=RED, lw=1, ls=":")
    ax.text(xc_exact + 8, v.max() * 0.45, f"inflection $x={xc_exact:.0f}$ mm\n($=2L/3$)", color=RED, fontsize=8.5)
    arrow(ax, (L / 2, v.min() * 0 + 10), (L / 2, 1.0), RED, lw=1.8, ms=8)
    arrow(ax, (L + a, 10), (L + a, 1.0), RED, lw=1.8, ms=8)
    ax.text(L / 2 + 10, 8, "$P$", color=RED)
    ax.text(L + a - 20, 8, "$P$", color=RED)
    ax.set_title("Mock 3, Q13: loads at the centre and at the tip", fontsize=9.5)
    ax.set_xlabel("x (mm)")
    ax.set_ylim(-1.6 * abs(v.min()) - 2, 14)
    ax.set_ylim(v.min() * 1.4 - 2, 14)
    print("   mock3 q13: contraflexion", xc_exact, "min v", v.min(), "tip", v[-1])
    fig.tight_layout()
    save(fig, "AML-mock-overhangs.png")


def d_2d():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.5))
    e = np.linspace(0, 0.28, 400)
    from scipy.interpolate import PchipInterpolator
    S = PchipInterpolator([0, 0.0012, 0.02, 0.05, 0.10, 0.16, 0.20, 0.26], [0, 240, 240, 300, 360, 400, 380, 320])(e)
    S = np.where(e > 0.26, np.nan, S)
    for ax, title in zip(axs, ["same gauge length: load vs extension", "stress vs strain: one curve", "geometrically similar ($L_0\\propto d$)"]):
        ax.set_title(title, fontsize=9.5)
    A1 = pi * 10**2 / 4
    L1 = 50.0
    ax = axs[0]
    ax.plot(e * L1, S * A1 / 1e3, color=BLUE, lw=2, label="$d=10$ mm")
    ax.plot(e * L1, S * 4 * A1 / 1e3, color=ORANGE, lw=2, label="$2d=20$ mm")
    ax.set_xlabel("extension (mm), $L_0=50$ mm"); ax.set_ylabel("load (kN)")
    ax.legend(frameon=False)
    ax.text(5, 40, "load $\\times4$\nsame extension", fontsize=8.5, color=ORANGE)
    ax = axs[1]
    ax.plot(e, S, color=GREEN, lw=4, alpha=0.4)
    ax.plot(e, S, color=INK, lw=1, ls="--")
    ax.set_xlabel("strain $e$"); ax.set_ylabel("stress $S$ (MPa)")
    ax.text(0.04, 120, "both specimens:\nthe same curve\n($E$, $\\sigma_Y$, $\\sigma_u$, %EL\nare material properties)", fontsize=8.5)
    ax = axs[2]
    ax.plot(e * L1, S * A1 / 1e3, color=BLUE, lw=2, label="$d=10$, $L_0=50$")
    ax.plot(e * 2 * L1, S * 4 * A1 / 1e3, color=ORANGE, lw=2, label="$2d=20$, $L_0=100$")
    ax.set_xlabel("extension (mm)"); ax.set_ylabel("load (kN)")
    ax.legend(frameon=False)
    ax.text(10, 40, "load $\\times4$, extension $\\times2$", fontsize=8.5, color=ORANGE)
    fig.tight_layout()
    save(fig, "AML-tensile-size-effect.png")


if __name__ == "__main__":
    bridges()
    mirror_optics()
    photoelastic()
    real_q13()
    mock_overhangs()
    d_2d()
