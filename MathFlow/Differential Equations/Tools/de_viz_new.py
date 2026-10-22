"""Figures for the NEW notes (Lectures 15-25: Frobenius cases, Legendre, Gamma, Bessel).  Run `python de_viz_new.py`."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon
from scipy import special as sc, integrate
import sympy as sp

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote", name)
P = lambda n, x: sc.eval_legendre(n, x)

# ======================================================================================================================
# Frobenius
# ======================================================================================================================
def fig_frobenius_cases():
    fig, ax = plt.subplots(1, 4, figsize=(16, 4.2)); x = np.linspace(.02, 4, 800)
    a = ax[0]  # indicial-root positions
    a.set_xlim(-2.5, 2.5); a.set_ylim(-1, 3.4); a.axis("off")
    for yy, (r1, r2, lab, c) in zip((2.8, 1.8, .8, -.2), ((1, -.5, "Case I   r1 - r2 = 3/2  (not an integer)", C[0]), (0, 0, "Case II   r1 = r2", C[1]), (.5, -.5, "Case III   r1 - r2 = 1 (integer), no log", C[2]), (1, -1, "Case III   r1 - r2 = 2 (integer), log forced", C[3]))):
        a.plot([-2.3, 2.3], [yy, yy], color="0.7", lw=1); a.plot([r1], [yy], "o", color=c, ms=10); a.plot([r2], [yy], "s", color=c, ms=9, mfc="none", mew=2)
        a.text(-2.4, yy+.28, lab, fontsize=8.5, color=c)
    a.set_title("indicial roots: larger root r1 (o), smaller r2 (square)", fontsize=9)
    a = ax[1]; a.plot(x, x*(1+x/5+x**2/70), color=C[0], lw=2, label=r"$y_1=x(1+x/5+x^2/70+\dots)$"); a.plot(x, x**-.5*(1-x-x**2/2-x**3/18), color=C[1], lw=2, label=r"$y_2=x^{-1/2}(1-x-x^2/2-\dots)$")
    a.set_ylim(-1, 6); a.legend(fontsize=8); a.set_title("Case I: two Frobenius series, no logarithm\n" r"$2x^2y''+xy'-(x+1)y=0$")
    a = ax[2]; a.plot(x, sc.j0(x), color=C[0], lw=2, label=r"$y_1=J_0(x)$"); a.plot(x, sc.y0(x), color=C[1], lw=2, label=r"$y_2=J_0\ln x+\sum\dots\ (\propto Y_0)$"); a.set_ylim(-2, 1.2); a.legend(fontsize=8)
    a.set_title("Case II: repeated root, the logarithm is forced\n" r"$xy''+y'+xy=0$")
    a = ax[3]; a.plot(x, sc.jv(1, x), color=C[0], lw=2, label=r"$J_1$ ($r_1=1$)"); a.plot(x, sc.yv(1, x), color=C[1], lw=2, label=r"$Y_1$ ($r_2=-1$, log + $x^{-1}$)")
    a.plot(x, sc.jv(.5, x), color=C[2], lw=1.8, ls="--", label=r"$J_{1/2}$ (no log)"); a.plot(x, sc.jv(-.5, x), color=C[4], lw=1.8, ls="--", label=r"$J_{-1/2}$ (no log)")
    a.set_ylim(-2.5, 1.5); a.legend(fontsize=8); a.set_title("Case III: integer gap. Order 1/2: no log;  order 1: log")
    for a in ax[1:]: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N1-frobenius-cases.png")

def fig_frobenius_examples():
    x = np.linspace(.01, 6, 800); fig, ax = plt.subplots(1, 4, figsize=(16, 4))
    a = ax[0]; a.plot(x, np.cos(np.sqrt(x)), color=C[0], lw=2, label=r"$\cos\sqrt{x}$"); a.plot(x, np.sin(np.sqrt(x)), color=C[1], lw=2, label=r"$\sin\sqrt{x}$")
    for N, ls in ((2, ":"), (5, "--")):
        s = sum((-1)**k*x**k/float(sp.factorial(2*k)) for k in range(N)); a.plot(x, s, color=C[0], ls=ls, lw=1, label=f"series, {N} terms")
    a.set_ylim(-1.5, 1.5); a.legend(fontsize=8); a.set_title(r"$4xy''+2y'+y=0$: $r=0,\frac{1}{2}$" "\nseries = $\\cos\\sqrt{x}$, $\\sin\\sqrt{x}$")
    a = ax[1]; xx = np.linspace(.02, .98, 500); a.plot(xx, 1/(1-xx), color=C[0], lw=2, label=r"$y_1=\frac{1}{1-x}=\sum x^m$"); a.plot(xx, np.log(xx)/(1-xx), color=C[1], lw=2, label=r"$y_2=\frac{\ln x}{1-x}$")
    a.set_ylim(-8, 8); a.legend(fontsize=8); a.set_title(r"$(x^2-x)y''+(3x-1)y'+y=0$: $r=0,0$" "\nCase II, log needed")
    a = ax[2]; xx = np.linspace(.03, 5, 600); a.plot(xx, 1/xx, color=C[0], lw=2, label=r"$x^{-1}$"); a.plot(xx, np.log(xx)/xx, color=C[1], lw=2, label=r"$x^{-1}\ln x$"); a.set_ylim(-4, 6); a.legend(fontsize=8)
    a.set_title(r"$x^2y''+3xy'+y=0$: $r=-1,-1$" "\nEuler equation, Case II")
    a = ax[3]; xx = np.linspace(.01, 4, 600)
    def ser(r, N=12):
        c = [1.0]
        for n in range(1, N): c.append(-c[-1]/(2*(n+r)*(n+r-1)-(n+r)+1))
        return xx**r*sum(ck*xx**k for k, ck in enumerate(c))
    a.plot(xx, ser(1), color=C[0], lw=2, label=r"$r=1$"); a.plot(xx, ser(.5), color=C[1], lw=2, label=r"$r=\frac{1}{2}$"); a.set_ylim(-1.2, 1.2); a.legend(fontsize=8)
    a.set_title(r"$2x^2y''-xy'+(1+x)y=0$: $r=1,\frac{1}{2}$" "\nCase I")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N2-frobenius-examples.png")

# ======================================================================================================================
# Legendre
# ======================================================================================================================
def fig_legendre_poly():
    x = np.linspace(-1, 1, 600); fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
    a = ax[0]
    for n in range(0, 6): a.plot(x, P(n, x), lw=1.7, label=f"$P_{n}$")
    a.plot([1], [1], "ko"); a.legend(ncol=3, fontsize=8); a.set_title("$P_0\\ldots P_5$: all pass through (1, 1);\n$P_n$ has $n$ zeros in (−1, 1)"); a.set_xlabel("x")
    a = ax[1]; X = sp.symbols('x'); f = (X**2-1)**4
    xs = np.linspace(-1.1, 1.1, 600)
    for k in range(0, 5):
        d = sp.lambdify(X, sp.diff(f, X, k), "numpy"); y = d(xs)*np.ones_like(xs); y = y/np.max(np.abs(y)); a.plot(xs, y+ (4-k)*2.2, color=C[0], lw=1.6)
        zs = [float(r_) for r_ in sp.roots(sp.Poly(sp.diff(f, X, k), X)).keys() if r_.is_real]; a.plot(zs, [(4-k)*2.2]*len(zs), "o", color=C[1], ms=4)
        a.text(1.12, (4-k)*2.2, f"$D^{k}$", fontsize=9, va="center")
    a.set_yticks([]); a.set_title("Rodrigues: $D^k(x^2-1)^4$ gains a root per derivative\n(by Rolle); $D^4$ gives $P_4$"); a.set_xlabel("x"); a.set_xlim(-1.15, 1.3)
    a = ax[2]; n = np.arange(0, 11); vals1 = [float(P(k, 1.0)) for k in n]; valsm1 = [float(P(k, -1.0)) for k in n]; w = .35
    a.bar(n-w/2, vals1, w, color=C[0], label="$P_n(1)=1$"); a.bar(n+w/2, valsm1, w, color=C[1], label="$P_n(-1)=(-1)^n$"); a.bar(n, [P(k, 0.0) for k in n], .2, color=C[2], label="$P_n(0)$ (0 for odd $n$)")
    a.legend(fontsize=8); a.set_title("end-point and mid-point values"); a.set_xlabel("n")
    fig.tight_layout(); save(fig, "DE-N4-legendre-polynomials.png")

def fig_generating():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))
    a = ax[0]; a.set_aspect("equal"); a.set_xlim(-.4, 2.3); a.set_ylim(-.3, 1.7); a.axis("off")
    O, Q, R = np.array([0, 0]), np.array([1.8, 0]), np.array([1.0, 1.0]); th = np.arctan2(1, 1)
    a.plot([O[0], Q[0]], [O[1], Q[1]], "k", lw=1.8); a.plot([O[0], R[0]], [O[1], R[1]], color=C[0], lw=2); a.plot([R[0], Q[0]], [R[1], Q[1]], color=C[1], lw=2.2)
    a.plot(*O, "ko"); a.plot(*Q, "o", color=C[1]); a.plot(*R, "o", color=C[0])
    a.text(.35, .62, "$r'$", color=C[0], fontsize=12); a.text(.7, -.18, "$r$", fontsize=12); a.text(1.55, .55, "$d=\\sqrt{r^2-2rr'\\cos\\theta+r'^2}$", color=C[1], fontsize=10, rotation=-52)
    a.text(.35, .12, "$\\theta$", fontsize=12); a.text(-.35, 1.55, "$\\dfrac{1}{d}=\\dfrac{1}{r}\\sum_n P_n(\\cos\\theta)\\left(\\dfrac{r'}{r}\\right)^n$", fontsize=11)
    a.set_title("Where it comes from: potential of a point source\n$x=\\cos\\theta$, $t=r'/r$")
    a = ax[1]; x = np.linspace(-1, 1, 400); t = .6; G = 1/np.sqrt(1-2*x*t+t*t); a.plot(x, G, "k", lw=2.4, label=r"$G(x,t)=(1-2xt+t^2)^{-1/2}$, $t=0.6$")
    for N, c in ((1, C[1]), (3, C[2]), (6, C[0])): a.plot(x, sum(P(n, x)*t**n for n in range(N+1)), color=c, lw=1.4, label=f"$\\sum_{{n\\leq{N}}}P_nt^n$")
    a.legend(fontsize=8); a.set_xlabel("x"); a.set_title("partial sums converge for $|t|<1$")
    a = ax[2]; n = np.arange(0, 41)
    for x0, c in ((1.0, C[1]), (0.5, C[0]), (0.2, C[2]), (-1.0, C[3])):
        a.semilogy(n, np.abs(P(n, x0))+1e-17, "o-", ms=3, color=c, label=f"$|P_n({x0:g})|$")
    a.set_ylim(1e-3, 3); a.set_xlabel("n"); a.set_title("coefficients of $t^n$ stay $\leq 1$ in size, hence radius $|t|<1$"); a.legend(fontsize=8)
    fig.tight_layout(); save(fig, "DE-N5-generating-function.png")

def fig_inner_product():
    n = 6; xs = sp.symbols('x')
    mono = np.array([[float(sp.integrate(xs**(i+j), (xs, -1, 1))) for j in range(n)] for i in range(n)])
    leg = np.array([[float(sp.integrate(sp.legendre(i, xs)*sp.legendre(j, xs), (xs, -1, 1))) for j in range(n)] for i in range(n)])
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))
    for a, M, ttl in ((ax[0], mono, r"Gram matrix of monomials $\langle x^i,x^j\rangle$" "\n(not orthogonal)"), (ax[1], leg, r"Gram matrix of $P_i$: $\langle P_i,P_j\rangle$" "\n(diagonal = 2/(2n+1))")):
        im = a.imshow(M, cmap="viridis"); a.set_xticks(range(n)); a.set_yticks(range(n)); a.grid(False); a.set_title(ttl)
        for i in range(n):
            for j in range(n): a.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", color="w" if M[i, j] < M.max()*.6 else "k", fontsize=7.5)
    a = ax[2]; x = np.linspace(-np.pi, np.pi, 500)
    for k, c in zip((1, 2, 3), C): a.plot(x, np.sin(k*x), color=c, lw=1.6, label=f"$\\sin {k}x$")
    a.plot(x, np.sin(x)*np.sin(2*x), "k--", lw=1.2, label=r"$\sin x\,\sin2x$: area 0"); a.legend(fontsize=8); a.set_title("another orthogonal system on $[-\\pi,\\pi]$"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N6-inner-product.png")

def fig_orthogonality():
    x = np.linspace(-1, 1, 800); fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
    a = ax[0]; a.plot(x, P(2, x)*P(3, x), color=C[0], lw=2); a.fill_between(x, 0, P(2, x)*P(3, x), where=P(2, x)*P(3, x) > 0, color=C[2], alpha=.4); a.fill_between(x, 0, P(2, x)*P(3, x), where=P(2, x)*P(3, x) < 0, color=C[1], alpha=.4)
    a.set_title(r"$P_2P_3$ is odd: green and red areas cancel" "\n" r"$\int_{-1}^1P_2P_3\,dx=0$"); a.set_xlabel("x")
    a = ax[1]; a.plot(x, P(3, x)*P(5, x), color=C[0], lw=2, label=r"$P_3P_5$"); a.plot(x, P(2, x)*P(4, x), color=C[4], lw=2, label=r"$P_2P_4$"); a.fill_between(x, 0, P(2, x)*P(4, x), color=C[4], alpha=.2)
    a.legend(fontsize=8); a.set_title("even products also integrate to 0 when $m\\neq n$\n(positive and negative lobes balance)"); a.set_xlabel("x")
    a = ax[2]; n = np.arange(0, 9); a.bar(n, 2/(2*n+1), color=C[0]); [a.text(k, 2/(2*k+1)+.03, f"2/{2*k+1}", ha="center", fontsize=8) for k in n]
    a.set_title(r"norms: $\int_{-1}^1P_n^2\,dx=\dfrac{2}{2n+1}$" "\n" r"orthonormal family: $\sqrt{\frac{2n+1}{2}}\,P_n$"); a.set_xlabel("n"); a.set_ylim(0, 2.3)
    fig.tight_layout(); save(fig, "DE-N7-orthogonality-norm.png")

def legendre_partial(f, N, x, a=-1, b=1):
    out = 0*x; cs = []
    for n in range(N+1):
        c = (2*n+1)/2*integrate.quad(lambda q: f(q)*P(n, q), -1, 1, points=[0], limit=200)[0]; cs.append(c); out = out+c*P(n, x)
    return out, cs
def fig_legendre_series():
    x = np.linspace(-1, 1, 1200); fig, ax = plt.subplots(2, 3, figsize=(15, 8))
    funs = (("$|x|$", np.abs), ("sign(x)", np.sign), ("$x$ on $[0,1]$, 0 on $[-1,0]$", lambda q: q if q > 0 else 0.0))
    for j, (nm, f) in enumerate(funs):
        a = ax[0, j]; fv = np.array([f(q) for q in x]); a.plot(x, fv, "k", lw=2.2, label="f")
        for N, c in ((1, C[1]), (3, C[2]), (7, C[4]), (15, C[0])):
            y, cs = legendre_partial(f, N, x); a.plot(x, y, color=c, lw=1.3, label=f"$N={N}$")
        a.set_title(f"Legendre partial sums of {nm}"); a.legend(fontsize=7, ncol=3); a.set_xlabel("x"); a.set_ylim(-1.5, 1.5)
        a = ax[1, j]; y, cs = legendre_partial(f, 14, x); a.bar(range(len(cs)), cs, color=C[0]); a.set_title("coefficients $a_n=\\frac{2n+1}{2}\\int fP_n$"); a.set_xlabel("n")
    fig.tight_layout(); save(fig, "DE-N8-legendre-series.png")
    # least squares vs Taylor
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2)); f = np.exp
    n = 3; y, cs = legendre_partial(f, n, x); tay = sum(x**k/float(sp.factorial(k)) for k in range(n+1))
    a = ax[0]; a.plot(x, f(x)-y, color=C[0], lw=2, label="Legendre truncation (min $L^2$ error)"); a.plot(x, f(x)-tay, color=C[1], lw=2, label="Taylor truncation")
    a.legend(fontsize=8); a.set_title(r"error in approximating $e^x$ by a cubic"); a.set_xlabel("x")
    a = ax[1]; N = np.arange(1, 11); e_l, e_t = [], []
    for k in N:
        y, _ = legendre_partial(f, k, x); tay = sum(x**j/float(sp.factorial(j)) for j in range(k+1)); e_l.append(np.sqrt(np.trapezoid((f(x)-y)**2, x))); e_t.append(np.sqrt(np.trapezoid((f(x)-tay)**2, x)))
    a.semilogy(N, e_l, "o-", color=C[0], label="Legendre"); a.semilogy(N, e_t, "s-", color=C[1], label="Taylor"); a.legend(); a.set_xlabel("degree"); a.set_ylabel("$L^2$ error"); a.set_title("Least squares: the Legendre truncation is always best")
    fig.tight_layout(); save(fig, "DE-N8b-least-squares.png")

def fig_recurrences():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); x = np.linspace(-1, 1, 400)
    a = ax[0]; n = 4; lhs = (2*n+1)*x*P(n, x); rhs = (n+1)*P(n+1, x)+n*P(n-1, x); a.plot(x, lhs, color=C[0], lw=4, alpha=.5, label=r"$(2n+1)xP_n$"); a.plot(x, rhs, "k--", lw=1.6, label=r"$(n+1)P_{n+1}+nP_{n-1}$"); a.legend(fontsize=8); a.set_title("three-term recurrence (I), $n=4$"); a.set_xlabel("x")
    a = ax[1]; n = 5; X = sp.symbols('x'); coef = {k: 2*k+1 for k in range(n-1, -1, -2)}
    a.bar(list(coef.keys()), list(coef.values()), color=C[0]); a.set_xticks(range(0, n)); a.set_title(r"Christoffel: $P_5'=9P_4+5P_2+P_0$" "\n" r"(bar height = coefficient $2k+1$)"); a.set_xlabel("k")
    a = ax[2]; ns = np.arange(1, 11); a.bar(ns, ns*(ns+1), color=C[2]); a.set_title(r"$\int_{-1}^1(P_n')^2dx=n(n+1)$"); a.set_xlabel("n")
    fig.tight_layout(); save(fig, "DE-N9-legendre-recurrences.png")

# ======================================================================================================================
# Gamma & Bessel
# ======================================================================================================================
def fig_gamma():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4)); x = np.linspace(-4.5, 5, 4000); y = sc.gamma(x); y[np.abs(y) > 25] = np.nan
    a = ax[0]; a.plot(x, y, color=C[0], lw=2); a.set_ylim(-8, 25); a.axhline(0, color="k", lw=.7)
    for k in range(0, 5): a.axvline(-k, color=C[1], ls=":", lw=1)
    xm = 1.4616321; a.plot(xm, sc.gamma(xm), "o", color=C[1]); a.annotate("min 0.8856 at 1.4616", (xm, sc.gamma(xm)), (1.8, 3.5), arrowprops=dict(arrowstyle="->"), fontsize=8)
    pts = np.arange(1, 6); a.plot(pts, sc.gamma(pts), "ks", ms=5); a.text(3.2, 12, "squares: $\\Gamma(n+1)=n!$", fontsize=8); a.set_title("$\\Gamma(x)$: poles at $0,-1,-2,\\dots$; sign alternates"); a.set_xlabel("x")
    a = ax[1]; xs = np.linspace(.05, 6, 400); a.semilogy(xs, sc.gamma(xs), color=C[0], lw=2, label=r"$\Gamma(x)$"); a.semilogy(pts, sc.factorial(pts-1), "ks", ms=5, label="$(n-1)!$"); a.legend(); a.set_title("interpolates the factorial"); a.set_xlabel("x")
    a = ax[2]; ths = np.array([-2.5, -1.5, -.5, .5, 1.5, 2.5]); a.stem(ths, sc.gamma(ths), basefmt="k-"); [a.text(t_, sc.gamma(t_)+(.5 if sc.gamma(t_) > 0 else -1.0), f"{sc.gamma(t_):.4f}", ha="center", fontsize=8) for t_ in ths]
    a.set_ylim(-5.5, 3.5); a.set_title(r"half-integer values: $\Gamma(\frac{1}{2})=\sqrt{\pi}$, $\Gamma(-\frac{5}{2})=-\frac{8\sqrt{\pi}}{15}=-0.9453$"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N10-gamma.png")

def fig_bessel_first():
    x = np.linspace(0, 20, 1000); fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
    a = ax[0]
    for n in range(0, 5): a.plot(x, sc.jv(n, x), lw=1.7, label=f"$J_{n}$")
    a.plot(x, np.sqrt(2/(np.pi*np.maximum(x, 1e-9))), "k:", lw=1); a.plot(x, -np.sqrt(2/(np.pi*np.maximum(x, 1e-9))), "k:", lw=1); a.set_ylim(-.6, 1.05); a.set_xlim(0, 20); a.legend(ncol=5, fontsize=8)
    a.set_title(r"$J_n(x)$ decays like $\sqrt{2/\pi x}$ (dotted envelope)"); a.set_xlabel("x")
    a = ax[1]; xx = np.linspace(0, 12, 600)
    a.plot(xx, sc.j0(xx), "k", lw=2.4, label=r"$J_0$")
    for N, c in ((2, C[1]), (4, C[2]), (8, C[0])):
        s = sum((-1)**k*(xx/2)**(2*k)/float(sp.factorial(k))**2 for k in range(N+1)); a.plot(xx, s, color=c, lw=1.2, label=f"{N+1} terms")
    a.set_ylim(-1.5, 1.5); a.legend(fontsize=8); a.set_title(r"series $\sum\frac{(-1)^k}{(k!)^2}(x/2)^{2k}$ converges for all $x$"); a.set_xlabel("x")
    a = ax[2]; z0 = sc.jn_zeros(0, 6); z1 = sc.jn_zeros(1, 6)
    a.plot(xx, sc.j0(xx), color=C[0], lw=1.8, label=r"$J_0$"); a.plot(xx, sc.jv(1, xx), color=C[1], lw=1.8, label=r"$J_1$"); a.plot(z0[z0 < 12], np.zeros((z0 < 12).sum()), "o", color=C[0]); a.plot(z1[z1 < 12], np.zeros((z1 < 12).sum()), "s", color=C[1])
    a.set_title("zeros: $J_0$: " + ", ".join(f"{z:.3f}" for z in z0[:3]) + "…\n$J_1$: " + ", ".join(f"{z:.3f}" for z in z1[:3]) + "…", fontsize=9); a.legend(fontsize=8); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N11-bessel-first-kind.png")

def fig_bessel_second():
    x = np.linspace(.05, 15, 1000); fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
    a = ax[0]
    for n in range(0, 4): a.plot(x, sc.yv(n, x), lw=1.7, label=f"$Y_{n}$")
    a.set_ylim(-2, 1); a.legend(ncol=4, fontsize=8); a.set_title("$Y_n(x)\\to-\\infty$ as $x\\to0^+$"); a.set_xlabel("x")
    a = ax[1]; xs = np.logspace(-3, 1, 300); a.semilogx(xs, sc.y0(xs), color=C[1], lw=2, label=r"$Y_0$"); a.semilogx(xs, 2/np.pi*np.log(xs/2)+2*0.5772156649/np.pi, "k--", label=r"$\frac{2}{\pi}(\ln\frac{x}{2}+\gamma)$")
    a.semilogx(xs, sc.j0(xs), color=C[0], lw=2, label=r"$J_0$"); a.set_ylim(-4, 1.5); a.legend(fontsize=8); a.set_title("small $x$: $Y_0\\sim\\frac{2}{\\pi}\\ln x$ (logarithmic)"); a.set_xlabel("x")
    a = ax[2]; nu = .3; xx = np.linspace(.05, 12, 600)
    a.plot(xx, sc.jv(nu, xx), color=C[0], lw=1.8, label=r"$J_{0.3}$"); a.plot(xx, sc.jv(-nu, xx), color=C[2], lw=1.8, label=r"$J_{-0.3}$"); a.plot(xx, sc.yv(nu, xx), color=C[1], lw=1.8, ls="--", label=r"$Y_{0.3}=\frac{J_\nu\cos\nu\pi-J_{-\nu}}{\sin\nu\pi}$")
    a.set_ylim(-2, 2); a.legend(fontsize=8); a.set_title("non-integer order: $J_{\\nu}$, $J_{-\\nu}$ independent; $Y_\\nu$ is a combination"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N12-bessel-second-kind.png")

def fig_bessel_props():
    x = np.linspace(.05, 20, 1000); fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
    a = ax[0]; env = np.sqrt(2/(np.pi*x))
    a.plot(x, sc.jv(.5, x), color=C[0], lw=2, label=r"$J_{1/2}=\sqrt{2/\pi x}\,\sin x$"); a.plot(x, sc.jv(-.5, x), color=C[1], lw=2, label=r"$J_{-1/2}=\sqrt{2/\pi x}\,\cos x$")
    a.plot(x, sc.jv(1.5, x), color=C[2], lw=1.6, ls="--", label=r"$J_{3/2}$"); a.plot(x, env, "k:"); a.plot(x, -env, "k:"); a.set_ylim(-1, 1); a.legend(fontsize=8); a.set_title("half-integer orders are elementary"); a.set_xlabel("x")
    a = ax[1]; z = 4.0; J0, J1 = sc.j0(z), sc.j1(z); J2 = 2/z*J1-J0; J3 = 4/z*J2-J1
    a.bar(range(4), [J0, J1, J2, J3], color=[C[0], C[0], C[4], C[4]]); [a.text(k, v+(.02 if v > 0 else -.05), f"{v:.6f}", ha="center", fontsize=8) for k, v in enumerate([J0, J1, J2, J3])]
    a.set_xticks(range(4)); a.set_xticklabels(["$J_0(4)$", "$J_1(4)$", "$J_2(4)$", "$J_3(4)$"]); a.set_title(r"recurrence $J_{n+1}=\frac{2n}{x}J_n-J_{n-1}$ climbs from $J_0,J_1$" "\n(blue = tabulated, orange = computed)", fontsize=9)
    a = ax[2]; xx = np.linspace(0, 12, 600); nu = 2
    a.plot(xx, sc.jvp(nu, xx), color=C[0], lw=3, alpha=.5, label=r"$J_2'$"); a.plot(xx, .5*(sc.jv(1, xx)-sc.jv(3, xx)), "k--", lw=1.4, label=r"$\frac{1}{2}(J_1-J_3)$"); a.legend(fontsize=8); a.set_title(r"derivative identity $2J_\nu'=J_{\nu-1}-J_{\nu+1}$"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-N13-bessel-properties.png")

def fig_bessel_generating():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.3)); x = 3.0; th = np.linspace(-np.pi, np.pi, 600)
    a = ax[0]; target = np.exp(1j*x*np.sin(th)).real; a.plot(th, target, "k", lw=3, alpha=.4, label=r"$\cos(x\sin\theta)$, $x=3$")
    for N, c in ((1, C[1]), (2, C[2]), (3, C[4]), (6, C[0])):
        s = sc.jv(0, x)+2*sum(sc.jv(2*k, x)*np.cos(2*k*th) for k in range(1, N+1)); a.plot(th, s, color=c, lw=1.2, label=f"terms $J_0\\ldots J_{{{2*N}}}$")
    a.legend(fontsize=7); a.set_xlabel(r"$\theta$"); a.set_title(r"put $t=e^{i\theta}$: $\cos(x\sin\theta)=J_0+2\sum J_{2k}\cos2k\theta$")
    a = ax[1]; t = .6; xs = np.linspace(0, 8, 300); a.plot(xs, np.exp(xs/2*(t-1/t)), "k", lw=3, alpha=.4, label=r"$e^{\frac{x}{2}(t-1/t)}$, $t=0.6$")
    a.plot(xs, sum(sc.jv(n, xs)*t**n for n in range(-12, 13)), color=C[0], lw=1.2, ls="--", label=r"$\sum_{n=-12}^{12}J_n(x)t^n$"); a.legend(fontsize=8); a.set_xlabel("x"); a.set_title("two-sided (Laurent) series in $t$")
    a = ax[2]; n = np.arange(-8, 9); a.bar(n, sc.jv(n, 3.0), color=[C[0] if k >= 0 else C[1] for k in n]); a.set_title(r"Laurent coefficients at $x=3$: $J_{-n}=(-1)^nJ_n$"); a.set_xlabel("n")
    fig.tight_layout(); save(fig, "DE-N14-bessel-generating.png")

if __name__ == "__main__":
    for f in (fig_frobenius_cases, fig_frobenius_examples, fig_legendre_poly, fig_generating, fig_inner_product, fig_orthogonality, fig_legendre_series, fig_recurrences, fig_gamma, fig_bessel_first, fig_bessel_second, fig_bessel_props, fig_bessel_generating): f()
