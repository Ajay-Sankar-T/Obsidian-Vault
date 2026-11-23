"""Redraws the Tutorial 1 circuits and plots into  Problems/Tutorial 1 - Circuit Laws and Theorems/assets/.
Run:  python ee_figs_t1.py"""
import os
import numpy as np
from ee_draw import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Problems", "Tutorial 1 - Circuit Laws and Theorems", "assets")
os.makedirs(OUT, exist_ok=True)


def fig(name, xl, yl, title, draw, size=(7.2, 3.6)):
    f, ax = plt.subplots(figsize=size)
    draw(ax)
    finish(ax, xl, yl, title)
    save(f, os.path.join(OUT, name))


def q1(ax):
    xs = [3, 6, 9]
    wire(ax, (0, 3), (1, 3)); res(ax, (1, 3), (3, 3), "R", side=-1); wire(ax, (0, 0), (12.8, 0))
    battery(ax, (0, 0), (0, 3), "$V_R$", plus=2, side=-1)
    wire(ax, (0, 3), (1, 3))
    prev = 3
    for k, x in enumerate(xs):
        dot(ax, x, 3); res(ax, (x, 3), (x, 0), "2R", side=1)
        if k < 2:
            res(ax, (x, 3), (xs[k + 1], 3), "R", side=-1)
    res(ax, (9, 3), (12, 3), "R", side=-1); res(ax, (12, 3), (12, 0), "R", side=1); dot(ax, 12, 0)
    for x, n in zip([0.0] + xs, ["$V_1$", "$V_2$", "$V_3$", "$V_4$"]):
        ax.text(x + (0.45 if x == 0 else 0), 3.35, n, ha="center", fontsize=10, color=BLUE)
    for x, n in zip([2.0, 4.5, 7.5, 10.5], ["$I_1$", "$I_2$", "$I_3$", "$I_4$"]):
        arrow(ax, (x - 0.45, 3.45), (x + 0.45, 3.45), n, side=1, off=0.28)
    arrow(ax, (-1.0, -0.6), (-1.0, 0.6), "", c=ORANGE); ax.text(-1.4, 0, "$R_{in}$", ha="right", va="center", color=ORANGE, fontsize=10)
    wire(ax, (-1.0, 3), (0, 3)); ax.plot([-1.0], [3], "o", mfc="w", mec=ORANGE, ms=4)
    ax.annotate("", xy=(-1.0, 2.95), xytext=(-1.0, 0.05), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.4))


def q2(ax):
    wire(ax, (0, 0), (9, 0))
    battery(ax, (0, 0), (0, 3), "$E_1$=10 V", plus=2, side=-1); wire(ax, (0, 3), (0.5, 3)); res(ax, (0.5, 3), (3, 3), "3 Ω")
    dot(ax, 3, 3); res(ax, (3, 3), (3, 1.7), "8 Ω"); battery(ax, (3, 1.7), (3, 0), "$E_2$=10 V", plus=1, side=-1)
    res(ax, (3, 3), (6.5, 3), "6 Ω"); dot(ax, 6.5, 3); res(ax, (6.5, 3), (6.5, 0), "12 Ω"); dot(ax, 6.5, 0)
    wire(ax, (6.5, 3), (9, 3)); battery(ax, (9, 3), (9, 0), "$E_3$=10 V", plus=1, side=1)
    node(ax, 3, 3, "A", dy=0.2, c=BLUE); node(ax, 6.5, 3, "B", dy=0.2, c=BLUE)
    arrow(ax, (6.5 + 0.35, 2.5), (6.5 + 0.35, 1.5), "0.833 A", side=1, off=0.5)


def q3(ax):
    wire(ax, (0, 0), (10.5, 0)); wire(ax, (0, 3), (10.5, 3))
    isrc(ax, (0, 3), (0, 0), "8 A", side=-1); res(ax, (3, 3), (3, 0), "6 Ω", side=1); res(ax, (6, 3), (6, 0), "3 Ω", side=1)
    isrc(ax, (9, 0), (9, 3), "2 A", side=1)
    for x in (3, 6, 9): dot(ax, x, 3); dot(ax, x, 0)
    arrow(ax, (3.9, 2.7), (3.9, 1.8), "$I_1$", side=1); arrow(ax, (6.9, 2.7), (6.9, 1.8), "$I_2$", side=1)
    arrow(ax, (10.3, 0.2), (10.3, 2.8), "$V_0$", side=1, c=RED)


def q4(ax):
    wire(ax, (0, 0), (9.5, 0)); wire(ax, (0, 3), (9.5, 3))
    battery(ax, (0, 0), (0, 3), "12 V", plus=2, side=-1); res(ax, (3, 3), (3, 0), "$R_1$=6 Ω", side=1)
    isrc(ax, (6, 0), (6, 3), "$KI$", side=1, dep=True); res(ax, (9, 3), (9, 0), "$R_2$=3 Ω", side=1)
    for x in (3, 6, 9): dot(ax, x, 3); dot(ax, x, 0)
    arrow(ax, (1.0, 3.3), (1.9, 3.3), "$I_1$", side=1); arrow(ax, (3.9, 2.7), (3.9, 1.8), "$I$", side=1)


def q5(ax):
    wire(ax, (0, 0), (7.5, 0)); wire(ax, (0, 3), (7.5, 3))
    res(ax, (0, 3), (0, 1.8), "20 Ω", side=-1); vsrc(ax, (0, 1.8), (0, 0), "$10\\,i_1$", plus=1, side=-1, dep=True, r=0.45)
    res(ax, (4, 3), (4, 0), "$R_L$", side=1)
    res(ax, (7, 3), (7, 1.8), "40 Ω", side=1); battery(ax, (7, 1.8), (7, 0), "50 V", plus=1, side=1)
    dot(ax, 4, 3); dot(ax, 4, 0)
    arrow(ax, (4.8, 3.3), (5.9, 3.3), "$i_1$", side=1)
    node(ax, 4.8, 3, None); node(ax, 4.8, 0, None)


def q6(ax):
    wire(ax, (0, 0), (10, 0)); wire(ax, (0, 3), (0.5, 3))
    battery(ax, (0, 0), (0, 3), "24 V", plus=2, side=-1); res(ax, (0.5, 3), (3.2, 3), "10 Ω"); dot(ax, 3.2, 3)
    isrc(ax, (3.2, 0), (3.2, 3), "2 A", side=-1); res(ax, (3.2, 3), (6.4, 3), "20 Ω"); dot(ax, 6.4, 3)
    res(ax, (6.4, 3), (6.4, 0), "30 Ω", side=1); res(ax, (6.4, 3), (9.5, 3), "45 Ω"); battery(ax, (9.5, 3), (9.5, 0), "48 V", plus=1, side=1)
    ax.text(4.8, 3.9, "+  $V_x$  −", ha="center", color=RED, fontsize=10); dot(ax, 3.2, 0); dot(ax, 6.4, 0)


def q7(ax):
    wire(ax, (0, 0), (10.8, 0)); wire(ax, (0, 3), (3, 3))
    isrc(ax, (0, 0), (0, 3), "10 A", side=-1); res(ax, (3, 3), (3, 0), "1 Ω", side=-1); dot(ax, 3, 3); dot(ax, 3, 0)
    res(ax, (3, 3), (7, 3), "2.5 Ω"); dot(ax, 7, 3); dot(ax, 7, 0); res(ax, (7, 3), (7, 0), "0.5 Ω", side=1)
    wire(ax, (7, 3), (10, 3)); isrc(ax, (10, 0), (10, 3), "4 A", side=1)
    ax.text(3, 3.55, "$V_1$", ha="center", color=BLUE, fontsize=10); ax.text(7, 3.55, "$V_2$", ha="center", color=BLUE, fontsize=10)
    for x, n in ((1.5, "$I_a$"), (5, "$I_b$"), (8.6, "$I_c$")):
        ax.add_patch(FancyArrowPatch((x - 0.55, 1.2), (x + 0.55, 1.2), connectionstyle="arc3,rad=-1.0", arrowstyle="-|>", mutation_scale=11, color=ORANGE, lw=1.5))
        ax.text(x, 1.45, n, ha="center", fontsize=9, color=ORANGE)


def q8(ax):
    # nodes a (3,4) on the top rail, L (0,2), TR (7,4), R (7,2), b (3,2)
    wire(ax, (0, 4), (2, 4)); wire(ax, (2, 4), (3, 4)); dot(ax, 3, 4)
    battery(ax, (0, 4), (0, 2), "45 V", plus=1, side=-1)
    wire(ax, (3, 4), (3.7, 4)); battery(ax, (3.7, 4), (5.8, 4), "120 V", plus=1, side=1); wire(ax, (5.8, 4), (7, 4))
    res(ax, (7, 4), (7, 2), "15 Ω", side=1); wire(ax, (7, 2), (7, 0))
    res(ax, (0, 2), (3, 2), "10 Ω", side=1); dot(ax, 3, 2); res(ax, (3, 2), (7, 2), "5 Ω", side=1)
    res(ax, (3, 4), (3, 2), "20 Ω", side=1)
    wire(ax, (0, 2), (0, 0)); battery(ax, (0, 0), (2.8, 0), "20 V", plus=1, side=-1); res(ax, (2.8, 0), (7, 0), "5 Ω", side=-1)
    node(ax, 3, 4, "a", c=RED); node(ax, 3, 2, "b", dy=-0.55, c=RED); dot(ax, 0, 2); dot(ax, 7, 2)


def q9(ax):
    wire(ax, (0, 0), (11.5, 0)); wire(ax, (0, 3), (0.5, 3))
    battery(ax, (0, 0), (0, 3), "120 V", plus=2, side=-1); res(ax, (0.5, 3), (3.3, 3), "30 Ω"); dot(ax, 3.3, 3); dot(ax, 3.3, 0)
    res(ax, (3.3, 3), (3.3, 0), "60 Ω", side=-1)
    battery(ax, (3.3, 3), (5.6, 3), "40 V", plus=2, side=1); res(ax, (5.6, 3), (8.4, 3), "10 Ω"); dot(ax, 8.4, 3); dot(ax, 8.4, 0)
    res(ax, (8.4, 3), (8.4, 0), "30 Ω", side=-1); res(ax, (8.4, 3), (10.9, 3), "$R_L$"); battery(ax, (10.9, 3), (10.9, 0), "10 V", plus=2, side=1)
    node(ax, 8.4, 3, "a", c=RED); node(ax, 10.9, 3, "b", c=RED)


def q10(ax):
    wire(ax, (0, 0), (8, 0)); wire(ax, (0, 3), (1, 3))
    battery(ax, (0, 0), (0, 3), "20 V", plus=2, side=-1); res(ax, (1, 3), (4, 3), "$R_1$=2 Ω"); dot(ax, 4, 3)
    res(ax, (4, 3), (4, 1.7), "$R_2$=2 Ω", side=-1); battery(ax, (4, 1.7), (4, 0), "30 V", plus=1, side=-1)
    battery(ax, (4, 3), (7, 3), "40 V", plus=1, side=1); wire(ax, (7, 3), (8, 3)); res(ax, (8, 3), (8, 0), "$R_L$", side=1)
    node(ax, 8, 3, "a", c=RED); node(ax, 8, 0, "b", dy=-0.55, c=RED)


def q11(ax):
    a, b, c, d, e = (3, 4), (6, 2), (0, 2), (3, 2), (3, 0)
    battery(ax, c, a, "100 V", plus=2, side=1)
    isrc(ax, d, a, "5 A", side=-1); res(ax, a, b, "12.5 Ω", side=1)
    res(ax, c, d, "20 Ω", side=1); battery(ax, d, b, "150 V", plus=2, side=1)
    res(ax, d, e, "25 Ω", side=-1); res(ax, c, e, "10 Ω", side=-1); isrc(ax, e, b, "10 A", side=-1)
    for n, p, dx, dy in (("a", a, 0, 0.2), ("b", b, 0.3, 0), ("c", c, -0.3, 0), ("d", d, 0.3, 0.25), ("e", e, 0, -0.55)):
        node(ax, p[0], p[1], n, dx=dx, dy=dy, c=RED)
    ax.text(3.3, 1.65, "+", fontsize=9, color=BLUE, ha="center"); ax.text(3.3, 0.35, "−", fontsize=9, color=BLUE, ha="center"); ax.text(3.95, 1.0, "$v_4$", fontsize=9, color=BLUE, ha="center", va="center")


def q12(ax):
    p, a, q = (0, 4), (3, 4), (6, 4); d, e, b = (0, 2), (3, 2), (6, 2); r, c, s = (0, 0), (3, 0), (6, 0)
    res(ax, p, a, "2 Ω"); res(ax, a, q, "3 Ω"); isrc(ax, p, d, "4.5 A", side=-1); battery(ax, q, b, "5 V", plus=1, side=1)
    battery(ax, a, e, "2.2 V", plus=2, side=1); res(ax, d, e, "9 Ω"); res(ax, e, b, "4 Ω"); res(ax, d, r, "3 Ω", side=-1)
    battery(ax, r, c, "3 V", plus=1, side=-1); isrc(ax, e, c, "2 A", side=-1); res(ax, b, s, "6 Ω", side=1); res(ax, s, c, "1 Ω", side=-1)
    for n, pt, dx, dy in (("a", a, 0, 0.2), ("b", b, 0.35, 0), ("c", c, 0, -0.55), ("d", d, -0.35, 0), ("e", e, 0.35, 0.2)):
        node(ax, pt[0], pt[1], n, dx=dx, dy=dy, c=RED)


def q13(ax):
    A, B, C = (0, 0), (8, 0), (4, 6.9); A_, B_, C_ = (2.1, 1.9), (5.9, 1.9), (4, 3.6)
    res(ax, A, C, "5", side=-1, body=1.4); res(ax, C, B, "5", side=-1, body=1.4); res(ax, A, B, "5", side=-1, body=1.4)
    res(ax, A, A_, "4.75", side=1, body=1.0); res(ax, B, B_, "4.5", side=-1, body=1.0); res(ax, C, C_, "3.25", side=1, body=1.0)
    res(ax, A_, C_, "1.5", side=-1, body=1.0); res(ax, B_, C_, "2.5", side=1, body=1.0); res(ax, A_, B_, "1 Ω", side=-1, body=1.0)
    for n, pt, dx, dy in (("A", A, -0.35, -0.55), ("B", B, 0.35, -0.55), ("C", C, 0, 0.2)):
        node(ax, pt[0], pt[1], n, dx=dx, dy=dy, c=RED)
    for pt in (A_, B_, C_): dot(ax, *pt)


def q14(ax):
    a, c, b, d = (3, 4), (0, 2), (6, 2), (3, 0)
    res(ax, c, a, "$R_{ca}$=15 Ω", side=1); res(ax, a, b, "$R_{ab}$=20 Ω", side=1); res(ax, c, b, "$R_{bc}$=35 Ω", side=1)
    res(ax, c, d, "$R_{cd}$=8 Ω", side=-1); res(ax, b, d, "$R_{bd}$=25 Ω", side=-1)
    wire(ax, a, (-2.2, 4)); battery(ax, (-2.2, 4), (-2.2, 0), "E=180 V", plus=1, side=-1); wire(ax, (-2.2, 0), d)
    for n, pt, dx, dy in (("a", a, 0, 0.2), ("b", b, 0.35, 0), ("c", c, -0.35, 0), ("d", d, 0, -0.55)):
        node(ax, pt[0], pt[1], n, dx=dx, dy=dy, c=RED)


def q10_plot():
    f, ax = plt.subplots(figsize=(6.6, 3.6))
    RL = np.linspace(0.02, 12, 600); Pw = (15 / (1 + RL)) ** 2 * RL
    ax.plot(RL, Pw, color=BLUE, lw=2)
    for x, y, t in ((3, 42.1875, "3 Ω: 42.19 W"), (1, 56.25, "1 Ω: $P_{max}$=56.25 W"), (3 + 2 * 2 ** 0.5, 28.125, "5.83 Ω"), (3 - 2 * 2 ** 0.5, 28.125, "0.172 Ω")):
        ax.plot([x], [y], "o", color=RED if "max" in t else ORANGE); ax.annotate(t, (x, y), xytext=(x + 0.3, y + 3), fontsize=9)
    ax.axhline(28.125, color=GREY, ls="--", lw=1); ax.text(8.3, 29.5, "$P_{max}/2$ = 28.1 W", fontsize=9, color=GREY)
    ax.set_xlabel("$R_L$ (Ω)"); ax.set_ylabel("power in $R_L$ (W)"); ax.set_title("Q10: power delivered to $R_L$ ($V_{th}$=15 V, $R_{th}$=1 Ω)"); ax.grid(alpha=0.3)
    save(f, os.path.join(OUT, "T1-Q10-power-curve.png"))


if __name__ == "__main__":
    specs = [
        ("T1-Q1-circuit.png", (-2.2, 13.2), (-1.0, 4.4), "Q1: R-2R ladder", q1, (8.2, 3.4)),
        ("T1-Q2-circuit.png", (-1.5, 10.5), (-0.6, 3.8), "Q2: three batteries, four resistors", q2, (7.2, 3.2)),
        ("T1-Q3-circuit.png", (-1.5, 11.5), (-0.6, 3.6), "Q3: two current sources", q3, (7.4, 2.8)),
        ("T1-Q4-circuit.png", (-1.5, 10.5), (-0.6, 3.8), "Q4: dependent current source $KI$", q4, (7.2, 2.9)),
        ("T1-Q5-circuit.png", (-1.8, 8.6), (-0.6, 3.8), "Q5: dependent source, find $R_L$ for maximum power", q5, (7.2, 3.0)),
        ("T1-Q6-circuit.png", (-1.5, 11), (-0.6, 4.3), "Q6: superposition for $V_x$", q6, (7.6, 3.1)),
        ("T1-Q7-circuit.png", (-1.5, 11.5), (-0.6, 4.0), "Q7: meshes with current sources", q7, (7.4, 2.9)),
        ("T1-Q8-circuit.png", (-1.4, 8.4), (-1.0, 5.0), "Q8: Thevenin equivalent seen by the 20 Ω resistor", q8, (6.6, 4.0)),
        ("T1-Q9-circuit.png", (-1.6, 12.6), (-0.6, 3.8), "Q9: Norton equivalent seen by $R_L$", q9, (6.4, 2.4)),
        ("T1-Q10-circuit.png", (-1.5, 9.5), (-1.0, 3.9), "Q10: maximum power into $R_L$", q10, (6.4, 3.0)),
        ("T1-Q11-circuit.png", (-1.5, 7.5), (-1.0, 4.9), "Q11: supernodes a–c and b–d", q11, (6.0, 3.8)),
        ("T1-Q12-circuit.png", (-1.5, 7.6), (-0.8, 5.0), "Q12: mesh analysis and power balance", q12, (6.2, 4.0)),
        ("T1-Q13-circuit.png", (-1.5, 9.5), (-1.0, 7.9), "Q13: resistance between A and B", q13, (5.8, 5.4)),
        ("T1-Q14-circuit.png", (-3.2, 7.6), (-1.0, 5.0), "Q14: bridge network fed from a–d", q14, (6.4, 3.8)),
    ]
    for name, xl, yl, title, fn, size in specs:
        fig(name, xl, yl, title, fn, size)
    q10_plot()
    print("T1 figures written to", os.path.abspath(OUT))
