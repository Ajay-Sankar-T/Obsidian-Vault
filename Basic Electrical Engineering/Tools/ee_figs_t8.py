"""Tutorial 8 (induction machine) figures -> Problems/Tutorial 8 - Induction Machines/assets/.   Run:  python ee_figs_t8.py"""
import os
import math
import numpy as np
from ee_draw import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Problems", "Tutorial 8 - Induction Machines", "assets")
os.makedirs(OUT, exist_ok=True)


def machine(s, Vph=400 / math.sqrt(3), r1=0.15, x1=0.45, r2=0.12, x2=0.45, xm=28.5, ws=2 * math.pi * 25, rext=0.0):
    """exact equivalent circuit; returns stator current, rotor current, developed torque (Thevenin not needed)"""
    Zr = (r2 + rext) / s + 1j * x2
    Zp = 1 / (1 / (1j * xm) + 1 / Zr); Zin = r1 + 1j * x1 + Zp; I1 = Vph / Zin; I2 = I1 * Zp / Zr
    return I1, I2, 3 * abs(I2) ** 2 * (r2 + rext) / s / ws


def fig_revolving():
    f, axs = plt.subplots(1, 2, figsize=(11.5, 3.8))
    wt = np.linspace(0, 2 * np.pi, 400)
    for k, (c, lab) in enumerate(((BLUE, "$i_a$"), (GREEN, "$i_b$"), (ORANGE, "$i_c$"))):
        axs[0].plot(np.degrees(wt), np.sin(wt - k * 2 * np.pi / 3), color=c, lw=2, label=lab)
    for ang in (0, 60, 120, 180): axs[0].axvline(ang, color=GREY, ls=":", lw=1)
    axs[0].set_xlabel("ωt (degrees)"); axs[0].set_title("three-phase currents, $120^\\circ$ apart in time"); axs[0].legend(ncol=3, fontsize=8); axs[0].grid(alpha=0.3)
    al = np.linspace(-180, 180, 600)
    for k, (wd, c) in enumerate(((0, BLUE), (30, GREEN), (60, ORANGE), (90, RED))):
        axs[1].plot(al, 1.5 * np.sin(np.radians(wd - al)), color=c, lw=2, label=f"ωt = {wd}°")
    axs[1].set_xlabel("space angle α (degrees)"); axs[1].set_ylabel("$F_R/F_m$"); axs[1].set_title("resultant MMF $\\frac{3}{2}F_m\\sin(\\omega t-\\alpha)$: a travelling wave of constant height")
    axs[1].legend(fontsize=8, ncol=2, loc="lower center"); axs[1].grid(alpha=0.3); axs[1].set_ylim(-1.8, 1.8)
    save(f, os.path.join(OUT, "T8-Q2-revolving-field.png"))


def fig_torque_slip():
    f, axs = plt.subplots(1, 2, figsize=(12, 4.2))
    s = np.linspace(-1.0, 2.0, 1200); s = s[np.abs(s) > 1e-3]
    ws = 2 * math.pi * 25; T = np.array([machine(x)[2] for x in s])
    ax = axs[0]
    ax.plot(s, T, color=BLUE, lw=2)
    ax.axhline(0, color="k", lw=0.8); ax.axvline(0, color="k", lw=0.8); ax.axvline(1, color=GREY, ls=":")
    ax.fill_between(s, T, 0, where=(s > 0) & (s < 1), color=BLUE, alpha=0.12)
    ax.text(0.45, 330, "motoring\n(0 < s < 1)", ha="center", fontsize=9); ax.text(-0.6, -330, "generating\n(s < 0, rotor above $n_s$)", ha="center", fontsize=9)
    ax.text(1.5, 130, "braking\n(s > 1, plugging)", ha="center", fontsize=9)
    ax.plot([0.1325], [469.7], "o", color=RED); ax.annotate("pull-out torque\n$s_m$ = 0.133, 469.7 N·m", (0.1325, 469.7), xytext=(0.35, 410), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.plot([1], [136.3], "o", color=ORANGE); ax.annotate("starting torque\n136.3 N·m", (1, 136.3), xytext=(1.2, 60), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.plot([0.04], [machine(0.04)[2]], "o", color=GREEN); ax.annotate("full load ($s$ = 0.04)", (0.04, machine(0.04)[2]), xytext=(0.2, -150), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_xlabel("slip s"); ax.set_ylabel("developed torque (N·m)"); ax.set_title("Q5: torque–slip characteristic (the Q11 motor)"); ax.grid(alpha=0.3)
    ax = axs[1]
    ss = np.linspace(0.005, 1, 500)
    for rx, c, lab in ((0, BLUE, "$R_{ext}$ = 0"), (0.5455, GREEN, "$R_{ext}$ = 0.545 Ω: max torque at start"), (1.5, ORANGE, "$R_{ext}$ = 1.5 Ω")):
        ax.plot(1 - ss, [machine(x, rext=rx * 1.44)[2] for x in ss], color=c, lw=2, label=lab)
    ax.set_xlabel("speed / synchronous speed = 1 − s"); ax.set_ylabel("torque (N·m)"); ax.set_title("more rotor resistance: same $T_{max}$, peak moves to lower speed"); ax.legend(fontsize=8); ax.grid(alpha=0.3)
    save(f, os.path.join(OUT, "T8-Q5-torque-slip.png"))


def fig_speeds():
    f, ax = plt.subplots(figsize=(7.6, 3.6))
    labels = ["stator field\nw.r.t. stator", "rotor\nw.r.t. stator", "stator field\nw.r.t. rotor", "rotor field\nw.r.t. rotor", "rotor field\nw.r.t. stator", "rotor field\nw.r.t. stator field"]
    vals = [1500, 1440, 60, 60, 1500, 0]
    cols = [BLUE, ORANGE, GREEN, GREEN, BLUE, GREY]
    ax.bar(range(6), vals, color=cols)
    for i, v in enumerate(vals): ax.text(i, v + 35, f"{v} rpm", ha="center", fontsize=9)
    ax.set_xticks(range(6)); ax.set_xticklabels(labels, fontsize=8); ax.set_ylim(0, 1750); ax.set_ylabel("speed (rpm)")
    ax.set_title("Q7: 4-pole, 50 Hz motor at 1440 rpm ($s=0.04$)"); ax.grid(axis="y", alpha=0.3)
    save(f, os.path.join(OUT, "T8-Q7-speeds.png"))


def fig_rotor_curves():
    s = np.linspace(0.005, 1, 400); E = 120; R2 = 0.2; X20 = 1.0; ws = 2 * math.pi * 25
    I = s * E / np.sqrt(R2 ** 2 + (s * X20) ** 2); pf = R2 / np.sqrt(R2 ** 2 + (s * X20) ** 2); T = 3 * I ** 2 * R2 / s / ws
    f, axs = plt.subplots(1, 3, figsize=(12.5, 3.5))
    axs[0].plot(s, I, color=BLUE, lw=2); axs[0].set_title("rotor current $I_2$ (A)"); axs[0].plot([0.04, 1], [23.53, 117.67], "o", color=RED)
    axs[1].plot(s, pf, color=GREEN, lw=2); axs[1].set_title("rotor power factor"); axs[1].plot([0.04, 1], [0.98, 0.196], "o", color=RED)
    axs[2].plot(s, T, color=ORANGE, lw=2); axs[2].set_title("torque (N·m)"); axs[2].plot([0.04, 1], [52.89, 52.89], "o", color=RED)
    axs[2].annotate("52.9 N·m at both", (0.04, 52.89), xytext=(0.2, 40), arrowprops=dict(arrowstyle="->"), fontsize=9)
    for a in axs: a.set_xlabel("slip s"); a.grid(alpha=0.3)
    save(f, os.path.join(OUT, "T8-Q8-rotor-vs-slip.png"))


def fig_power_flow():
    f, ax = plt.subplots(figsize=(9.6, 3.6))
    steps = [("input\n11200 W", 11200, BLUE), ("stator Cu\n388.8 W", -388.8, RED), ("core\n163.3 W", -163.3, RED), ("air-gap\n10648 W", 10648, GREEN), ("rotor Cu\n228 W", -228, RED), ("F & W\n420 W", -420, RED), ("shaft\n10000 W", 10000, ORANGE)]
    x = 0; level = 0
    for i, (lab, v, c) in enumerate(steps):
        if lab.startswith(("input", "air-gap", "shaft")):
            ax.bar(i, v, color=c); level = v
        else:
            ax.bar(i, -v, bottom=level + v, color=c); level += v
    ax.set_xticks(range(len(steps))); ax.set_xticklabels([s[0] for s in steps], fontsize=8); ax.set_ylim(9400, 11450); ax.set_ylabel("W")
    ax.set_title("Q9: power flow of the 10 kW induction motor at full load (η = 89.3 %)"); ax.grid(axis="y", alpha=0.3)
    save(f, os.path.join(OUT, "T8-Q9-power-flow.png"))


def fig_equiv():
    def circ(ax):
        wire(ax, (0, 0), (13.4, 0)); vsrc(ax, (0, 0), (0, 3), "$V_1$", plus=2, side=1, ac=True); wire(ax, (0, 3), (0.5, 3))
        res(ax, (0.5, 3), (2.7, 3), "$r_1$"); ind(ax, (2.7, 3), (4.9, 3), "$x_1$"); dot(ax, 5.6, 3); wire(ax, (4.9, 3), (5.6, 3))
        ind(ax, (5.6, 3), (5.6, 0), "$x_\\varphi$", side=-1)
        wire(ax, (5.6, 3), (6.3, 3)); ind(ax, (6.3, 3), (8.5, 3), "$x_2'$"); res(ax, (8.5, 3), (10.9, 3), "$r_2'/s$"); wire(ax, (10.9, 3), (11.6, 3)); wire(ax, (11.6, 3), (11.6, 0))
        arrow(ax, (1.0, 3.9), (2.2, 3.9), "$I_1$", off=0.3); arrow(ax, (6.5, 3.9), (7.7, 3.9), "$I_2'$", off=0.3)
        ax.annotate("", xy=(12.4, 2.95), xytext=(12.4, 0.05), arrowprops=dict(arrowstyle="<->", color=BLUE)); ax.text(12.6, 1.5, "$P_g$ drawn in $r_2'/s$", rotation=90, va="center", color=BLUE, fontsize=9)
        ax.text(8.5, 4.3, "$r_2'/s=r_2'+r_2'(1-s)/s$:  rotor copper + mechanical load", fontsize=9, color=GREEN)
    f, ax = plt.subplots(figsize=(9.8, 3.4)); circ(ax); finish(ax, (-1.6, 13.4), (-0.6, 4.7), "Q10, Q11: per-phase equivalent circuit referred to the stator"); save(f, os.path.join(OUT, "T8-Q10-Q11-equivalent-circuit.png"))


if __name__ == "__main__":
    fig_revolving(); fig_torque_slip(); fig_speeds(); fig_rotor_curves(); fig_power_flow(); fig_equiv()
    print("T8 figures written to", os.path.abspath(OUT))
