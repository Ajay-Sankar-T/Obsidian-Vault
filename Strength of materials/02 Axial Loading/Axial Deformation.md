Related: [[Generalized Hooke's Law and Poisson's Ratio]] · [[Concept of Stress]] · [[Statically Indeterminate Axial Members]]

## Deformation of a Prismatic Bar

For a bar of length $L$, constant cross-section $A$, modulus $E$, under constant axial force $N$:
$$\sigma = \frac{N}{A}, \qquad \varepsilon = \frac{\sigma}{E} = \frac{N}{AE}, \qquad \delta = \varepsilon L = \frac{NL}{AE}$$

$AE$ is the **axial stiffness** of the member (units of force).

## Varying Cross-Section or Load

If $N(x)$ or $A(x)$ varies continuously along the length:
$$\delta = \int_0^L \frac{N(x)}{A(x)E}\,dx$$

For a member made of $n$ prismatic segments (different $N_i, A_i, E_i, L_i$), superpose:
$$\delta = \sum_{i=1}^n \frac{N_iL_i}{A_iE_i}$$

## Axial Member as a Spring

The relation $\delta = NL/(AE)$ is exactly Hooke's-law-for-a-spring, $N=k\delta$, with equivalent stiffness $k=AE/L$. Axial members in series/parallel combine like springs:
- **Series** (same $N$ through each): $\dfrac{1}{k_{eq}}=\sum \dfrac{1}{k_i}$
- **Parallel** (same $\delta$, loads share): $k_{eq}=\sum k_i$

This spring analogy is essential for [[Statically Indeterminate Axial Members]], where compatibility of displacement (not just equilibrium) is needed to solve for the internal forces.

## Saint-Venant's Principle

The formula $\sigma=N/A$ assumes a uniform stress distribution across the section. Near points of load application or abrupt cross-section change, the actual stress distribution is non-uniform, but **Saint-Venant's principle** states that this local disturbance decays and the stress becomes essentially uniform at a distance comparable to the largest cross-sectional dimension away from the disturbance. Stress concentrations near holes, fillets, and notches are quantified by a stress-concentration factor $K$: $\sigma_{max}=K\sigma_{avg}$.

---
Next: [[Statically Indeterminate Axial Members]]
