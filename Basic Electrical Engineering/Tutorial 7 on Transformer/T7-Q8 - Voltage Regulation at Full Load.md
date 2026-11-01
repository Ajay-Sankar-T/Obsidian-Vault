---
tags: [EE1100, transformer, tutorial-solution, voltage-regulation]
---

# T7-Q8 — Voltage Regulation at Full Load

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q7 - OC and SC Test Parameters]] · Next: [[T7-Q9 - Efficiency and Regulation from Tests]]

> [!question] A 20 kVA, 2500/500 V, 50 Hz transformer: HV $r_1=8\ \Omega$, $x_1=17\ \Omega$; LV $r_2=0.3\ \Omega$, $x_2=0.7\ \Omega$. Find the voltage regulation and the secondary terminal voltage at full load for a power factor of (a) 0.8 lagging, (b) 0.8 leading, with the primary at 2500 V. *[(a) 10.59 %, 447.04 V (b) $-2.65\ \%$, 513.28 V]*

**Tests:** [[Transformer Voltage Regulation and Efficiency|regulation formula]], leading versus lagging load.

## Given
$a=5$, $E_2=2500/5=500$ V, $I_2=\dfrac{20000}{500}=40$ A.

## Principle and why it applies
Refer to the LV side: $R_{e2}=r_2+r_1/a^2=0.3+\dfrac8{25}=0.62\ \Omega$, $X_{e2}=0.7+\dfrac{17}{25}=1.38\ \Omega$. The regulation formula $E_2-V_2\approx I_2(R_{e2}\cos\phi\pm X_{e2}\sin\phi)$ uses $+$ for lagging, $-$ for leading.

## Solution
Drops: $I_2R_{e2}=24.8$ V, $I_2X_{e2}=55.2$ V.

**(a) 0.8 lag.** $E_2-V_2\approx24.8(0.8)+55.2(0.6)=19.84+33.12=52.96$ V.
$$VR=\frac{52.96}{500}=10.59\ \%,\qquad V_2=500-52.96=447.04\ \text{V}.$$
**(b) 0.8 lead.** $E_2-V_2\approx19.84-33.12=-13.28$ V.
$$VR=-2.66\ \%,\qquad V_2=500+13.28=513.28\ \text{V}.$$

| | approximate (sheet) | exact phasor sum |
|---|---|---|
| lag | $V_2=447.04$ V, $VR=10.59\ \%$ | $V_2=446.2$ V ($VR=10.76\ \%$) |
| lead | $V_2=513.28$ V, $VR=-2.66\ \%$ | $V_2=509.8$ V ($VR=-1.96\ \%$) |

## Result
(a) $VR=10.59\ \%$, $V_2=447.0$ V. (b) $VR=-2.66\ \%$ (voltage **rises**), $V_2=513.3$ V.

## Check
Exact: $V_1'^2=(V_2+\Delta_r)^2+\Delta_q^2$ with $\Delta_r=I(R\cos\phi\pm X\sin\phi)$, $\Delta_q=I(X\cos\phi\mp R\sin\phi)$; for the leading case the quadrature drop is large (59 V), so the approximation overestimates $V_2$ by 3.5 V (0.7 %). A leading (capacitive) load can **raise** the secondary voltage above the no-load value: [[Transformer Voltage Regulation and Efficiency#Voltage regulation|the zero-regulation angle]] is $-\tan^{-1}(R_{e2}/X_{e2})=-24.2^\circ$.

![[T7-Q8-Q9-plots.png]]

## Trap / alternative
Quoting the sign of $VR$ for the leading case as positive. The quoted $-2.65\ \%$ in the sheet is $-13.28/500=-2.656\ \%$. Exact regulation should be used when the quadrature drop is not small compared with $V_2$.

## Concepts used
- [[10 Single Phase Transformers]] · [[Transformer Voltage Regulation and Efficiency]]
