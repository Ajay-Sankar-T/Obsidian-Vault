"""Tiny schematic helpers (matplotlib) shared by the EE1100 figure scripts.
Every element is drawn *between two points* on a straight line, so layouts are just coordinates.
side=+1 puts the label above a horizontal element / to the right of a vertical one; side=-1 the opposite."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

LW = 1.7
BLUE, ORANGE, RED, GREEN, GREY = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a", "#777777"


def wire(ax, *pts, c="k", lw=LW):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=c, lw=lw, solid_capstyle="round", zorder=1)


def dot(ax, x, y, c="k"):
    ax.plot([x], [y], "o", color=c, ms=4, zorder=3)


def node(ax, x, y, name=None, dx=0.0, dy=0.25, c="k"):
    ax.plot([x], [y], "o", mfc="w", mec=c, ms=5, zorder=3)
    if name:
        ax.text(x + dx, y + dy, name, ha="center", va="bottom", fontsize=9, color=c)


def _frame(p1, p2):
    x1, y1 = p1; x2, y2 = p2
    L = float(np.hypot(x2 - x1, y2 - y1))
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return L, ux, uy, -uy, ux


def _lab(ax, p1, p2, txt, side, off, **kw):
    if not txt:
        return
    xm, ym = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    L, ux, uy, px, py = _frame(p1, p2)
    if abs(px) > 0.7:      # vertical element: put the label beside it, anchored away from the body
        ha = "left" if px * side > 0 else "right"
        ax.text(xm + px * side * (off * 0.75), ym, txt, ha=ha, va="center", fontsize=9, **kw)
    else:
        ax.text(xm + px * off * side, ym + py * off * side, txt, ha="center", va="center", fontsize=9, **kw)


def _lead(ax, p1, p2, body):
    """draw the two leads, return the body start/end points"""
    L, ux, uy, px, py = _frame(p1, p2)
    a = (L - body) / 2
    s = (p1[0] + ux * a, p1[1] + uy * a)
    e = (p1[0] + ux * (a + body), p1[1] + uy * (a + body))
    wire(ax, p1, s); wire(ax, e, p2)
    return s, e, ux, uy, px, py


def res(ax, p1, p2, lab="", side=1, n=6, body=1.2, w=0.17):
    s, e, ux, uy, px, py = _lead(ax, p1, p2, body)
    pts = [s]
    for k in range(n):
        t = (k + 0.5) / n
        sg = w * (1 if k % 2 == 0 else -1)
        pts.append((s[0] + (e[0] - s[0]) * t + px * sg, s[1] + (e[1] - s[1]) * t + py * sg))
    pts.append(e)
    wire(ax, *pts)
    _lab(ax, p1, p2, lab, side, 0.42)


def ind(ax, p1, p2, lab="", side=1, n=4, body=1.2):
    s, e, ux, uy, px, py = _lead(ax, p1, p2, body)
    r = body / (2 * n)
    th = np.linspace(np.pi, 0, 24)
    for k in range(n):
        cx = s[0] + ux * (r + 2 * r * k); cy = s[1] + uy * (r + 2 * r * k)
        xs = cx + r * np.cos(th) * ux + r * np.sin(th) * px * 1.0
        ys = cy + r * np.cos(th) * uy + r * np.sin(th) * py * 1.0
        ax.plot(xs, ys, color="k", lw=LW, zorder=1)
    _lab(ax, p1, p2, lab, side, 0.42)


def cap(ax, p1, p2, lab="", side=1, gap=0.22, plate=0.38):
    L, ux, uy, px, py = _frame(p1, p2)
    c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    a = (c[0] - ux * gap / 2, c[1] - uy * gap / 2); b = (c[0] + ux * gap / 2, c[1] + uy * gap / 2)
    wire(ax, p1, a); wire(ax, b, p2)
    for q in (a, b):
        wire(ax, (q[0] - px * plate, q[1] - py * plate), (q[0] + px * plate, q[1] + py * plate), lw=2.2)
    _lab(ax, p1, p2, lab, side, 0.5)


def battery(ax, p1, p2, lab="", plus=2, side=1):
    """DC source drawn as long (+) and short (-) plates; plus=1 puts + at p1, plus=2 at p2"""
    L, ux, uy, px, py = _frame(p1, p2)
    c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    d = 0.14
    pl = (c[0] + ux * d * (1 if plus == 2 else -1), c[1] + uy * d * (1 if plus == 2 else -1))
    mi = (c[0] - ux * d * (1 if plus == 2 else -1), c[1] - uy * d * (1 if plus == 2 else -1))
    first, second = (mi, pl) if plus == 2 else (pl, mi)
    wire(ax, p1, first); wire(ax, second, p2)
    wire(ax, (pl[0] - px * 0.42, pl[1] - py * 0.42), (pl[0] + px * 0.42, pl[1] + py * 0.42), lw=2.2)
    wire(ax, (mi[0] - px * 0.22, mi[1] - py * 0.22), (mi[0] + px * 0.22, mi[1] + py * 0.22), lw=3.6)
    _lab(ax, p1, p2, lab, side, 0.62)


def vsrc(ax, p1, p2, lab="", plus=2, side=1, r=0.4, dep=False, ac=False):
    """circular voltage source; dep=True draws a diamond (dependent source); ac=True a sine"""
    L, ux, uy, px, py = _frame(p1, p2)
    c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    s = (c[0] - ux * r, c[1] - uy * r); e = (c[0] + ux * r, c[1] + uy * r)
    wire(ax, p1, s); wire(ax, e, p2)
    if dep:
        ax.plot([c[0] - ux * r, c[0] + px * r, c[0] + ux * r, c[0] - px * r, c[0] - ux * r],
                [c[1] - uy * r, c[1] + py * r, c[1] + uy * r, c[1] - py * r, c[1] - uy * r], color="k", lw=LW, zorder=2)
    else:
        ax.add_patch(Circle(c, r, fill=True, fc="w", ec="k", lw=LW, zorder=2))
    if ac:
        t = np.linspace(-1, 1, 40) * r * 0.65
        ax.plot(c[0] + ux * t + px * 0.17 * np.sin(t / (r * 0.65) * np.pi), c[1] + uy * t + py * 0.17 * np.sin(t / (r * 0.65) * np.pi), "k", lw=1.2, zorder=3)
    else:
        sg = 1 if plus == 2 else -1
        ax.text(c[0] + ux * r * 0.52 * sg, c[1] + uy * r * 0.52 * sg, "+", ha="center", va="center", fontsize=8, zorder=4)
        ax.text(c[0] - ux * r * 0.52 * sg, c[1] - uy * r * 0.52 * sg, "−", ha="center", va="center", fontsize=8, zorder=4)
    _lab(ax, p1, p2, lab, side, 0.72)


def isrc(ax, p1, p2, lab="", side=1, r=0.4, dep=False):
    """current source; the arrow points from p1 towards p2 (direction of the source current)"""
    L, ux, uy, px, py = _frame(p1, p2)
    c = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    s = (c[0] - ux * r, c[1] - uy * r); e = (c[0] + ux * r, c[1] + uy * r)
    wire(ax, p1, s); wire(ax, e, p2)
    if dep:
        ax.plot([c[0] - ux * r, c[0] + px * r, c[0] + ux * r, c[0] - px * r, c[0] - ux * r],
                [c[1] - uy * r, c[1] + py * r, c[1] + uy * r, c[1] - py * r, c[1] - uy * r], color="k", lw=LW, zorder=2)
    else:
        ax.add_patch(Circle(c, r, fill=True, fc="w", ec="k", lw=LW, zorder=2))
    ax.add_patch(FancyArrowPatch((c[0] - ux * r * 0.6, c[1] - uy * r * 0.6), (c[0] + ux * r * 0.6, c[1] + uy * r * 0.6),
                                 arrowstyle="-|>", mutation_scale=11, lw=1.6, color="k", zorder=4))
    _lab(ax, p1, p2, lab, side, 0.72)


def arrow(ax, p, q, txt="", c=BLUE, off=0.22, side=1, fs=9):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=11, lw=1.5, color=c, zorder=5))
    if txt:
        L, ux, uy, px, py = _frame(p, q)
        ax.text((p[0] + q[0]) / 2 + px * off * side, (p[1] + q[1]) / 2 + py * off * side, txt, color=c, ha="center", va="center", fontsize=fs)


def gnd(ax, x, y):
    wire(ax, (x, y), (x, y - 0.22))
    for k, w in enumerate((0.3, 0.2, 0.1)):
        wire(ax, (x - w, y - 0.22 - 0.09 * k), (x + w, y - 0.22 - 0.09 * k))


def finish(ax, xl, yl, title=None):
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect("equal"); ax.axis("off")
    if title:
        ax.set_title(title, fontsize=10)


def save(fig, path, dpi=150):
    fig.tight_layout()
    fig.savefig(path, dpi=dpi)
    plt.close(fig)
