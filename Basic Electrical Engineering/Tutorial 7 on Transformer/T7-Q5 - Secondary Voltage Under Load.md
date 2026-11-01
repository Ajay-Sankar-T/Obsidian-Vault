---
tags: [EE1100, transformer, tutorial-solution, voltage-regulation, load-voltage]
---

# T7-Q5 — Secondary Terminal Voltage Under Load

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q4 - Referred Impedances and Short-Circuit Voltage]] · Next: [[T7-Q6 - Equivalent Circuit on the LT Side]]

> [!question] A 10 kVA, 2500/250 V transformer: $r_1=4.8\ \Omega$, $x_1=11.2\ \Omega$, $r_2=0.048\ \Omega$, $x_2=0.112\ \Omega$. With the primary held at 2500 V, find the secondary terminal voltage when (a) the LV side carries a load impedance $5+j3.5\ \Omega$, (b) the transformer delivers rated current at 0.8 pf lagging. *[(a) 242 V (b) 241.6 V]*

**Tests:** [[Transformer Voltage Regulation and Efficiency|voltage regulation]], series equivalent impedance.

## Given
$a=10$; $V_1=2500$ V so $E_2=V_1/a=250$ V (no-load secondary voltage). Rated LV current $I_{2r}=10000/250=40$ A.

## Principle and why it applies
Refer everything to the LV side: $R_{e2}=r_2+r_1/a^2=0.048+0.048=0.096\ \Omega$, $X_{e2}=0.112+0.112=0.224\ \Omega$. The source ($250$ V) drives $Z_{e2}$ in series with the load, so the terminal voltage is the source minus the drop in $Z_{e2}$.

## Solution
**(a)** $Z_{tot}=(5+0.096)+j(3.5+0.224)=5.096+j3.724\ \Omega$, $|Z_{tot}|=6.311\ \Omega$, $I_2=250/6.311=39.61$ A.
$$V_2=I_2|Z_L|=39.61\times\sqrt{5^2+3.5^2}=39.61\times6.103=241.7\ \text{V}.$$

**(b)** Rated current at 0.8 lag: $I_2=40$ A, $\phi=36.87^\circ$. Drops: $I_2R_{e2}=3.84$ V, $I_2X_{e2}=8.96$ V. With $V_2$ as reference,
$$250^2=(V_2+3.84\cdot0.8+8.96\cdot0.6)^2+(8.96\cdot0.8-3.84\cdot0.6)^2=(V_2+8.448)^2+4.864^2$$
$$V_2=\sqrt{62500-23.7}-8.448=241.5\ \text{V}.$$
Approximate (regulation) formula: $V_2\approx250-8.448=241.55$ V.

## Result
(a) $V_2=241.7$ V ($\approx242$ V). (b) $V_2=241.5$ V (approximate method $241.6$ V).

## Check
$\%VR=\dfrac{250-241.5}{250}=3.4\ \%$, i.e. $r_{e,pu}\cos\phi+x_{e,pu}\sin\phi$ with $r_{pu}=\frac{40\cdot0.096}{250}=1.54\ \%$, $x_{pu}=3.58\ \%$: $1.23+2.15=3.38\ \%$ ✓.

## Trap / alternative
Using the **unreferred** impedances, or dropping $r_1$ and $x_1$ (they are as large as $r_2,x_2$ once referred). Also, (b) specifies the current at rated value, not the load impedance.

## Concepts used
- [[10 Single Phase Transformers]] · [[Transformer Voltage Regulation and Efficiency]]
