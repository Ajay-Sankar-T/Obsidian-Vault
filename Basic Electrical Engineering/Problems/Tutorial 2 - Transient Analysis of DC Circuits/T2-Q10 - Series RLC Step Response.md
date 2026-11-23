---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RLC, step-response, damping]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q10: Series RLC Step Response and Damping Ranges

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q9 - Switch Closes in an RC Network]] · Next: [[T2-Q11 - Second-Order Equation with Initial Conditions]]

> [!question] A series RLC circuit with a 100 V DC source, $R=50\ \Omega$, $L=0.1$ H, $C=50\ \mu$F. Determine the critical resistance $R_c$, damping factor $\zeta$, natural frequency $\omega_n$, damped frequency $\omega_d$. If the switch closes at $t=0$ with zero initial conditions, find $i$, $v_R$, $v_L$, $v_C$. Classify the response and give the range of $R$ for overdamped, critically damped, underdamped and undamped behaviour. *[Sheet: $R_c=89.44\ \Omega$, $\zeta=0.559$, $\omega_n=447.2$, $\omega_d=370.8$ rad/s; $i=2.7e^{-250t}\sin371t$ A; underdamped]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#4. Second-order circuits (L and C together)|series RLC step response]], damping classification.

## Given
$V=100$ V, $R=50\ \Omega$, $L=0.1$ H, $C=50\ \mu$F, $i(0)=0$, $v_C(0)=0$.

## Principle and why it applies
KVL after the switch closes: $L\dfrac{di}{dt}+Ri+v_C=V$ with $i=C\,dv_C/dt$. The initial conditions are zero, so $\dfrac{di}{dt}(0^+)=\dfrac VL$ (the whole 100 V appears across $L$ at $0^+$). The final state is $i_\infty=0$, $v_{C\infty}=V$ (the capacitor blocks DC). The damping ratio $\zeta=R/R_c$ tells us the *shape*.

## Diagram
![[T2-Q10-circuit.png]]

## Solution
$$\omega_n=\frac1{\sqrt{LC}}=\frac1{\sqrt{0.1\times50\times10^{-6}}}=447.2\ \text{rad/s},\qquad \alpha=\frac R{2L}=250\ \text{s}^{-1},$$
$$R_c=2\sqrt{\frac LC}=2\sqrt{2000}=\mathbf{89.44\ \Omega},\qquad \zeta=\frac{R}{R_c}=\frac{\alpha}{\omega_n}=\mathbf{0.559},\qquad \omega_d=\sqrt{\omega_n^2-\alpha^2}=\mathbf{370.8\ rad/s}.$$
$\zeta<1$: **underdamped** (also $R=50<R_c$).

**Current:** $i=\dfrac{V}{\omega_dL}e^{-\alpha t}\sin\omega_dt=\dfrac{100}{370.8\times0.1}e^{-250t}\sin371t$:
$$\mathbf{i=2.70\,e^{-250t}\sin371t\ \text{A}}.$$
**Element voltages:**
$$v_R=Ri=135\,e^{-250t}\sin371t\ \text{V},$$
$$v_L=L\frac{di}{dt}=e^{-250t}\big(100\cos371t-67.4\sin371t\big)\ \text{V}\quad(=0.1e^{-250t}[1001.7\cos371t-675\sin371t]\ \text{V}),$$
$$v_C=V-v_R-v_L=100-e^{-250t}\big(100\cos371t+67.4\sin371t\big)\ \text{V}.$$

**Ranges of $R$** (with $L=0.1$ H, $C=50\ \mu$F fixed):

| Response | Condition |
|---|---|
| overdamped | $R>R_c=89.44\ \Omega$ |
| critically damped | $R=89.44\ \Omega$ |
| underdamped | $0<R<89.44\ \Omega$ |
| undamped (pure oscillation at 447.2 rad/s) | $R=0$ |

## Result
$$\boxed{R_c=89.44\ \Omega,\ \zeta=0.559,\ \omega_n=447.2,\ \omega_d=370.8\ \text{rad/s};\ \ i=2.70e^{-250t}\sin371t\ \text{A};\ \text{underdamped}}$$

![[T2-Q10-response.png]]

![[T2-Q10-damping-vs-R.png]]

**Figure:** (top) the element voltages sum to 100 V at every instant; (bottom) $v_C$ for four resistances: the capacitor overshoots 100 V when underdamped (the ringing), approaches it without overshoot at critical damping, and slowly when over-damped.

## Check
Overshoot of $v_C$: $e^{-\pi\alpha/\omega_d}=e^{-2.12}=12\ \%$, peak $\approx112$ V. At $t=0^+$: $v_L=100$ V, $v_R=0$, $v_C=0$ ✓ (KVL). Final: $i\to0$, $v_C\to100$ V ✓.

## Trap / alternative
- Writing the amplitude of the current as $V/L=1000$ (the critically damped coefficient) instead of $V/(\omega_dL)=2.70$ A.
- The sheet's $v_C$ is printed in a factored form with a $0.269$ coefficient; it is the same function ($0.269\times371=100$, $0.269\times250=67.3$).
- "Undamped" requires $R=0$, not $R\to\infty$; large $R$ is overdamped (sluggish, not oscillatory).

## Concepts used
- Series RLC step response, damping ratio, critical resistance ([[Theory - Transients in RL, RC and RLC Circuits]], [[DC Step Response of RLC Circuits]], [[Series RLC Natural Response - Damping Cases]])
