---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RLC, initial-conditions]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q11: From an Integro-Differential Equation to a Circuit and a Solution

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q10 - Series RLC Step Response]] · Next: [[T2-Q12 - Parallel RLC Step Response]]

> [!question] An engineering device with two independent energy-storage elements is governed by $\;2\dfrac{di}{dt}+36i+450\displaystyle\int i\,dt=900$. Just before the forcing function is applied $i=10$ and $450\displaystyle\int_{-\infty}^0 i\,dt=70$. (a) Draw and label the equivalent circuit. (b) Does the response have a non-zero steady-state value? (c) Find $i(t)$. *[Sheet: $i(t)=28.87\,e^{-9t}\sin(12t+20.27^\circ)$ A]*

**Tests:** recognising a circuit from its equation, non-zero initial conditions, second-order solution.

## Given
$2\,\dot i+36\,i+450\int i\,dt=900$, with $i(0^+)=10$ and the integral term equal to $70$ at $t=0$.

## Principle and why it applies
Compare with KVL around a series loop: $\;L\dfrac{di}{dt}+Ri+\dfrac1C\displaystyle\int i\,dt=e(t)$. Term by term: $L=2$ H, $R=36\ \Omega$, $1/C=450\ \text{F}^{-1}$ so $C=\dfrac1{450}\ \text{F}=2.22$ mF, and the source is a **constant 900 V**. The "initial value of the integrating device" $450\int_{-\infty}^0i\,dt=70$ is by definition the initial capacitor voltage, $v_C(0)=70$ V. So the equation is just a series RLC circuit with a 900 V DC source and non-zero initial energy.

## Diagram
Series loop: 900 V source, $R=36\ \Omega$, $L=2$ H, $C=2.22$ mF, in which $i(0)=10$ A and $v_C(0)=70$ V.

## Solution
**(a)** Series RLC: $R=36\ \Omega$, $L=2$ H, $C=\tfrac1{450}$ F, 900 V source, $i(0)=10$ A, $v_C(0)=70$ V.

**(b) Steady state.** For $t\to\infty$ the capacitor charges to the source voltage ($v_C\to900$ V) and no DC current can flow: $i_\infty=0$. **The steady-state value in the time domain is zero** (the 900 V ends up on the capacitor).

**(c) Complete solution.** $\alpha=\dfrac R{2L}=9$, $\omega_0=\sqrt{\dfrac1{LC}}=\sqrt{\dfrac{450}2}=15$, $\omega_d=\sqrt{225-81}=12$ rad/s: underdamped ($\zeta=0.6$). Since $i_\infty=0$, $i=e^{-9t}(A\cos12t+B\sin12t)$.
- $i(0)=10\Rightarrow A=10$.
- Slope at $0^+$ from the original equation: $2\dot i(0)=900-36(10)-70=470\Rightarrow\dot i(0)=235$ A/s.
- $\dot i(0)=-9A+12B=235\Rightarrow 12B=325\Rightarrow B=27.08$.

$$i=e^{-9t}(10\cos12t+27.08\sin12t)=\sqrt{10^2+27.08^2}\,e^{-9t}\sin\!\big(12t+\arctan\tfrac{10}{27.08}\big)=\mathbf{28.87\,e^{-9t}\sin(12t+20.27^\circ)\ A}.$$

## Result
$$\boxed{i(t)=28.87\,e^{-9t}\sin(12t+20.27^\circ)\ \text{A};\quad i_\infty=0}$$

![[T2-Q11-response.png]]

## Check
$i(0)=28.87\sin20.27^\circ=10.0$ A ✓. The capacitor voltage ends at 900 V: $\int_0^\infty i\,dt=\dfrac{900-70}{450}=1.844$ C, and indeed $\int_0^\infty28.87e^{-9t}\sin(12t+0.3537)\,dt=1.844$ ✓ (charge delivered to the capacitor).

## Trap / alternative
- Putting the 900 on the wrong side: a constant forcing term does **not** produce a constant current here; the integral term absorbs it.
- Taking $\dot i(0)=900/L$ (the zero-initial-condition value) instead of using the actual initial values of $i$ and $v_C$.
- Alternatively differentiate once to get $2\ddot i+36\dot i+450i=0$ (the 900 disappears), then use $i(0)=10$ and $\dot i(0)=235$ as above.

## Concepts used
- Series RLC natural response with initial conditions ([[Theory - Transients in RL, RC and RLC Circuits]], [[Series RLC Natural Response - Damping Cases]])
