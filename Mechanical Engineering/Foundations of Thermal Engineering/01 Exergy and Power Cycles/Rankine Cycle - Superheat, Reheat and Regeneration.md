---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME2102)"
aliases: [Rankine cycle, Steam power plant, Reheat, Regeneration, Feedwater heater, Superheat, Steam turbine cycle]
---

# Rankine Cycle — Superheat, Reheat and Regeneration

> [!abstract] In one breath
> The Rankine cycle is the steam power plant: **pump** the liquid up in pressure (cheap, because liquid is nearly incompressible), **boil and superheat** it, **expand** it through a turbine, **condense** it. Efficiency improves when the *average temperature of heat addition* rises and the *temperature of heat rejection* falls: the three upgrades (superheat, reheat, regeneration) are all ways of doing that.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Exergy and Reversible Work]]. Next: [[Brayton Cycle - Intercooling, Reheat and Regeneration]].

## 1. The ideal cycle

| Process | What | Equation (per kg) |
| --- | --- | --- |
| 1→2 | isentropic pump | $w_p=v_1(P_2-P_1)$, $h_2=h_1+w_p$ |
| 2→3 | boiler: heat at constant $P$ (preheat, boil, superheat) | $q_{in}=h_3-h_2$ |
| 3→4 | isentropic turbine | $w_t=h_3-h_4$, $s_4=s_3$ |
| 4→1 | condenser: heat rejection at constant $P$ (and $T$) | $q_{out}=h_4-h_1$ |

$$
\eta_{th}=\frac{w_t-w_p}{q_{in}}=1-\frac{q_{out}}{q_{in}},\qquad \text{back-work ratio }\frac{w_p}{w_t}\ll1\ (\text{here }0.6\ \%)
$$

## 2. Worked example (properties from steam tables)

Boiler 8 MPa and 500 °C ($T_{sat}=295$ °C), condenser 10 kPa ($T_{sat}=45.8$ °C):

| Cycle | $q_{in}$ (kJ/kg) | net work (kJ/kg) | $\eta$ | exhaust quality |
| --- | --- | --- | --- | --- |
| **Simple** | 3200 | 1261 ($w_t=1269$, $w_p=8.1$) | **0.394** | 0.81 |
| **Reheat** at 1.5 MPa to 500 °C | 3741 | 1533 | **0.410** | **0.92** |
| **Regenerative**, one open feedwater heater at 1 MPa | 2629 | 1107 | **0.421** | |
| Carnot between 500 °C and 45.8 °C | | | 0.587 | |
| Simple, with $\eta_t=0.85$, $\eta_p=0.80$ | | | 0.334 | 0.89 |

The Carnot efficiency is far higher because the water is heated over a range of temperatures from 46 °C up to 500 °C, while Carnot takes all heat at the top.

![[FTE-1-rankine.png]]

## 3. The three upgrades

**Higher boiler pressure and temperature.** Raising $P_b$ raises the mean temperature of heat addition but pushes the exhaust wetter; raising $T_{max}$ (superheat) raises efficiency *and* dries the exhaust. Limits: metallurgy of the boiler tubes and turbine blades (around 600 °C).

**Lower condenser pressure.** Lowers the heat-rejection temperature (10 kPa: 46 °C). Limit: the cooling water temperature and the air leakage into the vacuum.

**Reheat.** Expand to an intermediate pressure, return the steam to the boiler to be reheated to $T_{max}$, then finish the expansion. It raises the exhaust quality from 0.81 to 0.92 (limit about 0.9 to protect the last blades from erosion by drops) and allows a higher boiler pressure. Efficiency gain is modest (here 0.394 → 0.410).

**Regeneration.** Bleed some steam from the turbine to heat the feedwater. The feedwater enters the boiler warm, so heat is added at a higher mean temperature. With an **open** feedwater heater (mixing) at 1 MPa the bled fraction is $y=(h_f-h_2)/(h_{ext}-h_2)=0.215$: 21.5 % of the steam bypasses the low-pressure turbine and the condenser, and $\eta$ rises to 0.421. A **closed** heater keeps the streams separate (needs a drain pump or trap); real plants use 5–8 heaters. In the ideal limit with infinitely many heaters regeneration approaches Carnot efficiency for the heat-addition process.

**Combined effect.** Superheat, reheat and several heaters give 40–45 % in modern subcritical plants and over 45 % in supercritical ones.

## 4. Real cycle

Irreversibilities: turbine and pump efficiency (the steam leaves with higher entropy and drier than ideal), pressure drop in pipes and boiler, heat loss. With $\eta_t=0.85$ the net work falls and $\eta$ from 0.394 to 0.334, but the exhaust is drier (0.89 against 0.81).

> [!warning] Traps
> - Using the saturated-liquid enthalpy $h_f$ as $h_2$: the pump adds $w_p=v\Delta P$.
> - Taking the turbine exit from the **same enthalpy** instead of the same entropy.
> - Forgetting the mass fraction $(1-y)$ in the low-pressure turbine and the pump after a feedwater heater.
> - Using reheat to increase efficiency a lot: its main role is to dry the exhaust.
> - Using $x_4<0.85$ without noting blade erosion.

> [!question]- Predict first: raise the boiler pressure at fixed $T_{max}$ = 500 °C. What happens to $\eta$ and to the exhaust quality?
> $\eta$ rises (higher mean heat-addition temperature) but the exhaust gets *wetter* (the expansion starts from a lower-entropy state). This is the motivation for reheat in high-pressure plants.

> [!question]- Why is the pump work only 0.6 % of the turbine work?
> The liquid has specific volume $10^{-3}$ m³/kg against about 10 m³/kg for the steam: compressing a liquid takes about a thousandth of the work of compressing the vapour. That is why steam, not gas, is the working fluid of large plants.

## 5. Connections

- [[Exergy and Reversible Work]] — heat transfer across a large $\Delta T$ in the boiler destroys exergy; regeneration reduces it.
- [[Heat Exchangers - LMTD and NTU]] and [[Boiling and Condensation]] — boiler and condenser.
- [[Linear Momentum Equation]] and [[Momentum Equation Applications - Jets, Vanes, Bends]] — the turbine converts the nozzle's momentum into shaft work ([[Turbomachines - Euler Equation and Velocity Triangles]]).
- [[Conservation Laws and Flow Networks]] — every component is a node with mass and energy balances.
