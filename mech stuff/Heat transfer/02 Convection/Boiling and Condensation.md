---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Pool boiling, Nukiyama curve, Critical heat flux, Film condensation, Nusselt condensation, Dropwise condensation]
---

# Boiling and Condensation

> [!abstract] In one breath
> Phase change moves heat with the **latent heat** $h_{fg}$, so $h$ is 10–100 times a single-phase value. Boiling follows the **boiling curve**: heat flux rises with the excess temperature until a **critical heat flux** after which a vapour film insulates the surface (burnout). Condensation is a falling liquid film whose thickness, not the vapour, sets the resistance.

Part of [[Heat Transfer - MOC]]. Previous: [[Natural Convection]]. Next: [[Thermal Radiation - Laws, View Factors and Networks]].

## 1. Pool boiling regimes

Water at 1 atm on a heated surface of temperature $T_s$; excess temperature $\Delta T_e=T_s-T_{sat}$:

| Regime | $\Delta T_e$ | What happens |
| --- | --- | --- |
| Natural convection | < 5 K | liquid carries the heat, no bubbles |
| **Nucleate boiling** | 5–30 K | bubbles form at nucleation sites; mixing gives very high $h$ |
| **Critical heat flux** | ≈ 20–30 K | vapour columns merge; maximum flux |
| Transition | 30–120 K | unstable film patches; flux falls |
| **Film boiling** | > 120 K | steady vapour blanket; low $h$ (radiation helps) |

Heat flux is the controlled quantity in a heater (electric, nuclear): beyond the critical flux the surface jumps to film boiling at a temperature that may exceed the melting point (**burnout**).

## 2. Correlations

**Nucleate boiling (Rohsenow):**

$$
q''=\mu_l h_{fg}\sqrt{\frac{g(\rho_l-\rho_v)}{\sigma}}\Bigg[\frac{c_{p,l}\Delta T_e}{C_{sf}\,h_{fg}\,Pr_l^{\,n}}\Bigg]^3
$$

$C_{sf}\approx0.013$ and $n=1$ for water on polished copper. $q''\propto\Delta T_e^3$: ten percent more superheat gives about 33 % more flux.

**Critical heat flux (Zuber):**

$$
q''_{max}=0.131\,\rho_v^{1/2}h_{fg}\big[\sigma g(\rho_l-\rho_v)\big]^{1/4}
$$

**Film condensation on a vertical plate (Nusselt):**

$$
\bar h=0.943\Bigg[\frac{g\rho_l(\rho_l-\rho_v)k_l^3\,h_{fg}'}{\mu_lL(T_{sat}-T_s)}\Bigg]^{1/4},\qquad
h_{fg}'=h_{fg}+0.68\,c_{p,l}(T_{sat}-T_s)
$$

Liquid properties at $T_f=(T_{sat}+T_s)/2$. Horizontal tube: the same form with a coefficient 0.729 and $D$ replacing $L$. The film is laminar for $Re_\delta=4\dot m/\mu<30$ and wavy above; the formula is then slightly conservative.

## 3. Worked examples (water at 1 atm)

| Quantity | Value |
| --- | --- |
| $\rho_l,\ \rho_v$ | 958 and 0.598 kg/m³ |
| $h_{fg}$ | 2256 kJ/kg |
| $\sigma$ | 0.0589 N/m |
| **Zuber CHF** | **1.11 MW/m²** |
| Rohsenow at $\Delta T_e=10$ K | 140 kW/m² |
| $\Delta T_e$ at the CHF | ≈ 20 K |

The nucleate branch is steep: 10 K gives 140 kW/m², 20 K reaches the critical flux of 1.1 MW/m².

![[HT-5-boiling.png]]

**Condensation.** Steam at 100 °C on a 1 m vertical plate at 80 °C: $h_{fg}'=2314$ kJ/kg and

$$
\bar h=\mathbf{5300\ W/m^2K},\quad q''=107\ \text{kW/m}^2,\quad
\dot m'=\frac{q''}{h_{fg}'}=0.046\ \text{kg/(s·m)},\quad Re_\delta=587
$$

(wavy-laminar, so the laminar formula is a bit low). Compare 5.6 W/m²K for air by natural convection: condensation is about a thousand times better.

> [!warning] Traps
> - Using the **surface** temperature instead of the excess $T_s-T_{sat}$ in Rohsenow.
> - Treating the critical heat flux as a temperature: it is a flux, and it fixes the safe operating limit.
> - Using steam properties for the liquid film in Nusselt's formula: the liquid is at $T_f$, below $T_{sat}$.
> - Non-condensable gas (air) in condensers: even 1 % air lowers $h$ many times by blanketing the surface.

> [!question]- Predict first: a surface held at 300 °C in water at 1 atm. Is it in nucleate boiling?
> No. $\Delta T_e=200$ K is far beyond the critical flux region: it is in **film boiling**, a stable vapour film with low $h$. A hot forging dropped in water behaves the same way (Leidenfrost effect).

> [!question]- Why does dropwise condensation give an order of magnitude higher $h$ than film condensation?
> There is no continuous liquid film; drops coalesce, roll off and re-expose bare surface, so the thermal resistance of the film that sets $\bar h$ is missing. Hard to maintain, so designs use film values.

## 4. Connections

- [[Natural Convection]] — buoyancy of the vapour is what drives bubble departure and the Zuber hydrodynamic argument.
- [[Viscous Flow and Exact Solutions - Solved Problems]] — the condensate film is the lava film of problem 2 (a gravity-viscous balance, $u\propto\rho g\delta^2/\mu$), with the surface speed set by the film thickness.
- [[Foundations of Thermal Engineering - MOC]] — the saturation properties and $h_{fg}$ come from the steam tables; condensers close the Rankine cycle.
- [[Dimensional Analysis and Similitude - Formula Bank]] — Jakob number $Ja=c_p\Delta T/h_{fg}$ compares sensible and latent heat.
