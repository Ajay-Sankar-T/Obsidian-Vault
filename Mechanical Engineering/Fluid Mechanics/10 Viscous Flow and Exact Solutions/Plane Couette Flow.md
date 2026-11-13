---
tags: [concept, fluid-mechanics, viscous-flow, exact-solution, couette]
status: draft
aliases: [Couette flow, plane Couette flow, shear-driven flow, journal bearing, viscometer, Couette-Poiseuille flow]
up: "[[Fluid Mechanics - MOC]]"
---

# Plane Couette Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Navier-Stokes Equations|Navier-Stokes Equations]], [[Boundary Conditions in Fluid Flow|Boundary Conditions]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §2]] · problems: [[Viscous Flow and Exact Solutions - Solved Problems|Solved Problems]]

## Core Idea

> **One-sentence definition:** plane Couette flow is the steady laminar flow between two parallel plates, one fixed and one moving at speed $U$, with no pressure gradient; the velocity profile is a straight line.

**Intuition:** the moving plate drags the adjacent fluid, and viscosity passes the drag from layer to layer. With nothing else acting, every layer must transmit the *same* shear stress, so the velocity gradient is constant: the profile is linear.

## Governing Relations

Geometry: plates at $y=0$ and $y=h$; lower plate fixed; upper plate at $u=U$.

**Navier–Stokes reduction** (steady, fully developed, $v=w=0$, $dp/dx=0$): $\ \mu\,\dfrac{d^2u}{dy^2}=0$.

$$\boxed{u(y)=U\frac yh},\qquad\tau=\mu\frac{du}{dy}=\frac{\mu U}h\ \text{(uniform)},\qquad q=\frac{Uh}{2}\ \text{(flow per unit width)},\qquad\bar u=\frac U2$$

**Couette + Poiseuille** (add a pressure gradient $dp/dx$):

$$u=\frac{U\,y}{h}+\frac{-dp/dx}{2\mu}\,y(h-y),\qquad q=\frac{Uh}{2}+\frac{-dp/dx\;h^3}{12\mu}$$

or in terms of $P=-\dfrac{dp}{dx}\dfrac{h^2}{2\mu U}$: $\ u/U=y/h+P\,(y/h)(1-y/h)$. Backflow near the fixed wall when $P<-1$ (adverse gradient).

**Journal bearing** (thin gap $h\ll$ radius $R$): unrolls into plane Couette flow with $U=\omega R$, plate length $2\pi R$.

**Where:** $\mu$ = viscosity; $h$ = gap; $U$ = plate speed; $q$ = volume flow per unit width.

**Assumptions:** laminar ($Re=\rho\bar uh/\mu<1400$ for plates), steady, fully developed (away from the ends), Newtonian, negligible viscous heating.

## Visual

![[FM-N1-laminar-profiles.png]]

**Figure:** left panel, the linear Couette profile; the middle and right panels show the two pressure-driven solutions (same ODE, different boundary conditions).

![[FM-N10-couette-poiseuille.png]]

**Figure:** the combined Couette–Poiseuille family: a favourable pressure gradient ($P>0$) bulges the profile forward; an adverse gradient ($P<-1$) reverses the flow at the stationary wall.

## When To Use

- **Viscometers** (rotating cylinder, cone-and-plate): shear stress against rate gives $\mu$.
- **Lubrication**: journal bearings, sliding pads, thin oil films.
- **Moving-wall problems** and wire or belt coating.
- Two-layer or multi-layer shear flows.

**Recognition pattern:** "plate moves at speed $U$ over a thin fluid layer", "oil film between sliding surfaces", "rotating shaft in a close-fitting sleeve" → **Couette flow**.

## Method

1. **Identify:** geometry, which wall moves, whether a pressure gradient acts.
2. **Choose** the ODE $\mu u''=dp/dx$ and the boundary conditions $u(0)=0$, $u(h)=U$.
3. **Apply:** integrate twice; $dp/dx=0$ gives $u=Uy/h$.
4. **Compute** $\tau=\mu U/h$, force $=\tau\times$ area, power $=F\,U$.
5. **Check:** the shear stress is uniform; check $Re$, and for a curved gap that $h\ll R$.

## Derivation / Why It Works

Force balance on a thin slab $dy$ in $x$: shear stress difference across the slab equals the pressure-gradient force, $d\tau/dy=dp/dx$. With $dp/dx=0$ the shear is constant, $\tau=c$, and Newton's law gives $du/dy=c/\mu$, so $u=cy/\mu$. The condition $u(h)=U$ gives $c=\mu U/h$. Equivalent statement: it is the Navier–Stokes $x$-equation $0=-\partial_xp+\mu\,\partial_y^2u$ with the symmetries applied.

## Common Traps

- **Trap:** using the moving-plate speed in a rotating bearing without the factor: $U=\omega R$, not $\omega D$.
- **Trap:** applying the thin-gap result when $h$ is not small compared with $R$ (then use the cylindrical solution).
- **Trap:** adding a pressure gradient and forgetting the Poiseuille term (or the backflow condition).
- **Trap:** ignoring viscous heating in thin films at high speed (the temperature rise can change $\mu$).

## Example

### Given
A journal bearing: shaft diameter 50 mm turning at 3000 rpm in a sleeve of length 40 mm, uniform clearance $h=0.1$ mm filled with oil, $\mu=0.05$ Pa·s. Find the drag torque and power.

### Approach
Thin gap, so use plane Couette flow with $U=\omega R$.

### Solution
$$\omega=3000\times\frac{2\pi}{60}=314.2\ \text{rad/s},\quad U=\omega R=7.854\ \text{m/s},$$
$$\tau=\frac{\mu U}{h}=\frac{0.05\times7.854}{10^{-4}}=3927\ \text{Pa},\quad F=\tau\,\pi DL=3927\times6.283\times10^{-3}=24.7\ \text{N},$$
$$T=FR=0.617\ \text{N·m},\qquad P=T\omega=194\ \text{W}.$$

**Answer:** 0.617 N·m of torque, 194 W dissipated as heat in the oil film.
**Key takeaway:** $\tau\propto1/h$: halving the clearance doubles the drag, and all of that power ends up as heat.

## Connections

### Prerequisites
- [[Navier-Stokes Equations|Navier-Stokes Equations]]
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]]
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

### Related Concepts
- [[Plane Poiseuille Flow|Plane Poiseuille Flow]] — add a pressure gradient.
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]
- [[Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]] — a viscometer is a Couette device.

### Next
- [[Plane Poiseuille Flow|Plane Poiseuille Flow]]

### Cross-domain links
- [[Torsion of Circular Shafts|Torsion of Circular Shafts]] — a Couette fluid layer between rotating cylinders is the viscous counterpart of a torsion member: $\tau=\mu\dot\gamma$ against $\tau=G\gamma$, and the torque is shear times area times radius in both.
- [[Steady Conduction and Thermal Resistance Networks|Steady Conduction and Thermal Resistance Networks]] — linear profile with uniform flux: velocity $\leftrightarrow$ temperature, $\tau\leftrightarrow$ heat flux, $\mu/h\leftrightarrow k/L$.

## Quick Recall

> **In one line:** a moving plate over a fixed one with no pressure gradient gives $u=Uy/h$ and a uniform shear stress $\tau=\mu U/h$.

**Formula / trigger:** $$u=U\frac yh,\quad\tau=\frac{\mu U}h,\quad q=\frac{Uh}2$$

**Remember:** linear profile, uniform stress; add $\frac{-dp/dx}{2\mu}y(h-y)$ for Couette–Poiseuille.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]
