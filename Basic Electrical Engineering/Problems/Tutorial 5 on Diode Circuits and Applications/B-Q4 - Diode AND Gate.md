---
tags: [EE1100, diodes, tutorial-solution, logic]
---

# B-Q4 — Diode AND Gate

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q3 - Series Battery Rectifier]] · Next: [[B-Q5 - Ideal Diodes with Negative Reference]] · Related: [[B-Q2 - Diode OR Gate]]

> [!question] Fig. 4 (three diodes, $R_L=1$ kΩ to a 10 V supply): find $V_0$ for $E_1=E_2=E_3=0$; for $E_1=10$ V with the other inputs 0; and for the other input combinations. Practical diodes. Which logic element is this?

![[B4-B5-circuits.png]]

## 1. Theory

The diode **cathodes** are the inputs and the anodes are joined at $V_0$, which is pulled up to $+10$ V through $R_L$. The diode with the **lowest** cathode voltage conducts first and holds the common node at $E_{min}+0.7$ V (if that is below 10 V); the other diodes are then reverse biased.

$$V_0=\min\big(E_{min}+0.7,\ 10\ \text{V}\big)$$

## 2. Solution

**All inputs 0 V:** all three diodes conduct, $V_0=0+0.7=\boxed{0.7\ \text{V}}$, the current through $R_L$ is $(10-0.7)/1\text{ k}=9.3$ mA (3.1 mA in each diode).

**$E_1=10$ V, $E_2=E_3=0$:** $D_2$ and $D_3$ conduct and hold $V_0=0.7$ V; $D_1$ has anode 0.7 V and cathode 10 V, so it is OFF. $V_0=\boxed{0.7\ \text{V}}$.

**All inputs 10 V:** the diodes would need the node at 10.7 V, which is above the 10 V supply, so none conducts and no current flows through $R_L$: $V_0=\boxed{10\ \text{V}}$.

## 3. Truth table (circuit simulation of all 8 combinations)

| $E_1$ | $E_2$ | $E_3$ | $V_0$ | logic out |
|---|---|---|---|---|
| 0 | 0 | 0 | 0.7 V | 0 |
| 0 | 0 | 10 | 0.7 V | 0 |
| 0 | 10 | 0 | 0.7 V | 0 |
| 0 | 10 | 10 | 0.7 V | 0 |
| 10 | 0 | 0 | 0.7 V | 0 |
| 10 | 0 | 10 | 0.7 V | 0 |
| 10 | 10 | 0 | 0.7 V | 0 |
| 10 | 10 | 10 | **10 V** | **1** |

The output is high **only when all inputs are high**:

> [!success] The circuit realises a three-input **AND gate** (positive logic, "0" ≈ 0.7 V, "1" = 10 V).
