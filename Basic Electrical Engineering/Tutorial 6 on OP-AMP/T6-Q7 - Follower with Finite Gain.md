---
tags: [EE1100, op-amp, tutorial-solution, voltage-follower, non-ideal]
---

# T6-Q7 — Voltage Follower with a Real Op-Amp

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q6 - Integrator]] · Next: [[T6-Q8 - Photodiode Amplifier]]

> [!question] Fig. 7: voltage follower, source resistance $R_s=1$ kΩ, load $R_L=10$ kΩ. The op-amp has $A=10^5$, $R_i=100$ kΩ, $R_o=100\ \Omega$. For $V_o=10$ V, find $V_s$ and $V_o/V_s$. *[$V_s=10.0001$ V, $V_o/V_s=0.9999$]*

**Tests:** non-ideal op-amp model ([[Theory - Operational Amplifiers#4. Real op-amp|$A$, $R_i$, $R_o$]]), the voltage follower.

## Given
$R_s=1$ kΩ, $R_L=10$ kΩ, $A=10^5$, $R_i=100$ kΩ, $R_o=100\ \Omega$, $V_o=10$ V. Output tied to the inverting input.

## Principle and why it applies
Here the finite parameters matter, so the ideal rules ($v_d=0$, $i=0$) are replaced by the model: input resistance $R_i$ across the inputs, a source $Av_d$ in series with $R_o$ at the output ($v_d=v_+-v_-$).

![[T6-Q7-model.png]]

## Solution
1. Load current $I_o=V_o/R_L=10/10\,\text{k}=1$ mA.
2. Output equation: $V_o=Av_d-R_oI_o\ \Rightarrow\ v_d=\dfrac{V_o+R_oI_o}{A}=\dfrac{10+0.1}{10^5}=1.01\times10^{-4}$ V.
3. Input current $i=\dfrac{v_d}{R_i}=\dfrac{1.01\times10^{-4}}{10^5}=1.01\times10^{-9}$ A.
4. KVL on the input side: $V_s=R_si+v_d+V_o$ ($v_-=V_o$ because of the feedback wire):
$$V_s=10^3(1.01\times10^{-9})+1.01\times10^{-4}+10=10.000102\ \text{V}.$$
5. Gain: $\dfrac{V_o}{V_s}=\dfrac{10}{10.000102}=0.99999$.

## Result
$$V_s\approx10.0001\ \text{V},\qquad\frac{V_o}{V_s}\approx0.99999\ (\approx1)$$

## Check
The relative departure from unity is $\dfrac{v_d}{V_o}=\dfrac1A\Big(1+\dfrac{R_o}{R_L}\Big)=1.01\times10^{-5}$, as found. The input current is a nanoamp, so $R_s$ drops only 1 µV: the follower presents an effectively infinite impedance to the source and a near-zero impedance to the load.

## Trap / alternative
Using the ideal rule would give exactly $V_s=V_o$, $V_o/V_s=1$, which is the right idea but hides the question. The sheet prints $0.9999$ (truncated); the computed value is $0.99999$.

## Concepts used
- [[Theory - Operational Amplifiers]]
