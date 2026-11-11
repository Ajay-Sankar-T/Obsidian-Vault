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

## Check yourself

> [!question]- Q1. A 1.5 m aluminium bar ($E=70$ GPa, $A=400$ mm²) carries 28 kN. Find the elongation.
> $\delta=PL/AE=28\,000\times1.5/(400\times10^{-6}\times70\times10^9)=1.5$ mm.

> [!question]- Q2. A bar has two equal-length halves, one of area $A$ and one of area $2A$, same $E$, loaded by $P$ at the end. What is the total elongation?
> $\delta=\frac{P(L/2)}{AE}+\frac{P(L/2)}{2AE}=\frac{3PL}{4AE}$.

> [!question]- Q3. A uniform bar of length $L$ hangs from one end under its own weight. How much does it stretch?
> $\delta=\rho gL^2/2E$: the same as if half its weight acted at the free end, because the load carried varies linearly from zero to the full weight.

---
Next: [[Statically Indeterminate Axial Members]]
