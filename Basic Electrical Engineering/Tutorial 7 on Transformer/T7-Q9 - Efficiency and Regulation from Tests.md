---
tags: [EE1100, transformer, tutorial-solution, efficiency, maximum-efficiency, voltage-regulation]
---

# T7-Q9 — Efficiency and Regulation from Test Data

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q8 - Voltage Regulation at Full Load]] · Next: [[T7-Q10 - Maximum Efficiency and Regulation]]

> [!question] A 10 kVA, 2500/250 V transformer gave: OC test (LV side) 250 V, 0.8 A, 50 W; SC test (HV side) 60 V, 3 A, 45 W. (a) Efficiency at $\tfrac14$, $\tfrac12$, 1 and $1\tfrac14$ of full load, 0.8 pf. (b) The load (kVA) at which maximum efficiency occurs and its value at 0.8 pf. (c) Voltage regulation and secondary voltage at rated load for (i) 0.8 lag, (ii) 0.8 lead. *[(a) 97.32, 98.28, 98.40, 98.28 % (b) 7.905 kVA, 98.44 % (c) (i) 2.5 %, 243.75 V (ii) $-1.21\ \%$, 253.025 V]*

**Tests:** [[Transformer Voltage Regulation and Efficiency|efficiency and regulation]] from [[10 Single Phase Transformers#OC and SC tests|OC and SC tests]].

## Given
Rated HV current $I_{1r}=\dfrac{10000}{2500}=4$ A. The SC test was run at **3 A**, not at rated current. OC: $P_c=50$ W. SC: $V_{sc}=60$ V, $I_{sc}=3$ A, $P_{sc}=45$ W.

## Principle and why it applies
Core loss $=50$ W (OC power), constant for rated voltage. Copper loss varies as $I^2$, so scale the SC loss to the actual current:
$$P_{cu,FL}=P_{sc}\Big(\frac{I_{1r}}{I_{sc}}\Big)^2=45\Big(\frac43\Big)^2=80\ \text{W}.$$
At a fraction $x$ of full load: $P_{cu}=80x^2$, output $=10000\,x\,(0.8)$ W.

## Solution
**(a)** $\eta(x)=\dfrac{8000x}{8000x+50+80x^2}$:

| $x$ | output | losses | $\eta$ |
|---|---|---|---|
| $\tfrac14$ | 2000 W | $50+5$ | **97.32 %** |
| $\tfrac12$ | 4000 W | $50+20$ | **98.28 %** |
| 1 | 8000 W | $50+80$ | **98.40 %** |
| $1\tfrac14$ | 10000 W | $50+125$ | **98.28 %** |

**(b)** Maximum efficiency when copper loss equals core loss: $80x^2=50\Rightarrow x=\sqrt{50/80}=0.7906$. Load $=0.7906\times10=\boxed{7.906\ \text{kVA}}$; output $=6325$ W,
$$\eta_{max}=\frac{6325}{6325+2(50)}=\boxed{98.44\ \%}.$$

**(c)** From the SC test (HV side): $Z_{eH}=\dfrac{60}{3}=20\ \Omega$, $R_{eH}=\dfrac{45}{9}=5\ \Omega$, $X_{eH}=\sqrt{20^2-5^2}=19.36\ \Omega$. At rated current $4$ A: $IR=20$ V, $IX=77.46$ V.
$$VR_{lag}=\frac{20(0.8)+77.46(0.6)}{2500}=\frac{62.48}{2500}=2.50\ \%,\qquad V_2=250(1-0.025)=243.75\ \text{V}$$
$$VR_{lead}=\frac{20(0.8)-77.46(0.6)}{2500}=-1.22\ \%,\qquad V_2=250(1+0.0122)=253.05\ \text{V}$$

![[T7-Q8-Q9-plots.png]]

## Result
(a) $97.32,\ 98.28,\ 98.40,\ 98.28\ \%$. (b) $7.906$ kVA, $98.44\ \%$. (c) (i) $2.50\ \%$, $243.75$ V; (ii) $-1.22\ \%$, $253.05$ V.

## Check
Because $\eta=\big[1+\frac{P_c}{8000x}+\frac{80x}{8000}\big]^{-1}$ is unchanged under $x\to x_{opt}^2/x$, loads $x$ and $0.625/x$ have the same efficiency: $\eta(0.5)=\eta(1.25)=98.28\ \%$. The maximum is flat: the curve moves by only about 0.1 % between $x=0.5$ and $x=1.25$. The sheet's $-1.21\ \%$ and $253.025$ V use $-1.21\ \%$ (rounded down); computed $-1.219\ \%$ gives $253.05$ V.

## Trap / alternative
**Using 45 W as the full-load copper loss**: the SC test was done at 3 A, below rated 4 A. With 45 W the full-load efficiency would be $8000/(8000+95)=98.8\ \%$, not the sheet's $98.40\ \%$. Always scale by $(I_{rated}/I_{test})^2$.

## Concepts used
- [[10 Single Phase Transformers]] · [[Transformer Voltage Regulation and Efficiency]]
