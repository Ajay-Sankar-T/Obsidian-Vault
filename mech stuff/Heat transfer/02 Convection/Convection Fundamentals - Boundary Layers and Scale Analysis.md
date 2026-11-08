---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Convection, Boundary layer, Nusselt number, Prandtl number, Scale analysis, Newton's law of cooling]
---

# Convection Fundamentals — Boundary Layers and Scale Analysis

> [!abstract] In one breath
> Convection is conduction through a thin fluid layer whose thickness the flow sets. Newton's law $q''=h(T_s-T_\infty)$ just hides that thickness inside $h$. **Scale analysis** finds it without solving the equations: a laminar boundary layer grows like $\delta\sim x\,Re_x^{-1/2}$, so $h\sim k/\delta$ and $Nu_x\sim Re_x^{1/2}Pr^{1/3}$.

Part of [[Heat Transfer - MOC]]. Previous: [[Transient Conduction - Lumped Capacitance and Heisler Charts]]. Next: [[Forced Convection Correlations]], [[Natural Convection]].

## 1. $h$ is a conduction problem in disguise

At a wall the fluid is at rest (no slip), so heat leaves by conduction there:

$$
q''_s=-k_f\frac{\partial T}{\partial y}\Big|_{y=0}=h\,(T_s-T_\infty)\ \Rightarrow\
h=\frac{-k_f\,\partial T/\partial y|_0}{T_s-T_\infty},\qquad
Nu=\frac{hL}{k_f}=\frac{\text{convective}}{\text{conductive}}
$$

$Nu$ is the dimensionless temperature gradient at the wall: a thin thermal layer means a large $Nu$.

## 2. Governing equations (steady, 2-D, constant properties)

Continuity, x-momentum and energy for a boundary layer ($\partial/\partial x\ll\partial/\partial y$):

$$
\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}=0,\quad
u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}=\nu\frac{\partial^2u}{\partial y^2},\quad
u\frac{\partial T}{\partial x}+v\frac{\partial T}{\partial y}=\alpha\frac{\partial^2T}{\partial y^2}
$$

The momentum and energy equations have the **same form**; the only difference is $\nu$ against $\alpha$. Their ratio is the **Prandtl number** $Pr=\nu/\alpha=\mu c_p/k$: how fast momentum diffuses compared with heat. Air $0.71$; water at 20 °C $7$; engine oil $10^3$–$10^4$; liquid metals $10^{-2}$.

## 3. Scale analysis (the exam method)

**Velocity layer.** At distance $x$ from the leading edge the fluid has been in the layer for $t\sim x/U$ and diffuses momentum $\delta\sim\sqrt{\nu t}$:

$$
\frac{U^2}{x}\sim\nu\frac{U}{\delta^2}\ \Rightarrow\
\frac{\delta}{x}\sim Re_x^{-1/2}\qquad(\text{exact: }\delta=5x\,Re_x^{-1/2})
$$

**Thermal layer, $Pr\gtrsim1$** (thermal layer sits inside the velocity layer): heat diffuses only $\delta_T\sim\delta\,Pr^{-1/3}$. **$Pr\ll1$** (liquid metal): $\delta_T\gg\delta$ and the flow is nearly uniform across it, $\delta_T\sim\delta\,Pr^{-1/2}$.

$$
Nu_x=\frac{hx}{k}\sim\frac{x}{\delta_T}\ \Rightarrow\ \boxed{Nu_x\sim Re_x^{1/2}\,Pr^{1/3}}
$$

The exact similarity (Blasius/Pohlhausen) solution fixes the constants:

$$
Nu_x=0.332\,Re_x^{1/2}Pr^{1/3},\qquad
\overline{Nu}_L=0.664\,Re_L^{1/2}Pr^{1/3}\ (\text{average is twice the local value at }L)
$$

Because $h_x\propto x^{-1/2}$, the heat transfer is largest near the leading edge, where the layer is thinnest.

## 4. The pattern of correlations

Scale analysis gives the **form**; experiments fix the constants:

| Situation | Dimensionless groups | Typical form |
| --- | --- | --- |
| Forced convection | $Re,\ Pr$ | $Nu=C\,Re^m\,Pr^n$ |
| Natural convection | $Ra=Gr\,Pr$ | $Nu=C\,Ra^n$ |
| Mixed | $Gr/Re^2$ decides | combine the two |

This is the [[Buckingham Pi Theorem]] at work: $h$ depends on $\rho,\mu,k,c_p,U,L$, giving $Nu=f(Re,Pr)$ by dimensional analysis alone.

## 5. Worked example: air over a plate

Air at 300 K ($\nu=1.57\times10^{-5}$, $k=0.0264$, $Pr=0.707$) at 5 m/s over a 1 m plate:

$$
Re_L=\frac{5(1)}{1.57\times10^{-5}}=3.2\times10^5\ (<5\times10^5:\ \text{laminar}),\quad
\overline{Nu}_L=0.664(564)(0.707)^{1/3}=333,\quad
\bar h=\mathbf{8.8\ W/m^2K}
$$

Boundary-layer thickness at the trailing edge $\delta=5/\sqrt{Re_L}=8.9$ mm. Transition at $Re_x=5\times10^5$ would be $x=1.57$ m, beyond the plate.

![[HT-4-convection.png]]

> [!warning] Traps
> - Using $k$ of the *wall* in $Nu=hL/k$: it is the **fluid's** conductivity.
> - Property temperature: evaluate fluid properties at the film temperature $T_f=(T_s+T_\infty)/2$ (unless the correlation says bulk).
> - Applying $0.664\,Re^{1/2}Pr^{1/3}$ when $Pr<0.6$ (liquid metals) or $Re_L>5\times10^5$.
> - Forgetting $Nu$ built on $L$ for plates and on $D$ for pipes and cylinders.

> [!question]- Predict first: for oil ($Pr=1000$), is the thermal layer thicker or thinner than the velocity layer?
> Much thinner: $\delta_T/\delta\sim Pr^{-1/3}=0.1$. Heat does not diffuse far in the time the oil takes to pass, so the thermal layer stays inside the slow fluid close to the wall.

> [!question]- If the plate length doubles at the same speed, what happens to the average $h$?
> $\bar h\propto L^{-1/2}$, so it falls by 29 %. The total heat still rises as $L^{1/2}$ because the area doubled.

## 6. Connections

- [[Viscosity and Newton's Law of Viscosity]] — $\mu$ sets the momentum diffusivity $\nu$ in $Pr$.
- [[Viscous Flow and Exact Solutions - Formula Bank]] — fully developed laminar flows give constants like $Nu=3.66$ exactly; the boundary layer is the developing counterpart.
- [[Dimensional Analysis and Similitude - Formula Bank]] — why $Nu=f(Re,Pr)$.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — diffusion over a distance $\delta\sim\sqrt{\nu t}$ is the same scaling as heat penetration $\sqrt{\alpha t}$ in transient conduction.
