Related: [[Generalized Hooke's Law and Poisson's Ratio]] · [[Power Transmission by Shafts]]

## Kinematic Assumption

For a circular shaft twisted by torque $T$, cross-sections remain plane and rotate rigidly about the shaft axis (no warping, valid for circular cross-sections). A radial line rotates through angle $\phi(x)$; shear strain at radius $\rho$ varies **linearly**:
$$\gamma(\rho) = \rho\,\frac{d\phi}{dx} = \frac{\rho\,\phi}{L} \text{ (uniform } T\text{)}$$

## The Torsion Formula

Applying Hooke's law $\tau=G\gamma$ and integrating the resulting stress over the section to equate the internal torque resultant to $T$:
$$\tau(\rho) = \frac{T\rho}{J}, \qquad \tau_{max} = \frac{Tc}{J}$$
where $c$ is the outer radius and $J$ is the **polar moment of inertia**:
$$J = \int_A \rho^2\,dA = \begin{cases}\dfrac{\pi c^4}{2} & \text{solid circular section}\\[2mm] \dfrac{\pi(c_o^4-c_i^4)}{2} & \text{hollow (tube)}\end{cases}$$
Shear stress is **zero at the center, maximum at the outer surface** — this is why hollow shafts are structurally efficient (material removed from the low-stress center).

## Angle of Twist

$$\phi = \frac{TL}{GJ}, \qquad \phi = \int_0^L \frac{T(x)}{G(x)J(x)}\,dx \text{ (general case)}$$
$GJ$ is the **torsional stiffness**, directly analogous to $AE$ in [[Axial Deformation]] and $EI$ in [[Double Integration and Macaulay's Method]] — the same "stiffness × deformation = load" pattern recurs across all loading types.

## Statically Indeterminate Shafts

Composite/fixed-fixed shafts follow the same method as [[Statically Indeterminate Axial Members]]: equilibrium ($\sum T=0$) plus compatibility (total angle of twist $=0$ or matched between segments), using $\phi_i=T_iL_i/(G_iJ_i)$.

## Shear Stress on Perpendicular Planes

By equilibrium of a stress element, shear stress on the cross-section (from twisting) is paired with an equal shear stress on the longitudinal (axial) plane — this is why brittle materials (cast iron, chalk) fail in torsion along a $45°$ helical spiral: the shear state on the shaft surface corresponds to a principal tensile stress at $45°$ to the axis (see [[Plane Stress Transformation]]).

## Worked extensions
Stepped shafts, tapered bars, distributed torque, misfit between shafts (series), shrink-fit composite shafts (parallel) and gear-coupled shafts are worked, with figures and the energy-method check, in [[Tutorial 6 - Torsional Members/Tutorial 6 - Torsional Members|Tutorial 6 — Torsional Members]].

---
Next: [[Power Transmission by Shafts]]


## Cross-domain links

- [[Cross-Domain Synthesis/Second Moments of Area - One Integral, Many Jobs|Second Moments of Area]] — J = I_x + I_y = 2I for a circle; same integral as bending, buckling, centre of pressure.

## See also
- [[Flexure Formula]] — the polar moment $J$ here and the second moment $I$ there play the same role.
