---
tags: [EE1100, diodes, tutorial-solution, rectifier]
---

# A-Q6 — Rectifier Circuits and Waveforms

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q5 - Applications of Diodes]] · Next: [[A-Q7 - Ripple, Ripple Factor and Form Factor]]

> [!question] Draw the circuits for (i) a half-wave rectifier without and with a capacitor filter, (ii) a full-wave rectifier without and with a capacitor filter. Draw typical output voltage and current waveforms and also the input voltage and current waveforms. Resistive load, ideal diodes.

## 1. Theory

A rectifier converts the alternating source $v_s=V_m\sin\omega t$ into a unidirectional output.
- **Half-wave:** one diode conducts only while $v_s>0$ (the positive half-cycle).
- **Full-wave:** both half-cycles are used, either with a **bridge** of four diodes (two conduct at a time: $D_1,D_4$ when $v_s>0$ and $D_2,D_3$ when $v_s<0$) or with a **centre-tapped transformer** and two diodes.
- **Filter capacitor:** across the load, the capacitor charges to $V_m$ while the diode conducts near each peak, and then discharges through $R_L$ (time constant $R_LC$) while all diodes are off; the output is nearly constant with a small **ripple**.

Ideal diodes (no 0.7 V drop) and resistive load $R_L$ are assumed.

## 2. Circuits

![[A6-rectifier-circuits.png]]

*Centre-tap alternative:* a transformer with a centre-tapped secondary and two diodes whose anodes are at the two ends and whose cathodes are joined to the load; the load return is the centre tap.

## 3. Waveforms ($V_m=10$ V, $R_L=1$ kΩ, $f=50$ Hz; filter $C=100\ \mu$F)

![[A6-rectifier-waveforms.png]]

| Waveform | HW, no filter | HW + C | FW, no filter | FW + C |
|---|---|---|---|---|
| Input voltage $v_s$ | sinusoid | same | same | same |
| Input current $i_s$ | half-sine pulses of one polarity only (it has a **dc component**) | **narrow** tall pulses near each positive peak (≈ 180 mA peak here) | sinusoid of the same shape as $v_s$ (no dc) | narrow pulses of **alternating** sign near each peak (≈ ±135 mA here) |
| Output voltage $v_o$ | $V_m\sin\omega t$ for $0<\omega t<\pi$, zero for $\pi<\omega t<2\pi$ | stays near $V_m$, charging for a short time, then decays exponentially | $\lvert V_m\sin\omega t\rvert$ | $\lvert\sin\rvert$ peaks with shallow decay between them |
| Output current $i_o=v_o/R_L$ | same shape as $v_o$ | same shape as $v_o$ (nearly constant) | same shape as $v_o$ | same shape as $v_o$ |
| Output frequency (ripple) | $f=50$ Hz | $f$ | $2f=100$ Hz | $2f$ |
| Diode PIV | $V_m$ | $2V_m$ | $V_m$ (bridge) | $V_m$ (bridge) |

> [!note] Why the filtered input current is a narrow pulse
> The capacitor only takes charge when $v_s$ exceeds the capacitor voltage, i.e. during a short **conduction angle** $\theta_c\approx\sqrt{2V_r/V_m}$ (small for small ripple). The same charge per cycle ($=I_{dc}T$ for HW) must therefore flow in a short time, so the diode/transformer peak current is many times $I_{dc}$. This is why the diode and transformer ratings must be chosen for the **peak repetitive current**, not for the dc load current.

The numerical details of the ripple are in [[A-Q7 - Ripple, Ripple Factor and Form Factor]].
