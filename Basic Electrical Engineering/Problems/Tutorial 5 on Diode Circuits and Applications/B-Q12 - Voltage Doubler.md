---
tags: [EE1100, diodes, tutorial-solution, voltage-doubler]
---

# B-Q12 — Voltage Doubler

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q11 - Full-Wave Rectifier with Battery]]

> [!question] Fig. 11 (source $e$, diodes $D_1$, $D_2$, capacitors $C_1$, $C_2$ and resistor $R$): determine the magnitude of the maximum voltage across $R$ if $e=V_m\sin\omega t$. $R$ is very large.

![[B12-doubler.png]]

## 1. Theory

Two half-wave **peak detectors** of opposite polarity share the same source:
- $D_1$ (anode to $C_1$, cathode to the source's upper terminal) charges $C_1$ during the **negative** half-cycle.
- $D_2$ (anode to the source's upper terminal, cathode to $C_2$) charges $C_2$ during the **positive** half-cycle.

The resistor connects the two capacitor tops, so the output is the **sum** of the two capacitor voltages (they are in series through $R$).

## 2. Solution

Call $P$ the junction of $D_1$, $C_1$ and $R$, and $Q$ the junction of $D_2$, $C_2$ and $R$ (the bottom plates of both capacitors are joined to the lower source terminal, taken as ground).

**Negative peak of $e$** ($e=-V_m$): $D_1$ is forward biased (its anode is at $P$, its cathode at the source's upper terminal at $-V_m$), so it charges $C_1$ until $V_P=-V_m$ (ideal diode). $D_2$ is reverse biased.

**Positive peak of $e$** ($e=+V_m$): $D_2$ conducts and charges $C_2$ until $V_Q=+V_m$. $D_1$ is reverse biased ($V_P=-V_m$ is below $e$).

Since $R$ is very large the capacitors do not discharge appreciably, so they keep these peak values:

$$V_P=-V_m,\qquad V_Q=+V_m$$

$$V_R=V_Q-V_P=V_m-(-V_m)=\boxed{2V_m}$$

(each capacitor sits at $V_m$ in magnitude, in series through $R$: a voltage **doubler**).

## 3. Numerical check

Simulation with $V_m=10$ V, $C_1=C_2=100\ \mu$F, $R=1$ MΩ, $f=50$ Hz, ideal diodes: after about one and a half cycles $V_P\to-9.999$ V, $V_Q\to+9.997$ V, and $\max|V_R|=19.9987$ V $\approx2V_m$. Each diode conducts only for a brief interval near its peak, and the output stays practically constant at $2V_m$ (the right panel of the figure).

> [!note] Remarks
> - The diode PIV is $2V_m$ (e.g. when $e=+V_m$ and $V_P=-V_m$ across $D_1$).
> - With a finite load the output droops and has ripple at the source frequency; with practical diodes $V_R\approx2(V_m-V_\gamma)$.
> - Cascading more diode-capacitor stages gives voltage triplers, quadruplers etc. (Cockcroft–Walton multiplier).
