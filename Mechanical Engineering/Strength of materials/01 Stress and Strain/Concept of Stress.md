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

## Check yourself

> [!question]- Q1. A 20 mm diameter rod carries a 50 kN tensile load. What is the normal stress?
> $\sigma=P/A=50\,000/(\pi\,0.01^2)=159.2$ MPa.

> [!question]- Q2. A 10 mm bolt in single shear transmits 12 kN. What is the average shear stress?
> $\tau=V/A=12\,000/(\pi\,0.005^2)=152.8$ MPa.

> [!question]- Q3. Why does one axial load produce both normal and shear stress?
> Stress depends on the plane you cut. On a plane at angle $\theta$ to the cross-section, $\sigma_\theta=\sigma\cos^2\theta$ and $\tau_\theta=\sigma\sin\theta\cos\theta$. The shear is largest, $\sigma/2$, at $45^\circ$.

---
Next: [[Stress-Strain Diagram and Hooke's Law]]
