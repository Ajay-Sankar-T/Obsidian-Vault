---
tags: [EE1100, diodes, tutorial-solution]
---

# B-Q1 — Two-Diode Circuit with 0.7 V Drop

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q9 - Full-Wave Rectifier Filter Capacitor]] · Next: [[B-Q2 - Diode OR Gate]] · Method: [[Theory - Diode Models and Circuit Analysis]]

> [!question] In Fig. 1 (20 V battery, $D_1$, $D_2$, $R_1=3.3$ kΩ, $R_2=5.6$ kΩ) assume practical diodes (turn-on voltage 0.7 V). Determine $I_1$, $I_2$ and $I_{D2}$.

![[B1-circuit.png]]

## 1. Theory

Constant-drop model: an ON diode is a 0.7 V battery (anode higher), an OFF diode is open. Use the "assume, then check" method.

**Circuit reading:** battery $+$ → $D_1$ → node X. From X, $R_1$ (3.3 kΩ) and $D_2$ are in **parallel** down to node Y; Y returns through $R_2$ (5.6 kΩ) to the battery negative (ground). So $I_2=I_1+I_{D2}$.

## 2. Solution

**Assume** $D_1$ and $D_2$ both ON.

$$V_X=20-0.7=19.3\ \text{V},\qquad V_Y=V_X-0.7=18.6\ \text{V}$$

$$I_1=\frac{V_X-V_Y}{R_1}=\frac{0.7}{3.3\text{ k}}=0.2121\ \text{mA}$$

$$I_2=\frac{V_Y}{R_2}=\frac{18.6}{5.6\text{ k}}=3.3214\ \text{mA}$$

$$I_{D2}=I_2-I_1=3.3214-0.2121=3.1093\ \text{mA}$$

**Check:** $I_{D1}=I_2=3.32$ mA $>0$ and $I_{D2}=3.11$ mA $>0$, so both diodes are indeed ON (consistent).

$$\boxed{I_1=0.212\ \text{mA},\quad I_2=3.321\ \text{mA},\quad I_{D2}=3.109\ \text{mA}}$$

(matches the sheet). A brute-force simulation over all four ON/OFF combinations finds only this one consistent state.

> [!note] Why the shortcut works
> $D_2$ clamps the voltage across $R_1$ to 0.7 V (it is in parallel with $R_1$), so $I_1$ is fixed by $0.7/R_1$; $R_2$ then carries the full current, and $D_2$ takes whatever is left.
