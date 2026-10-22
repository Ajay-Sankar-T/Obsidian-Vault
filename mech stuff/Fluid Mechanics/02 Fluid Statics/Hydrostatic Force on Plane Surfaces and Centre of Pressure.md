---
tags: [fluid-mechanics, fluid-statics, centre-of-pressure]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Hydrostatic Force on Plane Surfaces and Centre of Pressure

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]], [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]

## Resultant force on a submerged plane surface

Pressure force on an elemental area: $dF=p\,dA$. Integrating over the surface, and using $p_c=\rho gh_c=\gamma h_c$ at the centroid:

$$\boxed{F_R=p_cA=\rho gh_cA=\gamma h_cA}$$

where $h_c$ is the **vertical depth of the centroid** — the resultant force depends only on the centroid's depth and the total area, regardless of the surface's shape or orientation, because pressure varies linearly with depth and the linear terms average out to the centroid value.

## Centre of pressure (CP)

The resultant force does **not** act through the centroid — it acts through the centre of pressure, always *below* the centroid, because the pressure (and hence the "weighting") is larger on the deeper part of the surface:

**Vertical plane:**
$$\boxed{h_{CP}=h_c+\frac{I_G}{Ah_c}}\qquad\Longrightarrow\qquad h_{CP}>h_c$$

**Inclined plane** (angle $\theta$ from horizontal, $y$ measured along the plane):
$$\boxed{y_{CP}=y_c+\frac{I_G}{Ay_c}},\qquad h_c=y_c\sin\theta,\qquad h_{CP}=y_{CP}\sin\theta$$

$I_G$ is the second moment of area about the horizontal centroidal axis — see [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]] for standard shapes and for why this is the *same* $I_G$ used in beam bending.

## Worked pattern (vertical projected rectangular gate)

$b=50\ \text{ft}$, $h=24\ \text{ft}$: $A=bh=1200\ \text{ft}^2$, centroid depth $h_{CG}=12\ \text{ft}$, $I_{xx}=\tfrac1{12}(50)(24)^3$. Since the surface is vertical, $\theta=90°$, $\sin\theta=1$:

$$y_{CP,\text{proj}}=-\frac{I_{xx}\sin\theta}{h_{CG}A_{\text{proj}}}=-4\ \text{ft}\qquad\Longrightarrow\qquad h_{CP}=h_{CG}+4=16\ \text{ft}$$

CP sits 4 ft below the centroid, at 16 ft total depth.

## Related
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]]
- [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula (Strength of Materials) — the same $I_G$ integral used for bending stress]]
