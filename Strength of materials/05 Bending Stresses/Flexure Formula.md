Related: [[Shear Force and Bending Moment Diagrams]] · [[Generalized Hooke's Law and Poisson's Ratio]] · [[Unsymmetric and Combined Bending]] · [[Shear Stress Formula for Beams]]

## Kinematic Assumption: Plane Sections Remain Plane

For pure bending of a straight, symmetric prismatic beam, cross-sections that are initially plane remain plane and perpendicular to the deformed axis (Euler-Bernoulli assumption). This forces the longitudinal strain to vary **linearly** through the depth:
$$\varepsilon(y) = -\frac{y}{\rho}$$
where $y$ is measured from the **neutral axis** (the fiber of zero strain) and $\rho$ is the radius of curvature.

## The Flexure Formula

Applying Hooke's law $\sigma=E\varepsilon$ and requiring the stress resultants over the cross-section to equal zero net axial force and the resultant moment $M$:
$$\int_A \sigma\,dA = 0 \implies \text{the neutral axis passes through the centroid of the section}$$
$$\int_A \sigma\,y\,dA = -M \implies \sigma(y) = -\frac{My}{I}$$
where $I=\int_A y^2\,dA$ is the **second moment of area** (moment of inertia) about the centroidal (neutral) axis. Maximum stress occurs at the extreme fiber $y=c$:
$$\sigma_{max} = \frac{Mc}{I} = \frac{M}{S}, \qquad S=\frac{I}{c} \text{ (section modulus)}$$

**Sign convention:** positive $M$ (sagging) puts the top fiber ($y>0$ measured upward from NA) in **compression** and the bottom fiber in **tension** — hence the minus sign in $\sigma=-My/I$ (many texts instead define $y$ downward or state the formula as $\sigma=Mc/I$ with tension/compression assigned by inspection).

## Common Section Properties

| Section | $I$ (about centroidal horizontal axis) |
|---|---|
| Rectangle $b\times h$ | $\dfrac{bh^3}{12}$ |
| Circle, radius $r$ | $\dfrac{\pi r^4}{4}$ |
| Hollow circle | $\dfrac{\pi(r_o^4-r_i^4)}{4}$ |

For composite/built-up sections, use the **parallel-axis theorem**: $I=I_c+Ad^2$, where $I_c$ is about the part's own centroid and $d$ is the distance from that centroid to the overall neutral axis.

## Curvature-Moment Relation

$$\frac{1}{\rho} = \frac{M}{EI}$$
This is the fundamental relation extended in [[Double Integration and Macaulay's Method]] (using $1/\rho\approx d^2v/dx^2$ for small deflections) to find beam deflections directly from $M(x)$.

---
Cross-domain: [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|the same I integral computes centre of pressure in fluid statics]]

Next: [[Unsymmetric and Combined Bending]]
