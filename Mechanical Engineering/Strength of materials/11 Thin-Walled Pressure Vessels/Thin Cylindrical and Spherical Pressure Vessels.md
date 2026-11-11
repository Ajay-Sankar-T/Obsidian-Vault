Related: [[Plane Stress Transformation]] · [[Mohr's Circle for Stress]] · [[Generalized Hooke's Law and Poisson's Ratio]]

## Thin-Wall Assumption

A pressure vessel is "thin-walled" when wall thickness $t$ is small compared to the radius $r$ (rule of thumb: $r/t\ge10$). Under this assumption, stress can be treated as **uniform through the thickness**, found from simple equilibrium (membrane theory) rather than a full elasticity solution.

![[SM-C-pressure-vessel.png]]

**Figure:** cutting along the axis shows the hoop stress, cutting across shows the longitudinal stress. For $p=2$ MPa, $r=0.5$ m, $t=10$ mm the hoop stress is $100$ MPa and the axial stress $50$ MPa.

## Cylindrical Vessel Under Internal Pressure $p$

Two independent stresses act in the wall (both **tensile**, both principal stresses since the free inner/outer surfaces carry zero shear):

**Hoop (circumferential) stress** — from equilibrium of half the cylinder split along its axis, pressure pushing apart is balanced by wall tension on two longitudinal cuts:
$$\sigma_h = \frac{pr}{t}$$

**Longitudinal (axial) stress** — from equilibrium of a capped end, pressure force on the circular end area is balanced by wall tension around the circumference:
$$\sigma_l = \frac{pr}{2t}$$

Note $\sigma_h=2\sigma_l$ — the hoop stress is always twice the longitudinal stress for a thin cylinder, which is *why* cylindrical vessels/pipes that fail from overpressure typically split **longitudinally** (along a line parallel to the axis, since that's the plane the larger hoop stress acts to open up).

## Spherical Vessel Under Internal Pressure $p$

By symmetry, the stress is the same in every direction in the wall:
$$\sigma = \frac{pr}{2t}$$
(equal to the cylinder's longitudinal stress formula) — a sphere is the most efficient shape for resisting internal pressure, since it has no "weak direction" like the cylinder's hoop stress.

## Stress State at the Wall and Maximum Shear

At the outer (or inner) surface, the through-thickness stress is approximately zero (free surface, or $-p$ at the inner surface itself, usually negligible compared to $\sigma_h,\sigma_l$), so the wall is approximately in a **biaxial (plane) stress state** $(\sigma_h,\sigma_l,0)$ — directly analyzable with [[Plane Stress Transformation]] and [[Mohr's Circle for Stress]] to find maximum shear stress, which governs yielding in ductile-vessel design:

**Cylinder:** treating the three principal stresses as $\sigma_h=pr/t,\ \sigma_l=pr/2t,\ \sigma_r\approx0$, the absolute maximum shear stress (considering all three principal planes, not just the 2D in-plane pair) is
$$\tau_{max} = \frac{\sigma_h-0}{2} = \frac{pr}{2t}$$
(the largest gap is between the hoop stress and the through-thickness stress, not between hoop and longitudinal).

## Strain in the Wall

Using the biaxial (plane-stress) form of [[Generalized Hooke's Law and Poisson's Ratio]], the change in radius/length of the vessel under pressure can be found from $\varepsilon_h,\varepsilon_l$ — this connects pressure-vessel analysis back to strain-gauge-based experimental stress analysis (see [[Strain Transformation and Rosettes]]), a common way pressure vessel stresses are verified in practice.

## Design Note

Vessel design codes (ASME, etc.) apply these thin-wall formulas with an appropriate factor of safety and often a **joint efficiency** factor (for welded seams, which are weaker than the parent material) multiplying the allowable stress.


## Check yourself

> [!question]- Q1. A thin cylinder with $p=2$ MPa, $r=0.5$ m, $t=10$ mm. Find the hoop and axial stresses.
> $\sigma_h=pr/t=100$ MPa and $\sigma_l=pr/2t=50$ MPa.

> [!question]- Q2. What is the wall stress in a sphere of the same $p$, $r$ and $t$?
> $\sigma=pr/2t=50$ MPa in every direction, half the hoop stress of the cylinder.

> [!question]- Q3. Why does a boiled sausage split along its length?
> The hoop stress is twice the axial stress, so the weaker longitudinal seam fails first.

## Cross-domain links

- [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — hoop stress from the projected-area force balance used for hydrostatic force on curved surfaces.
