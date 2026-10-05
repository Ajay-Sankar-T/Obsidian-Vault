---
tags: [fluid-mechanics, fluid-statics, buoyancy]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Buoyancy and Archimedes' Principle

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]]

## Archimedes' principle

$$\boxed{F_B=\rho_f gV_D}$$

$\rho_f$ — fluid density, $V_D$ — volume of fluid displaced by the submerged (or partially submerged) body.

$$\boxed{\text{Buoyant force}=\text{weight of displaced fluid}}$$

This is exactly the vertical-force result from [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]] applied to a *closed* curved surface (the whole body): summing the vertical pressure-force components over every point on a closed surface leaves only the net difference between the (larger) upward pressure on the bottom and the (smaller) downward pressure on the top — precisely the weight of the fluid that would otherwise occupy that volume. The buoyant force acts through the **centre of buoyancy** $B$, the centroid of the *displaced volume* (not necessarily the centroid of the body itself, if the body has non-uniform density).

## Submerged body — stability of orientation

| Condition | Behaviour |
|---|---|
| $B$ above $G$ | stable |
| $G$ above $B$ | unstable |
| $G=B$ | neutral |

And for whether it sinks, rises, or hovers: $\rho_{\rm body}>\rho_f\Rightarrow$ sinks; $\rho_{\rm body}<\rho_f\Rightarrow$ rises; $\rho_{\rm body}=\rho_f\Rightarrow$ neutral buoyancy.

## Floating body — equilibrium condition

$$\boxed{W=F_B}\qquad\Longrightarrow\qquad W=\rho_fgV_D$$

If the body's own (average) density is $\rho_B$: $\rho_BgV=\rho_fgV_D$, so

$$\boxed{\frac{V_D}{V}=\frac{\rho_B}{\rho_f}}$$

the **fraction of the body submerged** — this is why an iceberg (density $\approx0.92\rho_{\rm water}$) floats with about 92% of its volume underwater.

## Related
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]]
- [[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies — Metacentre]] (the "$B$ above $G$" stability rule above is only the *first-order* story — floating-body stability needs the full metacentre analysis, since a floating body's $B$ moves when it tilts, unlike a fully submerged body's)
