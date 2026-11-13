---
tags: [concept, fluid-mechanics, inviscid-flow, euler-equations]
status: draft
aliases: [Euler equations, inviscid momentum equation, frictionless flow equation, streamline coordinates, rigid-body fluid motion]
up: "[[Fluid Mechanics - MOC]]"
---

# Euler's Equations of Fluid Motion

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Material Derivative and Fluid Acceleration|Material Derivative]], [[Pressure and the Hydrostatic Equation|Hydrostatic Equation]], [[Ideal Fluid|Ideal Fluid]] · formulas: [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank §1]]

## Core Idea

> **One-sentence definition:** Euler's equations are Newton's second law for a frictionless fluid element: mass times acceleration equals the pressure force plus the body force, $\rho\,D\mathbf V/Dt=-\nabla p+\rho\mathbf g$.

**Intuition:** without viscosity the only surface force on an element is the pressure difference across it. A net pressure *gradient* accelerates the fluid toward lower pressure; gravity adds its weight. Everything about inviscid flow follows from this balance.

## Governing Relation

$$\boxed{\rho\frac{D\mathbf V}{Dt}=\rho\Big[\frac{\partial\mathbf V}{\partial t}+(\mathbf V\cdot\nabla)\mathbf V\Big]=-\nabla p+\rho\mathbf g}$$

Cartesian ($z$ up): $\ \rho a_x=-\dfrac{\partial p}{\partial x},\ \ \rho a_y=-\dfrac{\partial p}{\partial y},\ \ \rho a_z=-\dfrac{\partial p}{\partial z}-\rho g$.

**Streamline coordinates** ($s$ along the streamline, $n$ toward the centre of curvature, radius $R$):

$$\frac{\partial V}{\partial t}+V\frac{\partial V}{\partial s}=-\frac1\rho\frac{\partial p}{\partial s}-g\frac{\partial z}{\partial s},\qquad\frac{V^2}{R}=-\frac1\rho\frac{\partial p}{\partial n}-g\frac{\partial z}{\partial n}$$

- Along $s$: integrates to Bernoulli.
- Normal to $s$: pressure **increases away from the centre of curvature** (centripetal force); for straight parallel streamlines the pressure is hydrostatic across the flow.

**Rigid-body motion** ($D\mathbf V/Dt=\mathbf a$ uniform, no relative motion): $\nabla p=\rho(\mathbf g-\mathbf a)$, the hydrostatic equation with $\mathbf g$ replaced by $\mathbf g-\mathbf a$.

**Where:** $p$ = pressure; $\mathbf g$ = gravitational acceleration; $\mathbf a=D\mathbf V/Dt$.

**Assumptions:** inviscid ($\mu=0$), continuum, no body force other than gravity (add others as needed). Valid for compressible or incompressible flow.

## Visual

Draw a curved streamline with a small element: pressure is higher on the outer face than the inner face; the difference provides the centripetal force $\rho V^2/R$ per unit volume. For a flow in a duct bend, this gives high pressure on the outer wall and low on the inner wall.

## When To Use

- Deriving **Bernoulli** (integrate along a streamline) and the **pressure field** in an accelerating or rotating fluid.
- **Tank on a truck**, **rotating cylinder of liquid**, **bend pressure distribution**.
- Giving the inviscid limit of the Navier–Stokes equations: [[Navier-Stokes Equations|Navier-Stokes Equations]] with $\mu=0$.

**Recognition pattern:** "frictionless", "ideal fluid", "tank accelerates", "liquid in a rotating container" → **Euler's equations**.

## Method

1. **Identify** the acceleration of each element ($D\mathbf V/Dt$; zero relative acceleration in rigid-body cases).
2. **Choose** coordinates (Cartesian for linear acceleration, streamline or cylindrical for curved motion).
3. **Apply** $\nabla p=\rho(\mathbf g-\mathbf a)$ or the streamwise and normal components; integrate to find $p$.
4. **Check:** reduce to hydrostatics when $\mathbf a=0$; compare the sign of $\partial p/\partial n$ with the centripetal direction.

## Derivation / Why It Works

For an element of volume $dV$ the net pressure force is $-\nabla p\,dV$ (pressure acts inward on every face; the difference across opposite faces gives the gradient). Add the body force $\rho\mathbf g\,dV$ and set it equal to mass times acceleration $\rho\,dV\,D\mathbf V/Dt$. Dropping $\tau$ from the full momentum equation ([[Navier-Stokes Equations|Navier-Stokes]]) gives the same result. Using the vector identity $(\mathbf V\cdot\nabla)\mathbf V=\nabla(\tfrac12V^2)-\mathbf V\times\boldsymbol\zeta$, the equation becomes
$$\frac{\partial\mathbf V}{\partial t}+\nabla\Big(\frac{V^2}2\Big)-\mathbf V\times\boldsymbol\zeta=-\frac{\nabla p}\rho-g\nabla z.$$
The term $\mathbf V\times\boldsymbol\zeta$ is perpendicular to $\mathbf V$, so dotting with a displacement **along** a streamline eliminates it (Bernoulli), and it vanishes everywhere if the flow is irrotational.

## Common Traps

- **Trap:** using the hydrostatic equation $\nabla p=\rho\mathbf g$ in an accelerating tank.
  - **Avoid it by:** replacing $\mathbf g$ with $\mathbf g-\mathbf a$.
- **Trap:** getting the sign of the normal pressure gradient wrong in curved flow.
  - **Avoid it by:** remembering that pressure rises *away* from the centre of curvature.
- **Trap:** applying Euler's equations where viscosity matters (boundary layers, wakes, pipes at low $Re$).
- **Trap:** forgetting that along a streamline Bernoulli applies, but between streamlines only if irrotational.

## Example

### Given
A tank of water accelerates horizontally at $a=3$ m/s². A cylindrical tank rotates at $\Omega=10$ rad/s with water at rest relative to the walls.

### Solution
**Accelerating tank:** $\nabla p=\rho(\mathbf g-\mathbf a)$ so $\partial p/\partial x=-\rho a,\ \partial p/\partial z=-\rho g$. The free surface is a line of constant $p$, with slope
$$\tan\theta=\frac ag=\frac3{9.81}=0.306\ \Rightarrow\ \theta=17.0^\circ.$$

**Rotating tank:** $\partial p/\partial r=\rho\Omega^2r,\ \partial p/\partial z=-\rho g$, so the surface is $z=\Omega^2r^2/(2g)$. At $r=0.1$ m the rise above the axis is
$$z=\frac{10^2(0.1)^2}{2(9.81)}=0.051\ \text{m}.$$

**Answer:** surface tilted at 17.0°; paraboloid rising 5.1 cm at $r=0.1$ m.
**Key takeaway:** when the fluid moves as a rigid body, replace $\mathbf g$ by $\mathbf g-\mathbf a$ and the hydrostatic method still works.

## Connections

### Prerequisites
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]

### Related Concepts
- [[Ideal Fluid|Ideal Fluid]]
- [[Vorticity and Circulation|Vorticity and Circulation]] — the $\mathbf V\times\boldsymbol\zeta$ term.
- [[Moving and Accelerating Control Volumes|Moving and Accelerating Control Volumes]]
- [[Linear Momentum Equation|Linear Momentum Equation]] — the integral version.

### Next
- [[Bernoulli Equation|Bernoulli Equation]], [[Navier-Stokes Equations|Navier-Stokes Equations]]

### Cross-domain links
- [[Energy Methods - A Unified View|Energy Methods — A Unified View]] — integrating Euler along a streamline is the work–energy theorem for a fluid parcel.
- [[Turbomachines - Euler Equation and Velocity Triangles|Turbomachines — Euler Equation and Velocity Triangles]] — a different "Euler equation" (angular momentum across a rotor); do not confuse the two.

## Quick Recall

> **In one line:** $\rho\,D\mathbf V/Dt=-\nabla p+\rho\mathbf g$: mass × acceleration = pressure force + weight.

**Formula / trigger:** $$\rho\frac{D\mathbf V}{Dt}=-\nabla p+\rho\mathbf g,\qquad\text{rigid body: }\nabla p=\rho(\mathbf g-\mathbf a)$$

**Remember:** pressure rises away from the centre of curvature; the surface in an accelerating tank slopes at $\tan\theta=a/g$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
