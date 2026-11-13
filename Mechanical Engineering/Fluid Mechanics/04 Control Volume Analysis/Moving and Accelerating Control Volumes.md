---
tags: [concept, fluid-mechanics, control-volume, momentum]
status: draft
aliases: [moving control volume, accelerating control volume, relative velocity, non-inertial control volume, rocket]
up: "[[Fluid Mechanics - MOC]]"
---

# Moving and Accelerating Control Volumes

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Reynolds Transport Theorem|Reynolds Transport Theorem]], [[Linear Momentum Equation|Linear Momentum Equation]] · see also: [[Angular Momentum Principle|Angular Momentum Principle]]

## Core Idea

> **One-sentence definition:** when the control volume itself moves, fluid crosses its surface at the **relative** velocity $\mathbf W=\mathbf V-\mathbf V_{CV}$, and if it accelerates, a fictitious force $-\int a_{CV}\,dm$ must be added to the momentum balance.

**Intuition:** the equations in [[Linear Momentum Equation|Linear Momentum Equation]] assume a CV fixed in an inertial frame. A cart, a rocket or a moving vane is not. Either work in the frame of the CV and use relative velocities, or keep the inertial frame and correct the mass flux.

## Governing Relations

Velocity relation: $\ \mathbf V=\mathbf W+\mathbf V_{CV}$ (absolute = relative + CV velocity).

**Mass** (any moving or deforming CV):

$$\frac{\partial}{\partial t}\int_{CV}\rho\,dV+\oint_{CS}\rho\,(\mathbf W\cdot\mathbf n)\,dA=0$$

**Case 1: CV moving at constant velocity (inertial).** Newton's law is unchanged; only the flux uses $\mathbf W$:

$$\boxed{\sum\mathbf F=\frac{\partial}{\partial t}\int_{CV}\mathbf W\rho\,dV+\oint_{CS}\mathbf W\,\rho\,(\mathbf W\cdot\mathbf n)\,dA}$$

(equivalently, work entirely with relative velocities; the constant offset $\mathbf V_{CV}$ drops out because of mass conservation).

**Case 2: CV with rectilinear acceleration $\mathbf a_{CV}$ (non-inertial):**

$$\boxed{\sum\mathbf F-\int_{CV}\mathbf a_{CV}\,\rho\,dV=\frac{\partial}{\partial t}\int_{CV}\mathbf W\rho\,dV+\oint_{CS}\mathbf W\,\rho\,(\mathbf W\cdot\mathbf n)\,dA}$$

$\sum\mathbf F$ contains only **real** forces (pressure, weight, supports). The term $-\int\mathbf a_{CV}\rho\,dV$ is the inertial (d'Alembert) force on the mass inside.

**Where:** $\mathbf W$ = fluid velocity measured **relative to the CV**; $\mathbf V_{CV}$, $\mathbf a_{CV}$ = velocity and acceleration of the CV in an inertial frame.

**Assumptions:** rigid CV translating without rotation (rotation adds Coriolis and centrifugal terms).

## Visual

Sketch a jet of speed $V$ striking a vane that moves away at $U$. In the vane's frame the jet arrives at $V-U$. Draw the CV on the vane, label $\mathbf W_{\rm in}=V-U$ and $\mathbf W_{\rm out}$ along the vane exit, and check the mass flow entering the CV is $\rho A(V-U)$ for a **single** vane.

## When To Use

- A **vane, plate or cart moving** under a jet; a **boat or aircraft** with a steady flow past it in its own frame.
- **Rockets** and anything whose mass changes while accelerating.
- A tank on wheels that is pushed by its own outflow.

**Recognition pattern:** "the vane moves at speed $U$", "rocket accelerates", "mounted on a cart" → **relative velocity, possibly with an inertial term**.

## Method

1. **Identify** whether the CV moves at constant velocity (inertial) or accelerates.
2. **Choose** axes attached to the CV; write every velocity as $\mathbf W=\mathbf V-\mathbf V_{CV}$.
3. **Apply** mass conservation with $\mathbf W$ to find the relative mass flow at each port.
4. **Apply** the momentum equation (add $-\int a_{CV}\rho\,dV$ if accelerating) using $\mathbf W$ in the flux.
5. **Check:** a single moving vane receives $\rho A(V-U)$, a train of vanes receives the full $\rho AV$; signs of the inertial term.

## Derivation / Why It Works

The RTT holds in any frame provided the velocity in the flux term is the velocity *relative to the control surface*, because that is what carries a property across it. For a constant-velocity CV, Newton's law is frame-invariant (Galilean invariance), so the force balance is the same. For an accelerating CV, apply Newton's law in the CV's frame by adding the force $-m\,\mathbf a_{CV}$ to each fluid element: summing over the CV mass gives the extra integral.

## Common Traps

- **Trap:** using the jet's mass flow $\rho AV$ for a single receding plate.
  - **Why:** the plate runs away from the jet, so only the part $\rho A(V-U)$ arrives per second.
  - **Avoid it by:** counting the mass that actually crosses the CV in its own frame.
- **Trap:** using absolute velocity in the flux term of an accelerating CV.
- **Trap:** forgetting the inertial term for an accelerating CV, or giving it the wrong sign.
- **Trap:** applying the formula to a **rotating** CV without Coriolis terms.

## Example

### Given
A water jet of speed $V=20$ m/s and area $A=1\times10^{-3}$ m² ($\rho=998$ kg/m³) strikes a flat plate normal to the jet, which moves away at $U=8$ m/s. Also a rocket of mass 500 kg burning 10 kg/s with exhaust speed 2000 m/s relative to the rocket.

### Solution
**Plate:** relative speed $W=V-U=12$ m/s, mass flow on the plate $\rho AW$. The relative momentum is destroyed:

$$F=\rho A(V-U)^2=998\times10^{-3}\times12^2=143.7\ \text{N}.$$

For a fixed plate $F=\rho AV^2=399.2$ N. For a **series** of plates (a wheel) that eventually intercepts the entire flow, $F=\rho AV(V-U)=239.5$ N.

**Rocket:** thrust $=\dot m\,V_e=10\times2000=20$ kN; initial acceleration, ignoring drag:

$$a=\frac{\dot mV_e}{M}-g=\frac{20\,000}{500}-9.81=30.2\ \text{m/s}^2.$$

**Answer:** 143.7 N on the single moving plate (399 N fixed, 240 N for a train); 30.2 m/s² for the rocket.
**Key takeaway:** the same jet pushes harder on a series of vanes than on one running vane because the mass flow entering the control volume is larger.

## Connections

### Prerequisites
- [[Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Linear Momentum Equation|Linear Momentum Equation]]

### Related Concepts
- [[Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications — Jets, Vanes, Bends]] — the fixed-vane versions of these problems.
- [[Angular Momentum Principle|Angular Momentum Principle]] — the rotating case.
- [[System and Control Volume|System and Control Volume]] — why the CV can be chosen freely.

### Next
- [[Euler's Equations of Fluid Motion|Euler's Equations of Fluid Motion]] — an accelerating tank uses $\rho(\mathbf g-\mathbf a)$ in the same way.

### Cross-domain links
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors — Velocity Polygons]] — relative velocity $\mathbf W=\mathbf V-\mathbf V_{CV}$ is the relative-velocity construction of kinematics of machines.
- [[Energy Methods - A Unified View|Energy Methods — A Unified View]] — frame changes redistribute work between "kinetic energy" and "work done by the support" without changing the physics.

## Quick Recall

> **In one line:** use $\mathbf W=\mathbf V-\mathbf V_{CV}$ in the flux terms; add $-\int a_{CV}\rho\,dV$ if the CV accelerates.

**Formula / trigger:** $$\sum\mathbf F-\int\mathbf a_{CV}\rho\,dV=\partial_t\!\int\mathbf W\rho\,dV+\oint\mathbf W\rho(\mathbf W\!\cdot\!\mathbf n)\,dA$$

**Remember:** single moving vane: $\rho A(V-U)^2$; train of vanes: $\rho AV(V-U)$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
