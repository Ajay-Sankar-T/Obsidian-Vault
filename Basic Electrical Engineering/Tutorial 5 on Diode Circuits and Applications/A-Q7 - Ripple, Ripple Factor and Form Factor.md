---
tags: [EE1100, diodes, tutorial-solution, rectifier]
---

# A-Q7 — Ripple, Ripple Factor and Form Factor

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q6 - Rectifier Circuits and Waveforms]] · Next: [[A-Q8 - Half-Wave Rectifier Filter Capacitor]]

> [!question] Define the ripple, ripple factor (RF) and form factor (FF) of a rectifier output. Calculate and compare their values for half-wave and full-wave rectifiers without and with a capacitor filter. Input $v_s=V_m\sin314t$.

## 1. Definitions

For the output $v_o(t)$ with period $T_o$:

$$V_{dc}=\frac1{T_o}\int v_o\,dt,\qquad V_{rms}=\sqrt{\frac1{T_o}\int v_o^2\,dt}$$

- **Ripple:** the ac component left in the dc output, $v_r(t)=v_o(t)-V_{dc}$. Its peak-to-peak value is $V_r$ and its rms value is
$$V_{ac}=\sqrt{V_{rms}^2-V_{dc}^2}.$$
- **Form factor:** $FF=\dfrac{V_{rms}}{V_{dc}}$ (shape of the waveform; $FF=1$ for pure dc).
- **Ripple factor:** $RF=\dfrac{V_{ac}}{V_{dc}}=\sqrt{FF^2-1}$ (smaller is better; $RF=0$ for pure dc).

Frequency: $\omega=314$ rad/s so $f=50$ Hz.

## 2. Without filter

**Half-wave** ($v_o=V_m\sin\omega t$ for $0<\omega t<\pi$, else 0):
$$V_{dc}=\frac1{2\pi}\int_0^\pi V_m\sin\theta\,d\theta=\frac{V_m}\pi,\qquad V_{rms}^2=\frac1{2\pi}\int_0^\pi V_m^2\sin^2\theta\,d\theta=\frac{V_m^2}4\Rightarrow V_{rms}=\frac{V_m}2$$
$$FF=\frac{V_m/2}{V_m/\pi}=\frac\pi2=1.571,\qquad RF=\sqrt{\frac{\pi^2}4-1}=1.211$$

**Full-wave** ($v_o=|V_m\sin\omega t|$):
$$V_{dc}=\frac{2V_m}\pi,\qquad V_{rms}=\frac{V_m}{\sqrt2}$$
$$FF=\frac\pi{2\sqrt2}=1.111,\qquad RF=\sqrt{\frac{\pi^2}8-1}=0.483$$

## 3. With a capacitor filter (triangular-ripple approximation)

The capacitor discharges roughly linearly through $R_L$ for (almost) one output period $T_o$ ($=1/f$ for half-wave, $1/2f$ for full-wave), losing
$$V_r=\frac{I_{dc}T_o}{C}\approx\frac{V_m}{fR_LC}\ (\text{HW}),\qquad V_r\approx\frac{V_m}{2fR_LC}\ (\text{FW}).$$
The output is then a sawtooth of peak-to-peak $V_r$ about $V_{dc}\approx V_m-V_r/2$, whose rms value is $V_r/(2\sqrt3)$:

$$V_{ac}\approx\frac{V_r}{2\sqrt3},\qquad RF=\frac{V_{ac}}{V_{dc}}\approx\frac{V_r}{2\sqrt3\,(V_m-V_r/2)}\ \xrightarrow{V_r\ll V_m}\ \begin{cases}\dfrac1{2\sqrt3\,fR_LC}&\text{(HW)}\\[2mm]\dfrac1{4\sqrt3\,fR_LC}&\text{(FW)}\end{cases}$$
$$FF=\sqrt{1+RF^2}\ \approx 1.$$

## 4. Comparison (numerical, $V_m=10$ V, $R_L=1$ kΩ, $f=50$ Hz)

The "exact" columns come from a time-stepped simulation of the ideal rectifier driving the $R_L\|C$ load (discharge exponential, conduction only when $v_s$ exceeds the capacitor voltage).

| Quantity | HW, no filter | FW, no filter | HW, $C=100\,\mu$F | FW, $C=100\,\mu$F | HW, $C=200\,\mu$F | FW, $C=200\,\mu$F |
|---|---|---|---|---|---|---|
| $V_{dc}$ (V) | 3.183 | 6.366 | 9.177 | 9.601 | 9.560 | 9.785 |
| $V_{rms}$ (V) | 5.000 | 7.071 | 9.190 | 9.604 | 9.563 | 9.786 |
| Ripple pp $V_r$ (V) | 10 | 10 | 1.655 | 0.828 | 0.889 | 0.441 |
| $V_{ac}$ rms (V) | 3.856 | 3.078 | 0.488 | 0.246 | 0.260 | 0.130 |
| **RF** | **1.211** | **0.483** | 0.0532 | 0.0256 | 0.0272 | 0.0133 |
| **FF** | **1.571** | **1.111** | 1.0014 | 1.0003 | 1.0004 | 1.0001 |
| formula RF $\approx\frac1{2\sqrt3fRC}$ / $\frac1{4\sqrt3fRC}$ | | | 0.0577 | 0.0289 | 0.0289 | 0.0144 |

![[A7-rf-ff.png]]

> [!success] Conclusions
> - Without a filter, full-wave has lower RF (0.483 vs 1.211) and higher $V_{dc}$ (twice).
> - A capacitor reduces RF by one to two orders of magnitude; FF → 1.
> - For the same $C$, full-wave ripple is **half** that of half-wave (the capacitor discharges for half as long), so RF is also halved.
> - The linear-discharge formulas are slightly pessimistic (they assume discharge for the whole period, but the capacitor recharges earlier).
