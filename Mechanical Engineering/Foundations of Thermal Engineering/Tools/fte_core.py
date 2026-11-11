"""Foundations of Thermal Engineering (ME2102 / ME3105): numbers and figures for the concept notes.
   python fte_core.py -> prints every quoted number, writes ../assets/FTE-*.png.  Steam and R134a from CoolProp."""
import os
from math import pi, sqrt, log, exp, tan, atan, radians, degrees
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
import CoolProp.CoolProp as CP
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})
K0 = 273.15


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


W = "Water"
PS = CP.PropsSI


def h(T=None, P=None, Q=None, s=None, fluid=W):
    if T is not None and P is not None:
        return PS("H", "T", T, "P", P, fluid)
    if P is not None and Q is not None:
        return PS("H", "P", P, "Q", Q, fluid)
    if P is not None and s is not None:
        return PS("H", "P", P, "S", s, fluid)
    if T is not None and Q is not None:
        return PS("H", "T", T, "Q", Q, fluid)


# ====================================================================== exergy
def exergy():
    T0, P0 = 298.15, 101325.0
    r = {}
    r["heat_1000K"] = 1000.0 * (1 - T0 / 1000.0)
    Q = 1000.0
    Sg = Q * (1 / 500 - 1 / 1000)
    r.update(Sgen=Sg, Xdest=T0 * Sg, X_before=Q * (1 - T0 / 1000), X_after=Q * (1 - T0 / 500))
    P1, T1 = 5e6, 673.15
    h1, s1 = h(T=T1, P=P1), PS("S", "T", T1, "P", P1, W)
    h0, s0 = PS("H", "T", T0, "P", P0, W), PS("S", "T", T0, "P", P0, W)
    r["psi_steam"] = ((h1 - h0) - T0 * (s1 - s0)) / 1e3
    r["dh"] = (h1 - h0) / 1e3
    r["eta_II_turbine"] = None
    # throttling steam 5 MPa 400C to 1 MPa
    hh = h1
    s2 = PS("S", "H", hh, "P", 1e6, W)
    r["throttle_dest"] = T0 * (s2 - s1) / 1e3
    # adiabatic turbine 5MPa/400C to 10 kPa, isentropic efficiency 0.85: work and exergy destroyed
    h2s = PS("H", "P", 1e4, "S", s1, W)
    w_s = (h1 - h2s)
    w = 0.85 * w_s
    h2 = h1 - w
    s2a = PS("S", "H", h2, "P", 1e4, W)
    r.update(w_ideal=w_s / 1e3, w_real=w / 1e3, dest_turbine=T0 * (s2a - s1) / 1e3, eta_II=w / (w + T0 * (s2a - s1)))
    return r


# ====================================================================== Rankine
def rankine():
    P_b, T_max, P_c = 8e6, 773.15, 10e3
    out = {}
    h1 = h(P=P_c, Q=0); v1 = 1 / PS("D", "P", P_c, "Q", 0, W)
    wp = v1 * (P_b - P_c)
    h2 = h1 + wp
    h3 = h(T=T_max, P=P_b); s3 = PS("S", "T", T_max, "P", P_b, W)
    h4 = h(P=P_c, s=s3); x4 = PS("Q", "P", P_c, "S", s3, W)
    wt = h3 - h4
    qin = h3 - h2
    out["simple"] = dict(wp=wp / 1e3, wt=wt / 1e3, qin=qin / 1e3, eta=(wt - wp) / qin, x4=x4, wnet=(wt - wp) / 1e3, h=(h1, h2, h3, h4), s3=s3)
    # reheat at 1.5 MPa to 500 C
    P_r = 1.5e6
    h4a = h(P=P_r, s=s3)
    h5 = h(T=T_max, P=P_r); s5 = PS("S", "T", T_max, "P", P_r, W)
    h6 = h(P=P_c, s=s5); x6 = PS("Q", "P", P_c, "S", s5, W)
    wt_r = (h3 - h4a) + (h5 - h6)
    qin_r = (h3 - h2) + (h5 - h4a)
    out["reheat"] = dict(wt=wt_r / 1e3, qin=qin_r / 1e3, eta=(wt_r - wp) / qin_r, x6=x6, P_r=P_r)
    # regenerative, one open feedwater heater at 1 MPa
    P_x = 1e6
    h_ext = h(P=P_x, s=s3); x_ext = PS("Q", "P", P_x, "S", s3, W)
    h_f7 = h(P=P_x, Q=0); v7 = 1 / PS("D", "P", P_x, "Q", 0, W)
    wp1 = v1 * (P_x - P_c); h2b = h1 + wp1
    wp2 = v7 * (P_b - P_x); h8 = h_f7 + wp2
    y = (h_f7 - h2b) / (h_ext - h2b)
    wt_reg = (h3 - h_ext) + (1 - y) * (h_ext - h4)
    wp_reg = (1 - y) * wp1 + wp2
    qin_reg = h3 - h8
    out["regen"] = dict(y=y, wt=wt_reg / 1e3, wp=wp_reg / 1e3, qin=qin_reg / 1e3, eta=(wt_reg - wp_reg) / qin_reg)
    # reheat + regeneration is not computed; effect of superheat and pressure
    # real: eta_t = .85 eta_p = .8 on simple
    h4r = h3 - 0.85 * wt; wp_r = wp / 0.8
    out["simple_real"] = dict(eta=(h3 - h4r - wp_r) / (h3 - (h1 + wp_r)), x4=PS("Q", "P", P_c, "H", h4r, W))
    # carnot between Tmax and Tc
    out["carnot"] = 1 - PS("T", "P", P_c, "Q", 0, W) / T_max
    out["Tsat_c"] = PS("T", "P", P_c, "Q", 0, W) - K0
    out["Tsat_b"] = PS("T", "P", P_b, "Q", 0, W) - K0
    return out


def fig_rankine(r):
    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    Tc = np.linspace(273.2, 647, 200)
    sl = [PS("S", "T", t, "Q", 0, W) / 1e3 for t in Tc]; sv = [PS("S", "T", t, "Q", 1, W) / 1e3 for t in Tc]
    ax.plot(sl, Tc - K0, color=GREY); ax.plot(sv, Tc - K0, color=GREY)
    P_b, P_c, T_max = 8e6, 10e3, 773.15
    def path(P, s_from, s_to, n=40):
        pts = []
        for s in np.linspace(s_from, s_to, n):
            pts.append((s / 1e3, PS("T", "P", P, "S", s, W) - K0))
        return np.array(pts)
    s1 = PS("S", "P", P_c, "Q", 0, W); s2 = s1
    sB_l = PS("S", "P", P_b, "Q", 0, W); sB_v = PS("S", "P", P_b, "Q", 1, W); s3 = r["simple"]["s3"]
    ax.plot([s1 / 1e3, s1 / 1e3], [PS("T", "P", P_c, "Q", 0, W) - K0, PS("T", "P", P_c, "S", s1 + 1, W) - K0 + 0.1], color=BLUE, lw=2)
    p = path(P_b, s1 + 1, sB_l); ax.plot(p[:, 0], p[:, 1], color=BLUE, lw=2.4, label="simple: heat in at 8 MPa")
    Tsb = PS("T", "P", P_b, "Q", 0, W) - K0
    ax.plot([sB_l / 1e3, sB_v / 1e3], [Tsb, Tsb], color=BLUE, lw=2.4)
    p = path(P_b, sB_v, s3); ax.plot(p[:, 0], p[:, 1], color=BLUE, lw=2.4)
    ax.plot([s3 / 1e3, s3 / 1e3], [T_max - K0, PS("T", "P", P_c, "S", s3, W) - K0], color=BLUE, lw=2.4)
    Tc_ = PS("T", "P", P_c, "Q", 0, W) - K0
    x4 = r["simple"]["x4"]; s4v = PS("S", "P", P_c, "Q", 1, W)
    ax.plot([s3 / 1e3, s1 / 1e3], [Tc_, Tc_], color=BLUE, lw=2.4)
    # reheat extra
    P_r = r["reheat"]["P_r"]; h5s = PS("S", "T", T_max, "P", P_r, W)
    ax.plot([s3 / 1e3, s3 / 1e3], [T_max - K0, PS("T", "P", P_r, "S", s3, W) - K0], color=ORANGE, lw=2, ls="--")
    p = path(P_r, s3, h5s); ax.plot(p[:, 0], p[:, 1], color=ORANGE, lw=2.2, ls="--", label="reheat at 1.5 MPa to 500 °C")
    ax.plot([h5s / 1e3, h5s / 1e3], [T_max - K0, Tc_], color=ORANGE, lw=2.2, ls="--")
    ax.set_xlim(0, 9.5); ax.set_ylim(0, 600); ax.set_xlabel("entropy s (kJ/kg·K)"); ax.set_ylabel("temperature (°C)"); ax.legend(fontsize=9, loc="upper left")
    ax.set_title("Rankine on a T–s diagram: reheat keeps the exhaust drier (x = %.2f against %.2f)" % (r["reheat"]["x6"], r["simple"]["x4"]), fontsize=9.5)
    save(fig, "FTE-1-rankine.png")


# ====================================================================== Brayton
CPA, GAM = 1.005, 1.4
K_EXP = (GAM - 1) / GAM


def brayton():
    T1, T3, rp = 300.0, 1400.0, 10.0
    out = {}
    T2 = T1 * rp ** K_EXP; T4 = T3 / rp ** K_EXP
    wc, wt = CPA * (T2 - T1), CPA * (T3 - T4)
    out["simple"] = dict(T2=T2, T4=T4, wc=wc, wt=wt, wnet=wt - wc, qin=CPA * (T3 - T2), eta=(wt - wc) / (CPA * (T3 - T2)), bwr=wc / wt, eta_formula=1 - rp ** -K_EXP)
    eps = 0.8
    T5 = T2 + eps * (T4 - T2)
    qin_reg = CPA * (T3 - T5)
    out["regen"] = dict(T5=T5, qin=qin_reg, eta=(wt - wc) / qin_reg)
    rp1 = sqrt(rp)
    T2i = T1 * rp1 ** K_EXP
    wc2 = 2 * CPA * (T2i - T1)
    T4i = T3 / rp1 ** K_EXP
    wt2 = 2 * CPA * (T3 - T4i)
    qin_ir = CPA * (T3 - T2i) + CPA * (T3 - T4i)
    out["inter_reheat"] = dict(wc=wc2, wt=wt2, wnet=wt2 - wc2, qin=qin_ir, eta=(wt2 - wc2) / qin_ir, T4i=T4i)
    T5r = T2i + eps * (T4i - T2i)
    qin_all = CPA * (T3 - T5r) + CPA * (T3 - T4i)
    out["all"] = dict(eta=(wt2 - wc2) / qin_all, T5=T5r)
    # optimal pressure ratio for maximum net work
    rp_opt = (T3 / T1) ** (1 / (2 * K_EXP))
    out["rp_opt_work"] = rp_opt
    # real: eta_c = .85, eta_t = .88
    wc_r = wc / 0.85; wt_r = wt * 0.88
    out["real"] = dict(wnet=wt_r - wc_r, eta=(wt_r - wc_r) / (CPA * (T3 - (T1 + wc_r / CPA))))
    return out


def fig_brayton(b):
    fig, (a, c) = plt.subplots(1, 2, figsize=(11, 4.4))
    rps = np.linspace(2, 40, 200); T1, T3 = 300.0, 1400.0
    eta = 1 - rps ** -K_EXP
    wnet = CPA * (T3 - T3 / rps ** K_EXP - T1 * rps ** K_EXP + T1)
    a.plot(rps, eta, color=BLUE, lw=2.4, label="efficiency"); a.set_xlabel("pressure ratio r_p"); a.set_ylabel("thermal efficiency", color=BLUE)
    a2 = a.twinx(); a2.plot(rps, wnet, color=ORANGE, lw=2.2, label="net work"); a2.set_ylabel("net work (kJ/kg)", color=ORANGE); a2.grid(False)
    a.axvline(b["rp_opt_work"], color=GREY, ls=":"); a.text(b["rp_opt_work"] + .5, 0.05, "max work at r_p = %.1f" % b["rp_opt_work"], fontsize=9)
    a.set_title("Brayton cycle (T₁ = 300 K, T₃ = 1400 K): efficiency rises with r_p, work peaks", fontsize=9.5)
    labs = ["simple", "+ regenerator\n(ε = 0.8)", "+ intercooling\nand reheat", "all three"]
    vals = [b["simple"]["eta"], b["regen"]["eta"], b["inter_reheat"]["eta"], b["all"]["eta"]]
    c.bar(range(4), vals, color=[BLUE, GREEN, ORANGE, PURPLE]); [c.text(i, v + .01, "%.3f" % v, ha="center") for i, v in enumerate(vals)]
    c.set_xticks(range(4)); c.set_xticklabels(labs, fontsize=9); c.set_ylabel("thermal efficiency"); c.set_ylim(0, .75)
    c.set_title("r_p = 10: intercooling and reheat raise work but not efficiency by themselves", fontsize=9.5)
    fig.suptitle("Gas turbine cycles (air standard, γ = 1.4)", fontsize=11)
    save(fig, "FTE-2-brayton.png")


# ====================================================================== refrigeration
R = "R134a"


def refrigeration():
    Te, Tc = 263.15, 313.15
    pe, pc = PS("P", "T", Te, "Q", 1, R), PS("P", "T", Tc, "Q", 0, R)
    h1 = PS("H", "T", Te, "Q", 1, R); s1 = PS("S", "T", Te, "Q", 1, R)
    h2s = PS("H", "P", pc, "S", s1, R)
    h3 = PS("H", "T", Tc, "Q", 0, R)
    h4 = h3
    out = dict(pe=pe / 1e3, pc=pc / 1e3, h1=h1 / 1e3, h2s=h2s / 1e3, h3=h3 / 1e3, qL=(h1 - h4) / 1e3, wc=(h2s - h1) / 1e3, COP=(h1 - h4) / (h2s - h1),
               COP_carnot=Te / (Tc - Te), x4=PS("Q", "H", h4, "P", pe, R), rp=pc / pe)
    out["COP_HP"] = out["COP"] + 1
    h2 = h1 + (h2s - h1) / 0.8
    out["COP_real"] = (h1 - h4) / (h2 - h1)
    # subcooling by 5 K
    h3s = PS("H", "T", Tc - 5, "P", pc, R)
    out["COP_sub"] = (h1 - h3s) / (h2s - h1)
    out["T2s"] = PS("T", "P", pc, "H", h2s, R) - K0
    return out


def fig_refrigeration(r):
    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    Tc_ = np.linspace(240, 370, 100)
    hl = [PS("H", "T", t, "Q", 0, R) / 1e3 for t in Tc_]; hv = [PS("H", "T", t, "Q", 1, R) / 1e3 for t in Tc_]; ps = [PS("P", "T", t, "Q", 0, R) / 1e5 for t in Tc_]
    ax.semilogy(hl, ps, color=GREY); ax.semilogy(hv, ps, color=GREY)
    ax.plot([r["h1"], r["h2s"], r["h3"], r["h3"], r["h1"]], [r["pe"] / 100, r["pc"] / 100, r["pc"] / 100, r["pe"] / 100, r["pe"] / 100], color=BLUE, lw=2.6)
    for (x, y, t) in ((r["h1"], r["pe"] / 100, "1"), (r["h2s"], r["pc"] / 100, "2"), (r["h3"], r["pc"] / 100, "3"), (r["h3"], r["pe"] / 100, "4")):
        ax.plot([x], [y], "o", color=RED); ax.text(x + 3, y * 1.05, t, fontsize=11, weight="bold")
    ax.text(r["h3"] + 35, r["pe"] / 100 * 1.5, "evaporator: q_L = %.1f kJ/kg" % r["qL"], fontsize=9, color=BLUE)
    ax.text(r["h1"] - 10, r["pc"] / 100 * 1.15, "compressor: w = %.1f kJ/kg" % r["wc"], fontsize=9, color=BLUE)
    ax.set_xlabel("enthalpy h (kJ/kg)"); ax.set_ylabel("pressure (bar)"); ax.set_title("R134a, evaporator −10 °C, condenser 40 °C: COP = %.2f (Carnot %.2f)" % (r["COP"], r["COP_carnot"]), fontsize=9.5)
    save(fig, "FTE-3-refrigeration.png")


# ====================================================================== psychrometrics
PATM = 101325.0


def psat(Tc):
    return PS("P", "T", Tc + K0, "Q", 0, W)


def omega(Tc, phi):
    pv = phi * psat(Tc)
    return 0.622 * pv / (PATM - pv)


def omega_sat(Tc):
    return omega(Tc, 1.0)


def enth(Tc, w):
    return 1.006 * Tc + w * (2501 + 1.86 * Tc)


def wetbulb(Tc, w):
    f = lambda Tw: ((2501 - 2.326 * Tw) * omega_sat(Tw) - 1.006 * (Tc - Tw)) / (2501 + 1.86 * Tc - 4.186 * Tw) - w
    return brentq(f, 0.0, Tc)


def psychro():
    out = {}
    T1, phi1 = 35.0, 0.5
    w1 = omega(T1, phi1); h1 = enth(T1, w1)
    pv1 = phi1 * psat(T1)
    Tdp = PS("T", "P", pv1, "Q", 1, W) - K0
    out.update(w1=w1, h1=h1, Tdp=Tdp, Twb=wetbulb(T1, w1), pv1=pv1 / 1e3, pg1=psat(T1) / 1e3)
    T2 = 14.0
    w2 = omega_sat(T2); h2 = enth(T2, w2)
    hf2 = 4.186 * T2
    out.update(w2=w2, h2=h2, cond=w1 - w2, q_cool=(h1 - h2) - (w1 - w2) * hf2)
    T3 = 24.0
    h3 = enth(T3, w2)
    out.update(h3=h3, q_reheat=h3 - h2, phi3=PATM * w2 / (0.622 + w2) / psat(T3), SHR=(1.006 + 1.86 * w1) * (T1 - T2) / out["q_cool"])
    # evaporative cooler (adiabatic saturation) from 35C 20 %
    w_ec = omega(35.0, 0.2); Tw = wetbulb(35.0, w_ec)
    out["evap"] = dict(w=w_ec, Twb=Tw, T_out_90=35.0 - 0.9 * (35.0 - Tw))
    return out


def fig_psychro(p):
    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    Tg = np.linspace(0, 45, 200)
    for phi in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        ax.plot(Tg, [omega(t, phi) * 1000 for t in Tg], color=BLUE if phi < 1 else RED, lw=1.0 if phi < 1 else 2.4)
        t_l = 38 if phi >= 0.3 else 43
        ax.text(t_l, omega(t_l, phi) * 1000, "%d %%" % (phi * 100), fontsize=7.5, color=GREY)
    pts = [(35.0, p["w1"] * 1000), (14.0, p["w2"] * 1000), (24.0, p["w2"] * 1000)]
    ax.plot([pt[0] for pt in pts], [pt[1] for pt in pts], "o-", color=ORANGE, lw=2.4)
    ax.text(pts[0][0] + .6, pts[0][1] + .4, "1: 35 °C, 50 %%\nω = %.1f g/kg" % (p["w1"] * 1000, ), fontsize=9)
    ax.text(pts[1][0] - 9, pts[1][1] + 1.2, "2: 14 °C, 100 %\n(cool and dehumidify)", fontsize=9)
    ax.text(pts[2][0] - 1, pts[2][1] - 1.9, "3: 24 °C, %.0f %%\n(reheat)" % (100 * p["phi3"]), fontsize=9)
    ax.plot([p["Tdp"], p["w1"] * 0 + p["Tdp"]], [0, omega_sat(p["Tdp"]) * 1000], color=GREY, ls=":"); ax.plot([p["Tdp"], 35], [p["w1"] * 1000] * 2, color=GREY, ls=":"); ax.text(p["Tdp"] + .3, 0.4, "dew point %.1f °C" % p["Tdp"], fontsize=8.5, color=GREY)
    ax.set_xlim(0, 45); ax.set_ylim(0, 30); ax.set_xlabel("dry-bulb temperature (°C)"); ax.set_ylabel("humidity ratio ω (g water / kg dry air)")
    ax.set_title("Psychrometric chart (101.3 kPa) with a cooling, dehumidifying and reheating process", fontsize=9.5)
    save(fig, "FTE-4-psychrometric.png")


# ====================================================================== Otto, Diesel, Dual
CV, RGAS = 0.718, 0.287


def engines():
    out = {}
    r, g = 9.0, GAM
    out["otto_eta"] = 1 - r ** (1 - g)
    T1, p1 = 300.0, 100.0
    qin = 1800.0
    T2 = T1 * r ** (g - 1); T3 = T2 + qin / CV; T4 = T3 / r ** (g - 1)
    wnet = qin - CV * (T4 - T1)
    v1 = RGAS * T1 / p1; v2 = v1 / r
    out["otto"] = dict(T2=T2, T3=T3, T4=T4, wnet=wnet, mep=wnet / (v1 - v2), p3=p1 * r ** g * T3 / T2, eta=wnet / qin, p2=p1 * r ** g)
    rd, rc = 18.0, 2.0
    out["diesel_eta"] = 1 - rd ** (1 - g) * (rc ** g - 1) / (g * (rc - 1))
    out["otto_at_18"] = 1 - rd ** (1 - g)
    al = 1.5
    out["dual_eta"] = 1 - rd ** (1 - g) * (al * rc ** g - 1) / ((al - 1) + g * al * (rc - 1))
    # engine test
    N, T_b, Vd, nR = 4000.0, 180.0, 2.0e-3, 2
    Pb = 2 * pi * N / 60 * T_b
    mf, LHV = 5.0e-3, 44e6
    out["test"] = dict(Pb=Pb / 1e3, bmep=Pb * nR / (Vd * N / 60) / 1e6, bsfc=mf * 3600 / (Pb / 1e3) * 1e3 / 1e3 * 1e3 / 1e3, eta_b=Pb / (mf * LHV), Ptot=Pb / 1e3)
    out["test"]["bsfc"] = mf * 1e3 * 3600 / (Pb / 1e3)
    return out


def fig_engines(e):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    rr = np.linspace(4, 24, 100)
    a.plot(rr, 1 - rr ** (1 - GAM), color=BLUE, lw=2.4, label="Otto")
    for rc, col in ((1.5, GREEN), (2.0, ORANGE), (3.0, RED)):
        a.plot(rr, 1 - rr ** (1 - GAM) * (rc ** GAM - 1) / (GAM * (rc - 1)), color=col, lw=1.8, ls="--", label="Diesel, cut-off %.1f" % rc)
    a.plot([9], [e["otto_eta"]], "o", color=BLUE); a.plot([18], [e["diesel_eta"]], "o", color=ORANGE)
    a.set_xlabel("compression ratio r"); a.set_ylabel("ideal thermal efficiency (γ = 1.4)"); a.legend(fontsize=9); a.set_title("Diesel loses to Otto at the same r, wins at its higher practical r", fontsize=9.5)
    # p-v for Otto and Diesel same r
    r = 9.0; v1 = 1.0; v2 = v1 / r
    v = np.linspace(v2, v1, 50)
    p1 = 1.0
    p_c = p1 * (v1 / v) ** GAM
    b.plot(v / v1, p_c, color=BLUE, lw=2.2)
    p2 = p1 * r ** GAM; p3 = p2 * 3.0
    b.plot([v2, v2], [p2, p3], color=BLUE, lw=2.2)
    p_e = p3 * (v2 / v) ** GAM; b.plot(v / v1, p_e, color=BLUE, lw=2.2)
    b.plot([v1, v1], [p_e[-1], p1], color=BLUE, lw=2.2)
    rc = 2.0; v3 = rc * v2
    vv = np.linspace(v3, v1, 50); pd = p2 * (v3 / vv) ** GAM
    b.plot([v2, v3], [p2, p2], color=ORANGE, lw=2.2); b.plot(vv / v1, pd, color=ORANGE, lw=2.2)
    b.plot([v1, v1], [pd[-1], p1], color=ORANGE, lw=2.2)
    b.set_xlabel("v / v₁"); b.set_ylabel("p / p₁"); b.set_title("p–v: Otto (heat at constant volume), Diesel (at constant pressure)", fontsize=9.5)
    b.text(0.13, 40, "Otto", color=BLUE); b.text(0.28, 22, "Diesel", color=ORANGE)
    fig.suptitle("Air-standard engine cycles", fontsize=11)
    save(fig, "FTE-5-engines.png")


# ====================================================================== combustion
def cp0(T, fluid):
    return PS("Cp0molar", "T", T, "P", 101325, fluid)


def dh(T, fluid, T0=298.15):
    return quad(lambda t: cp0(t, fluid), T0, T)[0]


def combustion():
    out = {}
    Ma = 28.97
    out["AF_CH4"] = 2 * 4.76 * Ma / 16.043
    out["AF_C8H18"] = 12.5 * 4.76 * Ma / 114.23
    out["LHV_CH4"] = 802.3 / 16.043 * 1e3 / 1e3     # kJ/mol / (kg/mol): MJ/kg
    hf = dict(CO2=-393.52, H2O_g=-241.83, H2O_l=-285.83, C8H18_l=-249.90, CH4=-74.87)
    out["LHV_CH4_check"] = -(hf["CO2"] + 2 * hf["H2O_g"] - hf["CH4"])
    out["HHV_CH4"] = -(hf["CO2"] + 2 * hf["H2O_l"] - hf["CH4"])
    out["LHV_oct"] = -(8 * hf["CO2"] + 9 * hf["H2O_g"] - hf["C8H18_l"])
    out["LHV_oct_MJkg"] = out["LHV_oct"] / 114.23
    # adiabatic flame temperature, CH4 + 2(O2 + 3.76 N2), reactants at 298 K, complete combustion to CO2, H2O(g), N2
    def Tad(phi=1.0):
        # lean: excess air; products CO2, 2 H2O, N2, O2
        a = 2.0 / phi
        n = dict(CO2=1.0, Water=2.0, Nitrogen=3.76 * a, Oxygen=max(a - 2.0, 0.0))
        f = lambda T: sum(v * dh(T, k) / 1e3 for k, v in n.items()) - 802.3
        return brentq(f, 800, 3600)
    out["Tad_stoich"] = Tad(1.0)
    out["Tad_phi07"] = Tad(1 / 1.43)      # about 43 % excess air
    out["Tad_200_air"] = Tad(0.5)
    return out


# ====================================================================== turbomachines
def turbo():
    out = {}
    N, r2 = 1450.0, 0.15
    u2 = 2 * pi * N / 60 * r2
    cm2, b2 = 2.5, radians(25)
    ct2 = u2 - cm2 / tan(b2)
    out.update(u2=u2, ct2=ct2, H=u2 * ct2 / 9.81, w=u2 * ct2)
    out["affinity"] = dict(Q=2.0, H=4.0, P=8.0)
    U, cx, a2 = 300.0, 150.0, radians(60)
    ct2g = cx * tan(a2)
    w = U * ct2g
    wt2 = ct2g - U
    w2sq = cx ** 2 + wt2 ** 2; w3sq = cx ** 2 + U ** 2
    dh_rotor = (w3sq - w2sq) / 2
    out["turbine"] = dict(ct2=ct2g, w=w / 1e3, wt2=wt2, b2=degrees(atan(wt2 / cx)), b3=degrees(atan(-U / cx)), R=dh_rotor / w, dh_rotor=dh_rotor / 1e3)
    return out


def fig_turbo(t):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.6))
    U, cx = 300.0, 150.0
    for ax_, title in ((a, "stage inlet (station 2): nozzle exit"), (b, "stage exit (station 3): axial absolute flow")):
        ax_.set_aspect("equal"); ax_.axis("off")
    ct2 = t["turbine"]["ct2"]
    # inlet triangle: absolute c2 = (cx, ct2); blade speed U; relative w2 = c2 - U
    a.annotate("", (ct2, cx), (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=2.4)); a.text(ct2 / 2 + 10, cx / 2 + 25, "c₂", color=RED, fontsize=12)
    a.annotate("", (U, 0), (0, 0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.4)); a.text(U / 2, -25, "U = 300", color=GREEN, ha="center", fontsize=11)
    a.annotate("", (ct2, cx), (U, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.4)); a.text(U + 12, cx / 2 + 10, "w₂", color=BLUE, fontsize=12)
    a.annotate("", (0, cx), (0, 0), arrowprops=dict(arrowstyle="-", color=GREY, ls="--")); a.text(-30, cx / 2, "c_x = 150", color=GREY, rotation=90, va="center")
    a.text(ct2 / 2, cx + 25, "c_θ2 = %.0f, α₂ = 60°, β₂ = %.0f°" % (ct2, t["turbine"]["b2"]), ha="center", fontsize=9)
    a.set_xlim(-80, 360); a.set_ylim(-60, 230)
    b.annotate("", (0, cx), (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=2.4)); b.text(-35, cx / 2, "c₃ = 150 (axial)", color=RED, fontsize=11, rotation=90, va="center")
    b.annotate("", (U, 0), (0, 0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.4)); b.text(U / 2, -25, "U = 300", color=GREEN, ha="center", fontsize=11)
    b.annotate("", (0, cx), (U, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.4)); b.text(U / 2 + 15, cx / 2 + 20, "w₃", color=BLUE, fontsize=12)
    b.text(U / 2, cx + 25, "β₃ = %.1f°" % t["turbine"]["b3"], ha="center", fontsize=9)
    b.set_xlim(-80, 360); b.set_ylim(-60, 230)
    fig.suptitle("Velocity triangles of an axial turbine stage: w = U (c_θ2 − c_θ3) = %.1f kJ/kg, reaction %.2f" % (t["turbine"]["w"], t["turbine"]["R"]), fontsize=10.5)
    save(fig, "FTE-6-velocity-triangles.png")


# ====================================================================== nozzle
def nozzle():
    g, R_ = 1.4, 287.0
    out = {}
    T0, p0, d = 300.0, 500e3, 0.020
    A = pi * d ** 2 / 4
    mdot = A * p0 * sqrt(g / (R_ * T0)) * (2 / (g + 1)) ** ((g + 1) / (2 * (g - 1)))
    out.update(mdot=mdot, a0=sqrt(g * R_ * T0), crit=(2 / (g + 1)) ** (g / (g - 1)), T_star=T0 * 2 / (g + 1))
    M = 2.0
    T = T0 / (1 + (g - 1) / 2 * M ** 2)
    out.update(M2_T=T, M2_V=M * sqrt(g * R_ * T), M2_p=p0 * (1 + (g - 1) / 2 * M ** 2) ** (-g / (g - 1)) / 1e3, M2_AA=(1 / M) * ((2 / (g + 1)) * (1 + (g - 1) / 2 * M ** 2)) ** ((g + 1) / (2 * (g - 1))))
    out["p_back_choke"] = p0 * out["crit"] / 1e3
    return out


def fig_nozzle(n):
    g = 1.4
    M = np.linspace(0.05, 3.0, 300)
    AA = (1 / M) * ((2 / (g + 1)) * (1 + (g - 1) / 2 * M ** 2)) ** ((g + 1) / (2 * (g - 1)))
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    a.plot(M, AA, color=BLUE, lw=2.4, label="A/A*"); a.plot(M, 1 / (1 + (g - 1) / 2 * M ** 2), color=ORANGE, lw=2, label="T/T₀")
    a.plot(M, (1 + (g - 1) / 2 * M ** 2) ** (-g / (g - 1)), color=GREEN, lw=2, label="p/p₀")
    a.set_ylim(0, 4); a.axvline(1, color=GREY, ls=":"); a.text(1.03, 3.5, "sonic at the throat", fontsize=9, color=GREY)
    a.set_xlabel("Mach number M"); a.set_ylabel("ratio to stagnation or throat value"); a.legend(fontsize=9); a.set_title("isentropic flow of air: one area, two Mach numbers", fontsize=9.5)
    pb = np.linspace(1.0, 0.0, 200)
    p0 = 1.0
    crit = n["crit"]
    m_flow = np.where(pb > crit, np.sqrt(np.maximum((pb) ** (2 / g) - (pb) ** ((g + 1) / g), 0)) * np.sqrt(2 * g / (g - 1)), np.sqrt((crit) ** (2 / g) - (crit) ** ((g + 1) / g)) * np.sqrt(2 * g / (g - 1)))
    b.plot(pb, m_flow / m_flow.max(), color=BLUE, lw=2.4)
    b.axvline(crit, color=RED, ls="--"); b.text(crit + .02, .3, "choked below p_b/p₀ = %.3f" % crit, color=RED, fontsize=9)
    b.invert_xaxis(); b.set_xlabel("back pressure / stagnation pressure"); b.set_ylabel("mass flow / maximum"); b.set_title("convergent nozzle: the flow stops responding to back pressure", fontsize=9.5)
    fig.suptitle("Compressible flow in a nozzle", fontsize=11)
    save(fig, "FTE-7-nozzle.png")


if __name__ == "__main__":
    ex, rk, br, rf, ps, en, cb, tb, nz = exergy(), rankine(), brayton(), refrigeration(), psychro(), engines(), combustion(), turbo(), nozzle()
    for name, d in (("exergy", ex), ("rankine", rk), ("brayton", br), ("refrigeration", rf), ("psychro", ps), ("engines", en), ("combustion", cb), ("turbo", tb), ("nozzle", nz)):
        print("---", name)
        for k, v in d.items():
            if callable(v):
                continue
            if isinstance(v, dict):
                print(f"  {k:14s}", {a: (round(b, 4) if isinstance(b, (int, float)) else b) for a, b in v.items() if not callable(b)})
            elif isinstance(v, (int, float)):
                print(f"  {k:14s}", round(v, 5))
            else:
                print(f"  {k:14s}", v)
    fig_rankine(rk); fig_brayton(br); fig_refrigeration(rf); fig_psychro(ps); fig_engines(en); fig_turbo(tb); fig_nozzle(nz)
