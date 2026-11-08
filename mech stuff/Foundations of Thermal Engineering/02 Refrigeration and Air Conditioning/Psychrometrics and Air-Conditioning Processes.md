---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME2102)"
aliases: [Psychrometrics, Psychrometric chart, Humidity ratio, Relative humidity, Dew point, Wet-bulb temperature, Air conditioning, Cooling and dehumidification, Evaporative cooling]
---

# Psychrometrics and Air-Conditioning Processes

> [!abstract] In one breath
> Air is a mixture of dry air and water vapour, and comfort and drying depend on the vapour. Treat the **dry air** as the thing that flows (its mass flow is constant through any process) and carry the vapour as an extra: the **humidity ratio** $\omega$. Every air-conditioning process, cooling, heating, humidifying, dehumidifying, is a mass balance on water and an energy balance, drawn as a line on the **psychrometric chart**.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Vapour-Compression Refrigeration and Heat Pumps]]. Next: [[Otto, Diesel and Dual Cycles and Engine Performance]].

## 1. Properties of moist air

With total pressure $p$ and vapour partial pressure $p_v$:

| Property | Definition |
| --- | --- |
| **Humidity ratio** $\omega$ | $\dfrac{m_v}{m_a}=0.622\dfrac{p_v}{p-p_v}$ (kg vapour per kg dry air) |
| **Relative humidity** $\phi$ | $p_v/p_g(T)$, with $p_g$ the saturation pressure at the dry-bulb temperature |
| **Dew point** $T_{dp}$ | saturation temperature at $p_v$: the temperature at which dew first forms on cooling at constant $\omega$ |
| **Dry-bulb** $T$ | the ordinary thermometer |
| **Wet-bulb** $T_{wb}$ | a thermometer with a wet wick in moving air; evaporation cools it to a temperature set by $\omega$ (adiabatic saturation temperature, ≈) |
| **Enthalpy** (per kg dry air) | $h=c_{pa}T+\omega\,h_g\approx1.006\,T+\omega(2501+1.86\,T)$ kJ/kg, $T$ in °C |

For comfort, 22–26 °C and 40–60 % relative humidity.

## 2. The chart

A chart has $T$ on the horizontal axis, $\omega$ vertical, curves of constant $\phi$ (the 100 % curve is the saturation line), constant $h$ and $T_{wb}$ lines, and the specific volume. **Sensible** processes (heating or cooling at constant $\omega$) are horizontal; **latent** ones (adding or removing vapour) are vertical.

![[FTE-4-psychrometric.png]]

## 3. Worked example: cooling, dehumidifying and reheating

Outdoor air at 35 °C, 50 % ($p_g=5.63$ kPa):

| State | $T$ | $\phi$ | $\omega$ (g/kg) | $h$ (kJ/kg) |
| --- | --- | --- | --- | --- |
| 1 outdoor | 35 °C | 50 % | **17.8** | **80.8** |
| 2 after cooling coil | 14 °C | 100 % | **10.0** | **39.3** |
| 3 after reheat | 24 °C | **54 %** | 10.0 | 49.5 |

- $p_v=0.5\times5.63=2.81$ kPa, **dew point 23.0 °C**, wet-bulb 26.1 °C. The coil surface must be below 23 °C for the air to dehumidify at all.
- **Condensate:** $\omega_1-\omega_2=\mathbf{7.8\ g/kg}$ dry air (of the 17.8 g that came in).
- **Cooling load:** $q_{cool}=(h_1-h_2)-(\omega_1-\omega_2)h_f=\mathbf{41.1}$ kJ/kg dry air. Of this, only the part $c_p\Delta T$ is sensible: the **sensible heat ratio** is 0.53, so almost half of the work goes to taking moisture out.
- **Reheat** to 24 °C: $q_{reheat}=\mathbf{10.2}$ kJ/kg and the relative humidity rises to 54 %: comfortable.

Energy balance for a general component: $\dot m_a(h_1-h_2)=\dot Q+\dot m_{cond}h_f$ with the water balance $\dot m_{cond}=\dot m_a(\omega_1-\omega_2)$.

## 4. The standard processes

| Process | Line on the chart | Notes |
| --- | --- | --- |
| Sensible heating | horizontal, to the right | $\omega$ constant; $\phi$ falls |
| Sensible cooling | horizontal, to the left, down to the dew point | $\phi$ rises |
| **Cooling and dehumidification** | down and left along the coil line to saturation | needs coil temperature below the dew point |
| Humidification (steam) | nearly vertical | adds latent energy |
| **Evaporative cooling** | up and to the left along a constant-$h$ (wet-bulb) line | cheap in dry climates |
| **Adiabatic mixing** of two streams | straight line between the states, split by the dry-air mass ratio | |
| Cooling tower | water cooled to near the wet-bulb temperature | limit: $T_{wb}$ |

**Evaporative cooler example.** Air at 35 °C, 20 % ($\omega=7.0$ g/kg, wet-bulb 18.9 °C): a cooler of 90 % effectiveness supplies air at $35-0.9(35-18.9)=\mathbf{20.5\ ^\circ C}$. The air is cooler but wetter: useful when the wet-bulb is well below the dry-bulb, useless in humid weather.

## 5. Method

1. Locate each state from two properties ($T$, $\phi$ or $T_{wb}$).
2. Dry-air mass balance (equal in and out); water balance for $\omega$.
3. Energy balance with enthalpies from the chart or formula; include the condensate enthalpy $h_f=4.186\,T_{condensate}$ if liquid leaves.
4. The load: sensible $\dot m_a c_p\Delta T$, latent $\dot m_a\Delta\omega\,h_{fg}$.

> [!warning] Traps
> - Using the mass of **moist** air for the flow: use dry air (it is constant).
> - Cooling below the dew point and not removing the condensate from the balance.
> - Using relative humidity as the mass fraction of water: it is a ratio of pressures.
> - Confusing wet-bulb with dew-point temperature (dew point $\le$ wet-bulb $\le$ dry-bulb).
> - Heating to a higher temperature and expecting the dew point to change: heating at constant $\omega$ leaves the dew point unchanged.

> [!question]- Predict first: heat 24 °C, 60 % air to 30 °C without adding water. What happens to the relative humidity?
> It falls (to about 42 %): the vapour pressure is unchanged but $p_g$ at 30 °C (4.25 kPa) exceeds that at 24 °C (2.98 kPa). The dew point stays at about 15.8 °C.

> [!question]- Why does a cooling coil at 14 °C remove water but a coil at 25 °C does not?
> Air at 35 °C/50 % has a dew point of 23 °C. Only if the coil surface is below that does vapour condense on it. At 25 °C the coil only cools the air sensibly.

## 6. Connections

- [[Vapour-Compression Refrigeration and Heat Pumps]] — the coil is the evaporator; the latent load is part of the refrigerating effect.
- [[Conservation of Mass (Continuity Equation)]] and [[Reynolds Transport Theorem]] — mass balance on dry air and water.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — in a cooling tower or evaporative cooler the approach to the wet-bulb temperature is exponential in tower height.
- [[Natural Convection]] and [[Forced Convection Correlations]] — heat and mass transfer on a coil use the same correlations (Lewis analogy).
