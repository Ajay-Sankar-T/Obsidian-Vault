"""Measurements, Instrumentation and Control (ME2400): numbers and figures for the concept notes.
   python mic_core.py -> prints every quoted number, writes ../assets/MIC-*.png"""
import os
from math import pi, sqrt, exp, log, atan, degrees, radians
import numpy as np
from scipy import signal
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets")
os.makedirs(OUT, exist_ok=True)
BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#2b6cb0", "#c0392b", "#2f855a", "#718096", "#dd6b20", "#6b46c1"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": .25})


def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), dpi=150); plt.close(fig)


# ------------------------------------------------------------ uncertainty and bridges
def uncertainty():
    # P = V^2 / R,  V = 12.00 +- 0.05 V,  R = 47.0 +- 0.5 ohm
    V, dV, R, dR = 12.0, 0.05, 47.0, 0.5
    P = V ** 2 / R
    dP = P * sqrt((2 * dV / V) ** 2 + (dR / R) ** 2)
    dP_worst = P * (2 * dV / V + dR / R)
    return dict(P=P, dP_rss=dP, dP_worst=dP_worst, rel=dP / P)


def bridges():
    GF, eps, Vs = 2.0, 1000e-6, 5.0
    q = Vs * GF * eps / 4
    return dict(quarter=q, half=2 * q, full=4 * q, dRR=GF * eps, gain_for_1V=1.0 / q, K_type_mV_per_100K=4.1)


def rtd():
    R0, a = 100.0, 0.00385
    return dict(R100=R0 * (1 + a * 100), per_degree=R0 * a)


def fig_bridge():
    eps = np.linspace(0, 2000e-6, 100)
    Vs, GF = 5.0, 2.0
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    a.plot(eps * 1e6, Vs * GF * eps / 4 * 1e3, color=BLUE, lw=2.2, label="quarter bridge")
    a.plot(eps * 1e6, Vs * GF * eps / 2 * 1e3, color=GREEN, lw=2.2, label="half bridge (2 active gauges)")
    a.plot(eps * 1e6, Vs * GF * eps * 1e3, color=ORANGE, lw=2.2, label="full bridge (4 active gauges)")
    a.plot([1000], [Vs * GF * 1000e-6 / 4 * 1e3], "o", color=RED); a.annotate("1000 µε: 2.5 mV", (1000, 2.5), (1150, 1.0), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    a.set_xlabel("strain (µε)"); a.set_ylabel("bridge output (mV), V_s = 5 V, GF = 2"); a.legend(fontsize=9); a.set_title("more active arms, more signal (and temperature compensation)", fontsize=9.5)
    t = np.linspace(0, 1, 2000)
    f_sig = 7.0
    fs = 10.0
    b.plot(t, np.sin(2 * pi * f_sig * t), color=GREY, lw=1.2, label="7 Hz signal")
    ts = np.arange(0, 1, 1 / fs)
    b.plot(ts, np.sin(2 * pi * f_sig * ts), "o", color=RED, label="sampled at 10 Hz")
    b.plot(t, np.sin(2 * pi * (f_sig - fs) * t), color=RED, lw=1.5, ls="--", label="what the samples look like: 3 Hz")
    b.set_xlabel("time (s)"); b.set_ylabel("amplitude"); b.legend(fontsize=8.5, loc="lower left"); b.set_title("aliasing: sampling below 2× the signal frequency", fontsize=9.5)
    fig.suptitle("Signal conditioning", fontsize=11)
    save(fig, "MIC-1-bridge.png")


# ------------------------------------------------------------ first order
def first_order():
    tau = 2.0
    r = dict(tau=tau, t63=tau, t95=3 * tau, t99=log(100) * tau)
    rate = 10.0
    r["ramp_lag"] = rate * tau
    f = 0.1
    w = 2 * pi * f
    r["amp"] = 1 / sqrt(1 + (w * tau) ** 2)
    r["phase_deg"] = -degrees(atan(w * tau))
    r["f_bw"] = 1 / (2 * pi * tau)
    # thermocouple bead tau = rho c d / (6 h) for a sphere
    rho, c, d, h = 8500.0, 400.0, 1e-3, 100.0
    r["tau_bead"] = rho * c * d / (6 * h)
    return r


def fig_first(r):
    tau = r["tau"]
    fig, (a, b, c) = plt.subplots(1, 3, figsize=(13, 4.2))
    t = np.linspace(0, 6 * tau, 300)
    a.plot(t / tau, 1 - np.exp(-t / tau), color=BLUE, lw=2.4)
    for k, col in ((1, RED), (3, GREEN)):
        a.plot([k], [1 - exp(-k)], "o", color=col); a.text(k + .1, 1 - exp(-k) - .08, "%.1f %%" % (100 * (1 - exp(-k))), color=col, fontsize=9)
    a.set_xlabel("t / τ"); a.set_ylabel("output / final value"); a.set_title("step response: 63 % at τ, 95 % at 3τ", fontsize=9.5)
    t = np.linspace(0, 6, 300)
    rate = 10.0
    out = rate * (t - tau * (1 - np.exp(-t / tau)))
    b.plot(t, rate * t, color=GREY, ls="--", label="input ramp (10 K/s)"); b.plot(t, out, color=BLUE, lw=2.4, label="sensor reading")
    b.annotate("", (5, rate * 5), (5, out[np.argmin(abs(t - 5))]), arrowprops=dict(arrowstyle="<->", color=RED)); b.text(5.1, rate * 5 - 10, "steady lag\nτ·rate = %.0f K" % r["ramp_lag"], color=RED, fontsize=9)
    b.set_xlabel("time (s)"); b.set_ylabel("temperature (K)"); b.legend(fontsize=9); b.set_title("ramp: a constant delay of τ", fontsize=9.5)
    w = np.logspace(-2, 2, 200) / tau
    c.semilogx(w * tau, 20 * np.log10(1 / np.sqrt(1 + (w * tau) ** 2)), color=BLUE, lw=2.4)
    c.axvline(1, color=GREY, ls=":"); c.text(1.1, -2, "corner ω = 1/τ: −3 dB", fontsize=9)
    c.set_xlabel("ω τ"); c.set_ylabel("magnitude (dB)"); c.set_title("frequency response: a low-pass filter", fontsize=9.5)
    fig.suptitle("First-order instrument (thermocouple, RC, lumped body)", fontsize=11)
    save(fig, "MIC-2-first-order.png")


# ------------------------------------------------------------ second order
def second_order():
    wn, z = 100.0, 0.2
    wd = wn * sqrt(1 - z ** 2)
    Mp = exp(-pi * z / sqrt(1 - z ** 2))
    r = dict(wn=wn, zeta=z, wd=wd, Mp=Mp, tp=pi / wd, ts2=4 / (z * wn), Mr=1 / (2 * z * sqrt(1 - z ** 2)), wr=wn * sqrt(1 - 2 * z ** 2))
    r["Mp_07"] = exp(-pi * 0.7 / sqrt(1 - 0.49))
    r["ts_07"] = 4 / (0.7 * wn)
    r["Mp_table"] = {zz: exp(-pi * zz / sqrt(1 - zz ** 2)) for zz in (0.1, 0.2, 0.4, 0.7)}
    return r


def fig_second(r):
    wn = r["wn"]
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    t = np.linspace(0, 0.3, 600)
    for z, col in ((0.1, RED), (0.2, ORANGE), (0.4, GREEN), (0.7, BLUE), (1.0, PURPLE), (2.0, GREY)):
        sys = signal.TransferFunction([wn ** 2], [1, 2 * z * wn, wn ** 2])
        tt, y = signal.step(sys, T=t)
        a.plot(tt, y, color=col, lw=2, label="ζ = %.1f" % z)
    a.axhline(1.05, color=GREY, ls=":"); a.axhline(0.95, color=GREY, ls=":")
    a.set_xlabel("time (s), ω_n = 100 rad/s"); a.set_ylabel("step response"); a.legend(fontsize=8.5, ncol=2); a.set_title("damping sets overshoot; ζ ≈ 0.7 settles fastest", fontsize=9.5)
    w = np.logspace(-1, 1, 400)
    for z, col in ((0.1, RED), (0.2, ORANGE), (0.4, GREEN), (0.7, BLUE), (1.0, PURPLE)):
        mag = 1 / np.sqrt((1 - w ** 2) ** 2 + (2 * z * w) ** 2)
        b.semilogx(w, 20 * np.log10(mag), color=col, lw=2, label="ζ = %.1f" % z)
    b.axhline(0, color="k", lw=.7); b.set_ylim(-30, 20); b.set_xlabel("ω / ω_n"); b.set_ylabel("magnitude (dB)"); b.legend(fontsize=8.5); b.set_title("resonant peak 1/(2ζ√(1−ζ²)); flat to ω_n only near ζ = 0.7", fontsize=9.5)
    fig.suptitle("Second-order instrument (accelerometer, manometer, mass-spring)", fontsize=11)
    save(fig, "MIC-3-second-order.png")


# ------------------------------------------------------------ feedback
def feedback():
    r = {}
    for K in (0.5, 1.0, 5.0):
        r[K] = dict(ess=1 / (1 + 5 * K), tau_cl=1 / (2 + 10 * K), final=10 * K / (2 + 10 * K))
    r["tau_ol"] = 0.5
    r["final_ol"] = 5.0
    return r


def fig_feedback(r):
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
    t = np.linspace(0, 3, 400)
    tt, y = signal.step(signal.TransferFunction([10], [1, 2]), T=t); a.plot(tt, y / 5, color=GREY, ls="--", lw=2, label="open loop (final value 5, shown ÷5)")
    for K, col in ((0.5, GREEN), (1.0, BLUE), (5.0, ORANGE)):
        tt, y = signal.step(signal.TransferFunction([10 * K], [1, 2 + 10 * K]), T=t); a.plot(tt, y, color=col, lw=2.2, label="K = %g: final %.3f, error %.1f %%" % (K, r[K]["final"], 100 * r[K]["ess"]))
    a.axhline(1, color="k", lw=.7); a.set_xlabel("time (s)"); a.set_ylabel("output for a unit step reference"); a.legend(fontsize=8.5, loc="lower right"); a.set_title("P control of G = 10/(s+2): faster and more accurate with K", fontsize=9.5)
    K = np.linspace(0, 20, 200)
    b.plot(K, 100 / (1 + 5 * K), color=BLUE, lw=2.4, label="steady-state error (%)")
    b2 = b.twinx(); b2.plot(K, 1 / (2 + 10 * K), color=ORANGE, lw=2.2, label="closed-loop time constant (s)"); b2.set_ylabel("closed-loop time constant (s)", color=ORANGE); b2.grid(False)
    b.set_xlabel("proportional gain K"); b.set_ylabel("steady-state error to a step (%)", color=BLUE); b.set_title("e_ss = 1/(1 + K·G(0)) never reaches zero with P alone", fontsize=9.5)
    fig.suptitle("Feedback", fontsize=11)
    save(fig, "MIC-4-feedback.png")


# ------------------------------------------------------------ PID
def pid_sim(Kp, Ti=None, Td=None, T=25.0, dt=0.002):
    """plant 1/(s+1)^3 (three cascaded lags), unit step reference; PID with a filtered derivative (filter factor N = 20)."""
    n = int(T / dt)
    x = np.zeros(3); y = np.zeros(n)
    integ = 0.0; z = 1.0 if False else 0.0
    N = 20.0
    for k in range(n):
        e = 1.0 - x[2]
        integ += e * dt
        if Td:
            z += dt * (N / Td) * (e - z)
            d = N * (e - z)
        else:
            d = 0.0
        u = Kp * (e + (integ / Ti if Ti else 0.0) + d)
        x[0] += dt * (u - x[0]); x[1] += dt * (x[0] - x[1]); x[2] += dt * (x[1] - x[2])
        y[k] = x[2]
    return np.arange(n) * dt, y


def pid():
    Ku, Pu = 8.0, 2 * pi / sqrt(3)
    zn = dict(P=(0.5 * Ku, None, None), PI=(0.45 * Ku, Pu / 1.2, None), PID=(0.6 * Ku, Pu / 2, Pu / 8))
    out = dict(Ku=Ku, Pu=Pu, gains={k: v for k, v in zn.items()})
    res = {}
    for name, (Kp, Ti, Td) in zn.items():
        t, y = pid_sim(Kp, Ti, Td)
        os_ = max(y.max() - 1, 0)
        idx = np.where(np.abs(y - 1) > 0.02)[0]
        ts = t[idx[-1]] if len(idx) else 0.0
        res[name] = dict(Kp=Kp, Ti=Ti, Td=Td, overshoot=os_, final=y[-1], ts2=ts, ess=1 - y[-1], t=t, y=y)
    out["res"] = res
    return out


def fig_pid(p):
    fig, ax = plt.subplots(figsize=(8, 4.6))
    cols = {"P": GREEN, "PI": BLUE, "PID": RED}
    for name, r in p["res"].items():
        ax.plot(r["t"], r["y"], color=cols[name], lw=2.2, label="%s: Kp=%.1f%s%s, overshoot %.0f %%, e_ss %.2f" % (name, r["Kp"], (", Ti=%.2f" % r["Ti"]) if r["Ti"] else "", (", Td=%.2f" % r["Td"]) if r["Td"] else "", 100 * r["overshoot"], r["ess"]))
    ax.axhline(1, color="k", lw=.7); ax.set_xlim(0, 25); ax.set_ylim(0, 2); ax.set_xlabel("time (s)"); ax.set_ylabel("output, unit step"); ax.legend(fontsize=8.5)
    ax.set_title("Ziegler–Nichols tuned loops on G = 1/(s+1)³ (K_u = 8, P_u = 3.63 s)", fontsize=10)
    save(fig, "MIC-5-pid.png")


# ------------------------------------------------------------ frequency response
def margins(K):
    L = lambda w: K / (1j * w * (1j * w + 1) * (1j * w + 2))
    wpc = sqrt(2.0)
    GM = 1 / abs(L(wpc))
    wgc = brentq(lambda w: abs(L(w)) - 1, 0.05, 5)
    PM = 180 + degrees(np.angle(L(wgc)))
    return dict(K=K, wpc=wpc, GM=GM, GM_dB=20 * np.log10(GM), wgc=wgc, PM=PM)


def fig_nyquist():
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.6))
    w = np.logspace(-2, 2, 2000)
    for K, col in ((2.0, BLUE), (6.0, RED), (10.0, ORANGE)):
        L = K / (1j * w * (1j * w + 1) * (1j * w + 2))
        a.plot(L.real, L.imag, color=col, lw=2, label="K = %g" % K)
        a.plot(L.real, -L.imag, color=col, lw=1, ls=":")
    a.plot([-1], [0], "kx", ms=10, mew=2); a.text(-1.0, -0.35, "−1", ha="center")
    a.set_xlim(-3.5, 1); a.set_ylim(-2.5, 2.5); a.set_xlabel("Re L(jω)"); a.set_ylabel("Im L(jω)"); a.legend(fontsize=9); a.set_title("Nyquist plot of L = K/[s(s+1)(s+2)]: K = 6 passes through −1", fontsize=9.5)
    m = margins(2.0)
    mag = 20 * np.log10(np.abs(2.0 / (1j * w * (1j * w + 1) * (1j * w + 2))))
    b.semilogx(w, mag, color=BLUE, lw=2.4); b.axhline(0, color="k", lw=.7)
    b.axvline(m["wgc"], color=GREEN, ls="--"); b.axvline(m["wpc"], color=RED, ls="--")
    b.plot([m["wpc"]], [-m["GM_dB"]], "o", color=RED); b.annotate("gain margin %.1f dB\n(K can rise ×%.1f)" % (m["GM_dB"], m["GM"]), (m["wpc"], -m["GM_dB"]), (2.5, -20), arrowprops=dict(arrowstyle="->", color=GREY), fontsize=9)
    b.text(m["wgc"] * 1.05, 18, "ω_gc = %.2f\nPM = %.0f°" % (m["wgc"], m["PM"]), color=GREEN, fontsize=9)
    b.set_xlim(0.05, 20); b.set_ylim(-60, 40); b.set_xlabel("ω (rad/s)"); b.set_ylabel("|L| (dB), K = 2"); b.set_title("margins read from the Bode magnitude", fontsize=9.5)
    fig.suptitle("Stability from the frequency response", fontsize=11)
    save(fig, "MIC-6-nyquist.png")


if __name__ == "__main__":
    print("uncertainty", uncertainty()); print("bridges", bridges()); print("rtd", rtd())
    f = first_order(); print("first", f)
    s = second_order(); print("second", s)
    fb = feedback(); print("feedback", fb)
    p = pid(); print("pid", {k: ({a: (round(b, 3) if isinstance(b, (int, float)) else b) for a, b in v.items() if a not in ("t", "y")} if isinstance(v, dict) else v) for k, v in p["res"].items()}, p["Ku"], p["Pu"])
    for K in (2.0, 3.0, 6.0):
        print("margins", margins(K))
    fig_bridge(); fig_first(f); fig_second(s); fig_feedback(fb); fig_pid(p); fig_nyquist()
