---
tags: [EE1100, diodes, tutorial-solution]
---

# B-Q7 — Asymmetric Diode–Resistor Network

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q6 - Diode Clamper]] · Next: [[B-Q8 - Half-Wave Rectifier with Series Resistor]]

> [!question] Fig. 7: $D_1$, $D_2$ ideal, $R_1=R_2=100\ \Omega$, $V_S$ a square wave of period 1 ms. Find the load current $i_L$.

![[B7-circuit-waveform.png]]

## 1. Theory

Between the source and $R_2$ there are two parallel branches:
- **Branch A:** $D_2$ alone, conducting from the source side to the load side (arrow points towards $R_2$).
- **Branch B:** $R_1$ in series with $D_1$, with $D_1$ pointing the **opposite** way (from the load side towards the source).

So the first branch passes positive source voltages with no series resistance and the second passes negative source voltages through an extra resistor.

## 2. Solution

**Positive half-cycle ($V_S>0$):** $D_2$ is forward biased (ON); $D_1$ is reverse biased (OFF), so branch B is open.
$$i_L=\frac{V_S}{R_2}=\frac{V_S}{100}=\boxed{0.01\,V_S}$$

**Negative half-cycle ($V_S<0$):** $D_2$ is OFF. $D_1$ conducts (its anode is on the load side, which is at the higher potential), and the current passes through $R_1$ and $R_2$ in series:
$$|i_L|=\frac{|V_S|}{R_1+R_2}=\frac{|V_S|}{200}=\boxed{0.005\,|V_S|}$$
flowing opposite to the reference direction of $i_L$ (upwards through $R_2$).

| Half-cycle | Conducting path | $i_L$ (reference: downwards through $R_2$) |
|---|---|---|
| positive | $D_2$ | $+V_S/100$ |
| negative | $D_1+R_1$ | $V_S/200$, a negative number (magnitude $0.005\lvert V_S\rvert$) |

> [!warning] Sign convention on the sheet
> The printed answer, "$i_L=-0.005V_S$" for the negative half-cycle, is in terms of the magnitude of $V_S$ in that half-cycle (so that $i_L<0$). With $V_S$ treated as a signed quantity, $i_L=+V_S/200$ (negative). Both describe a current of magnitude $0.005|V_S|$ flowing upwards.

**Example (amplitude ±10 V):** $i_L=+100$ mA in the positive half-cycle, $-50$ mA in the negative half-cycle (average $+25$ mA). A circuit simulation gives $+99.999$ mA with ($D_2$ ON, $D_1$ OFF) and $-49.99975$ mA with ($D_2$ OFF, $D_1$ ON).
