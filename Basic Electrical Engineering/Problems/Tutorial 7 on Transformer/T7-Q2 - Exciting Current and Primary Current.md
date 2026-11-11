---
tags: [EE1100, transformer, tutorial-solution, exciting-current, phasors]
---

# T7-Q2 — Exciting Current and Primary Current Under Load

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q1 - Turns and Core Area]] · Next: [[T7-Q3 - Voltage and Frequency Other Than Rated]]

> [!question] (a) A 2200/220 V, 50 Hz transformer takes an exciting current of 0.6 A and a core loss of 361 W with the HV side at rated voltage. Find the two components of the exciting current. (b) It supplies 60 A at 0.8 pf lagging on the LV side. Find the primary current and its power factor, ignoring leakage drops. *[(a) $I_c=0.164$ A, $I_\phi=0.577$ A (b) 6.48 A, 0.766 lag]*

**Tests:** [[10 Single Phase Transformers]] — no-load phasor diagram, current referred to the primary.

## Given
$V_1=2200$ V, $I_0=0.6$ A, $P_c=361$ W; $I_2=60$ A at $\cos\phi=0.8$ lag, turns ratio 10.

## Principle and why it applies
The exciting current $I_0$ has a **core-loss** component $I_c$ in phase with $V_1$ and a **magnetising** component $I_\phi$ lagging $V_1$ by $90^\circ$; $I_0=I_c-jI_\phi$. Under load the primary current is the phasor sum of $I_0$ and the load current referred to the primary, $I_2'=I_2/a$ ($a=10$), with no leakage drops so $V_1$ stays at its rated value and $I_0$ is unchanged.

## Solution
**(a)** $I_c=\dfrac{P_c}{V_1}=\dfrac{361}{2200}=0.164$ A, $I_\phi=\sqrt{I_0^2-I_c^2}=\sqrt{0.36-0.0269}=0.577$ A.

**(b)** $I_2'=\dfrac{60}{10}=6$ A, lagging $V$ by $\cos^{-1}0.8$: $I_2'=6(0.8-j0.6)=4.8-j3.6$ A.
$$I_1=I_0+I_2'=(0.164-j0.577)+(4.8-j3.6)=4.964-j4.177\ \text{A}$$
$$|I_1|=\sqrt{4.964^2+4.177^2}=6.49\ \text{A},\qquad\cos\phi_1=\frac{4.964}{6.49}=0.765\ \text{(lag)}.$$

## Result
(a) $I_c=0.164$ A, $I_\phi=0.577$ A. (b) $I_1=6.49$ A at pf $0.765$ lagging.

## Check
The lagging load current plus a lagging magnetising current gives an even lower power factor than the load alone ($0.8\to0.765$) ✓. Real power in: $2200\times4.964=10.92$ kW; real power out $=220\times60\times0.8=10.56$ kW, plus core loss $0.36$ kW ✓.

## Trap / alternative
Adding **magnitudes** ($0.6+6$): the currents are not in phase. The sheet gives $6.48$ A, which differs from $6.488$ only by rounding.

## Concepts used
- [[10 Single Phase Transformers]] · [[Phasors and Complex Algebra]]
