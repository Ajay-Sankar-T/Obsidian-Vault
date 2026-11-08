---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Dittus-Boelter, Gnielinski, Forced convection, Internal flow heat transfer, Flat plate correlations, Churchill-Bernstein]
---

# Forced Convection Correlations

> [!abstract] In one breath
> Choose the correlation in three steps: **external or internal flow; laminar or turbulent ($Re$); which temperature the properties are evaluated at**. Then $Nu=f(Re,Pr)$ gives $h$, and $q=hA\Delta T$ gives the heat.

Part of [[Heat Transfer - MOC]]. Previous: [[Convection Fundamentals - Boundary Layers and Scale Analysis]]. Next: [[Natural Convection]].

## 1. External flow over a flat plate (isothermal)

| Regime | Local | Average over $0\to L$ |
| --- | --- | --- |
| Laminar, $Re_x<5\times10^5$, $Pr\ge0.6$ | $Nu_x=0.332\,Re_x^{1/2}Pr^{1/3}$ | $\overline{Nu}_L=0.664\,Re_L^{1/2}Pr^{1/3}$ |
| Turbulent, $Re_x>5\times10^5$ | $Nu_x=0.0296\,Re_x^{4/5}Pr^{1/3}$ | |
| Mixed (laminar front, turbulent rest) | | $\overline{Nu}_L=(0.037\,Re_L^{4/5}-871)\,Pr^{1/3}$ |

Example (mixed): air at 25 m/s over a 2 m plate, $Re_L=3.2\times10^6$:

$$
\overline{Nu}_L=(0.037\times3.2\times10^6{}^{0.8}-871)(0.707)^{1/3}=4460,\qquad
\bar h=4460\frac{0.0264}{2}=\mathbf{59\ W/m^2K}
$$

Compare the laminar value 8.8 W/m²K at 5 m/s: higher speed and turbulence raise $h$ about 7 times.

**Cylinder and sphere in cross flow** have their own correlations (Churchill–Bernstein for the cylinder, Whitaker for the sphere), with $Nu$ based on the diameter.

## 2. Internal flow in a tube

Based on the bulk velocity and the diameter: $Re_D=\rho VD/\mu$; laminar for $Re_D<2300$.

**Fully developed laminar:** $Nu_D=3.66$ (constant wall temperature) or $4.36$ (constant heat flux). It is a constant: the temperature profile has become self-similar, so $h=Nu\,k/D$ does not change with speed or length.

**Turbulent, fully developed** (long tube, $L/D>10$):

$$
\textbf{Dittus–Boelter:}\ Nu_D=0.023\,Re_D^{0.8}Pr^{n},\quad n=0.4\ (\text{fluid heated}),\ 0.3\ (\text{cooled})
$$

$$
\textbf{Gnielinski:}\ Nu_D=\frac{(f/8)(Re_D-1000)Pr}{1+12.7\sqrt{f/8}\,(Pr^{2/3}-1)},\quad
f=(0.79\ln Re_D-1.64)^{-2}
$$

Gnielinski works down to $Re\approx3000$ and across a wider $Pr$ range; Dittus–Boelter is quick for $Re>10^4$.

**Example.** Water at 300 K ($\rho=997$, $\mu=8.5\times10^{-4}$, $k=0.610$, $Pr=5.86$) at 1 m/s in a 20 mm tube:

| | $Re_D$ | $Nu_D$ | $h$ (W/m²K) |
| --- | --- | --- | --- |
| Dittus–Boelter (heating) | 23 300 | 146 | 4440 |
| Gnielinski ($f=0.0251$) | 23 300 | 158 | **4820** |
| laminar value, for contrast | | 3.66 | 112 |

Turbulence raises $h$ about 40 times. The two correlations differ by 8 %, within their stated scatter.

![[HT-4-convection.png]]

## 3. Bulk temperature and exit state

In a tube the fluid heats up along the way. For a constant wall temperature $T_s$:

$$
\frac{T_s-T_{out}}{T_s-T_{in}}=\exp\Big(-\frac{\bar h\,PL}{\dot m c_p}\Big)\qquad
Q=\dot mc_p(T_{out}-T_{in})=\bar hA\,\Delta T_{lm}
$$

with $\Delta T_{lm}=\dfrac{\Delta T_{in}-\Delta T_{out}}{\ln(\Delta T_{in}/\Delta T_{out})}$ (the same logarithmic mean as heat exchangers).

## 4. Method

1. Sketch the situation: plate, tube, cylinder, bank; evaluate $Re$ with the right length (L for a plate, D for tube/cylinder).
2. Laminar or turbulent? Pick the row.
3. Properties at $T_f$ (external) or bulk temperature (internal).
4. $Nu\to h\to q$; check the bulk temperature rise if the tube is long.

> [!warning] Traps
> - Using Dittus–Boelter at $Re<10^4$ or in a short entrance region ($L/D<10$): the developing flow has a higher $h$.
> - Using the Nusselt number of a tube for a flow in an annulus or non-circular duct without the hydraulic diameter $D_h=4A/P$.
> - Applying "turbulent from the leading edge" over a short plate: laminar flow persists until $Re_x=5\times10^5$.
> - Forgetting that $h$ for the laminar tube does not depend on velocity.

> [!question]- Predict first: doubling the water speed in the tube. By how much does $h$ rise?
> $h\propto Re^{0.8}$, so $2^{0.8}=1.74$: +74 %. The pressure drop rises about 4 times ($f\,V^2$), so a faster flow buys heat at a steeply rising pumping cost.

> [!question]- Laminar flow in the tube at constant $Nu=3.66$: how can doubling the diameter change $h$?
> $h=3.66\,k/D$, so doubling $D$ **halves** $h$. In the laminar regime a thinner tube transfers heat better (the temperature profile fills the whole tube), a reason for microchannel coolers.

## 5. Connections

- [[Pipe Flow and Losses - Formula Bank]] — the same $f$ and $Re$; the Reynolds analogy ties friction factor to $Nu$ (Gnielinski's $f/8$).
- [[Viscous Flow and Exact Solutions - Formula Bank]] — the Poiseuille profile in a tube gives the laminar constants 3.66 and 4.36.
- [[Dimensional Analysis and Similitude - Formula Bank]] — model testing at the same $Re$ and $Pr$ gives the same $Nu$.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — the exponential approach of the bulk temperature to $T_s$ is the same law with the thermal length $\dot mc_p/\bar hP$.
