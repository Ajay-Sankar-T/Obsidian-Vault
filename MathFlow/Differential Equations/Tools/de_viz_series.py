"""Figures for the EXISTING series-solution notes (Lectures 12-14).  Run `python de_viz_series.py`."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import special as sc
from matplotlib.patches import Circle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote", name)

# ------------------------------------------------------------------------------- power-series method: y'' - y = 0
def fig_power_series():
    x = np.linspace(-4, 4, 400); fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    # recurrence a_{n+2} = a_n / ((n+1)(n+2)) from y'' - y = 0
    def psum(a0, a1, N):
        a = [a0, a1]
        for n in range(0, N): a.append(a[n]/((n+1)*(n+2)))
        return sum(a[k]*x**k for k in range(N+2))
    a = ax[0]; a.plot(x, np.cosh(x), "k", lw=2.4, label=r"$\cosh x$ (exact, $a_0=1,a_1=0$)")
    for N, c in ((2, C[1]), (6, C[2]), (12, C[0])): a.plot(x, psum(1, 0, N), color=c, lw=1.4, label=f"partial sum, degree {N+1}")
    a.set_ylim(-5, 30); a.legend(fontsize=8); a.set_title(r"$y''-y=0$: $a_{n+2}=\dfrac{a_n}{(n+1)(n+2)}$, even chain")
    a = ax[1]; a.plot(x, np.sinh(x), "k", lw=2.4, label=r"$\sinh x$ ($a_0=0,a_1=1$)")
    for N, c in ((2, C[1]), (6, C[2]), (12, C[0])): a.plot(x, psum(0, 1, N), color=c, lw=1.4, label=f"partial sum, degree {N+1}")
    a.set_ylim(-30, 30); a.legend(fontsize=8); a.set_title("odd chain: converges for every $x$ ($R=\\infty$)")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-S1-power-series.png")

# ------------------------------------------------------------------------------- radius of convergence
def fig_radius():
    fig, ax = plt.subplots(1, 3, figsize=(14.5, 4.3))
    a = ax[0]; a.set_aspect("equal"); a.axhline(0, color="k", lw=.8); a.axvline(0, color="k", lw=.8)
    a.add_patch(Circle((0, 0), 1, fc=C[0], alpha=.15, ec=C[0], lw=2)); a.plot([-1, 1], [0, 0], "x", color=C[1], ms=11, mew=3)
    a.add_patch(Circle((.5, 0), .5, fc=C[2], alpha=.2, ec=C[2], lw=2)); a.plot([.5], [0], "o", color=C[2]); a.plot([0], [0], "o", color=C[0])
    a.annotate("$x_0=0$: $R=1$", (0, 0), (-1.3, 1.15), arrowprops=dict(arrowstyle="->"), color=C[0]); a.annotate("$x_0=\\frac{1}{2}$: $R=\\frac{1}{2}$", (.5, 0), (.3, -1.25), arrowprops=dict(arrowstyle="->"), color=C[2])
    a.set_xlim(-1.8, 1.8); a.set_ylim(-1.6, 1.6); a.set_title("Legendre: singular points $x=\\pm1$ (red ×)\nR = distance to the nearest singular point"); a.set_xlabel("Re x"); a.set_ylabel("Im x")
    # Legendre non-integer p: even series partial sums
    a = ax[1]; p = 0.5; x = np.linspace(-1.15, 1.15, 600)
    def y1(N):
        co = [1.0]
        for n in range(0, 2*N, 2): co.append((n-p)*(n+p+1)/((n+1)*(n+2))*co[-1])
        return sum(c*x**(2*k) for k, c in enumerate(co))
    for N, c in ((5, C[1]), (20, C[2]), (80, C[0])): a.plot(x, y1(N), color=c, lw=1.4, label=f"{N+1} terms")
    a.axvline(-1, color="0.4", ls="--"); a.axvline(1, color="0.4", ls="--"); a.set_ylim(-3, 3); a.legend(fontsize=8)
    a.set_title(r"$(1-x^2)y''-2xy'+p(p+1)y=0$, $p=\frac{1}{2}$" "\npartial sums settle inside $|x|<1$, blow up outside"); a.set_xlabel("x")
    # Airy: all x
    a = ax[2]; x = np.linspace(-8, 4, 600); ai, aip, bi, bip = sc.airy(x)
    co = {0: 1.0, 1: 0.0, 2: 0.0}
    def airy_y1(N):
        a_ = [1.0, 0.0, 0.0]
        for n in range(1, N): a_.append(a_[n-1]/((n+2)*(n+1)))
        return sum(c*x**k for k, c in enumerate(a_))
    a.plot(x, airy_y1(60), color=C[0], lw=1.6, label=r"series $y_1=1+\frac{x^3}{6}+\dots$ (60 terms)")
    a.plot(x, airy_y1(15), color=C[1], lw=1.2, ls="--", label="15 terms (valid only near 0)")
    a.set_ylim(-5, 8); a.set_xlim(-8, 4); a.legend(fontsize=8); a.set_title("Airy $y''-xy=0$: no singular point,\n$R=\\infty$ (long series covers all of the window)"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-S2-radius-of-convergence.png")

# ------------------------------------------------------------------------------- Airy
def fig_airy():
    x = np.linspace(-10, 4, 800); ai, aip, bi, bip = sc.airy(x)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2)); a = ax[0]
    a.plot(x, ai, color=C[0], lw=2, label="Ai(x)"); a.plot(x, bi, color=C[1], lw=2, label="Bi(x)"); a.set_ylim(-1, 2); a.axhline(0, color="k", lw=.7); a.axvline(0, color="0.5", ls=":")
    a.legend(); a.set_title("Solutions of $y''=xy$\nx>0: exponential growth/decay (Ai decays);  x<0: oscillation"); a.set_xlabel("x")
    a = ax[1]; N = 40
    def ser(a0, a1):
        c = [a0, a1, 0.0]
        for n in range(1, N): c.append(c[n-1]/((n+2)*(n+1)))
        return sum(ck*x**k for k, ck in enumerate(c))
    f1, f2 = ser(1, 0), ser(0, 1); Ai0, Aip0 = sc.airy(0)[0], sc.airy(0)[1]
    a.plot(x, Ai0*f1+Aip0*f2, color=C[2], lw=2.4, label=r"$\mathrm{Ai}(0)\,y_1+\mathrm{Ai}'(0)\,y_2$ (40 terms)"); a.plot(x, ai, "k--", lw=1.2, label="Ai(x)")
    a.set_ylim(-1, 2); a.set_xlim(-6, 4); a.legend(fontsize=8); a.set_title("Ai is a specific combination of the two series $y_1$, $y_2$"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-S3-airy.png")

# ------------------------------------------------------------------------------- Hermite
def fig_hermite():
    from numpy.polynomial.hermite import hermval
    x = np.linspace(-3.2, 3.2, 600); fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    a = ax[0]
    for n in range(0, 5): a.plot(x, hermval(x, [0]*n+[1]), lw=1.6, label=f"$H_{n}$")
    a.set_ylim(-30, 30); a.legend(ncol=5, fontsize=8); a.set_title("Hermite polynomials: $y''-2xy'+2ny=0$\n(the series terminates when $n$ is a non-negative integer)")
    a = ax[1]
    for n in range(0, 5):
        nrm = 1/np.sqrt(2**n*sc.factorial(n)*np.sqrt(np.pi)); a.plot(x, nrm*hermval(x, [0]*n+[1])*np.exp(-x**2/2), lw=1.6, label=f"$\\psi_{n}$")
    a.legend(ncol=5, fontsize=8); a.set_title(r"$\psi_n=c_nH_n(x)e^{-x^2/2}$ (quantum oscillator states)" "\nwhy the polynomials matter in physics")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-S4-hermite.png")

# ------------------------------------------------------------------------------- Legendre's equation: P_n and Q_n
def Qn(n, x):
    Q0 = .5*np.log((1+x)/(1-x));
    if n == 0: return Q0
    Q1 = x*Q0-1
    if n == 1: return Q1
    q0, q1 = Q0, Q1
    for k in range(1, n): q0, q1 = q1, ((2*k+1)*x*q1-k*q0)/(k+1)
    return q1
def fig_legendre_eq():
    x = np.linspace(-.995, .995, 800); fig, ax = plt.subplots(1, 3, figsize=(14.5, 4.3))
    a = ax[0]
    for n in range(0, 5): a.plot(x, sc.eval_legendre(n, x), lw=1.6, label=f"$P_{n}$")
    a.set_ylim(-1.1, 1.1); a.legend(ncol=5, fontsize=8); a.set_title("polynomial solution $P_n$ (bounded on [−1, 1])")
    a = ax[1]
    for n in range(0, 4): a.plot(x, Qn(n, x), lw=1.6, label=f"$Q_{n}$")
    a.set_ylim(-3, 3); a.legend(ncol=4, fontsize=8); a.set_title("second solution $Q_n$ (infinite series, log-singular at $x=\\pm1$)")
    a = ax[2]; p = 2
    ev = np.array([1+0*x]); co = [1.0]
    for n in range(0, 80, 2): co.append((n-p)*(n+p+1)/((n+1)*(n+2))*co[-1])
    y1 = sum(c*x**(2*k) for k, c in enumerate(co)); a.plot(x, y1/ y1[-1] if False else -.5*(1-3*x**2), color=C[0], lw=2, label=r"$p=2$: $y_1$ terminates: $-\frac{1}{2}(1-3x^2)=P_2$")
    po = 2.5; co = [1.0]
    for n in range(0, 200, 2): co.append((n-po)*(n+po+1)/((n+1)*(n+2))*co[-1])
    a.plot(x, sum(c*x**(2*k) for k, c in enumerate(co)), color=C[1], lw=2, label=r"$p=2.5$: infinite series (log-singular at $\pm1$)")
    a.set_ylim(-2, 4); a.legend(fontsize=8); a.set_title("integer $p$ terminates; non-integer $p$ does not")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-S5-legendre-equation.png")

if __name__ == "__main__":
    for f in (fig_power_series, fig_radius, fig_airy, fig_hermite, fig_legendre_eq): f()
