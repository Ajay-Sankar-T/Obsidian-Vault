"""Figures for Modules 1 and 2: vectors, rotations, Newton's laws, frames, momentum, polar coordinates, pendulums."""
from ph_common import *
from matplotlib.patches import Arc, Polygon, Rectangle, Circle, FancyArrowPatch


def vec_dot_cross():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    u, v = np.array([3.0, 0.4]), np.array([1.6, 2.4])
    th = np.degrees(np.arctan2(v[1], v[0]) - np.arctan2(u[1], u[0]))
    blank(a, (-0.6, 4.2, -0.9, 3.0))
    arrow(a, 0, 0, *u, color=BLUE); arrow(a, 0, 0, *v, color=ORANGE)
    uh = u / np.linalg.norm(u); proj = (v @ uh) * uh
    a.plot([v[0], proj[0]], [v[1], proj[1]], ls="--", color=GREY, lw=1.3)
    a.plot([0, proj[0]], [0, proj[1]], color=GREEN, lw=5, alpha=.55, solid_capstyle="butt")
    a.add_patch(Arc((0, 0), 1.3, 1.3, theta1=np.degrees(np.arctan2(u[1], u[0])), theta2=np.degrees(np.arctan2(v[1], v[0])), color=INK))
    a.text(0.85, 0.55, r"$\theta$", fontsize=12)
    a.text(u[0] + .05, u[1] - .35, r"$\mathbf{u}$", color=BLUE, fontsize=13); a.text(v[0] - .35, v[1] + .1, r"$\mathbf{v}$", color=ORANGE, fontsize=13)
    a.text(proj[0] / 2 - .1, -.55, r"$v\cos\theta$", color=GREEN, fontsize=11)
    a.set_title(r"Dot product $\mathbf{u}\cdot\mathbf{v}=uv\cos\theta$" + "\n" + r"(shadow of $\mathbf{v}$ on $\mathbf{u}$, times $u$)", fontsize=9.5)
    blank(b, (-0.6, 5.2, -1.0, 3.4))
    P = [(0, 0), tuple(u), tuple(u + v), tuple(v)]
    b.add_patch(Polygon(P, closed=True, color=PURPLE, alpha=.18)); b.add_patch(Polygon(P, closed=True, fill=False, ec=PURPLE, lw=1.2))
    arrow(b, 0, 0, *u, color=BLUE); arrow(b, 0, 0, *v, color=ORANGE)
    b.text(1.9, 1.2, r"area $=|\mathbf{u}\times\mathbf{v}|$" + "\n" + r"$=uv\sin\theta$", ha="center", fontsize=10.5, color=PURPLE)
    b.text(2.3, -0.75, r"$\mathbf{u}\times\mathbf{v}$ points out of the page (right-hand rule)", ha="center", fontsize=9, color=INK)
    b.set_title("Cross product\n" + "(area of the parallelogram, normal to its plane)", fontsize=9.5)
    save(fig, "vec-dot-cross")


def vec_rotation():
    fig, ax = plt.subplots(figsize=(5.4, 4.6))
    blank(ax, (-2.1, 4.3, -1.0, 3.5))
    t = np.radians(30)
    ex, ey = np.array([1, 0]), np.array([0, 1]); e1, e2 = np.array([np.cos(t), np.sin(t)]), np.array([-np.sin(t), np.cos(t)])
    L = 3.6
    arrow(ax, 0, 0, L, 0, color=GREY, lw=1.6); arrow(ax, 0, 0, 0, L * .85, color=GREY, lw=1.6)
    arrow(ax, 0, 0, *(L * e1), color=BLUE, lw=1.6); arrow(ax, 0, 0, *(L * .85 * e2), color=BLUE, lw=1.6)
    ax.text(L + .05, -.3, r"$x$", color=GREY, fontsize=13); ax.text(-.3, L * .85, r"$y$", color=GREY, fontsize=13)
    ax.text(*(L * e1 + [.05, .02]), r"$x'$", color=BLUE, fontsize=13); ax.text(*(L * .85 * e2 + [-.35, .05]), r"$y'$", color=BLUE, fontsize=13)
    r = np.array([2.6, 1.9]); arrow(ax, 0, 0, *r, color=RED, lw=2.4)
    ax.text(r[0] + .06, r[1] + .06, r"$\mathbf{r}$", color=RED, fontsize=14)
    ax.plot([r[0], r[0]], [0, r[1]], ls=":", color=GREY); ax.plot([0, r[0]], [r[1], r[1]], ls=":", color=GREY)
    xp, yp = r @ e1, r @ e2
    ax.plot(*zip(r, xp * e1), ls=":", color=BLUE); ax.plot(*zip(r, yp * e2), ls=":", color=BLUE)
    ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=0, theta2=30, color=BLUE)); ax.text(.95, .2, r"$\phi$", color=BLUE, fontsize=12)
    ax.text(-1.9, -.85, "same arrow, two sets of numbers:\n" + r"$(x,y)=(%.2f,\,%.2f)$   $(x',y')=(%.2f,\,%.2f)$" % (r[0], r[1], xp, yp), fontsize=9.5)
    save(fig, "vec-rotation")


def newton_const_force():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9, 3.4))
    t = np.linspace(0, 4, 200); F, m = 2.0, 1.0
    for x0, v0, c in [(0, 0, BLUE), (1, 2, ORANGE), (3, -3, GREEN)]:
        a.plot(t, x0 + v0 * t + F / (2 * m) * t ** 2, color=c, lw=2.2, label=r"$x_0=%g,\ v_0=%g$" % (x0, v0))
    a.set_xlabel("t"); a.set_ylabel("x(t)"); a.legend(fontsize=8.5); a.set_title(r"$\ddot x=F_0/m$: three initial conditions, three futures")
    tt = np.linspace(-4, 4, 300); x0, v0 = 1.0, 2.0
    xf = x0 + v0 * tt + F / (2 * m) * tt ** 2
    b.plot(tt[tt >= 0], xf[tt >= 0], color=BLUE, lw=2.4, label="forward in time")
    b.plot(tt[tt <= 0], xf[tt <= 0], color=RED, lw=2.4, ls="--", label="run backwards (retrodiction)")
    b.plot([0], [x0], "o", color=INK); b.annotate("now: $x_0,\\ p_0$", (0, x0), (0.6, 12), arrowprops=dict(arrowstyle="->", color=INK), fontsize=9)
    b.set_xlabel("t"); b.set_ylabel("x(t)"); b.legend(fontsize=8.5, loc="upper center"); b.set_title("Determinism: state now fixes past and future")
    save(fig, "newton-determinism")


def momentum_collision():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9, 3.4))
    m1, m2 = 2.0, 1.0; x1, x2, v1, v2 = 0.0, 6.0, 2.0, -1.0
    t = np.linspace(0, 6, 400); tc = (x2 - x1) / (v1 - v2)
    u1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2); u2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    p1 = np.where(t < tc, x1 + v1 * t, x1 + v1 * tc + u1 * (t - tc)); p2 = np.where(t < tc, x2 + v2 * t, x2 + v2 * tc + u2 * (t - tc))
    cm = (m1 * p1 + m2 * p2) / (m1 + m2)
    a.plot(t, p1, color=BLUE, lw=2.4, label=r"mass $m_1=2$"); a.plot(t, p2, color=ORANGE, lw=2.4, label=r"mass $m_2=1$"); a.plot(t, cm, color=INK, lw=1.6, ls="--", label="centre of mass")
    a.axvline(tc, color=GREY, ls=":"); a.text(tc + .1, -1.2, "elastic collision", fontsize=8.5)
    a.set_xlabel("t"); a.set_ylabel("x"); a.legend(fontsize=8.5); a.set_title("Internal forces bend the paths, not the CM line")
    P1 = np.where(t < tc, m1 * v1, m1 * u1); P2 = np.where(t < tc, m2 * v2, m2 * u2)
    b.plot(t, P1, color=BLUE, lw=2.4, label=r"$p_1$"); b.plot(t, P2, color=ORANGE, lw=2.4, label=r"$p_2$"); b.plot(t, P1 + P2, color=INK, lw=2.4, ls="--", label=r"$p_1+p_2$")
    b.set_xlabel("t"); b.set_ylabel("momentum"); b.legend(fontsize=8.5); b.set_title("Third law: what one gains the other loses")
    save(fig, "momentum-collision")


def frames_cart():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.0))
    for ax, title in ((a, "Ground (inertial) frame"), (b, "Cart (non-inertial) frame")):
        blank(ax, (-0.3, 8.4, -0.7, 3.6)); ax.set_title(title, fontsize=10.5)
        ax.add_patch(Rectangle((1, 0.35), 4.2, .4, fc="#cbd5e0", ec=INK)); ax.add_patch(Circle((1.8, .2), .3, fc=INK)); ax.add_patch(Circle((4.4, .2), .3, fc=INK))
        ax.plot([-.3, 8.2], [-.12, -.12], color=GREY, lw=2)
        ax.add_patch(Circle((3.0, 1.15), .38, fc=ORANGE, ec=INK, zorder=5))
    arrow(a, 5.4, .55, 7.6, .55, color=BLUE); a.text(5.5, .78, r"cart acceleration $A$", color=BLUE, fontsize=9.5)
    arrow(a, 3.0, 1.55, 3.0, 2.0, color=GREY)
    a.text(0, 3.3, "no unexplained forces:", fontsize=9.5, color=GREEN); a.text(0, 2.85, r"$m\mathbf{a}=\mathbf{F}$", fontsize=11, color=GREEN)
    a.text(3.3, 1.85, "the string drags the ball\nforward with the cart", fontsize=8.8)
    arrow(b, 2.6, 1.15, 1.0, 1.15, color=RED); b.text(.2, 1.55, r"pseudo-force $-m\mathbf{A}$", color=RED, fontsize=9.5)
    b.text(0, 3.3, "an inertial force must be added:", fontsize=9.5, color=RED); b.text(0, 2.85, r"$m\mathbf{a}=\mathbf{F}-m\mathbf{A}$", fontsize=11, color=RED)
    b.text(3.3, 1.85, "the ball hangs still: string\ntension balances the pseudo-force", fontsize=8.8)
    save(fig, "frames-cart")


def polar_basis():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    blank(ax, (-.4, 5.0, -.4, 3.9))
    arrow(ax, 0, 0, 4.6, 0, color=GREY, lw=1.4); arrow(ax, 0, 0, 0, 3.7, color=GREY, lw=1.4)
    ax.text(4.65, -.25, "x", color=GREY, fontsize=12); ax.text(-.25, 3.6, "y", color=GREY, fontsize=12)
    ph = np.radians(40); r = 3.0; P = r * np.array([np.cos(ph), np.sin(ph)])
    ax.plot(*zip((0, 0), P), color=INK, lw=2.4); ax.plot(*P, "o", color=INK, ms=8)
    er, et = np.array([np.cos(ph), np.sin(ph)]), np.array([-np.sin(ph), np.cos(ph)])
    arrow(ax, *P, *(P + 1.1 * er), color=BLUE); arrow(ax, *P, *(P + 1.1 * et), color=ORANGE)
    ax.text(*(P + 1.22 * er + [.0, -.05]), r"$\hat{r}$", color=BLUE, fontsize=14); ax.text(*(P + 1.2 * et + [-.45, .05]), r"$\hat{\phi}$", color=ORANGE, fontsize=14)
    ax.add_patch(Arc((0, 0), 1.4, 1.4, theta1=0, theta2=40, color=INK)); ax.text(.85, .25, r"$\phi$", fontsize=13)
    ax.text(.75, 1.55, r"$r$", fontsize=13)
    arc = np.radians(np.linspace(40, 62, 30)); ax.plot(r * np.cos(arc), r * np.sin(arc), color=RED, lw=1.5, ls="--")
    ax.text(2.4, 1.15, "as the particle moves along the red arc,\nboth unit vectors turn with it:\n" + r"$d\hat{r}/dt=\dot\phi\,\hat{\phi}$,   $d\hat{\phi}/dt=-\dot\phi\,\hat{r}$", fontsize=8.8, va="top")
    save(fig, "polar-basis")


def pendulum_forces():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1.05, 1]})
    blank(a, (-1.3, 2.3, -3.1, .4))
    th = np.radians(32); L = 1.7; P = L * np.array([np.sin(th), -np.cos(th)])
    a.plot([-.8, .8], [0, 0], color=INK, lw=3); a.plot([0, 0], [0, -L], color=GREY, ls=":"); a.plot(*zip((0, 0), P), color=INK, lw=2)
    a.add_patch(Circle(P, .12, fc=ORANGE, ec=INK, zorder=5)); a.add_patch(Arc((0, 0), 1.0, 1.0, theta1=-90, theta2=-90 + 32, color=INK)); a.text(.12, -.78, r"$\theta$", fontsize=12)
    eth = np.array([np.cos(th), np.sin(th)]); er = np.array([np.sin(th), -np.cos(th)])
    arrow(a, *P, P[0], P[1] - .85, color=RED); a.text(P[0] + .08, P[1] - .85, r"$mg$", color=RED, fontsize=12)
    arrow(a, *P, *(P - .8 * er), color=BLUE); a.text(P[0] - .95, P[1] + .3, r"$T$", color=BLUE, fontsize=12)
    arrow(a, *P, *(P - 0.75 * eth * np.sin(th) / np.sin(th) * np.sin(th) * 1.0), color=GREEN, lw=2.6)
    a.text(P[0] - 1.2, P[1] - .42, r"$mg\sin\theta$ (restoring)", color=GREEN, fontsize=9)
    a.text(-1.25, -2.65, r"tangential: $mL\ddot\theta=-mg\sin\theta$", fontsize=9); a.text(-1.25, -2.95, r"radial: $T-mg\cos\theta=mL\dot\theta^{2}$", fontsize=9)
    x = np.linspace(0, np.pi, 300); b.plot(x, np.sin(x), color=BLUE, lw=2.4, label=r"$\sin\theta$ (exact restoring force)"); b.plot(x, x, color=ORANGE, lw=2, ls="--", label=r"$\theta$ (small-angle)")
    b.axvspan(0, .24, color=GREEN, alpha=.2); b.text(.3, 2.2, "within 1% for\n" + r"$\theta<14^\circ$", fontsize=8.5, color=GREEN)
    b.set_xlim(0, 2.2); b.set_ylim(0, 2.6); b.set_xlabel(r"$\theta$ (rad)"); b.legend(fontsize=8.5, loc="lower right"); b.set_title("Why the pendulum is only approximately SHM")
    save(fig, "pendulum-forces")


def conical_pendulum():
    fig, ax = plt.subplots(figsize=(5.0, 4.6))
    blank(ax, (-2.5, 2.7, -4.0, .8))
    al = np.radians(35); L = 3.0; R = L * np.sin(al); H = L * np.cos(al)
    ax.plot([-.7, .7], [0, 0], color=INK, lw=3); ax.plot([0, 0], [0, -H], color=GREY, ls=":")
    ax.plot(*zip((0, 0), (R, -H)), color=INK, lw=2); ax.add_patch(Circle((R, -H), .14, fc=ORANGE, ec=INK, zorder=5))
    th = np.linspace(0, 2 * np.pi, 100); ax.plot(R * np.cos(th), -H + .25 * np.sin(th), color=BLUE, ls="--", lw=1.4)
    ax.plot([0, R], [-H, -H], color=GREY, ls=":"); ax.text(R / 2 - .5, -H - .5, r"$R=L\sin\alpha$", fontsize=10)
    ax.add_patch(Arc((0, 0), 1.5, 1.5, theta1=-90, theta2=-90 + 35, color=INK)); ax.text(.1, -.95, r"$\alpha$", fontsize=12)
    ax.text(R * .55 + .12, -H * .5, r"$L$", fontsize=12)
    arrow(ax, R, -H, R, -H - .95, color=RED); ax.text(R + .1, -H - .95, r"$mg$", color=RED, fontsize=11)
    arrow(ax, R, -H, R - .55 * np.sin(al), -H + .55 * np.cos(al), color=BLUE, lw=2.2); ax.text(R - 1.0, -H + .72, r"$T$", color=BLUE, fontsize=11)
    arrow(ax, R, -H, 0.35, -H, color=GREEN, lw=1.8); ax.text(-2.4, -H - .62, r"net force (green) points to the centre", color=GREEN, fontsize=9)
    ax.text(-2.4, .5, r"$\omega=\sqrt{g/(L\cos\alpha)}$", fontsize=11)
    save(fig, "conical-pendulum")


if __name__ == "__main__":
    vec_dot_cross(); vec_rotation(); newton_const_force(); frames_cart(); momentum_collision(); polar_basis(); pendulum_forces(); conical_pendulum()
