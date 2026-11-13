---
tags: [concept, fluid-mechanics, kinematics, deformation]
status: draft
aliases: [fluid element motion, translation rotation deformation, strain rate, rate of strain tensor, dilatation, angular deformation]
up: "[[Fluid Mechanics - MOC]]"
---

# Motion of a Fluid Element

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Differential Continuity Equation|Differential Continuity Equation]], [[Material Derivative and Fluid Acceleration|Material Derivative]] · formulas: [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank §4]]

## Core Idea

> **One-sentence definition:** a small fluid element, over a short time, can only translate, rotate, stretch (linear deformation) and shear (angular deformation), and the velocity-gradient tensor splits exactly into a part for each.

**Intuition:** pick a small square of fluid and watch where its corners go. A uniform velocity just carries it away. Differences in velocity from corner to corner turn it, stretch or squeeze its sides, and change its right angles. Only the last two change its *shape*, and only those create viscous stress.

## Governing Relation

Velocity-gradient tensor, split into symmetric and antisymmetric parts:

$$\nabla\mathbf V=\underbrace{\tfrac12\big(\nabla\mathbf V+\nabla\mathbf V^{T}\big)}_{\dot{\boldsymbol\varepsilon}\ \text{(strain rate)}}+\underbrace{\tfrac12\big(\nabla\mathbf V-\nabla\mathbf V^{T}\big)}_{\text{rotation}}$$

| Motion | 2-D expression | Meaning |
|---|---|---|
| **Translation** | $(u,v)$ | element moves with the local velocity |
| **Linear deformation** | $\dot\varepsilon_{xx}=\dfrac{\partial u}{\partial x},\ \dot\varepsilon_{yy}=\dfrac{\partial v}{\partial y}$ | rate of stretch of a line along each axis |
| **Dilatation** (volume change) | $\nabla\cdot\mathbf V=\dot\varepsilon_{xx}+\dot\varepsilon_{yy}+\dot\varepsilon_{zz}$ | zero for incompressible flow |
| **Angular deformation** | $\dot\varepsilon_{xy}=\dfrac12\Big(\dfrac{\partial v}{\partial x}+\dfrac{\partial u}{\partial y}\Big)$, engineering $\dot\gamma_{xy}=2\dot\varepsilon_{xy}$ | rate at which a right angle closes |
| **Rotation** | $\omega_z=\dfrac12\Big(\dfrac{\partial v}{\partial x}-\dfrac{\partial u}{\partial y}\Big)$ | mean turning rate of two perpendicular lines |

Vector form: $\boldsymbol\omega=\tfrac12\nabla\times\mathbf V$ (vorticity is $\boldsymbol\zeta=2\boldsymbol\omega$).

**Newtonian link:** viscous shear stress is $\tau_{xy}=\mu\dot\gamma_{xy}$: **only deformation, never rotation, produces viscous stress** (see [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]]).

**Where:** $\dot\varepsilon_{ij}$ = rate-of-strain tensor (1/s); $\omega_z$ = angular velocity of the element (rad/s).

**Assumptions:** small element, short time, smooth velocity field.

## Visual

![[FM-K1-element-motion.png]]

**Figure:** the four elementary motions (dashed = at $t$, filled = at $t+dt$). Only angular deformation closes the right angle without turning the axes; rotation turns the element without distorting it.

![[FM-K2-shear-decomposition.png]]

**Figure:** simple shear $u=\dot\gamma y$ has **straight streamlines yet is rotational**: it equals a clockwise rotation $\omega_z=-\dot\gamma/2$ plus a pure strain $\dot\varepsilon_{xy}=\dot\gamma/2$.

## When To Use

- Computing **strain rates**, shear rates and dilatation from a velocity field.
- Deciding whether a flow is rotational ([[Vorticity and Circulation|Vorticity and Circulation]]).
- Building the Newtonian **stress** from the velocity field.

**Recognition pattern:** "rate of deformation", "angular velocity of a fluid element", "rate of change of volume", "shear strain rate" → **element motion**.

## Method

1. **Identify** the velocity components and their spatial derivatives.
2. **Choose** the quantity wanted: normal strain rates ($u_x,v_y,w_z$), shear strain rate (sum of cross derivatives), rotation (difference of cross derivatives).
3. **Apply** the formulas; take the symmetric combination for deformation and the antisymmetric for rotation.
4. **Check:** dilatation $=u_x+v_y+w_z$ must vanish for incompressible flow; a rigid-body rotation $u=-\Omega y,\ v=\Omega x$ has zero strain rate and $\omega_z=\Omega$.

## Derivation / Why It Works

Expand the velocity near the element centre: $\mathbf V(\mathbf x+d\mathbf x)=\mathbf V+\nabla\mathbf V\cdot d\mathbf x$. Every matrix is the sum of its symmetric and antisymmetric parts; the antisymmetric part acts on $d\mathbf x$ as $\boldsymbol\omega\times d\mathbf x$ (rigid rotation, no change of length), and the symmetric part changes lengths and angles. The sum of the trace gives the volume change rate $\nabla\cdot\mathbf V$.

## Common Traps

- **Trap:** equating "straight streamlines" with "no rotation".
  - **Why:** shear flow is rotational.
  - **Avoid it by:** computing $v_x-u_y$ explicitly.
- **Trap:** mixing the tensor shear strain rate $\dot\varepsilon_{xy}$ and the engineering one $\dot\gamma_{xy}=2\dot\varepsilon_{xy}$.
- **Trap:** using $\omega$ where vorticity $\zeta=2\omega$ is intended.
- **Trap:** attributing viscous stress to rotation.

## Example

### Given
The planar velocity field $u=3y,\ v=2x$ (in s⁻¹ units), and, separately, the stagnation flow $u=2x,\ v=-2y$.

### Solution
**Field 1:** $u_y=3,\ v_x=2$.
$$\omega_z=\tfrac12(v_x-u_y)=-0.5\ \text{rad/s},\quad\zeta_z=-1\ \text{s}^{-1},\quad\dot\gamma_{xy}=u_y+v_x=5\ \text{s}^{-1},\quad\nabla\cdot\mathbf V=0.$$

**Field 2:** $\dot\varepsilon_{xx}=2,\ \dot\varepsilon_{yy}=-2,\ \omega_z=0,\ \dot\gamma_{xy}=0,\ \nabla\cdot\mathbf V=0.$ The element is stretched in $x$, squeezed in $y$, area conserved, no rotation.

**Answer:** field 1 is rotational (clockwise) with shear rate 5 s⁻¹; field 2 is a pure strain with constant area.
**Key takeaway:** one velocity gradient can contain both rotation and deformation; separate them by symmetric and antisymmetric parts.

## Connections

### Prerequisites
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[Differential Continuity Equation|Differential Continuity Equation]]

### Related Concepts
- [[Vorticity and Circulation|Vorticity and Circulation]] — the rotation part.
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]]
- [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]] — the strain-rate part sets the stress.
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

### Next
- [[Stress in a Moving Fluid|Stress in a Moving Fluid]]

### Cross-domain links
- [[Strain Transformation and Rosettes|Strain Transformation and Rosettes]] and [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law]] — a solid's small strain tensor is the symmetric part of the displacement gradient; the fluid's strain **rate** is the symmetric part of the velocity gradient, with $\mu$ replacing $G$.
- [[Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]] — principal strain rates are eigenvalues of $\dot{\boldsymbol\varepsilon}$, as principal strains are for solids.

## Quick Recall

> **In one line:** $\nabla\mathbf V$ = strain rate (symmetric: stretch and shear) + rotation (antisymmetric); only the strain rate stresses a Newtonian fluid.

**Formula / trigger:** $$\omega_z=\tfrac12(v_x-u_y),\quad\dot\gamma_{xy}=u_y+v_x,\quad\nabla\cdot\mathbf V=u_x+v_y+w_z$$

**Remember:** shear flow rotates; rigid rotation does not deform.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
