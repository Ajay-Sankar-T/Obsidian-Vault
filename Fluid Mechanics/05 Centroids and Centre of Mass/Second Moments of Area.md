---
tags: [fluid-mechanics, centroids, second-moment-of-area]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Second Moments of Area

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · used by: [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]], [[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies]]

## Definition

$$I_G = \int y^2\,dA$$

about a centroidal axis — exactly the same quantity used throughout [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula]] in the Strength of Materials vault. This is not a coincidence of notation: both the flexure formula $\sigma=-My/I$ and the fluid-statics center-of-pressure formula below arise from the identical mathematical operation — integrating a *linearly varying* quantity ($y$, or depth-proportional pressure) times a moment arm ($y$ again) over an area.

## Standard values (identical table to the Strength of Materials vault)

**Rectangle** (breadth $b$, height $h$, about centroidal axis parallel to $b$): $I_G=\dfrac{bh^3}{12}$

**Circle** (diameter $D$, about a centroidal diameter): $I_G=\dfrac{\pi D^4}{64}=\dfrac{\pi R^4}{4}$

**Parallel axis theorem** (needed whenever the reference axis isn't through the centroid, e.g. shifted to the free surface for [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Centre of Pressure]] problems): $I=I_G+Ad^2$, where $d$ is the distance between the two parallel axes.

## Two unrelated-looking uses of the same integral

1. **Centre of pressure** (fluid statics): $h_{CP}=h_c+\dfrac{I_G}{Ah_c}$ — the "extra depth" the resultant hydrostatic force acts at, below the centroid, because pressure increases with depth so the lower part of the surface is weighted more heavily.
2. **Bending stress** (solid mechanics, [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula]]): $\sigma=-My/I$ — the stress at height $y$ from the neutral axis, because bending strain increases linearly with $y$ so the outer fibres are weighted more heavily.

Both formulas are, structurally, "first moment of a linearly-varying load, normalized by area and by the linear coefficient" — see [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]] for the full derivation showing $I_G$ appears for exactly the same reason in each.

## Waterplane second moment (a third use, in stability)

[[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies — Metacentre]] uses $I_O$, the second moment of the **waterplane area** (the horizontal cross-section at the waterline), not a cross-sectional area — a different physical surface, same mathematical object. For a rectangular waterplane $L\times b$: tilting about the longitudinal axis uses $I_O=Lb^3/12$; tilting about the transverse axis uses $I_O=bL^3/12$. **Memory:** the dimension *perpendicular* to the tilt axis gets cubed — identical rule to which dimension gets cubed in the beam-bending $I_G=bh^3/12$ table.

## Related
- [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula (Strength of Materials)]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]
- [[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies — Metacentre]]
