---
tags: [fluid-mechanics, fundamentals]
up: "[[Fluid Mechanics - MOC]]"
---

# Fluids and Solids

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]]

## The defining distinction

The line between a solid and a fluid is drawn by how each responds to a **shear (tangential) stress** in [[Static Equilibrium|static equilibrium]]:

**Solid:** can resist a tangential force while remaining in static equilibrium — it deforms a *finite* amount and (fully or partly) recovers its shape when the load is removed.

**Fluid:** cannot sustain any shear stress in static equilibrium — under any nonzero shear, it deforms *continuously* (it flows) for as long as the stress is applied, and generally does **not** recover its original shape when the load is removed. This is the "zero memory" behavior of an ordinary fluid, with the exception of viscoelastic fluids (see [[Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]) which retain some elastic memory of past deformation.

## Why this is *the* foundational definition

Every later topic in this vault traces back to this one distinction:
- [[Pressure and the Hydrostatic Equation|Fluid statics]] is possible as a subject at all only because a fluid at rest carries **no shear stress anywhere** — the entire stress state at a point reduces to a single scalar, pressure, acting equally in all directions (in stark contrast to the full stress tensor $[\sigma]$ needed for a solid — see [[Concept of Stress|Concept of Stress]] in the Strength of Materials vault, and the cross-domain note below).
- [[Viscosity and Newton's Law of Viscosity|Viscosity]] is precisely the *quantitative* version of "how does a fluid resist shear once it's moving" — a fluid can't resist shear statically, but it does resist the *rate* of shearing once flowing.

## Cross-domain: a fluid at rest is a degenerate solid

A useful way to unify this with [[Concept of Stress|Concept of Stress]]: a fluid's stress state, $[\sigma]=-p[I]$ (pressure acting equally in all directions, no off-diagonal shear terms), is the *isotropic special case* of the general stress tensor used throughout the Strength of Materials vault. [[Mohr's Circle for Stress|Mohr's Circle for Stress]] degenerates to a **single point** on the $\sigma$-axis at $\sigma=-p$ for a fluid at rest — there is no principal-stress problem to solve, because every direction is already principal (the circle has radius zero). This is exactly why hydrostatic pressure needs no "transformation equations": $F_R=\rho gh_cA$ in [[Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces]] doesn't care about the orientation of the surface's own coordinate axes, only its depth.

## Related
- [[Continuum Concept|Continuum Concept]]
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Concept of Stress|Concept of Stress (Strength of Materials)]]
