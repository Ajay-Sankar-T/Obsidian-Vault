---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME3105)"
aliases: [Combustion, Stoichiometry, Air-fuel ratio, Equivalence ratio, Heating value, LHV, HHV, Adiabatic flame temperature, Enthalpy of formation]
---

# Combustion — Stoichiometry, Heating Value and Flame Temperature

> [!abstract] In one breath
> Combustion is a chemical reaction treated with **mass balances** (how much air per kg of fuel), the **first law** (how much energy comes out) and one more idea: the **adiabatic flame temperature**, the temperature the products reach if all the released energy goes into heating them.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Otto, Diesel and Dual Cycles and Engine Performance]]. Next: [[Turbomachines - Euler Equation and Velocity Triangles]].

## 1. Stoichiometry

Air is taken as 21 % O₂ and 79 % N₂ by mole: **3.76 mol N₂ per mol O₂**, so 4.76 mol air per mol O₂, with a mean molar mass 28.97 kg/kmol. Balance atoms for **complete combustion** to CO₂ and H₂O:

$$
\text{CH}_4+2(\text{O}_2+3.76\,\text{N}_2)\to\text{CO}_2+2\,\text{H}_2\text{O}+7.52\,\text{N}_2
$$

$$
\text{C}_8\text{H}_{18}+12.5(\text{O}_2+3.76\,\text{N}_2)\to8\,\text{CO}_2+9\,\text{H}_2\text{O}+47\,\text{N}_2
$$

**Air–fuel ratio (mass):** $AF=\dfrac{n_{air}M_{air}}{n_{fuel}M_{fuel}}$. Methane: $2(4.76)(28.97)/16.04=\mathbf{17.2}$; octane: $12.5(4.76)(28.97)/114.2=\mathbf{15.1}$ kg air per kg fuel (the **stoichiometric** or theoretical values). More air than that is **excess air**; the **equivalence ratio** is $\phi=AF_{stoich}/AF_{actual}$: $\phi<1$ lean, $>1$ rich. The dry-product analysis (Orsat) tells the actual air supply: measured CO₂ and O₂ in the exhaust fix the excess air.

## 2. First law and heating value

For a steady-flow burner with products leaving at the reactant temperature, the heat released is $q=h_R-h_P=-\Delta H^\circ_{comb}$ with enthalpies of formation: $\Delta H=\sum_Pn\,h_f^\circ-\sum_Rn\,h_f^\circ$.

| Species | $h_f^\circ$ (kJ/mol) |
| --- | --- |
| CO₂ | −393.52 |
| H₂O (gas) | −241.83 |
| H₂O (liquid) | −285.83 |
| CH₄ (g) | −74.87 |
| C₈H₁₈ (l) | −249.90 |

- **Higher heating value (HHV):** water in the products condensed. **Lower heating value (LHV):** water as vapour (the one used for engines, since exhaust is hot).
- **Methane:** $\text{LHV}=393.52+2(241.83)-74.87=\mathbf{802.3\ kJ/mol}=\mathbf{50.0\ MJ/kg}$; $\text{HHV}=890.3$ kJ/mol (the difference is $2h_{fg}$).
- **Octane (liquid):** $\text{LHV}=8(393.52)+9(241.83)-249.90=5075$ kJ/mol $=\mathbf{44.4\ MJ/kg}$.

For reactants and products at a different temperature, add the sensible enthalpies: $h=h_f^\circ+(h(T)-h(298))$.

## 3. Adiabatic flame temperature

With no heat loss and no work, $H_R=H_P$: the heat released heats the products:

$$
\sum_Pn_i\big[h^\circ_{f,i}+\Delta h_i(T_{ad})\big]=\sum_Rn_i\,h^\circ_{f,i}\ \Longrightarrow\ \sum_Pn_i\,\Delta h_i(T_{ad})=\text{LHV}\ (\text{per mol of fuel, reactants at }298\ \text{K})
$$

Solve for $T_{ad}$ with temperature-dependent specific heats. (Property data, e.g. from the ideal-gas part of the CO₂, H₂O and N₂ equations of state in `Tools/fte_core.py`.)

| Mixture (methane–air, air at 298 K) | $T_{ad}$ |
| --- | --- |
| stoichiometric ($\phi=1$) | **2327 K** |
| 43 % excess air ($\phi=0.7$) | **1846 K** |
| 100 % excess air ($\phi=0.5$) | **1481 K** |

Excess air dilutes the heat across more nitrogen and cools the flame: gas turbines run lean for exactly this reason (turbine-inlet temperature limits). The real stoichiometric flame is lower, about 2230 K, because of **dissociation** (CO₂ → CO + ½O₂, H₂O → H₂ + ½O₂, which absorb energy at high temperature) and heat loss; the peak temperature is near $\phi\approx1.05$.

## 4. Practical consequences

- Complete combustion needs enough air and good mixing; deficiency gives **CO** and soot.
- **Rich** or **lean** limits (flammability limits) bound the mixture that will burn at all; SI engines operate near $\phi=1$, diesels are lean overall.
- High flame temperature raises **NOₓ** (thermal NO forms above about 1800 K), so lean-burn or exhaust-gas recirculation reduces it.
- Energy balance on an engine or boiler: fuel energy = work + exhaust loss + cooling and radiation loss.

> [!warning] Traps
> - Using air as pure oxygen: remember the 3.76 mol of N₂ that comes with every mole of O₂.
> - Mixing mass and molar air–fuel ratios.
> - Using HHV in an engine efficiency without saying so (LHV is the convention).
> - Forgetting that excess air changes the product mix (extra O₂ and N₂), not just the amount of air.
> - Taking the adiabatic flame temperature as the real one: heat loss and dissociation lower it.

> [!question]- Predict first: burn methane with 100 % excess air instead of stoichiometric. Will the flame be half as hot?
> No: 1481 K against 2327 K. The temperature *rise* above 298 K falls from 2029 K to 1183 K (−42 %), not by half, because the same 802 kJ now heats 20 mol of products instead of 10.5 mol (the heat capacity of the products nearly doubles, while a hotter gas has a higher $c_p$ per mole, which softens the fall).

> [!question]- Why is the LHV of methane used for a gas turbine and not the HHV?
> The exhaust leaves hot and the water stays as vapour: its latent heat is never recovered, so the usable heat is the lower value (802 against 890 kJ/mol).

## 5. Connections

- [[Otto, Diesel and Dual Cycles and Engine Performance]] — the heat release feeding the cycle.
- [[Exergy and Reversible Work]] — combustion destroys a quarter of the fuel's exergy: heat at 2300 K is degraded to heat used at 800 K.
- [[Conservation of Mass (Continuity Equation)]] — atom balances are mass conservation per element.
- [[Energy Methods - A Unified View]] — the first law including chemical energy.
