"""Verification of GPS 7 & 8 (pipe flow, AM2530): every number quoted in
   '09 Pipe Flow and Losses/Pipe Flow and Losses - Solved Problems' is recomputed here and the Moody-chart figures are drawn.
   Run `python fm_pipe.py` (figures go to ../assets/)."""
import os
import numpy as np
from math import log10, sqrt, pi
from scipy.optimize import brentq, fsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G = 9.81
W20 = dict(rho=998., mu=1.01e-3, nu=1.01e-6)     # data sheet, water 20 C
W15 = dict(rho=999., mu=1.14e-3, nu=1.14e-6)     # water 15 C
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")


# ---------------------------------------------------------------- friction factor
def colebrook(Re, ed):
    if Re < 2300:
        return 64. / Re
    g = lambda f: 1 / sqrt(f) + 2.0 * log10(ed / 3.7 + 2.51 / (Re * sqrt(f)))
    return brentq(g, 0.005, 0.2)


def haaland(Re, ed):
    if Re < 2300:
        return 64. / Re
    return (-1.8 * log10((ed / 3.7) ** 1.11 + 6.9 / Re)) ** -2


def rough_limit(ed):
    return (-2.0 * log10(ed / 3.7)) ** -2


def moody_curve(ed, Re):
    return np.array([colebrook(r, ed) if ed > 0 else (haaland(r, 1e-12) if r >= 2300 else 64 / r) for r in Re])


def flow_from_head(avail, D, L, ed, nu, ff=colebrook, K=0.0):
    """avail = J/kg driving the flow (p/rho - g dz), velocity head V^2/2 (f L/D + K) = avail  ->  V."""
    def res(V):
        return V * V / 2 * (ff(V * D / nu, ed) * L / D + K) - avail
    V = brentq(res, 1e-4, 100)
    return V, ff(V * D / nu, ed)


# ================================================================ Problem 1  house water
def problem1():
    w = W20
    p_meter, p_pump, H = 200e3, 300e3, 15.0
    out = {}
    A = lambda D: pi * D * D / 4
    # existing: 12.7 mm, e/D = 0.05, L = 7 + 15 + 1
    D0, ed0, L0 = 0.0127, 0.05, 23.0
    V, f = flow_from_head(p_meter / w["rho"] - G * H, D0, L0, ed0, w["nu"])
    out["existing"] = dict(V=V, f=f, Re=V * D0 / w["nu"], Q=V * A(D0) * 6e4, avail=p_meter / w["rho"] - G * H, LD=L0 / D0, f_rough=rough_limit(ed0))
    # option 1: 19 mm smooth, same route
    D1 = 0.019
    V, f = flow_from_head(p_meter / w["rho"] - G * H, D1, 23.0, 0.0, w["nu"])
    out["opt1"] = dict(V=V, f=f, Re=V * D1 / w["nu"], Q=V * A(D1) * 6e4, LD=23.0 / D1)
    # option 2: old pipe, pump at foot of riser (pipe after pump: 15 m rise + 1 m horizontal)
    V, f = flow_from_head(p_pump / w["rho"] - G * H, D0, 16.0, ed0, w["nu"])
    out["opt2"] = dict(V=V, f=f, Re=V * D0 / w["nu"], Q=V * A(D0) * 6e4, avail=p_pump / w["rho"] - G * H, LD=16.0 / D0)
    return out


# ================================================================ Problem 2  drainpipes
def problem2():
    w = W20
    out = {}
    for D in (0.050, 0.075):
        ed = 0.15e-3 / D
        # g H = f (H/D) V^2/2  ->  V^2 = 2 g D / f, H cancels
        V = brentq(lambda V: V * V - 2 * G * D / colebrook(V * D / w["nu"], ed), 0.1, 50)
        Q = V * pi * D * D / 4
        out[D] = dict(V=V, f=colebrook(V * D / w["nu"], ed), Re=V * D / w["nu"], ed=ed, Q=Q, rain_mm_h=Q / 500 / 2.78e-7)
    # height independence check
    for H in (2.0, 5.0, 20.0):
        D = 0.05; ed = 0.15e-3 / D
        V = brentq(lambda V: G * H - colebrook(V * D / w["nu"], ed) * (H / D) * V * V / 2, 0.1, 50)
        out[("H", H)] = V
    out["area_ratio"] = (0.075 / 0.05) ** 2
    out["Q_ratio"] = out[0.075]["Q"] / out[0.050]["Q"]
    return out


# ================================================================ Problem 3  industrial supply line
def problem3(ff=haaland, elbows=4, Le_D=30, sizes=(0.1023, 0.1282, 0.1541)):
    w = W15
    Q, dp_avail, L = 5.7 / 60, 300e3, 65.0
    e = 0.15e-3

    def dp(D):
        V = 4 * Q / (pi * D * D)
        Re = V * D / w["nu"]
        f = ff(Re, e / D)
        return w["rho"] * (f * (L / D + elbows * Le_D) * V * V / 2), V, Re, f
    Dmin = brentq(lambda D: dp(D)[0] - dp_avail, 0.05, 0.4)
    table = {}
    for D in sizes:
        d, V, Re, f = dp(D)
        table[D] = dict(dp=d, V=V, Re=Re, f=f, p_plant=800e3 - d)
    return dict(Dmin=Dmin, table=table, dp_at_Dmin=dp(Dmin))


# ================================================================ Problem 4  Roman nozzle
def problem4():
    z0, D, K, AR, Kd = 1.5, 0.025, 0.04, 2.0, 0.30
    A = pi * D * D / 4
    V_a = sqrt(2 * G * z0 / (1 + K))
    V_b = sqrt(2 * G * z0 / (1 / AR ** 2 + K + Kd))
    p_exit_b = 998 * (G * z0 - V_b ** 2 / 2 * (1 + K))
    return dict(Qa=V_a * A * 1e3, Qb=V_b * A * 1e3, Va=V_a, Vb=V_b, gain=(V_b / V_a - 1) * 100, p_exit_b=p_exit_b, p_exit_a=0.0)


# ================================================================ Problem 5  scaled main
def problem5():
    w = W20
    Q, L = 0.010, 500.0
    out = {}

    def dp_for(D, e, Q=Q):
        V = 4 * Q / (pi * D * D)
        Re = V * D / w["nu"]
        f = haaland(Re, e / D)
        return f * L / D * w["rho"] * V * V / 2, dict(V=V, Re=Re, ed=e / D, f=f, LD=L / D)
    out["new"] = dp_for(0.100, 0.26e-3)
    out["old"] = dp_for(0.080, 2.0e-3)
    out["bore_only"] = dp_for(0.080, 0.26e-3)             # smaller bore, original roughness
    out["rough_only"] = dp_for(0.100, 2.0e-3)             # original bore, rougher wall
    dp_new = out["new"][0]
    # flow delivered by the old main at the original pressure drop
    D, e = 0.080, 2.0e-3

    def res(Qx):
        return dp_for(D, e, Qx)[0] - dp_new
    Qx = brentq(res, 1e-4, 0.05)
    out["Q_old"] = Qx
    out["Q_old_detail"] = dp_for(D, e, Qx)[1]
    return out


# ================================================================ Problem 6  laminar tubing
def problem6():
    w = W20
    D, L, alpha, Kent = 3.18e-3, 15.3, 2.0, 1.4
    Vmax = 2300 * w["nu"] / D
    Q = Vmax * pi * D * D / 4
    f = 64 / 2300
    fL = f * L / D
    h = Vmax ** 2 / 2 * (alpha + Kent + fL) / G
    return dict(Vmax=Vmax, Q_mL_s=Q * 1e6, f=f, fLD=fL, h=h, frac=fL / (alpha + Kent + fL), LD=L / D, Re=2300)


# ================================================================ figures
def moody_axes(ax):
    Re = np.logspace(3, 8, 200)
    for ed in (0.05, 0.03, 0.02, 0.01, 0.004, 0.002, 0.001, 0.0004, 0.0001, 0.00001):
        ax.loglog(Re[Re >= 4e3], moody_curve(ed, Re[Re >= 4e3]), color="#8a8f98", lw=0.9)
        ax.text(1.05e8, colebrook(1e8, ed), f"{ed:g}", fontsize=7, color="#555", va="center")
    ax.loglog(Re[Re >= 4e3], moody_curve(0, Re[Re >= 4e3]), color="#222", lw=1.3, label="smooth")
    ax.loglog(np.logspace(3, np.log10(2300), 20), 64 / np.logspace(3, np.log10(2300), 20), color="#222", lw=1.3)
    ax.set_xlim(1e3, 1e8); ax.set_ylim(0.008, 0.1)
    ax.set_xlabel("Re = VD/ν"); ax.set_ylabel("friction factor f")
    ax.grid(True, which="both", alpha=0.25)
    ax.set_yticks([0.01, 0.02, 0.03, 0.05, 0.1]); ax.set_yticklabels(["0.01", "0.02", "0.03", "0.05", "0.1"]); ax.minorticks_off()
    ax.axvline(2300, color="#bbb", ls="--", lw=0.8)


def figures(p1, p6):
    os.makedirs(ASSETS, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    moody_axes(ax)
    pts = [("existing, e/D = 0.05", p1["existing"], "#d94a4a", (-40, -36)), ("Option 2: pump, e/D = 0.05", p1["opt2"], "#e69500", (16, 14)), ("Option 1: 19 mm smooth", p1["opt1"], "#2a9d4a", (14, 10))]
    for lab, d, c, off in pts:
        ax.plot(d["Re"], d["f"], "o", color=c, ms=9, zorder=5)
        ax.annotate(lab, (d["Re"], d["f"]), textcoords="offset points", xytext=off, fontsize=8.5, color=c, weight="bold")
    ax.set_title("GPS 7 & 8, Q1: the three operating points")
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "FM-P1-moody-operating-points.png"), dpi=160); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    moody_axes(ax)
    ax.plot(p6["Re"], p6["f"], "o", color="#1f6feb", ms=9, zorder=5)
    ax.annotate("Q6: Re = 2300, f = 64/Re = 0.0278\n(largest flow that is still laminar)", (p6["Re"], p6["f"]), textcoords="offset points", xytext=(14, 18), fontsize=8.5, color="#1f6feb", weight="bold")
    ax.set_title("GPS 7 & 8, Q6: laminar operating point")
    fig.tight_layout(); fig.savefig(os.path.join(ASSETS, "FM-P6-laminar-point.png"), dpi=160); plt.close(fig)


def main():
    p1 = problem1(); print("Q1", {k: {a: round(b, 4) for a, b in v.items()} for k, v in p1.items()})
    p2 = problem2()
    print("Q2 50mm", {a: round(b, 5) for a, b in p2[0.05].items()}, "75mm", {a: round(b, 5) for a, b in p2[0.075].items()})
    print("Q2 H-independence V:", {k[1]: round(v, 4) for k, v in p2.items() if isinstance(k, tuple)}, "area ratio", p2["area_ratio"], "Q ratio", round(p2["Q_ratio"], 3))
    p3 = problem3(); print("Q3 Dmin(mm)", round(p3["Dmin"] * 1e3, 2))
    for D, d in p3["table"].items():
        print("   D", D, {a: round(b, 4) for a, b in d.items()})
    p3b = problem3(elbows=0); print("Q3 no elbows Dmin(mm)", round(p3b["Dmin"] * 1e3, 2))
    for D, d in p3b["table"].items():
        print("   D", D, {a: round(b, 4) for a, b in d.items()})
    p3c = problem3(ff=colebrook); print("Q3 Colebrook Dmin(mm)", round(p3c["Dmin"] * 1e3, 2))
    p4 = problem4(); print("Q4", {a: round(b, 4) for a, b in p4.items()})
    p5 = problem5()
    for k in ("new", "old", "bore_only", "rough_only"):
        print("Q5", k, round(p5[k][0] / 1e3, 2), "kPa", {a: round(b, 4) for a, b in p5[k][1].items()})
    print("Q5 Q_old (L/s)", round(p5["Q_old"] * 1e3, 3), {a: round(b, 4) for a, b in p5["Q_old_detail"].items()})
    p6 = problem6(); print("Q6", {a: round(b, 4) for a, b in p6.items()})
    figures(p1, p6)
    print("figures written")


if __name__ == "__main__":
    main()
