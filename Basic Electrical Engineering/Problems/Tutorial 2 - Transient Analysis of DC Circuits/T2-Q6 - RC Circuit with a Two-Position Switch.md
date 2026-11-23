---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RC-circuit, switching]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q6: RC Circuit with a Two-Position Switch

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q5 - RL Circuit with a Switch Opening]] · Next: [[T2-Q7 - Discharging a Capacitor through a Coil]]

> [!question] The switch S is thrown from position 1 to 2 at $t=0$. Find $v_C(t)$ and $i_C(t)$ for $t\ge0$. A 10 mA source with a $4\ \text{k}\Omega$ shunt, a $4\ \text{k}\Omega$ at position 2, and the branch $C=10\ \mu$F in series with $6\ \text{k}\Omega$. *[Sheet: $v_C=40e^{-10t}$ V, $i_C=-4e^{-10t}$ mA]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#3. First-order circuits (one storage element)|first-order RC discharge]]; initial value from a DC steady state.

## Given
Position 1 connects the capacitor branch ($C$ in series with $6\ \text{k}\Omega$) to node $a$, which carries the 10 mA source and a $4\ \text{k}\Omega$ shunt. Position 2 connects the capacitor branch to a separate $4\ \text{k}\Omega$ resistor returning to ground. $v_C$ is positive at the top plate, $i_C$ flows into it.

## Principle and why it applies
The capacitor voltage is continuous across the switching instant, so $v_C(0^+)$ equals the steady-state value reached in position 1. After the switch moves the source is gone and the capacitor discharges through whatever resistance it now sees: a **source-free RC circuit**, $v_C=v_C(0^+)e^{-t/RC}$.

## Diagram
![[T2-Q6-circuit.png]]

## Solution
**Before ($t<0$, position 1, long time):** DC steady state, the capacitor branch carries no current, so the 10 mA flows only through the $4\ \text{k}\Omega$ shunt:
$$V_a=10\ \text{mA}\times4\ \text{k}\Omega=40\ \text{V},\qquad v_C(0^-)=V_a=40\ \text{V}\ (\text{no drop in }6\ \text{k}\Omega\text{ since }i=0).$$
So $v_C(0^+)=40$ V.

**After ($t>0$, position 2):** the capacitor discharges through $6\ \text{k}\Omega+4\ \text{k}\Omega=10\ \text{k}\Omega$:
$$\tau=RC=10\times10^3\times10\times10^{-6}=0.1\ \text{s}.$$
$$v_C(t)=40e^{-t/0.1}=\mathbf{40e^{-10t}\ V}.$$
$$i_C=C\frac{dv_C}{dt}=10\times10^{-6}\times(-400)e^{-10t}=\mathbf{-4e^{-10t}\ mA}.$$

## Result
$$\boxed{v_C(t)=40e^{-10t}\ \text{V},\qquad i_C(t)=-4e^{-10t}\ \text{mA}\quad(t\ge0)}$$

![[T2-Q6-response.png]]

## Check
$i_C(0^+)=-v_C(0^+)/10\ \text{k}\Omega=-40/10^4=-4$ mA ✓. The negative sign says the current actually leaves the positive plate: the capacitor is discharging. Energy: initially $\tfrac12(10\ \mu)(40)^2=8$ mJ; dissipated in the $10\ \text{k}\Omega$: $\int i^2R\,dt=16\times10^{-6}\times10^4\times\dfrac{0.1}{2}=8$ mJ ✓.

## Trap / alternative
The $4\ \text{k}\Omega$ in the source network plays **no part** in the discharge (it is disconnected from the capacitor after the switch). A common error is to include it in $R$, or to use $v_C(0)=10$ mA $\times(4\parallel4)$, forgetting that in position 1 the capacitor branch is connected only to node $a$.

## Concepts used
- RC time constant, continuity of $v_C$, DC steady state ([[Theory - Transients in RL, RC and RLC Circuits]])
