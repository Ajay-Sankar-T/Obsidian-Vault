---
tags: [fluid-mechanics, kinematics]
up: "[[Fluid Mechanics - MOC]]"
---

# Lagrangian and Eulerian Descriptions

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Continuum Concept|Continuum Concept]]

## Lagrangian description

Follow individual fluid particles through space and time: $\mathbf x=\mathbf x(t)$ for each labeled particle. **Memory: Lagrangian = Follow.**

## Eulerian description

Observe the fluid at fixed locations in space, as a field: $\mathbf V=\mathbf V(x,y,z,t)$. **Memory: Eulerian = Observe.**

## Why fluid mechanics almost always uses Eulerian

Tracking every individual particle (Lagrangian) is natural for solid-body dynamics (a handful of rigid bodies) but impractical for a fluid continuum with effectively infinitely many "particles." The Eulerian field description is what makes the [[Continuum Concept|continuum]] assumption pay off: instead of tracking particles, define $\rho,\mathbf V,p$ as fields and write PDEs for them at fixed points.

## The two descriptions are not independent

Even working in the Eulerian frame, physical laws (Newton's second law, conservation of mass for a fixed set of matter) are stated most naturally for a **fixed body of material**, i.e. Lagrangian. The [[Material Derivative and Fluid Acceleration|material derivative]] is exactly the bridge: it computes "the rate of change following a particle" ($D/Dt$, Lagrangian) using only Eulerian field quantities and their spatial/temporal derivatives — never actually tracking any particle's trajectory. This same bridge — a "system" viewpoint (fixed matter) translated into a "field/region" viewpoint (fixed space) — reappears exactly as [[System and Control Volume|System and Control Volume]]'s distinction, one level up (an entire body of fluid, rather than a single particle).

## Related
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[System and Control Volume|System and Control Volume]]

## See also
- [[Streamlines, Pathlines, Streaklines and Timelines]] — a pathline is the Lagrangian picture of one particle.
