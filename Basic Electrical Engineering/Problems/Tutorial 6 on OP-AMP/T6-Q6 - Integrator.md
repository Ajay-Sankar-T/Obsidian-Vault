---
tags: [EE1100, op-amp, tutorial-solution, integrator]
---

# T6-Q6 — Op-Amp Integrator

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q5 - Difference Amplifier]] · Next: [[T6-Q7 - Follower with Finite Gain]]

> [!question] A steady voltage $V_i=0.75$ V is applied to the circuit of Fig. 6 with $R=200$ kΩ and $C=2.5\ \mu$F (capacitor in the feedback path). The capacitor is initially uncharged. Find $V_o$ 100 ms after the input is applied. *[$-0.15$ V]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|integrator]], [[First-Order AC Transients (RC and RL)|capacitor charging]].

## Given
$V_i=0.75$ V (DC), $R=200$ kΩ, $C=2.5\ \mu$F, $v_C(0)=0$, $t=100$ ms.

## Principle and why it applies
The inverting node is a virtual ground, so the input current is $i=V_i/R$ (constant for DC) and the whole of it charges $C$. The capacitor voltage is $\frac1C\int i\,dt$ and $V_o=-v_C$ (the capacitor's right plate is the output).

## Solution
$$V_o(t)=-\frac1{RC}\int_0^tV_i\,d\tau=-\frac{V_it}{RC}.$$
$RC=200\times10^3\times2.5\times10^{-6}=0.5$ s. So
$$V_o(0.1\ \text{s})=-\frac{0.75\times0.1}{0.5}=-0.15\ \text{V}.$$
The output is a **ramp** of slope $-V_i/RC=-1.5$ V/s.

![[T6-Q6-integrator.png]]

## Result
$$V_o(100\ \text{ms})=-0.15\ \text{V}$$

## Check
Charge: $i=0.75/200\,\text{k}=3.75\ \mu$A for 0.1 s gives $0.375\ \mu$C; $v_C=0.375\ \mu\text{C}/2.5\ \mu\text{F}=0.15$ V ✓. Dimensionally $V_i\,t/RC$ is volts ✓.

## Trap / alternative
- It is **not** an RC exponential: the op-amp holds the input current constant, so the capacitor charges linearly.
- The ramp continues until the output saturates at the supply rail (about $\pm12$ V after 8 s here). Real integrators add a large resistor across $C$ to stop DC drift.

## Concepts used
- [[Theory - Operational Amplifiers]] · [[First-Order AC Transients (RC and RL)]]
