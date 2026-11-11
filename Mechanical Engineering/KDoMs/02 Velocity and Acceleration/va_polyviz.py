"""Figures for the graphical-methods note:  python va_polyviz.py [g1 g2 g3 g4 g5]"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import *
from va_poly import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets"); os.makedirs(OUT, exist_ok=True)
B, O, G, K, RR, GR, PU = "#1f77b4", "#e8590c", "#7a7a7a", "#111111", "#d6204a", "#2a9d4a", "#9467bd"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
def save(fig, n): fig.savefig(os.path.join(OUT, n), dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote", n)
def vecarrow(ax, p, q, c, lw=2, ls="-", lab=None, off=(0, 0), fs=9):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, ls=ls, shrinkA=0, shrinkB=0))
    if lab: m = (np.asarray(p)+np.asarray(q))/2; ax.text(m[0]+off[0], m[1]+off[1], lab, color=c, fontsize=fs)
def node(ax, p, name, c=K, off=(.03, .03), fs=10): ax.plot(*p, "o", color=c, ms=4.5, zorder=5); ax.text(p[0]+off[0], p[1]+off[1], name, color=c, fontsize=fs)
def link(ax, pts, c=K, lw=2.2): ax.plot([p[0] for p in pts], [p[1] for p in pts], color=c, lw=lw)
def pad(ax, pts, m): p = np.array(pts); ax.set_xlim(p[:, 0].min()-m, p[:, 0].max()+m); ax.set_ylim(p[:, 1].min()-m, p[:, 1].max()+m); ax.set_aspect("equal"); ax.axis("off")

# ---- g1: Problem 2.9 slider-crank -------------------------------------------------------------------------------------
def g1():
    w2 = -1000*2*pi/60; P = poly_slider(6., 16., radians(45), w2)
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.8))
    ax = axs[0]; link(ax, [P["O2"], P["A"], P["B"]]); ax.plot([-2, 24], [0, 0], color=G, lw=1, ls="-."); node(ax, P["O2"], "O₂", off=(-.8, -1)); node(ax, P["A"], "A", off=(-.1, .5)); node(ax, P["B"], "B", off=(.3, .5))
    ax.add_patch(plt.Rectangle((P["B"][0]-1.2, -.9), 2.4, 1.8, fc="#cfe3f5", ec=B)); ax.set_title("Prob. 2.9: ω₂ = 1000 rpm CW, θ₂ = 45°, O₂A = 6, AB = 16 cm", fontsize=9.5); pad(ax, [[-2, -3], [24, 7]], 1)
    ax = axs[1]; o, a, b = P["o"], P["va"], P["vb"]
    vecarrow(ax, o, a, B, lab="V_A = ω₂·O₂A", off=(-190, 20)); vecarrow(ax, a, b, GR, lab="V_BA ⊥ AB (= ω₃·AB)", off=(10, 20)); vecarrow(ax, o, b, O, lab="V_B (horizontal)", off=(-30, -50), lw=2.4)
    for p, n in ((o, "o₂"), (a, "a"), (b, "b")): node(ax, p, n, off=(15, 15))
    ax.set_title(f"velocity polygon (cm/s):  V_B = {abs(b[0]):.0f} →,  ω₃ = {P['w3']:.1f} rad/s CCW", fontsize=9.5); pad(ax, [o, a, b], 120)
    ax = axs[2]; o, a, b, c = P["o"], P["aa"], P["ab"], P["aBA_n"]
    vecarrow(ax, o, a, B, lab="a_A = ω₂²·O₂A (→O₂)", off=(-9000, 2500)); vecarrow(ax, a, c, PU, lab="aⁿ_BA = ω₃²·AB (→A)", off=(-6000, 3500)); vecarrow(ax, c, b, GR, lw=1.6, lab="aᵗ_BA ⊥ AB", off=(-3000, -9000)); vecarrow(ax, o, b, O, lw=2.4, lab="a_B", off=(-3000, 3000))
    for p, n in ((o, "o₂"), (a, "a"), (c, "n"), (b, "b")): node(ax, p, n, off=(1500, 1500))
    ax.set_title(f"acceleration polygon (cm/s²):  a_B = {abs(b[0]):.0f} ←,  α₃ = {P['a3']:.0f} rad/s² CCW", fontsize=9.5); pad(ax, [o, a, b, c], 9000)
    fig.suptitle("The book's graphical readings are V_B = 574, ω₃ = 27.5, a_B = 46 000, α₃ = 2845; the constructions here give 566.5, 28.8, 47 490, 2788 (graphical accuracy ≈ 1–5 %)", fontsize=9.5, y=1.02); save(fig, "VG-g1-slider-crank-polygons.png")

# ---- g2: four-bar with polygons and images ---------------------------------------------------------------------------------
def g2():
    l = (5.5, 1.7, 5.5, 4.08); Q = poly_fourbar(l, radians(115), 2.0, 1.5, 1, kC=(2.2, 1.2)); s = Q["st"]
    fig, axs = plt.subplots(1, 3, figsize=(16, 5.2)); ax = axs[0]
    link(ax, [Q["O2"], Q["A"], Q["B"], Q["O4"]]); ax.plot([Q["O2"][0], Q["O4"][0]], [0, 0], color=G, ls="-.", lw=1); ax.fill([Q["A"][0], Q["B"][0], Q["C"][0]], [Q["A"][1], Q["B"][1], Q["C"][1]], color="#cfe3f5", alpha=.8)
    for p, n in ((Q["O2"], "O₂"), (Q["O4"], "O₄"), (Q["A"], "A"), (Q["B"], "B"), (Q["C"], "C")): node(ax, p, n, off=(.1, -.35))
    ax.set_title("four-bar, θ₂ = 115°, ω₂ = 2, α₂ = 1.5 (ABC = coupler)", fontsize=9.5); pad(ax, [Q["O2"], Q["O4"], Q["B"], Q["A"], Q["C"]], .8)
    ax = axs[1]; o, a, b, c = Q["o"], Q["va"], Q["vb"], Q["vc"]
    vecarrow(ax, o, a, B, lab="V_A", off=(.1, .1)); vecarrow(ax, a, b, GR, lab="V_BA ⊥ AB", off=(.1, .1)); vecarrow(ax, o, b, O, lw=2.4, lab="V_B ⊥ O₄B", off=(.1, -.3)); vecarrow(ax, a, c, GR, lw=1.2, ls="--"); vecarrow(ax, o, c, RR, lw=1.6, lab="V_C", off=(.1, -.2))
    ax.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]], color="#fbd9c4", alpha=.7)
    for p, n in ((o, "o₂ = o₄"), (a, "a"), (b, "b"), (c, "c")): node(ax, p, n, off=(.08, .08))
    ax.set_title("velocity polygon with the velocity image abc (⊥ ABC, scale ω₃)", fontsize=9.5); pad(ax, [o, a, b, c], .8)
    ax = axs[2]; o, a, b, c = Q["o"], Q["aa"], Q["ab"], Q["ac"]
    vecarrow(ax, o, a, B, lab="a_A", off=(.1, .1)); vecarrow(ax, a, Q["aBA_n"], PU, lw=1.4, lab="aⁿ_BA", off=(.1, .1)); vecarrow(ax, Q["aBA_n"], b, GR, lw=1.4, lab="aᵗ_BA", off=(.1, .1))
    vecarrow(ax, o, Q["aB_n"], PU, lw=1.4, lab="aⁿ_B", off=(.1, -.5)); vecarrow(ax, Q["aB_n"], b, GR, lw=1.4, lab="aᵗ_B ⊥ O₄B", off=(.1, -.5)); vecarrow(ax, o, b, O, lw=2.4, lab="a_B", off=(-.8, .1)); vecarrow(ax, o, c, RR, lw=1.6, lab="a_C", off=(.1, .1))
    ax.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]], color="#fbd9c4", alpha=.7)
    for p, n in ((o, "o₂ = o₄"), (a, "a"), (b, "b"), (c, "c")): node(ax, p, n, off=(.08, .08))
    phi = degrees(atan2(s["a3"], s["w3"]**2)); ax.set_title(f"acceleration polygon and image abc (turned by 180° − φ, φ = tan⁻¹(α₃/ω₃²) = {phi:.1f}°)", fontsize=9.5); pad(ax, [o, a, b, c, Q["aB_n"], Q["aBA_n"]], 1.2)
    save(fig, "VG-g2-fourbar-polygons-images.png")

# ---- g3: slotted lever (Prob 2.10 type): coincident points, Coriolis ---------------------------------------------------------
def g3():
    Z = poly_slotted(3.0, 5.0, radians(25), 2.0, 0.0); fig, axs = plt.subplots(1, 3, figsize=(16, 5.4)); ax = axs[0]; e = Z["e"]
    ax.plot(*zip(Z["O4"]-e*1.2, Z["O4"]+e*9.5), color=G, lw=6, alpha=.5); link(ax, [Z["O2"], Z["A"]])
    for p, n in ((Z["O2"], "O₂"), (Z["O4"], "O₄"), (Z["A"], "A₂ = A₃ = A₄")): node(ax, p, n, off=(.15, -.5))
    ax.set_title("slotted lever (l₁ = 3, l₂ = 5, θ₂ = 25°, ω₂ = 2): coincident points A₂, A₃, A₄", fontsize=9.5); pad(ax, [Z["O2"], Z["O4"], Z["A"], Z["O4"]+e*9], 1)
    ax = axs[1]; o = Z["o"]
    vecarrow(ax, o, Z["va2"], B, lab="V_A2 = V_A3 = ω₂·O₂A", off=(.1, .2)); vecarrow(ax, o, Z["va4"], O, lab="V_A4 ⊥ O₄A", off=(-3.8, -1.2)); vecarrow(ax, Z["va4"], Z["va2"], GR, lw=1.8, lab="V_A3/4 ∥ slot", off=(.3, -.5))
    for p, n in ((o, "o₂ = o₄"), (Z["va2"], "a₂ = a₃"), (Z["va4"], "a₄")): node(ax, p, n, off=(.15, .15))
    ax.set_title(f"velocity polygon:  V_A3 = V_A4 + V_A3/4  →  ω₄ = {Z['w4']:.3f} rad/s", fontsize=9.5); pad(ax, [o, Z["va2"], Z["va4"]], 1.5)
    ax = axs[2]; pts = [o, Z["p1"], Z["p2"], Z["d"], Z["aA3"]]
    vecarrow(ax, o, Z["aA3"], B, lw=2.4, lab="a_A3 = ω₂²·O₂A", off=(.2, .3)); vecarrow(ax, o, Z["p1"], PU, lab="aⁿ_A4 = ω₄²·O₄A", off=(-4.8, -.2)); vecarrow(ax, Z["p1"], Z["p2"], RR, lab="Coriolis 2ω₄×V_A3/4", off=(.2, -.4)); vecarrow(ax, Z["p2"], Z["d"], O, lab="aᵗ_A4 ⊥ O₄A", off=(.2, -.3)); vecarrow(ax, Z["d"], Z["aA3"], GR, lab="a_A3/4 ∥ slot", off=(.2, -.4))
    for p, n in zip(pts[1:], ("n", "c", "d", "a₃")): node(ax, p, n, off=(.15, .15))
    node(ax, o, "o₂ = o₄", off=(.15, .15)); ax.set_title(f"acceleration polygon (closes on a_A3):  α₄ = {Z['a4']:.3f} rad/s²", fontsize=9.5); pad(ax, pts, 2)
    save(fig, "VG-g3-slotted-lever-polygons.png")

# ---- g4: RPRP (Prob 2.11) ---------------------------------------------------------------------------------------------------------
def g4():
    R_ = rprp(); fig, axs = plt.subplots(1, 2, figsize=(11, 4.8)); ax = axs[0]; z = np.zeros(2)
    vecarrow(ax, z, R_["vP2"], B, lab="V_P2 = ω₂·O₂P₂ = 10 ↑", off=(.3, 0)); vecarrow(ax, R_["vP2"], R_["vP2"]+R_["vrel"], O, lab="V_P4/2 = 10 ↓", off=(.3, -.5)); node(ax, z, "o₂ (= p₄ since V_P4 = 0)", off=(.3, -1.2)); node(ax, R_["vP2"], "p₂", off=(.3, .3))
    ax.set_title("velocity: V_P4 = V_P2 + V_P4/2, both ⊥ O₂O₄-vertical, V_P4 horizontal ⇒ V_P4 = 0", fontsize=9.5); pad(ax, [z, R_["vP2"], [8, -2]], 3)
    ax = axs[1]; a1 = z+R_["aP2n"]; a2_ = a1+R_["aP2t"]; a3_ = a2_+R_["ac"]; a4 = a3_+R_["arel"]
    vecarrow(ax, z, a1, B, lab="aⁿ_P2 = ω₂²·O₂P₂ = 20", off=(-12, .8)); vecarrow(ax, a1, a2_, GR, lab="aᵗ_P2 = α₂·O₂P₂ = 20 ↓", off=(.8, -6)); vecarrow(ax, a2_, a3_, RR, lab="Coriolis 2ω₂V_P4/2 = 40 →", off=(-16, -3)); vecarrow(ax, a3_, a4, O, lab="a_P4/2 (vertical) = 20 ↑", off=(.8, 2)); vecarrow(ax, z, a4, PU, lw=2.4, lab="a_P4 = 20 →", off=(2, .8))
    node(ax, z, "o₂", off=(.5, .8)); ax.set_title("acceleration: a_P4 = a_P2ⁿ + a_P2ᵗ + a_c + a_P4/2  ⇒  a_P4 = 20 cm/s² →", fontsize=9.5); pad(ax, [z, a1, a2_, a3_, a4], 8)
    fig.suptitle("Prob. 2.11 (RPRP): ω₂ = 2 rad/s CCW, α₂ = 4 rad/s² CW, O₂P₂ = 5 cm — numbers reproduced exactly", fontsize=10.5); save(fig, "VG-g4-rprp.png")

# ---- g5: circle diagram of instantaneous centres (Prob. 2.8) ----------------------------------------------------------------------
def g5():
    fig, ax = plt.subplots(figsize=(6.8, 6.6)); pts = {i: np.array([cos(pi/2-(i-1)*pi/3), sin(pi/2-(i-1)*pi/3)]) for i in range(1, 7)}
    t = np.linspace(0, 2*pi, 200); ax.plot(np.cos(t), np.sin(t), color=G, lw=.8)
    known = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 6), (1, 4)]; found = [(2, 4), (1, 5), (2, 5), (2, 6)]
    for (i, j) in known: ax.plot(*zip(pts[i], pts[j]), color=K, lw=2)
    for k, (i, j) in enumerate(found): ax.plot(*zip(pts[i], pts[j]), color=(RR if (i, j) == (2, 6) else B), lw=(4 if (i, j) == (2, 6) else 1.8), ls="--" if (i, j) != (2, 6) else "-")
    for i, p in pts.items(): ax.plot(*p, "o", color=K, ms=9); ax.text(p[0]*1.14-.04, p[1]*1.14-.04, str(i), fontsize=14, weight="bold")
    ax.text(0, -1.45, "solid black: found by inspection (12, 23, 34, 45, 56, 16, 14)\nblue dashed: from Aronhold–Kennedy triangles, in the order 24, 15, 25\nthick red: the wanted P₂₆ (common side of triangles 126 & 256)", ha="center", fontsize=8.5)
    ax.set_title("Circle diagram, Whitworth mechanism (Prob. 2.8): 6 links → 15 centres", fontsize=10); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.8, 1.4); save(fig, "VG-g5-circle-diagram.png")

ALL = dict(g1=g1, g2=g2, g3=g3, g4=g4, g5=g5)
if __name__ == "__main__":
    check()
    for k in (sys.argv[1:] or ALL): ALL[k]()
