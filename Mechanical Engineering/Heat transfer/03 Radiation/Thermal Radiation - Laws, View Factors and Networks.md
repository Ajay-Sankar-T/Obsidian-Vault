---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Thermal radiation, Stefan-Boltzmann law, View factor, Radiosity, Radiation network, Radiation shield, Gray diffuse enclosure]
---

# Thermal Radiation — Laws, View Factors and Networks

> [!abstract] In one breath
> Every surface emits electromagnetic energy as $\varepsilon\sigma T^4$ and needs no medium. Between surfaces, the heat depends on **how the surfaces see each other** (view factors) and on **how black they are** (emissivities). Both go into a resistance network: a surface resistance $(1-\varepsilon)/\varepsilon A$ and a space resistance $1/AF$ in series, with $\sigma T^4$ playing the role of voltage.

Part of [[Heat Transfer - MOC]]. Previous: [[Boiling and Condensation]]. Next: [[Heat Exchangers - LMTD and NTU]].

## 1. Laws

| Law | Statement |
| --- | --- |
| Stefan–Boltzmann | blackbody emissive power $E_b=\sigma T^4$, $\sigma=5.67\times10^{-8}$ W/m²K⁴ |
| Real surface | $E=\varepsilon\sigma T^4$, emissivity $0\le\varepsilon\le1$ |
| Wien | peak wavelength $\lambda_{max}T=2898\ \mu\text{m·K}$ (sun ≈ 5800 K: 0.5 µm; room: 10 µm) |
| Kirchhoff | $\alpha_\lambda=\varepsilon_\lambda$ at the same wavelength and direction; for a gray body $\alpha=\varepsilon$ |
| Energy balance on a surface | $G=\rho G+\alpha G+\tau G$, so $\rho+\alpha+\tau=1$ (opaque: $\rho=1-\alpha$) |

**Gray diffuse surface:** $\varepsilon$ independent of wavelength and direction; reflected radiation is diffuse. This is the assumption behind every network below.

**Radiosity** $J$ is everything leaving a surface (emitted plus reflected): $J=\varepsilon E_b+\rho G$. The net heat from surface $i$:

$$
Q_i=\frac{E_{b,i}-J_i}{(1-\varepsilon_i)/(\varepsilon_iA_i)}
$$

## 2. View factors

$F_{ij}$ is the fraction of radiation leaving $i$ that strikes $j$. Rules:

- **Reciprocity:** $A_iF_{ij}=A_jF_{ji}$.
- **Summation** over an enclosure: $\sum_jF_{ij}=1$.
- **Flat or convex surface:** $F_{ii}=0$; **concave** surface sees itself.
- **Enclosed small body** in a large cavity: $F_{12}=1$.
- **Crossed-strings rule** (long 2-D geometries): $F_{ij}=\dfrac{\sum\text{crossed strings}-\sum\text{uncrossed strings}}{2\times\text{length of }i}$; for a triangle duct $F_{12}=\dfrac{L_1+L_2-L_3}{2L_1}$.

## 3. Two-surface enclosure

For two surfaces that see only each other (parallel plates, concentric cylinders or spheres):

$$
Q_{12}=\frac{\sigma(T_1^4-T_2^4)}{\dfrac{1-\varepsilon_1}{\varepsilon_1A_1}+\dfrac{1}{A_1F_{12}}+\dfrac{1-\varepsilon_2}{\varepsilon_2A_2}}
$$

For infinite parallel plates ($F_{12}=1$, $A_1=A_2$): $q''=\dfrac{\sigma(T_1^4-T_2^4)}{1/\varepsilon_1+1/\varepsilon_2-1}$.

**Example.** Plates at 500 K ($\varepsilon=0.8$) and 300 K ($\varepsilon=0.6$): blackbody value $3085$ W/m²; real value $3085/1.917=\mathbf{1609\ W/m^2}$.

## 4. Radiation shields

A thin sheet of low emissivity between the plates adds two surface resistances and cuts the flux:

$$
q''=\frac{\sigma(T_1^4-T_2^4)}{\Big(\frac1{\varepsilon_1}+\frac1{\varepsilon_3}-1\Big)+\Big(\frac1{\varepsilon_3}+\frac1{\varepsilon_2}-1\Big)}
$$

One shield with $\varepsilon_3=0.1$ on both sides: $1609\to\mathbf{147\ W/m^2}$ (−91 %), and the shield floats at 435 K. $N$ identical shields cut the flux roughly by $1/(N+1)$ when all emissivities are equal; here with low-$\varepsilon$ shields the first one does most of the job. That is the principle of multilayer insulation in spacecraft and of vacuum flasks.

![[HT-6-radiation.png]]

## 5. Three-surface enclosure by radiosity

Surfaces 1 and 2 with known temperatures, surface 3 **adiabatic (re-radiating)**: $Q_3=0$ so $J_3=E_{b3}$ and its temperature is found, not given. Solve the radiosity equations for each surface:

$$
\frac{E_{bi}-J_i}{(1-\varepsilon_i)/\varepsilon_i}=\sum_jF_{ij}(J_i-J_j)
$$

Long equilateral duct (side 1 m, so every $F=0.5$): surface 1 at 600 K ($\varepsilon=0.8$), surface 2 at 400 K ($\varepsilon=0.5$), surface 3 re-radiating. Result: $J=(6780,\ 3730,\ 5260)$ W/m², net flux $q_1=\mathbf{2280\ W/m^2}$ per metre of duct (all of it to surface 2), and $T_3=\mathbf{552\ K}$. A re-radiating wall transfers heat from the hot to the cold surface without absorbing any.

## 6. Method

1. Identify the surfaces; are the temperatures or the fluxes known for each?
2. Find $F_{ij}$ from reciprocity, summation and the table (or the crossed-strings rule).
3. Draw the network: $E_b$ nodes, surface resistances, $J$ nodes, space resistances. A black surface has zero surface resistance; an adiabatic surface has $J=E_b$.
4. Write one node equation per $J$ (KCL), solve, then $Q_i$.

> [!warning] Traps
> - Using Celsius in $T^4$.
> - Reciprocity with unequal areas: $F_{12}\ne F_{21}$.
> - Treating a re-radiating surface as insulation that blocks heat: it transmits heat by absorbing and re-emitting.
> - Using $F_{12}=1$ for plates of finite size: edge losses make it less than 1.
> - Using radiation for a gas without checking: gas radiation (CO₂, H₂O vapour, soot) needs an emissivity chart.

> [!question]- Predict first: add a second identical shield. Does the flux drop by half again?
> Not exactly. Each shield adds $2/\varepsilon_3-1=19$ resistance units against 1.92 originally. With one shield the flux is 147 W/m² and with two 77 W/m² — roughly halved, since the denominator goes from about 21 to 40.

> [!question]- Why does a re-radiating wall have no net heat flow but still change the answer?
> Its temperature floats to the value that makes absorbed equal emitted, so it adds no net energy but opens an extra *parallel* path between 1 and 2 through the $F_{13},F_{32}$ resistances, which increases $Q_{12}$.

## 7. Connections

- [[Series-Parallel Resistance Reduction]] — the network is a resistor circuit with $E_b$ as voltage and $Q$ as current; node equations are KCL.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — radiative cooling of a small body obeys $mc\,dT/dt=-\varepsilon\sigma A(T^4-T_{sur}^4)$, which is first-order only after linearisation with $h_r=4\varepsilon\sigma T_m^3$.
- [[Natural Convection]] — convection and radiation often act in parallel at the same surface ($h_{tot}=h_c+h_r$).
- [[Conservation Laws and Flow Networks]] — node equations for $J$ are conservation at a node, the same as KCL; the fourth-power law only makes the "source" nonlinear.
