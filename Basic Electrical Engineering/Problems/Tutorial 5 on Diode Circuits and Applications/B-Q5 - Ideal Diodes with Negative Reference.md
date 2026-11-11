---
tags: [EE1100, diodes, tutorial-solution, logic]
---

# B-Q5 — Ideal Diodes with a −5 V and a 0 V Input

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q4 - Diode AND Gate]] · Next: [[B-Q6 - Diode Clamper]]

> [!question] What is $V_0$ in the circuit of Fig. 5 (inputs $-5$ V and $0$ V through diodes, load $R_L=1$ kΩ to ground)? Assume ideal diodes.

![[B4-B5-circuits.png]]

## 1. Theory

Same structure as the AND gate ([[B-Q4 - Diode AND Gate]]): the diode cathodes are the inputs, the anodes meet at $V_0$, and $V_0$ is tied to ground through $R_L$ (here the pull-up level is 0 V). The diode with the **lowest** cathode voltage conducts and pulls the node down to that voltage (ideal: no drop).

## 2. Solution

Assume $D_1$ (cathode at $-5$ V) is ON: $V_0=-5$ V.
**Check $D_2$:** anode $=V_0=-5$ V, cathode $=0$ V, so $v_{D2}=-5$ V $<0$: reverse biased, OFF ✓.
**Check $D_1$:** current from ground through $R_L$ into the node and out through $D_1$ to the $-5$ V source: $I=\dfrac{0-(-5)}{1\text{ k}}=5\ \text{mA}>0$ ✓.

(If instead $D_2$ were ON, $V_0=0$ and $D_1$ would have anode 0 V, cathode $-5$ V: forward biased with no resistance to limit it — inconsistent.)

$$\boxed{V_0=-5\ \text{V}},\qquad I_{R_L}=I_{D1}=5\ \text{mA},\ I_{D2}=0.$$

A circuit simulation gives $V_0=-4.999995$ V with states ($D_1$ ON, $D_2$ OFF).
