Related: [[Statically Indeterminate Axial Members]] · [[Axial Deformation]]

## Free Thermal Expansion

A bar free to expand, subject to a uniform temperature change $\Delta T$, develops **no stress** — it simply elongates:
$$\delta_T = \alpha\,\Delta T\,L$$
where $\alpha$ is the coefficient of thermal expansion (units 1/°C). This is a strain with no associated stress: $\varepsilon_T=\alpha\Delta T$.

![[SM-C-thermal-stress.png]]

**Figure:** a bar free to expand develops no stress at all. The same temperature rise with both ends fixed produces compression $E\alpha\Delta T$, independent of the bar's length.

## Constrained Thermal Expansion

If the bar's ends are restrained (fully or partially) so it cannot freely expand, an internal (thermal) stress develops. The total deformation is the sum of the mechanical (load-induced) and thermal parts:
$$\delta = \delta_{\text{mechanical}} + \delta_T = \frac{NL}{AE} + \alpha\Delta T\,L$$

**Example — bar fully fixed at both ends, heated by $\Delta T$:** Compatibility requires total elongation $=0$:
$$\frac{NL}{AE}+\alpha\Delta T\,L = 0 \implies N = -AE\alpha\Delta T$$
The negative sign indicates the internal force is compressive when the bar is heated (it "wants" to expand but can't), giving
$$\sigma = \frac{N}{A} = -E\alpha\Delta T$$
This is independent of the bar's length — a purely constrained thermal problem is governed entirely by $E,\alpha,\Delta T$.

## Combined Mechanical + Thermal, Statically Indeterminate Case

For a partially-restrained or composite system, the same procedure as [[Statically Indeterminate Axial Members]] applies, but the compatibility equation must include the thermal term:
$$\delta_i = \frac{N_iL_i}{A_iE_i} + \alpha_i\Delta T_i\,L_i$$
substituted into the geometric compatibility condition, then combined with equilibrium.

**Composite bar (two materials in parallel, both ends free but bonded together):** since both materials share the same overall length change,
$$\frac{N_1}{A_1E_1}+\alpha_1\Delta T = \frac{N_2}{A_2E_2}+\alpha_2\Delta T, \qquad N_1+N_2=0$$
(equilibrium with no external load: the two materials just push/pull against each other because $\alpha_1\ne\alpha_2$). This is the basis of bimetallic strips and thermal-stress design checks in composite structures.

## Check yourself

> [!question]- Q1. A steel bar ($E=200$ GPa, $\alpha=12\times10^{-6}$/K) is held between rigid walls and heated by 50 K. Find the stress.
> $\sigma=-E\alpha\Delta T=-120$ MPa, compressive.

> [!question]- Q2. The same bar is 2 m long and free to expand. How far does it grow?
> $\delta_T=\alpha\Delta T L=12\times10^{-6}\times50\times2=1.2$ mm, with no stress at all.

> [!question]- Q3. Does the length of a fully restrained bar change the thermal stress?
> No. Both the free expansion and the length over which it is pushed back scale with $L$, so $\sigma=E\alpha\Delta T$ is independent of $L$.

---
Next: [[Torsion of Circular Shafts]]
