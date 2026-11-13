---
tags: [concept, fluid-mechanics, viscous-flow, reynolds-number, scaling]
status: draft
aliases: [Reynolds number, nondimensionalization, non-dimensional Navier-Stokes, scaling of Navier-Stokes, Stokes flow, creeping flow, boundary layer thickness]
up: "[[Fluid Mechanics - MOC]]"
---

# Nondimensionalisation and the Reynolds Number

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Navier-Stokes Equations|Navier-Stokes Equations]], [[Important Dimensionless Groups|Important Dimensionless Groups]] · formulas: [[Dimensional Analysis and Similitude - Formula Bank|Similitude Formula Bank §6]]

## Core Idea

> **One-sentence definition:** scaling the Navier–Stokes equations with a length $L$ and speed $U$ shows that the ratio of inertial to viscous forces, the Reynolds number $Re=\rho UL/\mu$, is the single parameter (with Froude and Strouhal) that controls the flow.

**Intuition:** the equations have six dimensional quantities, but once you measure lengths in units of $L$ and speeds in units of $U$, only one coefficient is left in front of the viscous term: $1/Re$. Large $Re$: viscosity is a thin correction (boundary layers). Small $Re$: inertia is negligible (creeping flow).

## Governing Relations

Define $x^*=x/L$, $\mathbf V^*=\mathbf V/U$, $t^*=tU/L$, $p^*=(p-p_\infty)/(\rho U^2)$. The incompressible Navier–Stokes equation becomes

$$\boxed{\frac{\partial\mathbf V^*}{\partial t^*}+(\mathbf V^*\cdot\nabla^*)\mathbf V^*=-\nabla^*p^*-\frac1{Fr}\hat{\mathbf k}+\frac1{Re}\nabla^{*2}\mathbf V^*},\qquad\nabla^*\cdot\mathbf V^*=0$$

with $Re=\dfrac{\rho UL}{\mu}=\dfrac{UL}{\nu}$ and $Fr=\dfrac{U^2}{gL}$. If the flow oscillates at frequency $\omega$ use $t^*=\omega t$ and a coefficient $St=\omega L/U$ in front of the time derivative.

**Meaning of $Re$** (three equivalent readings):

$$Re=\frac{\rho U^2/L}{\mu U/L^2}=\frac{\text{inertial force}}{\text{viscous force}}=\frac{L^2/\nu}{L/U}=\frac{\text{diffusion time}}{\text{convection time}}$$

**Limits:**

| Regime | Condition | Result |
|---|---|---|
| **Creeping (Stokes) flow** | $Re\ll1$ | pressure scale $\mu U/L$; $\ 0=-\nabla p+\mu\nabla^2\mathbf V$, linear, reversible |
| **Laminar, viscous-dominated** | $Re\sim1$–$10^3$ | full equation; exact solutions where unidirectional |
| **High-$Re$** | $Re\gg1$ | inviscid outer flow plus thin **boundary layer**, thickness $\delta/L\sim Re^{-1/2}$ (laminar) |
| **Turbulence** | above critical $Re$ | instabilities grow; see [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] |

**Boundary-layer estimate:** balance inertia $U^2/L$ with viscous diffusion $\nu U/\delta^2$: $\delta/L\sim(\nu/UL)^{1/2}=Re^{-1/2}$. For a flat plate the Blasius result is $\delta\approx5x/\sqrt{Re_x}$ (laminar).

**Typical values:**

| Flow | $Re$ |
|---|---|
| swimming bacterium | $10^{-5}$–$10^{-4}$ |
| person walking in air (0.5 m, 1.5 m/s) | $5\times10^4$ |
| water in a 25 mm pipe at 2 m/s | $5\times10^4$ |
| airliner wing (5 m chord, 250 m/s) | $8\times10^7$ |
| ship hull (100 m, 10 m/s) | $10^9$ |

**Where:** $L,U$ = characteristic length and speed; $\nu=\mu/\rho$.

**Assumptions:** incompressible, constant properties; the choice of $L,U$ is a convention and must be stated (pipe diameter against radius, mean against maximum velocity).

## Visual

![[FM-D1-scaling.png]]

**Figure:** the same scaling argument applied to a model: matching $Re$ and $Fr$ simultaneously needs $\nu_m/\nu_p=\alpha^{3/2}$, which is why the groups cannot all be matched at reduced scale ([[Flow Similarity and Model Studies|Flow Similarity]]).

## When To Use

- Deciding which terms in Navier–Stokes can be **neglected** (inertia at low $Re$, viscosity outside boundary layers).
- Setting up **model tests**: which groups to match.
- Estimating **boundary-layer thickness**, entry length, or transition.

**Recognition pattern:** "which term dominates", "very slow viscous flow", "thin layer near the wall", "dynamic similarity" → **scale the equations, find $Re$**.

## Method

1. **Identify** characteristic $L$, $U$ (and $\omega$ if unsteady) from the geometry and the flow.
2. **Choose** the pressure scale: $\rho U^2$ for high $Re$, $\mu U/L$ for low $Re$.
3. **Apply:** divide every term; read off the coefficients $St$, $1/Fr$, $1/Re$.
4. **Check:** drop terms with a small coefficient only if the neglected term does not control the *boundary conditions* (dropping the viscous term at high $Re$ removes the ability to impose no-slip: a boundary layer fixes that).

## Derivation / Why It Works

Substitute the scaled variables into $\rho(\partial_t\mathbf V+\mathbf V\cdot\nabla\mathbf V)=-\nabla p+\rho\mathbf g+\mu\nabla^2\mathbf V$. Each term acquires a dimensional factor: inertia $\rho U^2/L$, pressure $\rho U^2/L$, gravity $\rho g$, viscous $\mu U/L^2$. Divide by $\rho U^2/L$: inertia and pressure get coefficient 1, gravity $gL/U^2=1/Fr$ and viscous $\mu/(\rho UL)=1/Re$. Since the scaled equation and boundary conditions contain only $Re$, $Fr$ and the scaled geometry, the scaled solution depends only on those: precisely the statement of the [[Buckingham Pi Theorem|Π theorem]], derived from the physics.

## Common Traps

- **Trap:** quoting $Re$ without saying what $L$ and $U$ are.
  - **Avoid it by:** stating them (pipe: mean velocity and diameter, $Re_D=VD/\nu$).
- **Trap:** dropping $1/Re$ completely at high $Re$ and then trying to apply no-slip.
- **Trap:** using $\rho U^2$ as the pressure scale at $Re\ll1$ (the pressure then scales as $\mu U/L$).
- **Trap:** reading critical $Re$ values as exact thresholds.

## Example

### Given
Air ($\nu=1.5\times10^{-5}$ m²/s) flows at $U=3$ m/s over a flat plate. Find the Reynolds number at $x=0.5$ m and the laminar boundary-layer thickness there.

### Solution
$$Re_x=\frac{Ux}{\nu}=\frac{3(0.5)}{1.5\times10^{-5}}=10^5,\qquad\delta\approx\frac{5x}{\sqrt{Re_x}}=\frac{5(0.5)}{316}=7.9\ \text{mm}.$$

**Answer:** $Re_x=10^5$ (laminar, below the usual $5\times10^5$ transition) and $\delta\approx7.9$ mm, which is $\delta/x=1.6\%$: thin, as the $Re^{-1/2}$ scaling predicts.
**Key takeaway:** at high $Re$ the viscous effect is confined to a layer of thickness $\sim L/\sqrt{Re}$; outside it the flow is nearly inviscid.

## Connections

### Prerequisites
- [[Navier-Stokes Equations|Navier-Stokes Equations]]
- [[Buckingham Pi Theorem|Buckingham π Theorem]]

### Related Concepts
- [[Important Dimensionless Groups|Important Dimensionless Groups]]
- [[Flow Similarity and Model Studies|Flow Similarity and Model Studies]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]
- [[Euler's Equations of Fluid Motion|Euler's Equations]] — the $Re\to\infty$ limit.
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

### Next
- [[Plane Couette Flow|Plane Couette Flow]], [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]

### Cross-domain links
- [[Convection Fundamentals - Boundary Layers and Scale Analysis|Convection Fundamentals — Boundary Layers and Scale Analysis]] — the same scale analysis gives $\delta_T/\delta\sim Pr^{-1/2}$ and the Nusselt number.
- [[The Universal Second-Order Linear System|The Universal Second-Order Linear System]] — $1/Re$ plays the role of the damping ratio: the ratio of the dissipative to the inertial term.

## Quick Recall

> **In one line:** scaling Navier–Stokes leaves $1/Re$ in front of the viscous term; $Re=\rho UL/\mu$ is inertia over viscosity.

**Formula / trigger:** $$Re=\frac{\rho UL}{\mu},\qquad\frac{D\mathbf V^*}{Dt^*}=-\nabla^*p^*+\frac1{Re}\nabla^{*2}\mathbf V^*,\qquad\frac\delta L\sim Re^{-1/2}$$

**Remember:** low $Re$ = Stokes flow, high $Re$ = boundary layer, always state $L$ and $U$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
