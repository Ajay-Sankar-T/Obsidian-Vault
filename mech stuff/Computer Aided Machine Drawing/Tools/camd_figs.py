"""Computer Aided Machine Drawing (ME3283): numbers and figures for the concept notes.
   python camd_figs.py -> prints every quoted number, writes ../assets/CAMD-*.png"""
import os
from math import pi, sqrt, log10
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10})


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ------------------------------------------------------------ tolerances
def IT_values(D1, D2):
    D = sqrt(D1 * D2)
    i = 0.45 * D ** (1 / 3) + 0.001 * D
    return D, i, {g: round(m * i) for g, m in (("IT5", 7), ("IT6", 10), ("IT7", 16), ("IT8", 25), ("IT9", 40), ("IT10", 64), ("IT11", 100))}


def fits25():
    D, i, IT = IT_values(18, 30)
    out = dict(D=D, i=i, IT=IT)
    es_g = -2.5 * D ** 0.34; es_f = -5.5 * D ** 0.41; ei_k = 0.6 * D ** (1 / 3)
    out.update(es_g=es_g, es_f=es_f, ei_k=ei_k)
    hole = (0, 21)                                     # H7 for Ø25, µm (lower, upper)
    shafts = {"f7": (-41, -20), "g6": (-20, -7), "h6": (-13, 0), "k6": (2, 15), "n6": (15, 28), "p6": (22, 35), "s6": (35, 48)}
    fits = {}
    for nm, (ei, es) in shafts.items():
        c_max = hole[1] - ei                          # max clearance (negative: interference)
        c_min = hole[0] - es                          # min clearance
        kind = "clearance" if c_min >= 0 else ("interference" if c_max <= 0 else "transition")
        fits[nm] = dict(hole=hole, shaft=(ei, es), c_min=c_min, c_max=c_max, kind=kind)
    out["fits"] = fits
    out["IT_table"] = {rng: IT_values(*rng)[2] for rng in ((6, 10), (10, 18), (18, 30), (30, 50), (50, 80), (80, 120))}
    return out


def fig_tolerance(f):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.axhline(0, color="k", lw=1.2); ax.text(-0.6, 3, "basic size Ø25.000", fontsize=9)
    x = 0
    ax.add_patch(Rectangle((x, 0), 0.7, 21, fc="#bee3f8", ec=BLUE)); ax.text(x + .35, 24, "H7\n+21 / 0", ha="center", fontsize=9, color=BLUE)
    x = 1.3
    cols = {"clearance": GREEN, "transition": ORANGE, "interference": RED}
    for nm, d in f["fits"].items():
        ei, es = d["shaft"]
        ax.add_patch(Rectangle((x, ei), 0.7, es - ei, fc=cols[d["kind"]], alpha=.35, ec=cols[d["kind"]]))
        ax.text(x + .35, es + 3, nm, ha="center", fontsize=9, color=cols[d["kind"]])
        ax.text(x + .35, ei - 8, "%+d/%+d" % (es, ei), ha="center", fontsize=8, color=GREY)
        x += 1.0
    ax.set_xlim(-0.8, x + .3); ax.set_ylim(-60, 70); ax.set_xticks([]); ax.set_ylabel("deviation from the basic size (µm)")
    for k, c in cols.items():
        ax.plot([], [], "s", color=c, alpha=.5, label="H7/xx is a " + k + " fit")
    ax.legend(fontsize=8.5, loc="upper left"); ax.set_title("Ø25 hole basis: H7 against seven shaft grades (1 µm = 0.001 mm)", fontsize=10)
    save(fig, "CAMD-4-fits.png")


# ------------------------------------------------------------ roughness
def roughness():
    x = np.linspace(0, 4, 4001)
    rng = np.random.default_rng(3)
    y = 2.0 * np.sin(2 * pi * x / 0.5) + 0.6 * np.sin(2 * pi * x / 0.13) + 0.25 * rng.standard_normal(x.size)
    y -= y.mean()
    Ra = np.mean(np.abs(y))
    Rq = sqrt(np.mean(y ** 2))
    # Rz: mean of 5 sampling-length peak-to-valley
    segs = np.array_split(y, 5)
    Rz = np.mean([s.max() - s.min() for s in segs])
    f, r = 0.2, 0.8
    out = dict(Ra=Ra, Rq=Rq, Rz=Rz, Rmax_ideal=f ** 2 / (8 * r) * 1000, Ra_ideal=f ** 2 / (18 * sqrt(3) * r) * 1000, sine_Ra=2 * 2.5 / pi)
    out["x"], out["y"] = x, y
    return out


def fig_roughness(r):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw=dict(width_ratios=[1.4, 1]))
    a.plot(r["x"], r["y"], color=BLUE, lw=1)
    a.axhline(0, color="k", lw=.8, ls="--"); a.axhline(r["Ra"], color=RED, lw=1.2); a.axhline(-r["Ra"], color=RED, lw=1.2)
    a.text(4.02, r["Ra"], "+Ra", color=RED, va="center"); a.text(4.02, -r["Ra"], "−Ra", color=RED, va="center")
    a.set_xlabel("traverse length (mm)"); a.set_ylabel("height (µm)"); a.set_title("measured profile about the mean line: Ra = %.2f µm, Rz ≈ %.1f µm" % (r["Ra"], r["Rz"]), fontsize=9.5)
    a.spines[["top", "right"]].set_visible(False)
    procs = [("lapping", .025, .4), ("honing", .1, .8), ("grinding", .1, 1.6), ("reaming", .8, 3.2), ("turning", .8, 6.3), ("milling", 1.6, 6.3), ("drilling", 1.6, 12.5), ("sand casting", 12.5, 50)]
    for i, (n_, lo, hi) in enumerate(procs):
        b.barh(i, hi - lo, left=lo, color=BLUE, alpha=.7)
    b.set_xscale("log"); b.set_yticks(range(len(procs))); b.set_yticklabels([p[0] for p in procs]); b.set_xlabel("Ra (µm), typical range"); b.invert_yaxis(); b.spines[["top", "right"]].set_visible(False)
    b.set_title("what each process can reach", fontsize=9.5)
    save(fig, "CAMD-5-roughness.png")


# ------------------------------------------------------------ threads
def threads():
    out = {}
    d, P = 12.0, 1.75
    out.update(H=0.8660254 * P, d1=d - 1.0825 * P, d2=d - 0.6495 * P, At=pi / 4 * (d - 0.9382 * P) ** 2, root=d - 1.2269 * P)
    out["pitch_table"] = {6: 1.0, 8: 1.25, 10: 1.5, 12: 1.75, 16: 2.0, 20: 2.5, 24: 3.0}
    out["At_table"] = {dd: pi / 4 * (dd - 0.9382 * pp) ** 2 for dd, pp in out["pitch_table"].items()}
    out["fine_M12x1.25_At"] = pi / 4 * (12 - 0.9382 * 1.25) ** 2
    return out


def fig_thread(t):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.6))
    P = 1.75; H = t["H"]
    a.set_aspect("equal"); a.axis("off")
    xs = []
    for k in range(4):
        x0 = k * P
        crest_flat = P / 8; root_flat = P / 4
        pts = [(x0, 0), (x0 + root_flat / 2 + (P / 2 - root_flat / 2 - crest_flat / 2) * 0, 0)]
    # draw ISO profile: sharp-V height H, crest truncated H/8, root rounded H/4
    for k in range(5):
        x0 = k * P
        poly = [(x0, 0), (x0 + P / 8, 0), (x0 + P / 2 - P / 16, (5 / 8) * H), (x0 + P / 2 + P / 16, (5 / 8) * H), (x0 + 7 * P / 8, 0), (x0 + P, 0)]
        a.plot(*zip(*poly), color=BLUE, lw=2)
    a.plot([0, 5 * P], [0.625 * H + 0.15, 0.625 * H + 0.15], color=GREY, lw=.8, ls=":")
    a.annotate("", (P, -0.6), (0, -0.6), arrowprops=dict(arrowstyle="<->")); a.text(P / 2, -0.95, "pitch P", ha="center")
    a.annotate("", (-0.35, 0), (-0.35, 0.625 * H), arrowprops=dict(arrowstyle="<->")); a.text(-0.5, 0.35, "5H/8\n(thread\ndepth)", ha="right", fontsize=9)
    a.text(2.5 * P, 1.45, "60° flanks; H = 0.866 P = %.2f mm" % H, fontsize=9, ha="center")
    a.set_xlim(-2.5, 9.5); a.set_ylim(-1.4, 1.9); a.set_title("ISO metric thread profile (M12 × 1.75)", fontsize=10)
    # bolt & nut proportions
    d = 12.0
    b.set_aspect("equal"); b.axis("off")
    s = 1.5 * d + 3
    hh = 0.7 * d
    b.add_patch(Rectangle((0, 40), s, hh, fc="#e2e8f0", ec="k", lw=1.5))
    b.add_patch(Rectangle((s / 2 - d / 2, 0), d, 40, fc="#cbd5e0", ec="k", lw=1.5))
    b.plot([s / 2 - (d - 1.0825 * 1.75) / 2] * 2, [0, 28], color="k", lw=.8); b.plot([s / 2 + (d - 1.0825 * 1.75) / 2] * 2, [0, 28], color="k", lw=.8)
    b.annotate("", (s, 40 + hh + 5), (0, 40 + hh + 5), arrowprops=dict(arrowstyle="<->")); b.text(s / 2, 40 + hh + 8, "across flats s = 1.5d + 3 = %.0f" % s, ha="center", fontsize=9)
    b.annotate("", (-5, 40), (-5, 40 + hh), arrowprops=dict(arrowstyle="<->")); b.text(-7, 44, "k = 0.7d\n= %.1f" % hh, ha="right", fontsize=9)
    b.annotate("", (s / 2 + d / 2 + 4, 0), (s / 2 + d / 2 + 4, 40), arrowprops=dict(arrowstyle="<->")); b.text(s / 2 + d / 2 + 6, 20, "length", fontsize=9)
    b.add_patch(Rectangle((s + 18, 20), s, 0.8 * d, fc="#e2e8f0", ec="k", lw=1.5)); b.text(s + 18 + s / 2, 20 + 0.4 * d, "nut\nm = 0.8d\n= %.1f" % (0.8 * d), ha="center", va="center", fontsize=9)
    b.text(s / 2, -8, "hex bolt M12 (drawing proportions)", ha="center", fontsize=9)
    b.set_xlim(-25, s + 18 + s + 5); b.set_ylim(-14, 78); b.set_title("bolt and nut drawn from d only", fontsize=10)
    fig.suptitle("Screw threads", fontsize=11)
    save(fig, "CAMD-2-threads.png")


# ------------------------------------------------------------ sections
def fig_sections():
    fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.2))
    for a in axs:
        a.set_aspect("equal"); a.axis("off")
    # flanged bush: outer 40, bore 20, flange 60, length 50, flange 10
    def hatch_rect(a, x, y, w, h):
        a.add_patch(Rectangle((x, y), w, h, fc="white", ec="k", lw=1.8, hatch="////"))
    # (1) full section A-A of a flanged bush: two hatched halves (above and below the axis)
    a = axs[0]
    for sgn in (1, -1):
        y0 = 10 if sgn > 0 else -10 - 10
        hatch_rect(a, 0, sgn * 10 if sgn > 0 else -20, 50, 10) if False else None
    # upper wall (bore 20: r=10, bush outer 40: r=20) and flange (r=30, thickness 10)
    for sgn in (1, -1):
        y_in, y_out, y_fl = sgn * 10, sgn * 20, sgn * 30
        a.add_patch(Polygon([(0, y_in), (50, y_in), (50, y_out), (10, y_out), (10, y_fl), (0, y_fl)], closed=True, fc="white", ec="k", lw=1.8, hatch="////"))
    a.plot([-6, 56], [0, 0], color=RED, lw=1, ls="-.")
    a.set_xlim(-10, 60); a.set_ylim(-40, 40); a.set_title("full section: cut through the whole part;\nmaterial hatched, the bore left open", fontsize=9.5)
    # (2) half section: symmetric part: one half sectioned, the other half outside view
    a = axs[1]
    y_in, y_out, y_fl = 10, 20, 30
    a.add_patch(Polygon([(0, y_in), (50, y_in), (50, y_out), (10, y_out), (10, y_fl), (0, y_fl)], closed=True, fc="white", ec="k", lw=1.8, hatch="////"))
    a.add_patch(Rectangle((10, -20), 40, 10, fc="white", ec="k", lw=1.8)); a.add_patch(Rectangle((0, -30), 10, 20, fc="white", ec="k", lw=1.8)); a.add_patch(Rectangle((0, -10), 50, 20, fc="white", ec="none"))
    a.plot([0, 50], [-10, -10], color="k", lw=1.0, ls="--"); a.plot([0, 50], [10, 10], color="k", lw=1.8)
    a.plot([-6, 56], [0, 0], color=RED, lw=1, ls="-.")
    a.set_xlim(-10, 60); a.set_ylim(-40, 40); a.set_title("half section: a symmetric part shows\nthe inside (top) and the outside (bottom)", fontsize=9.5)
    # (3) ribs not hatched: bracket with rib and web
    a = axs[2]
    a.add_patch(Rectangle((0, 0), 60, 8, fc="white", ec="k", lw=1.8, hatch="////"))      # base plate
    a.add_patch(Rectangle((0, 8), 8, 40, fc="white", ec="k", lw=1.8, hatch="////"))      # vertical plate (section)
    a.add_patch(Polygon([(8, 8), (40, 8), (8, 36)], closed=True, fc="white", ec="k", lw=1.8))            # rib: NOT hatched when cut lengthwise
    a.text(26, 14, "rib\n(not hatched)", fontsize=8.5, color=RED, ha="center")
    a.set_xlim(-8, 70); a.set_ylim(-8, 56); a.set_title("a rib cut lengthwise is left unhatched\n(so it does not look solid)", fontsize=9.5)
    fig.suptitle("Sectional views: hatching is 45° thin lines on the cut material; the cutting plane is a chain line with arrows", fontsize=10.5)
    save(fig, "CAMD-1-sections.png")


# ------------------------------------------------------------ keys, rivets, welds
def keys_rivets():
    out = {}
    d = 40.0
    out["key"] = dict(b=d / 4, t=d / 6, L_hub=1.5 * d)
    t, d_r = 10.0, 6 * sqrt(10.0)
    dh = round(d_r + 1.5, 1) if d_r > 12 else d_r
    p = 60.0
    st, tau, sc = 100.0, 60.0, 150.0
    tear = (p - dh) * t * st
    shear = pi / 4 * dh ** 2 * tau
    crush = dh * t * sc
    out["rivet"] = dict(d=d_r, dh=dh, tear=tear, shear=shear, crush=crush, plate=p * t * st, eff=min(tear, shear, crush) / (p * t * st), head_D=1.6 * d_r, head_h=0.7 * d_r, margin=1.5 * dh)
    out["fillet"] = dict(throat=0.707 * 6, per_mm=0.707 * 6 * 80)
    return out


def fig_keys_rivets():
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.4))
    a.set_aspect("equal"); a.axis("off")
    d = 40
    a.add_patch(Circle((0, 0), d / 2, fc="#e2e8f0", ec="k", lw=1.8))
    bk, tk = d / 4, d / 6
    a.add_patch(Rectangle((-bk / 2, d / 2 - tk / 2), bk, tk * 1.0, fc="#fbd38d", ec="k", lw=1.5))
    a.add_patch(Circle((0, 0), d / 2 + 14, fill=False, ec="k", lw=1.5))
    a.text(0, -4, "Ø40", ha="center"); a.text(0, -35, "key b = d/4 = 10, t = d/6 = 6.7\n(hub length 1.5 d = 60)", ha="center", fontsize=9)
    a.text(0, 42, "keyway: half in the shaft, half in the hub", ha="center", fontsize=9, color=GREY)
    a.set_xlim(-45, 45); a.set_ylim(-45, 50); a.set_title("sunk key on a Ø40 shaft", fontsize=10)
    # rivet lap joint
    b.set_aspect("equal"); b.axis("off")
    t = 10; d_r = 6 * sqrt(10); dh = d_r + 1.5
    b.add_patch(Rectangle((0, 0), 120, t, fc="#e2e8f0", ec="k", lw=1.5)); b.add_patch(Rectangle((50, t), 120, t, fc="#cbd5e0", ec="k", lw=1.5))
    for x in (65, 125):
        b.add_patch(Rectangle((x - dh / 2, 0), dh, 2 * t, fc="#fbd38d", ec="k", lw=1.2))
        b.add_patch(Polygon([(x - 0.8 * d_r, 2 * t), (x - 0.5 * d_r, 2 * t + 0.7 * d_r), (x + 0.5 * d_r, 2 * t + 0.7 * d_r), (x + 0.8 * d_r, 2 * t)], closed=True, fc="#fbd38d", ec="k", lw=1.2))
    b.annotate("", (125, -6), (65, -6), arrowprops=dict(arrowstyle="<->")); b.text(95, -14, "pitch p = 60", ha="center", fontsize=9)
    b.text(95, 40, "d = 6√t = %.0f mm, hole %.1f, snap head Ø%.0f × %.0f" % (d_r, dh, 1.6 * d_r, 0.7 * d_r), ha="center", fontsize=9)
    b.set_xlim(-10, 180); b.set_ylim(-22, 50); b.set_title("single-riveted lap joint (t = 10 mm)", fontsize=10)
    fig.suptitle("Keys and rivets", fontsize=11)
    save(fig, "CAMD-3-keys-rivets.png")


# ------------------------------------------------------------ assembly
def fig_assembly():
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    steps = ["free bolt", "+ concentric with the hole", "+ head face on the plate"]
    dof = [6, 2, 1]
    removed = [0, 4, 1]
    ax.bar(range(3), dof, color=BLUE, alpha=.75)
    for i, (v, r) in enumerate(zip(dof, removed)):
        ax.text(i, v + .15, "%d DOF" % v, ha="center", fontsize=10)
        if r:
            ax.text(i, max(v / 2, .5), "-%d" % r, ha="center", color="white", fontsize=12, weight="bold")
    ax.set_xticks(range(3)); ax.set_xticklabels(steps, fontsize=9); ax.set_ylabel("degrees of freedom of the bolt"); ax.set_ylim(0, 7.2)
    ax.text(1.9, 4.4, "the face mate would remove 3 (one translation,\ntwo rotations), but the two rotations were\nalready gone: a redundant constraint,\nso only 1 is new", ha="right", fontsize=8.5, color=RED)
    ax.text(2, 1.7, "left: spin about the axis (harmless)", ha="center", fontsize=8.5, color=GREY)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Assembly mates are degrees-of-freedom bookkeeping (a free part has 6)", fontsize=10)
    save(fig, "CAMD-6-assembly.png")


if __name__ == "__main__":
    f = fits25(); print("fits:", {k: v for k, v in f.items() if k not in ("fits",)})
    for nm, d in f["fits"].items():
        print(" ", nm, d)
    r = roughness(); print("roughness", {k: round(v, 3) for k, v in r.items() if k not in ("x", "y")})
    t = threads(); print("threads", {k: (round(v, 3) if not isinstance(v, dict) else {a: round(b, 1) for a, b in v.items()}) for k, v in t.items()})
    k = keys_rivets(); print("keys/rivets", k)
    fig_tolerance(f); fig_roughness(r); fig_thread(t); fig_sections(); fig_keys_rivets(); fig_assembly()
