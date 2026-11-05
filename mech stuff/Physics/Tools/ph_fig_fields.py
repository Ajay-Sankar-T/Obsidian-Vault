"""Figures for Modules 5 and 8: gradient, curl, line integrals, curvilinear coordinates, flux, divergence, Stokes, continuity and Bernoulli."""
from ph_common import *
from matplotlib.patches import Polygon, Circle, Rectangle, FancyArrowPatch, Arc
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def grad_contours():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.0), gridspec_kw={"width_ratios": [1.25, 1]})
    x = np.linspace(-2.2, 2.2, 300); X, Y = np.meshgrid(x, x); f = lambda X, Y: X * np.exp(-X ** 2 - Y ** 2)
    cs = a.contourf(X, Y, f(X, Y), levels=18, cmap="RdBu_r", alpha=.75); a.contour(X, Y, f(X, Y), levels=18, colors="k", linewidths=.4)
    xs = np.linspace(-1.9, 1.9, 13); XS, YS = np.meshgrid(xs, xs)
    gx = (1 - 2 * XS ** 2) * np.exp(-XS ** 2 - YS ** 2); gy = -2 * XS * YS * np.exp(-XS ** 2 - YS ** 2)
    m = np.hypot(gx, gy) > .02; a.quiver(XS[m], YS[m], gx[m], gy[m], color=INK, scale=7, width=.005)
    a.set_aspect("equal"); a.set_title(r"$f=xe^{-x^2-y^2}$: $\nabla f$ crosses contours at right angles"); a.set_xlabel("x"); a.set_ylabel("y"); a.grid(False)
    al = np.linspace(-180, 180, 400); b.plot(al, np.cos(np.radians(al)), color=BLUE, lw=2.6)
    b.axhline(0, color=GREY, lw=1); b.set_xticks([-180, -90, 0, 90, 180]); b.set_xlabel(r"angle $\alpha$ between direction $\hat{u}$ and $\nabla f$ (degrees)"); b.set_ylabel(r"$D_{\hat u}f\,/\,|\nabla f|$")
    b.annotate("steepest climb\n(along the gradient)", (0, 1), (-150, .55), fontsize=9, arrowprops=dict(arrowstyle="->", color=INK)); b.annotate("no change:\nalong a contour", (90, 0), (95, -.7), fontsize=9, arrowprops=dict(arrowstyle="->", color=INK))
    b.set_title(r"Slope in direction $\hat u$: $D_{\hat u}f=\nabla f\cdot\hat u$")
    save(fig, "grad-contours")


def curl_fields():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2))
    x = np.linspace(-1.6, 1.6, 40); X, Y = np.meshgrid(x, x)
    loop = np.array([[-.6, -.6], [.6, -.6], [.6, .6], [-.6, .6], [-.6, -.6]])

    def circ(F):
        s = 0
        for p, q in zip(loop[:-1], loop[1:]):
            tt = np.linspace(0, 1, 2001); P = p[None] + tt[:, None] * (q - p)[None]; Fx, Fy = F(P[:, 0], P[:, 1])
            s += np.trapezoid(Fx * (q - p)[0] + Fy * (q - p)[1], tt)
        return s
    F1 = lambda x, y: (y, x); F2 = lambda x, y: (-y, x)
    for ax, F, ttl in ((a, F1, r"$\mathbf{F}=(y,\,x)$: conservative, curl $=0$"), (b, F2, r"$\mathbf{F}=(-y,\,x)$: not conservative, curl $=2\hat{z}$")):
        U, V = F(X, Y); ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap="Blues", density=1.3, linewidth=1.4, arrowsize=1.2)
        ax.plot(loop[:, 0], loop[:, 1], color=RED, lw=2.6); ax.set_aspect("equal"); ax.set_title(ttl, fontsize=10); ax.grid(False); ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
        ax.text(0, 0, r"$\oint\mathbf{F}\cdot d\mathbf{r}=%.2f$" % circ(F), ha="center", va="center", fontsize=10.5, color=RED, bbox=dict(fc="white", ec=RED, boxstyle="round,pad=.3"))
    a.contour(X, Y, X * Y, levels=10, colors=GREY, linewidths=.8, linestyles="--")
    save(fig, "curl-fields")
    print("circulation F1, F2 around the 1.2x1.2 square:", round(circ(F1), 4), round(circ(F2), 4), "(expected 0 and 2*1.44 =", 2 * 1.44, ")")


def work_paths():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.1))
    x = np.linspace(-.1, 1.2, 14); X, Y = np.meshgrid(x, x)
    Fc = lambda x, y: (y ** 2, 2 * x * y); Fn = lambda x, y: (-y, x)

    def W(F, path):
        s = 0
        for p, q in zip(path[:-1], path[1:]):
            p, q = np.array(p, float), np.array(q, float); tt = np.linspace(0, 1, 4001); P = p + tt[:, None] * (q - p); Fx, Fy = F(P[:, 0], P[:, 1]); s += np.trapezoid(Fx * (q - p)[0] + Fy * (q - p)[1], tt)
        return s
    A = [(0, 0), (1, 1)]; B = [(0, 0), (1, 0), (1, 1)]
    for ax, F, ttl in ((a, Fc, r"$\mathbf{F}=(y^2,\,2xy)=\nabla(xy^2)$"), (b, Fn, r"$\mathbf{F}=(-y,\,x)$")):
        U, V = F(X, Y); ax.quiver(X, Y, U, V, color=GREY, alpha=.85, width=.005, scale=14)
        ax.plot(*zip(*A), color=BLUE, lw=3, label="path A (diagonal): W = %.2f" % W(F, A)); ax.plot(*zip(*B), color=ORANGE, lw=3, label="path B (along x, then up): W = %.2f" % W(F, B))
        ax.plot([0, 1], [0, 1], "o", color=INK); ax.set_aspect("equal"); ax.set_title(ttl, fontsize=10.5); ax.legend(fontsize=8.5, loc="upper left"); ax.set_ylim(-.15, 1.45); ax.set_xlim(-.15, 1.3)
    save(fig, "work-paths")
    print("work, conservative A,B:", round(W(Fc, A), 4), round(W(Fc, B), 4), " non-conservative A,B:", round(W(Fn, A), 4), round(W(Fn, B), 4))


def sph_axes(ax, L=1.3):
    for v, lab in (((L, 0, 0), "x"), ((0, L, 0), "y"), ((0, 0, L), "z")):
        ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color=GREY, lw=1.4); ax.text(v[0] * 1.08, v[1] * 1.08, v[2] * 1.08, lab, color=GREY, fontsize=12)
    ax.set_axis_off(); ax.set_box_aspect((1, 1, 1)); ax.set_xlim(-.2, 1.1); ax.set_ylim(-.2, 1.1); ax.set_zlim(0, 1.2)


def coords_spherical():
    fig = plt.figure(figsize=(5.8, 5.4)); ax = fig.add_subplot(111, projection="3d"); sph_axes(ax)
    th, ph, r = np.radians(55), np.radians(40), 1.0
    P = r * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    ax.plot(*zip((0, 0, 0), P), color=INK, lw=2.6); ax.plot(*zip((P[0], P[1], 0), P), color=GREY, ls=":"); ax.plot(*zip((0, 0, 0), (P[0], P[1], 0)), color=GREY, ls=":")
    ax.plot(*P.reshape(3, 1), "o", color=INK, ms=7)
    t = np.linspace(0, th, 40); ax.plot(.35 * np.sin(t) * np.cos(ph), .35 * np.sin(t) * np.sin(ph), .35 * np.cos(t), color=BLUE, lw=2); ax.text(.1, .05, .5, r"$\theta$", color=BLUE, fontsize=13)
    t = np.linspace(0, ph, 40); ax.plot(.4 * np.cos(t), .4 * np.sin(t), 0 * t, color=ORANGE, lw=2); ax.text(.42, .08, 0, r"$\phi$", color=ORANGE, fontsize=13)
    er = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]); et = np.array([np.cos(th) * np.cos(ph), np.cos(th) * np.sin(ph), -np.sin(th)]); ep = np.array([-np.sin(ph), np.cos(ph), 0])
    for v, c, lab in ((er, BLUE, r"$\hat{r}$"), (et, GREEN, r"$\hat{\theta}$"), (ep, ORANGE, r"$\hat{\phi}$")):
        ax.quiver(*P, *v, length=.38, color=c, lw=2.2, arrow_length_ratio=.25); Q = P + .46 * v; ax.text(*Q, lab, color=c, fontsize=13)
    ax.text(.42, .22, .3, r"$r$", fontsize=13)
    ax.set_title(r"Spherical: $x=r\sin\theta\cos\phi,\ y=r\sin\theta\sin\phi,\ z=r\cos\theta$", fontsize=9)
    save(fig, "coords-spherical")


def coords_cylindrical():
    fig = plt.figure(figsize=(5.8, 5.4)); ax = fig.add_subplot(111, projection="3d"); sph_axes(ax)
    ph, rho, z = np.radians(40), .9, .7
    P = np.array([rho * np.cos(ph), rho * np.sin(ph), z]); F = np.array([P[0], P[1], 0])
    ax.plot(*zip((0, 0, 0), F), color=INK, lw=2.6); ax.plot(*zip(F, P), color=INK, lw=2.6); ax.plot(*zip((0, 0, 0), P), color=GREY, ls=":"); ax.plot(*P.reshape(3, 1), "o", color=INK, ms=7)
    t = np.linspace(0, ph, 40); ax.plot(.4 * np.cos(t), .4 * np.sin(t), 0 * t, color=ORANGE, lw=2); ax.text(.42, .08, 0, r"$\phi$", color=ORANGE, fontsize=13)
    ax.text(.25, .1, 0.03, r"$\rho$", fontsize=13); ax.text(F[0] + .06, F[1], z / 2, r"$z$", fontsize=13)
    er = np.array([np.cos(ph), np.sin(ph), 0]); ep = np.array([-np.sin(ph), np.cos(ph), 0]); ez = np.array([0, 0, 1])
    for v, c, lab in ((er, BLUE, r"$\hat{\rho}$"), (ep, ORANGE, r"$\hat{\phi}$"), (ez, GREEN, r"$\hat{z}$")):
        ax.quiver(*P, *v, length=.36, color=c, lw=2.2, arrow_length_ratio=.25); ax.text(*(P + .44 * v), lab, color=c, fontsize=13)
    ax.set_title(r"Cylindrical: $x=\rho\cos\phi,\ y=\rho\sin\phi,\ z=z$", fontsize=9.5)
    save(fig, "coords-cylindrical")


def flux_patches():
    fig, ax = plt.subplots(figsize=(9.2, 3.5)); blank(ax, (-.3, 9.6, -1.6, 2.3))
    for cx, ang, lab, c in ((1.4, 90, r"face-on: $\Phi=FA$", BLUE), (4.7, 55, r"tilted: $\Phi=FA\cos\theta$", GREEN), (8.0, 0, r"edge-on: $\Phi=0$", RED)):
        for yy in np.linspace(-1.1, 1.5, 6):
            arrow(ax, cx - 1.3, yy, cx + 1.3 if False else cx - .5, yy, color="#a0aec0", lw=1.2, ms=9)
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))]); p0, p1 = np.array([cx, .2]) - d * .9, np.array([cx, .2]) + d * .9
        ax.plot(*zip(p0, p1), color=c, lw=5, solid_capstyle="round"); n = np.array([np.sin(np.radians(ang)), -np.cos(np.radians(ang))]); n = n if n[0] >= 0 else -n
        arrow(ax, cx, .2, cx + n[0] * .9, .2 + n[1] * .9, color=INK, lw=2); ax.text(cx + n[0] * .9 + .05, .2 + n[1] * .9 + .1, r"$\hat{n}$", fontsize=12)
        ax.text(cx, -1.45, lab, ha="center", fontsize=10.5, color=c)
    ax.text(-.1, 2.0, r"uniform field $\mathbf{F}$ (grey arrows); the surface only 'catches' the component along its normal: $d\Phi=\mathbf{F}\cdot\hat{n}\,dA$", fontsize=9.5)
    save(fig, "flux-patches")


def div_fields():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.9))
    x = np.linspace(-2, 2, 40); X, Y = np.meshgrid(x, x); R2 = X ** 2 + Y ** 2 + 1e-9
    cases = [((X, Y), r"source: $\mathbf{F}=(x,y)$" + "\n" + r"$\nabla\!\cdot\!\mathbf{F}=+2$"), ((-X, -Y), r"sink: $\mathbf{F}=(-x,-y)$" + "\n" + r"$\nabla\!\cdot\!\mathbf{F}=-2$"),
             ((X / R2, Y / R2), r"line source: $\mathbf{F}=\mathbf{r}/r^2$" + "\n" + r"$\nabla\!\cdot\!\mathbf{F}=0$ away from 0")]
    for ax, ((U, V), ttl) in zip(axs, cases):
        mg = np.hypot(U, V); ax.streamplot(X, Y, U, V, color=PURPLE, density=1.15, linewidth=np.clip(2.6 * mg / np.percentile(mg, 90), .3, 3.2), arrowsize=1.2); ax.set_aspect("equal"); ax.set_title(ttl, fontsize=9.5); ax.grid(False)
        ax.add_patch(Circle((0, 0), 1.0, fill=False, ec=RED, lw=2))
    axs[0].text(0, 0, "net out", color=RED, ha="center", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1)); axs[1].text(0, 0, "net in", color=RED, ha="center", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1))
    fig.text(.5, .01, "line thickness = field strength: it grows with r for a source, but falls as 1/r for the line source, so the flux through every circle stays equal", ha="center", fontsize=8.5, color=GREY)
    save(fig, "div-fields")


def curl_paddle():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.9))
    x = np.linspace(-2, 2, 40); X, Y = np.meshgrid(x, x); R2 = X ** 2 + Y ** 2 + 1e-9
    cases = [((-Y, X), r"rigid rotation $(-y,x)$" + "\n" + r"curl $=+2$: paddle spins", +1), ((Y, 0 * X), r"shear $(y,0)$" + "\n" + r"curl $=-1$: paddle spins (clockwise)", -1), ((-Y / R2, X / R2), r"irrotational vortex $(-y,x)/r^2$" + "\n" + r"curl $=0$ away from 0: paddle just circles", 0)]
    for ax, ((U, V), ttl, s) in zip(axs, cases):
        ax.streamplot(X, Y, U, V, color=ORANGE, density=1.15, linewidth=1.3, arrowsize=1.2); ax.set_aspect("equal"); ax.grid(False); ax.set_title(ttl, fontsize=9)
        c = (1.1, .2) if s == 0 else (0, 0)
        if s == 0:
            ax.plot(*c, "o", color=INK, ms=4)
        for k in range(4):
            ang = k * np.pi / 2 + (np.pi / 4 if s == 0 else 0.3); ax.plot([c[0], c[0] + .35 * np.cos(ang)], [c[1], c[1] + .35 * np.sin(ang)], color=INK, lw=3)
        ax.add_patch(Circle(c, .09, fc="white", ec=INK, zorder=5))
        if s:
            th = np.linspace(0, 1.6 * np.pi, 50) * (1 if s > 0 else -1) + (0.4 if s > 0 else 1.2); ax.plot(.62 * np.cos(th), .62 * np.sin(th), color=RED, lw=2); ax.annotate("", xy=(.62 * np.cos(th[-1]), .62 * np.sin(th[-1])), xytext=(.62 * np.cos(th[-3]), .62 * np.sin(th[-3])), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    save(fig, "curl-paddle")


def stokes_surfaces():
    fig = plt.figure(figsize=(7.2, 5.0)); ax = fig.add_subplot(111, projection="3d")
    u = np.linspace(0, 2 * np.pi, 80); v = np.linspace(0, np.pi / 2, 30); U, V = np.meshgrid(u, v)
    ax.plot_surface(np.sin(V) * np.cos(U), np.sin(V) * np.sin(U), np.cos(V), color=BLUE, alpha=.22, linewidth=0)
    r = np.linspace(0, 1, 12); Rg, Ug = np.meshgrid(r, u); ax.plot_surface(Rg * np.cos(Ug), Rg * np.sin(Ug), 0 * Rg, color=ORANGE, alpha=.28, linewidth=0)
    ax.plot(np.cos(u), np.sin(u), 0 * u, color=RED, lw=3.2)
    for k in (0.5, 2.2, 3.9, 5.6):
        ax.quiver(np.cos(k), np.sin(k), 0, -np.sin(k) * .0, 0, 0)
    a0 = 5.2; ax.quiver(np.cos(a0), np.sin(a0), 0, -np.sin(a0) * .35, np.cos(a0) * .35, 0, color=RED, lw=3, arrow_length_ratio=.5)
    for (xx, yy) in ((0.3, 0.2), (-.4, .3), (.1, -.5)):
        zc = np.sqrt(max(1 - xx ** 2 - yy ** 2, 0)); ax.quiver(xx, yy, zc, 0, 0, .3, color=GREEN, lw=2, arrow_length_ratio=.3); ax.quiver(xx, yy, 0, 0, 0, .3, color=GREEN, lw=2, arrow_length_ratio=.3)
    ax.text(0, 0, 1.35, r"$\nabla\times\mathbf{F}$ (green) pierces both surfaces", ha="center", color=GREEN, fontsize=9)
    ax.text(1.2, -.4, 0, r"boundary $C$", color=RED, fontsize=10); ax.text(.45, .6, .75, r"$S_1$ (cap)", color=BLUE, fontsize=10); ax.text(-.9, -.1, 0, r"$S_2$ (disc)", color=ORANGE, fontsize=10)
    ax.set_axis_off(); ax.set_box_aspect((1, 1, .8)); ax.view_init(elev=24, azim=-60)
    ax.set_title("Stokes: the same circulation for ANY surface bounded by C", fontsize=10, pad=14)
    save(fig, "stokes-surfaces")


def venturi():
    fig, (a, b) = plt.subplots(2, 1, figsize=(8.4, 5.6), sharex=True, gridspec_kw={"height_ratios": [1.15, 1]})
    x = np.linspace(0, 10, 400); A = 1 - .6 * np.exp(-((x - 5) / 1.4) ** 2); R = np.sqrt(A) * .8
    a.fill_between(x, R, 1.1, color="#cbd5e0"); a.fill_between(x, -R, -1.1, color="#cbd5e0"); a.plot(x, R, color=INK, lw=2); a.plot(x, -R, color=INK, lw=2)
    for f in np.linspace(-.9, .9, 9):
        a.plot(x, f * R / .8 * .95 / 1.0 * 1.0, color=BLUE, lw=1.1)
    a.set_ylim(-1.1, 1.1); a.set_ylabel("pipe"); a.set_yticks([]); a.grid(False); a.set_title("Venturi: streamlines crowd together in the throat, so the flow speeds up")
    arrow(a, .3, 0, 1.6, 0, color=RED, lw=2.4); arrow(a, 4.4, 0, 6.2, 0, color=RED, lw=3.2)
    a.text(.3, .25, r"slow  $v_1$", color=RED, fontsize=9.5); a.text(4.3, .28, r"fast  $v_2=v_1A_1/A_2$", color=RED, fontsize=9.5)
    v = 2.0 / A; p = 1e5 + .5 * 1000 * (2.0 ** 2 - v ** 2)
    b.plot(x, v, color=ORANGE, lw=2.6, label="speed v (m/s)"); b.set_ylabel("speed (m/s)", color=ORANGE); b2 = b.twinx(); b2.plot(x, (p - 1e5) / 1000, color=BLUE, lw=2.6, label="gauge change in p (kPa)"); b2.set_ylabel("pressure change (kPa)", color=BLUE); b2.grid(False)
    b.set_xlabel("position along the pipe"); b.set_title(r"Bernoulli: $p+\frac{1}{2}\rho v^2$ constant, so $p$ dips where $v$ peaks (water, $v_1=2$ m/s)")
    b2.spines["right"].set_visible(True)
    save(fig, "venturi")
    print("venturi: throat area ratio %.2f, v2 = %.2f m/s, dp = %.1f kPa" % (A.min(), v.max(), (p.min() - 1e5) / 1000))


if __name__ == "__main__":
    grad_contours(); curl_fields(); work_paths(); coords_spherical(); coords_cylindrical(); flux_patches(); div_fields(); curl_paddle(); stokes_surfaces(); venturi()
