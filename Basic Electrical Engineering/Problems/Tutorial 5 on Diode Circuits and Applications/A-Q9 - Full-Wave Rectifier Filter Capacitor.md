---
tags: [EE1100, diodes, tutorial-solution, rectifier, filter]
---

# A-Q9 — Filter Capacitor for a Full-Wave Rectifier (5 % ripple)

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q8 - Half-Wave Rectifier Filter Capacitor]] · Next: [[B-Q1 - Two-Diode Circuit with 0.7 V Drop]]

> [!question] A full-wave rectifier has 5 % ripple in the output relative to the peak input voltage $v_s=V_m\sin314t$. Design the capacitor filter for $R_2=1\ \text{k}\Omega$.

## 1. Theory

In a full-wave rectifier the capacitor is recharged **twice** per source cycle, so the discharge time is $T/2=1/2f$:

$$V_r=\frac{I_{dc}}{2fC}=\frac{V_m}{2fR_2C}\quad\Longrightarrow\quad C=\frac{V_m}{2fR_2V_r}$$

($V_r$ is again the peak-to-peak ripple.) Compared with the half-wave case ([[A-Q8 - Half-Wave Rectifier Filter Capacitor]]) the same ripple needs **half** the capacitance.

## 2. Solution

$f=50$ Hz, $V_r=0.05V_m$, $R_2=1$ kΩ:

$$C=\frac1{2\times50\times1000\times0.05}=2\times10^{-4}\ \text{F}\quad\Longrightarrow\quad\boxed{C\approx200\ \mu\text{F}}$$

## 3. Check with the exact waveform

The exact steady-state discharge needs $C=174.6\ \mu$F for $V_{pp}=0.05V_m$, so 200 µF (the standard value above it is chosen) gives a ripple slightly below 5 % (about 4.4 % of $V_m$).

![[A8-A9-capacitor-design.png]]

| | formula | exact |
|---|---|---|
| $C$ for 5 % ripple | 200 µF | 174.6 µF |
| output $V_{dc}\approx V_m-V_r/2$ | $0.975V_m$ | $0.9785V_m$ (with 200 µF) |
| RF $=\dfrac{V_r}{2\sqrt3V_{dc}}$ | 0.0148 | 0.0133 (200 µF) |

## 4. Design checks
- Voltage rating of $C$: $\ge V_m$ (add margin).
- Bridge diode PIV: $V_m$ (centre-tap: $2V_m$).
- Ripple frequency $=2f=100$ Hz.
- Peak diode current is much larger than $I_{dc}$ because conduction occurs only near the peaks (see [[A-Q6 - Rectifier Circuits and Waveforms]]).

> [!tip] If "5 % ripple" meant the rms ripple factor
> $C=\dfrac1{4\sqrt3fR_2\,RF}=\dfrac1{4\sqrt3(50)(1000)(0.05)}=57.7\ \mu$F. Using the peak-to-peak reading (as in A-Q8) gives 200 µF.

See also the design curves in [[A-Q8 - Half-Wave Rectifier Filter Capacitor]].
