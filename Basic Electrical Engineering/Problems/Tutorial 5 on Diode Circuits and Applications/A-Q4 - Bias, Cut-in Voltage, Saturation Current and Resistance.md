---
tags: [EE1100, diodes, tutorial-solution]
---

# A-Q4 — Forward/Reverse Bias, Cut-in Voltage, Saturation Current, Resistances

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q3 - V-I Characteristics of a p-n Diode]] · Next: [[A-Q5 - Applications of Diodes]]

> [!question] Explain: (i) forward bias, (ii) reverse bias, (iii) cut-in voltage, (iv) reverse saturation current, (v) forward-bias and reverse-bias resistance.

## 1. Definitions

| Term | Meaning |
|---|---|
| **Forward bias** | p side (anode) connected to the positive terminal, n side (cathode) to the negative. The barrier is lowered, the depletion region narrows, and a large current flows (limited by the external circuit). |
| **Reverse bias** | anode connected to the negative terminal. The barrier is raised, the depletion region widens, and only a very small current $\approx I_s$ flows. |
| **Cut-in (threshold, knee) voltage $V_\gamma$** | the forward voltage below which the current is negligible and above which it rises rapidly. Si ≈ 0.6–0.7 V, Ge ≈ 0.2–0.3 V, GaAs LED ≈ 1.2–2 V. It follows from $V_\gamma\approx\eta V_T\ln(I/I_s)$ for a "useful" current $I$. |
| **Reverse saturation current $I_s$** | the small, nearly voltage-independent reverse current due to thermally generated minority carriers. Strongly temperature dependent (doubles per ≈ 10 °C). |
| **Forward (dynamic) resistance $r_f$** | $r_f=\dfrac{dv_D}{di_D}=\dfrac{\eta V_T}{I_D}$ ($\approx26/I_D[\text{mA}]\ \Omega$ at 300 K): small, a few ohms at tens of mA. |
| **Reverse resistance $R_r$** | $R_r=\dfrac{|V_R|}{I_s}$ (static) — very large (MΩ–TΩ). |

The ideal diode is the limit $r_f\to0$, $R_r\to\infty$, $V_\gamma\to0$.

## 2. Illustration

![[A4-diode-terms.png]]

Example with $I_s=1$ pA, $\eta=1$:

| Quantity | Value |
|---|---|
| current at $v_D=0.60$ V | $I_se^{0.60/0.02586}=11.9$ mA |
| forward resistance there, $r_f=\eta V_T/I$ | **2.17 Ω** |
| reverse resistance at $-5$ V, $R_r=5/I_s$ | $5\times10^{12}\ \Omega$ |
| forward-to-reverse resistance ratio | $\sim10^{12}$ |

> [!tip] Static vs dynamic resistance
> Static: $R=V/I$ (slope of the line from the origin). Dynamic: $r=dV/dI$ (slope of the tangent). For a diode in the forward region the dynamic resistance is far smaller than the static value $V/I$.
