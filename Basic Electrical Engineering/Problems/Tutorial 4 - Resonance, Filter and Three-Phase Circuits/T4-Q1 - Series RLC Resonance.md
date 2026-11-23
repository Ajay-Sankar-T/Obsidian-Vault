---
tags: [EE1100, tutorial-solution, resonance, RLC-circuit, quality-factor]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q1 - Series RLC Resonance"]
---

# T4-Q1: Series RLC Resonance

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Next: [[T4-Q2 - Parallel RLC Resonance]]

> [!question] A series RLC circuit has $R=10\ \Omega$, $L=0.01$ H, $C=100\ \mu$F. (a) Resonant frequency in rad/s. (b) Quality factor. (c) Bandwidth. (d) Lower and upper half-power frequencies. (e) If $e(t)=1\sin1000t$ is applied, the maximum voltage across the capacitor. *[Sheet: 1000 rad/s; 1; 1000 rad/s; 618.03 and 1618.03 rad/s; 1 V]*

**Tests:** [[Theory - Resonance and Passive Filters#2. Series RLC resonance (voltage source)|series resonance]], $Q$, exact half-power points at low $Q$.

## Given
$R=10\ \Omega$, $L=10$ mH, $C=100\ \mu$F; source amplitude $1$ V at $\omega=1000$ rad/s.

## Principle and why it applies
In a series RLC the current is largest when $X_L=X_C$ (the reactances cancel and $Z=R$). The response curve is characterised by $\omega_0$, the quality factor $Q$ (how sharply it peaks) and the half-power frequencies where $|X|=R$ (current down to $1/\sqrt2$).

## Diagram
![[T4-Q1-Q2-Q3-resonance.png]]

## Solution
**(a)** $\omega_0=\dfrac1{\sqrt{LC}}=\dfrac1{\sqrt{0.01\times100\times10^{-6}}}=\dfrac1{\sqrt{10^{-6}}}=\mathbf{1000\ rad/s}$ ($f_0=159$ Hz).

**(b)** $Q=\dfrac{\omega_0L}{R}=\dfrac{1000\times0.01}{10}=\mathbf{1}$ (equivalently $\tfrac1R\sqrt{L/C}=\tfrac1{10}\sqrt{100}=1$).

**(c)** $BW=\dfrac{\omega_0}{Q}=\dfrac RL=\dfrac{10}{0.01}=\mathbf{1000\ rad/s}$.

**(d)** With $Q=1$ the narrow-band estimate $\omega_0\pm BW/2=500,\,1500$ is poor; use the exact expression
$$\omega_{1,2}=\omega_0\Big[\sqrt{1+\frac1{4Q^2}}\mp\frac1{2Q}\Big]=1000\big[1.1180\mp0.5\big]\ \Rightarrow\ \omega_1=\mathbf{618.03\ rad/s},\quad \omega_2=\mathbf{1618.03\ rad/s}.$$
(They differ by $BW=1000$ ✓ and their product is $\omega_0^2=10^6$ ✓.)

**(e)** At $\omega=\omega_0$: $Z=R=10\ \Omega$, so $I_{max}=\dfrac{1\ \text{V}}{10\ \Omega}=0.1$ A and
$$V_{C,max}=I_{max}\,X_C=0.1\times\frac1{1000\times10^{-4}}=0.1\times10=\mathbf{1\ V}\quad(=Q\times1\ \text{V}).$$

## Result
$$\boxed{\omega_0=1000\ \text{rad/s},\ Q=1,\ BW=1000\ \text{rad/s},\ \omega_1=618.03,\ \omega_2=1618.03\ \text{rad/s},\ V_{C,max}=1\ \text{V}}$$

## Check
Half-power check at $\omega_1=618.03$: $X_L=6.18\ \Omega$, $X_C=16.18\ \Omega$, $|X|=10\ \Omega=R$ ✓ (so $|Z|=14.14=\sqrt2R$ and $I=1/\sqrt2$ of the peak). At $\omega_2=1618.03$: $X_L=16.18$, $X_C=6.18$, $|X|=10$ ✓.

## Trap / alternative
At $Q=1$ the capacitor voltage equals the source voltage, so there is no magnification: "$V_C=Q\times V$" gives $1$ V here. For high $Q$ the capacitor voltage is large, as in [[T4-Q3 - Series RLC from Q and Bandwidth]]. And remember $\omega_{1,2}$ are not symmetric about $\omega_0$ on a linear axis.

## Concepts used
- Series RLC resonance, quality factor, bandwidth ([[Theory - Resonance and Passive Filters]], [[Frequency Response and Resonance Curves]], [[08 Resonance and Magnetically Coupled Circuits]])
