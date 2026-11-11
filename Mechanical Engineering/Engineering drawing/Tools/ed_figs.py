"""ME1480 Engineering Drawing figures. Output: ../assets/ED-*.png"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets")); os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, GREEN, RED, PURPLE, GREY = "#2b6cb0", "#dd6b20", "#2f855a", "#c53030", "#6b46c1", "#718096"
plt.rcParams.update({"figure.dpi": 150, "font.size": 10, "axes.grid": False})


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, "ED-%s.png" % name), bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote ED-%s.png" % name)


def dim_h(ax, x0, x1, y, text, off=0, fs=8):
    ax.annotate("", xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle="<|-|>", color="k", lw=.8, mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text((x0 + x1) / 2, y + 1.2 + off, text, ha="center", fontsize=fs)


def dim_v(ax, x, y0, y1, text, fs=8, side=1):
    ax.annotate("", xy=(x, y0), xytext=(x, y1), arrowprops=dict(arrowstyle="<|-|>", color="k", lw=.8, mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text(x + side * 1.6, (y0 + y1) / 2, text, va="center", ha="left" if side > 0 else "right", fontsize=fs)


def a_series():
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    sizes = [("A0", 841, 1189), ("A1", 594, 841), ("A2", 420, 594), ("A3", 297, 420), ("A4", 210, 297), ("A5", 148, 210)]
    cols = [BLUE, GREEN, ORANGE, PURPLE, RED, GREY]
    for (n, w, l), c in zip(sizes, cols):
        ax.add_patch(Rectangle((0, 0), l, w, fill=False, ec=c, lw=2.4))
        ax.text(l - 8, w - 14, "%s  %d × %d" % (n, l, w), ha="right", va="top", color=c, fontsize=9, fontweight="bold")
    ax.plot([0, 1189], [0, 841], color="k", lw=.8, ls=":"); ax.text(560, 330, "all share the diagonal: ratio length : width = √2 : 1", rotation=35, fontsize=9)
    ax.set_xlim(-30, 1230); ax.set_ylim(-30, 880); ax.set_aspect("equal"); ax.set_xlabel("mm"); ax.set_title("A-series sheets: fold in half along the long side and you get the next size")
    save(fig, "a-series")
    print("A-series: ratio 1189/841 =", round(1189 / 841, 4), "sqrt2 =", round(2 ** .5, 4), " A0 area m2 =", round(1.189 * .841, 4), " A4 area m2 =", round(.297 * .210, 5))


def sheet_layout():
    fig, ax = plt.subplots(figsize=(8.6, 6.0)); W, L = 297, 420
    ax.add_patch(Rectangle((0, 0), L, W, fc="#fffdf5", ec="k", lw=1.2)); m = 12
    ax.add_patch(Rectangle((m, m), L - 2 * m, W - 2 * m, fill=False, ec="k", lw=2.4))
    nx, ny = 8, 6; gx, gy = (L - 2 * m) / nx, (W - 2 * m) / ny
    for i in range(nx):
        ax.plot([m + i * gx] * 2, [W - m, W - m + 5], "k", lw=.8); ax.plot([m + i * gx] * 2, [m - 5, m], "k", lw=.8)
        ax.text(m + (i + .5) * gx, W - m + 7, str(i + 1), ha="center", fontsize=8); ax.text(m + (i + .5) * gx, m - 10, str(i + 1), ha="center", fontsize=8)
    for j in range(ny):
        ax.plot([m - 5, m], [m + j * gy] * 2, "k", lw=.8); ax.plot([L - m, L - m + 5], [m + j * gy] * 2, "k", lw=.8)
        ax.text(m - 9, m + (j + .5) * gy, "FEDCBA"[j], va="center", fontsize=8); ax.text(L - m + 8, m + (j + .5) * gy, "FEDCBA"[j], va="center", fontsize=8)
    tb_w, tb_h = 170, 40; x0, y0 = L - m - tb_w, m
    ax.add_patch(Rectangle((x0, y0), tb_w, tb_h, fc="#e6f0fa", ec="k", lw=1.6))
    for xx in (x0 + 100,): ax.plot([xx, xx], [y0, y0 + tb_h], "k", lw=1)
    ax.plot([x0, x0 + tb_w], [y0 + 20, y0 + 20], "k", lw=1); ax.plot([x0 + 100, x0 + tb_w], [y0 + 10, y0 + 10], "k", lw=1)
    ax.text(x0 + 4, y0 + 28, "TITLE: drawing name", fontsize=7.5); ax.text(x0 + 4, y0 + 8, "NAME, DATE, DWG No.", fontsize=7)
    ax.text(x0 + 104, y0 + 13, "SCALE 1:1", fontsize=7); ax.text(x0 + 104, y0 + 2.5, "projection", fontsize=7)
    ax.annotate("title block (bottom right)", (x0 + 40, y0 + tb_h), (x0 - 20, y0 + 80), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("border", (m, W / 2), (40, W / 2 + 40), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate("grid reference: even number of divisions,\neach 25–75 mm", (m + 3 * gx, W - m), (m + 2 * gx, W - m - 50), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_xlim(-10, L + 10); ax.set_ylim(-20, W + 20); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("A3 sheet (420 × 297 mm): border, grid reference and title block (schematic)")
    save(fig, "sheet-layout")
    print("sheet grid division size (420-24)/8, (297-24)/6 =", round(gx, 1), round(gy, 1), "mm")


def scales():
    fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.6))
    for ax, (lab, k) in zip(axs, (("SCALE 2:1 (enlargement)", 2.0), ("SCALE 1:1 (full size)", 1.0), ("SCALE 1:2 (reduction)", 0.5))):
        w, h = 40 * k, 25 * k; ax.add_patch(Rectangle((0, 0), w, h, fc="#e6f0fa", ec="k", lw=1.6)); ax.add_patch(Circle((w / 2, h / 2), 6 * k, fill=False, ec="k", lw=1.4))
        ax.plot([w / 2 - 9 * k, w / 2 + 9 * k], [h / 2, h / 2], color=RED, lw=.8, ls="-."); ax.plot([w / 2, w / 2], [h / 2 - 9 * k, h / 2 + 9 * k], color=RED, lw=.8, ls="-.")
        dim_h(ax, 0, w, -7 * max(k, .6), "40", fs=9); dim_v(ax, -5, 0, h, "25", fs=9, side=-1)
        ax.set_xlim(-18, 90); ax.set_ylim(-22, 62); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(lab, fontsize=10)
        ax.text(w / 2, h + 4 * max(k, .6), "drawn %.0f × %.0f mm" % (w, h), ha="center", fontsize=8, color=GREY)
    fig.suptitle("The dimension numbers are the TRUE size (40 and 25 mm) whatever the scale", y=1.0, fontsize=10.5)
    save(fig, "scales")
    print("mural exercise: scale factor 45/3 =", 45 / 3)


def lines():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.4), gridspec_kw={"width_ratios": [.8, 1.2]})
    items = [("Continuous thick", "visible line (outlines)", dict(lw=3, ls="-")), ("Continuous thin", "dimension, extension, leader lines", dict(lw=1, ls="-")),
             ("Dashed thick", "hidden line (cannot be seen)", dict(lw=2.4, ls=(0, (5, 3)))), ("Chain thin", "centre line (axes, symmetry, paths)", dict(lw=1, ls=(0, (8, 2, 1, 2))))]
    for i, (n, use, kw) in enumerate(items):
        y = 3 - i; a.plot([0, 3], [y, y], color="k", **kw); a.text(3.2, y + .12, n, fontsize=10, fontweight="bold"); a.text(3.2, y - .22, use, fontsize=8.5, color=GREY)
    a.set_xlim(-.2, 8.5); a.set_ylim(-.6, 3.6); a.axis("off"); a.set_title("Basic line types (BIS SP 46)")
    # a plate with a hole: front view and side view, with hidden line and centre lines
    b.add_patch(Rectangle((0, 0), 60, 35, fill=False, lw=2.6)); b.add_patch(Circle((30, 17.5), 8, fill=False, lw=2.6))
    b.plot([30, 30], [4, 31], color="k", lw=.9, ls=(0, (8, 2, 1, 2))); b.plot([16, 44], [17.5, 17.5], color="k", lw=.9, ls=(0, (8, 2, 1, 2)))
    b.add_patch(Rectangle((80, 0), 12, 35, fill=False, lw=2.6)); b.plot([80, 92], [9.5, 9.5], color="k", lw=2.2, ls=(0, (5, 3))); b.plot([80, 92], [25.5, 25.5], color="k", lw=2.2, ls=(0, (5, 3)))
    b.plot([76, 96], [17.5, 17.5], color="k", lw=.9, ls=(0, (8, 2, 1, 2)))
    b.text(30, -7, "front view:\nhole visible", ha="center", fontsize=8.5); b.text(86, -7, "side view:\nhole hidden (dashed)", ha="center", fontsize=8.5)
    b.annotate("centre lines mark the hole's axis", (30, 17.5), (6, 46), arrowprops=dict(arrowstyle="->"), fontsize=8.5); b.set_xlim(-6, 104); b.set_ylim(-14, 58); b.set_aspect("equal"); b.axis("off"); b.set_title("Same hole, two views")
    save(fig, "lines")


def dimensioning():
    fig, ax = plt.subplots(figsize=(8.4, 5.0))
    ax.add_patch(Rectangle((0, 0), 80, 40, fill=False, lw=2.6)); ax.add_patch(Circle((20, 20), 7, fill=False, lw=2.6)); ax.add_patch(Circle((60, 20), 7, fill=False, lw=2.6))
    for cx in (20, 60):
        ax.plot([cx, cx], [8, 32], color="k", lw=.8, ls=(0, (8, 2, 1, 2))); ax.plot([cx - 12, cx + 12], [20, 20], color="k", lw=.8, ls=(0, (8, 2, 1, 2)))
    for x in (0, 80):
        ax.plot([x, x], [41, 52], color="k", lw=.8)
    dim_h(ax, 0, 80, 50, "80"); ax.plot([0, 0], [-1, -14], "k", lw=.8); ax.plot([20, 20], [-1, -14], "k", lw=.8); ax.plot([60, 60], [-1, -14], "k", lw=.8)
    dim_h(ax, 0, 20, -12, "20"); dim_h(ax, 20, 60, -12, "40"); dim_h(ax, 60, 80, -12, "20")
    ax.plot([81, 94], [0, 0], "k", lw=.8); ax.plot([81, 94], [40, 40], "k", lw=.8); dim_v(ax, 92, 0, 40, "40", side=1)
    ax.annotate("", xy=(20 + 7 * np.cos(np.radians(135)), 20 + 7 * np.sin(np.radians(135))), xytext=(4, 56 - 12), arrowprops=dict(arrowstyle="-|>", color="k", lw=.8, mutation_scale=8))
    ax.plot([4, 14], [44, 44], "k", lw=.8); ax.text(15, 44.5, "Ø14, 2 holes", fontsize=9)
    ax.annotate("extension line", (80, 46), (88, 56), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=BLUE), color=BLUE); ax.annotate("dimension line\nwith arrowheads", (40, 50), (30, 62), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=RED), color=RED, ha="center")
    ax.annotate("leader line", (12, 43), (-14, 56), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GREEN), color=GREEN)
    ax.set_xlim(-22, 110); ax.set_ylim(-24, 70); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("A dimensioned plate (all dimensioning lines thin; dimensions in mm)")
    save(fig, "dimensioning")


def first_angle():
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    # object: L-shaped block 60 wide, 40 high, 30 deep with a step (top-right notch 20x15)
    def front(x0, y0):
        pts = [(0, 0), (60, 0), (60, 25), (40, 25), (40, 40), (0, 40), (0, 0)]; return [(x0 + a, y0 + b) for a, b in pts]
    fx, fy = 0, 50
    F = front(fx, fy); ax.plot(*zip(*F), color="k", lw=2.4); ax.plot([fx + 40, fx + 40], [fy, fy + 25], color="k", lw=1.2)
    ax.text(fx + 30, fy + 20, "FRONT\nVIEW", ha="center", fontsize=9, color=BLUE)
    tx, ty = 0, 0; T = [(tx, ty), (tx + 60, ty), (tx + 60, ty + 30), (tx, ty + 30), (tx, ty)]; ax.plot(*zip(*T), color="k", lw=2.4); ax.plot([tx + 40, tx + 40], [ty, ty + 30], color="k", lw=1.2)
    ax.text(tx + 30, ty + 15, "TOP VIEW\n(below the front)", ha="center", fontsize=9, color=GREEN)
    sx, sy = 80, 50; S = [(sx, sy), (sx + 30, sy), (sx + 30, sy + 40), (sx, sy + 40), (sx, sy)]; ax.plot(*zip(*S), color="k", lw=2.4); ax.plot([sx, sx + 30], [sy + 25, sy + 25], color="k", lw=2.0, ls=(0, (5, 3)))
    ax.text(sx + 15, sy + 20, "LEFT SIDE\nVIEW\n(right of\nthe front)", ha="center", fontsize=8.5, color=ORANGE)
    for x in (0, 40, 60):
        ax.plot([x, x], [32, 49], color=GREY, lw=.7, ls=":")
    for y in (50, 75, 90):
        ax.plot([61, 79], [y, y], color=GREY, lw=.7, ls=":")
    ax.annotate("projection lines align the views", (50, 41), (85, 20), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=8.5, color=GREY)
    ax.set_xlim(-8, 124); ax.set_ylim(-8, 106); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("First-angle projection (BIS): top view below, left side view to the right")
    save(fig, "first-angle")


if __name__ == "__main__":
    a_series(); sheet_layout(); scales(); lines(); dimensioning(); first_angle()
