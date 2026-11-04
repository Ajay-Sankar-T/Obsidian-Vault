"""AM2200 Tutorial 9 (columns): every number in 'Tutorial 9 - Columns' is recomputed here, and the transcendental buckling
   conditions of Q3-Q5 are checked with an independent method (integrating the buckling ODE and finding where the boundary
   determinant vanishes).   Run: python sm_t9.py   (figures go to ../assets/)"""
import os
import numpy as np
from math import pi, sqrt, sin, cos, tan, radians
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, RED, GREEN, GREY = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a", "#777777"


# ------------------------------------------------------------------ Q1
def q1():
    E, d, L = 200e9, 25e-3, 0.800
    I = pi / 4 * (d / 2) ** 4
    A = pi * d**2 / 4
    Pcr = pi**2 * E * I / L**2
    arm = 0.250 * sin(radians(45))                     # vertical distance A -> B
    k = 0.350 / arm                                     # F_BC = k P  (moments about A)
    P = Pcr / k
    r = sqrt(I / A)
    return dict(I_mm4=I * 1e12, A_mm2=A * 1e6, Pcr_kN=Pcr / 1e3, arm_mm=arm * 1e3, k=k, P_kN=P / 1e3,
                sigma_cr_MPa=Pcr / A / 1e6, slender=L / r, r_mm=r * 1e3)


# ------------------------------------------------------------------ Q2
def q2():
    E, sy, L, FS = 200e9, 360e6, 2.0, 3.0
    b, h = 0.030, 0.020                                 # width along y, height along x in the sketch
    Ix = h * b**3 / 12                                  # bending about the x-x axis uses the 30 mm width
    Iy = b * h**3 / 12
    A = b * h
    Pcr_x = pi**2 * E * Ix / (1.0 * L) ** 2             # pinned-pinned: K = 1
    Pcr_y = pi**2 * E * Iy / (0.5 * L) ** 2             # fixed-fixed: K = 0.5
    Pcr = min(Pcr_x, Pcr_y)
    Pallow = Pcr / FS
    # beam C-B-tip: pin at C, support from AB at B (1.5 m), uniform w over 2.0 m  ->  F_AB = w*2.0*1.0/1.5
    ratio = 2.0 * 1.0 / 1.5
    w = Pallow / ratio
    sig = lambda K, I: pi**2 * E / (K * L / sqrt(I / A)) ** 2
    return dict(Ix_mm4=Ix * 1e12, Iy_mm4=Iy * 1e12, Pcr_x_kN=Pcr_x / 1e3, Pcr_y_kN=Pcr_y / 1e3, Pallow_kN=Pallow / 1e3,
                F_over_w=ratio, w_kNm=w / 1e3, sig_cr_x_MPa=sig(1.0, Ix) / 1e6, sig_cr_y_MPa=sig(0.5, Iy) / 1e6,
                sigma_actual_MPa=Pallow / A / 1e6, sy=sy / 1e6)


# ------------------------------------------------------------------ independent buckling solver
def det_F(F, EI, l, cT_left, cT_right, rigid_left=0.0):
    """General pinned-pinned column with rotational springs (cT) at the ends, axial force F.
       Unknowns: end slope th0 and transverse reaction V0.  EI y'' = M0 + V0 x - F y  with M0 = cT_left*th0.  Returns the
       determinant of the 2x2 boundary system at x = l:  y(l) = 0,  EI y''(l) = -cT_right y'(l)."""
    cols = []
    for th0, V0 in ((1.0, 0.0), (0.0, 1.0)):
        M0 = cT_left * th0

        def rhs(x, s):
            y, yp = s
            return [yp, (M0 + V0 * x - F * y) / EI]
        sol = solve_ivp(rhs, [0, l], [0.0, th0], rtol=1e-11, atol=1e-13)
        y, yp = sol.y[0, -1], sol.y[1, -1]
        ypp = (M0 + V0 * l - F * y) / EI
        cols.append([y, ypp * EI + cT_right * yp])
    return cols[0][0] * cols[1][1] - cols[1][0] * cols[0][1]


def first_root(f, lo, hi, n=400):
    xs = np.linspace(lo, hi, n)
    v = [f(x) for x in xs]
    for a, b, fa, fb in zip(xs[:-1], xs[1:], v[:-1], v[1:]):
        if fa * fb < 0:
            return brentq(f, a, b, xtol=1e-12)
    return None


# ------------------------------------------------------------------ Q3
def q3():
    # top: no rotation, no lateral translation; bottom: no rotation, free to translate.  y = (M/F)(1 - cos kx): y'(L)=0 -> kL = pi.
    return dict(Pcr_EI_over_L2=pi**2, K=1.0)


# ------------------------------------------------------------------ Q4
def q4(beta=1.0):
    """beta = cT*l/EI.  Symmetric mode:  tan u = -(2/beta) u,  u = k l / 2 in (pi/2, pi);  Pcr = (2u)^2 EI/l^2."""
    f = lambda u: np.tan(u) + 2.0 / beta * u
    u = brentq(f, pi / 2 + 1e-6, pi - 1e-6)
    return u, (2 * u) ** 2


def q4_check():
    EI, l = 1.0, 1.0
    cT = EI / l
    F = first_root(lambda F: det_F(F, EI, l, cT, cT), 1.0, 60.0, 600)
    return F


# ------------------------------------------------------------------ Q5
def q5():
    f = lambda x: x * np.cos(x) + np.sin(x)             # k a cos(ka) + sin(ka) = 0
    x = first_root(f, 0.5, 4.0)
    return x, x**2


def q5_check():
    """rigid left half of length a (rotates about the left pin by phi), elastic right half, pinned right end."""
    a, EI = 1.0, 1.0

    def det(F):
        k = sqrt(F / EI)
        # y = A cos kx + B sin kx on 0<x<a ; y(0) = A ; y'(0) = B k = y(0)/a ; y(a) = 0
        sol = solve_ivp(lambda x, s: [s[1], -F / EI * s[0]], [0, a], [1.0, 1.0 / a], rtol=1e-11, atol=1e-13)
        return sol.y[0, -1]
    return first_root(det, 0.5, 20.0, 800)


# ------------------------------------------------------------------ figures
def draw_hatch(ax, x0, x1, y, side="below", n=8, L=0.03):
    for xx in np.linspace(x0, x1, n):
        ax.plot([xx, xx - L], [y, y - L] if side == "below" else [y, y + L], color="k", lw=0.8)


def fig_q1(r):
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    A = np.array([0.0, 0.0]); T = np.array([0.0, 0.35]); B = np.array([0.1768, -0.1768]); C = B + np.array([0.8, 0.0])
    ax.plot(*zip(T, A), color=BLUE, lw=5, solid_capstyle="round"); ax.plot(*zip(A, B), color=BLUE, lw=5, solid_capstyle="round")
    ax.plot(*zip(B, C), color=GREY, lw=3)
    for p, t in ((A, "A"), (B, "B"), (C, "C")):
        ax.plot(*p, "ko", ms=7); ax.text(p[0] + 0.015, p[1] + 0.03, t, fontsize=12)
    ax.annotate("", xy=(T[0] - 0.01, T[1]), xytext=(T[0] + 0.17, T[1]), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
    ax.text(T[0] + 0.18, T[1] - 0.01, "P", color=RED, fontsize=13, weight="bold")
    ax.annotate("", xy=(B[0] + 0.12, B[1] + 0.0), xytext=(B[0] + 0.01, B[1]), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.5))
    ax.text(B[0] + 0.14, B[1] + 0.02, r"$F_{BC}$ (compression in rod)", color=ORANGE, fontsize=10)
    ax.plot([A[0] - 0.05, A[0] - 0.05], [A[1], T[1]], color="k", lw=0.8); ax.text(A[0] - 0.06, 0.17, "350 mm", ha="right", fontsize=9)
    ax.plot([A[0] - 0.12, A[0] - 0.12], [A[1], B[1]], color="k", lw=0.8); ax.text(A[0] - 0.13, -0.09, "176.8 mm", ha="right", fontsize=9)
    ax.plot([A[0], A[0] - 0.12], [B[1], B[1]], color="k", lw=0.5, ls=":")
    ax.text(0.2, 0.2, r"$\sum M_A=0:\ P(350)=F_{BC}(250\sin45^\circ)$" + "\n" + rf"$F_{{BC}}={r['k']:.3f}\,P$", fontsize=11)
    ax.text(0.45, -0.28, "BC: pinned-pinned, L = 800 mm", fontsize=10, ha="center")
    ax.set_xlim(-0.35, 1.2); ax.set_ylim(-0.35, 0.5); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Q1: statics gives the rod force, Euler gives the limit", fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "SM-T9-Q1-control-rod.png"), dpi=150); plt.close(fig)


def fig_q2(r):
    fig, axs = plt.subplots(1, 3, figsize=(12.2, 4.2), gridspec_kw=dict(width_ratios=[1.5, 1, 1.1]))
    ax = axs[0]
    ax.plot([0, 2.0], [0, 0], color=GREY, lw=5)
    for x in np.linspace(0.05, 1.95, 14):
        ax.annotate("", xy=(x, 0.03), xytext=(x, 0.3), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1))
    ax.text(1.0, 0.37, "w (kN/m) over 2.0 m", ha="center", color=BLUE)
    ax.plot(0, 0, "ko", ms=8); ax.text(-0.02, 0.1, "C", ha="right")
    ax.plot(1.5, 0, "ko", ms=8); ax.text(1.5, 0.1, "B")
    ax.plot([1.5, 1.5], [0, -2.0], color=ORANGE, lw=6); ax.text(1.6, -1.0, "AB\n2 m", color=ORANGE)
    ax.plot(1.5, -2.0, "ko", ms=8); ax.text(1.38, -2.15, "A", ha="right")
    ax.annotate("", xy=(1.5, -0.35), xytext=(1.5, -1.0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.text(0.2, -0.75, r"$\sum M_C=0$:" + "\n" + rf"$F_{{AB}}(1.5)=w(2.0)(1.0)$" + "\n" + rf"$F_{{AB}}={r['F_over_w']:.3f}\,w$", fontsize=10)
    ax.set_xlim(-0.3, 2.3); ax.set_ylim(-2.4, 0.7); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("loads on BC and the compression in AB", fontsize=10)
    ax = axs[1]
    ax.add_patch(plt.Rectangle((-15, -10), 30, 20, fill=False, lw=2, color=BLUE))
    ax.annotate("", xy=(-25, 0), xytext=(25, 0), arrowprops=dict(arrowstyle="-", ls="--", color=GREY)); ax.annotate("", xy=(0, -17), xytext=(0, 17), arrowprops=dict(arrowstyle="-", ls="--", color=GREY))
    ax.text(26, 1, "y", fontsize=11); ax.text(1.5, 18, "x", fontsize=11)
    ax.text(0, -22, "30 mm", ha="center"); ax.text(18, 0, "20 mm", rotation=90, va="center")
    ax.text(0, 24, rf"$I_x=\frac{{20\cdot30^3}}{{12}}={r['Ix_mm4']:.0f}$ mm$^4$" + "\n" + rf"$I_y=\frac{{30\cdot20^3}}{{12}}={r['Iy_mm4']:.0f}$ mm$^4$", ha="center", fontsize=9)
    ax.set_xlim(-30, 35); ax.set_ylim(-28, 38); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("section of AB", fontsize=10)
    ax = axs[2]
    bars = ax.bar(["x-x\n(pinned, K=1)", "y-y\n(fixed, K=0.5)"], [r["Pcr_x_kN"], r["Pcr_y_kN"]], color=[RED, GREEN])
    for b, v in zip(bars, [r["Pcr_x_kN"], r["Pcr_y_kN"]]):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.1f} kN", ha="center")
    ax.set_ylabel(r"$P_{cr}$ (kN)"); ax.set_title("the weaker axis governs", fontsize=10); ax.set_ylim(0, 48)
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "SM-T9-Q2-column-AB.png"), dpi=150); plt.close(fig)


def fig_q3():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.6))
    L = 1.0
    x = np.linspace(0, L, 200)
    d = 0.12
    y = d / 2 * (1 - np.cos(pi * x / L))
    ax = axs[0]
    ax.plot(y, L - x, color=RED, lw=2.5, label=r"buckled shape  $v=\frac{\delta}{2}\left(1-\cos\frac{\pi x}{L}\right)$")
    ax.plot([0, 0], [0, L], color=GREY, lw=1.2, ls="--", label="straight column")
    ax.add_patch(plt.Rectangle((-0.05, L), 0.1, 0.05, fill=False)); ax.text(0.0, L + 0.09, "P", ha="center", color=RED, weight="bold")
    ax.annotate("", xy=(0, L + 0.01), xytext=(0, L + 0.17), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.plot([-0.1, -0.1], [L - 0.1, L + 0.1], color="k", lw=3); ax.plot([0.1, 0.1], [L - 0.1, L + 0.1], color="k", lw=3)
    ax.text(0.14, L, "guide: no rotation,\nno sway at the top", fontsize=8, va="center")
    ax.add_patch(plt.Rectangle((d - 0.05, -0.07), 0.1, 0.07, fill=False)); ax.plot([d - 0.08, d + 0.08], [-0.085, -0.085], "o-", color="k", ms=5)
    ax.text(d + 0.1, -0.05, "base: no rotation,\nfree to roll", fontsize=8)
    ax.annotate("", xy=(d, 0.0), xytext=(0, 0.0), arrowprops=dict(arrowstyle="<->", color=BLUE)); ax.text(d / 2, 0.04, r"$\delta$", ha="center", color=BLUE)
    ax.set_xlim(-0.3, 0.45); ax.set_ylim(-0.2, 1.3); ax.set_aspect("equal"); ax.axis("off"); ax.legend(loc="lower right", fontsize=7); ax.set_title("Q3: sway mode, zero slope at both ends", fontsize=10)
    ax = axs[1]
    names = ["pinned-pinned", "fixed-pinned", "fixed-guided\n(this problem)", "fixed-fixed", "fixed-free"]
    vals = [pi**2, pi**2 / 0.49, pi**2, 4 * pi**2, pi**2 / 4]
    cols = [GREY, GREY, RED, GREY, GREY]
    ax.barh(names, vals, color=cols)
    for i, v in enumerate(vals):
        ax.text(v + 0.5, i, f"{v:.2f}", va="center", fontsize=9)
    ax.set_xlabel(r"$P_{cr}\,L^2/EI$"); ax.set_title("same column, different ends (K = effective length factor)", fontsize=9); ax.set_xlim(0, 48)
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "SM-T9-Q3-sway-column.png"), dpi=150); plt.close(fig)


def fig_q4(u, Pc):
    fig, axs = plt.subplots(1, 3, figsize=(13.2, 4.2))
    ax = axs[0]
    uu = np.linspace(pi / 2 + 0.01, pi - 0.01, 400)
    ax.plot(uu, np.tan(uu), color=BLUE, lw=2, label=r"$\tan u$"); ax.plot(uu, -2 * uu, color=ORANGE, lw=2, label=r"$-2u$")
    ax.plot([u], [-2 * u], "o", color=RED, ms=8); ax.annotate(rf"$u={u:.4f}$", (u, -2 * u), xytext=(u + 0.2, -7), arrowprops=dict(arrowstyle="->"))
    ax.set_ylim(-12, 3); ax.axhline(0, color="k", lw=0.5); ax.set_xlabel(r"$u=kl/2$"); ax.legend(); ax.set_title(r"Q4: $\tan u=-2u$ (for $EI=lc_T$)", fontsize=10); ax.grid(alpha=0.3)
    ax = axs[1]
    k = 2 * u
    x = np.linspace(0, 1, 300)
    A_ = -1.0
    y = np.cos(k * x) * A_ + A_ * np.tan(k / 2) * np.sin(k * x) - A_ * 1.0 * 1.0   # y = A cos + B sin - A with A = -Ms/F  (up to scale)
    y = -(np.cos(k * x) - 1 + np.tan(k / 2) * np.sin(k * x)) * 1.0
    y = y / np.max(np.abs(y)) * 0.15
    ax.plot(x, y, color=RED, lw=2.5); ax.plot([0, 1], [0, 0], color=GREY, ls="--")
    for xs in (0, 1):
        ax.plot(xs, 0, "ko", ms=7)
    ax.set_ylim(-0.1, 0.35); ax.set_title(rf"buckled shape, $P_{{cr}}={Pc:.2f}\,EI/l^2$", fontsize=10); ax.set_xlabel("x / l"); ax.set_aspect(2.5)
    ax.annotate("spring $c_T$", (0, 0), xytext=(0.02, 0.2), fontsize=9, arrowprops=dict(arrowstyle="->")); ax.annotate("spring $c_T$", (1, 0), xytext=(0.7, 0.2), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax = axs[2]
    betas = np.logspace(-2, 3, 200)
    pc = [q4(b)[1] for b in betas]
    ax.semilogx(betas, pc, color=BLUE, lw=2)
    ax.axhline(pi**2, color=GREY, ls="--"); ax.axhline(4 * pi**2, color=GREY, ls="--"); ax.text(0.012, pi**2 + 0.8, r"pinned: $\pi^2$", fontsize=9); ax.text(0.012, 4 * pi**2 - 3, r"fixed: $4\pi^2$", fontsize=9)
    ax.plot([1], [Pc], "o", color=RED, ms=8); ax.annotate(rf"$c_Tl/EI=1$: {Pc:.2f}", (1, Pc), xytext=(5, 16), arrowprops=dict(arrowstyle="->"))
    ax.set_xlabel(r"stiffness ratio $c_Tl/EI$"); ax.set_ylabel(r"$P_{cr}\,l^2/EI$"); ax.set_title("from pinned to clamped as the springs stiffen", fontsize=10); ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "SM-T9-Q4-spring-ends.png"), dpi=150); plt.close(fig)


def fig_q5(x0, Pc):
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axs[0]
    xx = np.linspace(0.3, 3.0, 400)
    ax.plot(xx, np.tan(np.where(np.abs(np.cos(xx)) < 1e-3, np.nan, xx)), alpha=0)
    xs = np.linspace(pi / 2 + 0.02, pi - 0.02, 300)
    ax.plot(xs, np.tan(xs), color=BLUE, lw=2, label=r"$\tan ka$"); ax.plot(xs, -xs, color=ORANGE, lw=2, label=r"$-ka$")
    ax.plot([x0], [-x0], "o", color=RED, ms=8); ax.annotate(rf"$ka={x0:.4f}$", (x0, -x0), xytext=(x0 + 0.12, -7), arrowprops=dict(arrowstyle="->"))
    ax.set_ylim(-10, 1); ax.axhline(0, color="k", lw=0.5); ax.set_xlabel("ka"); ax.legend(); ax.grid(alpha=0.3); ax.set_title(r"Q5: buckling condition $\tan ka=-ka$", fontsize=10)
    ax = axs[1]
    a = 1.0; k = x0 / a
    xe = np.linspace(0, a, 200)
    ye = np.cos(k * xe) + np.sin(k * xe) / (k * a)
    ye = ye / ye[0]
    ax.plot([-a, 0], [-a * 0 + 0, 0], alpha=0)
    ax.plot([-a, 0], [0, 1.0], color=ORANGE, lw=7, label="rigid part (straight, rotates about the pin)")
    ax.plot(xe, ye, color=RED, lw=2.5, label="elastic part")
    ax.plot([-a, a], [0, 0], color=GREY, ls="--", lw=1)
    for xs in (-a, a):
        ax.plot(xs, 0, "ko", ms=7)
    ax.set_aspect(1.0); ax.set_ylim(-0.2, 1.3); ax.legend(fontsize=8, loc="upper right"); ax.set_title(rf"buckled shape, $F_{{cr}}={Pc:.3f}\,EI/a^2$", fontsize=10); ax.set_xlabel("x / a  (x = 0 at the joint)")
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "SM-T9-Q5-rigid-elastic.png"), dpi=150); plt.close(fig)


if __name__ == "__main__":
    r1 = q1(); print("Q1", {k: round(v, 4) for k, v in r1.items()})
    r2 = q2(); print("Q2", {k: round(v, 4) for k, v in r2.items()})
    print("Q3", q3())
    u, Pc4 = q4(); print("Q4  u =", round(u, 6), " Pcr l^2/EI =", round(Pc4, 5), " check by integration:", round(q4_check(), 5))
    for b in (0.1, 1.0, 10.0, 100.0):
        print("     beta", b, "->", round(q4(b)[1], 4))
    x5, Pc5 = q5(); print("Q5  ka =", round(x5, 6), " Fcr a^2/EI =", round(Pc5, 5), " check by integration (F a^2/EI):", round(q5_check(), 5), " Le/a =", round(pi / x5, 4))
    fig_q1(r1); fig_q2(r2); fig_q3(); fig_q4(u, Pc4); fig_q5(x5, Pc5)
    print("figures written")
