---
tags: [EE1100, transformer, tutorial-solution, efficiency, voltage-regulation, per-unit]
---

# T7-Q10 — Regulation from the Maximum-Efficiency Condition

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q9 - Efficiency and Regulation from Tests]]

> [!question] The maximum efficiency of a 100 kVA single-phase transformer is 98 % and occurs at 80 % of full load at 0.8 pf. The leakage impedance is 5 %. Find the voltage regulation at rated load, 0.8 pf lagging. *[3.75 %]*

**Tests:** [[Transformer Voltage Regulation and Efficiency|maximum-efficiency condition]], per-unit quantities.

## Given
$S=100$ kVA; $\eta_{max}=0.98$ at $x=0.8$, $\cos\phi=0.8$; $|z_e|=0.05$ pu. No voltages are given, so work **per unit** ($V_2=1$, $I_2=1$ at rated load).

## Principle and why it applies
At maximum efficiency, copper loss equals core loss, **at that load**. That gives the copper loss, hence the resistance, in pu; the impedance magnitude then gives the reactance.

## Solution
1. Output at maximum efficiency: $P_o=0.8\times100\ \text{kVA}\times0.8=64$ kW.
2. $\eta=\dfrac{P_o}{P_o+2P_c}=0.98\ \Rightarrow\ 2P_c=64\Big(\dfrac1{0.98}-1\Big)=1.3061$ kW, so $P_c=P_{cu}(0.8)=653.1$ W.
3. Copper loss at **full** load: $P_{cu,FL}=\dfrac{653.1}{0.8^2}=1020.4$ W, so
$$r_{e}=\frac{1020.4}{100\,000}=0.010204\ \text{pu}\ (1.02\ \%).$$
4. $x_e=\sqrt{z_e^2-r_e^2}=\sqrt{0.05^2-0.010204^2}=0.04895$ pu.
5. Regulation (0.8 lag): $VR=r_e\cos\phi+x_e\sin\phi=0.010204(0.8)+0.04895(0.6)=0.00816+0.02937=0.03753$.

## Result
$$VR=3.75\ \%$$

## Check
At full load the losses are $1020+653=1673$ W on an output of $80$ kW, so $\eta_{FL}=\dfrac{80}{80+1.673}=97.95\ \%$, a little below the $98\ \%$ maximum at 80 % load, as it should be.

## Trap / alternative
Lecture 39 solves this same problem but takes the **whole** 5 % as reactance ($x_e=0.05$), getting $VR=0.0102(0.8)+0.05(0.6)=3.82\ \%$. The impedance is the vector sum of $r_e$ and $x_e$, so the reactance is $0.04895$, not $0.05$, and the sheet's $3.75\ \%$ is the right answer. The error is small only because $r_e\ll x_e$.

## Concepts used
- [[10 Single Phase Transformers]] · [[Transformer Voltage Regulation and Efficiency]]
