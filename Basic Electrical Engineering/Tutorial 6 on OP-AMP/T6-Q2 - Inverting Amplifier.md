---
tags: [EE1100, op-amp, tutorial-solution, inverting-amplifier]
---

# T6-Q2 — Inverting Amplifier

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q1 - Amplifier Gain and Design]] · Next: [[T6-Q3 - Non-inverting Amplifier]]

> [!question] The op-amp of Fig. 2 has $V_i=1$ mV with $R_1=15$ kΩ and $R_2=1.2$ MΩ. Find the voltage gain and the output voltage. *[Gain $-80$, $V_o=-80$ mV]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|inverting amplifier]], virtual ground.

## Given
$R_1=15$ kΩ from $V_i$ to the inverting input, $R_2=1.2$ MΩ in the feedback path, non-inverting input grounded, $V_i=1$ mV.

## Principle and why it applies
Negative feedback through $R_2$ and the grounded $+$ input: virtual short $v_-=v_+=0$ and no input current, so the current through $R_1$ must all flow through $R_2$.

## Solution
KCL at the inverting node: $\dfrac{V_i-0}{R_1}=\dfrac{0-V_o}{R_2}\ \Rightarrow\ V_o=-\dfrac{R_2}{R_1}V_i$.

![[T6-Q2-Q3-circuits.png]]

**(a)** $A_v=-\dfrac{1.2\times10^6}{15\times10^3}=-80$.
**(b)** $V_o=-80\times1\ \text{mV}=-80\ \text{mV}$.

## Result
$$A_v=-80,\qquad V_o=-80\ \text{mV}$$

## Check
Current in $R_1$: $1\ \text{mV}/15\ \text{k}\Omega=66.7$ nA; across $R_2$: $66.7\ \text{nA}\times1.2\ \text{M}\Omega=80$ mV, polarity such that $V_o$ is below ground ✓. The input resistance seen by the source is $R_1=15$ kΩ (not infinite).

## Trap / alternative
Quoting a positive gain: the minus sign is the 180° phase shift of the inverting configuration. Also $1+R_2/R_1=81$ is the **non-inverting** formula, not this one.

## Concepts used
- [[Theory - Operational Amplifiers]]
