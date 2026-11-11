"""Manufacturing Technology (ME2302 / ME3305): numbers and figures for the concept notes.
   python mfg_core.py -> prints every quoted number, writes ../assets/MFG-*.png"""
import os
from math import pi, sqrt, log, exp, sin, cos, tan, atan, radians, degrees, asin
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ----------------------------------------------------------------- casting
def casting():
    B = 2.0                                  # s/mm2, sand mould (illustrative)
    r = {}
    V = 1e6
    sphere_r = (3 * V / (4 * pi)) ** (1 / 3)
    cube = V ** (1 / 3)
    cyl_D = (4 * V / pi) ** (1 / 3)
    plate = (200, 200, 25)
    shapes = {"sphere": V / (4 * pi * sphere_r ** 2), "cylinder D=H": V / (1.5 * pi * cyl_D ** 2), "cube": V / (6 * cube ** 2),
              "plate 200x200x25": V / (2 * (200 * 200 + 2 * 200 * 25))}
    r["VA"] = shapes
    r["t"] = {k: B * v ** 2 for k, v in shapes.items()}
    Vc, Ac = 200 * 200 * 50, 2 * (200 * 200 + 2 * 200 * 50)
    VAc = Vc / Ac
    tc = B * VAc ** 2
    D_riser = 6 * 1.118 * VAc                  # t_riser = 1.25 t_casting, cylinder H=D, V/A = D/6
    r.update(VAc=VAc, tc=tc, D_riser=D_riser, V_riser=pi * D_riser ** 3 / 4, V_shrink=0.03 * Vc, V_req=0.03 * Vc / 0.14)
    return r


def fig_casting(c):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    names = list(c["t"].keys()); t = [c["t"][k] / 60 for k in names]
    a.bar(range(4), t, color=[BLUE, GREEN, ORANGE, RED]); a.set_xticks(range(4)); a.set_xticklabels([n.replace(" ", "\n", 1) for n in names], fontsize=8.5)
    [a.text(i, v + 0.2, "%.1f min" % v, ha="center", fontsize=9) for i, v in enumerate(t)]
    a.set_ylabel("solidification time (min), B = 2 s/mm²"); a.set_title("same volume (10⁶ mm³), different shapes: the compact one freezes last", fontsize=9.5)
    VA = np.linspace(2, 30, 100)
    b.plot(VA, 2.0 * VA ** 2 / 60, color=BLUE, lw=2.4)
    b.plot([c["VAc"]], [c["tc"] / 60], "o", color=RED, ms=8); b.annotate("plate 200×200×50:\nV/A = %.1f mm, t = %.1f min" % (c["VAc"], c["tc"] / 60), (c["VAc"], c["tc"] / 60), (4, 12), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.plot([c["VAc"] * 1.118], [1.25 * c["tc"] / 60], "s", color=GREEN, ms=8); b.annotate("riser must reach\n1.25 t: V/A = %.1f mm" % (1.118 * c["VAc"]), (c["VAc"] * 1.118, 1.25 * c["tc"] / 60), (19, 3), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("V/A (mm)"); b.set_ylabel("t = B (V/A)² (min)"); b.set_title("Chvorinov's rule", fontsize=9.5)
    fig.suptitle("Casting: solidification time", fontsize=11)
    save(fig, "MFG-1-casting.png")


# ----------------------------------------------------------------- bulk deformation
def bulk():
    r = {}
    K, n = 600.0, 0.2
    D0, h0, h1, mu = 50.0, 60.0, 30.0, 0.1
    eps = log(h0 / h1)
    sf = K * eps ** n / (1 + n)
    A1 = pi / 4 * D0 ** 2 * h0 / h1
    r1 = sqrt(A1 / pi)
    F = sf * A1 * (1 + 2 * mu * r1 / (3 * h1)) / 1e6        # MN
    r.update(eps=eps, sf=sf, A1=A1, D1=2 * r1, F=F, F_ideal=sf * A1 / 1e6)
    R, hh0, hh1, muR = 250.0, 10.0, 8.0, 0.15
    dh = hh0 - hh1
    r.update(Lc=sqrt(R * dh), dh_max=muR ** 2 * R)
    Kw, nw = 500.0, 0.15
    d0, d1 = 6.0, 4.0
    ew = log(d0 ** 2 / d1 ** 2)
    sfw = Kw * ew ** nw / (1 + nw)
    r.update(ew=ew, sfw=sfw, draw_stress=sfw * ew, area_red=1 - (d1 / d0) ** 2, rx=(d0 / d1) ** 2)
    return r


def fig_bulk(b):
    fig, (a, c) = plt.subplots(1, 2, figsize=(11, 4.2))
    h = np.linspace(60, 20, 100)
    K, n, mu = 600, 0.2, 0.1
    eps = np.log(60 / h); sf = K * eps ** n / (1 + n)
    A = pi / 4 * 50 ** 2 * 60 / h; r = np.sqrt(A / pi)
    F = sf * A * (1 + 2 * mu * r / (3 * h)) / 1e6
    a.plot(60 - h, F, color=BLUE, lw=2.4, label="with friction μ = 0.1")
    a.plot(60 - h, sf * A / 1e6, color=GREEN, lw=1.8, ls="--", label="frictionless")
    a.plot([30], [b["F"]], "o", color=RED); a.annotate("h = 30 mm: F = %.2f MN" % b["F"], (30, b["F"]), (8, 2.5), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("reduction in height (mm), from h₀ = 60 mm"); a.set_ylabel("forging force (MN)"); a.legend(fontsize=9); a.set_title("cold upsetting a Ø50 steel billet: force climbs as the area grows", fontsize=9.5)
    muv = np.linspace(0.02, 0.4, 100)
    c.plot(muv, muv ** 2 * 250, color=BLUE, lw=2.4); c.axhline(2, color=RED, ls="--"); c.text(0.03, 2.4, "demanded draft 2 mm", color=RED, fontsize=9)
    c.set_xlabel("friction coefficient μ"); c.set_ylabel("maximum draft Δh = μ²R (mm), R = 250 mm"); c.set_title("rolling: the rolls bite only if μ² R ≥ Δh", fontsize=9.5)
    fig.suptitle("Bulk deformation", fontsize=11)
    save(fig, "MFG-2-bulk.png")


# ----------------------------------------------------------------- sheet
def sheet():
    r = {}
    t, w, TS, Dd = 2.0, 100.0, 400.0, 32.0
    r["F_bend"] = 1.33 * TS * w * t ** 2 / Dd
    R_, alpha, K = 4.0, pi / 2, 0.4
    r["BA"] = alpha * (R_ + K * t)
    d, hcup, tt, TSd = 50.0, 40.0, 1.0, 300.0
    D0 = sqrt(d ** 2 + 4 * d * hcup)
    r.update(D0=D0, DR=D0 / d, F_draw=pi * d * tt * TSd * (D0 / d - 0.7) / 1e3, blank_area_check=pi * D0 ** 2 / 4, cup_area=pi * d ** 2 / 4 + pi * d * hcup)
    r["F_blank"] = 0.7 * 400.0 * pi * 40.0 * 2.0 / 1e3
    r["clear"] = 0.075 * 2.0
    return r


def fig_sheet(s):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    d = 50; h = np.linspace(5, 90, 100)
    D0 = np.sqrt(d ** 2 + 4 * d * h)
    a.plot(h, D0 / d, color=BLUE, lw=2.4); a.axhline(2.0, color=RED, ls="--"); a.text(6, 2.03, "limiting draw ratio ≈ 2.0 (one stage)", color=RED, fontsize=9)
    a.plot([40], [s["DR"]], "o", color=ORANGE, ms=8); a.annotate("h = 40 mm: D₀/d = %.2f\nneeds a redraw" % s["DR"], (40, s["DR"]), (52, 1.5), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("cup height h (mm), Ø50 cup"); a.set_ylabel("draw ratio D₀/d"); a.set_title("cup height from constant area: D₀² = d² + 4dh", fontsize=9.5)
    # bending: neutral axis and bend allowance
    t = 2.0; R_ = 4.0
    for ang, col in ((60, GREEN), (90, BLUE), (120, ORANGE)):
        K = 0.4; BA = radians(ang) * (R_ + K * t)
        b.bar(ang, BA, width=18, color=col); b.text(ang, BA + .3, "%.1f mm" % BA, ha="center", fontsize=9)
    b.set_xlabel("bend angle (deg)"); b.set_ylabel("bend allowance BA = α(R + Kt) (mm)"); b.set_title("t = 2 mm, R = 4 mm, K = 0.4: length of the flat blank used by the bend", fontsize=9.5)
    fig.suptitle("Sheet metal", fontsize=11)
    save(fig, "MFG-3-sheet.png")


# ----------------------------------------------------------------- machining
def machining():
    r = {}
    t0, tc, alpha, w = 0.25, 0.50, radians(10), 3.0
    rr = t0 / tc
    phi = atan(rr * cos(alpha) / (1 - rr * sin(alpha)))
    gamma = 1 / tan(phi) + tan(phi - alpha)
    Fc, Ft = 1200.0, 500.0
    F = sqrt(Fc ** 2 + Ft ** 2)
    Ff = Fc * sin(alpha) + Ft * cos(alpha)
    N = Fc * cos(alpha) - Ft * sin(alpha)
    mu = Ff / N
    beta = atan(mu)
    Fs = Fc * cos(phi) - Ft * sin(phi)
    As = t0 * w / sin(phi)
    tau = Fs / As
    V = 2.0
    r.update(r=rr, phi=degrees(phi), gamma=gamma, F=F, Ff=Ff, N=N, mu=mu, beta=degrees(beta), Fs=Fs, As=As, tau=tau, P=Fc * V, u=Fc / (t0 * w),
             phi_merchant=45 + 10 / 2 - degrees(beta) / 2)
    return r


def fig_machining(m):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    rr = np.linspace(0.2, 1.0, 100)
    for al, col in ((0, GREEN), (10, BLUE), (20, ORANGE)):
        ph = np.degrees(np.arctan(rr * np.cos(np.radians(al)) / (1 - rr * np.sin(np.radians(al)))))
        a.plot(rr, ph, color=col, lw=2.2, label="rake α = %d°" % al)
    a.plot([m["r"]], [m["phi"]], "o", color=RED, ms=8); a.annotate("r = 0.5, α = 10°: φ = %.1f°" % m["phi"], (m["r"], m["phi"]), (0.55, 18), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("chip-thickness ratio r = t₀/t_c"); a.set_ylabel("shear angle φ (deg)"); a.legend(fontsize=9); a.set_title("a thicker chip (smaller r) means a smaller shear angle", fontsize=9.5)
    # force circle
    b.set_aspect("equal"); b.axis("off")
    Fc, Ft = 1200.0, 500.0
    al = radians(10); phi = radians(m["phi"])
    F = np.array([Fc, Ft])      # resultant in cutting frame (x along cut direction, y thrust)
    Fvec = F
    b.add_patch(Circle(Fvec / 2, np.hypot(*Fvec) / 2, fill=False, ec=GREY, ls="--"))
    b.annotate("", Fvec, (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=2)); b.text(Fvec[0] * .55, Fvec[1] * .75 + 40, "R = %.0f N" % m["F"], color=RED)
    b.annotate("", (Fc, 0), (0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2)); b.text(Fc / 2, -90, "F_c = 1200 N (cutting)", color=BLUE, ha="center")
    b.annotate("", (Fc, Ft), (Fc, 0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2)); b.text(Fc + 30, Ft / 2, "F_t = 500 N\n(thrust)", color=GREEN)
    b.text(0, -280, "shear force F_s = %.0f N on the shear plane (φ = %.1f°)\nfriction F = %.0f N, normal N = %.0f N, μ = %.2f (β = %.1f°)\nτ_s = %.0f MPa" % (m["Fs"], m["phi"], m["Ff"], m["N"], m["mu"], m["beta"], m["tau"]), fontsize=9)
    b.set_xlim(-100, 1500); b.set_ylim(-400, 700); b.set_title("Merchant's force circle: all forces are components of one resultant R", fontsize=9.5)
    fig.suptitle("Orthogonal cutting", fontsize=11)
    save(fig, "MFG-4-cutting.png")


# ----------------------------------------------------------------- tool life
def toollife():
    n, C = 0.25, 300.0
    r = dict(T_at_100=(C / 100) ** (1 / n), V_for_60=C / 60 ** n)
    Co, Ttc, Ct = 0.5, 2.0, 3.0
    Tc = (1 / n - 1) * (Ttc + Ct / Co)
    Vc = C / Tc ** n
    Tp = (1 / n - 1) * Ttc
    Vp = C / Tp ** n
    D, L, f, Th = 50.0, 200.0, 0.2, 1.0
    Tm = lambda V: pi * D * L / (1000 * V * f)
    cost = lambda V: Co * Th + Co * Tm(V) + (Tm(V) / (C / V) ** (1 / n)) * (Co * Ttc + Ct)
    r.update(Tc=Tc, Vc=Vc, Tp=Tp, Vp=Vp, Tm_c=Tm(Vc), cost_c=cost(Vc), cost_p=cost(Vp), cost_60=cost(C / 60 ** n), cost=cost, Tm=Tm, Co=Co, Th=Th, Ttc=Ttc, Ct=Ct, C=C, n=n)
    r["time_c"] = Th + Tm(Vc) + Tm(Vc) / Tc * Ttc
    r["time_p"] = Th + Tm(Vp) + Tm(Vp) / Tp * Ttc
    return r


def fig_toollife(t):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    V = np.linspace(40, 300, 200)
    a.loglog(V, (t["C"] / V) ** (1 / t["n"]), color=BLUE, lw=2.4)
    a.plot([100], [t["T_at_100"]], "o", color=RED); a.annotate("100 m/min: 81 min", (100, t["T_at_100"]), (150, 300), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.plot([t["V_for_60"]], [60], "s", color=GREEN); a.annotate("60 min life: %.0f m/min" % t["V_for_60"], (t["V_for_60"], 60), (150, 100), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("cutting speed V (m/min)"); a.set_ylabel("tool life T (min)"); a.set_title("Taylor: V Tⁿ = C (n = 0.25, C = 300): +10 % speed cuts the life by 32 %", fontsize=9.5)
    Vv = np.linspace(60, 260, 200)
    tm = np.array([t["Tm"](v) for v in Vv]); life = (t["C"] / Vv) ** (1 / t["n"])
    cm = t["Co"] * t["Th"] + t["Co"] * tm
    ct = tm / life * (t["Co"] * t["Ttc"] + t["Ct"])
    b.plot(Vv, cm, color=GREEN, lw=1.8, ls="--", label="machining + loading"); b.plot(Vv, ct, color=ORANGE, lw=1.8, ls="--", label="tool changes + tool cost")
    b.plot(Vv, cm + ct, color=BLUE, lw=2.6, label="total cost per part")
    b.plot([t["Vc"]], [t["cost_c"]], "o", color=RED, ms=8); b.annotate("minimum cost\nV = %.0f m/min, T = %.0f min" % (t["Vc"], t["Tc"]), (t["Vc"], t["cost_c"]), (170, 0.95), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("cutting speed V (m/min)"); b.set_ylabel("cost per part"); b.legend(fontsize=9); b.set_title("an optimum exists: slow is wasteful, fast wears tools", fontsize=9.5)
    fig.suptitle("Tool life and economics", fontsize=11)
    save(fig, "MFG-5-toollife.png")


# ----------------------------------------------------------------- fixtures & metrology
def gdt():
    r = {}
    r["virtual"] = 10.0 - 0.2
    r["total_at_LMC"] = 0.2 + (10.1 - 10.0)
    return r


def fig_fixture_gdt():
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.4))
    a.set_aspect("equal"); a.axis("off"); a.set_xlim(-1, 11.5); a.set_ylim(-1, 7)
    # isometric-ish block with locator points
    a.add_patch(Rectangle((0, 0), 6, 4, fc="#e2e8f0", ec="k", lw=1.5))
    a.add_patch(plt.Polygon([(6, 0), (8, 1.5), (8, 5.5), (6, 4)], fc="#cbd5e0", ec="k", lw=1.5))
    a.add_patch(plt.Polygon([(0, 4), (2, 5.5), (8, 5.5), (6, 4)], fc="#edf2f7", ec="k", lw=1.5))
    for x, y in ((1, 0), (5, 0), (3, 0)):
        a.plot([x], [y - .25], "o", color=RED, ms=9)
    a.text(3, -.85, "1-2-3: three points on the base", ha="center", color=RED, fontsize=9)
    for x, y in ((6.0, 0.7), (6.0, 3.3)):
        a.plot([x + .25], [y], "s", color=BLUE, ms=9)
    a.text(8.0, 2.8, "4-5: two points\non the long side", color=BLUE, fontsize=9)
    a.plot([4.4], [5.0], "^", color=GREEN, ms=10); a.text(0.2, 6.2, "6: one point on the end face", color=GREEN, fontsize=9)
    a.set_title("3-2-1 principle: six points remove six degrees of freedom", fontsize=9.5)
    D = np.linspace(10.0, 10.1, 50)
    b.plot(D, 0.2 + (D - 10.0), color=BLUE, lw=2.6)
    b.axhline(0.2, color=GREY, ls=":"); b.text(10.03, 0.21, "stated position tolerance Ø0.2 at MMC", fontsize=9, color=GREY)
    b.plot([10.1], [0.3], "o", color=RED); b.annotate("hole at LMC (Ø10.1): Ø0.3 allowed", (10.1, 0.3), (10.01, 0.27), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.set_xlabel("actual hole diameter (mm), size limits Ø10.0 to Ø10.1"); b.set_ylabel("allowed position tolerance zone (mm)"); b.set_title("MMC bonus tolerance: a larger hole may sit further off", fontsize=9.5)
    fig.suptitle("Locating, and tolerancing, a part", fontsize=11)
    save(fig, "MFG-6-fixture-gdt.png")


# ----------------------------------------------------------------- joining
def joining():
    r = {}
    eta, V, I, v = 0.8, 25.0, 200.0, 5.0
    r["HI"] = eta * V * I / v           # J/mm
    r["HI2"] = eta * V * I / 2.5
    return r


if __name__ == "__main__":
    c, b, s, m, t, g, j = casting(), bulk(), sheet(), machining(), toollife(), gdt(), joining()
    for name, d in (("casting", c), ("bulk", b), ("sheet", s), ("machining", m), ("toollife", t), ("gdt", g), ("joining", j)):
        print("---", name)
        for k, v in d.items():
            if callable(v):
                continue
            print(f"  {k:12s}", {a: round(x, 3) for a, x in v.items()} if isinstance(v, dict) else round(v, 4))
    fig_casting(c); fig_bulk(b); fig_sheet(s); fig_machining(m); fig_toollife(t); fig_fixture_gdt()
