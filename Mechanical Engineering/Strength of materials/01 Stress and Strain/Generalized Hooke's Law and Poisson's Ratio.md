Related: [[Stress-Strain Diagram and Hooke's Law]] · [[Axial Deformation]] · [[Plane Stress Transformation]]

## Poisson's Ratio

When a bar is stretched axially, it contracts laterally. For uniaxial stress $\sigma_x$:
$$\varepsilon_y = \varepsilon_z = -\nu\varepsilon_x = -\nu\frac{\sigma_x}{E}$$
where $\nu$ (Poisson's ratio) is a material property, typically $0.25$–$0.35$ for metals (theoretical bounds for isotropic materials: $-1<\nu<0.5$).

## Generalized Hooke's Law (Isotropic, Linear Elastic)

For a general 3D stress state, superposing the effect of each normal stress on each direction:
$$\varepsilon_x = \frac{1}{E}\left[\sigma_x-\nu(\sigma_y+\sigma_z)\right], \quad \varepsilon_y = \frac{1}{E}\left[\sigma_y-\nu(\sigma_x+\sigma_z)\right], \quad \varepsilon_z = \frac{1}{E}\left[\sigma_z-\nu(\sigma_x+\sigma_y)\right]$$
For shear (no coupling between shear and normal terms in isotropic materials):
$$\gamma_{xy}=\frac{\tau_{xy}}{G}, \qquad \gamma_{yz}=\frac{\tau_{yz}}{G}, \qquad \gamma_{zx}=\frac{\tau_{zx}}{G}$$

## Shear Modulus and the Relation Between $E, G, \nu$

$$G = \frac{E}{2(1+\nu)}$$
$G$ (modulus of rigidity) is the slope of the shear stress-shear strain diagram, directly analogous to $E$ for normal stress-strain.

## Bulk Modulus and Dilatation

Volumetric strain (dilatation) under general stress:
$$e = \varepsilon_x+\varepsilon_y+\varepsilon_z = \frac{1-2\nu}{E}(\sigma_x+\sigma_y+\sigma_z)$$
Under uniform hydrostatic pressure $\sigma_x=\sigma_y=\sigma_z=-p$:
$$p = -Ke, \qquad K = \frac{E}{3(1-2\nu)}$$
$K$ is the **bulk modulus**. As $\nu\to0.5$ (incompressible limit), $K\to\infty$.

## Plane Stress Simplification ($\sigma_z=0$)

$$\varepsilon_x=\frac{1}{E}(\sigma_x-\nu\sigma_y), \qquad \varepsilon_y=\frac{1}{E}(\sigma_y-\nu\sigma_x), \qquad \varepsilon_z=-\frac{\nu}{E}(\sigma_x+\sigma_y)$$
Inverting for stress in terms of strain (used in plane-stress finite element formulations):
$$\sigma_x=\frac{E}{1-\nu^2}(\varepsilon_x+\nu\varepsilon_y), \qquad \sigma_y=\frac{E}{1-\nu^2}(\varepsilon_y+\nu\varepsilon_x)$$

This generalized law is what connects [[Concept of Stress]] to every subsequent loading case: axial ([[Axial Deformation]]), torsion ([[Torsion of Circular Shafts]]), and bending ([[Flexure Formula]]) are all special cases of applying Hooke's law to a specific, simplified strain field.

Fully worked applications of this law — restrained/confined deformation, composite members, principal-stress conversion, thermal restraint, and dissimilar-plate problems — are in [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4 — Stress-Strain Relationship]].

## Check yourself

> [!question]- Q1. Steel ($E=200$ GPa, $\nu=0.3$) carries a uniaxial stress of 100 MPa. Find the axial and lateral strains.
> $\varepsilon_x=\sigma/E=5\times10^{-4}$ and $\varepsilon_y=\varepsilon_z=-\nu\varepsilon_x=-1.5\times10^{-4}$.

> [!question]- Q2. Find the shear modulus of the same steel.
> $G=E/[2(1+\nu)]=200/2.6=76.9$ GPa.

> [!question]- Q3. Why can $\nu$ not exceed $0.5$ for an isotropic material?
> The bulk modulus $K=E/[3(1-2\nu)]$ must be positive, so $\nu<0.5$. At $\nu=0.5$ the material is incompressible (rubber is close).

---
Next: [[Axial Deformation]]
