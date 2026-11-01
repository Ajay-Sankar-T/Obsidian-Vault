---
tags: [EE1100, op-amp, tutorial-solution, non-inverting-amplifier]
---

# T6-Q3 — Non-inverting Amplifier

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q2 - Inverting Amplifier]] · Next: [[T6-Q4 - Inverting Summer]]

> [!question] Fig. 3: the input voltage is $-0.5$ V; the feedback resistor is 15 kΩ and the resistor from the inverting input to ground is 6.8 kΩ. Find (a) the voltage gain, (b) the output voltage. *[3.2058, $-1.6029$ V]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|non-inverting amplifier]], [[Voltage Divider Rule]].

## Given
Input to the $+$ terminal; $R_f=15$ kΩ (output to $-$); $R_g=6.8$ kΩ ($-$ to ground); $V_{in}=-0.5$ V.

## Principle and why it applies
The input drives the **non-inverting** pin, and the feedback divides the output down to the inverting pin. Rule: $v_-=v_+=V_{in}$, and the divider gives $v_-=V_o\dfrac{R_g}{R_g+R_f}$.

## Solution
$V_o=V_{in}\Big(1+\dfrac{R_f}{R_g}\Big)$.

**(a)** $A_v=1+\dfrac{15}{6.8}=1+2.2059=\boxed{3.2059}$.
**(b)** $V_o=3.2059\times(-0.5)=\boxed{-1.603\ \text{V}}$.

![[T6-Q2-Q3-circuits.png]]

## Result
$A_v=3.206$ (positive: same polarity), $V_o=-1.603$ V.

## Check
Divider: $V_o\frac{6.8}{21.8}=-1.603\times0.3119=-0.5$ V $=V_{in}$ ✓. The gain is always $\ge1$ for this configuration.

## Trap / alternative
Using the inverting formula $-R_f/R_g=-2.2$: the input is on the $+$ terminal here, so the sign is positive and the "1 +" appears. The sheet's $3.2058$ is rounding of $3.20588$.

## Concepts used
- [[Theory - Operational Amplifiers]] · [[Voltage Divider Rule]]
