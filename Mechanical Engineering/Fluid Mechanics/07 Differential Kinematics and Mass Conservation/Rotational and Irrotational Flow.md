---
tags: [concept, fluid-mechanics, kinematics, irrotational, potential-flow]
status: draft
aliases: [irrotational flow, rotational flow, velocity potential, stream function, potential flow, Laplace equation]
up: "[[Fluid Mechanics - MOC]]"
---

# Rotational and Irrotational Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Vorticity and Circulation|Vorticity and Circulation]], [[Differential Continuity Equation|Differential Continuity Equation]] · formulas: [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank §6]]

## Core Idea

> **One-sentence definition:** a flow is **irrotational** where $\nabla\times\mathbf V=\mathbf 0$ (fluid elements do not spin) and **rotational** otherwise; irrotational flow can be described by a single scalar potential $\phi$ with $\mathbf V=\nabla\phi$.

**Intuition:** an irrotational flow is the smooth, "no shear, no swirl" part of the motion, typically the region outside boundary layers. It is mathematically far easier because three velocity components collapse into one scalar function.

## Governing Relations

$$\textbf{Irrotational: }\ \nabla\times\mathbf V=0\ \Longleftrightarrow\ \mathbf V=\nabla\phi,\qquad u=\phi_x,\ v=\phi_y,\ w=\phi_z$$

Incompressible **and** irrotational: **Laplace's equation**

$$\boxed{\nabla^2\phi=0},\qquad\text{plane: }\ u=\phi_x=\psi_y,\ \ v=\phi_y=-\psi_x,\ \ \nabla^2\psi=0$$

- Streamlines ($\psi=$ const) and potential lines ($\phi=$ const) are **orthogonal** except at stagnation points.
- In irrotational flow the Bernoulli constant is the **same everywhere**, not only along one streamline ([[Bernoulli Equation|Bernoulli Equation]]).
- Rotational plane flow has $\nabla^2\psi=-\zeta_z\neq0$.

| Flow | $\psi$ | $\phi$ | Irrotational? |
|---|---|---|---|
| uniform stream $U$ | $Uy$ | $Ux$ | yes |
| stagnation $u=Kx,\ v=-Ky$ | $Kxy$ | $\tfrac K2(x^2-y^2)$ | yes |
| line vortex $K/r$ | $-K\ln r$ | $K\theta$ | yes, except at the axis |
| solid-body rotation $u=-\Omega y,\ v=\Omega x$ | $-\tfrac12\Omega r^2$ | none | **no**, $\zeta=2\Omega$ |
| simple shear $u=\dot\gamma y$ | $\tfrac12\dot\gamma y^2$ | none | **no**, $\zeta=-\dot\gamma$ |

**Where:** $\phi$ = velocity potential; $\psi$ = stream function (White's sign convention $u=\psi_y$).

**Assumptions:** simply connected region for a single-valued $\phi$ (the free vortex has a multi-valued $\phi=K\theta$).

## Visual

The same two motion figures that appear in [[Motion of a Fluid Element|Motion of a Fluid Element]] decide the question: if the element only stretches and shears but its axes show no net rotation (stagnation flow, the dashed-to-filled picture in FM-K4), the flow is irrotational.

![[FM-K4-p459-element.png]]

**Figure:** an element in the stagnation flow $\mathbf V=x\mathbf i-y\mathbf j$ is stretched in $x$ and squeezed in $y$ by factors $e^{\pm t}$; it stays rectangular (irrotational) and its area is conserved (incompressible).

## When To Use

- Whenever the flow is a **steady, high-$Re$ region away from walls**: use potential flow (Laplace) for pressures on bodies.
- To justify applying Bernoulli **between different streamlines**.
- To construct flows by **superposition** (uniform stream + source + vortex).

**Recognition pattern:** "outside the boundary layer", "ideal flow past a cylinder", "potential function" → **irrotational flow**.

## Method

1. **Identify** the velocity field; check continuity first.
2. **Choose** the test: compute $\zeta=\nabla\times\mathbf V$.
3. **Apply:** if $\zeta=0$, integrate $u=\phi_x$ in $x$, add $f(y)$, then match $v=\phi_y$ to fix $f$; likewise for $\psi$.
4. **Check:** $\nabla^2\phi=0$, orthogonality of streamlines and potential lines, and the sign convention of $\psi$.

## Derivation / Why It Works

The curl of a gradient is identically zero, so any $\mathbf V=\nabla\phi$ is irrotational. Conversely, if the curl vanishes everywhere in a simply connected region, the line integral $\oint\mathbf V\cdot d\mathbf l=0$ (Stokes) so $\phi=\int\mathbf V\cdot d\mathbf l$ is path-independent. Substituting $\mathbf V=\nabla\phi$ into $\nabla\cdot\mathbf V=0$ gives $\nabla^2\phi=0$.

## Common Traps

- **Trap:** deciding rotationality from the streamline shape.
  - **Why:** straight streamlines in shear flow are rotational; curved streamlines of a free vortex are irrotational.
  - **Avoid it by:** computing the curl.
- **Trap:** using Bernoulli between two streamlines in a rotational flow.
- **Trap:** forgetting the singularity at a vortex axis.
- **Trap:** mixing the sign conventions of $\psi$ between textbooks.

## Example

### Given
The flow $u=x^2-y^2,\ v=-2xy$ (from the continuity example). Is it irrotational? Find $\phi$.

### Solution
$$\zeta_z=v_x-u_y=-2y-(-2y)=0\ \ \checkmark,\qquad\nabla\cdot\mathbf V=2x-2x=0\ \ \checkmark$$
Integrate $u=\phi_x$: $\phi=x^3/3-xy^2+f(y)$; $v=\phi_y=-2xy+f'(y)=-2xy\Rightarrow f=$ const.

$$\boxed{\phi=\frac{x^3}{3}-xy^2},\qquad\psi=x^2y-\frac{y^3}{3}.$$

**Answer:** irrotational and incompressible, with $\phi=x^3/3-xy^2$.
**Key takeaway:** passing both tests means the flow can be described by $\phi$, and Bernoulli's constant is global.

## Connections

### Prerequisites
- [[Vorticity and Circulation|Vorticity and Circulation]]
- [[Differential Continuity Equation|Differential Continuity Equation]]

### Related Concepts
- [[Bernoulli Equation|Bernoulli Equation]] — global constant if irrotational.
- [[Euler's Equations of Fluid Motion|Euler's Equations]] — irrotational solutions of Euler.
- [[Streamlines, Pathlines, Streaklines and Timelines|Streamlines, Pathlines, Streaklines and Timelines]]

### Next
- [[Euler's Equations of Fluid Motion|Euler's Equations]], [[Bernoulli Equation|Bernoulli Equation]]

### Cross-domain links
- [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] — Laplace's equation for $\phi$ also governs steady heat conduction (temperature, see [[Steady Conduction and Thermal Resistance Networks|Steady Conduction]]) and electrostatics (potential); torsion and laminar duct flow obey the same operator with a constant source term (Poisson).
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — $\phi$ plays the role of the node voltage, $\mathbf V=\nabla\phi$ is the current, and $\nabla\cdot\mathbf V=0$ is KCL.

## Quick Recall

> **In one line:** irrotational $\Leftrightarrow\nabla\times\mathbf V=0\Leftrightarrow\mathbf V=\nabla\phi$; with continuity, $\nabla^2\phi=0$.

**Formula / trigger:** $$\nabla\times\mathbf V=0,\qquad\nabla^2\phi=0,\qquad u=\phi_x=\psi_y,\ v=\phi_y=-\psi_x$$

**Remember:** shear flow is rotational; the free vortex is irrotational except at its axis.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
