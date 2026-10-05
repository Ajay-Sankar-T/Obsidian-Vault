---
tags: [fluid-mechanics, centroids, centre-of-mass]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Centre of Mass and Centroids

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · used by: [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces]], [[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy]]

## Discrete particles

$$\boxed{x_{CM}=\frac{\sum m_ix_i}{\sum m_i}},\quad \boxed{y_{CM}=\frac{\sum m_iy_i}{\sum m_i}},\quad \boxed{z_{CM}=\frac{\sum m_iz_i}{\sum m_i}}\qquad\text{vector: }\boxed{\mathbf r_{CM}=\frac{\sum m_i\mathbf r_i}{\sum m_i}}$$

## Continuous body

$$\boxed{\mathbf r_{CM}=\frac1M\int\mathbf r\,dm},\qquad \boxed{M=\int dm}$$

Components: $x_{CM}=\frac1M\int x\,dm$, and analogously for $y_{CM},z_{CM}$.

## Choosing $dm$

- Thin wire: $dm=\lambda\,dx$ (line density $\lambda$)
- Thin plate: $dm=\sigma\,dA$ (areal density $\sigma$)
- 3D solid: $dm=\rho\,dV$

For a **uniform** body, $dm\propto dV$ (or $dA$), so $\boxed{x_{CM}=\dfrac{\int x\,dV}{\int dV}}$ and $\boxed{\text{centre of mass}=\text{centroid}}$ — the two only coincide when density is uniform; for a non-uniform body (e.g. a ship's hull with concentrated machinery), the centre of gravity $G$ used in [[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies]] is generally **not** the geometric centroid of the hull's volume.

## Symmetry shortcut

If an object has a symmetry axis/plane, the COM lies on it:

- Uniform rod: $x_{CM}=L/2$
- Rectangle: $(x_{CM},y_{CM})=(b/2,h/2)$
- Circle/sphere/cylinder: geometric centre (along the axis, for a cylinder)
- Triangle: intersection of medians, at $h/3$ from the base (or $2h/3$ from the vertex)

## Related
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Composite Bodies and Cutouts|Composite Bodies and Cutouts]]
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]
