"""Tutorial 9 (flat-face cam) and Tutorial 10 (flywheel, two-plane balancing): numbers + figures.
Run from anywhere:  python tut9_10.py        -> prints every quoted number, writes assets/T9-*.png, T10-*.png, T9-anim.gif
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon
from matplotlib.animation import FuncAnimation, PillowWriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})

# =====================================================================  TUTORIAL 9
H, R0, E = 25.0, 50.0, 15.0           # lift, base-circle radius, offset (mm)
BETA = np.pi / 2                       # rise / return angle (rad)
RPM = 100.0
W = RPM * 2 * np.pi / 60               # rad/s


def cyc(u):
    """cycloidal rise, u = phi/beta in [0,1]; returns s, ds/dtheta, d2s/dtheta2 (mm, mm/rad, mm/rad^2)"""
    s = H * (u - np.sin(2 * np.pi * u) / (2 * np.pi))
    s1 = (H / BETA) * (1 - np.cos(2 * np.pi * u))
    s2 = (2 * np.pi * H / BETA ** 2) * np.sin(2 * np.pi * u)
    return s, s1, s2


def motion(theta_deg):
    """full 360 deg law: dwell 0-90, rise 90-180, dwell 180-270, return 270-360"""
    t = np.atleast_1d(np.asarray(theta_deg, float)) % 360
    s = np.zeros_like(t); s1 = np.zeros_like(t); s2 = np.zeros_like(t)
    r = (t >= 90) & (t < 180)
    s[r], s1[r], s2[r] = cyc((t[r] - 90) / 90)
    d = (t >= 180) & (t < 270)
    s[d] = H
    b = t >= 270
    a, a1, a2 = cyc((t[b] - 270) / 90)
    s[b], s1[b], s2[b] = H - a, -a1, -a2
    return s, s1, s2


def profile(theta_deg):
    """cam-fixed coordinates of the contact point (cam rotates CCW, follower on the +y axis)"""
    s, s1, _ = motion(theta_deg)
    th = np.radians(theta_deg)
    xg, yg = s1, R0 + s                # ground frame: contact lies s1 to the right of O, at height R0+s
    x, y = xg * np.cos(th) + yg * np.sin(th), -xg * np.sin(th) + yg * np.cos(th)
    if np.ndim(theta_deg) == 0:
        return float(x[0]), float(y[0])
    return x, y


def t9_numbers():
    n = {}
    n["omega"] = W
    n["vmax"] = 2 * H * W / BETA / 1000          # m/s
    n["amax"] = 2 * np.pi * H * W ** 2 / BETA ** 2 / 1000   # m/s^2
    th = 120.0                                     # 30 deg into the rise (rise starts at 90 deg)
    s, s1, s2 = motion(th)
    n["s30"], n["s1_30"], n["s2_30"] = s[0], s1[0], s2[0]
    n["rho30"] = R0 + s[0] + s2[0]
    n["ecc30_rise_side"] = s1[0] - E
    n["ecc30_other"] = s1[0] + E
    n["v30"] = s1[0] * W / 1000
    n["a30"] = s2[0] * W ** 2 / 1000
    tt = np.linspace(0, 360, 36001)
    S, S1, S2 = motion(tt)
    n["rho_min"] = (R0 + S + S2).min()
    n["rho_min_at"] = tt[(R0 + S + S2).argmin()]
    n["s1max"] = S1.max()
    n["face_half"] = np.abs(S1).max() + E
    n["ecc_max_rise"] = np.abs(S1[(tt >= 90) & (tt <= 180)] - E).max()
    n["ecc_max_return"] = np.abs(S1[(tt >= 270)] - E).max()
    # numerical cross-check of vmax/amax from finite differences of s(t)
    dt = np.radians(0.001) / W
    ss = motion(np.degrees(W * np.arange(0, 2 * np.pi / W, dt))[::50])[0]
    return n


def fig_t9_motion():
    th = np.linspace(0, 360, 1441)
    s, s1, s2 = motion(th)
    v, a = s1 * W / 1000, s2 * W ** 2 / 1000
    fig, ax = plt.subplots(3, 1, figsize=(8, 7.2), sharex=True)
    for x in (90, 180, 270):
        for a_ in ax:
            a_.axvline(x, color=GREY, lw=.6, ls=":")
    ax[0].plot(th, s, color=BLUE, lw=2); ax[0].set_ylabel("displacement s (mm)")
    ax[1].plot(th, v, color=GREEN, lw=2); ax[1].set_ylabel("velocity (m/s)")
    ax[2].plot(th, a, color=RED, lw=2); ax[2].set_ylabel("acceleration (m/s²)")
    n = t9_numbers()
    ax[1].annotate(f"v_max = {n['vmax']:.3f} m/s", (135, n["vmax"]), (190, n["vmax"] * .72), arrowprops=dict(arrowstyle="->", color=GREY))
    ax[2].annotate(f"a_max = {n['amax']:.2f} m/s²", (112.5, n["amax"]), (190, n["amax"] * .8), arrowprops=dict(arrowstyle="->", color=GREY))
    ax[0].plot([120], [n["s30"]], "o", color=ORANGE); ax[0].annotate("30° into rise\ns = %.2f mm" % n["s30"], (120, n["s30"]), (150, 4), arrowprops=dict(arrowstyle="->", color=GREY))
    for a_ in ax:
        a_.axvline(120, color=ORANGE, lw=1, ls="--")
    for x, t in ((45, "dwell"), (135, "rise"), (225, "dwell"), (315, "return")):
        ax[0].text(x, H * 1.08, t, ha="center", color=GREY)
    ax[0].set_ylim(-2, H * 1.25)
    ax[2].set_xlabel("cam angle θ (deg), 100 rpm"); ax[2].set_xticks(range(0, 361, 30))
    fig.suptitle("Tutorial 9 · cycloidal rise and return, 25 mm lift in 90°", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T9-fig1-motion.png"), dpi=150); plt.close(fig)


def face_line(th_deg, half=(-36, 36)):
    """face of the follower at cam angle th, drawn in the cam-fixed frame (inversion)"""
    s, s1, _ = motion(th_deg)
    th = np.radians(th_deg)
    xs = np.array(half, float)
    yg = np.full(2, R0 + s[0])
    return xs * np.cos(th) + yg * np.sin(th), -xs * np.sin(th) + yg * np.cos(th)


def fig_t9_profile():
    n = t9_numbers()
    th = np.linspace(0, 360, 2881)
    x, y = profile(th)
    fig, ax = plt.subplots(figsize=(6.6, 6.6))
    ax.add_patch(Polygon(np.c_[x, y], closed=True, fc="#fdebd0", ec="none"))
    # colour the four phases
    for lo, hi, c, lab in ((0, 90, GREY, "dwell"), (90, 180, RED, "rise"), (180, 270, GREY, "dwell"), (270, 360, BLUE, "return")):
        m = (th >= lo) & (th <= hi)
        ax.plot(x[m], y[m], color=c, lw=2.4)
    ax.add_patch(Circle((0, 0), R0, fill=False, ls="--", ec=GREY, lw=1))
    ax.add_patch(Circle((0, 0), E, fill=False, ls=":", ec=PURPLE, lw=1))
    ax.plot(0, 0, "k+", ms=10)
    # follower position at theta = 120 deg  (inverted: axis rotates clockwise)
    thc = 120.0
    fx, fy = face_line(thc, (-40, 40))
    ax.plot(fx, fy, color=ORANGE, lw=3)
    cx, cy = profile(thc); ax.plot(cx, cy, "o", color=ORANGE, ms=8, zorder=5)
    t = np.radians(thc)
    # follower axis (offset to the rise side) in the inverted frame
    ax_dir = np.array([np.sin(t), np.cos(t)]); ax_nrm = np.array([np.cos(t), -np.sin(t)])
    p0 = E * ax_nrm - 20 * ax_dir; p1 = E * ax_nrm + (R0 + n["s30"]) * ax_dir
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=PURPLE, lw=1.2, ls="-.")
    ax.annotate("contact point at 30° into rise\nρ = %.1f mm,  ε = %.1f mm" % (n["rho30"], n["ecc30_rise_side"]), (cx, cy), (cx - 38, cy - 40), arrowprops=dict(arrowstyle="->", color=ORANGE), color=ORANGE, fontsize=9)
    ax.text(0, R0 + 6, "base circle 50", color=GREY, ha="center", fontsize=8)
    ax.text(72, -32, "rise", color=RED, fontsize=11, ha="center")
    ax.text(-80, 52, "return", color=BLUE, fontsize=11, ha="center")
    ax.set_aspect("equal"); ax.set_xlim(-95, 95); ax.set_ylim(-95, 95)
    ax.set_title("Tutorial 9a · cam profile (cam-fixed view, anticlockwise rotation)\ndashed = base circle, dotted = offset circle (15 mm); orange = face at θ = 120°", fontsize=9.5)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T9-fig2-profile.png"), dpi=150); plt.close(fig)


def fig_t9_graphical():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 5.4), gridspec_kw=dict(width_ratios=[1, 1.05]))
    N = 6
    phi = np.arange(N + 1) * 90 / N
    u = phi / 90
    s, s1, _ = cyc(u)
    r = H / (2 * np.pi)
    # ---- displacement diagram with the textbook cycloid construction
    a1.set_aspect("auto"); a1.grid(False)
    a1.plot([0, 90], [0, H], color=GREY, lw=1, ls="--")                # diagonal (uniform rise)
    ang = np.radians(-60 * np.arange(N + 1))                           # points on the generating circle
    cxs, cys = -9 + r * np.cos(np.linspace(0, 2 * np.pi, 200)) * 90 / 25 * 0 + 0, 0
    # the circle (radius h/2pi) is drawn on the displacement axis; x is stretched so it looks round
    k = 3.0
    circ_x = -14 + r * k * np.cos(np.linspace(0, 2 * np.pi, 200)); circ_y = r * np.sin(np.linspace(0, 2 * np.pi, 200))
    a1.plot(circ_x, circ_y, color=PURPLE, lw=1.2)
    for i in range(N + 1):
        py = r * np.sin(ang[i])
        a1.plot([-14 + r * k * np.cos(ang[i]), 0], [py, py], color=PURPLE, lw=.8, ls=":")
        a1.plot([-14 + r * k * np.cos(ang[i])], [py], "o", color=PURPLE, ms=3)
        # parallel to the diagonal through (0, py)
        a1.plot([0, phi[i]], [py, py + H * u[i]], color=GREY, lw=.8)
        a1.plot([phi[i], phi[i]], [0, s[i]], color=BLUE, lw=.8, ls="-")
        a1.text(phi[i], -2.2, str(i), ha="center", fontsize=9)
        a1.text(phi[i] + 1.2, s[i] - 1.2, f"{s[i]:.2f}", fontsize=8, color=BLUE)
    a1.plot(np.linspace(0, 90, 200), cyc(np.linspace(0, 1, 200))[0], color=RED, lw=2)
    a1.plot(phi, s, "o", color=RED, ms=5)
    a1.text(-14, -r - 6.5, "circle Ø = h/π = 7.96 mm\n(6 equal arcs)", ha="center", fontsize=8, color=PURPLE)
    a1.set_xlim(-30, 98); a1.set_ylim(-11, 28)
    a1.set_xlabel("cam rotation φ during rise (deg), 6 × 15°"); a1.set_ylabel("follower lift s (mm)")
    a1.set_title("b · displacement diagram: cycloid by construction", fontsize=10)
    # ---- inversion: face lines
    th0 = 90
    a2.set_aspect("equal"); a2.grid(False)
    a2.add_patch(Circle((0, 0), R0, fill=False, ls="--", ec=GREY, lw=1))
    a2.add_patch(Circle((0, 0), E, fill=False, ls=":", ec=PURPLE, lw=1))
    tt = np.linspace(90, 180, 400); px, py_ = profile(tt)
    a2.plot(px, py_, color=RED, lw=2)
    cols = plt.cm.viridis(np.linspace(0, .85, N + 1))
    for i in range(N + 1):
        th = th0 + phi[i]
        fx, fy = face_line(th, (-40, 40))
        a2.plot(fx, fy, color=cols[i], lw=1.2)
        t = np.radians(th)
        ax_dir = np.array([np.sin(t), np.cos(t)]); nrm = np.array([np.cos(t), -np.sin(t)])
        p0 = E * nrm; p1 = E * nrm + (R0 + s[i]) * ax_dir
        a2.plot([p0[0], p1[0]], [p0[1], p1[1]], color=cols[i], lw=.7, ls="-.")
        cx, cy = profile(th); a2.plot(cx, cy, "o", color=cols[i], ms=4)
        a2.text(*(np.array([cx, cy]) * 1.12 + nrm * 6), str(i), color=cols[i], fontsize=9, ha="center", va="center")
    a2.plot(0, 0, "k+", ms=9)
    a2.set_xlim(-20, 98); a2.set_ylim(-98, 20)
    a2.set_title("b · inversion: faces at distance 50 + s, perpendicular to the\nrotating axis (tangent to the offset circle); envelope = profile", fontsize=9.5)
    fig.suptitle("Tutorial 9b · graphical construction of the rise, six equal steps (position 0 = start of rise at θ = 90°)", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T9-fig3-graphical.png"), dpi=150); plt.close(fig)
    return phi, s


def fig_t9_rho():
    n = t9_numbers()
    th = np.linspace(0, 360, 1441)
    s, s1, s2 = motion(th)
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4))
    a.plot(th, R0 + s + s2, color=BLUE, lw=2)
    a.axhline(0, color="k", lw=.8)
    a.fill_between(th, 0, R0 + s + s2, color=BLUE, alpha=.1)
    a.plot([120], [n["rho30"]], "o", color=ORANGE); a.annotate("ρ = %.1f mm\nat 30° into rise" % n["rho30"], (120, n["rho30"]), (160, 100), arrowprops=dict(arrowstyle="->", color=GREY))
    a.plot([n["rho_min_at"]], [n["rho_min"]], "o", color=RED); a.annotate("ρ_min = %.1f mm" % n["rho_min"], (n["rho_min_at"], n["rho_min"]), (200, 30), arrowprops=dict(arrowstyle="->", color=GREY))
    a.set_xlabel("cam angle θ (deg)"); a.set_ylabel("radius of curvature ρ = R₀ + s + s″ (mm)"); a.set_title("ρ stays positive, so the profile is convex", fontsize=10); a.set_xticks(range(0, 361, 90))
    b.plot(th, s1 - E, color=GREEN, lw=2, label="offset on the rise side (e = +15)")
    b.plot(th, s1 + E, color=GREY, lw=1.4, ls="--", label="offset on the other side (e = −15)")
    b.axhline(0, color="k", lw=.8)
    b.plot([120, 120], [n["ecc30_rise_side"], n["ecc30_other"]], "o", color=ORANGE)
    b.annotate("%.2f mm" % n["ecc30_rise_side"], (120, n["ecc30_rise_side"]), (135, -22), arrowprops=dict(arrowstyle="->", color=GREY))
    b.annotate("%.2f mm" % n["ecc30_other"], (120, n["ecc30_other"]), (150, 52.5), arrowprops=dict(arrowstyle="->", color=GREY))
    b.axvspan(90, 180, color=RED, alpha=.06); b.text(135, -50, "driving effort", ha="center", color=RED, fontsize=8)
    b.set_xlabel("cam angle θ (deg)"); b.set_ylabel("eccentricity of driving effort ε = s′ − e (mm)"); b.set_title("which side the offset goes matters", fontsize=10); b.legend(fontsize=8, loc="upper right"); b.set_ylim(-55, 64); b.set_xticks(range(0, 361, 90))
    fig.suptitle("Tutorial 9d · curvature and driving-effort eccentricity over the whole cycle", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T9-fig4-rho-ecc.png"), dpi=150); plt.close(fig)


def anim_t9():
    th_all = np.linspace(0, 360, 721)
    cx, cy = profile(th_all)
    fig, ax = plt.subplots(figsize=(4.6, 4.8))
    ax.set_aspect("equal"); ax.set_xlim(-75, 75); ax.set_ylim(-70, 110); ax.axis("off")
    cam = Polygon(np.c_[cx, cy], closed=True, fc="#fdebd0", ec=BLUE, lw=2)
    ax.add_patch(cam)
    ax.plot(0, 0, "k+", ms=10)
    face, = ax.plot([], [], color=ORANGE, lw=4)
    stem, = ax.plot([], [], color=ORANGE, lw=4)
    dot, = ax.plot([], [], "o", color=RED, ms=7, zorder=5)
    ax.plot([E, E], [R0 + 28, 108], color=PURPLE, lw=.8, ls="-.")
    txt = ax.text(0, -62, "", ha="center", fontsize=9)
    ph = ax.text(0, 102, "", ha="center", fontsize=10, color=GREY)

    def upd(i):
        th = i * 6.0
        s, s1, _ = motion(th)
        r = np.radians(th)
        c, sn = np.cos(r), np.sin(r)
        pts = np.c_[cx, cy] @ np.array([[c, sn], [-sn, c]])      # rotate CCW by theta
        cam.set_xy(pts)
        y = R0 + s[0]
        face.set_data([-36, 36], [y, y]); stem.set_data([E, E], [y, y + 16])
        dot.set_data([s1[0]], [y])
        txt.set_text("θ = %3d°   s = %5.2f mm" % (th, s[0]))
        phase = "dwell" if (th < 90 or 180 <= th < 270) else ("rise" if th < 180 else "return")
        ph.set_text(phase)
        return cam, face, stem, dot, txt, ph

    an = FuncAnimation(fig, upd, frames=60, interval=70, blit=False)
    an.save(os.path.join(OUT, "T9-anim.gif"), writer=PillowWriter(fps=14), dpi=70)
    plt.close(fig)


# =====================================================================  TUTORIAL 10 Q1  (flywheel)
AREAS = {"suction": .45e-3, "compression": 1.7e-3, "expansion": 6.8e-3, "exhaust": .65e-3}
SCALE = 3e6                                   # J per m^2 of diagram area
N1, N2, K = 202.0, 198.0, 1.2


def t10_flywheel():
    n = {}
    E_ = {k: v * SCALE for k, v in AREAS.items()}
    n["E"] = E_
    Wnet = E_["expansion"] - E_["suction"] - E_["compression"] - E_["exhaust"]
    n["Wnet"] = Wnet
    n["Tmean"] = Wnet / (4 * np.pi)
    n["Tmax"] = 2 * E_["expansion"] / np.pi
    n["DE_width"] = np.pi * (1 - n["Tmean"] / n["Tmax"])
    n["dE"] = .5 * n["DE_width"] * (n["Tmax"] - n["Tmean"])
    n["wmean"] = (N1 + N2) / 2 * 2 * np.pi / 60
    n["Cs"] = (N1 - N2) / ((N1 + N2) / 2)
    n["I"] = n["dE"] / (n["wmean"] ** 2 * n["Cs"])
    w1, w2 = N1 * 2 * np.pi / 60, N2 * 2 * np.pi / 60
    n["I_exact"] = n["dE"] / (.5 * (w1 ** 2 - w2 ** 2))
    n["m"] = n["I"] / K ** 2
    # numerical check by integrating the full torque curve
    th, T = torque_curve()
    d = T - n["Tmean"]
    En = np.concatenate([[0], np.cumsum((d[1:] + d[:-1]) / 2 * np.diff(th))])
    n["dE_num"] = En.max() - En.min()
    n["cycle_net_num"] = En[-1]
    n["th"], n["E_curve"] = th, En
    return n


def torque_curve(npts=40001):
    th = np.linspace(0, 4 * np.pi, npts)
    T = np.zeros_like(th)
    amp = {k: 2 * v * SCALE / np.pi for k, v in AREAS.items()}
    order = [("suction", -1), ("compression", -1), ("expansion", 1), ("exhaust", -1)]
    for i, (k, sg) in enumerate(order):
        x = (th - i * np.pi) / np.pi
        m = (x >= 0) & (x <= 1)
        T[m] = sg * amp[k] * (1 - np.abs(2 * x[m] - 1))
    return th, T


def fig_t10_flywheel():
    n = t10_flywheel()
    th, T = torque_curve()
    fig, (a, b) = plt.subplots(2, 1, figsize=(9, 7.6), sharex=True)
    a.plot(th / np.pi, T / 1e3, color=BLUE, lw=2)
    a.axhline(0, color="k", lw=.8)
    a.axhline(n["Tmean"] / 1e3, color=RED, lw=1.5)
    a.text(0.05, n["Tmean"] / 1e3 + .35, "T_mean = %.1f N·m (uniform resisting torque)" % n["Tmean"], color=RED, fontsize=9)
    x0 = 2 + .5 * n["Tmean"] / n["Tmax"]; x1 = 3 - .5 * n["Tmean"] / n["Tmax"]
    a.fill([x0, 2.5, x1], [n["Tmean"] / 1e3, n["Tmax"] / 1e3, n["Tmean"] / 1e3], color=ORANGE, alpha=.5)
    a.text(2.5, n["Tmax"] / 1e3 * .55, "ΔE\n%.0f J" % n["dE"], ha="center", fontsize=10)
    a.text(2.5, n["Tmax"] / 1e3 + .3, "T_max = %.0f" % n["Tmax"], ha="center", fontsize=9)
    a.text(1.0, -4.2 / 1.0 * 0.3, "")
    for i, (k, v) in enumerate(n["E"].items()):
        a.text(i + .5, (-4.4 if k != "expansion" else 3.2), "%s\n%d J" % (k, v), ha="center", fontsize=8.5, color=GREY)
    a.set_ylabel("engine torque (kN·m)"); a.set_ylim(-5.2, 14.5)
    a.set_title("Tutorial 10 Q1 · turning-moment diagram, one cycle = 4π (720°)", fontsize=10.5)
    b.plot(n["th"] / np.pi, n["E_curve"] / 1e3, color=GREEN, lw=2)
    imax, imin = n["E_curve"].argmax(), n["E_curve"].argmin()
    b.plot(n["th"][[imax, imin]] / np.pi, n["E_curve"][[imax, imin]] / 1e3, "o", color=RED)
    b.annotate("max at E", (n["th"][imax] / np.pi, n["E_curve"][imax] / 1e3), (3.1, n["E_curve"][imax] / 1e3 - 3), arrowprops=dict(arrowstyle="->", color=GREY))
    b.annotate("min at D", (n["th"][imin] / np.pi, n["E_curve"][imin] / 1e3), (.9, n["E_curve"][imin] / 1e3 + 4), arrowprops=dict(arrowstyle="->", color=GREY))
    xe = n["th"][imax] / np.pi
    b.annotate("", (xe + .12, n["E_curve"][imax] / 1e3), (xe + .12, n["E_curve"][imin] / 1e3), arrowprops=dict(arrowstyle="<->", color=ORANGE))
    b.text(xe + .17, (n["E_curve"][imax] + n["E_curve"][imin]) / 2e3, "ΔE = %.0f J" % n["dE_num"], color=ORANGE, fontsize=10, va="center")
    b.set_ylabel("kinetic energy above start (kJ)"); b.set_xlabel("crank angle θ / π"); b.set_xticks(range(0, 5))
    b.set_title("energy stored in the flywheel: ∫(T − T_mean) dθ closes after 4π", fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T10-fig1-turning-moment.png"), dpi=150); plt.close(fig)


def fig_t10_sizing():
    n = t10_flywheel()
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4))
    cs = np.linspace(.005, .06, 200)
    a.plot(cs * 100, n["dE"] / (n["wmean"] ** 2 * cs) / K ** 2, color=BLUE, lw=2)
    a.plot([n["Cs"] * 100], [n["m"]], "o", color=RED, ms=8)
    a.annotate("202–198 rpm\nCs = 2 %%  →  %.0f kg" % n["m"], (n["Cs"] * 100, n["m"]), (3.4, n["m"] * 1.25), arrowprops=dict(arrowstyle="->", color=GREY))
    a.set_xlabel("coefficient of fluctuation of speed Cs (%)"); a.set_ylabel("flywheel mass (kg)"); a.set_title("m ∝ 1/Cs: half the ripple, twice the iron", fontsize=10)
    k = np.linspace(.6, 2.0, 200)
    b.plot(k, n["I"] / k ** 2, color=GREEN, lw=2)
    b.plot([K], [n["m"]], "o", color=RED, ms=8)
    b.annotate("k = 1.2 m  →  %.0f kg" % n["m"], (K, n["m"]), (1.4, n["m"] * 1.4), arrowprops=dict(arrowstyle="->", color=GREY))
    b.set_xlabel("radius of gyration k (m)"); b.set_ylabel("flywheel mass (kg)"); b.set_title("m ∝ 1/k²: I = %.0f kg·m² is fixed, put the mass at the rim" % n["I"], fontsize=10)
    fig.suptitle("Tutorial 10 Q1 · what sets the flywheel mass", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T10-fig2-sizing.png"), dpi=150); plt.close(fig)


# =====================================================================  TUTORIAL 10 Q2  (two-plane balancing)
ZA, ZC, ZD, ZB = -15.0, 0.0, 50.0, 65.0        # cm along the axis, origin at plane C
MT, RT, RCD = 2.0, 15.0, 10.0
ANG = {"A1": 90.0, "A2": -30.0, "B2": 150.0, "B1": -60.0}      # degrees, anticlockwise from the +x axis of the end view


def cplx(a):
    return np.exp(1j * np.radians(a))


def t10_balance():
    n = {}
    FA = MT * RT * (cplx(ANG["A1"]) + cplx(ANG["A2"]))
    FB = MT * RT * (cplx(ANG["B1"]) + cplx(ANG["B2"]))
    FD = (FA * (ZA - ZC) + FB * (ZB - ZC)) / (ZD - ZC)           # moments about plane C
    FC = FA + FB - FD                                            # forces
    n.update(FA=FA, FB=FB, FC=FC, FD=FD)
    for k, F in (("C", FC), ("D", FD)):
        mass = abs(F) / RCD
        add = np.degrees(np.angle(F)) % 360
        rem = (add + 180) % 360
        n[k] = dict(mass=mass, add=add, remove=rem, cw_from_A1_remove=(90 - rem) % 360, cw_from_A1_add=(90 - add) % 360)
    # residual: rotor unbalance U = -(trial system); correction = remove (= -mass at rem) in C and D
    corrF = -(n["C"]["mass"] * RCD * cplx(n["C"]["remove"]) + n["D"]["mass"] * RCD * cplx(n["D"]["remove"]))
    corrM = -(n["C"]["mass"] * RCD * cplx(n["C"]["remove"]) * ZC + n["D"]["mass"] * RCD * cplx(n["D"]["remove"]) * ZD)
    Utrial_F = FA + FB
    Utrial_M = FA * ZA + FB * ZB
    n["resid_F"] = abs(-Utrial_F + corrF)         # rotor U = -T ; plus correction must vanish
    n["resid_M"] = abs(-Utrial_M + corrM)
    return n


def fig_t10_geometry():
    n = t10_balance()
    fig = plt.figure(figsize=(11.5, 4.9))
    ax = fig.add_axes([.03, .12, .52, .78])
    ax.set_xlim(-30, 80); ax.set_ylim(-24, 30); ax.axis("off"); ax.set_aspect("equal")
    ax.plot([-25, 75], [0, 0], color=GREY, lw=1, ls="-.")
    ax.add_patch(plt.Rectangle((ZC, -9), ZD - ZC, 18, fc="#e2e8f0", ec=GREY))
    ax.add_patch(plt.Rectangle((ZA, -5), ZC - ZA, 10, fc="#edf2f7", ec=GREY))
    ax.add_patch(plt.Rectangle((ZD, -5), ZB - ZD, 10, fc="#edf2f7", ec=GREY))
    for z, lab, col in ((ZA, "A", RED), (ZC, "C", BLUE), (ZD, "D", BLUE), (ZB, "B", RED)):
        ax.plot([z, z], [-13, 13], color=col, lw=2)
        ax.text(z, -17, lab, ha="center", fontsize=13, color=col, fontweight="bold")
    ax.plot([ZA, ZA], [0, RT * .6], "o-", color=RED, ms=0)   # no-op to keep ordering
    for (z0, z1, y, t) in ((ZA, ZC, 25, "15"), (ZC, ZD, 25, "50"), (ZD, ZB, 25, "15")):
        ax.annotate("", (z1, y), (z0, y), arrowprops=dict(arrowstyle="<->", color=GREY))
        ax.text((z0 + z1) / 2, y + 1.2, t + " cm", ha="center", fontsize=9)
    ax.text(ZA, 14.5, "2 × 2 kg\nat r = 15", ha="center", fontsize=8, color=RED)
    ax.text(ZB, 14.5, "2 × 2 kg\nat r = 15", ha="center", fontsize=8, color=RED)
    ax.text(ZC, -22, "r = 10 cm: remove material", fontsize=8, color=BLUE, ha="left")
    ax.set_title("side view: planes along the shaft", fontsize=10)
    # end view
    ax2 = fig.add_axes([.58, .08, .4, .84]); ax2.set_aspect("equal"); ax2.axis("off"); ax2.set_xlim(-24, 24); ax2.set_ylim(-24, 24)
    ax2.add_patch(Circle((0, 0), RT, fill=False, ec=GREY, ls="--"))
    ax2.plot([-20, 20], [0, 0], color=GREY, lw=.6, ls=":"); ax2.plot([0, 0], [-20, 20], color=GREY, lw=.6, ls=":")
    for k, a in ANG.items():
        p = RT * cplx(a)
        ax2.plot([0, p.real], [0, p.imag], color=RED, lw=1.2)
        ax2.plot(p.real, p.imag, "o", ms=10, mfc="white", mec=RED, mew=2)
        q = (RT + 3.2) * cplx(a); ax2.text(q.real, q.imag, k, ha="center", va="center", fontsize=11, color=RED, fontweight="bold")
    for (a0, a1, r, t) in ((90, 150, 6, "60°"), (90, -30, 9, "120°"), (150, 300, 11, "150°")):
        arr = np.radians(np.linspace(a0, a1 if a1 > a0 or a0 != 150 else a1, 40)) if a0 != 90 or a1 > 0 else np.radians(np.linspace(a0, a1, 40))
        ax2.plot(r * np.cos(arr), r * np.sin(arr), color=GREY, lw=1)
    ax2.text(-5.5, 8.2, "60°", fontsize=9); ax2.text(8.8, 5.5, "120°", fontsize=9); ax2.text(-14.5, -6.5, "150°", fontsize=9)
    ax2.set_title("end view from plane A: trial masses (2 kg each, r = 15 cm)", fontsize=10)
    fig.savefig(os.path.join(OUT, "T10-fig3-geometry.png"), dpi=150); plt.close(fig)


def fig_t10_result():
    n = t10_balance()
    fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.5))
    # force polygon (kg.cm)  FA + FB  vs  FC + FD
    a = axs[0]; a.set_aspect("equal"); a.grid(True, alpha=.25)
    pts = [0, n["FA"], n["FA"] + n["FB"]]
    a.annotate("", (pts[1].real, pts[1].imag), (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    a.annotate("", (pts[2].real, pts[2].imag), (pts[1].real, pts[1].imag), arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    c = n["FC"]; d = n["FD"]
    a.annotate("", (c.real, c.imag), (0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    a.annotate("", ((c + d).real, (c + d).imag), (c.real, c.imag), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    a.text(pts[1].real / 2 + 1, pts[1].imag / 2 - 3, "F_A = 30", color=RED); a.text((pts[1] + n["FB"] / 2).real + 1, (pts[1] + n["FB"] / 2).imag - 3, "F_B = 15.5", color=RED)
    a.text(c.real / 2 + 1, c.imag / 2 + 1, "F_C = %.1f" % abs(c), color=BLUE); a.text((c + d / 2).real - 14, (c + d / 2).imag - 1, "F_D = %.1f" % abs(d), color=BLUE)
    a.set_xlim(-20, 45); a.set_ylim(-25, 30)
    a.set_title("force polygon (kg·cm): A+B = C+D\nboth routes end at the same point", fontsize=9.5)
    # moment (couple) polygon about plane C : FA*(ZA-ZC), FB*(ZB-ZC), FD*(ZD-ZC)
    b = axs[1]; b.set_aspect("equal"); b.grid(True, alpha=.25)
    mA = n["FA"] * (ZA - ZC); mB = n["FB"] * (ZB - ZC); mD = n["FD"] * (ZD - ZC)
    p = [0, mA, mA + mB]
    b.annotate("", (mA.real, mA.imag), (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    b.annotate("", ((mA + mB).real, (mA + mB).imag), (mA.real, mA.imag), arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    b.annotate("", (mD.real, mD.imag), (0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    b.text(mA.real - 150, mA.imag + 20, "F_A·(−15)", color=RED); b.text(mA.real / 2 + 80, (mA + mB / 2).imag + 120, "F_B·65", color=RED); b.text(mD.real - 340, mD.imag - 50, "F_D·50", color=BLUE)
    b.set_xlim(-1300, 700); b.set_ylim(-1300, 700)
    b.set_title("moment polygon about plane C (kg·cm²):\nF_D·50 closes it", fontsize=9.5)
    # final answer end view
    e = axs[2]; e.set_aspect("equal"); e.axis("off"); e.set_xlim(-16, 16); e.set_ylim(-16, 16)
    e.add_patch(Circle((0, 0), RCD, fill=False, ec=GREY, ls="--"))
    e.plot([-14, 14], [0, 0], color=GREY, lw=.6, ls=":"); e.plot([0, 0], [-14, 14], color=GREY, lw=.6, ls=":")
    for k, col in (("C", BLUE), ("D", PURPLE)):
        add = RCD * cplx(n[k]["add"]); rem = RCD * cplx(n[k]["remove"])
        e.plot([add.real], [add.imag], "o", mfc="white", mec=col, ms=8, ls="", alpha=.6)
        e.annotate("", (rem.real, rem.imag), (0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2))
        e.plot(rem.real, rem.imag, "x", color=col, ms=12, mew=3)
        q = (RCD + 4.6) * cplx(n[k]["remove"])
        e.text(q.real, q.imag, "remove %s\n%.2f kg at %.1f° CW from A₁" % (k, n[k]["mass"], n[k]["cw_from_A1_remove"]), ha="center", va="center", fontsize=8.5, color=col)
    A1 = RCD * cplx(90); e.annotate("A₁ ref", (A1.real, A1.imag), (A1.real + 2, A1.imag + 3.5), fontsize=8, color=GREY)
    e.set_title("answer: material to remove at r = 10 cm\n(hollow dots = the equivalent mass to add)", fontsize=9.5)
    fig.suptitle("Tutorial 10 Q2 · two-plane balance through planes C and D", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T10-fig4-balance.png"), dpi=150); plt.close(fig)


# =====================================================================
def fig_t10_result():          # replaces the first draft above
    n = t10_balance()
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.8))
    FA, FB, FC, FD = n["FA"], n["FB"], n["FC"], n["FD"]

    def arrow(a, p, q, col, lab=None, ls="-"):
        a.annotate("", (q.real, q.imag), (p.real, p.imag), arrowprops=dict(arrowstyle="->", color=col, lw=2, ls=ls))
        if lab:
            a.plot([], [], color=col, lw=2, ls=ls, label=lab)

    a = axs[0]; a.set_aspect("equal")
    arrow(a, 0j, FA, RED, "F_A = 30.0 at 30°"); arrow(a, FA, FA + FB, RED, "F_B = 15.5 at 225°")
    arrow(a, 0j, FC, BLUE, "F_C = %.1f at %.0f°" % (abs(FC), np.degrees(np.angle(FC)))); arrow(a, FC, FC + FD, BLUE, "F_D = %.1f at %.0f°" % (abs(FD), np.degrees(np.angle(FD)) % 360))
    a.plot([(FA + FB).real], [(FA + FB).imag], "ko", ms=5)
    a.set_xlim(-5, 45); a.set_ylim(-8, 30); a.legend(fontsize=8, loc="lower right")
    a.set_title("force polygon (kg·cm): A + B and C + D\nend at the same point", fontsize=9.5)
    b = axs[1]; b.set_aspect("equal")
    mA, mB, mD = FA * (ZA - ZC), FB * (ZB - ZC), FD * (ZD - ZC)
    arrow(b, 0j, mA, RED, "F_A·(−15)"); arrow(b, mA, mA + mB, RED, "F_B·65")
    arrow(b, 0j, mD, BLUE, "F_D·50")
    b.plot([(mA + mB).real], [(mA + mB).imag], "ko", ms=5)
    b.set_xlim(-1300, 200); b.set_ylim(-1200, 200); b.legend(fontsize=8, loc="upper right")
    b.set_title("moment polygon about plane C (kg·cm²):\nA and B couples = F_D·50", fontsize=9.5)
    e = axs[2]; e.set_aspect("equal"); e.axis("off"); e.set_xlim(-22, 22); e.set_ylim(-21, 21)
    e.add_patch(Circle((0, 0), RCD, fill=False, ec=GREY, ls="--"))
    e.plot([-17, 17], [0, 0], color=GREY, lw=.6, ls=":"); e.plot([0, 0], [0, 17], color=GREY, lw=.8, ls=":")
    e.text(0.6, 17.4, "A₁ (reference)", fontsize=8, color=GREY)
    for k, col, tp, ha in (("C", BLUE, (-21.5, -15.5), "left"), ("D", PURPLE, (2.5, 14.2), "left")):
        add = RCD * cplx(n[k]["add"]); rem = RCD * cplx(n[k]["remove"])
        e.plot([add.real], [add.imag], "o", mfc="white", mec=col, ms=9, alpha=.7)
        e.annotate("", (rem.real, rem.imag), (0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2))
        e.plot(rem.real, rem.imag, "x", color=col, ms=12, mew=3)
        e.text(tp[0], tp[1], "remove %.2f kg at plane %s\n%.1f° clockwise from A₁" % (n[k]["mass"], k, n[k]["cw_from_A1_remove"]), ha=ha, fontsize=8.5, color=col)
    e.set_title("answer (r = 10 cm): × = material removed,\n○ = equivalent mass it replaces", fontsize=9.5)
    fig.suptitle("Tutorial 10 Q2 · two-plane balance through planes C and D", fontsize=11)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "T10-fig4-balance.png"), dpi=150); plt.close(fig)


if __name__ == "__main__":
    n9 = t9_numbers()
    print("--- Tutorial 9 ---")
    for k in ("omega", "vmax", "amax", "s30", "s1_30", "s2_30", "v30", "a30", "rho30", "ecc30_rise_side", "ecc30_other", "rho_min", "rho_min_at", "s1max", "face_half", "ecc_max_rise", "ecc_max_return"):
        print(f"{k:18s} {n9[k]:.4f}")
    u = np.arange(7) / 6
    print("six-step rise s (mm):", np.round(cyc(u)[0], 3))
    fig_t9_motion(); fig_t9_profile(); fig_t9_graphical(); fig_t9_rho(); anim_t9()
    n10 = t10_flywheel()
    print("--- Tutorial 10 Q1 ---")
    print("energies J", {k: round(v) for k, v in n10["E"].items()})
    for k in ("Wnet", "Tmean", "Tmax", "DE_width", "dE", "dE_num", "cycle_net_num", "wmean", "Cs", "I", "I_exact", "m"):
        print(f"{k:14s} {n10[k]:.4f}")
    fig_t10_flywheel(); fig_t10_sizing()
    nb = t10_balance()
    print("--- Tutorial 10 Q2 ---")
    print("F_A", nb["FA"], abs(nb["FA"]), np.degrees(np.angle(nb["FA"])) % 360)
    print("F_B", nb["FB"], abs(nb["FB"]), np.degrees(np.angle(nb["FB"])) % 360)
    for k in ("C", "D"):
        print(k, {a: round(b, 3) for a, b in nb[k].items()})
    print("residual force, moment:", nb["resid_F"], nb["resid_M"])
    fig_t10_geometry(); fig_t10_result()
