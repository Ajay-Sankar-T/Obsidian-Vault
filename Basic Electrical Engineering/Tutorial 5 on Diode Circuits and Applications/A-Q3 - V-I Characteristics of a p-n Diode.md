---
tags: [EE1100, diodes, tutorial-solution]
---

# A-Q3 — V-I Characteristics of a p-n Junction Diode

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q2 - Poisson Equation, Field and Potential]] · Next: [[A-Q4 - Bias, Cut-in Voltage, Saturation Current and Resistance]]

> [!question] Explain the V-I characteristics of a p-n junction diode. Write the equation and draw the graph relating voltage and current.

## 1. Theory

An external voltage $v_D$ (anode positive) changes the barrier height from $V_0$ to $V_0-v_D$.

### Forward bias ($v_D>0$)
The barrier and the depletion width shrink, so many majority carriers diffuse across the junction and become minority carriers on the other side (**minority-carrier injection**). The diffusion current rises **exponentially** with $v_D$, while the drift current is almost unchanged.

### Reverse bias ($v_D<0$)
The barrier grows and the depletion region widens, so majority carriers cannot cross. Only the thermally generated minority carriers drift across: a tiny, nearly constant **reverse saturation current** $I_s$ (pA–nA for Si).

### Reverse breakdown
For $|v_D|>V_{BR}$ the current rises sharply: **Zener** effect (tunnelling, $V_{BR}\lesssim5$ V, heavily doped) or **avalanche** (impact ionisation, $V_{BR}\gtrsim7$ V). It is non-destructive if the power is limited.

## 2. The equation (Shockley)

$$\boxed{i_D=I_s\Big(e^{\,v_D/(\eta V_T)}-1\Big)},\qquad V_T=\frac{kT}{q}=\frac{T}{11600}\approx25.9\ \text{mV}\ (300\ \text{K}),\quad\eta=1\ldots2$$

| Region | Approximation |
|---|---|
| $v_D\gg V_T$ | $i_D\approx I_se^{v_D/\eta V_T}$ |
| $v_D=0$ | $i_D=0$ |
| $v_D\le-3V_T$ | $i_D\approx-I_s$ |

## 3. Graph

![[A3-iv-characteristics.png]]

- **Left:** linear axes for Si ($I_s=1$ pA) and Ge ($I_s=1$ µA): Ge turns on at a smaller voltage (≈ 0.2–0.3 V) than Si (≈ 0.6–0.7 V).
- **Middle:** the reverse region with breakdown at $-V_{BR}$.
- **Right:** semi-log plot of the forward current: a straight line, one decade per $2.3\eta V_T\approx60$ mV.

## 4. Temperature behaviour (extra)
$I_s$ roughly doubles for every 10 °C; for a fixed current $v_D$ falls by about $2$ mV/°C.
