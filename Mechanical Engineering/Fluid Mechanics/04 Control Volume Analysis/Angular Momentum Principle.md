---
tags: [concept, fluid-mechanics, control-volume, angular-momentum]
status: draft
aliases: [angular momentum equation, moment of momentum, torque on a control volume, Euler turbine equation, lawn sprinkler]
up: "[[Fluid Mechanics - MOC]]"
---

# Angular Momentum Principle

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Reynolds Transport Theorem|Reynolds Transport Theorem]], [[Linear Momentum Equation|Linear Momentum Equation]] · next: [[Moving and Accelerating Control Volumes|Moving and Accelerating Control Volumes]]

## Core Idea

> **One-sentence definition:** the net torque on the fluid in a control volume about a fixed point equals the rate of change of the angular momentum stored inside plus the net flux of angular momentum through the surface.

**Intuition:** linear momentum tells you the *force* a device must supply to turn a flow. Angular momentum tells you the *torque* needed to give the flow a swirl. Anything that swirls fluid (pump, turbine, sprinkler, propeller) exerts or receives a torque equal to the swirl it adds per second.

## Governing Relation

Take $B=\mathbf r\times m\mathbf V$ and $b=\mathbf r\times\mathbf V$ in the [[Reynolds Transport Theorem|Reynolds Transport Theorem]], for an inertial control volume and a fixed point $O$:

$$\boxed{\sum\mathbf M_O=\frac{\partial}{\partial t}\int_{CV}(\mathbf r\times\mathbf V)\rho\,dV+\oint_{CS}(\mathbf r\times\mathbf V)\,\rho\,(\mathbf V\cdot\mathbf n)\,dA}$$

**Steady, uniform at each port:**

$$\sum\mathbf M_O=\sum_{\rm out}\dot m\,(\mathbf r\times\mathbf V)-\sum_{\rm in}\dot m\,(\mathbf r\times\mathbf V)$$

**Planar swirl about a shaft axis** ($V_\theta$ = tangential component of the **absolute** velocity):

$$\boxed{T_{\rm shaft\ on\ fluid}=\dot m\,(r_2V_{\theta2}-r_1V_{\theta1})},\qquad P=\omega T=\dot m\,(U_2V_{\theta2}-U_1V_{\theta1}),\ U=\omega r$$

The last form is the **Euler turbomachine equation** (head $=P/\dot mg$), developed with velocity triangles in [[Turbomachines - Euler Equation and Velocity Triangles|Turbomachines — Euler Equation and Velocity Triangles]].

**Where:**
- $\sum\mathbf M_O$ = sum of external torques (shaft, wall reactions, pressure and body-force moments) about $O$
- $\mathbf r$ = position from $O$ to the point on the surface; $\dot m$ = mass flow through a port
- $V_\theta$ = tangential velocity measured in an **inertial** frame

**Assumptions:** inertial control volume, fixed moment point, flow uniform over each port (otherwise integrate).

## Visual

No new figure: use the sprinkler sketch in the example. Draw the control volume around the rotating arm, mark $R$, the nozzle speed $V_{\rm rel}$ relative to the arm, and the arm speed $\omega R$; the absolute tangential exit velocity is $V_{\rm rel}-\omega R$.

## When To Use

- Torque on a **sprinkler, rotating arm, pump or turbine runner, fan, propeller, rocket nozzle on a swivel**.
- Torque on a bend or a vane when the line of action of the force matters (moment arm).
- Problems that ask for **rotation speed** at zero or given friction torque.

**Recognition pattern:** "torque", "power of the turbine/pump", "rotates freely", "tangential velocity" → **angular momentum**.

## Method

1. **Identify** the axis and a fixed moment point $O$ on it; draw the control volume around the rotor.
2. **Choose** a sign convention for torque (counter-clockwise positive).
3. **Apply** at each port: compute $\dot m$, the **absolute** tangential velocity $V_\theta$, and the lever arm $r$; form $\dot m\,r\,V_\theta$.
4. **Solve** $\sum M=\sum\dot m r V_\theta|_{\rm out}-\sum\dot m r V_\theta|_{\rm in}$ for the unknown torque or speed.
5. **Check:** incoming fluid with no swirl contributes zero; pressures acting at atmospheric produce no net torque; the shaft torque *on the fluid* is the opposite of the torque *on the shaft*.

## Derivation / Why It Works

For a system of fixed mass, the angular momentum about $O$ changes only by the external torques (Newton's second law moment form, $\sum\mathbf M=d\mathbf H/dt$ with $\mathbf H=\int\mathbf r\times\mathbf V\,dm$). The RTT converts $d/dt$ of the system quantity into a control-volume derivative plus a surface flux. Internal torques between fluid parcels cancel in pairs, so only external torques remain.

## Common Traps

- **Trap:** using the velocity relative to the rotating arm for $V_\theta$.
  - **Why:** angular momentum is defined with the absolute velocity.
  - **Avoid it by:** subtracting the wall speed: $V_\theta=V_{\rm rel}-\omega R$ for a jet leaving backwards.
- **Trap:** dropping the sign of the torque (a sprinkler turns opposite to its jets).
- **Trap:** taking moments about a moving point or including atmospheric pressure forces that cancel.
- **Trap:** treating the fluid torque on the rotor as the torque on the fluid (Newton's third law again).

## Example

### Given
A two-armed sprinkler. Arms of radius $R=0.15$ m, two nozzles of diameter 5 mm, total flow $Q=3\times10^{-4}$ m³/s of water ($\rho=998$ kg/m³), discharging tangentially to atmosphere. Find (a) the torque needed to hold it at rest, (b) the free-running speed with no friction, (c) the speed with a 0.05 N·m bearing friction.

### Approach
Water enters on the axis with no angular momentum. Each nozzle passes $Q/2$ with relative speed $V_{\rm rel}$.

### Solution
$$V_{\rm rel}=\frac{Q/2}{\pi d^2/4}=\frac{1.5\times10^{-4}}{1.9635\times10^{-5}}=7.639\ \text{m/s},\qquad\dot m=\rho Q=0.2994\ \text{kg/s}.$$

(a) At rest: $T=\dot m\,R\,V_{\rm rel}=0.2994\times0.15\times7.639=0.343$ N·m.

(b) Free spin: no external torque, so $\dot m R(V_{\rm rel}-\omega R)=0$ and $\omega=V_{\rm rel}/R=50.9$ rad/s $=486$ rpm.

(c) With friction torque $T_f$: $\dot m R(V_{\rm rel}-\omega R)=T_f$, so $V_{\rm rel}-\omega R=0.05/0.04491=1.113$ m/s, giving $\omega=43.5$ rad/s $=415$ rpm.

**Answer:** 0.343 N·m, 486 rpm, 415 rpm.
**Key takeaway:** the water leaves with *zero absolute swirl* when the arm runs freely; friction forces the water to keep some swirl, which is what takes torque out of the stream.

## Connections

### Prerequisites
- [[Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Linear Momentum Equation|Linear Momentum Equation]]

### Related Concepts
- [[Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications]] — the linear-momentum partner problems.
- [[Moving and Accelerating Control Volumes|Moving and Accelerating Control Volumes]] — relative against absolute velocity.
- [[Turbomachines - Euler Equation and Velocity Triangles|Turbomachines — Euler Equation and Velocity Triangles]] — the same equation used for pumps and turbines.

### Next
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]] — turns shaft power into head.

### Cross-domain links
- [[Two-Body Problem and Hohmann Transfer|Two-Body Problem and Hohmann Transfer]] — conservation of $\mathbf r\times\mathbf V$ under a central force is the same statement as $\sum M_O=0$ here.
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors]] — velocity triangles are the vector bookkeeping for $V_\theta$.
- [[Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — power $=T\omega$ balances across a machine just as $\dot m(U_2V_{\theta2}-U_1V_{\theta1})$ does.

## Quick Recall

> **In one line:** torque on the fluid $=\dot m\,(rV_\theta)_{\rm out}-\dot m\,(rV_\theta)_{\rm in}$, with $V_\theta$ in the inertial frame.

**Formula / trigger:** $$T=\dot m\,(r_2V_{\theta2}-r_1V_{\theta1}),\qquad P=T\omega$$

**Remember:** a freely spinning sprinkler leaves the water with zero absolute swirl: $\omega R=V_{\rm rel}$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
