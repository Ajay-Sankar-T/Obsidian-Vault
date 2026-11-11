"""EE1100 Tutorial 6 (op-amps) and Tutorial 7 (transformers): every number in the solution notes is recomputed here.
   Run: python ee_t6_t7.py   (add --figs to redraw the figures into the tutorial folders' assets/)"""
import sys
import os
import numpy as np
from math import sqrt, pi, cos, sin, acos, atan2, degrees, radians

# ================================================================== Tutorial 6
def t6():
    r = {}
    # Q1
    r["Q1 gain"] = 4 / 2e-3                       # 4 V out for 2 mV in
    r["Q1 design Rf for Rg=1k (non-inverting)"] = (r["Q1 gain"] - 1) * 1e3
    # Q2 inverting
    r["Q2 gain"] = -1.2e6 / 15e3
    r["Q2 Vo (mV)"] = r["Q2 gain"] * 1.0
    # Q3 non-inverting 1 + 15/6.8
    r["Q3 gain"] = 1 + 15 / 6.8
    r["Q3 Vo"] = r["Q3 gain"] * -0.5
    # Q4 summer
    r["Q4 Vo"] = -60 * (0.3 / 15 + 0.5 / 25 + 0.8 / 32)
    # Q5 difference amplifier
    r["Q5 (a)(b)(c)(d) mV"] = [15 * (v2 - v1) for v1, v2 in ((4, 0), (0, 6), (40, 30), (25, 40))]
    # Q6 integrator
    R, C, Vi, t = 200e3, 2.5e-6, 0.75, 0.1
    r["Q6 Vo"] = -Vi * t / (R * C)
    # Q7 follower with finite gain, Ri, Ro
    A, Ri, Ro, Rs, RL, Vo = 1e5, 100e3, 100., 1e3, 10e3, 10.
    Io = Vo / RL
    vd = (Vo + Ro * Io) / A
    i_in = vd / Ri
    Vs = Rs * i_in + vd + Vo
    r["Q7 vd (V)"], r["Q7 Vs"], r["Q7 Vo/Vs"] = vd, Vs, Vo / Vs
    # closed form gain: Vo/Vs
    Z = (Rs + Ri) + 0   # series input path to the output node through Ri
    # Q8 photodiode
    Rf, R1, R2, Vo8 = 10e3, 75., 1e3, 8.
    ii = Vo8 / (Rf * R2 / R1)
    r["Q8 ii (uA)"] = ii * 1e6
    r["Q8 P (mW)"] = ii * 1e6 / 10
    # Q9
    vb = 3 * 10 / (5 + 10)
    va = vb
    vo = va - (3 - va) / 2e3 * 8e3
    r["Q9 vb"], r["Q9 vo"] = vb, vo
    r["Q9 i_4k (mA)"] = vo / 4e3 * 1e3
    r["Q9 i_8k feedback (mA)"] = (va - vo) / 8e3 * 1e3
    r["Q9 io op-amp output (mA)"] = r["Q9 i_4k (mA)"] - r["Q9 i_8k feedback (mA)"]
    # Q10: Vo = (1 + R2/R1) R4/(R3+R4) V2 - (R2/R1) V1 ; condition for V2 - V1
    # Q11: z = 2x - 3y with Rf/R1 = 3 and R3 = R4
    Rf, R1, R3, R4 = 30e3, 10e3, 10e3, 10e3
    g_inv, g_non = Rf / R1, (1 + Rf / R1) * R4 / (R3 + R4)
    r["Q11 coefficients (x, y)"] = (g_non, -g_inv)
    # Q12: non-inverting summer of four inputs
    r["Q12 gain with Rg=10k Rf=30k"] = (1 + 30 / 10) / 4
    return r


# ================================================================== Tutorial 7
def t7():
    r = {}
    # Q1
    r["Q1 turns (13 V/turn)"] = (2310 / 13, 220 / 13)
    r["Q1 area (13 V/turn, cm2)"] = 13 / (4.44 * 50 * 1.4) * 1e4
    r["Q1 area (12.22 V/turn, cm2)"] = (220 / 18) / (4.44 * 50 * 1.4) * 1e4
    r["Q1 turns with ratio 10.5"] = (189, 18)
    # Q2
    Ic = 361 / 2200
    Iphi = sqrt(0.6**2 - Ic**2)
    r["Q2 Ic, Iphi"] = (Ic, Iphi)
    I0 = complex(Ic, -Iphi)
    I2p = 6 * complex(0.8, -0.6)
    I1 = I0 + I2p
    r["Q2 I1, pf"] = (abs(I1), I1.real / abs(I1))
    # Q4
    a = 10
    r["Q4 a"] = (2.4 / a**2, 6 / a**2, 0.03 * a**2, 0.07 * a**2)
    Re1, Xe1 = 2.4 + 3, 6 + 7
    Re2, Xe2 = Re1 / a**2, Xe1 / a**2
    r["Q4 eq"] = (Re1, Xe1, Re2, Xe2)
    r["Q4 loss full load (W)"] = (33000 / 220)**2 * Re2
    Vsc = 160 * sqrt(Re2**2 + Xe2**2) * a
    r["Q4 Vsc (V), Psc (W)"] = (Vsc, 160**2 * Re2)
    # Q5
    Re2, Xe2 = 0.048 + 4.8 / 100, 0.112 + 11.2 / 100
    Z = complex(5 + Re2, 3.5 + Xe2)
    I = 250 / abs(Z)
    r["Q5a V2"] = I * abs(complex(5, 3.5))
    I2, ph = 40, acos(0.8)
    dR, dI = I2 * Re2 * 0.8 + I2 * Xe2 * 0.6, I2 * Xe2 * 0.8 - I2 * Re2 * 0.6
    r["Q5b V2 exact, approx"] = (sqrt(250**2 - dI**2) - dR, 250 - dR)
    # Q6
    Zl = (380 + 230j) / 100
    Zs = 0.2 + 0.7j
    I = 250 / (Zs + Zl)
    V2 = I * Zl
    Ish = 250 / 500 + 250 / (1j * 250)
    I1 = I + Ish
    P_out = abs(I)**2 * Zl.real
    P_in = (250 * I1.conjugate()).real
    r["Q6"] = dict(V2=abs(V2) * 1, I1=abs(I1) / 10, pf=I1.real / abs(I1), Pout=P_out, eta=P_out / P_in * 100, Pin=P_in)
    # Q7
    Ic, Iphi = 105 / 250, sqrt(1.4**2 - (105 / 250)**2)
    r["Q7 OC LV"] = (250 / Ic, 250 / Iphi)
    r["Q7 OC HV"] = (250 / Ic * 100, 250 / Iphi * 100)
    Zeq, Req = 104 / 8, 320 / 64
    Xeq = sqrt(Zeq**2 - Req**2)
    r["Q7 SC HV Zeq, Req, Xeq"] = (Zeq, Req, Xeq)
    r["Q7 per winding HV, LV"] = (Req / 2, Xeq / 2, Req / 2 / 100, Xeq / 2 / 100)
    # Q8
    Re2, Xe2 = 0.3 + 8 / 25, 0.7 + 17 / 25
    I2 = 20000 / 500
    for name, sgn in (("lag", 1), ("lead", -1)):
        dV = I2 * (Re2 * 0.8 + sgn * Xe2 * 0.6)
        Rx, Ix = I2 * (Re2 * 0.8 + sgn * Xe2 * 0.6), I2 * (Xe2 * 0.8 - sgn * Re2 * 0.6)
        V2x = sqrt(500**2 - Ix**2) - Rx
        r[f"Q8 {name}"] = dict(Re2=Re2, Xe2=Xe2, dV=dV, VR_pct=dV / 500 * 100, V2_approx=500 - dV, V2_exact=V2x, VR_exact=(500 - V2x) / 500 * 100)
    # Q9
    Pc, Psc_t, Isc_t, Vsc_t = 50., 45., 3., 60.
    Irated = 10000 / 2500
    Pcu_fl = Psc_t * (Irated / Isc_t)**2
    r["Q9 Pcu full load"] = Pcu_fl
    r["Q9 eta"] = {x: 10000 * x * 0.8 / (10000 * x * 0.8 + Pc + Pcu_fl * x**2) * 100 for x in (0.25, 0.5, 1, 1.25)}
    xo = sqrt(Pc / Pcu_fl)
    r["Q9 x_opt, kVA, eta_max"] = (xo, 10 * xo, 10000 * xo * 0.8 / (10000 * xo * 0.8 + 2 * Pc) * 100)
    Zeq = 60 / 3
    Req = 45 / 9
    Xeq = sqrt(Zeq**2 - Req**2)
    r["Q9 Req, Xeq (HV)"] = (Req, Xeq)
    IR, IX = Irated * Req, Irated * Xeq
    r["Q9 VR lag, lead (%)"] = ((IR * 0.8 + IX * 0.6) / 2500 * 100, (IR * 0.8 - IX * 0.6) / 2500 * 100)
    r["Q9 V2 lag, lead"] = (250 * (1 - (IR * 0.8 + IX * 0.6) / 2500), 250 * (1 - (IR * 0.8 - IX * 0.6) / 2500))
    # Q10
    Po = 100e3 * 0.8 * 0.8
    Pc = Po * (1 / 0.98 - 1) / 2
    Pcu_fl = Pc / 0.8**2
    re_pu = Pcu_fl / 100e3
    xe_pu = sqrt(0.05**2 - re_pu**2)
    r["Q10"] = dict(Pc=Pc, Pcu_fl=Pcu_fl, re_pct=re_pu * 100, xe_pct=xe_pu * 100, VR_pct=(re_pu * 0.8 + xe_pu * 0.6) * 100, lecture_VR=(re_pu * 0.8 + 0.05 * 0.6) * 100)
    # lecture 39 example
    r["L39 example"] = dict(Re2=0.1 + 2.5 / 25, Xe2=0.4 + 10 / 25)
    return r


# ================================================================== figures
HAVE_FIG = "--figs" in sys.argv
if HAVE_FIG:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    BLUE, ORANGE, RED, GREEN = "#2a6fd6", "#e8892b", "#d94a4a", "#2a9d4a"

    def wire(ax, *pts, **kw):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=kw.get("c", "k"), lw=kw.get("lw", 1.8), solid_capstyle="round")

    def res(ax, x1, y1, x2, y2, label="", pos="above", n=6):
        L = np.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        px, py = -uy, ux
        a, b = 0.2 * L, 0.8 * L
        pts = [(x1, y1), (x1 + ux * a, y1 + uy * a)]
        for k in range(n):
            t = a + (b - a) * (k + 0.5) / n
            s = 0.12 * (1 if k % 2 == 0 else -1)
            pts.append((x1 + ux * t + px * s, y1 + uy * t + py * s))
        pts += [(x1 + ux * b, y1 + uy * b), (x2, y2)]
        wire(ax, *pts)
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        off = 0.3 if pos == "above" else -0.35
        if abs(uy) > abs(ux):
            ax.text(xm + (0.3 if pos == "above" else -0.3), ym, label, ha="left" if pos == "above" else "right", va="center", fontsize=9)
        else:
            ax.text(xm, ym + off, label, ha="center", va="center", fontsize=9)

    def opamp(ax, x, y, w=1.6, h=1.5, flip=False, signs=("-", "+")):
        """triangle with inputs on the left at (x, y+h/4) and (x, y-h/4), output at (x+w, y)"""
        ax.add_patch(Polygon([(x, y + h / 2), (x, y - h / 2), (x + w, y)], closed=True, fill=False, lw=1.8))
        top, bot = (signs[0], signs[1]) if not flip else (signs[1], signs[0])
        ax.text(x + 0.18, y + h / 4, top, fontsize=11, va="center")
        ax.text(x + 0.18, y - h / 4, bot, fontsize=11, va="center")
        return (x, y + h / 4), (x, y - h / 4), (x + w, y)

    def gnd(ax, x, y):
        wire(ax, (x, y), (x, y - 0.25))
        for k, w in enumerate((0.3, 0.2, 0.1)):
            wire(ax, (x - w, y - 0.25 - 0.1 * k), (x + w, y - 0.25 - 0.1 * k))

    def dot(ax, x, y):
        ax.plot([x], [y], "ko", ms=4)

    def finish(ax, xl, yl, title=None):
        ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect("equal"); ax.axis("off")
        if title:
            ax.set_title(title, fontsize=10)

    def inverting(ax, x0, y0, R1, Rf, vin, vout, extra=""):
        inn, inp, out = opamp(ax, x0 + 3, y0)
        res(ax, x0, inn[1], x0 + 2, inn[1], R1)  # R1
        wire(ax, (x0 + 2, inn[1]), (inn[0], inn[1]))
        dot(ax, x0 + 2.4, inn[1])
        wire(ax, (x0 + 2.4, inn[1]), (x0 + 2.4, y0 + 1.6)); wire(ax, (x0 + 2.4, y0 + 1.6), (out[0] + 0.6, y0 + 1.6))
        res(ax, x0 + 2.4, y0 + 1.6, out[0] + 0.6, y0 + 1.6, Rf)
        wire(ax, (out[0] + 0.6, y0 + 1.6), (out[0] + 0.6, out[1])); dot(ax, out[0] + 0.6, out[1])
        wire(ax, out, (out[0] + 1.3, out[1]))
        wire(ax, inp, (inp[0] - 0.6, inp[1])); gnd(ax, inp[0] - 0.6, inp[1])
        ax.text(x0 - 0.3, inn[1], vin, ha="right", va="center", fontsize=10)
        ax.text(out[0] + 1.4, out[1], vout, ha="left", va="center", fontsize=10)
        ax.plot([x0], [inn[1]], "o", mfc="w", mec="k", ms=5); ax.plot([out[0] + 1.3], [out[1]], "o", mfc="w", mec="k", ms=5)

    def fig_q1():
        t = np.array([0, 1, 2, 4, 5])
        vin = np.array([0, 2, 0, 2, 0])
        fig, axs = plt.subplots(1, 3, figsize=(13, 3.6))
        ax = axs[0]
        ax.plot(t, vin, color=BLUE, lw=2); ax.set_title("input $v_i$ (mV)"); ax.set_xlabel("t (µs)"); ax.grid(alpha=0.3)
        ax = axs[1]
        ax.plot(t, vin * 2000 / 1000, color=ORANGE, lw=2); ax.set_title("output $v_o$ (V) = 2000 × input"); ax.set_xlabel("t (µs)"); ax.grid(alpha=0.3)
        ax = axs[2]
        v = np.linspace(0, 2, 5)
        ax.plot(v, 2 * v, color=GREEN, lw=2, marker="o"); ax.set_title("transfer line $v_o=2000\\,v_i$: straight, through 0\n⇒ linear"); ax.set_xlabel("$v_i$ (mV)"); ax.set_ylabel("$v_o$ (V)"); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q1-waveforms.png", dpi=150); plt.close(fig)
        # design: non-inverting stage
        fig, ax = plt.subplots(figsize=(7.2, 3.6))
        inn, inp, out = opamp(ax, 3, 0)
        wire(ax, inp, (0.6, inp[1])); ax.plot([0.6], [inp[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.4, inp[1], "$v_i$", ha="right", va="center")
        wire(ax, inn, (2, inn[1])); dot(ax, 2, inn[1])
        res(ax, 2, inn[1], 2, -2.4, "$R_g$ = 1 kΩ"); gnd(ax, 2, -2.4)
        wire(ax, (2, inn[1]), (2, 1.8)); wire(ax, (2, 1.8), (5.8, 1.8)); res(ax, 2, 1.8, 5.8, 1.8, "$R_f$ = 1.999 MΩ  (2 MΩ)")
        wire(ax, (5.8, 1.8), (5.8, out[1])); dot(ax, 5.8, out[1]); wire(ax, out, (6.7, out[1])); ax.plot([6.7], [out[1]], "o", mfc="w", mec="k", ms=5); ax.text(6.85, 0, "$v_o$", va="center")
        finish(ax, (0, 7.5), (-3.2, 2.6), "Q1: non-inverting amplifier, gain $1+R_f/R_g\\approx2000$")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q1-design.png", dpi=150); plt.close(fig)

    def fig_q2_q3():
        fig, axs = plt.subplots(1, 2, figsize=(13, 3.8))
        inverting(axs[0], 0, 0, "$R_1$ = 15 kΩ", "$R_2$ = 1.2 MΩ", "$V_i$", "$V_o$")
        finish(axs[0], (-1.5, 8.5), (-2.5, 2.8), "Q2: inverting, $A_v=-R_2/R_1=-80$")
        ax = axs[1]
        inn, inp, out = opamp(ax, 3, 0)
        wire(ax, inp, (0.6, inp[1])); ax.plot([0.6], [inp[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.4, inp[1], "input", ha="right", va="center")
        wire(ax, inn, (2, inn[1])); dot(ax, 2, inn[1])
        res(ax, 2, inn[1], 2, -2.4, "6.8 kΩ"); gnd(ax, 2, -2.4)
        wire(ax, (2, inn[1]), (2, 1.8)); wire(ax, (2, 1.8), (5.8, 1.8)); res(ax, 2, 1.8, 5.8, 1.8, "15 kΩ")
        wire(ax, (5.8, 1.8), (5.8, out[1])); dot(ax, 5.8, out[1]); wire(ax, out, (6.7, out[1])); ax.plot([6.7], [out[1]], "o", mfc="w", mec="k", ms=5)
        finish(ax, (0, 7.5), (-3.2, 2.6), "Q3: non-inverting, $A_v=1+15/6.8=3.206$")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q2-Q3-circuits.png", dpi=150); plt.close(fig)

    def fig_q4_q5():
        fig, axs = plt.subplots(1, 2, figsize=(13, 4.6))
        ax = axs[0]
        inn, inp, out = opamp(ax, 4, 0, h=1.8)
        ys = [1.4, 0.4, -0.6]
        labs = ["15 kΩ", "25 kΩ", "32 kΩ"]; vs = ["0.3 V", "0.5 V", "0.8 V"]
        for y_, l, v in zip(ys, labs, vs):
            ax.plot([0], [y_], "o", mfc="w", mec="k", ms=5); ax.text(-0.2, y_, v, ha="right", va="center", fontsize=9)
            res(ax, 0, y_, 2.2, y_, l)
            wire(ax, (2.2, y_), (2.8, y_))
        wire(ax, (2.8, 1.4), (2.8, -0.6)); dot(ax, 2.8, 0.45); wire(ax, (2.8, inn[1]), inn)
        wire(ax, (2.8, inn[1]), (2.8, 2.5)); wire(ax, (2.8, 2.5), (6.9, 2.5)); res(ax, 2.8, 2.5, 6.9, 2.5, "60 kΩ")
        wire(ax, (6.9, 2.5), (6.9, 0)); dot(ax, 6.9, 0); wire(ax, out, (7.8, 0)); ax.plot([7.8], [0], "o", mfc="w", mec="k", ms=5); ax.text(8, 0, "$V_o=-3.9$ V", va="center")
        wire(ax, inp, (3.2, inp[1])); gnd(ax, 3.2, inp[1])
        finish(ax, (-1.8, 9.6), (-2.2, 3.2), "Q4: inverting summer $V_o=-R_f\\sum V_k/R_k$")
        ax = axs[1]
        inn, inp, out = opamp(ax, 5, 0)
        res(ax, 1, inn[1], 3.6, inn[1], "8 kΩ"); wire(ax, (3.6, inn[1]), inn); dot(ax, 3.6, inn[1])
        wire(ax, (3.6, inn[1]), (3.6, 1.8)); wire(ax, (3.6, 1.8), (7.4, 1.8)); res(ax, 3.6, 1.8, 7.4, 1.8, "120 kΩ")
        wire(ax, (7.4, 1.8), (7.4, 0)); dot(ax, 7.4, 0); wire(ax, out, (8.2, 0)); ax.plot([8.2], [0], "o", mfc="w", mec="k", ms=5)
        ax.plot([1], [inn[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.8, inn[1], "$V_1$", ha="right", va="center")
        res(ax, 1, inp[1], 3.6, inp[1], "8 kΩ"); wire(ax, (3.6, inp[1]), inp); dot(ax, 3.6, inp[1])
        ax.plot([1], [inp[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.8, inp[1], "$V_2$", ha="right", va="center")
        res(ax, 3.6, inp[1], 3.6, -2.4, "120 kΩ"); gnd(ax, 3.6, -2.4)
        ax.text(8.4, 0, "$V_o=15(V_2-V_1)$", va="center")
        finish(ax, (-0.2, 11), (-3.2, 2.6), "Q5: difference amplifier, gain $R_f/R=15$")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q4-Q5-circuits.png", dpi=150); plt.close(fig)

    def fig_q6():
        fig, axs = plt.subplots(1, 2, figsize=(12.5, 3.8))
        ax = axs[0]
        inn, inp, out = opamp(ax, 3.4, 0)
        ax.plot([0], [inn[1]], "o", mfc="w", mec="k", ms=5); ax.text(-0.2, inn[1], "$V_i$", ha="right", va="center")
        res(ax, 0, inn[1], 2.2, inn[1], "R = 200 kΩ"); wire(ax, (2.2, inn[1]), inn); dot(ax, 2.2, inn[1])
        wire(ax, (2.2, inn[1]), (2.2, 1.8)); wire(ax, (2.2, 1.8), (3.3, 1.8))
        wire(ax, (3.3, 1.8), (3.3, 2.15)); wire(ax, (3.9, 1.8), (3.9, 2.15)); wire(ax, (3.1, 1.8), (3.1, 1.8))
        ax.plot([3.0, 4.2], [2.0, 2.0], alpha=0)  # keep extents
        wire(ax, (3.2, 2.2), (3.2, 1.4)); wire(ax, (3.6, 2.2), (3.6, 1.4)); wire(ax, (2.2, 1.8), (3.2, 1.8)); wire(ax, (3.6, 1.8), (5.8, 1.8)); ax.text(3.4, 2.6, "C = 2.5 µF", ha="center", fontsize=9)
        wire(ax, (5.8, 1.8), (5.8, 0)); dot(ax, 5.8, 0); wire(ax, out, (6.6, 0)); ax.plot([6.6], [0], "o", mfc="w", mec="k", ms=5); ax.text(6.8, 0, "$V_o$", va="center")
        wire(ax, inp, (2.9, inp[1])); gnd(ax, 2.9, inp[1])
        finish(ax, (-1.2, 8), (-2.2, 3.2), "Q6: integrator, $V_o=-\\frac{1}{RC}\\int V_i\\,dt$")
        ax = axs[1]
        tt = np.linspace(0, 0.3, 100)
        ax.plot(tt * 1e3, -0.75 * tt / 0.5, color=BLUE, lw=2)
        ax.plot([100], [-0.15], "o", color=RED); ax.annotate("100 ms: $-0.15$ V", (100, -0.15), xytext=(130, -0.05), arrowprops=dict(arrowstyle="->"))
        ax.set_xlabel("t (ms)"); ax.set_ylabel("$V_o$ (V)"); ax.set_title("ramp of slope $-V_i/RC=-1.5$ V/s"); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q6-integrator.png", dpi=150); plt.close(fig)

    def fig_q9():
        fig, ax = plt.subplots(figsize=(8.5, 4.4))
        inn, inp, out = opamp(ax, 5, 0, h=1.8)
        # source
        ax.add_patch(plt.Circle((0.4, -1.6), 0.45, fill=False, lw=1.8)); ax.text(0.4, -1.6, "3 V", ha="center", va="center", fontsize=9)
        wire(ax, (0.4, -1.15), (0.4, 2.2)); wire(ax, (0.4, -2.05), (0.4, -3.2)); gnd(ax, 0.4, -3.2)
        pass
        # 2k from top node to inverting node
        res(ax, 0.4, 1.0, 3.6, 1.0, "2 kΩ"); wire(ax, (0.4, 1.0), (0.4, 2.2))
        wire(ax, (3.6, 1.0), inn[:1] + (1.0,)); wire(ax, (3.6, 1.0), (3.6, inn[1])); wire(ax, (3.6, inn[1]), inn); dot(ax, 3.6, 1.0)
        ax.text(3.7, inn[1] + 0.4, "$v_a=2$ V", fontsize=9)
        wire(ax, (3.6, 1.0), (3.6, 2.4)); wire(ax, (3.6, 2.4), (7.6, 2.4)); res(ax, 3.6, 2.4, 7.6, 2.4, "8 kΩ")
        wire(ax, (7.6, 2.4), (7.6, 0)); dot(ax, 7.6, 0); wire(ax, out, (7.6, 0))
        res(ax, 7.6, 0, 7.6, -2.6, "4 kΩ", pos="above"); wire(ax, (7.6, -2.6), (7.6, -3.2)); gnd(ax, 7.6, -3.2)
        ax.text(7.9, 0.5, "$v_o=-2$ V", fontsize=9)
        # 5k to vb, 10k to ground
        res(ax, 0.4, -0.45, 3.6, -0.45, "5 kΩ"); wire(ax, (0.4, -0.45), (0.4, 1.0)); wire(ax, (3.6, -0.45), (3.6, inp[1])); wire(ax, (3.6, inp[1]), inp); dot(ax, 3.6, -0.45)
        ax.text(1.0, -1.45, r"$v_b = 3\cdot\frac{10}{15} = 2$ V", fontsize=9)
        res(ax, 3.6, -0.45, 3.6, -2.7, "10 kΩ", pos="below"); gnd(ax, 3.6, -2.7)
        finish(ax, (-0.8, 9.8), (-4, 3.2), "Q9: $v_a=v_b$; KCL at $v_a$: $\\frac{3-2}{2}=\\frac{2-v_o}{8}$ mA  ⇒  $v_o=-2$ V")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q9-circuit.png", dpi=150); plt.close(fig)

    def fig_q10_q12():
        fig, axs = plt.subplots(1, 2, figsize=(13, 4.8))
        ax = axs[0]
        inn, inp, out = opamp(ax, 5, 0)
        ax.plot([0.5], [inn[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.3, inn[1], "$V_1$", ha="right", va="center")
        res(ax, 0.5, inn[1], 3.6, inn[1], "$R_1$"); wire(ax, (3.6, inn[1]), inn); dot(ax, 3.6, inn[1])
        wire(ax, (3.6, inn[1]), (3.6, 1.8)); wire(ax, (3.6, 1.8), (7.4, 1.8)); res(ax, 3.6, 1.8, 7.4, 1.8, "$R_2$")
        wire(ax, (7.4, 1.8), (7.4, 0)); dot(ax, 7.4, 0); wire(ax, out, (8.2, 0)); ax.plot([8.2], [0], "o", mfc="w", mec="k", ms=5); ax.text(8.4, 0, "$V_o$", va="center")
        ax.plot([0.5], [inp[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.3, inp[1], "$V_2$", ha="right", va="center")
        res(ax, 0.5, inp[1], 3.6, inp[1], "$R_3$"); wire(ax, (3.6, inp[1]), inp); dot(ax, 3.6, inp[1])
        res(ax, 3.6, inp[1], 3.6, -2.4, "$R_4$"); gnd(ax, 3.6, -2.4)
        finish(ax, (-0.4, 9.4), (-3.2, 2.6))
        ax.set_title("Q10: $V_o=\\frac{R_2}{R_1}\\,(V_2-V_1)$ when $\\frac{R_2}{R_1}=\\frac{R_4}{R_3}$\n($V_o=V_2-V_1$ for $R_1=R_2$, $R_3=R_4$)", fontsize=10)
        ax = axs[1]
        inn, inp, out = opamp(ax, 5, 0)
        ax.plot([0.5], [inn[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.3, inn[1], "$y$", ha="right", va="center")
        res(ax, 0.5, inn[1], 3.6, inn[1], "10 kΩ"); wire(ax, (3.6, inn[1]), inn); dot(ax, 3.6, inn[1])
        wire(ax, (3.6, inn[1]), (3.6, 1.8)); wire(ax, (3.6, 1.8), (7.4, 1.8)); res(ax, 3.6, 1.8, 7.4, 1.8, "30 kΩ")
        wire(ax, (7.4, 1.8), (7.4, 0)); dot(ax, 7.4, 0); wire(ax, out, (8.2, 0)); ax.plot([8.2], [0], "o", mfc="w", mec="k", ms=5); ax.text(8.4, 0, "$z=2x-3y$", va="center")
        ax.plot([0.5], [inp[1]], "o", mfc="w", mec="k", ms=5); ax.text(0.3, inp[1], "$x$", ha="right", va="center")
        res(ax, 0.5, inp[1], 3.6, inp[1], "10 kΩ"); wire(ax, (3.6, inp[1]), inp); dot(ax, 3.6, inp[1])
        res(ax, 3.6, inp[1], 3.6, -2.4, "10 kΩ"); gnd(ax, 3.6, -2.4)
        finish(ax, (-0.4, 11), (-3.2, 2.6))
        ax.set_title("Q11: one-stage design, $z=4\\cdot\\frac{1}{2}\\,x-3y$", fontsize=10)
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q10-Q11-circuits.png", dpi=150); plt.close(fig)
        # Q12
        fig, ax = plt.subplots(figsize=(8.2, 4.6))
        inn, inp, out = opamp(ax, 5.2, 0, h=2.0)
        for k, y_ in enumerate((1.9, 0.9, -0.1, -1.1)):
            ax.plot([0], [y_], "o", mfc="w", mec="k", ms=5); ax.text(-0.2, y_, f"$v_{k + 1}$", ha="right", va="center")
            res(ax, 0, y_, 2.2, y_, "10 kΩ")
            wire(ax, (2.2, y_), (2.9, y_))
        wire(ax, (2.9, 1.9), (2.9, -1.1)); dot(ax, 2.9, inp[1]); wire(ax, (2.9, inp[1]), inp)
        wire(ax, inn, (4.2, inn[1])); dot(ax, 4.2, inn[1])
        res(ax, 4.2, inn[1], 4.2, -2.4, "$R_g$ = 10 kΩ"); gnd(ax, 4.2, -2.4)
        wire(ax, (4.2, inn[1]), (4.2, 2.8)); wire(ax, (4.2, 2.8), (7.8, 2.8)); res(ax, 4.2, 2.8, 7.8, 2.8, "$R_f$ = 30 kΩ")
        wire(ax, (7.8, 2.8), (7.8, 0)); dot(ax, 7.8, 0); wire(ax, out, (8.6, 0)); ax.plot([8.6], [0], "o", mfc="w", mec="k", ms=5); ax.text(8.8, 0, "$v_o=\\sum v_k$", va="center")
        finish(ax, (-1, 11), (-3.4, 3.6), "Q12: non-inverting summer: $v_+=\\frac{1}{4}\\sum v_k$, gain $1+R_f/R_g=4$")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q12-summer.png", dpi=150); plt.close(fig)

    def fig_q7_q8():
        fig, ax = plt.subplots(figsize=(8.6, 4.2))
        # equivalent model of follower
        ax.text(0.0, 2.0, "$R_s$ = 1 kΩ", fontsize=9, ha="center")
        ax.plot([-1], [1.5], "o", mfc="w", mec="k", ms=5); ax.text(-1.2, 1.5, "$V_s$", ha="right", va="center")
        res(ax, -1, 1.5, 1.4, 1.5, "$R_s$"); wire(ax, (1.4, 1.5), (3.0, 1.5)); dot(ax, 3.0, 1.5)
        res(ax, 3.0, 1.5, 3.0, -0.8, "$R_i$ = 100 kΩ"); wire(ax, (3.0, -0.8), (3.0, -1.2)); dot(ax, 3.0, -1.2)
        ax.add_patch(plt.Circle((5.3, -0.4), 0.5, fill=False, lw=1.8)); ax.text(5.3, -0.4, "$Av_d$", ha="center", va="center", fontsize=9)
        wire(ax, (3.0, -1.2), (5.3, -1.2), (5.3, -0.9)); wire(ax, (5.3, 0.1), (5.3, 1.5)); res(ax, 5.3, 1.5, 7.3, 1.5, "$R_o$ = 100 Ω")
        dot(ax, 7.9, 1.5); wire(ax, (7.3, 1.5), (9.2, 1.5))
        res(ax, 9.2, 1.5, 9.2, -1.2, "$R_L$ = 10 kΩ"); wire(ax, (9.2, -1.2), (3.0, -1.2)); ax.text(9.5, 0.2, "$V_o$", fontsize=10)
        wire(ax, (3.0, -1.2), (3.0, -2.2)); dot(ax, 3.0, -1.2)
        ax.text(3.2, -2.5, "(inverting input tied to the output: $v_d=v_+-v_o$)", fontsize=8.5)
        ax.set_xlim(-2.4, 10.5); ax.set_ylim(-3, 2.6); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("Q7: non-ideal follower model ($A=10^5$, $R_i$, $R_o$ finite)", fontsize=10)
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q7-model.png", dpi=150); plt.close(fig)
        fig, ax = plt.subplots(figsize=(9.2, 3.6))
        inn, inp, out = opamp(ax, 4, 0)
        ax.annotate("", xy=(0.2, 1.4), xytext=(1.6, 2.4), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2)); ax.text(1.0, 2.5, "light", color=ORANGE, ha="center")
        ax.add_patch(Polygon([(1.4, 0.9), (2.0, 0.9), (1.7, 0.3)], closed=True, fill=False, lw=1.8)); wire(ax, (1.4, 0.3), (2.0, 0.3)); wire(ax, (1.7, 0.9), (1.7, inn[1]), inn); wire(ax, (1.7, 0.3), (1.7, -0.3)); gnd(ax, 1.7, -0.3)
        dot(ax, 3.0, inn[1]); wire(ax, (3.0, inn[1]), (3.0, 1.8)); wire(ax, (3.0, 1.8), (6.2, 1.8)); res(ax, 3.0, 1.8, 6.2, 1.8, "$R_f$ = 10 kΩ")
        wire(ax, (6.2, 1.8), (6.2, 0)); dot(ax, 6.2, 0); wire(ax, out, (6.2, 0)); wire(ax, inp, (3.2, inp[1])); gnd(ax, 3.2, inp[1])
        res(ax, 6.2, 0, 8.4, 0, "$R_1$ = 75 Ω")
        inn2, inp2, out2 = opamp(ax, 8.4, 0)
        wire(ax, (8.4, 0), (8.4, inn2[1])); wire(ax, (8.4, inn2[1]), inn2); wire(ax, inp2, (8.0, inp2[1])); gnd(ax, 8.0, inp2[1])
        wire(ax, (8.4, inn2[1]), (8.4, 1.8)); wire(ax, (8.4, 1.8), (11.0, 1.8)); res(ax, 8.4, 1.8, 11.0, 1.8, "$R_2$ = 1 kΩ")
        wire(ax, (11.0, 1.8), (11.0, 0)); dot(ax, 11.0, 0); wire(ax, out2, (11.8, 0)); ax.plot([11.8], [0], "o", mfc="w", mec="k", ms=5); ax.text(12.0, 0, "$V_0$", va="center")
        ax.text(1.2, -1.0, "$i_i$", fontsize=9)
        finish(ax, (-0.5, 13), (-2.2, 3.3), r"Q8: stage 1 gives $V_1=-R_f\,i_i$, stage 2 gives $V_0=-\frac{R_2}{R_1}V_1$, so $V_0=\frac{R_fR_2}{R_1}\,i_i$")
        fig.tight_layout(); fig.savefig(OUT6 + "/T6-Q8-circuit.png", dpi=150); plt.close(fig)

    def fig_t7():
        # Q6 equivalent circuit
        fig, ax = plt.subplots(figsize=(8.6, 3.6))
        wire(ax, (0, 2), (2.2, 2)); wire(ax, (0, -0.6), (6.2, -0.6)); ax.text(-0.15, 0.7, "$V_1$", ha="right")
        dot(ax, 2.2, 2); dot(ax, 2.2, -0.6)
        res(ax, 2.2, 2, 2.2, 0.8, "500 Ω"); wire(ax, (2.2, 0.8), (2.2, 0.6));
        res(ax, 2.2, 0.6, 2.2, -0.6, "")
        ax.text(2.0, 1.4, "$R_c$ = 500 Ω", ha="right", fontsize=9); ax.text(2.0, 0.0, "$jX_m$ = j250 Ω", ha="right", fontsize=9)
        res(ax, 2.2, 2, 4.2, 2, "0.2 Ω"); res(ax, 4.2, 2, 6.2, 2, "j0.7 Ω")
        wire(ax, (6.2, 2), (6.4, 2)); wire(ax, (6.2, -0.6), (6.4, -0.6))
        res(ax, 6.2, 2, 6.2, -0.6, "$Z_L'$ = 3.8 + j2.3 Ω")
        ax.text(0.0, -1.3, "referred to the 250 V (LT) side; $Z_L'=(380+j230)/10^2$", fontsize=8.5)
        finish(ax, (-1.4, 8.8), (-1.8, 2.8), "T7 Q6: equivalent circuit referred to the low-tension side")
        fig.tight_layout(); fig.savefig(OUT7 + "/T7-Q6-circuit.png", dpi=150); plt.close(fig)
        # Q7 exact equivalent circuit, LV side
        fig, ax = plt.subplots(figsize=(10, 3.8))
        wire(ax, (0, 2), (1.0, 2)); res(ax, 1.0, 2, 3.4, 2, "0.025 Ω"); res(ax, 3.4, 2, 5.8, 2, "j0.06 Ω")
        dot(ax, 5.8, 2); wire(ax, (5.8, 2), (6.2, 2)); wire(ax, (0, -0.8), (13.0, -0.8)); dot(ax, 5.8, -0.8)
        res(ax, 5.8, 2, 5.8, 0.6, "595.2 Ω", pos="below"); wire(ax, (5.8, 0.6), (5.8, 0.4)); res(ax, 5.8, 0.4, 5.8, -0.8, "j187.3 Ω", pos="below")
        wire(ax, (5.8, 2), (7.0, 2)); res(ax, 7.0, 2, 9.4, 2, "0.025 Ω"); res(ax, 9.4, 2, 11.8, 2, "j0.06 Ω"); wire(ax, (11.8, 2), (12.4, 2))
        ax.text(3.0, 3.0, "primary leakage (referred to LV)", fontsize=8.5, ha="center"); ax.text(9.6, 3.0, "secondary leakage", fontsize=8.5, ha="center"); ax.text(12.5, 2.0, "ideal 1:1", fontsize=8.5, va="center")
        ax.text(0.1, 0.6, "$V_1'$ ", fontsize=10)
        pass
        finish(ax, (-0.8, 13.6), (-1.5, 3.8), "T7 Q7: exact equivalent circuit referred to the LV side (series impedance split equally)")
        fig.tight_layout(); fig.savefig(OUT7 + "/T7-Q7-circuit.png", dpi=150); plt.close(fig)
        # Q8 regulation phasor diagrams  and  Q9 efficiency curve
        fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.3))
        ax = axs[0]
        x = np.linspace(0, 1.25, 200)
        eta = 10000 * x * 0.8 / (10000 * x * 0.8 + 50 + 80 * x**2) * 100
        ax.plot(x, eta, color=BLUE, lw=2)
        xo = sqrt(50 / 80)
        ax.plot([xo], [10000 * xo * 0.8 / (10000 * xo * 0.8 + 100) * 100], "o", color=RED)
        ax.annotate(f"max at {xo:.3f} of full load\n7.905 kVA, 98.44 %", (xo, 98.44), xytext=(0.15, 98.0), arrowprops=dict(arrowstyle="->"))
        for xx in (0.25, 0.5, 1, 1.25):
            e = 10000 * xx * 0.8 / (10000 * xx * 0.8 + 50 + 80 * xx**2) * 100
            ax.plot([xx], [e], "s", color=GREEN); ax.text(xx, e - 0.45, f"{e:.2f}", ha="center", fontsize=8)
        ax.set_xlabel("load / rated load"); ax.set_ylabel("efficiency (%)"); ax.set_title("T7 Q9: efficiency at 0.8 pf, core loss 50 W, copper loss 80 W at full load"); ax.grid(alpha=0.3); ax.set_ylim(96, 99)
        ax.title.set_fontsize(9)
        ax = axs[1]
        I = 40.0; Re, Xe = 0.62, 1.38
        for name, sg, col in (("0.8 lag", 1, RED), ("0.8 lead", -1, GREEN)):
            ph = acos(0.8) * sg
            I2 = I * complex(cos(ph), -sin(ph))   # lag: current behind V2
            V2 = 450
            E = V2 + I2 * complex(Re, Xe)
            ax.annotate("", xy=(V2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5)) if sg == 1 else None
            pts = [0, V2, V2 + I2.real * Re - I2.imag * 0 * 0]
            a = complex(V2, 0)
            b = a + I2 * Re
            c = b + I2 * complex(0, Xe)
            ax.plot([0, a.real], [0, a.imag], color="k", lw=1.5)
            ax.plot([a.real, b.real, c.real], [a.imag, b.imag, c.imag], color=col, lw=2, label=f"{name}: $E_2=$ {abs(c):.1f} V")
            ax.plot([0, c.real], [0, c.imag], "--", color=col, lw=1)
        ax.set_aspect("equal"); ax.legend(fontsize=8); ax.set_title("T7 Q8: phasor diagram (not to scale), $E_2=V_2+I_2(R_e+jX_e)$", fontsize=9); ax.set_xlabel("real"); ax.set_ylabel("imag"); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(OUT7 + "/T7-Q8-Q9-plots.png", dpi=150); plt.close(fig)


if __name__ == "__main__":
    for title, f in (("TUTORIAL 6", t6), ("TUTORIAL 7", t7)):
        print("==", title)
        for k, v in f().items():
            print(f"  {k}: {v}")
    if HAVE_FIG:
        here = os.path.dirname(os.path.abspath(__file__))
        OUT6 = os.path.join(here, "..", "Problems", "Tutorial 6 on OP-AMP", "assets")
        OUT7 = os.path.join(here, "..", "Problems", "Tutorial 7 on Transformer", "assets")
        os.makedirs(OUT6, exist_ok=True); os.makedirs(OUT7, exist_ok=True)
        for fn in (fig_q1, fig_q2_q3, fig_q4_q5, fig_q6, fig_q7_q8, fig_q9, fig_q10_q12, fig_t7):
            fn(); print("figure", fn.__name__)
