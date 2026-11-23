---
tags: [EE1100, tutorial-solution, AC-circuits, impedance, RLC-circuit, resonance]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q7: Series RLC: Element Voltages Larger Than the Source

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Impedance and Series-Parallel AC Circuits]] · Previous: [[T3-Q6 - Adding Parallel Branch Currents]] · Next: [[T3-Q8 - Complex Power of a Series RLC]]

> [!question] $e(t)=150\sin1000t$ is applied across a series RLC circuit with $R=40\ \Omega$, $L=0.13$ H, $C=10\ \mu$F. (a) The rms steady-state current. (b) Instantaneous voltages across $L$ and $C$. (c) Compare the rms voltages across $L$ and $C$ with the applied voltage and comment. (d) Draw the complete phasor diagram. *[Sheet: $\bar I=2.12\angle-36.86^\circ$ A; $v_C=300\sin(1000t-126.86^\circ)$, $v_L=389.75\sin(1000t+53.14^\circ)$ V; $\bar V=106\angle0^\circ$, $\bar V_L=275.6\angle53.14^\circ$, $\bar V_C=212.13\angle-126.86^\circ$ V]*

**Tests:** [[Impedance and Series-Parallel AC Circuits|series RLC impedance]], voltage magnification (a first look at resonance).

## Given
$\omega=1000$ rad/s, $V_{rms}=150/\sqrt2=106.07$ V. $X_L=\omega L=130\ \Omega$, $X_C=\dfrac1{\omega C}=\dfrac1{1000\times10^{-5}}=100\ \Omega$.

## Principle and why it applies
In a series circuit the **same current** flows through all three elements; each element voltage is $\bar I$ times its impedance. $L$ and $C$ voltages are $180^\circ$ apart (one leads $I$ by $90^\circ$, the other lags by $90^\circ$), so they **partly cancel** in the KVL sum even though each is large. When $X_L$ and $X_C$ are both much bigger than $R$ the cancellation leaves the source small compared with either element voltage: *voltage magnification*, the idea behind resonance.

## Diagram
![[T3-Q4-Q6-Q7-phasors.png]]

## Solution
$$Z=R+j(X_L-X_C)=40+j30=50\angle36.87^\circ\ \Omega.$$
**(a)** $\bar I=\dfrac{106.07\angle0^\circ}{50\angle36.87^\circ}=\mathbf{2.121\angle-36.87^\circ\ A}$ (the current lags: net inductive).

**(b)** $V_L=IX_L=2.121\times130=275.8$ V rms ($390.0$ V peak), at $-36.87^\circ+90^\circ=+53.13^\circ$; $V_C=IX_C=212.1$ V rms ($300$ V peak), at $-36.87^\circ-90^\circ=-126.87^\circ$:
$$\mathbf{v_L=390\sin(1000t+53.13^\circ)\ V},\qquad \mathbf{v_C=300\sin(1000t-126.87^\circ)\ V}.$$
(The sheet's $389.75$ V uses $I$ rounded to $2.12$ A; exact $390.0$ V.) Also $V_R=IR=84.85$ V at $-36.87^\circ$.

**(c)** $V_L=275.8$ V and $V_C=212.1$ V are **2.6 and 2.0 times the 106 V source**. This does not violate KVL because the phasors add vectorially: $\bar V_L+\bar V_C=(X_L-X_C)\,\bar I\angle90^\circ=63.6\angle53.13^\circ$ V only, and $\bar V_R+\bar V_L+\bar V_C=\bar V$.

**(d)** Phasor diagram (reference $\bar V$ at $0^\circ$): $\bar I$ at $-36.87^\circ$; $\bar V_R$ along $\bar I$; $\bar V_L$ $90^\circ$ ahead of $\bar I$; $\bar V_C$ $90^\circ$ behind it; they close to $\bar V$.

## Result
$$\boxed{\bar I=2.12\angle-36.87^\circ\ \text{A};\ \ v_L=390\sin(1000t+53.13^\circ),\ v_C=300\sin(1000t-126.87^\circ)\ \text{V};\ \ V_L,V_C>V}$$

## Check
KVL in rectangular form: $\bar V_R=67.9-j50.9$, $\bar V_L=165.5+j220.6$, $\bar V_C=-127.3-j169.7$ V; sum $=106.1+j0$ ✓. The resonant frequency is $\omega_0=1/\sqrt{LC}=877$ rad/s, so $\omega=1000$ is above resonance (inductive), consistent with the lagging current; the quality factor $Q=\omega_0L/R=2.85$, so the voltage magnification at resonance would be $2.85\times$.

## Trap / alternative
Expect element voltages **larger than the source** in any series circuit with $X\gg R$; it is the headline of [[Frequency Response and Resonance Curves|resonance]] and the reason capacitors in resonant circuits need voltage ratings far above the supply. Also keep $X_C=1/(\omega C)$ with $C$ in farads ($10\ \mu\text{F}=10^{-5}$ F).

## Concepts used
- Series impedance, phasor diagram, voltage magnification ([[Impedance and Series-Parallel AC Circuits]], [[Frequency Response and Resonance Curves]])
