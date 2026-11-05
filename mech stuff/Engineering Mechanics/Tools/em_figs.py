"""AM1100 Engineering Mechanics figures + the numbers quoted in the notes. Output: ../assets/EM-*.png"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets")); os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, GREEN, RED, PURPLE, GREY, TEAL = "#2b6cb0", "#dd6b20", "#2f855a", "#c53030", "#6b46c1", "#718096", "#2c7a7b"
plt.rcParams.update({"figure.dpi": 150, "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": "#e2e8f0",
                     "axes.axisbelow": True, "legend.frameon": False, "axes.prop_cycle": matplotlib.cycler(color=[BLUE, ORANGE, GREEN, RED, PURPLE, TEAL])})
g = 9.81


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, "EM-%s.png" % name), bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote EM-%s.png" % name)


def arr(ax, p0, p1, c="k", lw=2, ms=12, **kw):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, mutation_scale=ms, shrinkA=0, shrinkB=0, **kw))


def nogrid(ax, lim=None):
    ax.axis("off"); ax.set_aspect("equal")
    if lim:
        ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])


# ----------------------------------------------------------------------------- statics
def force_system():
    F1 = 200 * np.array([np.cos(np.radians(30)), np.sin(np.radians(30))]); F2 = 300 * np.array([np.cos(np.radians(120)), np.sin(np.radians(120))]); R = F1 + F2
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.1))
    nogrid(a, (-190, 260, -30, 460)); arr(a, (0, 0), tuple(F1), BLUE); arr(a, (0, 0), tuple(F2), ORANGE); arr(a, (0, 0), tuple(R), RED, lw=3)
    a.plot([F1[0], R[0]], [F1[1], R[1]], color=ORANGE, ls="--", lw=1); a.plot([F2[0], R[0]], [F2[1], R[1]], color=BLUE, ls="--", lw=1)
    a.text(F1[0] + 5, F1[1] - 25, "F₁ = 200 N at 30°", color=BLUE, fontsize=9); a.text(F2[0] - 140, F2[1] + 10, "F₂ = 300 N at 120°", color=ORANGE, fontsize=9)
    a.text(R[0] + 8, R[1] + 5, "R = %.0f N at %.1f°" % (np.hypot(*R), np.degrees(np.arctan2(R[1], R[0]))), color=RED, fontsize=9.5, fontweight="bold"); a.set_title("2-D: add components, then R and angle")
    F = np.array([300, -200, 400.]); Fm = np.linalg.norm(F); l = F / Fm
    ax = b; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.text(.3, 9, r"3-D force  $\mathbf{F}=(300,\,-200,\,400)$ N", fontsize=11)
    ax.text(.3, 7.8, r"$F=\sqrt{300^2+200^2+400^2}=%.1f$ N" % Fm, fontsize=11)
    ax.text(.3, 6.3, "direction cosines  l = F_x/F = %.3f" % l[0], fontsize=10.5); ax.text(.3, 5.4, "                                    m = F_y/F = %.3f" % l[1], fontsize=10.5); ax.text(.3, 4.5, "                                    n = F_z/F = %.3f" % l[2], fontsize=10.5)
    ax.text(.3, 3.2, r"check:  $l^2+m^2+n^2=%.3f$" % (l @ l), fontsize=11, color=GREEN); ax.text(.3, 2.0, "angles: θx = %.1f°, θy = %.1f°, θz = %.1f°" % tuple(np.degrees(np.arccos(l))), fontsize=10.5)
    ax.set_title("3-D: three components and three direction cosines")
    save(fig, "force-system")
    print("force system: R =", np.round(R, 2), round(float(np.hypot(*R)), 1), "N at", round(float(np.degrees(np.arctan2(R[1], R[0]))), 1), "deg;  3-D |F| =", round(float(Fm), 2), "cosines", np.round(l, 3), "angles", np.round(np.degrees(np.arccos(l)), 1))


def moments_couples():
    fig, (a, b, c) = plt.subplots(1, 3, figsize=(11.4, 3.9))
    nogrid(a, (-1, 6, -1.5, 5)); a.plot(0, 0, "ko"); a.text(-.4, -.6, "O", fontsize=11); P = np.array([3, 2]); F = np.array([60, 80]) / 30; arr(a, tuple(P), tuple(P + F), RED, lw=2.6)
    arr(a, (0, 0), tuple(P), GREY, lw=1.4); a.text(1.1, .6, "r = (3, 2) m", fontsize=9, color=GREY); a.text(P[0] + F[0] - 1.9, P[1] + F[1] + .15, "F = (60, 80) N", color=RED, fontsize=9)
    a.text(-.9, -.9, "M_O = x F_y − y F_x = 3(80) − 2(60) = 120 N·m (ccw)", fontsize=8.5); a.set_title("Moment of a force about O")
    nogrid(b, (-1, 6, -2, 4)); arr(b, (1, 3), (1, 1), RED, lw=2.6); arr(b, (4, 1), (4, 3), RED, lw=2.6); b.plot([1, 4], [2, 2], "k:", lw=1); b.text(2.4, 2.1, "d", fontsize=11)
    b.text(.2, -1.2, "couple M = F d, the same about ANY point", fontsize=9); b.text(1.3, 3.4, "F", color=RED); b.text(4.1, 3.2, "F", color=RED); b.set_title("A couple: equal, opposite, parallel forces")
    nogrid(c, (-1, 9, -2, 4)); arr(c, (0, 1), (2, 1), RED, lw=2.6); c.plot(0, 1, "ko"); c.text(.8, 1.4, "F", color=RED); c.text(3.0, 1.0, "≡", fontsize=18); c.plot(4.5, 1, "ko"); arr(c, (4.5, 1), (6.5, 1), RED, lw=2.6)
    th = np.linspace(-.9, .9, 40); c.plot(4.5 + .6 * np.cos(th + 1.57 + 1.57), 1 + .6 * np.sin(th + 3.14), color=PURPLE, lw=2); c.text(5.2, 2.2, "+ M = F d", color=PURPLE, fontsize=10)
    c.set_title("Force at A ≡ force at O + a couple"); c.text(-.5, -1.3, "moving a force sideways adds the couple Fd", fontsize=9)
    save(fig, "moments-couples")


def supports():
    fig, ax = plt.subplots(figsize=(10.6, 3.6)); ax.axis("off"); ax.set_xlim(0, 22); ax.set_ylim(-1.5, 5)
    def beamtip(x, y): ax.plot([x - 1.2, x + .6], [y, y], color="k", lw=4)
    # roller
    beamtip(2, 3); ax.add_patch(Circle((1.8, 2.7), .25, fc="w", ec="k")); ax.add_patch(Circle((.9, 2.7), .25, fc="w", ec="k")); ax.plot([0, 3], [2.4, 2.4], "k", lw=2); arr(ax, (1.4, 2.4), (1.4, 4.1), RED); ax.text(.4, 0.9, "Roller / smooth surface\n1 unknown: ⊥ to the surface", fontsize=8.5)
    # pin
    beamtip(8, 3); ax.add_patch(Polygon([(7.3, 3), (6.7, 2.2), (7.9, 2.2)], fc="w", ec="k")); ax.plot([6.3, 8.3], [2.2, 2.2], "k", lw=2); arr(ax, (7.3, 3), (7.3, 4.1), RED); arr(ax, (7.3, 3), (8.4, 3), RED); ax.text(5.6, 0.9, "Pin / hinge\n2 unknowns: Rx, Ry", fontsize=8.5)
    # fixed
    ax.add_patch(Rectangle((12.2, 2.2), .3, 1.6, fc="#cbd5e0", ec="k", hatch="////")); ax.plot([12.5, 14.5], [3, 3], color="k", lw=4); arr(ax, (12.5, 3.5), (12.5, 4.5), RED); arr(ax, (12.5, 3.1), (11.4, 3.1), RED); th = np.linspace(.4, 2.6, 30); ax.plot(12.5 + .5 * np.cos(th) * -1, 3 + .5 * np.sin(th) - 1.1, color=PURPLE, lw=2)
    ax.text(10.9, 0.9, "Fixed support\n3 unknowns: Rx, Ry and a moment M", fontsize=8.5)
    # cable
    ax.plot([18, 18], [2.4, 3.3], "k", lw=1.2); ax.plot([17.2, 18.8], [2.4, 2.4], "k", lw=2); ax.add_patch(Circle((18, 3.4), .15, fc="k")); ax.plot([18, 19.4], [3.4, 4.5], "k", lw=1.5, ls="--"); arr(ax, (18, 3.4), (18.7, 4.2), RED)
    ax.text(16.6, 0.9, "Cable / two-force link\n1 unknown: tension along it", fontsize=8.5)
    ax.set_title("Support reactions: one unknown for each motion the support prevents", fontsize=10.5)
    save(fig, "supports")


def solve_truss(nodes, members, supports_, loads):
    """nodes: {name:(x,y)}; members: [(a,b)]; supports_: {node:('pin'|'roller')}; loads: {node:(Fx,Fy)} -> member forces (tension +) and reactions"""
    names = list(nodes); idx = {n: i for i, n in enumerate(names)}; unknowns = len(members); rx = []
    for n, t in supports_.items():
        rx.append((n, "x")) if t == "pin" else None; rx.append((n, "y"))
    A = np.zeros((2 * len(names), unknowns + len(rx))); b = np.zeros(2 * len(names))
    for k, (p, q) in enumerate(members):
        d = np.array(nodes[q]) - np.array(nodes[p]); L = np.linalg.norm(d); u = d / L
        A[2 * idx[p], k] += u[0]; A[2 * idx[p] + 1, k] += u[1]; A[2 * idx[q], k] -= u[0]; A[2 * idx[q] + 1, k] -= u[1]
    for j, (n, c) in enumerate(rx):
        A[2 * idx[n] + (0 if c == "x" else 1), unknowns + j] = 1
    for n, (fx, fy) in loads.items():
        b[2 * idx[n]] -= fx; b[2 * idx[n] + 1] -= fy
    sol = np.linalg.solve(A, b); return sol[:unknowns], dict(zip(rx, sol[unknowns:]))


def truss():
    nodes = {"A": (0, 0), "B": (4, 0), "C": (8, 0), "D": (2, 3), "E": (6, 3)}
    members = [("A", "B"), ("B", "C"), ("A", "D"), ("D", "B"), ("D", "E"), ("B", "E"), ("E", "C")]
    F, R = solve_truss(nodes, members, {"A": "pin", "C": "roller"}, {"D": (0, -10), "E": (0, -10)})
    fig, ax = plt.subplots(figsize=(9.2, 4.3))
    for (p, q), f in zip(members, F):
        c = RED if f > 0.05 else (BLUE if f < -0.05 else GREY); ax.plot([nodes[p][0], nodes[q][0]], [nodes[p][1], nodes[q][1]], color=c, lw=3.4)
        mx, my = (nodes[p][0] + nodes[q][0]) / 2, (nodes[p][1] + nodes[q][1]) / 2
        ax.text(mx, my + (.28 if nodes[p][1] == nodes[q][1] == 0 else .1), "%s%s  %+.2f" % (p, q, f), ha="center", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1), color=c)
    for n, (x, y) in nodes.items():
        ax.plot(x, y, "ko", ms=7); ax.text(x - .15, y - .45 if y == 0 else y + .25, n, fontsize=11, fontweight="bold")
    for n in ("D", "E"):
        arr(ax, (nodes[n][0], nodes[n][1] + 1.3), nodes[n], "k", lw=2.2); ax.text(nodes[n][0] + .15, nodes[n][1] + 1.0, "10 kN")
    ax.add_patch(Polygon([(0, 0), (-.3, -.5), (.3, -.5)], fc="w", ec="k")); ax.add_patch(Circle((8, -.3), .22, fc="w", ec="k")); ax.plot([7.5, 8.5], [-.55, -.55], "k")
    ax.set_xlim(-1, 9.2); ax.set_ylim(-1.4, 4.8); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Solved by joint equilibrium (kN): red = tension, blue = compression")
    save(fig, "truss")
    print("truss forces kN:", {"%s%s" % m: round(float(f), 3) for m, f in zip(members, F)}, " reactions:", {k: round(float(v), 3) for k, v in R.items()})
    # method of sections: cut through DE, BE, BC, keep the right part (E, C)
    print("sections check, moment about B of right part: F_DE*3 ... = ", round(float(F[4]), 3))
    # simple triangle truss from the joints example
    n2 = {"A": (0, 0), "B": (6, 0), "C": (3, 4)}; m2 = [("A", "B"), ("A", "C"), ("B", "C")]
    F2, R2 = solve_truss(n2, m2, {"A": "pin", "B": "roller"}, {"C": (0, -10)}); print("triangle truss AB, AC, BC:", np.round(F2, 3), " reactions", {k: round(float(v), 2) for k, v in R2.items()})


def frame_fig():
    fig, ax = plt.subplots(figsize=(8.6, 4.3)); ax.axis("off"); ax.set_xlim(-2, 9); ax.set_ylim(-5.8, 3.4); ax.set_aspect("equal")
    ax.add_patch(Rectangle((-.35, -4.6), .35, 5.2, fc="#cbd5e0", ec="k", hatch="////")); ax.plot([0, 4], [0, 0], color=BLUE, lw=5); ax.plot([4, 0], [0, -4], color=ORANGE, lw=5)
    for p in ((0, 0), (0, -4), (4, 0)):
        ax.plot(*p, "o", color="w", mec="k", ms=10, mew=2)
    ax.text(-.5, .5, "A", fontsize=12, fontweight="bold"); ax.text(-.6, -4.5, "C", fontsize=12, fontweight="bold"); ax.text(4.2, .35, "B", fontsize=12, fontweight="bold")
    arr(ax, (2, 1.7), (2, .1), "k", lw=2.4); ax.text(2.15, 1.2, "20 kN", fontsize=10)
    ax.text(.3, -5.4, "BC: two-force member (force along BC)", color=ORANGE, fontsize=9)
    ax.text(5.1, -1.2, "Member AB (3 forces): load, pin A,\nand the force from BC.\n\nΣM_A = 0:  F_BC sin45° · 4 = 20 · 2\n⇒ F_BC = 14.14 kN (compression)\nΣFx: Ax = −10 kN ;  ΣFy: Ay = +10 kN", fontsize=9, va="top")
    ax.set_title("Frame with a two-force member: solve it first, it tells the direction")
    save(fig, "frame")
    print("frame: F_BC =", round(20 * 2 / (4 * np.sin(np.radians(45))), 3), " Ax, Ay =", -round(20 * 2 / 4, 2), round(20 - 10, 2))


def distributed():
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.7))
    x = np.linspace(0, 6, 100)
    cases = [("uniform  w = 5 kN/m", lambda x: 5 + 0 * x, 30, 3), ("triangular  0 → 9 kN/m", lambda x: 1.5 * x, 27, 4), ("trapezoid  3 → 9 kN/m", lambda x: 3 + x, 36, None)]
    for ax, (t, w, R, xb) in zip(axs, cases):
        ax.fill_between(x, 0, w(x), color=BLUE, alpha=.3); ax.plot(x, w(x), color=BLUE, lw=2.2); ax.set_ylim(0, 12.5); ax.set_xlim(0, 6.3)
        xc = np.trapezoid(x * w(x), x) / np.trapezoid(w(x), x); Rn = np.trapezoid(w(x), x); arr(ax, (xc, Rn / 6 + 1.5), (xc, 0.1), RED, lw=2.6)
        ax.text(xc + .2, Rn / 6 + 1.2, "R = %.0f kN\nat x = %.2f m" % (Rn, xc), color=RED, fontsize=9); ax.set_title(t, fontsize=10); ax.set_xlabel("x (m)"); ax.set_ylabel("w (kN/m)")
    save(fig, "distributed")
    print("distributed:", [(round(float(np.trapezoid(w(x), x)), 2), round(float(np.trapezoid(x * w(x), x) / np.trapezoid(w(x), x)), 3)) for _, w, _, _ in cases])


def friction_law():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9))
    P = np.linspace(0, 120, 400); mus, muk, N = .5, .4, 200.0; F = np.where(P <= mus * N, P, muk * N)
    a.plot(P, F, color=BLUE, lw=2.8); a.plot(P, np.minimum(P, 140), color=GREY, ls=":", lw=1); a.plot([mus * N], [mus * N], "o", color=RED); a.plot([mus * N, mus * N], [mus * N, muk * N], color=RED, ls="--")
    a.text(10, 70, "static: F = P (no motion)", color=BLUE, fontsize=9, rotation=40); a.text(102, 84, "kinetic: F = μ_k N", color=BLUE, fontsize=9); a.text(30, 106, "F_max = μ_s N", color=RED, fontsize=9)
    a.set_xlabel("applied force P (N)"); a.set_ylabel("friction force F (N)"); a.set_title("Friction law (N = 200 N)"); a.set_ylim(0, 120)
    th = np.linspace(0, 45, 200); mu = .5
    b.plot(th, np.tan(np.radians(th)), color=BLUE, lw=2.6, label="needed μ to hold: tan θ"); b.axhline(mu, color=RED, lw=1.6, ls="--", label="available μ_s = 0.5"); b.fill_between(th, 0, np.minimum(np.tan(np.radians(th)), mu), color=GREEN, alpha=.2)
    b.plot([np.degrees(np.arctan(mu))], [mu], "o", color=RED); b.text(np.degrees(np.arctan(mu)) + 1, .35, "slips beyond θ = %.1f°" % np.degrees(np.arctan(mu)), fontsize=9, color=RED)
    b.set_xlabel("incline angle θ (degrees)"); b.set_ylabel("coefficient of friction"); b.set_ylim(0, 1.1); b.legend(fontsize=8.5, loc="upper left"); b.set_title("Steepest stable slope: atan μ_s")
    save(fig, "friction-law")
    print("friction: angle of repose for mu=0.5:", round(float(np.degrees(np.arctan(.5))), 2), " tan25 =", round(float(np.tan(np.radians(25))), 4), " friction needed at 25 deg for 50 kg:", round(50 * g * np.sin(np.radians(25)), 1), "N; available", round(.5 * 50 * g * np.cos(np.radians(25)), 1))


def belt():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9))
    be = np.linspace(0, 6 * np.pi, 300)
    for mu, c in ((.1, GREEN), (.2, BLUE), (.3, ORANGE), (.5, RED)):
        a.semilogy(be / np.pi, np.exp(mu * be), color=c, lw=2.4, label="μ = %.1f" % mu)
    a.set_xlabel("wrap angle β (multiples of π: 1 = half turn, 2 = one turn)"); a.set_ylabel("T₂ / T₁ = e^{μβ}"); a.legend(fontsize=8.5); a.set_title("A few turns multiply the holding force enormously")
    a.plot([6], [np.exp(.3 * 6 * np.pi)], "o", color=RED); a.text(3.3, np.exp(.3 * 6 * np.pi) * .5, "3 turns, μ = 0.3:\n×286", fontsize=9, color=RED)
    th = np.linspace(0, 2 * np.pi, 200); b.axis("off"); b.set_aspect("equal"); b.set_xlim(-3, 3); b.set_ylim(-2.4, 2.4)
    b.add_patch(Circle((0, 0), 1, fc="#e2e8f0", ec="k", lw=2)); beta = np.radians(200); ang = np.linspace(np.radians(-10), np.radians(190), 60); b.plot(1.06 * np.cos(ang), 1.06 * np.sin(ang), color=PURPLE, lw=4)
    b.plot([1.06 * np.cos(np.radians(-10)), 1.06 * np.cos(np.radians(-10)) + 0.0], [1.06 * np.sin(np.radians(-10)), -2.2], color=BLUE, lw=2); b.plot([-1.06, -1.06], [0, -2.2], color=BLUE, lw=2)
    arr(b, (1.04, -1.6), (1.04, -2.3), RED, lw=2.4); b.text(1.2, -2.1, "T₁ (small hold)", color=RED, fontsize=9); arr(b, (-1.06, -1.1), (-1.06, -2.2), BLUE, lw=3.2); b.text(-2.9, -2.1, "T₂ (large load)", color=BLUE, fontsize=9)
    b.text(0, .1, "drum\nwrap β", ha="center", fontsize=9); b.set_title("Capstan: T₂ = T₁ e^{μβ} (impending slip)")
    save(fig, "belt-friction")
    print("belt: mu=0.3, beta=pi:", round(float(np.exp(.3 * np.pi)), 3), " 3 turns:", round(float(np.exp(.3 * 6 * np.pi)), 1), " holding force for 1000 N:", round(1000 / float(np.exp(.3 * 6 * np.pi)), 2), "N")


def virtual_work():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9)); th = np.linspace(-1.6, 1.6, 400); W_l2 = 1.0
    for k, c in ((0.5, RED), (1.0, GREEN), (2.0, BLUE)):
        V = .5 * k * th ** 2 + W_l2 * np.cos(th); b.plot(th, V, color=c, lw=2.4, label="k = %.1f × (W l/2)" % k)
    b.set_xlabel("θ (rad)"); b.set_ylabel("potential energy V (units of W l/2)"); b.set_ylim(-.1, 2.6); b.legend(fontsize=8.5); b.set_title("V(θ) = ½kθ² + (Wl/2) cos θ")
    a.axis("off"); a.set_xlim(0, 10); a.set_ylim(0, 8)
    lines = [r"Principle of virtual work:", r"$\delta W=\sum \mathbf{F}_i\cdot\delta\mathbf{r}_i=0$", "(for ideal, workless constraints)", "", r"Potential-energy form:", r"$dV/d\theta=0$ at equilibrium", r"$d^2V/d\theta^2>0$  stable   $<0$  unstable", "", r"Inverted rod with torsion spring $k$:", r"$V''(0)=k-\frac{Wl}{2}$"]
    for i, t in enumerate(lines):
        a.text(.2, 7.4 - .75 * i, t, fontsize=11 if t.startswith("$") else 10.5)
    save(fig, "virtual-work")


# ----------------------------------------------------------------------------- dynamics
def projectile():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9)); v = 30.0
    for ang, c in ((20, BLUE), (30, GREEN), (40, ORANGE), (45, RED), (60, PURPLE), (70, TEAL)):
        t = np.linspace(0, 2 * v * np.sin(np.radians(ang)) / g, 200); a.plot(v * np.cos(np.radians(ang)) * t, v * np.sin(np.radians(ang)) * t - g * t ** 2 / 2, color=c, lw=2.2, label="%d°" % ang)
    a.set_xlabel("x (m)"); a.set_ylabel("y (m)"); a.legend(fontsize=8, ncol=2, title="launch angle"); a.set_ylim(0, 50); a.set_title("v₀ = 30 m/s: 20° and 70° have equal range")
    ang = np.linspace(0, 90, 300); b.plot(ang, v ** 2 * np.sin(np.radians(2 * ang)) / g, color=BLUE, lw=2.6); b.plot([45], [v ** 2 / g], "o", color=RED); b.text(47, 88, "max range v²/g at 45° (no air)", fontsize=9, color=RED)
    b.set_xlabel("launch angle (degrees)"); b.set_ylabel("range (m)"); b.set_title("Range R = v₀² sin 2θ / g")
    save(fig, "projectile")
    th = np.radians(40); print("projectile 30 m/s at 40 deg: range", round(v ** 2 * np.sin(2 * th) / g, 2), " height", round((v * np.sin(th)) ** 2 / (2 * g), 2), " time", round(2 * v * np.sin(th) / g, 2), " | max range v^2/g =", round(v ** 2 / g, 2), " | a_n for 20 m/s on R=100 m:", 20 ** 2 / 100)


def energy_block():
    fig, ax = plt.subplots(figsize=(8.4, 3.9)); m, d, th, mu = 2.0, 3.0, np.radians(30), .2
    PE = m * g * d * np.sin(th); Wf = mu * m * g * np.cos(th) * d; KE = PE - Wf; v = np.sqrt(2 * KE / m)
    ax.bar(["PE lost\nm g d sin θ", "friction work\nμ m g cos θ · d", "KE gained\n½ m v²"], [PE, -Wf, KE], color=[BLUE, RED, GREEN]); ax.axhline(0, color="k", lw=1)
    for i, vv in enumerate([PE, -Wf, KE]):
        ax.text(i, vv + (1 if vv > 0 else -2.5), "%.2f J" % vv, ha="center", fontsize=10)
    ax.set_ylabel("energy (J)"); ax.set_title("2 kg block slides 3 m down a 30° incline, μ_k = 0.2: v = %.2f m/s" % v); ax.grid(axis="x", visible=False)
    save(fig, "energy-block")
    print("energy block: PE, Wf, KE, v =", round(PE, 3), round(Wf, 3), round(KE, 3), round(v, 3))


def bounce():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9)); e, h0 = 0.8, 2.0; t = [0.0]; hh = [h0]; y = []; tt = []
    T0 = np.sqrt(2 * h0 / g); tcur = 0; hcur = h0
    for n in range(8):
        T = np.sqrt(2 * hcur / g) * 2 if n else np.sqrt(2 * hcur / g)
        ts = np.linspace(0, T, 80)
        if n == 0:
            yy = hcur - g * ts ** 2 / 2
        else:
            yy = np.sqrt(2 * g * hcur) * ts - g * ts ** 2 / 2
        a.plot(tcur + ts, yy, color=BLUE, lw=2); tcur += T; hcur *= e ** 2
    a.set_xlabel("time (s)"); a.set_ylabel("height (m)"); a.set_title("Dropped from 2 m, e = 0.8: bounces shrink geometrically")
    n = np.arange(0, 9)
    for e_, c in ((.5, RED), (.8, BLUE), (.95, GREEN)):
        b.semilogy(n, h0 * e_ ** (2 * n), "o-", color=c, label="e = %.2f" % e_)
    b.set_xlabel("bounce number n"); b.set_ylabel("rebound height (m)"); b.legend(fontsize=8.5); b.set_title("hₙ = h₀ e²ⁿ")
    save(fig, "bounce")
    print("bounce: e=0.8: h1, h2 =", round(h0 * .64, 3), round(h0 * .64 ** 2, 3), " impact speed", round(float(np.sqrt(2 * g * h0)), 3), " rebound speed", round(.8 * float(np.sqrt(2 * g * h0)), 3), " energy lost 1-e^2 =", round(1 - .64, 2))


def rolling_wheel():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.1, 1]}); R = .3; v = 3.0; w = v / R
    a.set_aspect("equal"); a.axis("off"); a.set_xlim(-.6, 1.5); a.set_ylim(-.2, .8); th = np.linspace(0, 2 * np.pi, 200); a.plot(R * np.cos(th), R + R * np.sin(th), color="k", lw=2); a.plot([-.6, 1.5], [0, 0], color="k", lw=3)
    pts = {"C (centre)": (0, R, (v, 0), BLUE), "top T": (0, 2 * R, (2 * v, 0), GREEN), "contact IC": (0, 0, (0, 0), RED), "side P": (R, R, (v, -w * 0), ORANGE)}
    for name, (x, y, vel, c) in pts.items():
        a.plot(x, y, "o", color=c, ms=6)
    arr(a, (0, R), (v / 12, R), BLUE, lw=2.4); arr(a, (0, 2 * R), (2 * v / 12, 2 * R), GREEN, lw=2.4); a.text(.55, 2 * R - .02, "top: 2v = 6 m/s", color=GREEN, fontsize=9); a.text(.3, R + .11, "centre: v = 3 m/s", color=BLUE, fontsize=9)
    arr(a, (R, R), (R + v / 12, R - w * R / 12 * 1.0), ORANGE, lw=2.4); a.text(R + .24, R - .02, "side: √2 v", color=ORANGE, fontsize=9); a.text(.12, -.12, "contact point IC: v = 0 (instant centre)", color=RED, fontsize=9)
    a.set_title("Rolling without slipping: ground-frame velocities", fontsize=9.5)
    phi = np.linspace(0, 4 * np.pi, 400); x = R * (phi - np.sin(phi)); y = R * (1 - np.cos(phi)); b.plot(x, y, color=BLUE, lw=2.4); b.set_aspect("equal"); b.set_xlabel("x (m)"); b.set_ylabel("y (m)"); b.set_title("Path of a point on the rim: a cycloid (cusp at contact)")
    save(fig, "rolling-wheel")
    print("rolling: omega =", w, "rad/s; top speed", 2 * v, " side speed", round(np.hypot(v, w * R), 3), " cycloid arch length 8R =", 8 * R, "m")


def rolling_race():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9)); shapes = [("hoop / ring", 1.0, RED), ("solid cylinder", .5, BLUE), ("solid sphere", 2 / 5, GREEN), ("sliding block\n(no friction)", 0.0, GREY)]
    acc = [1 / (1 + k) for _, k, _ in shapes]
    a.bar([s[0] for s in shapes], acc, color=[s[2] for s in shapes]); a.set_ylabel("a / (g sin θ)")
    for i, v in enumerate(acc):
        a.text(i, v + .02, "%.3f" % v, ha="center", fontsize=9.5)
    a.set_ylim(0, 1.15); a.set_title("Acceleration down a slope: 1/(1 + k²/R²)"); a.grid(axis="x", visible=False)
    th = np.radians(30); t = np.linspace(0, 1.5, 100)
    for (n, k, c), aa in zip(shapes, acc):
        b.plot(t, .5 * aa * g * np.sin(th) * t ** 2, color=c, lw=2.6, label=n.replace("\n", " "))
    b.set_xlabel("time (s)"); b.set_ylabel("distance along the 30° slope (m)"); b.legend(fontsize=8.5); b.set_title("The race: sphere beats cylinder beats hoop")
    save(fig, "rolling-race")
    print("rolling race a/(g sin) hoop, cyl, sphere:", [round(x, 4) for x in acc[:3]], " cylinder at 30 deg: a =", round(acc[1] * g * np.sin(th), 3), " min mu cyl = tan(theta)/3 =", round(float(np.tan(th)) / 3, 4), " v at bottom h=1 m cyl: ", round(float(np.sqrt(4 * g * 1 / 3)), 3), " sphere:", round(float(np.sqrt(10 * g * 1 / 7)), 3), " hoop:", round(float(np.sqrt(g * 1)), 3), " block:", round(float(np.sqrt(2 * g * 1)), 3))


def inertia():
    fig, ax = plt.subplots(figsize=(10.4, 4.0)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 5)
    rows = [("thin rod, about centre", r"$\frac{1}{12}mL^2$", "k = 0.289 L"), ("thin rod, about end", r"$\frac{1}{3}mL^2$", "k = 0.577 L"), ("solid disk / cylinder, axis", r"$\frac{1}{2}mR^2$", "k = 0.707 R"), ("thin ring / hoop, axis", r"$mR^2$", "k = R"), ("solid sphere, diameter", r"$\frac{2}{5}mR^2$", "k = 0.632 R"), ("thin spherical shell", r"$\frac{2}{3}mR^2$", "k = 0.816 R")]
    ax.text(.2, 4.6, "body", fontsize=10.5, fontweight="bold"); ax.text(5.2, 4.6, "I (mass moment of inertia)", fontsize=10.5, fontweight="bold"); ax.text(9, 4.6, "radius of gyration", fontsize=10.5, fontweight="bold")
    for i, (n, f, k) in enumerate(rows):
        y = 3.8 - .62 * i; ax.text(.2, y, n, fontsize=10); ax.text(5.6, y, f, fontsize=12); ax.text(9, y, k, fontsize=10)
    ax.text(.2, .15, r"Parallel-axis theorem:  $I=I_G+md^2$      Radius of gyration:  $k=\sqrt{I/m}$      $I=\int r^2\,dm$", fontsize=10.5, color=PURPLE)
    save(fig, "inertia-table")
    print("inertia k/L, k/R:", round(float(np.sqrt(1 / 12)), 3), round(float(np.sqrt(1 / 3)), 3), round(float(np.sqrt(.5)), 3), round(float(np.sqrt(.4)), 3), round(float(np.sqrt(2 / 3)), 3))


if __name__ == "__main__":
    force_system(); moments_couples(); supports(); truss(); frame_fig(); distributed(); friction_law(); belt(); virtual_work()
    projectile(); energy_block(); bounce(); rolling_wheel(); rolling_race(); inertia()
