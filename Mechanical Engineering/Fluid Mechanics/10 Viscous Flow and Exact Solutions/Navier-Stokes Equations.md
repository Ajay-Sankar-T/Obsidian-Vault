---
tags: [concept, fluid-mechanics, viscous-flow, navier-stokes]
status: draft
aliases: [Navier-Stokes, Navier–Stokes equations, N-S equations, incompressible Navier-Stokes, viscous momentum equation]
up: "[[Fluid Mechanics - MOC]]"
---

# Navier-Stokes Equations

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]], [[Stress in a Moving Fluid|Stress in a Moving Fluid]], [[Differential Continuity Equation|Differential Continuity Equation]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §1]]

## Core Idea

> **One-sentence definition:** the Navier–Stokes equations are Newton's second law for a Newtonian fluid element: $\rho\,D\mathbf V/Dt=-\nabla p+\rho\mathbf g+\mu\nabla^2\mathbf V$, solved together with continuity $\nabla\cdot\mathbf V=0$.

**Intuition:** compared with Euler's equation there is one new force, viscous diffusion $\mu\nabla^2\mathbf V$: it smooths out velocity differences, spreading momentum from fast layers to slow ones. The nonlinear convective term $(\mathbf V\cdot\nabla)\mathbf V$ is what makes the equations hard.

## Governing Relations

For **incompressible** flow with **constant viscosity**:

$$\boxed{\rho\Big[\frac{\partial\mathbf V}{\partial t}+(\mathbf V\cdot\nabla)\mathbf V\Big]=-\nabla p+\rho\mathbf g+\mu\nabla^2\mathbf V},\qquad\nabla\cdot\mathbf V=0$$

Cartesian $x$-component:

$$\rho\Big(\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}+w\frac{\partial u}{\partial z}\Big)=-\frac{\partial p}{\partial x}+\rho g_x+\mu\Big(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+\frac{\partial^2u}{\partial z^2}\Big)$$

Cylindrical $z$-component (used for pipes, annuli):

$$\rho\Big(\frac{\partial v_z}{\partial t}+v_r\frac{\partial v_z}{\partial r}+\frac{v_\theta}r\frac{\partial v_z}{\partial\theta}+v_z\frac{\partial v_z}{\partial z}\Big)=-\frac{\partial p}{\partial z}+\rho g_z+\mu\Big[\frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial v_z}{\partial r}\Big)+\frac1{r^2}\frac{\partial^2v_z}{\partial\theta^2}+\frac{\partial^2v_z}{\partial z^2}\Big]$$

**Terms:**

| Term | Name | Meaning |
|---|---|---|
| $\rho\,\partial\mathbf V/\partial t$ | local inertia | unsteadiness |
| $\rho(\mathbf V\cdot\nabla)\mathbf V$ | convective inertia | **nonlinear**; steady acceleration through a varying field |
| $-\nabla p$ | pressure gradient | drives fluid to low pressure |
| $\rho\mathbf g$ | body force | gravity |
| $\mu\nabla^2\mathbf V$ | viscous diffusion | momentum spreading by shear |

**Modified pressure:** with $P=p+\rho gz$ ($z$ up) gravity disappears: $\rho\,D\mathbf V/Dt=-\nabla P+\mu\nabla^2\mathbf V$.

**Vorticity form (2-D):** $\dfrac{D\zeta}{Dt}=\nu\nabla^2\zeta$, where $\nu=\mu/\rho$: vorticity is advected and diffused, never created in the interior of an incompressible 2-D flow.

**Where:** $\nu=\mu/\rho$ = kinematic viscosity; $P$ = piezometric pressure.

**Assumptions:** continuum, Newtonian, incompressible, constant $\mu$. (The general form keeps $\nabla\cdot\boldsymbol\tau$ and a variable $\mu$.)

## Visual

No picture replaces the plane-flow reduction that follows: for $u=u(y)$ with steady, fully developed flow, every term but pressure gradient and viscous diffusion vanishes. The profile figure in [[Plane Couette Flow|Plane Couette]] and [[Hagen-Poiseuille Flow|Hagen–Poiseuille]] flows shows the result.

## When To Use

- To **derive** every exact viscous solution (Couette, Poiseuille, Hagen–Poiseuille, film flow).
- To **scale** the physics ([[Nondimensionalisation and the Reynolds Number|Reynolds number]], boundary layers).
- As the starting point of CFD.

**Recognition pattern:** "viscous flow", "find the velocity profile", "fully developed laminar flow", "derive from Navier–Stokes" → **N–S with the symmetries applied**.

## Method

1. **Identify** the symmetries: steady ($\partial_t=0$), fully developed ($\partial_x=0$), unidirectional ($v=w=0$), axisymmetric ($\partial_\theta=0$).
2. **Choose** the coordinate system that matches the boundaries.
3. **Apply:** continuity first (it fixes which components vanish), then the cross-stream momentum equations (pressure is hydrostatic across the flow), then the streamwise one reduces to an **ODE**.
4. **Integrate** twice and apply two boundary conditions ([[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]]).
5. **Check:** units, limiting cases, and the dimensionless form's $Re$.

## Derivation / Why It Works

Insert the Newtonian law into Cauchy's equation $\rho D\mathbf V/Dt=\rho\mathbf g-\nabla p+\nabla\cdot\boldsymbol\tau$. With $\tau_{ij}=\mu(\partial_ju_i+\partial_iu_j)$ and $\mu$ constant:
$$\partial_j\tau_{ij}=\mu\,\partial_j\partial_ju_i+\mu\,\partial_i(\partial_ju_j)=\mu\nabla^2u_i+\mu\,\partial_i(\nabla\cdot\mathbf V),$$
and the last term vanishes for incompressible flow, leaving $\mu\nabla^2\mathbf V$.

**Counting.** Four unknowns $(u,v,w,p)$, four equations (continuity and three momentum): the system is closed. The nonlinearity means there are very few exact solutions; those that exist have $(\mathbf V\cdot\nabla)\mathbf V\equiv0$ (unidirectional flows).

**Euler limit.** For $\mu\to0$ the equations reduce to Euler's but the highest derivative disappears, so the no-slip condition cannot be met: a thin **boundary layer** forms ([[Convection Fundamentals - Boundary Layers and Scale Analysis|Convection Fundamentals]]).

## Common Traps

- **Trap:** keeping $\mu\nabla^2\mathbf V$ in a flow with variable viscosity.
  - **Avoid it by:** writing $\nabla\cdot\boldsymbol\tau$ in full.
- **Trap:** forgetting the cross-stream momentum equation (it gives hydrostatic pressure across a unidirectional flow).
- **Trap:** keeping the convective term in a fully developed unidirectional flow (it vanishes since $\partial u/\partial x=0$).
- **Trap:** using the cylindrical form with the Cartesian Laplacian (the $\frac1r\partial_r(r\partial_r)$ structure matters).

## Example

### Given
Verify that plane Couette flow $u=Uy/h$, $v=w=0$ satisfies Navier–Stokes with no pressure gradient.

### Solution
Continuity: $\partial u/\partial x=0$ ✓. $y$ and $z$ momentum: pressure is hydrostatic. $x$-momentum: steady and $\partial_x=0$ so the convective term is zero, and
$$0=-\frac{\partial p}{\partial x}+\mu\frac{d^2u}{dy^2}=-\frac{\partial p}{\partial x}+0,$$
so $\partial p/\partial x=0$ ✓.

**Answer:** the linear profile is an exact solution with uniform pressure.
**Key takeaway:** a unidirectional flow turns the nonlinear PDE into a linear ODE, $\mu u''=dp/dx$.

## Connections

### Prerequisites
- [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]]
- [[Stress in a Moving Fluid|Stress in a Moving Fluid]]
- [[Differential Continuity Equation|Differential Continuity Equation]]
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]

### Related Concepts
- [[Euler's Equations of Fluid Motion|Euler's Equations of Fluid Motion]] — the $\mu=0$ limit.
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]]
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]]

### Next
- [[Plane Couette Flow|Plane Couette Flow]], [[Plane Poiseuille Flow|Plane Poiseuille Flow]], [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]

### Cross-domain links
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay]] — the vorticity equation $D\zeta/Dt=\nu\nabla^2\zeta$ is a diffusion equation, the same as heat conduction $\partial T/\partial t=\alpha\nabla^2T$; $\nu$ is the diffusivity of momentum ($\nu/\alpha=Pr$).
- [[Heat Transfer - MOC|Heat Transfer — MOC]] — convection–diffusion structure shared by $\mathbf V$, $T$ and concentration.

## Quick Recall

> **In one line:** $\rho\,D\mathbf V/Dt=-\nabla p+\rho\mathbf g+\mu\nabla^2\mathbf V$ with $\nabla\cdot\mathbf V=0$: inertia = pressure + gravity + viscous diffusion.

**Formula / trigger:** $$\rho\frac{D\mathbf V}{Dt}=-\nabla p+\rho\mathbf g+\mu\nabla^2\mathbf V$$

**Remember:** unidirectional flow kills the nonlinear term; the result is $\mu u''=dp/dx$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** advanced
- **Subjects:** [[Fluid Mechanics - MOC]]
