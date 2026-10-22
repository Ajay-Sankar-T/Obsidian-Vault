---
tags: [synthesis, cross-domain, second-moments, tensor]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Second Moments of Area — One Integral, Many Jobs

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

$$I=\int y^2\,dA$$

shows up wherever **something grows linearly with distance and is then multiplied by that same distance as a lever arm**. One factor of $y$ comes from the physics (strain, pressure, tilt volume, speed), the other from the moment arm. [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]] and [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula]] already point at each other; this note collects every appearance.

| Where | Result | Why the square |
|---|---|---|
| Beam bending | $\sigma=-My/I$, $\ \dfrac1\rho=\dfrac{M}{EI}$ | strain $\varepsilon=-y/\rho$ is linear in $y$; moment arm is $y$ |
| Torsion | $\tau=T\rho/J$, $\ \phi=\dfrac{TL}{GJ}$, $\ J=\int\rho^2dA$ | shear strain linear in $\rho$; arm is $\rho$ |
| Buckling | $P_{cr}=\dfrac{\pi^2EI}{L^2}$ | bending stiffness $EI$ resists lateral deflection ([[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling]]) |
| Centre of pressure | $h_{CP}=h_c+\dfrac{I_G}{Ah_c}$ | pressure linear in depth; arm is depth |
| Floating stability | metacentre uses waterplane $I_O$ | tilt displaces wedge volumes $\propto y$, arm $y$ ([[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Metacentre]]) |
| Rotating machines | $\tfrac12 J\omega^2$, $\ T=J\alpha$, $J=\int r^2dm$ | speed $\propto r$; momentum arm $r$ (reflected through gears in [[Cross-Domain Synthesis/Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]]) |

The "stiffness × deformation = load" family $AE,\ GJ,\ EI$ ([[Strength of materials/03 Torsion/Torsion of Circular Shafts|Torsion]] notes this) is the same pattern; only the geometric integral changes: $A$, $J$, $I$.

## Facts that connect them

- **Perpendicular-axis theorem:** $J=I_x+I_y$ for a plane section. Check: a circle has $I=\pi R^4/4$ and $J=\pi R^4/2$, both in the vault's tables. So $J=2I$ for a circle: $GJ$ is twice $GI$, the torsional analogue of $EI$.
- **It is a rank-2 tensor.** $I_x,I_y,I_{xy}$ transform with $\cos2\theta,\sin2\theta$, so **Mohr's circle applies unchanged** to second moments, with principal axes as the eigen-directions. This is the missing case flagged in [[Cross-Domain Synthesis/Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]] ("moment of inertia principal axes"); it is why [[Strength of materials/05 Bending Stresses/Unsymmetric and Combined Bending|Unsymmetric Bending]] needs principal axes. Rule: angle at $2\times$ means rank 2.
- **Buckling picks the weakest axis.** The column fails about the axis with the smallest principal $I$, so section choice (tubes over solid bars: $\pi(r_o^4-r_i^4)/4$) is about pushing area outward, where the square pays.
- **Parallel-axis theorem** $I=I_G+Ad^2$ is the same in all rows: floating bodies, composite beams, centre of pressure from a free surface.

## Common traps

- Cubing the wrong dimension: in $bh^3/12$ the dimension **perpendicular to the bending/tilt axis** is cubed, in beams and in waterplanes alike.
- Using $J$ for non-circular shafts (the formula holds only for circular sections).
- Taking the mass moment $J=\int r^2dm$ for the area moment $\int y^2dA$: different units, same structure.

## Related
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area (Fluid Mechanics)]]
- [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]
