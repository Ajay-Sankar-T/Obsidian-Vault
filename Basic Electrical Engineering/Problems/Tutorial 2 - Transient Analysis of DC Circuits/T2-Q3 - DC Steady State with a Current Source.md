---
tags: [EE1100, tutorial-solution, DC-circuits, transients, steady-state, energy]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q3: DC Steady State Driven by a Current Source

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q2 - DC Steady State with L and C]] · Next: [[T2-Q4 - Source-Free RL Decay]]

> [!question] Find $V_{in}$, $I_1$ and $I_2$ under DC steady state with $I_{in}=2$ A, and the total energy stored in the inductor and the capacitor. *[Sheet: $V_{in}=20$ V, $I_1=2$ A, $I_2=0$; $E_L=10$ mJ, $E_C=5$ mJ]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#2. DC steady state (Q2, Q3)|DC steady state]], energy in $L$ and $C$.

## Given
A 2 A current source feeding two parallel branches: ($L=5$ mH in series with $10\ \Omega$; current $I_1$) and ($C=25\ \mu$F in series with $40\ \Omega$; current $I_2$). $V_{in}$ is the voltage across the source.

## Principle and why it applies
In DC steady state the inductor is a short and the capacitor an open circuit, so the capacitor branch carries **no current** and the whole 2 A flows through the inductor branch. With no current, the $40\ \Omega$ has no voltage across it, so the capacitor takes the full terminal voltage.

## Diagram
![[T2-Q3-circuit.png]]

## Solution
$$I_2=0\ \text{A},\qquad I_1=I_{in}=2\ \text{A},\qquad V_{in}=I_1\times10\ \Omega=\mathbf{20\ V}.$$
Inductor energy: $E_L=\tfrac12LI_1^2=\tfrac12(5\ \text{mH})(2)^2=\mathbf{10\ mJ}$.

Capacitor voltage: $v_C=V_{in}-I_2\times40=20$ V (no drop in the $40\ \Omega$), so
$$E_C=\tfrac12Cv_C^2=\tfrac12(25\ \mu\text{F})(20)^2=\mathbf{5\ mJ}.$$

## Result
$$\boxed{V_{in}=20\ \text{V},\ I_1=2\ \text{A},\ I_2=0,\ E_L=10\ \text{mJ},\ E_C=5\ \text{mJ}\ (\text{total }15\ \text{mJ})}$$

## Check
KCL at the top node: $I_1+I_2=2$ A ✓. The resistive power is only in the $10\ \Omega$: $2^2\times10=40$ W $=V_{in}I_{in}=40$ W ✓ (storage elements dissipate nothing in steady state).

## Trap / alternative
The $40\ \Omega$ resistor is a distractor in steady state (it sets the *transient* time constant, $\tau=R C=1$ ms, but not the final voltages). Don't use the $40\ \Omega$ to compute the capacitor voltage as "$I\times40$"; $I_2$ is zero.

## Concepts used
- Open/short equivalents at DC, KCL, energy in $L$ and $C$ ([[Theory - Transients in RL, RC and RLC Circuits]])
