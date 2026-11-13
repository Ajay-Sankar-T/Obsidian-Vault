---
tags: [fluid-mechanics, kinematics, material-derivative]
up: "[[Fluid Mechanics - MOC]]"
---

# Material Derivative and Fluid Acceleration

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]

## The question it answers

*How does a fluid particle experience a quantity as it moves through a (possibly steady) field?*

## Definition

For a scalar field $\phi(x,y,z,t)$:

$$\boxed{\frac{D\phi}{Dt}=\frac{\partial\phi}{\partial t}+\mathbf V\cdot\nabla\phi}=\frac{\partial\phi}{\partial t}+u\frac{\partial\phi}{\partial x}+v\frac{\partial\phi}{\partial y}+w\frac{\partial\phi}{\partial z}$$

## Two parts

**Local (temporal) change** — $\dfrac{\partial\phi}{\partial t}$ — the change *at a fixed point*, present even if no fluid were moving through it.

**Convective (advective) change** — $\mathbf V\cdot\nabla\phi$ — the change a particle experiences purely because it is *moving through* a spatially varying field, even if the field itself is frozen in time ($\partial\phi/\partial t=0$).

$$\boxed{\text{Material change}=\text{Local change}+\text{Convective change}}$$

## Fluid acceleration

Applying the material derivative to velocity itself:

$$\boxed{\mathbf a=\frac{D\mathbf V}{Dt}=\frac{\partial\mathbf V}{\partial t}+(\mathbf V\cdot\nabla)\mathbf V}$$

Cartesian components:

$$a_x=\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}+w\frac{\partial u}{\partial z}$$
$$a_y=\frac{\partial v}{\partial t}+u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial y}+w\frac{\partial v}{\partial z}$$
$$a_z=\frac{\partial w}{\partial t}+u\frac{\partial w}{\partial x}+v\frac{\partial w}{\partial y}+w\frac{\partial w}{\partial z}$$

**Critical point:** $\boxed{\text{steady flow does NOT necessarily mean zero acceleration}}$ — "steady" only kills the *local* term $\partial\mathbf V/\partial t$; the convective term $(\mathbf V\cdot\nabla)\mathbf V$ survives whenever the velocity field varies in space, which it does in almost any real flow (e.g. fluid speeding up through a nozzle in steady flow is still accelerating).

## Worked example: $\mathbf V=(x,-y)$

$u=x,\ v=-y$, no time dependence so $\partial\mathbf V/\partial t=0$.

$$a_x=u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}=x(1)+(-y)(0)=x$$
$$a_y=u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial y}=x(0)+(-y)(-1)=y$$

$$\boxed{\mathbf a=(x,y)}$$

— nonzero and growing away from the origin, despite the flow being perfectly steady; this is the [[Streamlines, Pathlines, Streaklines and Timelines|streamline]] pattern $xy=C$ (a stagnation-point flow), and the fluid genuinely accelerates as it moves outward/inward along those hyperbolas.

## Cross-domain: material derivative as a moving-frame time constant

The split "local change + convective change" is structurally the chain rule applied along a moving trajectory — the exact same operation that turns a spatial exponential decay ($\sigma(x)\sim e^{-x/\ell}$, Saint-Venant's principle) into a temporal one when the observer moves at fixed speed through it. See [[Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay — Time Constants, Damping and Spatial Relaxation]] for the general spatial/temporal-decay unification this belongs to.

## Related
- [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]
- [[Streamlines, Pathlines, Streaklines and Timelines|Streamlines, Pathlines, Streaklines and Timelines]]

## See also (concept notes)

- [[Differential Continuity Equation]], [[Motion of a Fluid Element]] and [[Euler's Equations of Fluid Motion]] — the next steps.
