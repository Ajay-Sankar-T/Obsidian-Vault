"""Figures for the PDE notes (written to ../PDEs/assets/).   python de_pde_figs.py"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "05 Partial Differential Equations", "assets")
os.makedirs(OUT, exist_ok=True)
PI = np.pi
HYP, PAR, ELL = "#e8a33d", "#555555", "#3d7be8"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=150)
    plt.close(fig)


# ------------------------------------------------------------------------------ 1 characteristics and a Cauchy problem
def fig_characteristics():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3))
    # (n) u_x + 2x u_y = y, data on x = 0 :  characteristic base curves y - x^2 = c
    ax = axs[0]
    xs = np.linspace(-1.5, 1.5, 200)
    for c in np.arange(-1, 3.1, 0.5):
        ax.plot(xs, c + xs**2, color="#3d7be8", lw=1.2)
    ax.axvline(0, color="#d94a4a", lw=2.5, label="data curve  x = 0")
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 3.5)
    ax.set_title("A8 Q3(n): $u_x+2xu_y=y$, $u(0,y)=y^2$\nbase characteristics $y-x^2=c$ cross the data curve once")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.legend(loc="upper center", fontsize=8)
    # (q) u_x + u_y = 1 : data on y = x is itself a characteristic
    ax = axs[1]
    xs = np.linspace(-2, 2, 50)
    for c in np.arange(-3, 3.1, 0.75):
        ax.plot(xs, xs - c, color="#3d7be8", lw=1.2)
    ax.plot(xs, xs, color="#d94a4a", lw=3, label="data curve  y = x  (a characteristic)")
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_title("A8 Q3(q): $u_x+u_y=1$ with data on $y=x$\nthe data curve runs along a characteristic: no unique solution")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.legend(loc="lower right", fontsize=8)
    save(fig, "DE-PDE-characteristics.png")


# ------------------------------------------------------------------------------ 2 classification regions
def fig_regions():
    fig, axs = plt.subplots(2, 3, figsize=(11, 6.6))
    g = np.linspace(-4, 4, 801)
    X, Y = np.meshgrid(g, g)
    cases = [
        ("(b)  $yu_{xx}-xu_{xy}+yu_{yy}$:  $x^2-4y^2$", X**2 - 4 * Y**2),
        ("(c)  $(x+1)^2+(y-2)^2-1$", (X + 1)**2 + (Y - 2)**2 - 1),
        ("(h)  $x^2+y^2-1$", X**2 + Y**2 - 1),
        ("(i) Tricomi $yu_{xx}+u_{yy}$:  $-4y$", -Y),
        ("(l)  $xu_{xx}+yu_{yy}$:  $-4xy$", -X * Y),
        ("(m)  $y^2-4x$", Y**2 - 4 * X),
    ]
    for ax, (title, D) in zip(axs.flat, cases):
        ax.contourf(X, Y, np.where(D > 0, 1, 0), levels=[-0.5, 0.5, 1.5], colors=[ELL, HYP], alpha=0.55)
        ax.contour(X, Y, D, levels=[0], colors=[PAR], linewidths=2)
        ax.set_title(title, fontsize=9); ax.set_aspect("equal"); ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    fig.suptitle("A8 Q4: sign of the discriminant $B^2-4AC$   (orange: hyperbolic, blue: elliptic, grey line: parabolic)", fontsize=10)
    save(fig, "DE-PDE-classification-regions.png")


# ------------------------------------------------------------------------------ 3 d'Alembert space-time picture
def fig_dalembert():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3))
    ax = axs[0]
    x0, t0, c = 1.0, 1.5, 1.0
    ts = np.linspace(0, 2.2, 10)
    ax.fill([x0 - c * t0, x0 + c * t0, x0], [0, 0, t0], color=HYP, alpha=0.35, label="domain of dependence of $(x_0,t_0)$")
    for k in np.arange(-3, 5.1, 0.5):
        ax.plot(ts + k, ts, color="#bbbbbb", lw=0.6); ax.plot(k - ts, ts, color="#bbbbbb", lw=0.6)
    ax.plot([x0 - c * t0, x0], [0, t0], color="#d94a4a", lw=2); ax.plot([x0 + c * t0, x0], [0, t0], color="#d94a4a", lw=2)
    ax.plot([x0], [t0], "ko"); ax.text(x0 + 0.05, t0 + 0.08, "$(x_0,t_0)$")
    ax.plot([x0 - c * t0, x0 + c * t0], [0, 0], color="k", lw=3)
    ax.text(x0, -0.22, "$[x_0-ct_0,\\,x_0+ct_0]$ : data that matter", ha="center", fontsize=8)
    ax.set_xlim(-2, 4); ax.set_ylim(-0.4, 2.2); ax.set_xlabel("x"); ax.set_ylabel("t"); ax.legend(loc="upper left", fontsize=8)
    ax.set_title("Characteristics $x\\pm ct$ = const (grey) and the domain of dependence")
    ax = axs[1]
    for k in np.arange(0, 6.1, 0.5):
        ax.plot(ts + k, ts, color="#bbbbbb", lw=0.6)
    for k in np.arange(0, 3.1, 0.5):
        ax.plot(k - ts[ts <= k], ts[ts <= k], color="#bbbbbb", lw=0.6)
    tt = np.linspace(0, 3, 50)
    ax.plot(tt * c, tt, color="#d94a4a", lw=2.5, label="$x=ct$")
    ax.fill_betweenx(tt, tt * c, 6, color=HYP, alpha=0.25); ax.fill_betweenx(tt, 0, tt * c, color=ELL, alpha=0.25)
    ax.text(3.2, 0.5, "$x>ct$: both $f(x\\pm ct)$ use $x\\pm ct>0$\n(plain d'Alembert)", fontsize=8)
    ax.text(0.15, 2.6, "$x<ct$: $x-ct<0$,\nuse the odd (or even)\nextension", fontsize=8)
    ax.set_xlim(0, 6); ax.set_ylim(0, 3); ax.set_xlabel("x"); ax.set_ylabel("t")
    ax.set_title("Half line $x>0$: reflection at the boundary"); ax.legend(loc="lower right", fontsize=8)
    save(fig, "DE-PDE-dalembert.png")


# ------------------------------------------------------------------------------ 4 string: modes, plucked string
def fig_string():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3))
    x = np.linspace(0, 1, 400)
    ax = axs[0]
    for n, c in zip((1, 2, 3, 4), ("#3d7be8", "#e8a33d", "#2a9d4a", "#d94a4a")):
        ax.plot(x, np.sin(n * PI * x), color=c, lw=2, label=f"n = {n}:  $\\omega_n=n\\pi c/L$")
    ax.axhline(0, color="k", lw=0.8)
    ax.set_title("Fixed ends: eigenfunctions $\\sin(n\\pi x/L)$ (the standing-wave modes)")
    ax.set_xlabel("x / L"); ax.legend(fontsize=8)
    ax = axs[1]
    h, L, cc = 1.0, 1.0, 1.0
    def u(xx, t, N=400):
        out = 0
        for n in range(1, N):
            cn = 8 * h / (n**2 * PI**2) * np.sin(n * PI / 2)
            out = out + cn * np.sin(n * PI * xx / L) * np.cos(n * PI * cc * t / L)
        return out
    for t, col in zip((0, 0.1, 0.25, 0.4, 0.5), ("#222222", "#3d7be8", "#2a9d4a", "#e8a33d", "#d94a4a")):
        ax.plot(x, u(x, t), color=col, lw=1.8, label=f"ct/L = {t}")
    ax.set_title("A9 Q5: plucked string, midpoint raised to $h$ and released")
    ax.set_xlabel("x / L"); ax.legend(fontsize=8, ncol=2)
    save(fig, "DE-PDE-string.png")


# ------------------------------------------------------------------------------ 5 heat
def fig_heat():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3))
    x = np.linspace(0, 100, 500)
    ax = axs[0]
    c2 = 1.0
    def u10(xx, t, N=400):
        out = 0
        for n in range(1, N):
            out = out + 400 / (n**2 * PI**2) * np.sin(n * PI / 2) * np.sin(n * PI * xx / 100) * np.exp(-n**2 * PI**2 * c2 * t / 1e4)
        return out
    for t, col in zip((0, 100, 300, 1000, 3000), ("#222222", "#3d7be8", "#2a9d4a", "#e8a33d", "#d94a4a")):
        ax.plot(x, u10(x, t), color=col, lw=1.8, label=f"$c^2t$ = {t}")
    ax.set_title("A9 Q10: rod with ends at 0°, triangular start;\nhigher modes die first, the corner smooths out")
    ax.set_xlabel("x (cm)"); ax.legend(fontsize=8)
    ax = axs[1]
    xs = np.linspace(0, 10, 400)
    def u12(xx, t, N=400):
        out = -3 * xx + 90
        for n in range(1, N):
            cn = 80 / (n * PI) * ((-1)**(n + 1) - 1)
            out = out + cn * np.sin(n * PI * xx / 10) * np.exp(-n**2 * PI**2 * t / 100)
        return out
    for t, col in zip((0, 0.02, 0.1, 0.3, 1, 5), ("#222222", "#3d7be8", "#2a9d4a", "#e8a33d", "#d94a4a", "#8a4fff")):
        ax.plot(xs, u12(xs, t), color=col, lw=1.8, label=f"t = {t}")
    ax.plot(xs, -3 * xs + 90, "k--", lw=1, label="steady state $-3x+90$")
    ax.set_title("A9 Q12: $u=-3x+90+$ transient; start $5x+50$")
    ax.set_xlabel("x"); ax.legend(fontsize=8, ncol=2)
    save(fig, "DE-PDE-heat.png")


# ------------------------------------------------------------------------------ 6 Laplace
def fig_laplace():
    fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.1))
    # A10 Q2(b)
    xs = np.linspace(0, 1, 201)
    X, Y = np.meshgrid(xs, xs)
    U = np.zeros_like(X)
    for n in range(1, 60, 2):
        a = 8 / (n * PI)**3
        U += a / np.sinh(n * PI) * (np.sin(n * PI * X) * np.sinh(n * PI * (1 - Y)) + np.sin(n * PI * Y) * np.sinh(n * PI * (1 - X)))
    ax = axs[0]
    cs = ax.contourf(X, Y, U, 20, cmap="inferno"); fig.colorbar(cs, ax=ax, shrink=0.85)
    ax.set_title("A10 Q2(b): hot edges $x(1-x)$ on $y=0$\nand $y(1-y)$ on $x=0$", fontsize=9); ax.set_aspect("equal")
    # A10 Q6 strip
    ax = axs[1]
    xs = np.linspace(0, 10, 201); ys = np.linspace(0, 20, 201)
    X, Y = np.meshgrid(xs, ys)
    U = np.zeros_like(X)
    for n in range(1, 200):
        U += 800 / (n**2 * PI**2) * np.sin(n * PI / 2) * np.sin(n * PI * X / 10) * np.exp(-n * PI * Y / 10)
    cs = ax.contourf(X, Y, U, 20, cmap="inferno"); fig.colorbar(cs, ax=ax, shrink=0.85)
    ax.set_title("A10 Q6: semi-infinite strip, tent on $y=0$\n(mode $n$ dies as $e^{-n\\pi y/10}$)", fontsize=9)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    # A10 Q8(b) disk
    ax = axs[2]
    r = np.linspace(0, 1, 160); th = np.linspace(-PI, PI, 361)
    R, T = np.meshgrid(r, th)
    U = np.zeros_like(R)
    for n in range(1, 600):
        bn = 2 / (PI * n * n) * np.sin(n * PI / 2) - np.cos(n * PI / 2) / n
        U += bn * R**n * np.sin(n * T)
    cs = ax.contourf(R * np.cos(T), R * np.sin(T), U, 24, cmap="coolwarm"); fig.colorbar(cs, ax=ax, shrink=0.85)
    ax.add_patch(Circle((0, 0), 1, fill=False, color="k", lw=1)); ax.set_aspect("equal")
    ax.set_title("A10 Q8(b): unit disk, boundary value $\\theta$\non the right half, 0 on the left", fontsize=9)
    save(fig, "DE-PDE-laplace.png")


if __name__ == "__main__":
    for fn in (fig_characteristics, fig_regions, fig_dalembert, fig_string, fig_heat, fig_laplace):
        fn(); print("done", fn.__name__)
