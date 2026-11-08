"""Foundations of mechanisms (ME 2201 lectures 1-5): numbers + figures for the four notes in this folder.
   python found_core.py  -> prints every quoted number, writes assets/FND-*.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Arc

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10})


# ------------------------------------------------------------------ mobility
def kutzbach(n, j, h=0, nr=0, jr=0, mr=0):
    """M = 3(n-nr-1) - 2(j-jr) - h - mr   (planar)"""
    return 3 * (n - nr - 1) - 2 * (j - jr) - h - mr


MOBILITY_CASES = {
    "four-bar 4R": dict(n=4, j=4, h=0),
    "slider-crank": dict(n=4, j=4, h=0),
    "cam + roller follower (formula)": dict(n=4, j=3, h=1),
    "cam + roller follower (effective)": dict(n=4, j=3, h=1, mr=1),
    "three-crank parallelogram (formula)": dict(n=5, j=6, h=0),
    "three-crank parallelogram (effective)": dict(n=5, j=6, h=0, nr=1, jr=2),
    "8-link, sliding joint (lecture 3)": dict(n=8, j=10, h=0),
    "7-link with a cam pair (lecture 3)": dict(n=7, j=7, h=1),
    "8-link, multiple joints (lecture 5)": dict(n=8, j=9, h=0),
}


# ------------------------------------------------------------------ four-bar geometry
def circle_intersect(p0, r0, p1, r1, branch=+1):
    d = np.hypot(*(np.array(p1) - np.array(p0)))
    if d > r0 + r1 or d < abs(r0 - r1) or d == 0:
        return None
    a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
    h = np.sqrt(max(r0 ** 2 - a ** 2, 0))
    ex = (np.array(p1) - np.array(p0)) / d
    ey = np.array([-ex[1], ex[0]])
    return np.array(p0) + a * ex + branch * h * ey


def fourbar_pose(g, b, c, d, th, branch=+1):
    """ground g along x (O2 at origin, O4 at (g,0)), crank b, coupler c, follower d"""
    A = b * np.array([np.cos(th), np.sin(th)])
    B = circle_intersect(A, c, (g, 0), d, branch)
    return A, B


def crank_full_rotation(g, b, c, d, n=3600):
    """True if the input link b can complete a full turn (brute-force assembly check over one revolution)."""
    ths = np.linspace(0, 2 * np.pi, n, endpoint=False)
    for th in ths:
        if fourbar_pose(g, b, c, d, th) is None or fourbar_pose(g, b, c, d, th)[1] is None:
            return False
    return True


def grashof(links):
    s, p, q, l = sorted(links)
    return s + l - (p + q)           # <0 Grashof, 0 change point, >0 non-Grashof


def verify_grashof(trials=600, seed=1):
    """For random link sets: s+l<p+q  <=>  the shortest link can fully rotate relative to its neighbours (checked by assembly)."""
    rng = np.random.default_rng(seed)
    agree = bad = 0
    for _ in range(trials):
        L = rng.uniform(1, 10, 4)
        if abs(grashof(L)) < 0.05:
            continue
        i = int(np.argmin(L))
        # make the shortest link the crank (input) with ground = its neighbour; the other three are g, c, d in cyclic order
        order = [L[(i + k) % 4] for k in range(4)]            # crank, coupler-side neighbour, opposite, ground-side neighbour
        b, c_, opp, g_ = order[0], order[1], order[2], order[3]
        # chain crank b -- coupler c_ -- follower opp -- ground g_ -- back to crank
        ok = crank_full_rotation(g_, b, c_, opp, n=720)
        pred = grashof(L) < 0
        if ok == pred:
            agree += 1
        else:
            bad += 1
    return agree, bad


def classify(g, b, c, d):
    """name of the mechanism with ground g, input b, coupler c, output d"""
    L = [g, b, c, d]
    s = min(L)
    G = grashof(L)
    if G > 1e-9:
        return "triple rocker (non-Grashof)"
    if abs(G) <= 1e-9:
        return "change point"
    if g == s:
        return "drag link (double crank)"
    if c == s:
        return "double rocker"
    return "crank-rocker"


# ------------------------------------------------------------------ slider-crank
def slider_x(r, l, e, th):
    return r * np.cos(th) + np.sqrt(l ** 2 - (r * np.sin(th) - e) ** 2)


def offset_quick_return(r, l, e):
    a = np.degrees(np.arcsin(e / (l - r)) - np.arcsin(e / (l + r)))
    return (180 + a) / (180 - a), a


def whitworth_ratio(r_over_d):
    beta = np.degrees(np.arccos(r_over_d))
    return (180 - beta) / beta, beta


# ------------------------------------------------------------------ figures
def hatch(ax, x0, x1, y, down=True, n=7, L=0.18):
    ax.plot([x0, x1], [y, y], color="k", lw=2)
    for xx in np.linspace(x0, x1, n):
        ax.plot([xx, xx - L * .6], [y, y - L if down else y + L], color="k", lw=1)


def pin(ax, p, ground=False):
    ax.add_patch(Circle(p, 0.07, fc="white", ec="k", lw=1.6, zorder=6))
    if ground:
        hatch(ax, p[0] - .2, p[0] + .2, p[1] - .12, n=4, L=.12)


def link(ax, p, q, col=BLUE, lw=3.5):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=col, lw=lw, solid_capstyle="round", zorder=4)


def fig_pairs():
    fig, axs = plt.subplots(2, 4, figsize=(11.5, 5.4))
    for a in axs.ravel():
        a.set_aspect("equal"); a.axis("off"); a.set_xlim(-1.6, 1.6); a.set_ylim(-1.5, 1.4)
    def title(a, t, d, k):
        a.set_title(t, fontsize=10, weight="bold", color=BLUE if k == "lower" else ORANGE)
        a.text(0, -1.45, d, ha="center", fontsize=8.5, color=GREY)
    # revolute
    a = axs[0, 0]; a.add_patch(Rectangle((-1.2, -0.6), 2.4, .35, fc="#e2e8f0", ec="k")); link(a, (0, -.1), (1.1, .9)); a.add_patch(Circle((0, -.1), .18, fc="white", ec="k", lw=2)); a.plot(0, -.1, "k.", ms=4)
    a.add_patch(Arc((0, -.1), 1.1, 1.1, theta1=40, theta2=140, color=RED, lw=2)); title(a, "Revolute R · 1 DOF", "rotation about one axis", "lower")
    # prismatic
    a = axs[0, 1]; a.add_patch(Rectangle((-1.3, -.55), 2.6, .12, fc="k")); a.add_patch(Rectangle((-1.3, .15), 2.6, .12, fc="k")); a.add_patch(Rectangle((-.4, -.43), .8, .58, fc=BLUE, alpha=.8, ec="k"))
    a.annotate("", (1.1, -.1), (.45, -.1), arrowprops=dict(arrowstyle="<->", color=RED, lw=2)); title(a, "Prismatic P · 1 DOF", "translation along one line", "lower")
    # helical
    a = axs[0, 2]; a.add_patch(Rectangle((-.35, -1), .7, 2.0, fc="#cbd5e0", ec="k"))
    for y in np.linspace(-.8, .8, 8):
        a.plot([-.35, .35], [y, y + .18], color="k", lw=1)
    a.annotate("", (1.2, .5), (.5, .5), arrowprops=dict(arrowstyle="<->", color=RED, lw=2)); a.add_patch(Arc((-.9, 0), .8, .8, theta1=30, theta2=330, color=RED, lw=2)); title(a, "Helical H · 1 DOF", "rotation and translation tied by the lead", "lower")
    # cylindrical
    a = axs[0, 3]; a.add_patch(Rectangle((-.35, -1), .7, 2.0, fc="#cbd5e0", ec="k"))
    a.annotate("", (1.2, .5), (.5, .5), arrowprops=dict(arrowstyle="<->", color=RED, lw=2)); a.add_patch(Arc((-.9, 0), .8, .8, theta1=30, theta2=330, color=RED, lw=2)); title(a, "Cylindrical C · 2 DOF", "rotation and translation independent", "lower")
    # spherical
    a = axs[1, 0]; a.add_patch(Circle((0, 0), .55, fc=BLUE, alpha=.6, ec="k")); a.add_patch(Arc((0, 0), 1.5, 1.5, theta1=180, theta2=360, color="k", lw=3)); link(a, (0, .1), (.7, 1.0))
    for ang in (0, 60, 120): a.add_patch(Arc((0, 0), 1.9 + ang / 200, 1.9 + ang / 200, theta1=ang, theta2=ang + 40, color=RED, lw=2))
    title(a, "Spherical S · 3 DOF", "three rotations about one point", "lower")
    # planar
    a = axs[1, 1]; a.add_patch(Rectangle((-1.3, -.7), 2.6, .12, fc="k")); a.add_patch(Rectangle((-.6, -.5), 1.2, .3, fc=BLUE, alpha=.8, ec="k"))
    a.annotate("", (1.2, -.3), (.7, -.3), arrowprops=dict(arrowstyle="<->", color=RED, lw=2)); a.annotate("", (0, .5), (0, 0), arrowprops=dict(arrowstyle="<->", color=RED, lw=2)); a.add_patch(Arc((0, -.35), 1.4, 1.2, theta1=30, theta2=150, color=RED, lw=2)); title(a, "Planar E · 3 DOF", "two translations and a rotation", "lower")
    # cam-follower
    a = axs[1, 2]; t = np.linspace(0, 2 * np.pi, 200); a.plot(.8 * np.cos(t) + .15 * np.cos(2 * t), .7 * np.sin(t) - .4, color=BLUE, lw=3)
    a.plot([-.5, .5], [.42, .42], color=ORANGE, lw=4); a.plot([0, 0], [.42, 1.2], color=ORANGE, lw=4); title(a, "Cam-follower · higher pair", "line or point contact: rolling + sliding", "higher")
    # gears
    a = axs[1, 3]
    for cx, col in ((-.55, BLUE), (.55, ORANGE)):
        a.add_patch(Circle((cx, 0), .5, fc="none", ec=col, lw=3))
        for k in range(12):
            th = k * np.pi / 6; a.plot([cx + .5 * np.cos(th), cx + .62 * np.cos(th)], [.5 * np.sin(th), .62 * np.sin(th)], color=col, lw=2.5)
    title(a, "Gear teeth · higher pair", "line contact: rolling + sliding", "higher")
    fig.suptitle("Kinematic pairs: lower pairs have surface contact, higher pairs line or point contact (blue = lower, orange = higher)", fontsize=10.5)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-1-pairs.png"), dpi=150); plt.close(fig)


def fig_mobility():
    fig, axs = plt.subplots(1, 4, figsize=(13, 3.9))
    for a in axs:
        a.set_aspect("equal"); a.axis("off"); a.set_xlim(-.5, 4.2); a.set_ylim(-.9, 2.4)
    # 4R
    a = axs[0]; O2, A, B, O4 = (0, 0), (.6, 1.2), (3.0, 1.5), (3.6, 0)
    for p, q in ((O2, A), (A, B), (B, O4)): link(a, p, q)
    hatch(a, -.3, 3.9, -.14, n=14); [pin(a, p) for p in (O2, A, B, O4)]
    a.set_title("four-bar 4R\nn=4, j=4  →  M=1", fontsize=10, weight="bold")
    # slider-crank
    a = axs[1]; O2, A, B = (0, 0), (.7, 1.0), (3.2, 0.05)
    link(a, O2, A); link(a, A, B); a.add_patch(Rectangle((2.95, -.12), .5, .3, fc=ORANGE, ec="k", zorder=5)); hatch(a, -.3, 4, -.2, n=14); [pin(a, p) for p in (O2, A, B)]
    a.set_title("slider-crank\nn=4, j=4 (3R + 1P)  →  M=1", fontsize=10, weight="bold")
    # cam + roller follower
    a = axs[2]; t = np.linspace(0, 2 * np.pi, 200)
    a.fill(1 + .75 * np.cos(t) + .12 * np.cos(2 * t), .5 + .55 * np.sin(t), color="#cbd5e0", ec="k", lw=2); pin(a, (1, .5), ground=True)
    rc = (1.8, 1.2); a.add_patch(Circle(rc, .22, fc="#fed7aa", ec="k", lw=2, zorder=5)); link(a, rc, (3.6, 1.7), col=ORANGE); pin(a, (3.6, 1.7), ground=True); pin(a, rc)
    a.set_title("cam + roller follower\nn=4, j=3, h=1  →  M=2 (roller spin is idle)", fontsize=9.5, weight="bold"); a.text(1.9, -.55, "effective M = 2 − 1 = 1", ha="center", color=RED, fontsize=9.5)
    a.set_ylim(-.9, 2.4)
    # parallelogram
    a = axs[3]
    for x in (0.4, 1.8, 3.2):
        link(a, (x, 0), (x + .8, 1.3), col=BLUE); pin(a, (x, 0), ground=True)
    link(a, (1.2, 1.3), (4.0, 1.3), col=ORANGE); [pin(a, (x + .8, 1.3)) for x in (.4, 1.8, 3.2)]
    hatch(a, 0, 3.6, -.14, n=12)
    a.set_title("three equal cranks + coupler\nn=5, j=6  →  formula M=0, really M=1", fontsize=9.5, weight="bold"); a.text(1.9, -.55, "one crank is redundant: Mₑ = 3(5−1−1) − 2(6−2) = 1", ha="center", color=RED, fontsize=8.5)
    fig.suptitle("Kutzbach counts: n links, j full joints, h half joints", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-2-mobility.png"), dpi=150); plt.close(fig)


def first_valid(g, b, c, d, prefs=(55, 25, 110, 80, 140, 170, 200, 250, 300, 330)):
    for t in prefs:
        if fourbar_pose(g, b, c, d, np.radians(t))[1] is not None:
            return np.radians(t)
    raise ValueError("no assembling pose found")


def draw_fourbar(a, g, b, c, d, th, ground_link, title, col_ground=GREY, branch=+1):
    A, B = fourbar_pose(g, b, c, d, th, branch)
    O2, O4 = np.array([0, 0.0]), np.array([g, 0.0])
    link(a, O2, O4, col=col_ground, lw=3)
    link(a, O2, A, col=BLUE); link(a, A, B, col=GREEN); link(a, B, O4, col=ORANGE)
    for p in (O2, O4): pin(a, p, ground=False)
    pin(a, A); pin(a, B)
    a.set_title(title, fontsize=9.5, weight="bold")


def fig_inversions():
    # fixed lengths s=2, p=4, q=4.5, l=5 ; s+l=7 < p+q=8.5  (Grashof)
    lens = dict(s=2.0, p=4.0, q=4.5, l=5.0)
    loop = [lens["s"], lens["p"], lens["l"], lens["q"]]          # cyclic order around the loop: s, p, l, q
    fig, axs = plt.subplots(1, 4, figsize=(13.5, 3.9))
    # (ground index in loop, name)
    cases = [(3, "ground = q (next to s)\ncrank-rocker"), (0, "ground = s (shortest)\ndrag link (double crank)"), (1, "ground = p (next to s)\ncrank-rocker"), (2, "ground = l (opposite s)\ndouble rocker")]
    names = ["s", "p", "l", "q"]
    for a, (gi, tt) in zip(axs, cases):
        a.set_aspect("equal"); a.axis("off"); a.set_xlim(-3.2, 7.5); a.set_ylim(-4.6, 5.4)
        ln = [loop[(gi + k) % 4] for k in range(4)]        # ground, link adjacent (input), coupler, output
        g, b, c, d = ln
        th = first_valid(g, b, c, d)
        draw_fourbar(a, g, b, c, d, th, 0, tt)
        hatch(a, -.4, g + .4, -.18, n=12)
        a.text(g / 2, -.9, "fixed link %s = %.1f" % (names[gi], g), ha="center", fontsize=8.5, color=GREY)
    fig.suptitle("One chain (s=2, p=4, q=4.5, l=5; s+l=7 < p+q=8.5), four mechanisms: fixing a different link", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-3-inversions-4R.png"), dpi=150); plt.close(fig)
    return lens


def fig_grashof_map():
    l, s = 1.0, 0.3
    p = np.linspace(s, l, 300); q = np.linspace(s, l, 300)
    P, Q = np.meshgrid(p, q)
    G = s + l - (P + Q)
    fig, ax = plt.subplots(figsize=(6.6, 5.2))
    ax.contourf(P, Q, G <= 0, levels=[-.5, .5, 1.5], colors=["#fed7d7", "#c6f6d5"], alpha=.9)
    ax.plot(p, s + l - p, color="k", lw=2)
    ax.text(.82, .78, "Grashof\ns + l < p + q", color=GREEN, ha="center", fontsize=11, weight="bold")
    ax.text(.42, .42, "non-Grashof\ntriple rockers", color=RED, ha="center", fontsize=11, weight="bold")
    ax.text(.6, .73, "change points on the line", fontsize=8.5, rotation=-45, color="k")
    ax.set_xlim(s, l); ax.set_ylim(s, l); ax.set_xlabel("p / l"); ax.set_ylabel("q / l")
    ax.set_title("Four-bar link-length map for s = 0.3 l: only the sum of the two middle links matters", fontsize=9.5)
    ax.set_aspect("equal")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-4-grashof-map.png"), dpi=150); plt.close(fig)


def fig_slider():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.3))
    th = np.linspace(0, 2 * np.pi, 400)
    r = 1.0
    for l, col in ((2, RED), (3, ORANGE), (5, BLUE)):
        a1.plot(np.degrees(th), slider_x(r, l, 0, th) - l, color=col, lw=2.2, label="l/r = %d" % l)
    a1.plot(np.degrees(th), slider_x(r, 3, .8, th) - np.sqrt(3 ** 2 - .8 ** 2), color=PURPLE, lw=2, ls="--", label="l/r = 3, offset e = 0.8 r")
    a1.set_xlabel("crank angle θ (deg)"); a1.set_ylabel("slider position from the far dead centre (units of r)"); a1.set_xticks(range(0, 361, 90)); a1.grid(alpha=.25)
    a1.legend(fontsize=8); a1.set_title("slider position: stroke = 2r inline; shorter rod means a more lopsided curve", fontsize=9.5)
    rd = np.linspace(.05, .95, 200)
    a2.plot(rd, [whitworth_ratio(x)[0] for x in rd], color=BLUE, lw=2.4, label="Whitworth (crank-slotted lever)")
    for l, col in ((4, RED), (6, ORANGE)):
        es = np.linspace(0, 0.9 * (l - 1), 100)
        a2.plot(es / (l - 1), [offset_quick_return(1, l, e)[0] for e in es], color=col, lw=1.8, label="offset slider-crank, l/r = %d (x = e/(l−r))" % l)
    a2.axhline(1, color="k", lw=.8); a2.set_ylim(.9, 4); a2.set_xlim(0, 1); a2.set_xlabel("r/d (Whitworth) or e/(l−r) (offset slider-crank)"); a2.set_ylabel("quick-return ratio (slow stroke / fast stroke)")
    a2.grid(alpha=.25); a2.legend(fontsize=8); a2.set_title("quick return needs geometry that makes the crank sweep unequal angles", fontsize=9.5)
    fig.suptitle("The 3R-1P chain: slider-crank and its inversions", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-5-slider-crank.png"), dpi=150); plt.close(fig)


def fig_double_slider():
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.3))
    # elliptic trammel: bar of length a+b, tracing point P at distance a from the slider on the y axis (slot) ... P = (a cos f, b sin f)
    a_, b_ = 3.0, 1.8
    ax = axs[0]; ax.set_aspect("equal"); ax.set_xlim(-4.2, 4.2); ax.set_ylim(-3.2, 3.2); ax.grid(alpha=.2)
    ax.axhline(0, color="k", lw=1.2); ax.axvline(0, color="k", lw=1.2)
    f = np.linspace(0, 2 * np.pi, 300); ax.plot(a_ * np.cos(f), b_ * np.sin(f), color=PURPLE, lw=2, label="path of P: ellipse")
    for ph, col in ((35, BLUE), (110, GREEN), (200, ORANGE)):
        # bar of length L = a + b: one slider on the x slot at (L cos t, 0), the other on the y slot at (0, L sin t);
        # P lies a from the y-slot slider and b from the x-slot slider, so P = (a cos t, b sin t)
        t = np.radians(ph); L = a_ + b_
        Sx_, Ty_ = L * np.cos(t), L * np.sin(t)
        Pp = (Sx_ * (1 - b_ / L) * 1.0 + 0 * b_, Ty_ * (b_ / L))
        ax.plot([Sx_, 0], [0, Ty_], color=col, lw=3); ax.plot([Sx_, 0], [0, Ty_], "o", color="k", ms=4); ax.plot(*Pp, "o", color=RED, ms=7)
    ax.legend(fontsize=8, loc="lower left"); ax.set_title("elliptic trammel (P-R-R-P)\nP traces an ellipse, semi-axes a and b", fontsize=9.5)
    # scotch yoke vs slider crank
    ax = axs[1]; th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.degrees(th), np.cos(th), color=BLUE, lw=2.4, label="Scotch yoke: x = r cos θ (pure harmonic)")
    ax.plot(np.degrees(th), slider_x(1, 3, 0, th) - 3, color=RED, lw=2, ls="--", label="slider-crank l/r = 3 (shifted)")
    ax.set_xlabel("crank angle θ (deg)"); ax.set_ylabel("position (units of r)"); ax.set_xticks(range(0, 361, 90)); ax.grid(alpha=.25); ax.legend(fontsize=8)
    ax.set_title("Scotch yoke: exact sine, no rod-obliquity distortion", fontsize=9.5)
    # Oldham: Thales circle
    ax = axs[2]; ax.set_aspect("equal"); ax.set_xlim(-1.6, 2.6); ax.set_ylim(-1.7, 1.7); ax.grid(alpha=.2)
    e = 1.0; O2 = np.array([0.0, 0.0]); O4 = np.array([e, 0.0])
    f = np.linspace(0, 2 * np.pi, 300); ax.plot(e / 2 + e / 2 * np.cos(f), e / 2 * np.sin(f), color=PURPLE, lw=2, label="locus of the disc centre")
    for ph, col in ((25, BLUE), (70, GREEN), (115, ORANGE)):
        t = np.radians(ph); d2 = np.array([np.cos(t), np.sin(t)]); C = O2 + e * np.cos(t) * d2     # foot of perpendicular from O4 onto the line through O2
        ax.plot([-.9 * d2[0], 1.3 * d2[0]], [-.9 * d2[1], 1.3 * d2[1]], color=col, lw=1.5)
        n2 = np.array([-np.sin(t), np.cos(t)]); ax.plot([O4[0] - 1.1 * n2[0], O4[0] + 1.1 * n2[0]], [O4[1] - 1.1 * n2[1], O4[1] + 1.1 * n2[1]], color=col, lw=1.5, ls="--")
        ax.plot(*C, "o", color=RED, ms=6)
    ax.plot(*O2, "ks"); ax.plot(*O4, "ks"); ax.text(-.1, -.25, "O₂"); ax.text(e + .03, -.25, "O₄")
    ax.legend(fontsize=8, loc="lower right"); ax.set_title("Oldham coupling: slots cross on the\ncircle of diameter O₂O₄ (2 laps per turn)", fontsize=9.5)
    fig.suptitle("The double-slider chain (two R + two P): three inversions", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-7-double-slider.png"), dpi=150); plt.close(fig)


def fig_trace():
    """coupler midpoint path of a crank-rocker and the unreachable gap of a triple rocker"""
    fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.2))
    for a, (g, b, c, d, tt) in zip(axs, ((4.5, 2.0, 5.0, 4.0, "Grashof: crank can turn 360°"), (4.5, 3.5, 5.0, 4.0, "change point: s + l = p + q"), (4.5, 3.8, 5.0, 4.0, "non-Grashof: crank is limited"))):
        a.set_aspect("equal"); a.set_xlim(-6.5, 10); a.set_ylim(-6.5, 7.5); a.grid(alpha=.2)
        trace = []; ok = []
        for th in np.linspace(0, 2 * np.pi, 400):
            A, B = fourbar_pose(g, b, c, d, th)
            if B is None:
                continue
            trace.append((A + B) / 2); ok.append(th)
        trace = np.array(trace)
        if len(trace):
            a.plot(trace[:, 0], trace[:, 1], color=PURPLE, lw=1.6, label="coupler midpoint path")
        th0 = np.radians(40)
        A, B = fourbar_pose(g, b, c, d, th0)
        if B is None:
            th0 = ok[len(ok) // 2]; A, B = fourbar_pose(g, b, c, d, th0)
        draw_fourbar(a, g, b, c, d, th0, 0, "")
        full = crank_full_rotation(g, b, c, d)
        a.set_title("%s\nlinks g=%.1f, crank=%.1f, coupler=%.1f, follower=%.1f\ncrank turns fully: %s   (s+l−(p+q) = %+.1f)" % (tt, g, b, c, d, "YES" if full else "NO", grashof([g, b, c, d])), fontsize=8.5)
        if len(trace):
            a.legend(fontsize=7.5, loc="lower right")
    fig.suptitle("Same ground and coupler, growing crank: the path closes only while s + l < p + q", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "FND-6-grashof-sweep.png"), dpi=150); plt.close(fig)


if __name__ == "__main__":
    print("--- mobility")
    for k, v in MOBILITY_CASES.items():
        print(f"  {k:42s} {v}  M = {kutzbach(**v)}")
    print("  constrained chains (M=1): 3n = 2j + 4 ->", [(n, (3 * n - 4) // 2) for n in (4, 6, 8)])
    lens = {}
    print("--- Grashof brute-force check (random link sets, crank = shortest link):", verify_grashof())
    cases = [(4.5, 2.0, 5.0, 4.0), (4.5, 3.5, 5.0, 4.0), (4.5, 3.8, 5.0, 4.0)]
    for c in cases:
        print("  ", c, "grashof", grashof(list(c)), "crank full turn:", crank_full_rotation(*c))
    print("--- inversions of s=2,p=4,l=5,q=4.5:")
    loop = [2.0, 4.0, 5.0, 4.5]
    for gi, nm in enumerate("spl q".replace(" ", "")):
        pass
    for gi, nm in zip(range(4), ["s", "p", "l", "q"]):
        g, b, c, d = [loop[(gi + k) % 4] for k in range(4)]
        print(f"   ground={nm}: (g,b,c,d)=({g},{b},{c},{d})  ->", classify(g, b, c, d))
    print("--- slider-crank")
    print("   offset QR (r=1,l=4,e=1):", offset_quick_return(1, 4, 1.0))
    print("   offset QR (r=1,l=4,e=2.5):", offset_quick_return(1, 4, 2.5))
    print("   inline stroke (r=1):", slider_x(1, 3, 0, 0) - slider_x(1, 3, 0, np.pi))
    print("   Whitworth r/d=0.5:", whitworth_ratio(.5), " r/d=0.3:", whitworth_ratio(.3), " r/d=0.8:", whitworth_ratio(.8))
    fig_pairs(); fig_mobility(); fig_inversions(); fig_grashof_map(); fig_slider(); fig_trace(); fig_double_slider()
