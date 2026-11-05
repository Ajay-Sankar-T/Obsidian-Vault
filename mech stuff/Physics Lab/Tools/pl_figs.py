"""PH1030 figures. Output: ../assets/PL-*.png. Measurement 'data' here are SIMULATED from the theory with small noise, only to show what a good plot looks like."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets")); os.makedirs(ASSETS, exist_ok=True)
BLUE, ORANGE, GREEN, RED, PURPLE, GREY, TEAL = "#2b6cb0", "#dd6b20", "#2f855a", "#c53030", "#6b46c1", "#718096", "#2c7a7b"
plt.rcParams.update({"figure.dpi": 150, "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": "#e2e8f0",
                     "axes.axisbelow": True, "legend.frameon": False, "axes.prop_cycle": matplotlib.cycler(color=[BLUE, ORANGE, GREEN, RED, PURPLE, TEAL])})
rng = np.random.default_rng(7)
g = 9.81


def save(fig, name):
    fig.savefig(os.path.join(ASSETS, "PL-%s.png" % name), bbox_inches="tight", facecolor="white"); plt.close(fig); print("wrote PL-%s.png" % name)


def wl_color(nm):
    return {435.8: "#7a3fd0", 491.6: "#00a8b5", 546.1: "#22b04b", 577.0: "#d4b800", 579.1: "#c9a400"}.get(nm, "#444")


def error_types():
    fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.2, 3.5)); fig.subplots_adjust(wspace=.38)
    lo, hi = 60.1, 60.2; x = np.linspace(60.05, 60.25, 400); a.fill_between(x, 0, np.where((x >= lo) & (x <= hi), 1 / (hi - lo), 0), color=BLUE, alpha=.35)
    a.axvline((lo + hi) / 2, color=INK if False else "k", lw=1.3); a.errorbar([60.15], [4], xerr=[(hi - lo) / np.sqrt(12)], fmt="o", color=RED, capsize=4)
    a.text(60.16, 5.3, "σ = c/√12 = 0.03 cm", color=RED, fontsize=9); a.set_xlabel("length L (cm)"); a.set_ylabel("probability density"); a.set_title("Least-count error: any value\nin the interval is equally likely")
    T = 1.556 + rng.normal(0, 0.03, 10); b.plot(range(1, 11), T, "o", color=BLUE); b.axhline(T.mean(), color=ORANGE, lw=2); b.axhspan(T.mean() - T.std(ddof=1) / np.sqrt(10), T.mean() + T.std(ddof=1) / np.sqrt(10), color=ORANGE, alpha=.25)
    b.set_xlabel("repeat number"); b.set_ylabel("period estimate (s)"); b.set_title("Statistical error: scatter of repeats,\nband = standard error s/√N")
    Ns = np.arange(1, 41); c.plot(Ns, 0.03 / np.sqrt(Ns), color=BLUE, lw=2.4); c.set_xlabel("number of repeats N"); c.set_ylabel("uncertainty of the mean (s)"); c.set_title("Uncertainty of the mean falls as 1/√N\n(four times the data halves the error)")
    c.plot([4, 16], [0.03 / 2, 0.03 / 4], "o", color=RED)
    save(fig, "error-types")


def propagation():
    L, sL, T, sT = 0.6015, 0.0003, 1.556, 0.003; gg = 4 * np.pi ** 2 * L / T ** 2
    tL = 4 * np.pi ** 2 / T ** 2 * sL; tT = 8 * np.pi ** 2 * L / T ** 3 * sT; sg = np.hypot(tL, tT)
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.6))
    a.bar(["from L\n(0.03 cm)", "from T\n(0.003 s)"], [tL, tT], color=[BLUE, ORANGE]); a.set_ylabel("contribution to σ_g (m/s²)"); a.set_title("g = 4π²L/T²: g = %.3f ± %.3f m/s²\nthe period dominates (T enters squared)" % (gg, sg))
    for i, v in enumerate([tL, tT]):
        a.text(i, v * 1.02, "%.4f" % v, ha="center", fontsize=9)
    gs = np.array([9.78, 9.84, 9.80]); ss = np.array([0.08, 0.03, 0.05]); w = 1 / ss ** 2; gm = (w * gs).sum() / w.sum(); sm = 1 / np.sqrt(w.sum())
    b.errorbar(range(3), gs, yerr=ss, fmt="o", color=BLUE, capsize=4, label="three estimates"); b.axhspan(gm - sm, gm + sm, color=GREEN, alpha=.3, label="weighted mean %.3f ± %.3f" % (gm, sm)); b.axhline(gm, color=GREEN)
    b.set_xticks(range(3)); b.set_xticklabels(["run 1", "run 2", "run 3"]); b.set_ylabel("g (m/s²)"); b.legend(fontsize=8.5); b.set_title("Combine estimates with weights 1/σ²")
    save(fig, "error-propagation")
    print("propagation: g, sigma_g, rel(L), rel(T) =", round(gg, 4), round(sg, 4), round(sL / L * 100, 3), round(2 * sT / T * 100, 3), " weighted:", round(gm, 4), round(sm, 4))


def compound_pendulum():
    D = 1.0; K = D / np.sqrt(12); l = np.linspace(0.06, 0.5, 400); T = 2 * np.pi * np.sqrt((K ** 2 + l ** 2) / (g * l))
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
    a.plot(l * 100, T, color=BLUE, lw=2.6); T0 = 1.80; l1 = ((T0 ** 2 * g / (4 * np.pi ** 2)) - np.sqrt((T0 ** 2 * g / (4 * np.pi ** 2)) ** 2 - 4 * K ** 2)) / 2; Lq = T0 ** 2 * g / (4 * np.pi ** 2); l2 = Lq - l1
    a.axhline(T0, color=GREY, ls="--"); a.plot([l1 * 100, l2 * 100], [T0, T0], "o", color=RED); a.text(l1 * 100 + 1, T0 + .05, "l₁ = %.1f cm" % (l1 * 100), color=RED, fontsize=9); a.text(l2 * 100 - 12, T0 + .05, "l₂ = %.1f cm" % (l2 * 100), color=RED, fontsize=9)
    a.set_xlabel("distance l from pivot to centre of gravity (cm)"); a.set_ylabel("period T (s)"); a.set_ylim(1.4, 3.3); a.set_title("1 m rod: each T has two pivot points (l₁, l₂)\nL = l₁ + l₂,  K = √(l₁l₂)")
    ph = np.linspace(0, 80, 200); b.plot(ph, np.sqrt(1 / np.cos(np.radians(ph))), color=ORANGE, lw=2.6); b.set_xlabel("tilt of the oscillation plane Φ (degrees)"); b.set_ylabel("T(Φ) / T(0)"); b.set_title("Tilting the plane lowers the effective g:\nT ∝ 1/√cos Φ")
    save(fig, "compound-pendulum")
    print("pendulum: K =", round(K * 100, 2), "cm;  for T=1.80 s: L =", round(Lq * 100, 2), "cm, l1, l2 =", round(l1 * 100, 2), round(l2 * 100, 2), " check K=sqrt(l1 l2) =", round(np.sqrt(l1 * l2) * 100, 2), " g = 4pi^2 L/T^2 =", round(4 * np.pi ** 2 * Lq / T0 ** 2, 3))


def grating():
    N = 6.0e5  # 600 lines/mm
    lines = [(435.8, "violet 435.8 nm"), (491.6, "blue-green 491.6 nm"), (546.1, "green 546.1 nm"), (577.0, "yellow 577.0 nm"), (579.1, "yellow 579.1 nm")]
    fig, ax = plt.subplots(figsize=(9.4, 3.8))
    for m in (1, 2):
        for lam, nm in lines:
            sn = m * lam * 1e-9 * N
            if sn < 1:
                th = np.degrees(np.arcsin(sn)); ax.vlines([th, -th], 0, 1, color=wl_color(lam), lw=3, label=("%s  (1st order %.1f°)" % (nm, np.degrees(np.arcsin(lam * 1e-9 * N)))) if (m == 1 and th > 0) else None)
    ax.vlines([0], 0, 1.15, color="k", lw=3); ax.text(0, 1.2, "zero order (white)", ha="center", fontsize=9)
    ax.annotate("", xy=(20.5, 1.05), xytext=(15, 1.05), arrowprops=dict(arrowstyle="<->")); ax.text(17.8, 1.1, "m = 1", ha="center", fontsize=9)
    ax.annotate("", xy=(44, 1.05), xytext=(31, 1.05), arrowprops=dict(arrowstyle="<->")); ax.text(37.5, 1.1, "m = 2", ha="center", fontsize=9)
    ax.set_ylim(0, 1.4); ax.set_xlim(-50, 62); ax.set_yticks([]); ax.set_xlabel("diffraction angle θ (degrees)"); ax.grid(False); ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
    ax.set_title("Mercury spectrum on a 600 lines/mm grating: sin θ = mλN")
    save(fig, "grating-orders")
    print("grating: first-order angles deg:", [round(float(np.degrees(np.arcsin(lam * 1e-9 * N))), 2) for lam, _ in lines], " second order green:", round(float(np.degrees(np.arcsin(2 * 546.1e-9 * N))), 2), " max order for green:", int(1 / (546.1e-9 * N)))


def equipotential():
    a_, b_, V0 = 1.0, 5.0, 6.0
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    th = np.linspace(0, 2 * np.pi, 300)
    a.plot(a_ * np.cos(th), a_ * np.sin(th), color="k", lw=3); a.plot(b_ * np.cos(th), b_ * np.sin(th), color="k", lw=3)
    for V in (1, 2, 2.5, 3, 4, 5):
        r = a_ * (b_ / a_) ** (V / V0); a.plot(r * np.cos(th), r * np.sin(th), color=BLUE if V != 2.5 else RED, lw=2 if V != 2.5 else 3)
    for k in range(12):
        t = k * np.pi / 6; a.plot([a_ * np.cos(t), b_ * np.cos(t)], [a_ * np.sin(t), b_ * np.sin(t)], color=ORANGE, lw=1, alpha=.7)
    a.set_aspect("equal"); a.set_title("Concentric electrodes (red = 2.5 V line)"); a.axis("off")
    for y in np.linspace(0.5, 5.5, 6):
        b.plot([0, 6], [y, y], color=BLUE, lw=1.6)
    for x in np.linspace(0.5, 5.5, 6):
        b.annotate("", xy=(x, 5.9), xytext=(x, 0.1), arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1, alpha=.0))
    for xx in np.linspace(0.8, 5.2, 8):
        b.annotate("", xy=(xx, 5.6), xytext=(xx, 0.4), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2, alpha=.8))
    b.plot([0, 6], [0, 0], "k", lw=4); b.plot([0, 6], [6, 6], "k", lw=4); b.set_title("Parallel plates: uniform field"); b.set_aspect("equal"); b.axis("off")
    save(fig, "equipotential")
    print("equipotential: radius of the 2.5 V line (a=1, b=5, V0=6):", round(a_ * (b_ / a_) ** (2.5 / 6), 3), "(same units as a)")


def ultrasonic():
    f, v = 2e6, 1480.0; lam = v / f * 1e3; d = lam / 2  # mm
    x = np.linspace(0, 3.2, 1600); cur = 60 + 25 * np.cos(2 * np.pi * x / d) * np.exp(-x / 6)
    fig, ax = plt.subplots(figsize=(9, 3.6)); ax.plot(x, cur, color=BLUE, lw=2.4)
    pk = [i * d for i in range(0, int(3.2 / d) + 1)]; ax.plot(pk, [60 + 25 * np.exp(-p / 6) for p in pk], "o", color=RED, ms=6)
    for n in range(0, len(pk) - 3, 3):
        ax.annotate("", xy=(pk[n + 3], 98), xytext=(pk[n], 98), arrowprops=dict(arrowstyle="<->", color=GREEN)); ax.text((pk[n] + pk[n + 3]) / 2, 99.5, "3d = %.2f mm" % (3 * d), ha="center", fontsize=8.5, color=GREEN)
    ax.set_ylim(20, 106); ax.set_xlabel("reflector position (mm)"); ax.set_ylabel("anode current (µA)"); ax.set_title("Water, 2 MHz: maxima every d = λ/2 = %.3f mm  (λ = %.2f mm, v = fλ = %d m/s)" % (d, lam, v))
    save(fig, "ultrasonic")
    print("ultrasonic: lambda =", round(lam, 4), "mm; d =", round(d, 4), "mm; every third maximum spacing:", round(3 * d, 3), "mm; beta = 1/(rho v^2) =", "%.3e" % (1 / (998 * v ** 2)), "1/Pa")


def newton_rings():
    lam, R = 589.3e-9, 1.0
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.0), gridspec_kw={"width_ratios": [1, 1.2]})
    rr = np.linspace(0, 6e-3, 1200); xx, yy = np.meshgrid(np.linspace(-2.5e-3, 2.5e-3, 700), np.linspace(-2.5e-3, 2.5e-3, 700)); r = np.hypot(xx, yy)
    a.imshow(np.sin(np.pi * r ** 2 / (lam * R)) ** 2, cmap="YlOrBr_r", extent=[-2.5, 2.5, -2.5, 2.5]); a.set_title("Dark rings at r² = mλR (dark centre)"); a.set_xlabel("mm"); a.grid(False)
    m = np.arange(1, 13); D = 2 * np.sqrt(m * lam * R) * (1 + rng.normal(0, 0.004, m.size)); D2 = D ** 2 * 1e6  # mm^2
    b.plot(m, D2, "o", color=BLUE); sl, ic = np.polyfit(m, D2, 1); b.plot(m, sl * m + ic, color=RED, lw=2); lam_fit = sl * 1e-6 / (4 * R)
    b.set_xlabel("ring number m"); b.set_ylabel("D² (mm²)"); b.set_title("D² = 4λR m: slope %.3f mm² per ring\n→ λ = slope/4R = %.0f nm (true 589.3)" % (sl, lam_fit * 1e9))
    save(fig, "newton-rings")
    print("newton: slope mm^2/ring =", round(sl, 4), " lambda_fit nm =", round(lam_fit * 1e9, 1), " expected slope:", round(4 * lam * R * 1e6, 4), " D_1 =", round(2 * np.sqrt(lam * R) * 1e3, 3), "mm")


def transistor():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9))
    vbe = np.linspace(0, 0.8, 300)
    for vce, c in ((1, BLUE), (5, ORANGE)):
        ib = 1e-9 * (np.exp(vbe / 0.0259 / 1.5) - 1) * (1 - 0.02 * vce / 5) * 1e6; a.plot(vbe, np.minimum(ib, 200), color=c, lw=2.4, label="V_CE = %d V" % vce)
    a.set_ylim(0, 100); a.set_xlabel("V_BE (V)"); a.set_ylabel("I_B (µA)"); a.legend(fontsize=8.5); a.set_title("Input: a forward-biased diode")
    vce = np.linspace(0, 10, 300); beta = 100; VA = 80
    for ib, c in ((20, BLUE), (40, GREEN), (60, ORANGE)):
        ic = beta * ib / 1000 * (1 + vce / VA) * (1 - np.exp(-vce / 0.35)); b.plot(vce, ic, color=c, lw=2.4, label="I_B = %d µA" % ib)
    b.annotate("", xy=(7, beta * 40 / 1000 * (1 + 7 / VA)), xytext=(7, beta * 20 / 1000 * (1 + 7 / VA)), arrowprops=dict(arrowstyle="<->", color=RED)); b.text(7.15, 3.3, "ΔI_C at fixed V_CE\n→ β = ΔI_C/ΔI_B = 100", fontsize=8.5, color=RED)
    b.set_xlabel("V_CE (V)"); b.set_ylabel("I_C (mA)"); b.legend(fontsize=8.5, loc="lower right"); b.set_title("Output: flat active region")
    save(fig, "transistor")


def coil_field():
    r = 0.07; x = np.linspace(-0.2, 0.2, 400)
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
    B = r ** 3 / (r ** 2 + x ** 2) ** 1.5; a.plot(x * 100, B, color=BLUE, lw=2.6); a.set_xlabel("x along the axis (cm)"); a.set_ylabel("B / B(0)"); a.set_title("B(x) = μ₀nir² / 2(r²+x²)^{3/2}, r = 7 cm")
    a.axvline(r * 100 / 2, color=GREY, ls=":"); a.axvline(-r * 100 / 2, color=GREY, ls=":"); a.text(r * 100 / 2 + .5, 0.8, "inflection\nat x = ±r/2", fontsize=8.5, color=GREY)
    th0 = np.radians(60); Bratio = np.tan(th0)  # tan(theta) proportional to B
    th = np.degrees(np.arctan(Bratio * B)); b.plot(x * 100, th, color=ORANGE, lw=2.6); b.set_xlabel("x (cm)"); b.set_ylabel("compass deflection θ (degrees)"); b.set_title("The compass reads tan θ = B/B_E: set θ(0) ≈ 60°")
    save(fig, "coil-field")
    print("coil: B at x = r/2 relative:", round(r ** 3 / (r ** 2 + (r / 2) ** 2) ** 1.5, 4), " deflection at x=0 / x=r:", round(float(np.degrees(np.arctan(Bratio))), 1), round(float(np.degrees(np.arctan(Bratio * r ** 3 / (2 * r ** 2) ** 1.5))), 1))


def stefan():
    al, be = 4.82e-3, 6.67e-7; R0 = 0.83 / (1 + al * 27 + be * 27 ** 2)
    Rs = np.linspace(1.5, 9.0, 16); t = (-al + np.sqrt(al ** 2 - 4 * be * (1 - Rs / R0))) / (2 * be); T = t + 273
    V = 1e-14 * (T ** 4 - 300 ** 4) * (1 + rng.normal(0, 0.02, T.size)) * 1e3  # mV
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
    a.plot(Rs, T, "o-", color=BLUE); a.set_xlabel("filament resistance R (Ω)"); a.set_ylabel("temperature T (K)"); a.set_title("R(t) = R₀(1 + αt + βt²) inverted for T")
    b.loglog(T, V, "o", color=BLUE); sl, ic = np.polyfit(np.log10(T), np.log10(V), 1); xs = np.linspace(T.min(), T.max(), 20); b.loglog(xs, 10 ** ic * xs ** sl, color=RED, lw=2)
    b.set_xlabel("T (K, log)"); b.set_ylabel("thermopile V_TC (mV, log)"); b.set_title("log V_TC vs log T: slope %.2f (Stefan: 4)" % sl)
    save(fig, "stefan")
    print("stefan: R0 =", round(R0, 4), " T range K:", round(T.min()), round(T.max()), " fitted slope:", round(sl, 3), " check R=5 ohm -> T =", round(273 + (-al + np.sqrt(al ** 2 - 4 * be * (1 - 5 / R0))) / (2 * be)), "K")


def young_wood():
    M = np.array([0, 1, 2, 3, 4, 5]) * 100.0  # g
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8), gridspec_kw={"width_ratios": [1.3, 1]})
    k = 0.0079; up = k * M / 1000 * 1000 + rng.normal(0, .05, 6); dn = k * M + rng.normal(0, .05, 6) + 0.05
    a.plot(M, up, "o", color=BLUE, label="loading"); a.plot(M, dn, "s", color=ORANGE, label="unloading"); sl = np.polyfit(np.r_[M, M], np.r_[up, dn], 1)[0]; a.plot(M, sl * M, color=RED, lw=2, label="fit through the origin: %.4f mV/g" % sl)
    a.set_xlabel("load M (g)"); a.set_ylabel("unbalanced voltage dV (mV)"); a.legend(fontsize=8.5); a.set_title("Bridge output is linear in load\n(loading and unloading agree to the noise)")
    b.bar(["quarter bridge\n(1 active gauge)", "half bridge\n(tension + compression)"], [1, 2], color=[BLUE, GREEN]); b.set_ylabel("relative output"); b.set_title("Two gauges on opposite faces\ndouble the signal and cancel temperature")
    save(fig, "young-wood")
    print("wood: slope mV/g (simulated) =", round(sl, 5))


if __name__ == "__main__":
    INK = "k"
    error_types(); propagation(); compound_pendulum(); grating(); equipotential(); ultrasonic(); newton_rings(); transistor(); coil_field(); stefan(); young_wood()
