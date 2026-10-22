"""Figures for the EXISTING concept notes (Lectures 1-14) that had no visuals.  Run `python de_viz_old.py`."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import special as sc, integrate

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote", name)

def field(ax, f, xr, yr, n=19, color="0.55", scale=.55):
    X, Y = np.meshgrid(np.linspace(*xr, n), np.linspace(*yr, n)); S = f(X, Y); S = np.where(np.isfinite(S), S, 1e6)
    L = np.sqrt(1+S**2); dx = scale*(xr[1]-xr[0])/n/L*1.0; dy = scale*(yr[1]-yr[0])/n*S/L*1.0
    ax.quiver(X, Y, dx, dy, angles="xy", scale_units="xy", scale=1, color=color, headwidth=0, headlength=0, headaxislength=0, pivot="mid", width=.003)

# ----------------------------------------------------------------------------------------------------------------- Isoclines
def fig_isoclines():
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.3))
    xr, yr = (-3, 3), (-3, 3)
    xs = np.linspace(-3, 3, 200)
    # y' = x : isoclines vertical lines, solutions parabolas
    a = ax[0]; field(a, lambda X, Y: X, xr, yr)
    for c in (-2, -1, 0, 1, 2): a.axvline(c, color=C[4], lw=1, ls="--"); a.text(c+.05, 2.75, f"c={c}", color=C[4], fontsize=8)
    for K in (-2, -1, 0, 1, 2): a.plot(xs, xs**2/2+K, color=C[0], lw=1.6)
    a.set_title(r"$y'=x$: isoclines $x=c$ (vertical)" "\n" r"solutions $y=x^2/2+K$")
    # y' = -x/y : isoclines y = -x/c, solutions circles
    a = ax[1]; field(a, lambda X, Y: -X/np.where(np.abs(Y) < 1e-9, 1e-9, Y), xr, yr)
    for c in (-2, -1, -.5, .5, 1, 2): a.plot(xs, -xs/c, color=C[4], lw=1, ls="--")
    th = np.linspace(0, 2*np.pi, 300)
    for r in (1, 2, 2.9): a.plot(r*np.cos(th), r*np.sin(th), color=C[0], lw=1.6)
    a.set_title(r"$y'=-x/y$: isoclines = lines through $O$" "\n" r"solutions = circles $x^2+y^2=r^2$")
    # y' = x - y : isoclines y = x - c ; solutions y = x-1+K e^-x
    a = ax[2]; field(a, lambda X, Y: X-Y, xr, yr)
    for c in (-2, -1, 0, 1, 2): a.plot(xs, xs-c, color=C[4], lw=1, ls="--")
    for K in (-3, -1, 0, 1, 3): a.plot(xs, xs-1+K*np.exp(-xs), color=C[0], lw=1.6)
    a.plot(xs, xs-1, color=C[1], lw=2, label=r"$y=x-1$ (attractor)"); a.legend(loc="lower right", fontsize=8)
    a.set_title(r"$y'=x-y$: isoclines $y=x-c$" "\n" r"solutions approach $y=x-1$")
    for a in ax: a.set_xlim(xr); a.set_ylim(yr); a.set_xlabel("x"); a.set_ylabel("y"); a.set_aspect("equal")
    fig.suptitle("Direction fields: isoclines (dashed orange, constant slope) vs solution curves (blue)", y=1.02); fig.tight_layout(); save(fig, "DE-E1-isoclines.png")

# ----------------------------------------------------------------------------------------------------------------- Exact
def fig_exact():
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.4)); X, Y = np.meshgrid(np.linspace(-2, 2, 300), np.linspace(-2, 2, 300))
    a = ax[0]; F = X**2*Y+3*X-Y; cs = a.contour(X, Y, F, levels=np.arange(-9, 10, 1.5), colors="#1f77b4", linewidths=1.3)
    a.set_title(r"Ex. 1: $F=x^2y+3x-y=C$"); a.clabel(cs, fontsize=7)
    a = ax[1]; F = X*np.exp(Y)+Y**2; cs = a.contour(X, Y, F, levels=np.arange(0, 14, 1), colors="#1f77b4", linewidths=1.3)
    a.set_title(r"Ex. 3: $F=xe^y+y^2=C$"); a.clabel(cs, fontsize=7)
    a = ax[2]; Xg, Yg = np.meshgrid(np.linspace(-2, 2, 15), np.linspace(-2, 2, 15)); M = 2*Xg*Yg+3; N = Xg**2-1
    nm = np.hypot(M, N)+1e-9; a.quiver(Xg, Yg, M/nm, N/nm, color="0.45", width=.004); a.set_title(r"Ex. 1: $\nabla F=(M,N)$ (arrows) $\perp$ level curves")
    a.contour(X, Y, X**2*Y+3*X-Y, levels=np.arange(-9, 10, 1.5), colors="#1f77b4", linewidths=1.2)
    for a in ax: a.set_xlabel("x"); a.set_ylabel("y"); a.set_aspect("equal")
    fig.suptitle(r"Exact equation $M\,dx+N\,dy=0$: the solutions are the level curves of the potential $F(x,y)$", y=1.02); fig.tight_layout(); save(fig, "DE-E2-exact-level-curves.png")

# ----------------------------------------------------------------------------------------------------------------- Existence/uniqueness
def fig_existence():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2)); x = np.linspace(-.5, 3, 400)
    a = ax[0]; a.plot(x, np.exp(x), color=C[0], lw=2, label=r"$y=e^x$ (unique)")
    for K in (-1, -.5, .5, 1): a.plot(x, (1+K)*np.exp(x) if False else (1+K)*np.exp(x), color="0.7", lw=1)
    a.set_title(r"$y'=y$, $y(0)=1$: Lipschitz holds, one solution"); a.set_ylim(0, 12); a.legend()
    a = ax[1]; xx = np.linspace(0, 3, 300); a.plot(xx, np.zeros_like(xx), color=C[0], lw=2.4, label=r"$y\equiv0$")
    a.plot(xx, (2*xx/3)**1.5, color=C[1], lw=2.4, label=r"$y=(2x/3)^{3/2}$")
    for c in (.5, 1.0, 1.7):
        yy = np.where(xx > c, (2*(xx-c)/3)**1.5, 0.); a.plot(xx, yy, color=C[2], lw=1.2, alpha=.9)
    a.plot([], [], color=C[2], label="leave $y=0$ at any $x=c$"); a.legend(fontsize=8)
    a.set_title(r"$y'=y^{1/3}$, $y(0)=0$: Lipschitz fails at $y=0$," "\n" "infinitely many solutions"); a.set_xlabel("x")
    ax[0].set_xlabel("x"); ax[0].set_ylabel("y"); ax[1].set_ylabel("y"); fig.tight_layout(); save(fig, "DE-E3-uniqueness.png")

# ----------------------------------------------------------------------------------------------------------------- Applications
def fig_applications():
    fig, ax = plt.subplots(1, 3, figsize=(13.5, 3.8)); t = np.linspace(0, 5, 300)
    a = ax[0]
    for k in (.3, .6, 1.0): a.plot(t, np.exp(k*t), lw=2, label=f"k={k}")
    a.set_ylim(0, 25); a.set_title(r"Growth $P=P_0e^{kt}$"); a.legend(); a.set_xlabel("t")
    a = ax[1]
    for lam in (.3, .6, 1.0): a.plot(t, np.exp(-lam*t), lw=2, label=fr"$\lambda$={lam}")
    th = np.log(2)/.6; a.axvline(th, color="0.5", ls=":"); a.text(th+.05, .85, "half-life\n$\\ln2/\\lambda$", fontsize=8)
    a.set_title(r"Decay $N=N_0e^{-\lambda t}$"); a.legend(); a.set_xlabel("t")
    a = ax[2]
    for T0 in (100, 60, -10): a.plot(t, 20+(T0-20)*np.exp(-.7*t), lw=2, label=fr"$T_0$={T0}")
    a.axhline(20, color="k", ls="--", lw=1); a.text(3.6, 22, r"$T_s=20$", fontsize=9); a.set_title(r"Cooling $T=T_s+(T_0-T_s)e^{-kt}$"); a.legend(fontsize=8); a.set_xlabel("t")
    fig.tight_layout(); save(fig, "DE-E4-applications.png")

# ----------------------------------------------------------------------------------------------------------------- Linear & Bernoulli
def fig_linear_bernoulli():
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.2)); x = np.linspace(-1, 4, 400)
    a = ax[0]
    for K in (-3, -1, 0, 1, 3): a.plot(x, np.exp(-2*x)*(x+K), color=C[0], lw=1.6)
    a.set_ylim(-3, 6); a.set_title(r"$y'+2y=e^{-2x}$:  $y=e^{-2x}(x+C)$" "\n" "all curves decay to 0 (integrating factor $e^{2x}$)")
    a = ax[1]; xs = np.linspace(-3, 4, 400)
    for K in (-3, -1, 0, 1, 3):
        v = xs+K; yy = np.sign(v)*np.abs(v)**(1/3)*np.exp(-xs/3); a.plot(xs, yy, color=C[0], lw=1.6)
    a.set_ylim(-3, 3); a.set_title(r"Bernoulli $3y^2y'+y^3=e^{-x}$:  $y=(x+C)^{1/3}e^{-x/3}$" "\n" r"$v=y^3$ makes it linear: $v'+v=e^{-x}$"); a.set_xlim(-3, 4)
    a = ax[2]; xs = np.linspace(-1, 1.2, 600)
    for Cc in (-1, -.3, 0, .3, 1):
        base = xs+1/3+Cc*np.exp(3*xs); yy = np.where(base > 0, np.abs(base)**(-1/3), np.nan); a.plot(xs, yy, color=C[1], lw=1.6)
    a.set_ylim(0, 4); a.set_title(r"Bernoulli $y'=y(xy^3-1)$:  $y=[x+\frac{1}{3}+Ce^{3x}]^{-1/3}$" "\n" "solutions blow up where the bracket reaches 0")
    for a in ax: a.set_xlabel("x"); a.set_ylabel("y")
    fig.tight_layout(); save(fig, "DE-E5-linear-bernoulli.png")

# ----------------------------------------------------------------------------------------------------------------- Wronskian
def fig_wronskian():
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.2)); x = np.linspace(-2, 2, 400)
    a = ax[0]; a.plot(x, np.exp(x), color=C[0], lw=2, label="$e^x$"); a.plot(x, np.exp(2*x), color=C[1], lw=2, label="$e^{2x}$"); a.plot(x, np.exp(3*x), color=C[2], lw=2, ls="--", label=r"$W=e^{3x}>0$")
    a.set_ylim(-.5, 8); a.legend(); a.set_title(r"Independent: $W(e^x,e^{2x})=e^{3x}\neq0$")
    a = ax[1]; a.plot(x, np.sin(x), color=C[0], lw=2, label=r"$\sin x$"); a.plot(x, 2*np.sin(x), color=C[1], lw=2, label=r"$2\sin x$"); a.plot(x, 0*x, color=C[2], lw=2, ls="--", label=r"$W\equiv0$"); a.legend()
    a.set_title(r"Dependent: $y_2=2y_1\Rightarrow W\equiv0$")
    a = ax[2]; f1 = x**3; f2 = np.abs(x)**3; W = f1*(3*x*np.abs(x))-f2*3*x**2
    a.plot(x, f1, color=C[0], lw=2, label=r"$x^3$"); a.plot(x, f2, color=C[1], lw=2, label=r"$|x|^3$"); a.plot(x, W, color=C[2], lw=2, ls="--", label=r"$W\equiv0$"); a.legend()
    a.set_title(r"$W\equiv0$ but independent!" "\n" "(not solutions of one linear ODE with continuous coefficients)")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-E6-wronskian.png")

# ----------------------------------------------------------------------------------------------------------------- Constant coefficients
def fig_constant_coeff():
    fig = plt.figure(figsize=(14, 4.6)); gs = fig.add_gridspec(1, 4, width_ratios=[1.1, 1, 1, 1]); x = np.linspace(0, 6, 400)
    a = fig.add_subplot(gs[0]); a.axhline(0, color="k", lw=.8); a.axvline(0, color="k", lw=.8)
    for (re, im, c, m) in ((-1, 0, C[0], "o"), (-3, 0, C[0], "o"), (-1, 0, C[2], "s"), (-.5, 3, C[1], "^"), (-.5, -3, C[1], "^")): pass
    a.plot([-1, -3], [0, 0], "o", color=C[0], ms=9, label="real distinct"); a.plot([-1.5], [0], "s", color=C[2], ms=9, label="repeated")
    a.plot([-.5, -.5], [2.5, -2.5], "^", color=C[1], ms=9, label=r"complex $\alpha\pm i\beta$"); a.set_xlim(-4, 1); a.set_ylim(-4, 4)
    a.set_title("roots of $r^2+ar+b$ (stable half-plane)"); a.set_xlabel("Re r"); a.set_ylabel("Im r"); a.legend(fontsize=8, loc="upper left")
    a = fig.add_subplot(gs[1]); a.plot(x, 3*np.exp(-x)-2*np.exp(-3*x), color=C[0], lw=2); a.plot(x, -np.exp(-x)+2*np.exp(-3*x), color=C[0], lw=1.2, ls="--"); a.set_title(r"distinct: $c_1e^{r_1x}+c_2e^{r_2x}$" "\n" "(overdamped)")
    a = fig.add_subplot(gs[2]); a.plot(x, (1+3*x)*np.exp(-1.5*x), color=C[2], lw=2); a.plot(x, (1-1*x)*np.exp(-1.5*x), color=C[2], lw=1.2, ls="--"); a.set_title(r"repeated: $(c_1+c_2x)e^{rx}$" "\n" "(critically damped)")
    a = fig.add_subplot(gs[3]); a.plot(x, np.exp(-.5*x)*np.cos(3*x), color=C[1], lw=2); a.plot(x, np.exp(-.5*x), color="0.5", ls=":"); a.plot(x, -np.exp(-.5*x), color="0.5", ls=":"); a.set_title(r"complex: $e^{\alpha x}(c_1\cos\beta x+c_2\sin\beta x)$" "\n" "(underdamped)")
    for a in fig.axes[1:]: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-E7-constant-coefficients.png")

# ----------------------------------------------------------------------------------------------------------------- Resonance (undetermined coefficients)
def fig_resonance():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.2)); t = np.linspace(0, 40, 2000)
    a = ax[0]; a.plot(t, .5*t*np.sin(t), color=C[1], lw=1.6, label=r"$y''+y=\cos x$:  $y_p=\frac{1}{2}x\sin x$")
    a.plot(t, .5*t, color="0.6", ls=":"); a.plot(t, -.5*t, color="0.6", ls=":"); a.legend(fontsize=8, loc="upper left"); a.set_title("Resonance: RHS is a solution of the homogeneous equation" "\n" r"$\Rightarrow$ trial form must be multiplied by $x$")
    a = ax[1]; w = 1.3; yp = (np.cos(w*t)-np.cos(t))/(1-w**2); a.plot(t, yp, color=C[0], lw=1.4, label=r"$y''+y=\cos 1.3x$ (beats)")
    a.plot(t, np.cos(w*t)/(1-w**2), color="0.7", lw=1, label=r"$y_p=\cos(1.3x)/(1-1.3^2)$"); a.legend(fontsize=8, loc="upper right"); a.set_title(r"Near resonance: bounded beats (no $x$-factor needed)")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-E8-resonance.png")

# ----------------------------------------------------------------------------------------------------------------- Cauchy-Euler
def fig_cauchy_euler():
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.2)); x = np.linspace(.15, 4, 500)
    a = ax[0]; a.plot(x, x**2, color=C[0], lw=2, label="$x^2$"); a.plot(x, x**-1, color=C[1], lw=2, label="$x^{-1}$"); a.plot(x, 2*x**2-x**-1, color=C[2], lw=1.6, ls="--", label="$2x^2-x^{-1}$"); a.set_ylim(-4, 8); a.legend()
    a.set_title(r"distinct roots $m=2,-1$:  $C_1x^{m_1}+C_2x^{m_2}$")
    a = ax[1]; a.plot(x, x, color=C[0], lw=2, label="$x$"); a.plot(x, x*np.log(x), color=C[1], lw=2, label=r"$x\ln x$"); a.plot(x, x*(1+np.log(x)), color=C[2], lw=1.6, ls="--", label=r"$x(1+\ln x)$"); a.set_ylim(-1.5, 6); a.legend()
    a.set_title(r"repeated root $m=1$:  $x^m(C_1+C_2\ln x)$")
    a = ax[2]; xl = np.linspace(.03, 4, 1500); a.plot(xl, xl**.5*np.cos(2*np.log(xl)), color=C[0], lw=2, label=r"$x^{1/2}\cos(2\ln x)$"); a.plot(xl, xl**.5*np.sin(2*np.log(xl)), color=C[1], lw=2, label=r"$x^{1/2}\sin(2\ln x)$")
    a.plot(xl, xl**.5, color="0.6", ls=":"); a.plot(xl, -xl**.5, color="0.6", ls=":"); a.legend(fontsize=8); a.set_title(r"$m=\frac{1}{2}\pm2i$:  oscillates in $\ln x$ (infinitely often as $x\to0$)")
    for a in ax: a.set_xlabel("x")
    fig.tight_layout(); save(fig, "DE-E9-cauchy-euler.png")

if __name__ == "__main__":
    for f in (fig_isoclines, fig_exact, fig_existence, fig_applications, fig_linear_bernoulli, fig_wronskian, fig_constant_coeff, fig_resonance, fig_cauchy_euler): f()
