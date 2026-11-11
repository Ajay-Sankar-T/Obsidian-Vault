"""Figures for Modules 6 and 7: generalized coordinates, cyclic coordinates, effective potential, conics, Kepler, two-body, Hohmann."""
from ph_common import *
from matplotlib.patches import Circle, Arc, Polygon, Ellipse


def generalized_coords():
    fig, axs = plt.subplots(1, 3, figsize=(11, 3.9))
    a, b, c = axs
    blank(a, (-1.5, 1.7, -1.7, 1.7)); a.set_title("Bead on a ring:\n1 degree of freedom, $q=\\theta$", fontsize=10)
    th = np.linspace(0, 2 * np.pi, 200); a.plot(np.cos(th), np.sin(th), color=GREY, lw=3); p = np.radians(50)
    a.plot(np.cos(p), np.sin(p), "o", color=ORANGE, ms=14, mec=INK); a.plot([0, np.cos(p)], [0, np.sin(p)], color=INK, lw=1.4, ls=":"); a.add_patch(Arc((0, 0), .9, .9, theta1=0, theta2=50, color=BLUE, lw=2)); a.text(.5, .12, r"$\theta$", color=BLUE, fontsize=12)
    a.text(0, -1.55, "$x=R\\cos\\theta,\\ y=R\\sin\\theta$\n2 numbers, 1 constraint $x^2+y^2=R^2$", ha="center", fontsize=8.5)
    blank(b, (-1.5, 1.7, -2.3, .5)); b.set_title("Pendulum:\n1 degree of freedom, $q=\\theta$", fontsize=10)
    t = np.radians(35); P = 1.7 * np.array([np.sin(t), -np.cos(t)]); b.plot([-.6, .6], [0, 0], color=INK, lw=3); b.plot([0, 0], [0, -1.7], color=GREY, ls=":"); b.plot(*zip((0, 0), P), color=INK, lw=2)
    b.plot(*P, "o", color=ORANGE, ms=14, mec=INK); b.add_patch(Arc((0, 0), 1.0, 1.0, theta1=-90, theta2=-55, color=BLUE, lw=2)); b.text(.1, -.75, r"$\theta$", color=BLUE, fontsize=12)
    b.text(0, -2.25, "tension never appears:\nit does no work along the path", ha="center", fontsize=8.5)
    blank(c, (-1.8, 2.2, -3.3, .5)); c.set_title("Double pendulum:\n2 degrees of freedom, $q_1=\\theta_1,\\ q_2=\\theta_2$", fontsize=10)
    t1, t2 = np.radians(30), np.radians(-20); P1 = 1.4 * np.array([np.sin(t1), -np.cos(t1)]); P2 = P1 + 1.4 * np.array([np.sin(t2), -np.cos(t2)])
    c.plot([-.6, .6], [0, 0], color=INK, lw=3); c.plot([0, 0], [0, -1.4], color=GREY, ls=":"); c.plot([P1[0]] * 2, [P1[1], P1[1] - 1.4], color=GREY, ls=":")
    c.plot(*zip((0, 0), P1, P2), color=INK, lw=2); c.plot(*P1, "o", color=ORANGE, ms=13, mec=INK); c.plot(*P2, "o", color=GREEN, ms=13, mec=INK)
    c.add_patch(Arc((0, 0), .9, .9, theta1=-90, theta2=-60, color=BLUE, lw=2)); c.text(.1, -.68, r"$\theta_1$", color=BLUE, fontsize=11)
    c.add_patch(Arc(P1, .9, .9, theta1=-90 - 20, theta2=-90, color=PURPLE, lw=2)); c.text(P1[0] - .45, P1[1] - .78, r"$\theta_2$", color=PURPLE, fontsize=11)
    c.text(0, -3.25, "4 Cartesian numbers, 2 constraints", ha="center", fontsize=8.5)
    save(fig, "generalized-coords")


def cyclic_projectile():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
    g, vx, vy = 9.8, 6.0, 12.0; T = 2 * vy / g; t = np.linspace(0, T, 300); x = vx * t; y = vy * t - g * t ** 2 / 2
    a.plot(x, y, color=BLUE, lw=2.6)
    for tk in np.linspace(0, T, 7):
        xk, yk = vx * tk, vy * tk - g * tk ** 2 / 2; vyk = vy - g * tk
        arrow(a, xk, yk, xk + .09 * vx * 5, yk, color=GREEN, lw=1.8, ms=9); arrow(a, xk, yk, xk, yk + .09 * vyk * 5, color=RED, lw=1.8, ms=9) if abs(vyk) > .3 else None
        a.plot(xk, yk, "o", color=INK, ms=4)
    a.set_xlabel("x (m)"); a.set_ylabel("y (m)"); a.set_ylim(-1, 10.5); a.set_xlim(-1, 16); a.set_title(r"Green $p_x$ never changes; red $p_y$ does"); a.set_aspect("equal")
    b.plot(t, m := np.full_like(t, vx), color=GREEN, lw=2.6, label=r"$p_x=\partial L/\partial\dot x$ (x is cyclic)"); b.plot(t, vy - g * t, color=RED, lw=2.6, label=r"$p_y=m\dot y$ (y appears in $U=mgy$)")
    b.axhline(0, color=GREY, lw=1); b.set_xlabel("t (s)"); b.set_ylabel("momentum / m (m/s)"); b.legend(fontsize=8.5, loc="lower left"); b.set_title(r"$L=\frac{1}{2}m(\dot x^2+\dot y^2)-mgy$ does not contain $x$")
    save(fig, "cyclic-projectile")


def eff_potential():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.0), gridspec_kw={"width_ratios": [1.25, 1]})
    r = np.linspace(.28, 6, 800); Ue = -1 / r + .5 / r ** 2
    a.plot(r, -1 / r, color=GREY, ls="--", lw=1.6, label=r"gravity  $-k/r$"); a.plot(r, .5 / r ** 2, color=PURPLE, ls="--", lw=1.6, label=r"centrifugal  $L^2/2mr^2$"); a.plot(r, Ue, color=BLUE, lw=3, label=r"$U_{\rm eff}$")
    for E, c, lab in ((-.5, GREEN, "circle"), (-.3, ORANGE, "ellipse"), (0, RED, "parabola"), (.3, TEAL, "hyperbola")):
        a.axhline(E, color=c, lw=1.5, ls=":"); a.text(5.95, E + .03, lab + "  E=%+.1f" % E, ha="right", color=c, fontsize=8.5)
        if E < 0 and E > -.5:
            d = np.sqrt(1 + 2 * E); r1, r2 = (-1 + d) / (2 * E), (-1 - d) / (2 * E); a.plot([r1, r2], [E, E], "o", color=c, ms=6)
        if E == 0:
            a.plot([.5], [0], "o", color=c, ms=6)
        if E == .3:
            d = np.sqrt(1 + 2 * E); a.plot([(-1 - d) / (2 * E)], [E], "o", color=c, ms=6)
    a.plot([1], [-.5], "o", color=GREEN, ms=7); a.set_ylim(-1.05, .9); a.set_xlim(0, 6); a.set_xlabel(r"$r$  (units of $L^2/mk$)"); a.set_ylabel(r"energy  (units of $mk^2/L^2$)"); a.legend(fontsize=8.5, loc="lower right"); a.set_title("Effective potential: one-dimensional motion in r")
    th = np.linspace(0, 2 * np.pi, 600)
    for e, c in ((0, GREEN), (.6, ORANGE), (1, RED), (1.6, TEAL)):
        ph = th[(1 + e * np.cos(th)) > .12]; rr = 1 / (1 + e * np.cos(ph)); b.plot(rr * np.cos(ph), rr * np.sin(ph), color=c, lw=2.2, label="e = %.1f" % e)
    b.plot([0], [0], "o", color=INK, ms=7); b.set_aspect("equal"); b.set_xlim(-2.3, 4.4); b.set_ylim(-3, 3); b.legend(fontsize=8.5, loc="upper right"); b.set_title("The matching orbits (focus at the centre)"); b.set_xlabel("x"); b.set_ylabel("y")
    save(fig, "eff-potential")


def conics():
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    th = np.linspace(-np.pi, np.pi, 1500)
    for e, c, lab in ((0, GREEN, "circle  e=0"), (.5, ORANGE, "ellipse  e=0.5"), (.9, GOLD, "ellipse  e=0.9"), (1, RED, "parabola  e=1"), (1.6, TEAL, "hyperbola  e=1.6")):
        ph = th[(1 + e * np.cos(th)) > .15]; rr = 1 / (1 + e * np.cos(ph)); ax.plot(rr * np.cos(ph), rr * np.sin(ph), color=c, lw=2.2, label=lab)
    ax.plot([0], [0], "o", color=INK, ms=8); ax.annotate("focus (Sun)", (0, 0), (-3.4, -1.3), fontsize=9, arrowprops=dict(arrowstyle="->", color=INK)); ax.set_aspect("equal"); ax.set_xlim(-11, 3.5); ax.set_ylim(-4.5, 4.5)
    ax.legend(fontsize=9, loc="upper left"); ax.set_title(r"All conic sections $r=\ell/(1+e\cos\phi)$ with the same semi-latus rectum $\ell$"); ax.set_xlabel("x / ℓ"); ax.set_ylabel("y / ℓ")
    save(fig, "conics")


def kepler_laws():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.2), gridspec_kw={"width_ratios": [1.15, 1]})
    e, A = .6, 1.0; Bm = A * np.sqrt(1 - e ** 2); E = np.linspace(0, 2 * np.pi, 600)
    a.plot(A * (np.cos(E) - e), Bm * np.sin(E), color=INK, lw=1.8); a.plot([0], [0], "o", color=GOLD, ms=14, mec=INK); a.text(.05, -.14, "Sun (focus)", fontsize=8.5)

    def pos(Mn):
        Ek = Mn
        for _ in range(60):
            Ek = Ek - (Ek - e * np.sin(Ek) - Mn) / (1 - e * np.cos(Ek))
        return A * (np.cos(Ek) - e), Bm * np.sin(Ek)
    area_tot = np.pi * A * Bm
    for m0, c in ((0.0, BLUE), (np.pi, ORANGE)):
        Ms = np.linspace(m0, m0 + 2 * np.pi / 6, 60); pts = np.array([pos(m) for m in Ms]); poly = np.vstack([[0, 0], pts]); a.fill(poly[:, 0], poly[:, 1], color=c, alpha=.35, lw=0)
        a.plot(pts[:, 0], pts[:, 1], color=c, lw=3.2)
    a.text(.7, .12, "fast\n(near Sun)", color=BLUE, fontsize=8.5); a.text(-1.5, -.17, "slow", color=ORANGE, fontsize=9)
    a.text(-1.95, -1.42, "equal areas in equal times: each wedge is 1/6 of a period\nand so 1/6 of the ellipse area", fontsize=8.2, va="bottom")
    a.set_aspect("equal"); a.set_title("Kepler I and II (e = 0.6)"); a.set_xlabel("x / a"); a.set_ylabel("y / a"); a.set_xlim(-2, 1.4); a.set_ylim(-1.45, 1.0)
    names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    aa = np.array([.387, .723, 1.0, 1.524, 5.203, 9.537, 19.19, 30.07]); TT = np.array([.2408, .6152, 1.0, 1.881, 11.862, 29.457, 84.01, 164.8])
    slope = np.polyfit(np.log10(aa), np.log10(TT), 1)[0]
    b.loglog(aa, TT, "o", color=BLUE, ms=7); xs = np.logspace(-.5, 1.6, 50); b.loglog(xs, xs ** 1.5, color=RED, lw=1.8, ls="--", label=r"$T\propto a^{3/2}$")
    for n, x_, y_ in zip(names, aa, TT):
        b.annotate(n, (x_, y_), (6, -10), textcoords="offset points", fontsize=8)
    b.set_xlabel("semi-major axis a (AU)"); b.set_ylabel("period T (years)"); b.legend(fontsize=9, loc="upper left"); b.set_title("Kepler III: fitted slope %.3f" % slope)
    save(fig, "kepler-laws")
    print("Kepler III log-log slope over the 8 planets:", round(slope, 4), " (expected 1.5)")


def two_body():
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    m1, m2 = 3.0, 1.0; M = m1 + m2; e, p = .5, 1.0; ph = np.linspace(0, 2 * np.pi, 600); r = p / (1 + e * np.cos(ph)); X, Y = r * np.cos(ph), r * np.sin(ph)
    ax.plot(m2 / M * X, m2 / M * Y, color=BLUE, lw=2.4, label=r"heavy mass $m_1=3$"); ax.plot(-m1 / M * X, -m1 / M * Y, color=ORANGE, lw=2.4, label=r"light mass $m_2=1$")
    for k in (0, 100, 220, 360, 450):
        P1, P2 = (m2 / M * X[k], m2 / M * Y[k]), (-m1 / M * X[k], -m1 / M * Y[k]); ax.plot(*zip(P1, P2), color=GREY, lw=1, ls=":"); ax.plot(*P1, "o", color=BLUE, ms=11, mec=INK); ax.plot(*P2, "o", color=ORANGE, ms=7, mec=INK)
    ax.plot(0, 0, "+", color=RED, ms=16, mew=3); ax.text(.04, .06, "centre of mass", color=RED, fontsize=9)
    ax.set_aspect("equal"); ax.set_xlim(-.7, 2.7); ax.legend(fontsize=9, loc="upper right"); ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(r"Both bodies orbit the CM; the separation $\mathbf{r}$ moves like one body of mass $\mu=m_1m_2/(m_1+m_2)=0.75$", fontsize=9)
    save(fig, "two-body")


def hohmann():
    fig, ax = plt.subplots(figsize=(6.6, 5.4)); blank(ax, (-2.0, 1.7, -2.2, 1.7))
    r1, r2 = 1.0, 1.524; a_t = (r1 + r2) / 2; e_t = (r2 - r1) / (r2 + r1); th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r1 * np.cos(th), r1 * np.sin(th), color=BLUE, lw=2); ax.plot(r2 * np.cos(th), r2 * np.sin(th), color=RED, lw=2)
    ph = np.linspace(0, np.pi, 300); rt = a_t * (1 - e_t ** 2) / (1 + e_t * np.cos(ph)); ax.plot(rt * np.cos(ph), rt * np.sin(ph), color=GREEN, lw=3, ls="--")
    ax.plot(0, 0, "o", color=GOLD, ms=16, mec=INK); ax.plot([r1], [0], "o", color=BLUE, ms=9); ax.plot([-r2], [0], "o", color=RED, ms=9)
    ax.text(r1 + .05, -.17, "burn 1\nat departure", color=GREEN, fontsize=9); ax.text(-r2 - .05, -.35, "burn 2\nat arrival", color=GREEN, fontsize=9, ha="center")
    ax.text(0, .45, "transfer ellipse:\nhalf an orbit", color=GREEN, fontsize=9, ha="center"); ax.text(.55, -1.1, "inner orbit", color=BLUE, fontsize=9); ax.text(-1.6, -1.2, "outer orbit", color=RED, fontsize=9)
    arrow(ax, r1, 0, r1, .35, color=GREEN, lw=2.4); arrow(ax, -r2, 0, -r2, -.3, color=GREEN, lw=2.4)
    vp = np.sqrt(2 / r1 - 1 / a_t); va = np.sqrt(2 / r2 - 1 / a_t); dv1 = vp - 1; dv2 = np.sqrt(1 / r2) - va; tt = .5 * a_t ** 1.5 * 365.25
    ax.text(-1.95, -1.65, "Earth to Mars (a = 1 and 1.524 AU):\n" + r"$\Delta v_1=%.3f\,v_1$,   $\Delta v_2=%.3f\,v_1$   (%.0f days)" % (dv1, dv2, tt), fontsize=8.5, va="top")
    save(fig, "hohmann")
    print("Hohmann Earth->Mars: dv1 = %.4f v1 (= %.2f km/s), dv2 = %.4f v1 (= %.2f km/s), time %.0f days" % (dv1, dv1 * 29.78, dv2, dv2 * 29.78, tt))


if __name__ == "__main__":
    generalized_coords(); cyclic_projectile(); eff_potential(); conics(); kepler_laws(); two_body(); hohmann()
