---
tags: [EE1100, tutorial-solution, resonance, RLC-circuit, quality-factor, design]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q3 - Series RLC Parameters"]
---

# T4-Q3: Finding a Series RLC from $Q$, Bandwidth and $R$

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q2 - Parallel RLC Resonance]] · Next: [[T4-Q4 - RC Low-Pass Filter Design]]

> [!question] A voltage $e(t)=10\sin\omega t$ drives a series RLC circuit. At resonance the maximum capacitor voltage is $500$ V, the bandwidth is $400$ rad/s and the impedance at resonance is $100\ \Omega$. Find (a) $\omega_0$, (b) the band limits, (c) $L$ and $C$. *[Sheet: 20000 rad/s; 19800 and 20200 rad/s; $0.25$ H, $0.01\ \mu$F]*

**Tests:** inverse use of the resonance relations, voltage magnification $V_C=QV$.

## Given
Source amplitude $V_m=10$ V; $V_{C,max}=500$ V at resonance; $BW=400$ rad/s; $|Z|_{res}=R=100\ \Omega$.

## Principle and why it applies
At series resonance $Z=R$ and the capacitor voltage is $Q$ times the source voltage, $V_C=QV$. So the *ratio* of the two voltages gives $Q$ directly, and $BW=\omega_0/Q$ then fixes $\omega_0$; $R$ and $BW$ fix $L$ (since $BW=R/L$); $\omega_0$ fixes $C$.

## Diagram
![[T4-Q1-Q2-Q3-resonance.png]]

## Solution
**(a)** $Q=\dfrac{V_C}{V}=\dfrac{500}{10}=50$. Then $\omega_0=Q\cdot BW=50\times400=\mathbf{20\,000\ rad/s}$ (3.18 kHz).

**(b)** $Q=50$ is high, so the band is nearly symmetric: $\omega_{1,2}=\omega_0\mp\dfrac{BW}2=20\,000\mp200$:
$$\omega_1=\mathbf{19\,800\ rad/s},\qquad\omega_2=\mathbf{20\,200\ rad/s}$$
(exact: $19\,799.0$ and $20\,199.0$; the corrections are $\pm0.005\ \%$).

**(c)** $BW=\dfrac RL\Rightarrow L=\dfrac{R}{BW}=\dfrac{100}{400}=\mathbf{0.25\ H}$. From $\omega_0^2=\dfrac1{LC}$:
$$C=\frac1{\omega_0^2L}=\frac1{(2\times10^4)^2\times0.25}=\frac1{10^8}=\mathbf{0.01\ \mu F}.$$

## Result
$$\boxed{\omega_0=20\,000\ \text{rad/s},\quad\omega_{1,2}=19\,800,\ 20\,200\ \text{rad/s},\quad L=0.25\ \text{H},\quad C=0.01\ \mu\text{F}}$$

## Check
$Q=\dfrac{\omega_0L}{R}=\dfrac{20\,000\times0.25}{100}=50$ ✓. Current at resonance $I=10/100=0.1$ A; $V_C=I/(\omega_0C)=0.1/(20\,000\times10^{-8})=500$ V ✓ and $V_L=I\omega_0L=500$ V too (equal and opposite).

## Trap / alternative
The 500 V inside a 10 V circuit is not a mistake; it is the *point* of high $Q$ (and a safety/rating issue). Both the source and capacitor voltages must be quoted as the same kind (peak here). Using $BW=\omega_0/Q$ with $f_0$ instead of $\omega_0$ gives $BW$ in Hz; keep the units consistent.

## Concepts used
- Series resonance relations, voltage magnification ([[Theory - Resonance and Passive Filters]], [[Frequency Response and Resonance Curves]])
