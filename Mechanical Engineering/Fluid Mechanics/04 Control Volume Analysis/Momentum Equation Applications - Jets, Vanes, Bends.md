---
tags: [fluid-mechanics, control-volume, momentum, jets]
up: "[[Fluid Mechanics - MOC]]"
---

# Momentum Equation Applications — Jets, Vanes, Bends

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Linear Momentum Equation|Linear Momentum Equation]]

## Jet hitting a flat plate

A jet with velocity $V$ strikes a plate and stops (in the flow direction): $V_{1x}=V,\ V_{2x}=0$.

$$F_x=\dot m(0-V)\qquad\Rightarrow\qquad F=\dot mV=\rho AV\cdot V\qquad\Longrightarrow\qquad\boxed{F=\rho AV^2}$$

## Jet deflected by a vane

$\mathbf V_1=V\mathbf i$, outlet at angle $\theta$: $\mathbf V_2=V\cos\theta\,\mathbf i+V\sin\theta\,\mathbf j$.

$$\boxed{F_x=\dot mV(\cos\theta-1)}\qquad\boxed{F_y=\dot mV\sin\theta}$$

(forces **on the fluid by the vane** — the force of fluid **on** the vane is the negative of these, per [[Linear Momentum Equation|Linear Momentum Equation]]'s step 9).

## Nozzle

Continuity ([[Conservation of Mass (Continuity Equation)|Conservation of Mass]]): $A_1V_1=A_2V_2\Rightarrow V_2=\dfrac{A_1}{A_2}V_1$. Since $A_2<A_1$, $V_2>V_1$ — the nozzle accelerates the flow. The momentum equation on the nozzle as a whole must include pressure forces at the inlet/outlet and the wall reaction holding the nozzle in place.

## Pipe bend

Even if $V_1=V_2$ (same speed), a force is still required because the **direction** of velocity changes — momentum is a vector, and turning it (even at constant speed) requires a net force, exactly as [[Phasors and Complex Algebra|Phasors and Complex Algebra]] requires vector (not scalar) addition for anything with both magnitude and direction.

For a $90°$ bend: $V_{1x}=V_1,\ V_{1y}=0$ (inlet) and $V_{2x}=0,\ V_{2y}=V_2$ (outlet):

$$\boxed{\sum F_x=-\dot mV_1}\qquad\boxed{\sum F_y=\dot mV_2}$$

plus any pressure, weight, and support forces acting on the bend.

## Related
- [[Linear Momentum Equation|Linear Momentum Equation]]
- [[Conservation of Mass (Continuity Equation)|Conservation of Mass (Continuity Equation)]]

## See also
- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] — nozzle and Venturi flow combine Bernoulli with this momentum balance.
