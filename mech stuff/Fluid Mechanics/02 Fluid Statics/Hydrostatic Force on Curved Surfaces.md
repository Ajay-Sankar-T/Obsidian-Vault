---
tags: [fluid-mechanics, fluid-statics, curved-surfaces]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Hydrostatic Force on Curved Surfaces

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]

## Why $F=\rho gh_cA$ fails directly on a curved surface

$F_R=\rho gh_cA$ assumes every elemental pressure force $dF=p\,dA$ points in the **same direction** (perpendicular to a flat plane), so they can be summed as scalars. On a curved surface the normal direction changes from point to point, so the elemental forces must be summed as *vectors* — resolve into horizontal and vertical components and treat each separately.

## Horizontal component

Equal to the hydrostatic force on the **vertical projection** of the curved surface — i.e. treat the shadow the curved surface casts on a vertical plane as an ordinary plane surface and apply [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces]] directly to it:

$$\boxed{F_H=\gamma h_{CG}A_{\text{proj}}=\rho gh_{CG}A_{\text{proj}}}$$

**Memory:** horizontal force → vertical projection.

## Vertical component

Equal to the **weight of the (real or imaginary) fluid** directly above the curved surface, up to the free surface:

$$\boxed{F_V=\rho gV=\gamma V}$$

**Memory:** vertical force → weight of imaginary fluid. ($V$ is imaginary when the curved surface has fluid *below* it rather than above, e.g. a dam's downstream curve — the "imaginary" fluid volume above the surface up to the free-surface level is used regardless of whether real fluid actually occupies it, because pressure only depends on depth, per [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]].)

## Resultant

$$\boxed{F_R=\sqrt{F_H^2+F_V^2}},\qquad \boxed{\tan\alpha=\frac{F_V}{F_H}}$$

The line of action of $F_R$ passes through the point where $F_H$'s line of action (through the CP of the projected area) intersects $F_V$'s line of action (through the centroid of the pressure volume) — geometrically found, not by a single closed-form "CP of the curved surface" formula.

## Related
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]
- [[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]] (the vertical-component idea generalizes directly into buoyancy)


## Cross-domain links

- [[Cross-Domain Synthesis/Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — the same projected-area force balance gives hoop stress in a pressure vessel.
