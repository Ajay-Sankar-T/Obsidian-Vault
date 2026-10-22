Related: [[Strength of Materials - MOC]]

## Normal and Shear Stress

For a member carrying an internal force $F$ distributed over a cross-sectional area $A$, the **average stress** is
$$\sigma = \frac{P}{A} \quad \text{(normal stress, force} \perp \text{area)}, \qquad \tau = \frac{V}{A} \quad \text{(shear stress, force} \parallel \text{area)}$$

At a point, stress is defined as the limit of force per unit area as the area shrinks to a point:
$$\sigma = \lim_{\Delta A\to0}\frac{\Delta F_n}{\Delta A}, \qquad \tau = \lim_{\Delta A\to0}\frac{\Delta F_t}{\Delta A}$$

Units: Pa (N/m²), commonly MPa (N/mm²) in engineering practice.

## The Stress Tensor (General State of Stress)

At a point in a 3D body, the complete stress state requires 9 components (6 independent, by moment equilibrium $\tau_{xy}=\tau_{yx}$, etc.):
$$[\sigma] = \begin{pmatrix}\sigma_{xx} & \tau_{xy} & \tau_{xz}\\ \tau_{yx} & \sigma_{yy} & \tau_{yz}\\ \tau_{zx} & \tau_{zy} & \sigma_{zz}\end{pmatrix}$$

**Plane stress** (thin plates, beam surfaces, etc.) reduces this to three independent components $\sigma_x,\sigma_y,\tau_{xy}$ — see [[Plane Stress Transformation]].

## Sign Convention

- Tensile normal stress: positive.
- Compressive normal stress: negative.
- Shear stress: positive on a positive face pointing in the positive coordinate direction (right-hand rule consistent with the pair $\tau_{xy}=\tau_{yx}$).

## Equilibrium and Free-Body Diagrams

Internal stress resultants (axial force $N$, shear force $V$, bending moment $M$, torque $T$) at any section are found by cutting the member and applying equilibrium ($\sum F=0,\ \sum M=0$) to one side of the cut. This "method of sections" underlies:
- axial members ([[Axial Deformation]])
- torsion members ([[Torsion of Circular Shafts]])
- beams ([[Shear Force and Bending Moment Diagrams]])

## Factor of Safety

$$\text{FS} = \frac{\sigma_{\text{failure}}}{\sigma_{\text{allowable}}}$$
Failure stress is typically the yield strength $\sigma_Y$ (ductile materials) or ultimate strength $\sigma_u$ (brittle materials) — see [[Stress-Strain Diagram and Hooke's Law]].

---
Next: [[Stress-Strain Diagram and Hooke's Law]]
