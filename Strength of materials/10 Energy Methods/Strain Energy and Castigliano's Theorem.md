Related: [[Stress-Strain Diagram and Hooke's Law]] · [[Axial Deformation]] · [[Torsion of Circular Shafts]] · [[Flexure Formula]] · [[Euler Buckling of Columns]]

## Strain Energy Density

Work done by a gradually applied force, stored as recoverable elastic energy, per unit volume:
$$u = \int_0^\varepsilon \sigma\,d\varepsilon \overset{\text{linear elastic}}{=} \frac{1}{2}\sigma\varepsilon = \frac{\sigma^2}{2E}$$
This is the area under the stress-strain curve up to the current state — see **modulus of resilience** in [[Stress-Strain Diagram and Hooke's Law]]. For shear: $u=\tfrac12\tau\gamma=\tau^2/(2G)$.

## Total Strain Energy for Common Members

Integrating $u$ over the volume of the member gives the total strain energy $U$, expressed directly in terms of the internal stress resultant:

| Loading | Strain energy $U$ |
|---|---|
| Axial (constant $N$) | $\dfrac{N^2L}{2AE}$ |
| Axial (varying $N(x)$) | $\displaystyle\int_0^L \frac{N(x)^2}{2AE}\,dx$ |
| Torsion (constant $T$) | $\dfrac{T^2L}{2GJ}$ |
| Torsion (varying) | $\displaystyle\int_0^L \frac{T(x)^2}{2GJ}\,dx$ |
| Bending | $\displaystyle\int_0^L \frac{M(x)^2}{2EI}\,dx$ |

Each has the same structure: $U=\dfrac{(\text{stress resultant})^2\times\text{length}}{2\times\text{stiffness}}$ — the energy analogue of the "force $\times$ deformation / 2" formula for a linear spring, $U=\tfrac12k\delta^2=\tfrac12P\delta$.

## Castigliano's Second Theorem

For a linear-elastic structure with strain energy $U$ expressed as a function of the applied loads $P_1,P_2,\ldots$, the displacement **in the direction of** $P_i$ (at its point of application) is
$$\delta_i = \frac{\partial U}{\partial P_i}$$
This is extremely powerful for finding a single deflection/rotation **without** solving for the full deflection curve (contrast with [[Double Integration and Macaulay's Method]]):

1. Express internal $N(x),T(x),$ or $M(x)$ in terms of the actual loads, **including** a variable $P$ at the point/direction where the deflection is sought (introduce a fictitious "dummy load" $Q$ there if no real load acts, then set $Q=0$ after differentiating).
2. Write $U$ as an integral/sum in terms of $P$ (and other fixed loads).
3. Differentiate under the integral sign: $\delta=\dfrac{\partial U}{\partial P}=\displaystyle\int \frac{M}{EI}\frac{\partial M}{\partial P}\,dx$ (bending case; analogous for axial/torsion terms, and combinable by superposition when several loading types act together).
4. Set $P$ (or the dummy load $Q$) to its actual value.

**For a rotation** (slope) at a point, use a **dummy moment** $M_0$ in place of a dummy force, and $\theta=\partial U/\partial M_0$.

## Why This Matters for Statically Indeterminate Structures

Castigliano's **first theorem** (a companion result) provides that for a statically indeterminate structure, the redundant reaction $R$ can be found from the condition that the displacement at the redundant support is zero:
$$\frac{\partial U}{\partial R} = 0$$
This gives an alternative, often more systematic route to the same compatibility equations used in [[Statically Indeterminate Axial Members]] and indeterminate beam problems, especially useful when there are multiple redundants.

## Connection to Buckling

The energy stored during buckling ([[Euler Buckling of Columns]]) can also be analyzed via energy methods (Rayleigh-Ritz), where an assumed deflected shape is used to estimate $P_{cr}$ by equating the work done by $P$ to the bending strain energy stored in the assumed curvature — a preview of the finite-element / variational approach to structural mechanics.

---
Cross-domain: [[Cross-Domain Synthesis/Energy Methods - A Unified View|strain energy and circuit energy storage (½LI², ½CV²) are the same integral]] · [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|mechanical stiffness ↔ electrical elastance 1/C]]

Next: [[Thin Cylindrical and Spherical Pressure Vessels]]
