---
tags: [EE1100, tutorial-theory, AC-circuits, resonance, filters]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
---

# Theory: Resonance and Passive Filters

← up: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits|Tutorial 4]] · lectures: [[Lecture 20 Resonance, Frequency Response and Filters.pdf]], [[Lecture 21 Design of Passive Filters.pdf]], [[Lecture 22 Design of Passive Filters (Contd…).pdf]] · week: [[08 Resonance and Magnetically Coupled Circuits]] · fuller treatments: [[Frequency Response and Resonance Curves]], [[Filter Theory]], [[Series vs Parallel RLC - Key Distinctions]]

> [!abstract] The idea in one paragraph
> A circuit's response to a sinusoid depends on frequency because $X_L=\omega L$ grows and $X_C=1/\omega C$ shrinks with $\omega$. **Resonance** is the frequency at which the inductive and capacitive reactances cancel; the circuit then looks purely resistive, the response peaks, and the $L$ and $C$ voltages (or currents) are magnified by the quality factor $Q$. A **filter** is a circuit whose gain $|H(j\omega)|$ passes some frequencies and attenuates others; the same $RLC$ building blocks make low-pass, high-pass, band-pass and band-reject filters.

## 1. Frequency response and the −3 dB point

The **transfer function** $H(j\omega)=\bar V_{out}/\bar V_{in}$ is a complex number at each $\omega$; its magnitude is the gain and its angle the phase shift. Gain in decibels: $\;|H|_{dB}=20\log_{10}|H|$.

| Gain | $|H|$ | dB |
|---|---|---|
| unity | 1 | 0 |
| half power | $1/\sqrt2=0.707$ | $-3.01$ |
| one tenth | 0.1 | $-20$ |
| one hundredth | 0.01 | $-40$ |

The **half-power (cut-off) frequencies** are where $|H|=|H|_{max}/\sqrt2$, i.e. the power has fallen to half. The **bandwidth** is the width of the band between them (band-pass) or the band above/below one of them (low/high-pass).

## 2. Series RLC resonance (voltage source)

$$Z(j\omega)=R+j\Big(\omega L-\frac1{\omega C}\Big),\qquad \omega_0=\frac1{\sqrt{LC}}\ \ \Big(f_0=\frac{1}{2\pi\sqrt{LC}}\Big).$$

At $\omega_0$: $X_L=X_C$, $Z=R$ (minimum), the current is **maximum**, $I_0=V/R$, and in phase with $V$. Each reactive element carries a voltage $Q$ times the source:
$$V_L=V_C=I_0\,\omega_0L=Q\,V,\qquad Q=\frac{\omega_0L}{R}=\frac1{\omega_0RC}=\frac1R\sqrt{\frac LC}.$$
*Meaning of $Q$:* energy stored over energy lost per radian; also the voltage magnification. The **half-power frequencies** satisfy $|X|=R$:
$$\omega_{1,2}=\omega_0\Big[\sqrt{1+\frac1{4Q^2}}\mp\frac1{2Q}\Big],\qquad BW=\omega_2-\omega_1=\frac{\omega_0}{Q}=\frac RL,\qquad \omega_1\omega_2=\omega_0^2.$$
For $Q\gtrsim5$ the **narrow-band approximation** $\omega_{1,2}\approx\omega_0\mp BW/2$ is good; for small $Q$ (Tutorial 4 Q1, $Q=1$) it is poor, use the exact form. The response curve is **not symmetric** on a linear axis (it is symmetric on a log axis, since $\omega_1\omega_2=\omega_0^2$).

## 3. Parallel RLC resonance (current source)

$$Y(j\omega)=\frac1R+j\Big(\omega C-\frac1{\omega L}\Big),\qquad \omega_0=\frac1{\sqrt{LC}}\ \ (\text{same}),$$
At $\omega_0$: $Y=1/R$ (minimum), so the impedance and the voltage $V=IR$ are **maximum**; the inductor and capacitor currents are equal and opposite, each $Q\,I$, circulating inside the $LC$ loop:
$$Q=\frac{R}{\omega_0L}=\omega_0RC=R\sqrt{\frac CL},\qquad BW=\frac{\omega_0}{Q}=\frac1{RC},\qquad \omega_{1,2}=\omega_0\Big[\sqrt{1+\frac1{4Q^2}}\mp\frac1{2Q}\Big].$$
This is the **dual** of the series circuit: swap $V\leftrightarrow I$, $R\leftrightarrow1/R$, $L\leftrightarrow C$. A **small** parallel resistance means a **low** $Q$ (heavy damping), opposite to the series case where small $R$ means high $Q$.

| | series RLC | parallel RLC |
|---|---|---|
| source | voltage | current |
| at $\omega_0$ | $Z=R$ (min), $I$ max | $Y=1/R$ (min), $V$ max |
| $Q$ | $\omega_0L/R$ | $R/\omega_0L$ |
| $BW$ | $R/L$ | $1/RC$ |
| magnified | $V_L,V_C=QV$ | $I_L,I_C=QI$ |

## 4. The four basic filters

| Filter | Circuit | $H(j\omega)$ | Corner / centre | Passes |
|---|---|---|---|---|
| **low-pass** | series $R$, output across $C$ | $\dfrac1{1+j\omega RC}$ | $\omega_c=\dfrac1{RC}$ | below $\omega_c$ |
| **high-pass** | series $C$, output across $R$ | $\dfrac{j\omega RC}{1+j\omega RC}$ | $\omega_c=\dfrac1{RC}$ | above $\omega_c$ |
| **band-pass** | series $RLC$, output across $R$ | $\dfrac{R}{R+j(\omega L-1/\omega C)}$ | $\omega_0=\dfrac1{\sqrt{LC}}$, $BW=\dfrac RL$ | a band around $\omega_0$ |
| **band-reject (notch)** | parallel $LC$ in the signal path, load $R$ to ground | $\dfrac{R}{R+Z_{LC}}$, $Z_{LC}\to\infty$ at $\omega_0$ | $\omega_0=\dfrac1{\sqrt{LC}}$ | everything except a band around $\omega_0$ |

First-order filters have a gain of $1/\sqrt2$ ($-3$ dB) at $\omega_c$ and roll off at $20$ dB per decade. Design is inverting those formulas: choose one component, compute the other from $f_c=1/(2\pi RC)$ (Q4, Q5), or from $\omega_0^2=1/LC$ (Q7).

## 5. Selectivity: how large must $Q$ be?

For the series band-pass with $x=\omega/\omega_0$,
$$|H|=\frac1{\sqrt{1+Q^2\big(x-1/x\big)^2}}.$$
To attenuate a signal at relative offset $x$ by $A$ dB you need $Q^2(x-1/x)^2\ge10^{A/10}-1$. For $-20$ dB: $Q\,|x-1/x|\ge\sqrt{99}=9.95$ (Q8). A frequency offset that is equal above and below $\omega_0$ is **not** equally easy to reject: $|x-1/x|$ is $0.0396$ at $x=1.02$ but $0.0404$ at $x=0.98$, so the *high* side is the tighter requirement (it needs $Q\ge251.2$ against $246.2$ for the low side) and it sets the design.

## 6. Practical limits
Real inductors have series resistance, real capacitors leakage and parasitics. At RF the required $L$ and $C$ become comparable to stray values (Q8 needs $C=0.063$ pF), and lumped designs give way to distributed elements. High $Q$ means large internal voltages or currents (Q3: 500 V inside a 10 V circuit).

## 7. Common traps
- Using $\omega_0\mp BW/2$ for the band edges at **low** $Q$ (Q1, Q6).
- Using the series formulas ($Q=\omega_0L/R$, $BW=R/L$) for a **parallel** circuit.
- Mixing $\omega$ (rad/s) and $f$ (Hz): $BW$ and $Q$ are defined with the same variable; $\omega_0=2\pi f_0$.
- Forgetting that the peak voltage in a source description is not the rms (Q1(e), Q2(f)).

## 8. Cross-domain links
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] and [[2nd Order ODEs - MOC]]: a driven mass–spring–damper has the same $\omega_0=\sqrt{k/m}$, $Q$ and half-power bandwidth as the series RLC.
- [[First-Order Systems - Time Constant and Response]]: the RC low-pass of §4 is the frequency-domain view of the first-order time constant $\tau=RC$ ($\omega_c=1/\tau$).
