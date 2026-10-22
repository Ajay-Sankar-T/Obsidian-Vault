---
tags: [EE1100, diodes, tutorial-solution, rectifier]
---

# B-Q8 — Half-Wave Rectifier with a Series Resistor

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q7 - Asymmetric Diode Resistor Network]] · Next: [[B-Q9 - Battery Charging Rectifier Circuit]]

> [!question] Fig. 8: source $10\sin(100t)$, $R_1=10$ kΩ in series with ideal diode $D_1$, and $R_2=10$ kΩ across the output. Draw the output waveform.

![[B8-circuit-waveform.png]]

## 1. Theory

An ideal diode is a short circuit when forward biased and an open circuit when reverse biased. With the diode ON, $R_1$ and $R_2$ form a **voltage divider**:
$$V_0=v_s\,\frac{R_2}{R_1+R_2}.$$

## 2. Solution

- **Positive half-cycle** ($v_s>0$): $D_1$ ON.
$$V_0=10\sin(100t)\times\frac{10\text{ k}}{10\text{ k}+10\text{ k}}=\boxed{5\sin(100t)\ \text{V}}$$
- **Negative half-cycle** ($v_s<0$): $D_1$ OFF, no current, $V_0=\boxed{0}$.

The output is a half-wave rectified sine of peak 5 V. Angular frequency 100 rad/s ($f=15.9$ Hz, $T=62.8$ ms): the positive half lasts $\pi/100=31.4$ ms.

| | value |
|---|---|
| peak of $V_0$ | 5 V |
| $V_{dc}=5/\pi$ | 1.59 V |
| $V_{rms}=5/2$ | 2.5 V |
| peak current $=10/(20\text{ k})$ | 0.5 mA |
| diode PIV | 10 V |

Numerical check: the simulated output equals $\max(5\sin 100t,0)$ to $2.5\times10^{-7}$ V.
