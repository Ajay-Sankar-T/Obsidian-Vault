Related: [[Concept of Stress]] · [[Generalized Hooke's Law and Poisson's Ratio]]

## Normal Strain

For a bar of original length $L$ stretched to length $L+\delta$:
$$\varepsilon = \frac{\delta}{L}$$
Strain is dimensionless (often quoted in $\mu\varepsilon$ = $10^{-6}$).

## The Tensile Test and Stress-Strain Diagram

A standard tensile test plots engineering stress $\sigma=P/A_0$ against engineering strain $\varepsilon=\delta/L_0$ (both using **original** dimensions). Key features for a ductile material (e.g. mild steel):

- **Proportional limit:** stress up to which $\sigma \propto \varepsilon$ (Hooke's law holds).
- **Elastic limit:** maximum stress from which the material returns to zero strain on unloading.
- **Yield point / yield strength $\sigma_Y$:** stress at which large plastic strain begins with little stress increase.
- **Ultimate strength $\sigma_u$:** maximum stress reached (associated with necking).
- **Fracture stress:** stress at rupture.
- **Ductility:** measured by percent elongation $\dfrac{L_f-L_0}{L_0}\times100\%$ or percent reduction in area.

Brittle materials (cast iron, ceramics, glass) show little/no yielding and fracture near the proportional limit.

## Hooke's Law

In the linear-elastic region:
$$\sigma = E\varepsilon$$
where $E$ is the **modulus of elasticity** (Young's modulus), the slope of the initial linear portion of the $\sigma$-$\varepsilon$ curve. Typical values: steel $E\approx200$ GPa, aluminum $\approx70$ GPa, concrete $\approx25$ GPa.

## Elastic vs Plastic Behavior

- **Elastic:** deformation fully recovers on unloading (below elastic limit).
- **Plastic:** permanent (residual) deformation remains after unloading. Unloading from a point beyond yield follows a line parallel to the original elastic slope $E$.
- **Strain hardening:** the increase in stress required to continue plastic deformation beyond yield.

## Resilience and Toughness

- **Modulus of resilience** $u_r$ = area under the stress-strain curve up to the elastic limit = $\dfrac{\sigma_Y^2}{2E}$ (energy absorbed per unit volume without permanent deformation).
- **Modulus of toughness** $u_t$ = total area under the curve up to fracture (energy absorbed per unit volume before failure).

These connect to [[Strain Energy and Castigliano's Theorem]].

---
Next: [[Generalized Hooke's Law and Poisson's Ratio]]
