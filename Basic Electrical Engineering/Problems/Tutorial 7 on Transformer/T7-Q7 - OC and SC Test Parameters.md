---
tags: [EE1100, transformer, tutorial-solution, open-circuit-test, short-circuit-test]
---

# T7-Q7 — Equivalent-Circuit Parameters from OC and SC Tests

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q6 - Equivalent Circuit on the LT Side]] · Next: [[T7-Q8 - Voltage Regulation at Full Load]]

> [!question] A 20 kVA, 2500/250 V, 50 Hz transformer gave: OC test (LV side) 250 V, 1.4 A, 105 W; SC test (HV side) 104 V, 8 A, 320 W. Compute the parameters of the approximate equivalent circuit referred to the HV and LV sides, and draw the exact equivalent circuit referred to the LV side. *[HV: $R_{1H}=2.5$, $X_{1H}=6$, $R_{cH}=59524$, $X_{\phi H}=18726\ \Omega$; LV: $0.025$, $0.06$, $595.24$, $187.26\ \Omega$]*

**Tests:** [[10 Single Phase Transformers#OC and SC tests|OC and SC tests]], referring to the other side.

## Given
OC: $V_0=250$ V, $I_0=1.4$ A, $P_0=105$ W on the LV side. SC: $V_{sc}=104$ V, $I_{sc}=8$ A, $P_{sc}=320$ W on the HV side. Rated HV current $20000/2500=8$ A (the SC test is at rated current).

## Principle and why it applies
**OC test** (rated voltage on the LV side, HV open): the current is tiny, so copper loss is negligible and $P_0$ is the **core loss**, giving the shunt branch. **SC test** (HV side, LV shorted, low voltage, rated current): flux is tiny so core loss is negligible, $P_{sc}$ is **copper loss**, giving the series branch. The two branches are measured on different sides, so refer one set to the other with $a^2=100$.

## Solution
**Shunt branch, from the OC test (LV side).**
$$I_c=\frac{P_0}{V_0}=\frac{105}{250}=0.42\ \text{A},\quad I_\phi=\sqrt{1.4^2-0.42^2}=1.3355\ \text{A}$$
$$R_{cL}=\frac{V_0}{I_c}=595.2\ \Omega,\qquad X_{\phi L}=\frac{V_0}{I_\phi}=187.2\ \Omega.$$
Referred to the HV side (multiply by 100): $R_{cH}=59524\ \Omega$, $X_{\phi H}=18719\ \Omega$ (the sheet's 18726 comes from rounding $I_\phi$ to 1.335 A before dividing).

**Series branch, from the SC test (HV side).**
$$Z_{eH}=\frac{104}{8}=13\ \Omega,\quad R_{eH}=\frac{320}{8^2}=5\ \Omega,\quad X_{eH}=\sqrt{13^2-5^2}=12\ \Omega.$$
Split equally between the windings ($R_{1H}=R_2'=2.5\ \Omega$, $X_{1H}=X_2'=6\ \Omega$). Referred to the LV side (divide by 100): $R_{eL}=0.05\ \Omega$, $X_{eL}=0.12\ \Omega$, i.e. $R_{1L}=R_1'=0.025\ \Omega$, $X_{1L}=0.06\ \Omega$ for each winding.

| | HV side | LV side |
|---|---|---|
| $R_1=R_2'$ | 2.5 Ω | 0.025 Ω |
| $X_1=X_2'$ | 6 Ω | 0.06 Ω |
| $R_c$ | 59 524 Ω | 595.2 Ω |
| $X_\phi$ | 18 719 Ω (sheet 18 726) | 187.2 Ω (sheet 187.26) |

**Exact equivalent circuit referred to the LV side:** primary leakage $0.025+j0.06\ \Omega$, then the shunt branch ($R_c=595.2\ \Omega\parallel jX_\phi=j187.3\ \Omega$), then the secondary leakage $0.025+j0.06\ \Omega$ and the ideal transformer.

![[T7-Q7-circuit.png]]

## Result
Parameters in the table above; the exact circuit has the shunt branch between the primary and secondary leakage impedances.

## Check
Core loss at rated voltage: $250^2/595.2=105$ W ✓. Copper loss at rated current: $8^2\times5=320$ W ✓. The equal split is a convention; only the sum $R_e,X_e$ is measurable.

## Trap / alternative
Using the OC current as if it were purely magnetising (ignoring the core-loss component), or treating the SC voltage as the applied rating. In the **approximate** circuit the shunt branch moves to the input terminals and the series impedance is the whole $R_e+jX_e$; in the **exact** circuit the shunt branch sits between the two windings' leakage impedances.

## Concepts used
- [[10 Single Phase Transformers]] · [[Gears, Transformers and Reflected Impedance]]
