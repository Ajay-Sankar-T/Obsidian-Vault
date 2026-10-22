---
tags: [EE1100, diodes, tutorial-solution, logic]
---

# B-Q2 — Diode OR Gate

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q1 - Two-Diode Circuit with 0.7 V Drop]] · Next: [[B-Q3 - Series Battery Rectifier]] · Related: [[B-Q4 - Diode AND Gate]]

> [!question] Fig. 2: three diodes with anodes at $E_1,E_2,E_3$ and cathodes joined at $V_0$ with $R_L=1$ kΩ to ground. Practical diodes (0.7 V). Find $V_0$ for $E_1=E_2=10$ V, $E_3=0$ V; and for $E_1=E_2=0$, $E_3=10$ V.

![[B2-circuit.png]]

## 1. Theory

The anodes are the inputs and the cathodes are tied together to a load to ground. The diode with the **highest** anode voltage turns on first and pulls the common node up to $E_{max}-V_\gamma$; every other diode then has its cathode above its anode (reverse biased) and is OFF.

$$V_0=\max(E_1,E_2,E_3)-0.7\quad(\text{if }\max>0.7\ \text{V}),\qquad V_0=0\ \text{otherwise}.$$

This is the **OR** function in positive logic (1 = high ≈ 10 V, 0 = low ≈ 0 V), with a 0.7 V loss.

## 2. Solution

**Case 1:** $E_1=E_2=10$ V, $E_3=0$.
$D_1$ and $D_2$ conduct (equal inputs, they share the current); $D_3$ has its anode at 0 V and its cathode at $V_0=9.3$ V so it is reverse biased (OFF).
$$V_0=10-0.7=\boxed{9.3\ \text{V}},\qquad I_{R_L}=\frac{9.3}{1\text{ k}}=9.3\ \text{mA}\ (\text{4.65 mA through each of }D_1,D_2)$$

**Case 2:** $E_1=E_2=0$, $E_3=10$ V. Now only $D_3$ conducts; $D_1,D_2$ (anodes at 0 V, cathodes at 9.3 V) are OFF.
$$V_0=10-0.7=\boxed{9.3\ \text{V}},\qquad I_{D3}=9.3\ \text{mA}$$

The output is the same, because the output depends only on the **largest** input.

## 3. Truth table (positive logic, 10 V = 1)

| $E_1$ | $E_2$ | $E_3$ | $V_0$ | logic |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 V | 0 |
| any one or more 10 V | | | 9.3 V | 1 |

OR gate. (The logic-high level is degraded by 0.7 V, and the low level is exact 0 V.)
