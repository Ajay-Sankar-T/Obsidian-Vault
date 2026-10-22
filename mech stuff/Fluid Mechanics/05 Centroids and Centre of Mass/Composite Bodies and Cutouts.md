---
tags: [fluid-mechanics, centroids]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Composite Bodies and Cutouts

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/05 Centroids and Centre of Mass/Centre of Mass and Centroids|Centre of Mass and Centroids]]

## Composite objects

Break the object into simple shapes with known individual centroids. For each part $i$, find its mass (or, for uniform density, its area/volume) $m_i$ and centroid coordinates $x_i,y_i$, then:

$$\boxed{x_{CM}=\frac{\sum m_ix_i}{\sum m_i}},\qquad \boxed{y_{CM}=\frac{\sum m_iy_i}{\sum m_i}}$$

For uniform density, areas/volumes substitute directly for masses: $\boxed{x_C=\dfrac{\sum A_ix_i}{\sum A_i}}$ (2D) or $\boxed{x_C=\dfrac{\sum V_ix_i}{\sum V_i}}$ (3D).

## Holes and cutouts

Treat a hole as a **negative** area/volume: $\boxed{A_{\rm hole}<0}$, then apply the same weighted-average formula $x_C=\dfrac{\sum A_ix_i}{\sum A_i}$ unchanged — extremely useful for plates with circular or rectangular cutouts, since it avoids re-deriving the centroid formula for the resulting irregular shape from scratch.

## Cross-domain: this is superposition, again

Composite-body centroids and hole subtraction are a direct instance of the same **linear superposition** principle used throughout [[Strength of materials/05 Bending Stresses/Unsymmetric and Combined Bending|Unsymmetric and Combined Bending]] (superposing stress states) and [[07 AC Circuit Analysis and Network Theorems|AC network superposition]] (superposing circuit responses): break a complicated linear problem into simple pieces whose individual answers are known, then add them with the correct sign (a hole subtracts, exactly as a "negative source" would in electrical superposition of two sources with opposite polarity). See [[Cross-Domain Synthesis/Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay — Time Constants, Damping and Spatial Relaxation]]'s closing point that linearity is *why* superposition works at all, across every one of these domains.

## Related
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Centre of Mass and Centroids|Centre of Mass and Centroids]]
- [[Strength of materials/05 Bending Stresses/Unsymmetric and Combined Bending|Unsymmetric and Combined Bending (Strength of Materials) — the same superposition idea]]
