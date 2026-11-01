---
tags: [EE1100, transformer, tutorial-solution, emf-equation]
---

# T7-Q1 — Turns and Core Area from the EMF Equation

Hub: [[Tutorial 7 on Transformer]] · Next: [[T7-Q2 - Exciting Current and Primary Current]]

> [!question] The emf per turn of a single-phase 2310/220 V, 50 Hz transformer is approximately 13 V. Calculate (a) the number of primary and secondary turns, (b) the net core cross-section for a maximum flux density of 1.4 Wb/m². *[(a) 189, 18 (b) 393 cm²]*

**Tests:** [[10 Single Phase Transformers#EMF equation and turns ratio|EMF equation]] $E=4.44fN\Phi_m$, turns ratio.

## Given
$V_1/V_2=2310/220=10.5$, $f=50$ Hz, $E/N\approx13$ V, $B_m=1.4$ T.

## Principle and why it applies
Both windings link the same core flux, so every turn carries the same emf $E_t=4.44f\Phi_m$. Hence $N=E/E_t$ and the flux amplitude is $\Phi_m=E_t/4.44f$, with $A=\Phi_m/B_m$.

## Solution
**(a)** $N_1=\dfrac{2310}{13}=177.7$, $N_2=\dfrac{220}{13}=16.9$. Turns must be whole numbers **in the exact ratio 10.5:1**; the nearest pair is $N_1=189$, $N_2=18$, which gives $E_t=\dfrac{220}{18}=12.22$ V per turn ("approximately 13 V" in the problem).

**(b)** $\Phi_m=\dfrac{E_t}{4.44f}=\dfrac{12.22}{4.44\times50}=55.05$ mWb;
$$A=\frac{\Phi_m}{B_m}=\frac{0.05505}{1.4}=0.03932\ \text{m}^2=393\ \text{cm}^2.$$

## Result
$$N_1=189,\ N_2=18,\qquad A_{net}=393\ \text{cm}^2$$

## Check
$N_1/N_2=189/18=10.5$ ✓. Using exactly $13$ V/turn gives $A=\dfrac{13}{4.44\cdot50\cdot1.4}=418\ \text{cm}^2$ and non-integer turns; the key's 393 cm² uses $E_t=12.22$ V. $E_1=4.44\times50\times189\times0.05505=2310$ V ✓.

## Trap / alternative
Rounding $N_1$ and $N_2$ independently (178 and 17) breaks the ratio. Also "net" core area excludes insulation between laminations (a stacking factor of about 0.9 would make the gross section larger).

## Concepts used
- [[10 Single Phase Transformers]]
