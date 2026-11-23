---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RLC, parallel-RLC, step-response]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q12: Parallel RLC Driven by a Current Step

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q11 - Second-Order Equation with Initial Conditions]] · Next tutorial: [[Tutorial 3 - AC Circuit Analysis]]

> [!question] A parallel RLC circuit ($R=5\ \Omega$, $L=0.1$ mH, $C=8\ \mu$F) driven by a 10 A DC source (the sheet calls it "three-phase", but it is a single parallel circuit). (a) Determine the voltage $v$ across the capacitor. (b) Compute the currents through $R$, $L$ and $C$. *[Sheet: $v=37.74e^{-12500t}\sin(33119.1t)$ V]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#4. Second-order circuits (L and C together)|parallel RLC step response]], the dual of the series circuit.

## Given
$I=10$ A switched on at $t=0$; zero initial energy ($v(0)=0$, $i_L(0)=0$). $R=5\ \Omega$, $L=0.1$ mH, $C=8\ \mu$F in parallel.

## Principle and why it applies
KCL at the top node: $\;C\dfrac{dv}{dt}+\dfrac vR+\dfrac1L\displaystyle\int v\,dt=I$. This is the **dual** of the series RLC (voltage $\leftrightarrow$ current, $L\leftrightarrow C$, $R\leftrightarrow1/R$), so $\alpha=\dfrac1{2RC}$ and the roots follow the same pattern. At $t=0^+$ the inductor current is $0$ and the capacitor voltage is $0$ (so $i_R=0$): the **whole 10 A flows into the capacitor**, $C\,\dfrac{dv}{dt}(0^+)=10$.

## Solution
$$\alpha=\frac1{2RC}=\frac1{2\times5\times8\times10^{-6}}=12\,500\ \text{s}^{-1},\qquad \omega_0=\frac1{\sqrt{LC}}=\frac1{\sqrt{8\times10^{-10}}}=35\,355\ \text{rad/s},$$
$$\zeta=\frac\alpha{\omega_0}=0.354<1\ \Rightarrow\ \text{underdamped},\qquad \omega_d=\sqrt{\omega_0^2-\alpha^2}=33\,072\ \text{rad/s}.$$
With $v=e^{-\alpha t}(A\cos\omega_dt+B\sin\omega_dt)$ and $v(0)=0\Rightarrow A=0$; $\dfrac{dv}{dt}(0)=\dfrac IC\Rightarrow B\omega_d=\dfrac{10}{8\times10^{-6}}$:
$$\boxed{v(t)=\frac{I}{C\omega_d}e^{-\alpha t}\sin\omega_dt=37.80\,e^{-12500t}\sin(33072\,t)\ \text{V}}$$

**Branch currents.**
$$i_R=\frac vR=7.56\,e^{-12500t}\sin(33072t)\ \text{A},$$
$$i_L=I\Big[1-\frac{1}{\sqrt{1-\zeta^2}}e^{-\alpha t}\sin(\omega_dt+\theta)\Big]=10\big[1-1.069\,e^{-12500t}\sin(33072t+69.3^\circ)\big]\ \text{A},\quad\theta=\arccos\zeta=69.3^\circ,$$
$$i_C=-\frac{I}{\sqrt{1-\zeta^2}}e^{-\alpha t}\sin(\omega_dt-\theta)=-10.69\,e^{-12500t}\sin(33072t-69.3^\circ)\ \text{A}.$$

## Result
$$\boxed{v(t)=37.80\,e^{-12500t}\sin(33072t)\ \text{V};\quad i_L\to10\ \text{A};\quad i_R+i_L+i_C=10\ \text{A}}$$

![[T2-Q12-response.png]]

**Figure:** the current from the source is shared; at $0^+$ it all goes into $C$, then the inductor current builds up to 10 A (it overshoots slightly because the response rings), while $i_C$ and $i_R$ die away.

## Check
At $t=0$: $i_L=10[1-1.069\sin69.3^\circ]=0$ ✓, $i_C=-10.69\sin(-69.3^\circ)=10$ A ✓, $i_R=0$ ✓ (sum 10 A). KCL holds for all $t$ (the dashed sum in the figure is flat at 10 A). Final: $v\to0$ (the inductor is a DC short).

## Trap / alternative
- Using the **series** formula $\alpha=R/2L$ for a parallel circuit (here that gives $25\,000\ \text{s}^{-1}$ instead of $12\,500\ \text{s}^{-1}$); in a parallel circuit a *smaller* $R$ means *more* damping.
- The sheet's numbers ($\omega_d=33119.1$, amplitude 37.74, phase $69.51^\circ$) use $\zeta$ rounded to $0.35$; the exact values are $33072$, $37.80$ and $69.30^\circ$ (the difference is 0.14 %).
- The amplitude is $I/(C\omega_d)$, not $I/C$.

## Concepts used
- Parallel RLC natural/step response, KCL, duality with the series circuit ([[Theory - Transients in RL, RC and RLC Circuits]], [[Parallel RLC Natural Response - Damping Cases]], [[Series vs Parallel RLC - Key Distinctions]])
