---
tags: [fluid-mechanics, fundamentals]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Ideal Fluid

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

An **ideal fluid** is defined as a fluid with zero viscosity ($\mu=0$) — a hypothetical model, since every real fluid has $\mu>0$. It is the fluid-mechanics analogue of a "rigid body" or "massless spring" in mechanics: not physically real, but a useful limiting idealization that strips away one complicating effect (viscous shear resistance) so that other phenomena (pressure forces, inertia, potential flow) can be analyzed cleanly.

## Where the idealization is used

An ideal (inviscid) fluid cannot sustain any shear stress even while flowing (not just at rest, unlike a real fluid governed by [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Newton's Law of Viscosity]]). This dramatically simplifies the momentum equations — the [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]'s control-volume analysis, and the differential Navier-Stokes equations more generally, reduce to the (still nonlinear, but shear-free) Euler equations, the starting point for potential-flow theory.

## When the idealization is reasonable

Away from solid boundaries and in regions of the flow where velocity gradients are small, viscous shear stresses ($\tau=\mu\,du/dy$) are often negligible compared to pressure and inertial forces — this is the basis of boundary-layer theory (a topic listed in the course outline of [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Introduction|Introduction]] but not yet detailed in this vault): treat the bulk flow as ideal, and confine all viscous effects to a thin layer near solid surfaces.

## Related
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]
