---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME2102)"
aliases: [Refrigeration cycle, Vapour compression, COP, Heat pump, Refrigerant, R134a, Subcooling, Superheating, Cascade system, p-h diagram]
---

# Vapour-Compression Refrigeration and Heat Pumps

> [!abstract] In one breath
> A refrigerator moves heat from cold to hot by running a cycle backward, and a **vapour-compression cycle** does it with a refrigerant that evaporates in the cold space and condenses in the hot one. Four components, four points on a $p$–$h$ diagram, and one measure of performance: the **coefficient of performance**, COP $=q_L/w_c$, which can be above 1.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Brayton Cycle - Intercooling, Reheat and Regeneration]]. Next: [[Psychrometrics and Air-Conditioning Processes]].

## 1. The ideal cycle

| Process | Component | What happens |
| --- | --- | --- |
| 1→2 | compressor | isentropic compression of saturated vapour to $P_{cond}$ |
| 2→3 | condenser | heat rejected at constant pressure; desuperheat, condense to saturated liquid |
| 3→4 | expansion (throttle) valve | $h_4=h_3$; pressure falls, part of the liquid flashes |
| 4→1 | evaporator | heat absorbed at constant pressure and temperature; saturated vapour out |

$$
q_L=h_1-h_4,\quad w_c=h_2-h_1,\quad q_H=h_2-h_3,\qquad \text{COP}_R=\frac{q_L}{w_c},\quad \text{COP}_{HP}=\frac{q_H}{w_c}=\text{COP}_R+1
$$

The throttle is irreversible but cheap; an expander (turbine) would recover work but is impractical for a two-phase mixture. Upper bound: the Carnot value $COP_R=T_L/(T_H-T_L)$.

## 2. Worked example: R134a, evaporator at −10 °C, condenser at 40 °C

| State | Value |
| --- | --- |
| $P_{evap}$, $P_{cond}$, pressure ratio | 200.6 kPa, 1016.6 kPa, 5.07 |
| $h_1$ (sat. vapour at −10 °C) | 392.7 kJ/kg |
| $h_{2s}$ (isentropic compression, $T_2=46$ °C) | 426.5 kJ/kg |
| $h_3=h_4$ (sat. liquid at 40 °C) | 256.4 kJ/kg |
| quality at the evaporator inlet $x_4$ | 0.34 |
| refrigerating effect $q_L$ | **136.3 kJ/kg** |
| compressor work $w_c$ | **33.8 kJ/kg** |
| **COP** | **4.03** (Carnot 5.26) |
| heat pump COP | 5.03 |
| actual compressor ($\eta_c=0.80$) | COP **3.22** |
| with 5 K subcooling | COP **4.25** (+5.4 %) |

![[FTE-3-refrigeration.png]]

The flash fraction $x_4=0.34$ means a third of the liquid vaporises in the valve without absorbing any heat from the cold space: a loss that is the price of the throttle.

## 3. Practical improvements

- **Subcooling** the liquid below saturation (more liquid, lower $h_3$) raises $q_L$ at no compressor cost.
- **Superheating** the vapour ensures that no liquid reaches the compressor.
- **Liquid-suction heat exchanger:** the cold vapour leaving the evaporator subcools the liquid going to the valve.
- **Multistage compression with flash-chamber intercooling** (large pressure ratios; refrigerators below −30 °C) and **cascade systems** (two cycles with different refrigerants sharing a heat exchanger) for very low temperatures: see COP versus the Carnot limit.
- **Absorption refrigeration** uses heat instead of work.

## 4. Refrigerants

Required: suitable saturation pressures (positive and not too high at the evaporator and condenser temperatures), high latent heat, chemical stability, non-toxic and non-flammable, compatible with oil and metals, low **ozone-depletion** and **global-warming potential**. R12 and other CFCs are banned; **R134a** is being replaced by R1234yf, propane (R290), ammonia (R717, large industrial plants) and CO₂ (R744, transcritical).

> [!warning] Traps
> - Using $h_2=h_1$: the compressor adds $w_c$ to the enthalpy.
> - Letting the condenser temperature equal the sink temperature: it must be **above** it (and the evaporator below the cold space) so that heat flows.
> - Using the COP of a *heat pump* for a refrigerator or vice versa: $COP_{HP}=COP_R+1$.
> - Taking the throttle as isentropic: it is constant-enthalpy.
> - Treating COP as an efficiency less than 1.

> [!question]- Predict first: raise the condenser temperature from 40 °C to 50 °C. What happens to the COP?
> It falls: the pressure ratio rises (more compressor work) and the flash loss in the valve grows ($h_3$ is higher, so $q_L$ shrinks). Roughly 2–3 % COP per kelvin of temperature lift.

> [!question]- Why is a heat pump's COP above 1 acceptable?
> It moves heat rather than creating it: for 1 kWh of electricity it delivers about $COP_{HP}=5$ kWh of heat to the house, taking 4 kWh from the cold outdoors. An electric resistance heater gives 1.

## 5. Connections

- [[Exergy and Reversible Work]] — refrigeration is the reverse of a heat engine; second-law efficiency is $COP/COP_{Carnot}=4.03/5.26=77\ \%$.
- [[Heat Exchangers - LMTD and NTU]] and [[Boiling and Condensation]] — evaporator and condenser design.
- [[Psychrometrics and Air-Conditioning Processes]] — the cooling coil is the evaporator of this cycle.
- [[Conservation of Mass (Continuity Equation)]] — mass flow of refrigerant through every component is the same.
