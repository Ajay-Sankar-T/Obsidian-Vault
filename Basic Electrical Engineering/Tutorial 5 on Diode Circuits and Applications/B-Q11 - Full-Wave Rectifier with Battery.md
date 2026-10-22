---
tags: [EE1100, diodes, tutorial-solution, rectifier]
---

# B-Q11 — Full-Wave Rectifier Charging a 50 V Battery

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q10 - Two-Level Clipper]] · Next: [[B-Q12 - Voltage Doubler]]

> [!question] Fig. 10: each diode has a resistance of 10 Ω; $e_1=100\sin\omega t$ and $e_2=-e_1$ with respect to ground (centre tap). The load is $R_L=1$ kΩ in series with a 50 V battery. (a) Sketch the battery current vs time. (b) Find its average value.

![[B11-circuit-current.png]]

## 1. Theory

A centre-tapped full-wave rectifier: $D_1$ conducts when $e_1$ is positive and large enough, $D_2$ when $e_2=-e_1$ is. The two diodes feed the common node, so the load current always flows in the same direction. The battery (50 V, opposing the current) delays conduction until the instantaneous source voltage exceeds 50 V:

$$i(t)=\frac{|e_1(t)|-E}{R_{tot}}\quad\text{when }|e_1|>E,\qquad 0\ \text{otherwise}.$$

**Series resistance of the conducting path:** the 10 Ω resistor shown in each branch plus the 10 Ω diode resistance, plus $R_L$:
$$R_{tot}=10+10+1000=1020\ \Omega.$$

> [!note] Interpretation
> The figure draws a 10 Ω resistor in each diode branch and the text says each diode has a 10 Ω resistance, so I include both. This is the only reading that reproduces the sheet's answer $0.0214$ A (with 1010 Ω the average would be 0.0216 A).

## 2. Solution

### (a) Battery current
Conduction starts when $100\sin\omega t=50$, i.e. $\omega t_1=30^\circ$ and ends at $150^\circ$ (for $D_1$); $D_2$ conducts in the next half-cycle from $210^\circ$ to $330^\circ$:

$$i(t)=\begin{cases}\dfrac{100|\sin\omega t|-50}{1020},&30^\circ<\omega t<150^\circ\ \text{and}\ 210^\circ<\omega t<330^\circ\\[2mm]0,&\text{otherwise}\end{cases}$$

Peak current: $\dfrac{100-50}{1020}=49.0$ mA at $90^\circ$ and $270^\circ$. The current consists of **two identical sine-segment pulses per cycle** (figure, right).

### (b) Average current
By symmetry the average over one cycle equals twice the half-cycle contribution:

$$I_{avg}=\frac1{2\pi}\cdot2\int_{\pi/6}^{5\pi/6}\frac{100\sin\theta-50}{1020}\,d\theta=\frac1{\pi\cdot1020}\Big[100\big(\cos30^\circ-\cos150^\circ\big)-50\cdot\frac{2\pi}3\Big]$$

$$=\frac{173.205-104.720}{\pi\cdot1020}=\frac{68.485}{3204.4}=\boxed{0.02137\ \text{A}\approx0.0214\ \text{A}}$$

Simulation of the circuit (all diode states, 3601 points over a period) gives the same average, $21.372$ mA.

| | value |
|---|---|
| conduction angle per pulse | $120^\circ$ (30°→150°) |
| peak current | 49.0 mA |
| average battery current | **0.0214 A** |
