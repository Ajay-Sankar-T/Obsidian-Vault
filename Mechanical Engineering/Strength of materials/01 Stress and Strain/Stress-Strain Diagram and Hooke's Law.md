Related: [[Concept of Stress]] · [[Generalized Hooke's Law and Poisson's Ratio]]

## Normal Strain

For a bar of original length $L$ stretched to length $L+\delta$:
$$\varepsilon = \frac{\delta}{L}$$
Strain is dimensionless (often quoted in $\mu\varepsilon$ = $10^{-6}$).

![[SM-C-stress-strain.png]]

**Figure:** the labelled engineering curve of mild steel. The elastic part is exaggerated so that every feature is visible. Unloading beyond yield follows a line **parallel to the elastic line**, which is why a permanent set remains.

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

## Check yourself

> [!question]- Q1. What separates the yield strength from the ultimate strength?
> Yield strength is the stress at which permanent deformation begins. Ultimate strength is the largest engineering stress the specimen reaches before it necks down.

> [!question]- Q2. A 10 mm diameter, 2 m long steel rod ($E=200$ GPa) carries 15 kN within the elastic range. How much does it stretch?
> $\delta=PL/AE=15\,000\times2/(7.854\times10^{-5}\times200\times10^9)=1.91$ mm.

> [!question]- Q3. What does unloading from beyond yield look like on the diagram?
> The path is a straight line parallel to the elastic line. When the load reaches zero a permanent strain remains.

---
Next: [[Generalized Hooke's Law and Poisson's Ratio]]
