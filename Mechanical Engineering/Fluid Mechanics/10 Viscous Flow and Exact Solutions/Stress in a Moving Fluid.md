---
tags: [concept, fluid-mechanics, viscous-flow, stress-tensor]
status: draft
aliases: [stress tensor, fluid stress, traction, viscous stress, normal and shear stress in fluids, Cauchy momentum equation]
up: "[[Fluid Mechanics - MOC]]"
---

# Stress in a Moving Fluid

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]], [[Motion of a Fluid Element|Motion of a Fluid Element]], [[Concept of Stress|Concept of Stress]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §4]]

## Core Idea

> **One-sentence definition:** the force per unit area that one part of a fluid exerts on a neighbouring part across a surface with unit normal $\mathbf n$ is the traction $\mathbf t=\boldsymbol\sigma\cdot\mathbf n$, where the stress tensor $\boldsymbol\sigma=-p\,\mathbf I+\boldsymbol\tau$ splits into an isotropic pressure and a viscous part that exists only when the fluid deforms.

**Intuition:** at rest a fluid can only push (pressure, the same on every plane). Once it flows, adjacent layers also drag each other along (shear stress) and can be stretched or squeezed (viscous normal stress). The tensor $\boldsymbol\sigma$ collects all of that in nine numbers.

## Governing Relations

**Traction on a surface with outward normal $\mathbf n$:**

$$\mathbf t(\mathbf n)=\boldsymbol\sigma\cdot\mathbf n,\qquad t_i=\sigma_{ij}n_j$$

**Decomposition:**

$$\boxed{\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}}\qquad\begin{pmatrix}\sigma_{xx}&\tau_{xy}&\tau_{xz}\\\tau_{yx}&\sigma_{yy}&\tau_{yz}\\\tau_{zx}&\tau_{zy}&\sigma_{zz}\end{pmatrix}$$

- First index = face (direction of its normal), second index = direction of the force.
- **At rest:** $\tau_{ij}=0$ and $\sigma_{ij}=-p\,\delta_{ij}$ (isotropic, equal on every plane).
- **Symmetry:** the moment balance on a small element gives $\tau_{xy}=\tau_{yx}$ etc. (6 independent components).
- **Mechanical pressure:** $\bar p=-\tfrac13\sigma_{kk}=p-\tfrac13\tau_{kk}$.

**Cauchy's equation of motion** (from Newton's law on an element, any continuum):

$$\boxed{\rho\frac{D\mathbf V}{Dt}=\rho\mathbf g+\nabla\cdot\boldsymbol\sigma=\rho\mathbf g-\nabla p+\nabla\cdot\boldsymbol\tau}$$

**Where:** $p$ = thermodynamic pressure; $\tau_{ij}$ = viscous stress tensor; $\delta_{ij}$ = Kronecker delta; $\mathbf n$ = unit normal; $\mathbf t(\mathbf n)$ is the force per area exerted **by the material on the side $\mathbf n$ points into, on the material behind the surface**. So for a wall, take $\mathbf n$ pointing from the wall into the fluid and $\mathbf t$ is the force of the fluid on the wall.

**Assumptions:** continuum, no distributed couples (so $\boldsymbol\sigma$ is symmetric).

## Visual

![[FM-N6-stress-element.png]]

**Figure:** the stress components on a 2-D element (red: normal, green: shear), together with the statement of the decomposition. Shear stresses on perpendicular faces pair up, $\tau_{xy}=\tau_{yx}$.

## When To Use

- Computing the **force on a wall or plate** from a known velocity field (pressure plus viscous shear).
- Writing the **momentum equation** in a general form before specialising the fluid law.
- Interpreting what a viscometer or pressure-drop measurement actually measures.

**Recognition pattern:** "find the force of the fluid on the plate / wall / body" or "write the stress on a plane with normal $\mathbf n$" → **$\mathbf t=\boldsymbol\sigma\cdot\mathbf n$**.

## Method

1. **Identify** the surface and its unit normal $\mathbf n$ (from the body on which you want the force, **into the fluid**: then $\mathbf t=\boldsymbol\sigma\cdot\mathbf n$ is the force of the fluid on the body).
2. **Choose** the stress components from the flow law ([[Newtonian Constitutive Relation|Newtonian relation]]).
3. **Apply** $\mathbf t=\boldsymbol\sigma\cdot\mathbf n$ and integrate over the area.
4. **Check:** pressure acts opposite to the outward normal (hence the $-p$), pairs of shear stresses are equal, and the results reduce to hydrostatics for $\boldsymbol\tau=0$.

## Derivation / Why It Works

Net surface force on an element: sum of tractions on its six faces. In the limit of a small element this is the **divergence** of the stress tensor, $\nabla\cdot\boldsymbol\sigma$ per unit volume. Newton's second law gives Cauchy's equation. A moment balance on the element, with no body couples, forces the off-diagonal components to match, making $\boldsymbol\sigma$ symmetric. The split into $-p\mathbf I+\boldsymbol\tau$ is a definition: $\boldsymbol\tau$ is whatever stress remains once the isotropic part is removed, and it is the part that needs a constitutive law.

## Common Traps

- **Trap:** a sign error in the traction on a wall.
  - **Why:** the traction $\boldsymbol\sigma\cdot\mathbf n$ flips sign when $\mathbf n$ flips; the pressure part $-p\,\mathbf n$ then pushes the wrong way and the shear drags the wrong way.
  - **Avoid it by:** choosing $\mathbf n$ pointing **from the wall into the fluid**; then $\mathbf t=\boldsymbol\sigma\cdot\mathbf n$ is the force the fluid exerts on the wall (pressure part $-p\,\mathbf n$ presses into the wall).
- **Trap:** treating $p$ as the mean normal stress for a compressible fluid with bulk viscosity (they differ by $\tfrac13\tau_{kk}$).
- **Trap:** counting nine independent components; symmetry leaves six.
- **Trap:** adding the viscous normal stress at a no-slip wall in simple unidirectional flow: it is zero there.

## Example

### Given
Plane Couette flow of oil ($\mu=0.1$ Pa·s) between a fixed lower plate and an upper plate moving at $U=2$ m/s, gap $h=2$ mm, uniform pressure $p$. Find the force per unit area on the lower plate.

### Approach
Velocity $u=Uy/h$, so $\tau_{yx}=\mu\,du/dy=\mu U/h$. The normal from the wall into the fluid is $\mathbf n=\hat{\mathbf y}$, and $\boldsymbol\sigma=\begin{pmatrix}-p&\tau\\\tau&-p\end{pmatrix}$.

### Solution
$$\mathbf t=\boldsymbol\sigma\cdot\hat{\mathbf y}=(\tau_{xy},\,-p)=\Big(\frac{\mu U}h,\ -p\Big)=(100\ \text{Pa},\ -p).$$

**Answer:** the fluid drags the lower plate forward with 100 Pa of shear stress and presses on it with $p$ (the minus sign means directed into the wall, $-\hat{\mathbf y}$).
**Key takeaway:** one tensor gives both the normal (pressure) and tangential (drag) force on any surface.

## Connections

### Prerequisites
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
- [[Concept of Stress|Concept of Stress]]
- [[Motion of a Fluid Element|Motion of a Fluid Element]]

### Related Concepts
- [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]] — the law for $\boldsymbol\tau$.
- [[Navier-Stokes Equations|Navier-Stokes Equations]] — Cauchy plus the constitutive law.
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

### Next
- [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]]

### Cross-domain links
- [[Plane Stress Transformation|Plane Stress Transformation]] and [[Mohr's Circle for Stress|Mohr's Circle for Stress]] — the stress tensor transforms identically in a fluid and a solid, so principal stresses and Mohr's circle apply to viscous stress too.
- [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — a fluid has the same Cauchy equation as a solid; only the constitutive law differs (stress vs strain **rate**).

## Quick Recall

> **In one line:** $\sigma_{ij}=-p\delta_{ij}+\tau_{ij}$; traction $\mathbf t=\boldsymbol\sigma\cdot\mathbf n$; $\rho D\mathbf V/Dt=\rho\mathbf g+\nabla\cdot\boldsymbol\sigma$.

**Formula / trigger:** $$\mathbf t=\boldsymbol\sigma\cdot\mathbf n,\qquad\boldsymbol\sigma=-p\mathbf I+\boldsymbol\tau,\ \tau_{ij}=\tau_{ji}$$

**Remember:** pressure is the isotropic part; $\boldsymbol\tau$ appears only when the fluid deforms.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
