"""Figures for Modules 3 and 4: oscillations, damping, driving, 1-D potentials and phase portraits. Also prints the numbers quoted in the notes."""
from ph_common import *
from scipy.integrate import solve_ivp
from scipy.special import ellipk
from matplotlib.patches import Circle, Arc


def shm_signals():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.7), gridspec_kw={"width_ratios": [1.5, 1]})
    w = 2 * np.pi; t = np.linspace(0, 2, 500); A = 1
    a.plot(t, A * np.cos(w * t), color=BLUE, lw=2.6, label=r"$x=A\cos\omega t$")
    a.plot(t, -A * w * np.sin(w * t) / w, color=ORANGE, lw=2.2, label=r"$v/\omega=-A\sin\omega t$  (leads $x$ by $90^\circ$)")
    a.plot(t, -A * np.cos(w * t), color=GREEN, lw=2.2, ls="--", label=r"$a/\omega^{2}=-A\cos\omega t$  (opposite to $x$)")
    a.set_xlabel("t / T"); a.set_ylim(-1.5, 1.9); a.legend(fontsize=8, loc="upper right", ncol=1); a.set_title("Displacement, velocity and acceleration")
    blank(b, (-1.7, 1.9, -1.55, 1.55))
    th = np.linspace(0, 2 * np.pi, 200); b.plot(np.cos(th), np.sin(th), color=GREY, lw=1.2)
    p = np.radians(55); b.plot(*zip((0, 0), (np.cos(p), np.sin(p))), color=INK, lw=2.2); b.plot(np.cos(p), np.sin(p), "o", color=INK)
    b.plot([np.cos(p)] * 2, [0, np.sin(p)], ls=":", color=GREY); arrow(b, 0, 0, np.cos(p), 0, color=BLUE, lw=3)
    b.annotate("", xy=(np.cos(p) + .35, np.sin(p)), xytext=(np.cos(p), np.sin(p)), arrowprops=dict(arrowstyle="->", color=GREY))
    b.add_patch(Arc((0, 0), .8, .8, theta1=0, theta2=55, color=INK)); b.text(.5, .12, r"$\omega t$", fontsize=10)
    b.text(.22, -.28, r"$x=A\cos\omega t$", color=BLUE, fontsize=10); b.text(-1.65, 1.35, "uniform circular motion,\nseen edge-on", fontsize=9)
    save(fig, "shm-signals")


def shm_energy():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.7))
    w = 2 * np.pi; t = np.linspace(0, 2, 500); k = 1.0; A = 1.0
    PE = .5 * k * A ** 2 * np.cos(w * t) ** 2; KE = .5 * k * A ** 2 * np.sin(w * t) ** 2
    a.plot(t, PE, color=BLUE, lw=2.4, label=r"potential $\frac{1}{2}kx^{2}$"); a.plot(t, KE, color=ORANGE, lw=2.4, label=r"kinetic $\frac{1}{2}mv^{2}$")
    a.plot(t, PE + KE, color=INK, lw=2, ls="--", label="total E (constant)")
    a.set_xlabel("t / T"); a.set_ylabel("energy / (kA²)"); a.set_ylim(0, .75); a.legend(fontsize=8.5, loc="upper right"); a.set_title("Energy swaps forms twice per cycle")
    x = np.linspace(-1.25, 1.25, 300); b.plot(x, .5 * x ** 2, color=BLUE, lw=2.4); b.axhline(.5, color=INK, ls="--", lw=1.6)
    x0 = .6; b.plot([x0, x0], [0, .5 * x0 ** 2], color=BLUE, lw=6, alpha=.6, solid_capstyle="butt"); b.plot([x0, x0], [.5 * x0 ** 2, .5], color=ORANGE, lw=6, alpha=.6, solid_capstyle="butt")
    b.text(x0 + .05, .08, "U", color=BLUE, fontsize=11); b.text(x0 + .05, .33, "K", color=ORANGE, fontsize=11)
    b.plot([-1, 1], [.5, .5], "o", color=RED, ms=6); b.text(1.02, .52, "turning point", fontsize=8.5, color=RED); b.text(-1.2, .52, "turning point", fontsize=8.5, color=RED)
    b.set_xlabel("x / A"); b.set_ylabel("U(x)"); b.set_ylim(0, .75); b.set_title("Gap between E and U = kinetic energy")
    save(fig, "shm-energy")


def damped_regimes():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.7), gridspec_kw={"width_ratios": [1.4, 1]})
    w0 = 1.0; t = np.linspace(0, 25, 1000)
    for beta, c, lab in ((0.1, BLUE, r"underdamped  $\beta=0.1\,\omega_0$"), (1.0, GREEN, r"critical  $\beta=\omega_0$"), (3.0, ORANGE, r"overdamped  $\beta=3\,\omega_0$")):
        if beta < w0:
            w1 = np.sqrt(w0 ** 2 - beta ** 2); x = np.exp(-beta * t) * (np.cos(w1 * t) + beta / w1 * np.sin(w1 * t))
        elif beta == w0:
            x = (1 + beta * t) * np.exp(-beta * t)
        else:
            r = np.sqrt(beta ** 2 - w0 ** 2); r1, r2 = -beta + r, -beta - r; x = (r2 * np.exp(r1 * t) - r1 * np.exp(r2 * t)) / (r2 - r1)
        a.plot(t, x, color=c, lw=2.4, label=lab)
    a.plot(t, np.exp(-0.1 * t), color=BLUE, ls=":", lw=1.4); a.plot(t, -np.exp(-0.1 * t), color=BLUE, ls=":", lw=1.4); a.text(14.5, .45, r"envelope $e^{-\beta t}$", color=BLUE, fontsize=9)
    a.axhline(0, color=GREY, lw=1); a.set_xlabel(r"$\omega_0 t$"); a.set_ylabel("x / x(0)"); a.set_ylim(-1.1, 1.15); a.legend(fontsize=8.5, loc="upper right"); a.set_title("Release from rest at x(0) = 1")
    bs = np.linspace(0, 3, 400)
    for sgn in (1, -1):
        re = np.where(bs < 1, -bs, -bs + sgn * np.sqrt(np.maximum(bs ** 2 - 1, 0))); im = np.where(bs < 1, sgn * np.sqrt(np.maximum(1 - bs ** 2, 0)), 0)
        b.plot(re, im, color=PURPLE, lw=2.4)
    for beta, c in ((0, BLUE), (0.1, BLUE), (1, GREEN), (3, ORANGE)):
        if beta < 1:
            b.plot([-beta] * 2, [np.sqrt(1 - beta ** 2), -np.sqrt(1 - beta ** 2)], "o", color=c, ms=7)
        elif beta == 1:
            b.plot([-1], [0], "o", color=c, ms=7)
        else:
            rr = np.sqrt(beta ** 2 - 1); b.plot([-beta + rr, -beta - rr], [0, 0], "o", color=c, ms=7)
    b.axhline(0, color=GREY, lw=1); b.axvline(0, color=GREY, lw=1); b.set_xlabel(r"Re $r/\omega_0$"); b.set_ylabel(r"Im $r/\omega_0$"); b.set_xlim(-6.2, .5); b.set_ylim(-1.3, 1.3)
    b.set_title(r"Roots as $\beta$ grows: circle, then split"); b.text(-5.2, .55, "complex pair on a circle of radius " + r"$\omega_0$" + "\nuntil " + r"$\beta=\omega_0$" + ", then two real roots", fontsize=8.5)
    save(fig, "damped-regimes")


def driven_resonance():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
    r = np.linspace(0.01, 2.2, 800)
    for z, c in ((0.05, RED), (0.1, ORANGE), (0.25, GREEN), (0.5, BLUE), (0.9, PURPLE)):
        amp = 1 / np.sqrt((1 - r ** 2) ** 2 + (2 * z * r) ** 2); dl = np.degrees(np.arctan2(2 * z * r, 1 - r ** 2))
        a.plot(r, amp, color=c, lw=2.2, label=r"$Q=%.1f$" % (1 / (2 * z))); b.plot(r, dl, color=c, lw=2.2)
        if z < .7:
            rp = np.sqrt(1 - 2 * z ** 2); a.plot(rp, 1 / (2 * z * np.sqrt(1 - z ** 2)), "o", color=c, ms=4.5)
    a.set_ylim(0, 6); a.set_xlabel(r"driving frequency $\omega/\omega_0$"); a.set_ylabel(r"amplitude $/\,(F_0/k)$"); a.legend(fontsize=8.5, title="quality factor", title_fontsize=8.5)
    a.set_title("Narrow tall peaks for small damping"); b.set_xlabel(r"$\omega/\omega_0$"); b.set_ylabel(r"phase lag $\delta$ (degrees)"); b.set_yticks([0, 45, 90, 135, 180]); b.axhline(90, color=GREY, ls=":")
    b.set_title("Response lags the push by 90° at resonance")
    save(fig, "driven-resonance")


def rk(f, y0, t):
    return solve_ivp(f, (t[0], t[-1]), y0, t_eval=t, rtol=1e-9, atol=1e-11).y


def driven_transient():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.7), gridspec_kw={"width_ratios": [1.4, 1]})
    beta, w0, F, w = 0.08, 1.0, 1.0, 0.8; t = np.linspace(0, 120, 6000)
    f = lambda t, y: [y[1], -2 * beta * y[1] - w0 ** 2 * y[0] + F * np.cos(w * t)]
    x, v = solve_ivp(f, (0, 120), [0, 0], t_eval=t, rtol=1e-9, atol=1e-11).y
    D = np.sqrt((w0 ** 2 - w ** 2) ** 2 + (2 * beta * w) ** 2); Ass = F / D
    a.plot(t, x, color=BLUE, lw=1.6); a.axhline(Ass, color=RED, ls="--", lw=1.4); a.axhline(-Ass, color=RED, ls="--", lw=1.4)
    a.text(80, Ass + .12, "steady-state amplitude", color=RED, fontsize=8.5)
    a.set_xlabel(r"$\omega_0 t$"); a.set_ylabel("x"); a.set_title("Transient fades; steady state stays")
    b.plot(x, v, color=BLUE, lw=1.0); b.plot(x[0], v[0], "o", color=GREEN); b.plot(x[-1], v[-1], "o", color=RED)
    th = np.linspace(0, 2 * np.pi, 200); b.plot(Ass * np.cos(th), -Ass * w * np.sin(th + np.arctan2(2 * beta * w, w0 ** 2 - w ** 2)), color=RED, ls="--", lw=1.4)
    b.set_xlabel("x"); b.set_ylabel("v"); b.set_title("Spiral onto the limit cycle"); b.set_aspect("equal", "datalim")
    save(fig, "driven-transient")
    print("driven amplitude (beta=0.08, w=0.8):", round(Ass, 3), " numeric late max:", round(np.max(np.abs(x[t > 100])), 3))


def potential_1d():
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    U = lambda x: x ** 4 / 4 - x ** 2 / 2 + 0.12 * x
    x = np.linspace(-1.9, 1.9, 600); ax.plot(x, U(x), color=BLUE, lw=2.8)
    roots = np.roots([1, 0, -1, 0.12]).real; roots.sort()
    xs_min1, xs_max, xs_min2 = roots[0], roots[1], roots[2]
    ax.plot([xs_min1, xs_min2], [U(xs_min1), U(xs_min2)], "o", color=GREEN, ms=9, zorder=5); ax.plot([xs_max], [U(xs_max)], "o", color=RED, ms=9, zorder=5)
    ax.text(xs_min1, U(xs_min1) - .2, "stable", color=GREEN, fontsize=9, ha="center")
    ax.annotate("stable", (xs_min2, U(xs_min2)), (xs_min2 + .1, U(xs_min2) + .5), color=GREEN, fontsize=9, ha="center", arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.annotate("unstable\n" + r"$U''<0$", (xs_max, U(xs_max)), (xs_max + .1, U(xs_max) + .62), color=RED, fontsize=9, ha="center", arrowprops=dict(arrowstyle="->", color=RED))
    for E, c, lab in ((-0.18, ORANGE, "E₁: trapped in the deep well"), (0.12, PURPLE, "E₂: crosses the hump, both wells"), (0.55, TEAL, "E₃: reaches every x shown")):
        ax.axhline(E, color=c, lw=1.6, ls="--"); ax.text(1.95, E + .03, lab, color=c, fontsize=8.5, va="bottom")
    E = -0.18; xr = np.roots([1, 0, -2, .48, 4 * -E]) if False else None
    xx = x[(U(x) <= -0.18)]; xa, xb = xx[0], xx[xx < 0][-1] if np.any(xx < 0) else xx[-1]
    ax.plot([xa, xb], [-0.18, -0.18], "|", color=ORANGE, ms=18, mew=3)
    ax.text((xa + xb) / 2, -0.18 + .08, "turning points", fontsize=8, color=ORANGE, ha="center")
    ax.set_ylim(-.6, 1.75); ax.set_xlim(-1.9, 3.6); ax.set_xlabel("x"); ax.set_ylabel("U(x)"); ax.set_title("A potential energy curve encodes every 1-D motion at once")
    save(fig, "potential-1d")


def phase_linear():
    fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.4))
    cases = [("undamped\n(ellipses)", 0.0), ("underdamped\n(spiral)", 0.2), ("critical", 1.0), ("overdamped\n(node)", 2.0)]
    for ax, (title, beta) in zip(axs, cases):
        f = lambda t, y: [y[1], -2 * beta * y[1] - y[0]]
        for ic in [(1, 0), (0, 1), (-1.2, 0.3), (0.5, -1.4), (-0.4, -0.5), (1.5, 1.2), (-1.5, -1.2)]:
            tt = np.linspace(0, 40, 4000); x, v = rk(f, ic, tt)
            ax.plot(x, v, lw=1.5, color=BLUE, alpha=.9)
            k = int(len(tt) * (0.04 if beta == 0 else 0.015)); ax.annotate("", xy=(x[k + 4], v[k + 4]), xytext=(x[k], v[k]), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
        ax.plot([0], [0], "o", color=INK, ms=5); ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8); ax.set_aspect("equal"); ax.set_title(title, fontsize=10); ax.set_xlabel("x")
        if ax is axs[0]:
            ax.set_ylabel(r"$v/\omega_0$")
    save(fig, "phase-linear")


def phase_pendulum():
    fig, ax = plt.subplots(figsize=(9.2, 4.2))
    th = np.linspace(-2 * np.pi, 2 * np.pi, 600); om = np.linspace(-3, 3, 400); T, O = np.meshgrid(th, om)
    H = O ** 2 / 2 - np.cos(T)
    ax.contour(T, O, H, levels=[-.9, -.7, -.4, -.1, .3, .6, 1.5, 2.2, 3, 4, 5], colors=BLUE, linewidths=1.1, alpha=.8)
    ax.contour(T, O, H, levels=[1.0], colors=RED, linewidths=2.6)
    for c in (0, 2 * np.pi, -2 * np.pi):
        ax.plot(c, 0, "o", color=GREEN, ms=8, zorder=5)
    for c in (np.pi, -np.pi):
        ax.plot(c, 0, "X", color=RED, ms=10, zorder=5)
    ax.text(0.1, .32, "libration\n(back and forth)", color=BLUE, fontsize=9, ha="center"); ax.text(0, 2.35, "rotation (over the top)", color=BLUE, fontsize=9, ha="center")
    ax.text(0.4, 1.35, "separatrix  E = mgl", color=RED, fontsize=9, rotation=0)
    ax.text(np.pi + .12, -.45, "unstable\n(upside down)", color=RED, fontsize=8.5); ax.text(.12, -.5, "stable", color=GREEN, fontsize=8.5)
    ax.set_xticks(np.pi * np.arange(-2, 3)); ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    ax.set_xlabel(r"angle $\theta$"); ax.set_ylabel(r"$\dot\theta/\omega_0$"); ax.set_title("Phase portrait of the undamped pendulum")
    save(fig, "phase-pendulum")


def pendulum_period():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.7))
    th0 = np.radians(np.linspace(0.5, 175, 400)); ratio = 2 * ellipk(np.sin(th0 / 2) ** 2) / np.pi
    a.plot(np.degrees(th0), ratio, color=BLUE, lw=2.6, label="exact: " + r"$T/T_0=\frac{2}{\pi}K(\sin\frac{\theta_0}{2})$")
    a.plot(np.degrees(th0), 1 + th0 ** 2 / 16, color=ORANGE, ls="--", lw=2, label=r"first correction $1+\theta_0^{2}/16$")
    a.axhline(1, color=GREY, lw=1.2); a.set_ylim(.95, 3.2)
    for d in (30, 90, 150):
        r_ = 2 * ellipk(np.sin(np.radians(d) / 2) ** 2) / np.pi; a.plot(d, r_, "o", color=RED, ms=6); a.text(d - 4, r_ + .12, "%.3f" % r_, fontsize=8.5, color=RED, ha="right")
    a.set_xlabel(r"amplitude $\theta_0$ (degrees)"); a.set_ylabel(r"$T/T_0$"); a.legend(fontsize=8.5, loc="upper left"); a.set_title("Bigger swings take longer")
    t = np.linspace(0, 14, 1400)
    for d, c in ((10, BLUE), (90, GREEN), (170, RED)):
        y = rk(lambda t, y: [y[1], -np.sin(y[0])], (np.radians(d), 0), t)[0]; b.plot(t, y / np.radians(d), color=c, lw=2, label=r"$\theta_0=%d^\circ$" % d)
    b.plot(t, np.cos(t), color=GREY, ls=":", lw=1.4, label="SHM"); b.set_xlabel(r"$\omega_0 t$"); b.set_ylabel(r"$\theta/\theta_0$"); b.set_ylim(-1.6, 1.15); b.legend(fontsize=8, loc="lower center", ncol=4, columnspacing=1.0, handlelength=1.4); b.set_title("Large swings flatten at the turning points")
    save(fig, "pendulum-period")
    print("T/T0 at 30, 90, 150 deg:", [round(float(2 * ellipk(np.sin(np.radians(d) / 2) ** 2) / np.pi), 4) for d in (30, 90, 150)])


def double_well():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.0))
    x = np.linspace(-2, 2, 600); U = x ** 4 / 4 - x ** 2 / 2
    a.plot(x, U, color=BLUE, lw=2.8)
    for E, c in ((-0.2, ORANGE), (0.0, RED), (0.5, GREEN)):
        a.axhline(E, color=c, ls="--", lw=1.5)
    a.plot([-1, 1], [-.25, -.25], "o", color=GREEN, ms=8); a.plot([0], [0], "o", color=RED, ms=8); a.set_ylim(-.45, 1.3); a.set_xlabel("x"); a.set_ylabel("U(x)")
    a.text(-2.1, -0.36, "E<0: trapped in one well", color=ORANGE, fontsize=8.5); a.text(.15, .04, "E=0: separatrix", color=RED, fontsize=8.5); a.text(-1.95, .55, "E>0: free to cross", color=GREEN, fontsize=8.5)
    a.set_title("Double-well potential  $U=x^4/4-x^2/2$")
    X, V = np.meshgrid(np.linspace(-2.2, 2.2, 500), np.linspace(-1.6, 1.6, 400)); H = V ** 2 / 2 + X ** 4 / 4 - X ** 2 / 2
    b.contour(X, V, H, levels=[-.2, -.1, .1, .25, .5, .8, 1.2], colors=BLUE, linewidths=1.2); b.contour(X, V, H, levels=[0], colors=RED, linewidths=2.6)
    b.plot([-1, 1], [0, 0], "o", color=GREEN, ms=8); b.plot([0], [0], "X", color=RED, ms=10)
    b.set_xlabel("x"); b.set_ylabel("v"); b.set_title("Phase space: the figure-eight is E = 0")
    save(fig, "double-well")


if __name__ == "__main__":
    shm_signals(); shm_energy(); damped_regimes(); driven_resonance(); driven_transient(); potential_1d(); phase_linear(); phase_pendulum(); pendulum_period(); double_well()
