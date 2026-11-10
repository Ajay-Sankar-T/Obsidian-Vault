"""Figures for the Assignments 6-10 revision notes (written to ../Problems/assets/).   python de_a610_figs.py
FB-1 Bessel sheet, FB-2 boundary conditions to eigenfunctions, FB-3 what each equation does to mode n,
QB-1 (Part 1: Fourier-Bessel, Robin eigenvalues, Chebyshev), QB-2 (Part 2: Burgers characteristics, regions),
QB-3 (Part 3: struck string, reflection, plucked string, cooling rod, quarter disc)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import special as sc
from scipy.optimize import brentq

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Problems", "assets")
os.makedirs(OUT, exist_ok=True)
PI = np.pi
BLUE, ORANGE, RED, GREY, GREEN, PURPLE = "#3d7be8", "#e8a33d", "#d94a4a", "#555555", "#2f9e6e", "#8a5ad6"
plt.rcParams.update({"font.size": 9, "axes.grid": True, "grid.alpha": 0.25, "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=150)
    plt.close(fig)
    print("wrote", name)


# ------------------------------------------------------------------------------------------------ FB-1
def fig_fb1():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6))
    xs = np.linspace(0.001, 20, 2000)
    ax = axs[0]
    for n, c in zip(range(4), (BLUE, ORANGE, GREEN, PURPLE)):
        ax.plot(xs, sc.jv(n, xs), color=c, lw=1.6, label=f"$J_{n}$")
    env = np.sqrt(2 / (PI * xs))
    ax.plot(xs, env, "--", color=GREY, lw=1); ax.plot(xs, -env, "--", color=GREY, lw=1, label=r"$\pm\sqrt{2/\pi x}$")
    ax.set_ylim(-0.6, 1.05); ax.set_xlim(0, 20); ax.set_xlabel("x")
    ax.set_title("$J_n$: finite at 0, decaying like $x^{-1/2}$"); ax.legend(ncol=3, fontsize=7, loc="upper right")
    ax = axs[1]
    xs2 = np.linspace(0.05, 20, 2000)
    ax.plot(xs2, sc.yv(0, xs2), color=BLUE, lw=1.6, label="$Y_0$ (log)")
    ax.plot(xs2, sc.yv(1, xs2), color=ORANGE, lw=1.6, label=r"$Y_1\sim -2/\pi x$")
    ax.plot(xs2, sc.jv(0, xs2), color=BLUE, lw=0.8, alpha=0.5); ax.plot(xs2, sc.jv(1, xs2), color=ORANGE, lw=0.8, alpha=0.5)
    ax.set_ylim(-1.6, 1.0); ax.set_xlim(0, 20); ax.set_xlabel("x")
    ax.set_title("$Y_n$: unbounded at 0 (thin: $J_0,J_1$)"); ax.legend(fontsize=7, loc="lower right")
    ax = axs[2]
    xs3 = np.linspace(0.001, 20, 2000)
    sph = lambda n: np.sqrt(PI / (2 * xs3)) * sc.jv(n + 0.5, xs3)
    for n, c in zip(range(3), (BLUE, ORANGE, GREEN)):
        ax.plot(xs3, sph(n), color=c, lw=1.6, label=f"$j_{n}$")
    ax.plot(xs3, np.sin(xs3) / xs3, ":", color=GREY, lw=1)
    ax.set_xlim(0, 20); ax.set_ylim(-0.3, 1.05); ax.set_xlabel("x")
    ax.set_title(r"spherical $j_n=\sqrt{\pi/2x}\,J_{n+1/2}$ (elementary)"); ax.legend(fontsize=7)
    save(fig, "A610-FB-1-bessel-sheet.png")


# ------------------------------------------------------------------------------------------------ FB-2
def fig_fb2():
    fig, axs = plt.subplots(2, 2, figsize=(10.5, 6.0))
    xs = np.linspace(0, 1, 400)
    cols = (BLUE, ORANGE, GREEN)
    cases = [
        ("Dirichlet-Dirichlet   $y(0)=y(L)=0$", lambda n: np.sin(n * PI * xs), r"$\lambda_n=(n\pi/L)^2,\ n\geq1$", "sin"),
        ("Neumann-Neumann   $y'(0)=y'(L)=0$", lambda n: np.cos(n * PI * xs), r"$\lambda_n=(n\pi/L)^2,\ n\geq0$ (note $\lambda_0=0$)", "cos"),
        ("Dirichlet at 0, Neumann at L:   $y(0)=0,\\; y'(L)=0$", lambda n: np.sin((n - 0.5) * PI * xs), r"$\lambda_n=((2n-1)\pi/2L)^2$", "mix"),
        ("Neumann at 0, Dirichlet at L:   $y'(0)=0,\\; y(L)=0$", lambda n: np.cos((n - 0.5) * PI * xs), r"$\lambda_n=((2n-1)\pi/2L)^2$", "mix2"),
    ]
    for ax, (title, f, lam, kind) in zip(axs.ravel(), cases):
        rng = range(0, 3) if kind == "cos" else range(1, 4)
        for n, c in zip(rng, cols):
            ax.plot(xs, f(n), color=c, lw=1.7, label=f"$n={n}$")
        ax.axhline(0, color=GREY, lw=0.6)
        ax.set_title(title, fontsize=9); ax.text(0.5, -1.38, lam, ha="center", fontsize=8.5)
        ax.set_ylim(-1.5, 1.3); ax.set_xlabel("x / L"); ax.legend(ncol=3, fontsize=7, loc="upper right")
    save(fig, "A610-FB-2-bc-modes.png")


# ------------------------------------------------------------------------------------------------ FB-3
def fig_fb3():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6))
    cols = {1: BLUE, 2: ORANGE, 3: GREEN, 5: PURPLE}
    ax = axs[0]
    tt = np.linspace(0, 2, 400)
    for n, c in cols.items():
        ax.plot(tt, np.cos(n * PI * tt), color=c, lw=1.3, label=f"n={n}")
    ax.set_title("wave: $\\cos(n\\pi ct/L)$\nevery mode keeps its amplitude"); ax.set_xlabel("$ct/L$")
    ax.legend(ncol=4, fontsize=7, loc="lower center", bbox_to_anchor=(0.5, -0.42), frameon=False)
    ax = axs[1]
    tt = np.linspace(0, 0.5, 400)
    for n, c in cols.items():
        ax.plot(tt, np.exp(-n**2 * PI**2 * tt), color=c, lw=1.5, label=f"n={n}")
    ax.set_title("heat: $e^{-n^2\\pi^2c^2t/L^2}$\nhigh modes die first (rate $\\propto n^2$)"); ax.set_xlabel("$c^2t/L^2$"); ax.legend(ncol=4, fontsize=7)
    ax = axs[2]
    yy = np.linspace(0, 1, 400)
    for n, c in cols.items():
        ax.plot(yy, np.sinh(n * PI * yy) / np.sinh(n * PI), color=c, lw=1.5, label=f"n={n}")
    ax.set_title("Laplace: $\\sinh(n\\pi y/L)/\\sinh(n\\pi)$\nhigh modes live near the driven edge"); ax.set_xlabel("$y/L$"); ax.legend(ncol=4, fontsize=7)
    save(fig, "A610-FB-3-mode-factors.png")


# ------------------------------------------------------------------------------------------------ QB-1
def fig_qb1():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.7))
    ax = axs[0]
    xs = np.linspace(0, 1, 400)
    al = sc.jn_zeros(0, 3000)
    a = 8 / (al**3 * sc.jv(1, al))
    ax.plot(xs, 1 - xs**2, color=GREY, lw=3, alpha=0.5, label="$1-x^2$")
    for N, c in ((1, BLUE), (3, ORANGE), (8, GREEN)):
        ax.plot(xs, sum(a[k] * sc.jv(0, al[k] * xs) for k in range(N)), color=c, lw=1.4, label=f"{N} term" + ("s" if N > 1 else ""))
    ax.set_title("Q4: Fourier-Bessel series of $1-x^2$\n$a_n=8/(\\alpha_n^3J_1(\\alpha_n))$"); ax.legend(fontsize=7); ax.set_xlabel("x")
    ax = axs[1]
    ms = np.linspace(0.01, 15, 3000)
    ax.plot(ms, np.tan(ms), color=BLUE, lw=1.3, label=r"$\tan\mu$")
    ax.plot(ms, ms, color=RED, lw=1.5, label=r"$\mu$")
    ax.set_ylim(-12, 25)
    roots = [brentq(lambda m: np.sin(m) - m * np.cos(m), k * PI + 1e-6, k * PI + PI / 2 - 1e-6) for k in (1, 2, 3, 4)]
    ax.plot(roots, roots, "o", color=GREEN, ms=5)
    ax.set_title("Q8: $y(1)=y'(1)$ gives $\\tan\\mu=\\mu$\nroots 4.493, 7.725, 10.904, 14.066; plus $\\lambda=0$"); ax.legend(fontsize=7); ax.set_xlabel("$\\mu$")
    # remove tan asymptote jumps
    for line in ax.lines[:1]:
        yd = line.get_ydata().copy(); yd[np.abs(yd) > 30] = np.nan; line.set_ydata(yd)
    ax = axs[2]
    xs = np.linspace(-1, 1, 401)
    T = lambda n: np.cos(n * np.arccos(xs))
    ax.plot(xs, xs**4, color=GREY, lw=3, alpha=0.5, label="$x^4$")
    ax.plot(xs, 3 / 8 + 0 * xs, color=BLUE, lw=1.2, label="$T_0$ term only")
    ax.plot(xs, 3 / 8 * T(0) + 1 / 2 * T(2), color=ORANGE, lw=1.3, label="$T_0,T_2$")
    ax.plot(xs, (3 * T(0) + 4 * T(2) + T(4)) / 8, "--", color=GREEN, lw=1.5, label="$+T_4$: exact")
    ax.set_title("Q10: $x^4=(3T_0+4T_2+T_4)/8$\nfinite expansion in Chebyshev polynomials"); ax.legend(fontsize=7); ax.set_xlabel("x")
    save(fig, "A610-QB-1-bessel-sl.png")


# ------------------------------------------------------------------------------------------------ QB-2
def fig_qb2():
    fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.8))
    ax = axs[0]
    for x0 in np.linspace(-2, 2, 17):
        yy = np.linspace(0, 1, 50)
        ax.plot(x0 * (1 - yy), yy, color=BLUE, lw=1)
    ax.plot([0], [1], "o", color=RED, ms=6)
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(0, 1.15)
    ax.set_title("Q5: $uu_x+u_y=0$, $u(x,0)=-x$\ncharacteristics $x=x_0(1-y)$ all meet at $(0,1)$"); ax.set_xlabel("x"); ax.set_ylabel("y")
    ax = axs[1]
    for yv, c in ((0, BLUE), (0.5, ORANGE), (0.9, GREEN)):
        xs = np.linspace(-2, 2, 200)
        ax.plot(xs, -xs / (1 - yv), color=c, lw=1.6, label=f"y={yv}")
    ax.set_title("profiles $u=-x/(1-y)$ steepen\nslope $-1/(1-y)\\to-\\infty$ at $y=1$"); ax.legend(fontsize=7); ax.set_xlabel("x"); ax.set_ylim(-20, 20)
    ax = axs[2]
    X, Y = np.meshgrid(np.linspace(-3, 3, 400), np.linspace(-3, 3, 400))
    D = 1 + Y**2 - X**2
    ax.contourf(X, Y, D, levels=[-100, 0, 100], colors=["#b8d0f5", "#f5d8a8"], alpha=0.9)
    ax.contour(X, Y, D, levels=[0], colors=["#333"], linewidths=1.8)
    ax.text(0, 0, "hyperbolic", ha="center", color="#8a5a00", fontsize=9)
    ax.text(2.0, 0.2, "elliptic", ha="center", color="#1f4ea8", fontsize=9); ax.text(-2.0, -0.2, "elliptic", ha="center", color="#1f4ea8", fontsize=9)
    ax.set_title("Q7: $\\Delta=4(1+y^2-x^2)$\nparabolic on $x^2-y^2=1$"); ax.set_aspect("equal"); ax.set_xlabel("x"); ax.set_ylabel("y")
    save(fig, "A610-QB-2-pde.png")


# ------------------------------------------------------------------------------------------------ QB-3
def fig_qb3():
    fig, axs = plt.subplots(2, 3, figsize=(11.5, 6.4))
    # Q1 struck string
    ax = axs[0, 0]
    xs = np.linspace(-5, 5, 800)

    def ustruck(X, T):
        lo = np.maximum(X - T, -1); hi = np.minimum(X + T, 1)
        return 0.5 * np.maximum(hi - lo, 0)
    for T, c in ((0.5, BLUE), (1.0, ORANGE), (2.0, GREEN), (3.0, PURPLE)):
        ax.plot(xs, ustruck(xs, T), color=c, lw=1.6, label=f"t={T}")
    ax.set_title("Q1: struck string, $c=1$", fontsize=9); ax.legend(fontsize=7, ncol=2, loc="upper right"); ax.set_xlabel("x")
    # Q2 reflection
    ax = axs[0, 1]
    xs = np.linspace(0, 6, 800)
    f = lambda s: np.where((s > 1) & (s < 2), 1.0, 0.0)
    fo = lambda s: np.where(s >= 0, f(s), -f(-s))
    for T, c in ((0, GREY), (1.5, BLUE), (2.5, ORANGE), (3.5, GREEN)):
        ax.plot(xs, 0.5 * (fo(xs + T) + fo(xs - T)), color=c, lw=1.6, label=f"t={T}")
    ax.axvline(0, color="#333", lw=2)
    ax.set_title("Q2: reflection at a fixed end", fontsize=9); ax.legend(fontsize=7, ncol=2); ax.set_xlabel("x")
    # Q3 plucked
    ax = axs[0, 2]
    nn = np.arange(1, 13)
    A = 32 * np.sin(nn * PI / 4) / (3 * nn**2 * PI**2)
    ax.bar(nn, np.abs(A), color=[RED if abs(a) < 1e-9 else BLUE for a in A])
    ax.set_title("Q3: $|A_n|/h$, pluck at $L/4$", fontsize=9); ax.set_xlabel("n"); ax.set_xticks(nn)
    # Q5 cooling rod
    ax = axs[1, 0]
    L, c2 = 0.4, 1.11e-4
    n = np.arange(1, 4000, 2)
    tt = np.linspace(0, 600, 300)
    cen = [np.sum(400 / (n * PI) * np.sin(n * PI / 2) * np.exp(-n**2 * PI**2 * c2 * T / L**2)) for T in tt]
    ax.plot(tt, cen, color=BLUE, lw=1.8)
    ax.plot(tt, 400 / PI * np.exp(-PI**2 * c2 * tt / L**2), "--", color=ORANGE, lw=1.2, label="first mode only")
    ax.axhline(50, color=GREY, lw=0.7); ax.axhline(5, color=GREY, lw=0.7)
    ax.plot([136.5, 472.8], [50, 5], "o", color=RED)
    ax.set_ylim(0, 105); ax.set_title("Q5: rod centre, 50 at 136 s, 5 at 473 s", fontsize=9); ax.set_xlabel("t (s)"); ax.legend(fontsize=7)
    # Q8 source term
    ax = axs[1, 1]
    xs = np.linspace(0, 1, 300)
    n = np.arange(1, 400, 2)
    for T, c in ((0.0, GREY), (0.02, BLUE), (0.05, ORANGE), (0.1, GREEN), (0.4, PURPLE)):
        u = xs * (1 - xs) - np.sum(8 / (n[:, None]**3 * PI**3) * np.sin(n[:, None] * PI * xs) * np.exp(-n[:, None]**2 * PI**2 * T), axis=0)
        ax.plot(xs, u, color=c, lw=1.5, label=f"t={T}")
    ax.plot(xs, xs * (1 - xs), ":", color="#333", lw=1)
    ax.set_title("Q8: heating with source $+2$", fontsize=9); ax.legend(fontsize=7, ncol=5, loc="lower center", bbox_to_anchor=(0.5, -0.32), frameon=False); ax.set_xlabel("x")
    # Q13 quarter disc
    ax = axs[1, 2]
    R, T = np.meshgrid(np.linspace(0.001, 0.999, 300), np.linspace(0.001, PI / 2 - 0.001, 300))
    U = 2 / PI * np.arctan(2 * R**2 * np.sin(2 * T) / (1 - R**4))
    cs = ax.contourf(R * np.cos(T), R * np.sin(T), U, levels=np.linspace(0, 1, 11), cmap="viridis")
    ax.contour(R * np.cos(T), R * np.sin(T), U, levels=np.linspace(0, 1, 11), colors="white", linewidths=0.5)
    fig.colorbar(cs, ax=ax, fraction=0.046, pad=0.03)
    ax.set_aspect("equal"); ax.set_title("Q13: quarter disc, $u=1$ on the arc", fontsize=9); ax.set_xlabel("x"); ax.set_ylabel("y")
    save(fig, "A610-QB-3-waves-heat.png")


if __name__ == "__main__":
    fig_fb1(); fig_fb2(); fig_fb3(); fig_qb1(); fig_qb2(); fig_qb3()
