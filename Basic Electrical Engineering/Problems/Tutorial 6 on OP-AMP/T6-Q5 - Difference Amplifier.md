---
tags: [EE1100, op-amp, tutorial-solution, difference-amplifier]
---

# T6-Q5 — Difference Amplifier

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q4 - Inverting Summer]] · Next: [[T6-Q6 - Integrator]]

> [!question] Fig. 5: $V_1$ and $V_2$ each through 8 kΩ to the inverting and non-inverting inputs; feedback 120 kΩ; 120 kΩ from the $+$ input to ground. Find $V_o$ for (a) $V_1=4$ mV, $V_2=0$; (b) $V_1=0$, $V_2=6$ mV; (c) $V_1=40$ mV, $V_2=30$ mV; (d) $V_1=25$ mV, $V_2=40$ mV. *[(a) $-60$ mV (b) 90 mV (c) $-150$ mV (d) 225 mV]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|difference amplifier]], superposition.

## Given
$R_1=R_3=8$ kΩ, $R_2=R_4=120$ kΩ (the two ratios are equal: $R_2/R_1=R_4/R_3=15$).

## Principle and why it applies
Superposition on an ideal op-amp. With $V_2=0$ it is an inverting stage ($-\frac{R_2}{R_1}V_1$). With $V_1=0$ it is a non-inverting stage fed through the divider $\frac{R_4}{R_3+R_4}$.

## Solution
$$V_o=\Big(1+\frac{R_2}{R_1}\Big)\frac{R_4}{R_3+R_4}V_2-\frac{R_2}{R_1}V_1=16\cdot\frac{120}{128}V_2-15V_1=15\,(V_2-V_1).$$

| | $V_1$ | $V_2$ | $V_o=15(V_2-V_1)$ |
|---|---|---|---|
| (a) | 4 mV | 0 | $-60$ mV |
| (b) | 0 | 6 mV | $+90$ mV |
| (c) | 40 mV | 30 mV | $-150$ mV |
| (d) | 25 mV | 40 mV | $+225$ mV |

![[T6-Q4-Q5-circuits.png]]

## Result
$V_o=15\,(V_2-V_1)$: (a) $-60$ mV, (b) $90$ mV, (c) $-150$ mV, (d) $225$ mV.

## Check
(c) and (d) show that only the **difference** matters: a common-mode shift of the two inputs changes nothing (the ratio-matching condition). With mismatched resistors a common-mode part leaks into the output (CMRR of the circuit).

## Trap / alternative
Using the *inverting* gain $-15$ for both inputs: the $V_2$ path has a positive gain. Also the divider $\frac{120}{8+120}$ and the factor $(1+15)$ cancel to exactly $15$ only when $R_2/R_1=R_4/R_3$.

## Concepts used
- [[Theory - Operational Amplifiers]] · [[Voltage Divider Rule]]
