---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RL-circuit, energy]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q4: Source-Free RL Decay, Time Constant and Half-Energy Time

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q3 - DC Steady State with a Current Source]] · Next: [[T2-Q5 - RL Circuit with a Switch Opening]]

> [!question] In an $R$–$L$ loop, $v=120e^{-50t}$ V and $i=30e^{-50t}$ A for $t>0$. (a) Find $L$ and $R$. (b) The time constant. (c) The initial energy in the inductor. (d) The time to dissipate 50 % of the initial energy. *[Sheet: $L=0.08$ H, $R=4\ \Omega$; $\tau=0.02$ s; 36 J; 6.93 ms]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#3. First-order circuits (one storage element)|source-free first-order response]], reading $\tau$ from an exponent, energy decay.

## Given
$v(t)=120e^{-50t}$ V across the loop, $i(t)=30e^{-50t}$ A circulating, $t>0$. The loop is only $R$ and $L$ (no source), so the exponent $50\ \text{s}^{-1}$ is $1/\tau$.

## Principle and why it applies
A source-free RL loop obeys $L\dfrac{di}{dt}+Ri=0$, so $i=I_0e^{-t/\tau}$ with $\tau=L/R$. The terminal voltage $v$ is the voltage across the resistor (and, in magnitude, across the inductor, since the two are connected in a loop). So the **ratio** $v/i$ gives $R$ at every instant, and the exponent gives $\tau$, hence $L$.

## Solution
**(a)** The voltage across $R$ is $Ri$: $\ R=\dfrac vi=\dfrac{120e^{-50t}}{30e^{-50t}}=\mathbf{4\ \Omega}$. The exponent gives $\dfrac1\tau=\dfrac RL=50$, so $L=\dfrac{4}{50}=\mathbf{0.08\ H}$. (Check with the inductor law: $|v|=L\,|di/dt|=L\times50\times30e^{-50t}=1500L\,e^{-50t}$, which equals $120e^{-50t}$ when $L=0.08$ H ✓.)

**(b)** $\tau=\dfrac LR=\dfrac{0.08}{4}=\mathbf{0.02\ s}=20$ ms.

**(c)** $E_0=\tfrac12Li(0)^2=\tfrac12(0.08)(30)^2=\mathbf{36\ J}$.

**(d)** The energy remaining is $\tfrac12Li^2=36\,e^{-100t}$, decaying twice as fast as the current. Setting it to half:
$$e^{-100t}=\tfrac12\ \Rightarrow\ t_{1/2}=\frac{\ln2}{100}=\mathbf{6.93\ ms}\quad(=\tfrac{\tau}{2}\ln2).$$

## Result
$$\boxed{R=4\ \Omega,\ L=0.08\ \text{H};\quad \tau=20\ \text{ms};\quad E_0=36\ \text{J};\quad t_{1/2}=6.93\ \text{ms}}$$

![[T2-Q4-decay-energy.png]]

**Figure:** the current falls to 36.8 % at one time constant (20 ms), but the *energy* has already halved by 6.9 ms, because it goes as $i^2$.

## Check
All the energy ends up in the resistor: $\int_0^\infty i^2R\,dt=4\times900\times\dfrac{1}{100}=36$ J ✓ $=E_0$.

## Trap / alternative
The classic slip is to use the **current's** decay to find the half-energy time: $e^{-50t}=\tfrac12$ gives $13.9$ ms, which is the time for half the *current*. For energy use the exponent $2/\tau$. The time for half the current is $\tau\ln2$; for half the energy $\tfrac{\tau}{2}\ln2$.

## Concepts used
- RL time constant, energy in an inductor ([[Theory - Transients in RL, RC and RLC Circuits]])
