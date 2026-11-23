"""Tutorial 2 circuits and response plots -> Problems/Tutorial 2 - Transient Analysis of DC Circuits/assets/
Run:  python ee_figs_t2.py"""
import os
import math
import numpy as np
from ee_draw import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Problems", "Tutorial 2 - Transient Analysis of DC Circuits", "assets")
os.makedirs(OUT, exist_ok=True)


def sw(ax, p1, p2, closed=False, lab="", side=1):
    """single-pole switch drawn as a lever between p1 and p2 (horizontal)"""
    (x1, y1), (x2, y2) = p1, p2
    xm = (x1 + x2) / 2; w = (x2 - x1) * 0.28
    wire(ax, p1, (xm - w, y1)); wire(ax, (xm + w, y2), p2)
    dot(ax, xm - w, y1); dot(ax, xm + w, y2)
    if closed:
        wire(ax, (xm - w, y1), (xm + w, y2))
    else:
        wire(ax, (xm - w, y1), (xm + w * 0.7, y2 + 0.75 * abs(w)))
    if lab:
        ax.text(xm, y1 + 0.55 * side, lab, ha="center", fontsize=9)


def mk(name, xl, yl, title, draw, size=(7, 3.2)):
    f, ax = plt.subplots(figsize=size)
    draw(ax); finish(ax, xl, yl, title); save(f, os.path.join(OUT, name))


# ---------------------------------------------------------------- circuits
def c_q2(ax):
    wire(ax, (0, 0), (6, 0)); battery(ax, (0, 0), (0, 3), "$V_{in}$=15 V", plus=2, side=-1); wire(ax, (0, 3), (1, 3))
    res(ax, (1, 3), (4, 3), "20 Ω"); wire(ax, (1, 3), (1, 1.9)); cap(ax, (1, 1.9), (4, 1.9), "C", side=-1); wire(ax, (4, 1.9), (4, 3))
    dot(ax, 1, 3); dot(ax, 4, 3); wire(ax, (4, 3), (6, 3)); ind(ax, (6, 3), (6, 1.8), "L", side=1); res(ax, (6, 1.8), (6, 0), "10 Ω", side=1)
    arrow(ax, (0.25, 3.35), (0.95, 3.35), "$I_{in}$"); ax.text(2.5, 1.2, "$V_1$", color=BLUE, ha="center", fontsize=10)
    ax.text(7.2, 1.0, "$V_2$", color=BLUE, fontsize=10)


def c_q3(ax):
    wire(ax, (0, 0), (7.5, 0)); wire(ax, (0, 3), (7.5, 3)); isrc(ax, (0, 0), (0, 3), "$I_{in}$=2 A", side=-1)
    ind(ax, (3.5, 3), (3.5, 1.8), "5 mH", side=1); res(ax, (3.5, 1.8), (3.5, 0), "10 Ω", side=1)
    cap(ax, (6.5, 3), (6.5, 1.8), "25 µF", side=1); res(ax, (6.5, 1.8), (6.5, 0), "40 Ω", side=1)
    dot(ax, 3.5, 3); dot(ax, 6.5, 3); arrow(ax, (4.3, 2.8), (4.3, 2.1), "$I_1$"); arrow(ax, (7.3, 2.8), (7.3, 2.1), "$I_2$")
    arrow(ax, (1.6, 0.3), (1.6, 2.7), "$V_{in}$", c=RED)


def c_q5(ax):
    wire(ax, (0, 0), (8.2, 0)); isrc(ax, (0, 0), (0, 3), "2 A", side=-1); wire(ax, (0, 3), (1.8, 3)); dot(ax, 1.8, 3)
    res(ax, (1.8, 3), (1.8, 0), "12 Ω", side=-1); sw(ax, (1.8, 3), (3.4, 3), closed=True, lab="t = 0 (opens)")
    dot(ax, 3.4, 3); res(ax, (3.4, 3), (3.4, 0), "20 Ω", side=-1)
    wire(ax, (3.4, 3), (3.4, 4.4)); res(ax, (3.4, 4.4), (7.6, 4.4), "5 Ω"); wire(ax, (7.6, 4.4), (7.6, 3.4)); battery(ax, (7.6, 3.4), (7.6, 0), "20 V", plus=1, side=1)
    res(ax, (3.4, 3), (5.6, 3), "6 Ω"); ind(ax, (5.6, 3), (5.6, 0), "0.5 H", side=1); dot(ax, 5.6, 3)
    ax.text(6.3, 1.5, "+\n$v$\n−", fontsize=9, color=BLUE, ha="center", va="center")


def c_q6(ax):
    wire(ax, (0, 0), (8.6, 0)); isrc(ax, (0, 0), (0, 3), "10 mA", side=-1); wire(ax, (0, 3), (2, 3)); dot(ax, 2, 3)
    res(ax, (2, 3), (2, 0), "4 kΩ", side=-1)
    wire(ax, (2, 3), (4.4, 3)); dot(ax, 4.4, 3); res(ax, (4.4, 1.9), (4.4, 0), "4 kΩ", side=-1); dot(ax, 4.4, 1.9)
    wire(ax, (4.4, 3), (4.4, 3)); wire(ax, (6.2, 2.45), (4.4, 3), c="k"); ax.plot([4.4, 6.2], [1.9, 2.45], "k--", lw=1.0)
    ax.text(4.0, 3.3, "1", fontsize=9); ax.text(4.0, 1.5, "2", fontsize=9); ax.text(5.6, 2.9, "S", fontsize=9)
    wire(ax, (6.2, 2.45), (7.6, 2.45)); cap(ax, (7.6, 2.45), (7.6, 1.2), "10 µF", side=1); res(ax, (7.6, 1.2), (7.6, 0), "6 kΩ", side=1)
    arrow(ax, (6.7, 2.7), (7.3, 2.7), "$i_C$"); ax.text(8.4, 1.85, "+$v_C$", fontsize=9, color=BLUE, va="center")
    ax.text(5.9, 1.4, "t = 0", fontsize=8)


def c_q8(ax):
    wire(ax, (0, 0), (11.3, 0)); wire(ax, (0, 3), (2, 3)); cap(ax, (0, 3), (0, 0), "4 µF", side=-1); res(ax, (2, 3), (2, 0), "1250 Ω", side=-1); dot(ax, 2, 3)
    res(ax, (2, 3), (5, 3), "250 Ω"); dot(ax, 5, 3); wire(ax, (5, 3), (5, 2.5))
    # switch in the source branch (vertical)
    wire(ax, (5, 2.5), (5, 2.1)); ax.plot([5, 5.45], [2.1, 2.7], "k", lw=1.7); dot(ax, 5, 2.1); dot(ax, 5, 1.6)
    wire(ax, (5, 1.6), (5, 1.4)); battery(ax, (5, 1.4), (5, 0), "120 V", plus=1, side=1); ax.text(5.9, 2.2, "t = 0", fontsize=9)
    res(ax, (5, 3), (8, 3), "600 Ω"); dot(ax, 8, 3); res(ax, (8, 3), (8, 0), "2 kΩ", side=-1)
    res(ax, (8, 3), (10.6, 3), "100 Ω"); res(ax, (10.6, 3), (10.6, 0), "400 Ω", side=1); ax.text(11.5, 1.5, "+\n$v_o$\n−", fontsize=9, color=BLUE, ha="center", va="center")
    ax.text(-1.0, 1.5, "+\n$v_C$\n−", fontsize=9, color=BLUE, ha="center", va="center")


def c_q10(ax):
    wire(ax, (0, 0), (7.4, 0)); battery(ax, (0, 0), (0, 3), "100 V", plus=2, side=-1); wire(ax, (0, 3), (0.3, 3))
    sw(ax, (0.3, 3), (1.8, 3), closed=False, lab="S")
    res(ax, (1.8, 3), (4.2, 3), "50 Ω"); ind(ax, (4.2, 3), (6.6, 3), "0.1 H"); wire(ax, (6.6, 3), (7.4, 3)); cap(ax, (7.4, 3), (7.4, 0), "50 µF", side=1)
    arrow(ax, (0.45, 3.6), (1.35, 3.6), "$i$")


# ---------------------------------------------------------------- plots
def p_q1():
    t = np.array([0, 4, 8, 16.0])
    f, axs = plt.subplots(3, 2, figsize=(9.2, 7.2), sharex=True)
    i = [20, 20, 0, 0, -10, -10]; ti = [0, 4, 4, 8, 8, 16]
    axs[0, 0].plot(ti, i, color=BLUE, lw=2); axs[0, 0].set_ylabel("$i_C$ (mA)"); axs[0, 0].set_title("(a) capacitor, 8 µF")
    axs[1, 0].plot([0, 4, 8, 16], [0, 10, 10, 0], color=ORANGE, lw=2); axs[1, 0].set_ylabel("$v_C$ (V)")
    axs[2, 0].plot([0, 4, 4, 8, 8, 16], [0, 0.2, 0, 0, -0.1, 0], color=GREEN, lw=2); axs[2, 0].set_ylabel("$p$ (W)")
    v = [20, 20, 0, 0, -10, -10]
    axs[0, 1].plot(ti, v, color=BLUE, lw=2); axs[0, 1].set_ylabel("$v_L$ (mV)"); axs[0, 1].set_title("(b) inductor, 40 mH")
    axs[1, 1].plot([0, 4, 8, 16], [0, 2, 2, 0], color=ORANGE, lw=2); axs[1, 1].set_ylabel("$i_L$ (mA)")
    axs[2, 1].plot([0, 4, 4, 8, 8, 16], [0, 40, 0, 0, -20, 0], color=GREEN, lw=2); axs[2, 1].set_ylabel("$p$ (µW)")
    for a in axs.ravel(): a.grid(alpha=0.3)
    for a in axs[2]: a.set_xlabel("t (ms)")
    axs[0, 0].text(1, 14, "20 mA", fontsize=9); axs[1, 0].annotate("10 V", (4, 10), xytext=(4.3, 7), fontsize=9)
    axs[2, 0].annotate("0.2 W", (4, 0.2), xytext=(4.4, 0.16), fontsize=9); axs[2, 0].annotate("−0.1 W", (8, -0.1), xytext=(8.4, -0.08), fontsize=9)
    axs[2, 1].annotate("40 µW", (4, 40), xytext=(4.4, 32), fontsize=9); axs[2, 1].annotate("−20 µW", (8, -20), xytext=(8.4, -16), fontsize=9)
    save(f, os.path.join(OUT, "T2-Q1-waveforms.png"))


def p_q4():
    t = np.linspace(0, 0.1, 400); i = 30 * np.exp(-50 * t); v = 120 * np.exp(-50 * t); E = 0.5 * 0.08 * i ** 2
    f, axs = plt.subplots(1, 2, figsize=(10, 3.5))
    axs[0].plot(t * 1e3, i, color=BLUE, lw=2, label="$i=30e^{-50t}$ A"); axs[0].plot(t * 1e3, v / 4, color=ORANGE, lw=2, ls="--", label="$v/4$ (V ÷ 4)")
    axs[0].axvline(20, color="grey", ls=":"); axs[0].text(21, 25, "τ = 20 ms\n(36.8 %)", fontsize=9); axs[0].set_xlabel("t (ms)"); axs[0].legend(); axs[0].grid(alpha=0.3)
    axs[1].plot(t * 1e3, E, color=GREEN, lw=2); axs[1].axhline(18, color="grey", ls="--"); axs[1].plot([6.93], [18], "o", color=RED)
    axs[1].annotate("50 % of 36 J at 6.93 ms", (6.93, 18), xytext=(20, 24), arrowprops=dict(arrowstyle="->"), fontsize=9)
    axs[1].set_xlabel("t (ms)"); axs[1].set_ylabel("energy in L (J)"); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q4-decay-energy.png"))


def p_q5():
    t = np.linspace(0, 0.2, 400); iL = 1.6 + 0.4 * np.exp(-20 * t); v = -4 * np.exp(-20 * t)
    f, axs = plt.subplots(1, 2, figsize=(10, 3.4))
    axs[0].plot(t * 1e3, iL, color=BLUE, lw=2); axs[0].axhline(1.6, color="grey", ls="--"); axs[0].set_title("$i_L$: 2 A → 1.6 A, τ = 50 ms"); axs[0].set_xlabel("t (ms)"); axs[0].set_ylabel("A"); axs[0].grid(alpha=0.3)
    axs[1].plot(t * 1e3, v, color=ORANGE, lw=2); axs[1].set_title("$v=v_L=-4e^{-20t}$ V"); axs[1].set_xlabel("t (ms)"); axs[1].set_ylabel("V"); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q5-response.png"))


def p_q6():
    t = np.linspace(0, 0.5, 400); v = 40 * np.exp(-10 * t); i = -4 * np.exp(-10 * t)
    f, axs = plt.subplots(1, 2, figsize=(10, 3.4))
    axs[0].plot(t, v, color=BLUE, lw=2); axs[0].set_title("$v_C=40e^{-10t}$ V (τ = 0.1 s)"); axs[0].set_xlabel("t (s)"); axs[0].grid(alpha=0.3)
    axs[1].plot(t, i, color=ORANGE, lw=2); axs[1].set_title("$i_C=-4e^{-10t}$ mA (negative: discharging)"); axs[1].set_xlabel("t (s)"); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q6-response.png"))


def p_q7():
    t = np.linspace(0, 0.12, 800); i = 0.01601 * np.exp(-50 * t) * np.sin(312.25 * t); env = 0.01601 * np.exp(-50 * t)
    f, axs = plt.subplots(1, 2, figsize=(10.5, 3.6))
    axs[0].plot(t * 1e3, i * 1e3, color=BLUE, lw=2); axs[0].plot(t * 1e3, env * 1e3, color=GREY, ls="--"); axs[0].plot(t * 1e3, -env * 1e3, color=GREY, ls="--")
    axs[0].set_xlabel("t (ms)"); axs[0].set_ylabel("i (mA)"); axs[0].set_title("Q7: underdamped, $R=200\\ \\Omega<R_c=1265\\ \\Omega$"); axs[0].grid(alpha=0.3)
    L, C = 2, 5e-6; tt = np.linspace(0, 0.08, 1500)
    for R, c, lab in ((200, BLUE, "R = 200 Ω (under)"), (1264.9, GREEN, "R = 1265 Ω (critical)"), (3000, ORANGE, "R = 3000 Ω (over)")):
        a = R / (2 * L); w0 = 1 / math.sqrt(L * C)
        if R < 2 * math.sqrt(L / C) - 1e-6:
            wd = math.sqrt(w0 ** 2 - a ** 2); y = 10 / (wd * L) * np.exp(-a * tt) * np.sin(wd * tt)
        elif abs(R - 1264.9) < 1:
            y = 10 / L * tt * np.exp(-a * tt)
        else:
            s = math.sqrt(a ** 2 - w0 ** 2); s1, s2 = -a + s, -a - s; y = 10 / (L * (s1 - s2)) * (np.exp(s1 * tt) - np.exp(s2 * tt))
        axs[1].plot(tt * 1e3, y * 1e3, color=c, lw=2, label=lab)
    axs[1].set_xlabel("t (ms)"); axs[1].set_title("effect of the series resistance"); axs[1].legend(fontsize=8); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q7-damping.png"))


def p_q8_q9():
    t = np.linspace(0, 6e-3, 600)
    vc8 = 100 * np.exp(-t / 2.5e-3); vo8 = 25.6 * np.exp(-t / 2.5e-3)
    vc9 = 100 * (1 - np.exp(-t / 0.8333e-3)); vo9 = 38.4 * np.ones_like(t)
    f, axs = plt.subplots(1, 2, figsize=(10.5, 3.6))
    axs[0].plot(t * 1e3, vc8, color=BLUE, lw=2, label="$v_C$"); axs[0].plot(t * 1e3, vo8, color=ORANGE, lw=2, label="$v_o$ (after 0⁺)")
    axs[0].plot([0, 0], [38.4, 25.6], "o-", color=ORANGE, lw=1, ms=4); axs[0].plot([1.3], [59.45], "o", color=RED); axs[0].plot([1.3], [15.22], "o", color=RED)
    axs[0].annotate("59.45 V", (1.3, 59.45), xytext=(1.8, 66), fontsize=9); axs[0].annotate("15.22 V", (1.3, 15.22), xytext=(1.8, 22), fontsize=9)
    axs[0].set_title("Q8: switch opens, τ = 2.5 ms"); axs[0].set_xlabel("t (ms)"); axs[0].legend(); axs[0].grid(alpha=0.3)
    axs[1].plot(t * 1e3, vc9, color=BLUE, lw=2, label="$v_C$"); axs[1].plot(t * 1e3, vo9, color=ORANGE, lw=2, label="$v_o$")
    axs[1].plot([1.3], [78.99], "o", color=RED); axs[1].annotate("78.99 V", (1.3, 78.99), xytext=(1.8, 68), fontsize=9)
    axs[1].set_title("Q9: switch closes, τ = 0.833 ms"); axs[1].set_xlabel("t (ms)"); axs[1].legend(); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q8-Q9-response.png"))


def p_q10():
    R, L, C, V = 50, 0.1, 50e-6, 100
    a = R / (2 * L); wd = math.sqrt(1 / (L * C) - a ** 2); t = np.linspace(0, 0.03, 1500)
    i = V / (wd * L) * np.exp(-a * t) * np.sin(wd * t); vR = R * i
    vL = np.exp(-a * t) * (100 * np.cos(wd * t) - 67.42 * np.sin(wd * t)); vC = 100 - np.exp(-a * t) * (100 * np.cos(wd * t) + 67.42 * np.sin(wd * t))
    f, axs = plt.subplots(1, 2, figsize=(10.5, 3.7))
    axs[0].plot(t * 1e3, i, color=BLUE, lw=2); axs[0].set_title("current $i(t)$ (A)"); axs[0].set_xlabel("t (ms)"); axs[0].grid(alpha=0.3)
    axs[1].plot(t * 1e3, vR, label="$v_R$"); axs[1].plot(t * 1e3, vL, label="$v_L$"); axs[1].plot(t * 1e3, vC, label="$v_C$")
    axs[1].plot(t * 1e3, vR + vL + vC, "k--", lw=1, label="sum = 100 V"); axs[1].set_title("element voltages (KVL: they sum to 100 V)"); axs[1].set_xlabel("t (ms)"); axs[1].legend(fontsize=8, ncol=2); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q10-response.png"))
    # damping vs R
    f, ax = plt.subplots(figsize=(6.4, 3.4))
    for Rv, c, lab in ((20, BLUE, "R = 20 Ω ($\\zeta$=0.22)"), (50, GREEN, "R = 50 Ω ($\\zeta$=0.56)"), (89.44, ORANGE, "R = 89.4 Ω (critical)"), (200, RED, "R = 200 Ω (over)")):
        a2 = Rv / (2 * L); w0 = 1 / math.sqrt(L * C)
        if Rv < 89.43:
            w = math.sqrt(w0 ** 2 - a2 ** 2); y = 100 - np.exp(-a2 * t) * (100 * np.cos(w * t) + 100 * a2 / w * np.sin(w * t))
        elif abs(Rv - 89.44) < 0.1:
            y = 100 - 100 * np.exp(-a2 * t) * (1 + a2 * t)
        else:
            s = math.sqrt(a2 ** 2 - w0 ** 2); s1, s2 = -a2 + s, -a2 - s; y = 100 - 100 * (s1 * np.exp(s2 * t) - s2 * np.exp(s1 * t)) / (s1 - s2)
        ax.plot(t * 1e3, y, color=c, lw=2, label=lab)
    ax.axhline(100, color="grey", ls=":"); ax.set_xlabel("t (ms)"); ax.set_ylabel("$v_C$ (V)"); ax.set_title("Q10: capacitor voltage versus $R$ (step of 100 V)"); ax.legend(fontsize=8); ax.grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q10-damping-vs-R.png"))


def p_q11_q12():
    t = np.linspace(0, 0.6, 800); i = 28.87 * np.exp(-9 * t) * np.sin(12 * t + math.radians(20.27))
    f, ax = plt.subplots(figsize=(6.4, 3.4)); ax.plot(t, i, color=BLUE, lw=2); ax.plot(0, 10, "o", color=RED); ax.annotate("i(0) = 10 A", (0, 10), xytext=(0.08, 18), arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_xlabel("t (s)"); ax.set_ylabel("i (A)"); ax.set_title("Q11: $i(t)=28.87e^{-9t}\\sin(12t+20.27°)$"); ax.grid(alpha=0.3); save(f, os.path.join(OUT, "T2-Q11-response.png"))
    R, L, C = 5, 0.1e-3, 8e-6; a = 1 / (2 * R * C); w0 = 1 / math.sqrt(L * C); wd = math.sqrt(w0 ** 2 - a ** 2)
    t = np.linspace(0, 0.5e-3, 1500); v = 10 / (C * wd) * np.exp(-a * t) * np.sin(wd * t)
    th = math.acos(a / w0); k = 1 / math.sqrt(1 - (a / w0) ** 2)
    iL = 10 * (1 - k * np.exp(-a * t) * np.sin(wd * t + th)); iC = -10 * k * np.exp(-a * t) * np.sin(wd * t - th)
    iR = v / R
    f, axs = plt.subplots(1, 2, figsize=(10.5, 3.6))
    axs[0].plot(t * 1e6, v, color=BLUE, lw=2); axs[0].set_title("Q12: $v(t)$ (V)"); axs[0].set_xlabel("t (µs)"); axs[0].grid(alpha=0.3)
    axs[1].plot(t * 1e6, iR, label="$i_R$"); axs[1].plot(t * 1e6, iL, label="$i_L$"); axs[1].plot(t * 1e6, iC, label="$i_C$")
    axs[1].plot(t * 1e6, iR + iL + iC, "k--", lw=1, label="sum = 10 A"); axs[1].set_xlabel("t (µs)"); axs[1].set_title("branch currents (KCL)"); axs[1].legend(fontsize=8, ncol=2); axs[1].grid(alpha=0.3)
    save(f, os.path.join(OUT, "T2-Q12-response.png"))


if __name__ == "__main__":
    mk("T2-Q2-circuit.png", (-1.8, 8.4), (-0.6, 4.0), "Q2: DC steady state (C open, L short)", c_q2, (7.0, 3.0))
    mk("T2-Q3-circuit.png", (-1.8, 8.4), (-0.6, 3.9), "Q3: DC steady state with a current source", c_q3, (7.0, 2.8))
    mk("T2-Q5-circuit.png", (-1.5, 8.6), (-0.6, 5.0), "Q5: switch opens at t = 0", c_q5, (7.0, 4.2))
    mk("T2-Q6-circuit.png", (-1.5, 9.4), (-0.6, 3.9), "Q6: switch thrown from 1 to 2 at t = 0", c_q6, (7.2, 3.0))
    mk("T2-Q8-circuit.png", (-1.8, 12.2), (-0.6, 3.9), "Q8/Q9: the 120 V source is in the switched branch", c_q8, (8.6, 2.8))
    mk("T2-Q10-circuit.png", (-1.5, 9.0), (-0.6, 4.1), "Q10: series RLC step response", c_q10, (6.6, 3.0))
    p_q1(); p_q4(); p_q5(); p_q6(); p_q7(); p_q8_q9(); p_q10(); p_q11_q12()
    print("T2 figures written to", os.path.abspath(OUT))
