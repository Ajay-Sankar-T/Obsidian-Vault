Related: [[Flexure Formula]] · [[Axial Deformation]] · [[Plane Stress Transformation]]

## Unsymmetric Bending (Bending About a Non-Principal Axis, or Biaxial Bending)

If a beam is bent by moments $M_z$ and $M_y$ about both centroidal axes simultaneously (e.g. a beam loaded off the plane of symmetry), and the section has centroidal principal axes $y,z$ (products of inertia $I_{yz}=0$), the stress at a point $(y,z)$ superposes both effects:
$$\sigma(y,z) = -\frac{M_z\,y}{I_z} + \frac{M_y\,z}{I_y}$$
(sign conventions vary; the key idea is **linear superposition of two single-axis flexure formulas**, each exactly like [[Flexure Formula]]).

The **neutral axis** in unsymmetric bending is generally **not** aligned with either the load direction or a principal axis — it's the line where $\sigma=0$, found by setting the combined expression to zero. If the section's principal axes aren't known (product of inertia $I_{yz}\ne0$), the general (unsymmetric) flexure formula requires the full inertia tensor; it's usually simpler to first rotate to principal axes (an eigenvalue problem, exactly analogous to the principal-stress calculation in [[Plane Stress Transformation]]).

## Combined Axial Load and Bending (Eccentric Loading)

A load $P$ applied off-center (eccentricity $e$ from the centroid) is statically equivalent to a centroidal axial force $P$ plus a moment $M=Pe$. By superposition:
$$\sigma(y) = \frac{P}{A} \pm \frac{My}{I} = \frac{P}{A}\pm\frac{Pey}{I}$$
This combines [[Axial Deformation]]'s uniform stress with [[Flexure Formula]]'s linear bending stress. The **kern** (core) of a section is the region within which an eccentric load produces no tensile stress anywhere on the section — important for masonry/concrete design where tension isn't permitted.

## General Combined Loading

For a member simultaneously subject to axial force $N$, bending moments $M_y,M_z$, and (for a shaft) torque $T$, the normal stress at a point superposes the axial and bending contributions, while shear stress superposes the torsional ([[Torsion of Circular Shafts]]) and transverse-shear ([[Shear Stress Formula for Beams]]) contributions. The resulting combined stress state at a point is then analyzed using [[Plane Stress Transformation]] to find principal stresses and the maximum shear stress governing failure.

---
Next: [[Shear Stress Formula for Beams]]
