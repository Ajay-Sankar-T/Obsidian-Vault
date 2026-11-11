---
tags: [fluid-mechanics, fundamentals]
up: "[[Fluid Mechanics - MOC]]"
---

# Static Equilibrium (of a Fluid)

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]]

A fluid is in static equilibrium when every fluid particle is at rest (or moving with the same constant velocity as a rigid body) relative to the chosen reference frame — no relative motion between adjacent fluid layers.

## Why this condition is special for a fluid

Because a fluid cannot sustain shear stress while at rest (see [[Fluids and Solids|Fluids and Solids]]), static equilibrium forces the entire stress state down to a single scalar field, **pressure** $p(x,y,z)$, with no shear component anywhere. This is the starting assumption for the whole of [[Pressure and the Hydrostatic Equation|Fluid Statics]]: the only force a static fluid can exert on any surface (real or imaginary) is a normal (perpendicular) pressure force, $dF=p\,dA$, directed into the surface.

## Equilibrium of a fluid element

For a fluid element at rest under gravity, Newton's second law with zero acceleration reduces to a balance between the pressure-gradient force and the weight:

$$-\nabla p - \rho g\,\hat{k} = 0$$

which, expanded along the vertical direction, is exactly the hydrostatic equation $dP/dz=-\rho g$ derived in [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]. In the horizontal directions, $\partial p/\partial x=\partial p/\partial y=0$ — pressure in a static fluid under gravity depends **only** on depth, never on horizontal position, which is why every point at the same depth in a connected body of the same fluid has the same pressure (the rule used constantly in [[Manometers|Manometers]]).

## Related
- [[Fluids and Solids|Fluids and Solids]]
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
