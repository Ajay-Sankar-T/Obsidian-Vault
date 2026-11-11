---
tags: [EE1100, op-amp, tutorial-solution, summing-amplifier]
---

# T6-Q4 — Inverting Summing Amplifier

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q3 - Non-inverting Amplifier]] · Next: [[T6-Q5 - Difference Amplifier]]

> [!question] Fig. 4: three inputs 0.3 V, 0.5 V, 0.8 V through 15 kΩ, 25 kΩ, 32 kΩ into the inverting node; feedback 60 kΩ. Find $V_o$. *[$-3.9$ V]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|inverting summer]], KCL at a virtual ground.

## Given
$V_1=0.3$ V, $R_1=15$ kΩ; $V_2=0.5$ V, $R_2=25$ kΩ; $V_3=0.8$ V, $R_3=32$ kΩ; $R_f=60$ kΩ; $+$ input grounded.

## Principle and why it applies
The inverting node is a **virtual ground**, so each input resistor carries $V_k/R_k$ independently of the others; these currents add in the node and all flow through $R_f$.

## Solution
$$\frac{V_1}{R_1}+\frac{V_2}{R_2}+\frac{V_3}{R_3}+\frac{V_o}{R_f}=0\ \Rightarrow\ V_o=-R_f\Big(\frac{V_1}{R_1}+\frac{V_2}{R_2}+\frac{V_3}{R_3}\Big)$$
Per-input gains: $\frac{60}{15}=4$, $\frac{60}{25}=2.4$, $\frac{60}{32}=1.875$.
$$V_o=-(4\cdot0.3+2.4\cdot0.5+1.875\cdot0.8)=-(1.2+1.2+1.5)=-3.9\ \text{V}$$

![[T6-Q4-Q5-circuits.png]]

## Result
$$V_o=-3.9\ \text{V}$$

## Check
Currents: $20\ \mu\text{A}+20\ \mu\text{A}+25\ \mu\text{A}=65\ \mu\text{A}$; $65\ \mu\text{A}\times60\ \text{k}\Omega=3.9$ V ✓.

## Trap / alternative
Adding the three resistors in parallel: unnecessary, and wrong for the gain, since each input sees its **own** $R_k$ to the virtual ground (no interaction between sources).

## Concepts used
- [[Theory - Operational Amplifiers]]
