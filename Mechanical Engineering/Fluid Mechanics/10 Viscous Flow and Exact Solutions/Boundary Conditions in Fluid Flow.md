---
tags: [concept, fluid-mechanics, viscous-flow, boundary-conditions]
status: draft
aliases: [no-slip condition, no-penetration, free surface condition, interface conditions, symmetry condition, slip]
up: "[[Fluid Mechanics - MOC]]"
---

# Boundary Conditions in Fluid Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Navier-Stokes Equations|Navier-Stokes Equations]] · next: [[Plane Couette Flow|Plane Couette Flow]]

## Core Idea

> **One-sentence definition:** a boundary condition states what the velocity (and stress) must be on the edge of the flow region; the differential equation alone cannot choose among its many solutions, the boundary conditions do.

**Intuition:** the Navier–Stokes ODE for a unidirectional flow, $\mu u''=dp/dx$, has a two-parameter family of solutions. Two conditions (one at each edge) fix them. Get the conditions wrong and the answer is wrong even if the algebra is perfect.

## Governing Relations

| Boundary | Condition | Statement |
|---|---|---|
| **Solid wall** | **no-slip** | fluid velocity equals wall velocity: $\mathbf V=\mathbf V_{\rm wall}$ (both tangential and normal) |
| Solid wall, impermeable | **no-penetration** | $\mathbf V\cdot\mathbf n=\mathbf V_{\rm wall}\cdot\mathbf n$ (all that survives for an inviscid fluid) |
| **Free surface** (liquid–gas) | zero shear | $\mu\,\partial u/\partial n=0$ (gas viscosity negligible) |
| Free surface | normal stress | $p=p_{\rm atm}-\sigma\,(1/R_1+1/R_2)$ (surface tension, see [[Surface Tension and Capillarity|Surface Tension]]) |
| **Fluid–fluid interface** | velocity continuous | $\mathbf V_1=\mathbf V_2$ |
| Fluid–fluid interface | shear stress continuous | $\mu_1\partial u_1/\partial n=\mu_2\partial u_2/\partial n$ |
| **Symmetry plane / axis** | no flux, no shear | $V_n=0,\ \partial V_t/\partial n=0$; on a pipe axis: $\partial u/\partial r=0$ (finite $u$) |
| Inlet / outlet | specified $\mathbf V$ or $p$ | profile, or pressure; periodic and far-field conditions for repeating or unbounded flows |

**Slip at small scales:** at Knudsen number $Kn\gtrsim0.01$ the no-slip condition fails and slip appears ([[Knudsen Number|Knudsen Number]]).

**Counting rule:** one condition per derivative order per direction: a second-order ODE (such as $\mu u''=dp/dx$) needs two.

**Where:** $\mathbf n$ = unit normal to the boundary; $\sigma$ = surface tension.

**Assumptions:** continuum; Newtonian fluid; the no-slip condition is an empirical fact, confirmed for ordinary liquids and gases at normal scales.

## Visual

Sketch the flow region and mark each boundary with its condition. For film flow down an incline: no-slip $u=0$ at the bed, zero shear $du/dy=0$ at the free surface; for a pipe: $u=0$ at $r=R$ and $du/dr=0$ at $r=0$.

## When To Use

- Whenever you **integrate a viscous flow ODE** (Couette, Poiseuille, film, annulus).
- Setting up **numerical simulations**.
- Interface problems (two immiscible liquids, droplets).

**Recognition pattern:** "wall moves at", "free surface", "two layers of different viscosity", "centreline" → **choose the boundary condition for each edge**.

## Method

1. **Identify** every boundary and what it is physically (wall, free surface, interface, axis, inlet).
2. **Choose** the matching condition from the table.
3. **Apply:** count conditions against the order of the equation; two for a second-order ODE.
4. **Check:** the solution satisfies each condition, and signs (moving-wall direction) are consistent.

## Derivation / Why It Works

*No-slip:* molecules adjacent to a wall exchange momentum with it frequently enough to share its velocity. *Free surface:* for air against water the viscosity is about 50 times smaller and the density roughly 1000 times smaller, so the gas cannot support a shear stress comparable to the liquid's: $\tau_{\rm liquid}\approx0$. *Interface:* a thin interface has no mass to accelerate, so the forces on it must balance: shear stress continuous, velocity continuous.

## Common Traps

- **Trap:** using no-slip on a free surface.
  - **Avoid it by:** zero shear there, $du/dy=0$, not $u=0$.
- **Trap:** requiring $u=0$ on the centreline of a pipe.
  - **Avoid it by:** symmetry: $du/dr=0$ and finite velocity.
- **Trap:** a wrong sign for a moving wall (direction relative to the axis).
- **Trap:** neglecting surface tension at very small scales, or using slip at ordinary scales.

## Example

### Given
Two immiscible layers between a fixed lower plate and an upper plate moving at $U=1$ m/s: lower layer $\mu_1=0.1$ Pa·s, $h_1=1$ mm; upper layer $\mu_2=0.01$ Pa·s, $h_2=1$ mm. Find the interface velocity and the shear stress.

### Approach
Each layer is a Couette flow with linear profile. Boundary conditions: $u=0$ at the lower plate, $u=U$ at the upper plate, and at the interface $u_1=u_2=u_i$ with continuous shear.

### Solution
Shear continuity: $\mu_1\dfrac{u_i}{h_1}=\mu_2\dfrac{U-u_i}{h_2}$, so
$$u_i=\frac{\mu_2h_1U}{\mu_1h_2+\mu_2h_1}=\frac{0.01\times1}{0.1+0.01}=0.0909\ \text{m/s},$$
$$\tau=\mu_1\frac{u_i}{h_1}=0.1\times\frac{0.0909}{0.001}=9.09\ \text{Pa}.$$

**Answer:** $u_i=0.091$ m/s and $\tau=9.09$ Pa throughout.
**Key takeaway:** the interface stays close to the speed of the plate that borders the **more viscous** layer ($u_i\approx0$ here); the low-viscosity layer takes almost all of the velocity change, like the large resistor in a series circuit taking most of the voltage.

## Connections

### Prerequisites
- [[Navier-Stokes Equations|Navier-Stokes Equations]]
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

### Related Concepts
- [[Plane Couette Flow|Plane Couette Flow]], [[Plane Poiseuille Flow|Plane Poiseuille Flow]], [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]
- [[Surface Tension and Capillarity|Surface Tension and Capillarity]]
- [[Ideal Fluid|Ideal Fluid]] — only no-penetration survives with $\mu=0$.
- [[Knudsen Number|Knudsen Number]]

### Next
- [[Plane Couette Flow|Plane Couette Flow]]

### Cross-domain links
- [[Steady Conduction and Thermal Resistance Networks|Steady Conduction and Thermal Resistance Networks]] — the two-layer Couette problem is identical to heat flow through two layers in series: shear stress $\leftrightarrow$ heat flux, velocity $\leftrightarrow$ temperature, $\mu/h\leftrightarrow k/L$, and continuity of $\tau$ at the interface $\leftrightarrow$ continuity of heat flux.
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — same series-resistance structure.

## Quick Recall

> **In one line:** no-slip at walls, zero shear at free surfaces, continuous velocity and shear at interfaces, symmetry at axes.

**Formula / trigger:** $$\mathbf V=\mathbf V_{\rm wall}\ \text{(wall)},\quad\mu\,\partial_nu=0\ \text{(free surface)},\quad\partial_nu=0\ \text{(symmetry)}$$

**Remember:** two conditions for a second-order ODE; $u=0$ is wrong on a free surface or centreline.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
