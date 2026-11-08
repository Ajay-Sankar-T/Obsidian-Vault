---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Free convection, Rayleigh number, Grashof number, Churchill-Chu, Buoyancy-driven flow]
---

# Natural Convection

> [!abstract] In one breath
> No fan: a heated surface warms the fluid next to it, the warm fluid is lighter and rises, and the flow drives itself. The relevant number is the **Rayleigh number** $Ra=g\beta\Delta TL^3/(\nu\alpha)$, the ratio of buoyancy to the viscous and thermal drag that resists it. Everything else is $Nu=f(Ra,Pr)$.

Part of [[Heat Transfer - MOC]]. Previous: [[Forced Convection Correlations]]. Next: [[Boiling and Condensation]].

## 1. Where the numbers come from

The buoyancy force per volume is $\rho g\beta(T-T_\infty)$ with $\beta=-\frac1\rho\frac{\partial\rho}{\partial T}$ ($=1/T$ for an ideal gas, $T$ in kelvin). It enters the momentum equation, and the energy equation is unchanged. Scale analysis (a thermal layer $\delta_T$ with a vertical speed $U$):

$$
\text{buoyancy}\sim\text{viscous: } g\beta\Delta T\sim\frac{\nu U}{\delta_T^2},\qquad
\text{convection}\sim\text{conduction: } \frac{U}{L}\sim\frac{\alpha}{\delta_T^2}
$$

Eliminating $U$:

$$
\frac{\delta_T}{L}\sim Ra^{-1/4}\ \Rightarrow\ Nu\sim\frac{L}{\delta_T}\sim Ra^{1/4}\qquad(\text{laminar})
$$

The **Grashof number** $Gr=g\beta\Delta TL^3/\nu^2$ plays the role of $Re^2$ and $Ra=Gr\,Pr$. Transition on a vertical plate is at $Ra\approx10^9$, when $Nu\sim Ra^{1/3}$ (the layer no longer limits the heat, so $h$ is independent of $L$).

## 2. Correlations

**Vertical plate (isothermal), Churchill–Chu, valid for all $Ra$:**

$$
\overline{Nu}_L=\Bigg\{0.825+\frac{0.387\,Ra_L^{1/6}}{\big[1+(0.492/Pr)^{9/16}\big]^{8/27}}\Bigg\}^2
$$

For $Ra<10^9$ the simpler laminar form $\overline{Nu}=0.68+\dfrac{0.670\,Ra^{1/4}}{[1+(0.492/Pr)^{9/16}]^{4/9}}$ is used.

**Horizontal plate, hot side up:** $\overline{Nu}=0.54Ra^{1/4}$ ($10^4<Ra<10^7$), $0.15Ra^{1/3}$ above, with $L=A/P$. **Hot side down:** $0.27\,Ra^{1/4}$ (the heavy cold fluid is on the bottom, so the exchange is weak).

**Horizontal cylinder** (Churchill–Chu): same structure with $D$ as the length.

Properties are at the film temperature $T_f=(T_s+T_\infty)/2$; for gases $\beta=1/T_f$.

## 3. Worked example

Vertical plate, $L=0.5$ m, $T_s=80$ °C in still air at 20 °C: $T_f=323$ K, $\nu=1.80\times10^{-5}$, $\alpha=2.55\times10^{-5}$ m²/s, $Pr=0.704$, $\beta=1/323$.

$$
Ra=\frac{9.81\,(1/323)(60)(0.5)^3}{\nu\alpha}=\mathbf{5.0\times10^8}\ (\text{laminar}),\qquad
\overline{Nu}=99,\quad
\bar h=99\frac{0.0280}{0.5}=\mathbf{5.6\ W/m^2K}
$$

$q''=5.6\times60=334$ W/m². Natural convection in air gives $h\sim3$–$10$ W/m²K, so **radiation from the surface is comparable** and must not be ignored when $\varepsilon$ is high: $h_r\approx4\varepsilon\sigma T_m^3$ is about 6.3 W/m²K for $\varepsilon=0.9$ near 320 K.

![[HT-4-convection.png]]

> [!warning] Traps
> - Temperatures in kelvin for $\beta=1/T$.
> - Using $L$ of the plate for a cylinder: use the diameter.
> - Ignoring radiation. In still air at modest temperature it carries about half the heat from a dark surface.
> - Using properties at $T_\infty$ or $T_s$ instead of $T_f$.

> [!question]- Predict first: a vertical plate twice as tall. How does $\bar h$ change in the turbulent range?
> $Nu\sim Ra^{1/3}\propto L$, and $h=Nu\,k/L$ is **independent of $L$** in fully turbulent natural convection, because the layer thickness stops depending on height.

> [!question]- Why does a hot plate facing down lose heat so poorly?
> The hot fluid wants to rise but the plate is in the way, so it stays trapped under the plate and the flow is weak (lower $0.27Ra^{1/4}$ coefficient). A cold plate facing up is the same configuration.

## 4. Connections

- [[Forced Convection Correlations]] — mixed convection is judged by $Gr/Re^2$: below 0.1 forced dominates, above 10 natural dominates.
- [[Convection Fundamentals - Boundary Layers and Scale Analysis]] — the same scale-analysis method with buoyancy as the driver.
- [[Buoyancy and Archimedes' Principle]] — the same buoyancy force, here produced by a temperature-induced density difference $\rho\beta\Delta T$.
- [[Dimensional Analysis and Similitude - Formula Bank]] — $Ra$ is a $\Pi$ group, the product of $Gr$ and $Pr$.
