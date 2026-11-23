---
tags: [EE1100, tutorial-solution, resonance, RLC-circuit, parallel-RLC, quality-factor]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q2 - Parallel RLC Resonance"]
---

# T4-Q2: Parallel RLC Resonance

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q1 - Series RLC Resonance]] · Next: [[T4-Q3 - Series RLC from Q and Bandwidth]]

> [!question] A current source drives $R=10\ \Omega$, $L=1$ H, $C=1\ \mu$F in parallel. (a) Resonant frequency. (b) Quality factor. (c) Bandwidth. (d) Lower and upper half-power frequencies. (e) For $i(t)=1\sin1000t$ the maximum voltage across the capacitor. (f) The capacitor current. *[Sheet: 1000 rad/s; 0.01; $10^5$ rad/s; 10 and 100010 rad/s; 10 V; $0.00707\angle90^\circ$ A]*

**Tests:** [[Theory - Resonance and Passive Filters#3. Parallel RLC resonance (current source)|parallel resonance]], low-$Q$ behaviour, the dual of Q1.

## Given
$R=10\ \Omega$, $L=1$ H, $C=1\ \mu$F; source current amplitude $1$ A at $\omega=1000$ rad/s.

## Principle and why it applies
Parallel resonance is the **dual** of series resonance: $Y=\frac1R+j(\omega C-\frac1{\omega L})$ is smallest in magnitude when the susceptances cancel, so the voltage across the whole parallel block, $V=I/|Y|$, is **largest** at $\omega_0$ and equals $IR$.

## Diagram
![[T4-Q1-Q2-Q3-resonance.png]]

## Solution
**(a)** $\omega_0=\dfrac1{\sqrt{LC}}=\dfrac1{\sqrt{10^{-6}}}=\mathbf{1000\ rad/s}$.

**(b)** $Q=\dfrac{R}{\omega_0L}=\dfrac{10}{1000\times1}=\mathbf{0.01}$ (also $R\sqrt{C/L}=10\times10^{-3}$): a very **low** $Q$; the $10\ \Omega$ resistor loads the tank heavily.

**(c)** $BW=\dfrac{\omega_0}{Q}=\dfrac1{RC}=\dfrac{1}{10\times10^{-6}}=\mathbf{10^5\ rad/s}$.

**(d)** Exact: $\omega_{1,2}=\omega_0\Big[\sqrt{1+\tfrac1{4Q^2}}\mp\tfrac1{2Q}\Big]=1000\big[\sqrt{2501}\mp50\big]=1000\,[50.01\mp50]$:
$$\omega_1=\mathbf{10\ rad/s},\qquad \omega_2=\mathbf{100\,010\ rad/s}.$$
(The "bandwidth" runs from almost zero to $10^5$: the response is a broad plateau because $Q\ll1$, see the figure.)

**(e)** At resonance $Y=1/R$, so the voltage amplitude is $V_{max}=I_mR=1\times10=\mathbf{10\ V}$.

**(f)** The capacitor sees $V=10$ V at $\omega=1000$: $X_C=\dfrac1{\omega C}=1000\ \Omega$, so
$$I_{C,max}=\frac{V_{max}}{X_C}=\frac{10}{1000}=0.01\ \text{A peak}=\mathbf{0.00707\ A\ rms},\ \ \text{leading }V\text{ by }90^\circ.$$
(The sheet's $0.00707\angle90^\circ$ A is the **rms** value.) The inductor carries the same $0.01$ A peak at $-90^\circ$; they cancel and the resistor carries all $1$ A.

## Result
$$\boxed{\omega_0=1000,\ Q=0.01,\ BW=10^5\ \text{rad/s},\ \omega_{1,2}=10,\ 100\,010\ \text{rad/s},\ V_{max}=10\ \text{V},\ I_C=0.01\ \text{A peak}\ (0.00707\ \text{A rms})}$$

## Check
$I_C=Q\,I_{source}=0.01\times1$ A ✓ (circulating current is $Q$ times the source). Because $Q<1$ there is **no** current magnification; the tank resonates only in the sense that the net reactive current vanishes.

## Trap / alternative
Using the series formulas ($Q=\omega_0L/R=100$, $BW=R/L=10$) would be exactly backwards; for a parallel circuit a *smaller* $R$ gives a *smaller* $Q$. Also state whether a current is peak or rms: $0.01$ A peak is $0.00707$ A rms.

## Concepts used
- Parallel RLC resonance, duality with the series circuit ([[Theory - Resonance and Passive Filters]], [[Series vs Parallel RLC - Key Distinctions]])
