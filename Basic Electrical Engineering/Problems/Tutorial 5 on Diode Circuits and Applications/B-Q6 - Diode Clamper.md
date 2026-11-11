---
tags: [EE1100, diodes, tutorial-solution, clamper]
---

# B-Q6 — Diode Clamper

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q5 - Ideal Diodes with Negative Reference]] · Next: [[B-Q7 - Asymmetric Diode Resistor Network]]

> [!question] Fig. 6: a square wave $V_i=\pm20$ V (period $T$) is applied through a capacitor $C$; the node $V_0$ has a diode to ground and a resistor $R$ to ground. Sketch $V_0$ (ideal diode).

![[B6-clamper.png]]

> [!note] Circuit reading
> The diode symbol points **up** (anode to ground, cathode to the $V_0$ node), so the diode conducts whenever $V_0$ tries to go below 0 V. $RC\gg T$ is assumed (the standard clamper condition).

## 1. Theory

A clamper adds a dc level to the input. With the capacitor in series and a diode to ground:
- Whenever the diode conducts, the output node is held at 0 V (ideal) and the capacitor charges to the voltage $V_C=V_i-V_0=V_i$ at that instant.
- When the diode is OFF, the capacitor cannot discharge appreciably through $R$ (since $RC\gg T$), so $V_C$ stays constant and $V_0=V_i-V_C$ follows the input shifted by $-V_C$.

KVL: $V_0=V_i-V_C$.

## 2. Solution

**Steady state.** When $V_i=-20$ V the diode turns ON, $V_0=0$ and $V_C=-20-0=-20$ V (capacitor charged with the source-side plate negative). During the positive half-cycle, $V_C$ stays at $-20$ V, so
$$V_0=20-(-20)=+40\ \text{V}\quad(\text{diode OFF}).$$

| Interval | $V_i$ | Diode | $V_0$ |
|---|---|---|---|
| first half (positive) | $+20$ V | OFF | $+40$ V |
| second half (negative) | $-20$ V | ON | $0$ V |

The output is a square wave between **0 and +40 V**: the input's negative peak has been **clamped to 0 V** (a "positive clamper"), and the waveform keeps the same peak-to-peak value, 40 V.

**Start-up transient.** If the source starts at $+20$ V with the capacitor uncharged, the first half-cycle gives $V_0=+20$ V (decaying slowly with $RC$); the capacitor is charged to $-20$ V in the first negative half-cycle, and from then on the output is 0 / 40 V. In the figure ($RC=50T$) the steady state is reached after the first cycle.

> [!success] Result
> $V_0$ swings between $0$ and $+40$ V: average value 20 V = the peak of the input, $V_C=-20$ V.
> Numerical check: the simulated steady-state output has minimum $-1.6\times10^{-4}$ V and maximum $39.998$ V.
