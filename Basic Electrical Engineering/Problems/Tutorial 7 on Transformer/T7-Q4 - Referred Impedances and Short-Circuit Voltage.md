---
tags: [EE1100, transformer, tutorial-solution, referred-impedance, short-circuit]
---

# T7-Q4 — Referred Impedances and Short-Circuit Voltage

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q3 - Voltage and Frequency Other Than Rated]] · Next: [[T7-Q5 - Secondary Voltage Under Load]]

> [!question] A 33 kVA, 2200/220 V, 50 Hz transformer: HV $r_1=2.4\ \Omega$, $x_1=6\ \Omega$; LV $r_2=0.03\ \Omega$, $x_2=0.07\ \Omega$. (a) $r_1,x_1$ referred to the secondary. (b) $r_2,x_2$ referred to the primary. (c) Equivalent resistance and reactance referred to (i) primary, (ii) secondary. (d) Total ohmic loss at full load. (e) The voltage to apply to the HV side for a short-circuit current of 160 A in the LV winding, and the power input. *[(a) 0.024, 0.06 Ω (b) 3, 7 Ω (c) (i) 5.4, 13 Ω (ii) 0.054, 0.13 Ω (d) 1216 W (e) 225 V, 1382 W]*

**Tests:** [[Gears, Transformers and Reflected Impedance|reflected impedance]] $Z'=Z/a^2$ or $a^2Z$, equivalent impedance, short-circuit test.

## Given
$a=N_1/N_2=2200/220=10$.

## Principle and why it applies
An impedance on one side appears on the other multiplied by the **square** of the turns ratio (impedance $=V/I$, voltage scales by $a$, current by $1/a$). Referring both windings to one side puts them in series.

## Solution
**(a)** To the LV side divide by $a^2=100$: $r_1'=\dfrac{2.4}{100}=0.024\ \Omega$, $x_1'=\dfrac{6}{100}=0.06\ \Omega$.
**(b)** To the HV side multiply by 100: $r_2'=0.03\times100=3\ \Omega$, $x_2'=0.07\times100=7\ \Omega$.
**(c)** (i) Primary: $R_{e1}=r_1+r_2'=5.4\ \Omega$, $X_{e1}=x_1+x_2'=13\ \Omega$. (ii) Secondary: $R_{e2}=r_2+r_1'=0.054\ \Omega$, $X_{e2}=0.13\ \Omega$.
**(d)** Full-load currents: $I_1=\dfrac{33000}{2200}=15$ A, $I_2=\dfrac{33000}{220}=150$ A.
$$P_{cu}=I_1^2R_{e1}=15^2(5.4)=1215\ \text{W}\quad(=150^2\times0.054=1215\ \text{W}).$$
**(e)** Short-circuit impedance on the LV side: $Z_{e2}=\sqrt{0.054^2+0.13^2}=0.1408\ \Omega$. LV voltage for 160 A: $160\times0.1408=22.52$ V, so on the HV side
$$V_{sc}=10\times22.52=225.2\ \text{V},\qquad P_{sc}=I^2R_{e2}=160^2(0.054)=1382\ \text{W}.$$

## Result
(a) $0.024\ \Omega$, $0.06\ \Omega$ (b) $3\ \Omega$, $7\ \Omega$ (c) (i) $5.4\ \Omega$, $13\ \Omega$ (ii) $0.054\ \Omega$, $0.13\ \Omega$ (d) $1215$ W (e) $225$ V, $1382$ W.

## Check
$R_{e1}=a^2R_{e2}$: $100\times0.054=5.4$ ✓. The ohmic loss is the same whichever side it is computed on ✓. The sheet's 1216 W is rounding of the same $1215$ W.

## Trap / alternative
Using $a$ instead of $a^2$ for resistances, or dividing instead of multiplying when going the other way. A short-circuit "voltage" applied for the test is only about 10 % of rated (here $225/2200=10.2\ \%$): the flux is low, so core loss is negligible and the input power is all copper loss.

## Concepts used
- [[10 Single Phase Transformers]]
