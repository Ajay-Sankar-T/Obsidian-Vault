---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Heat exchanger, LMTD method, NTU method, Effectiveness-NTU, Counterflow, Parallel flow, Overall heat transfer coefficient]
---

# Heat Exchangers — LMTD and NTU

> [!abstract] In one breath
> A heat exchanger moves heat between two streams through a wall: $Q=UA\,\Delta T_{lm}$. Use the **LMTD method to size** it when all four terminal temperatures are known, and the **$\varepsilon$–NTU method to rate** it when only the inlet temperatures and the exchanger are known. Both rest on the same energy balances.

Part of [[Heat Transfer - MOC]]. Previous: [[Thermal Radiation - Laws, View Factors and Networks]].

## 1. The three equations

Energy balance on each stream (no loss to the surroundings), with heat-capacity rates $C=\dot mc_p$:

$$
Q=C_h(T_{h,in}-T_{h,out})=C_c(T_{c,out}-T_{c,in})=UA\,\Delta T_{lm}
$$

$U$ comes from the resistance chain wall–films–fouling: $\dfrac{1}{UA}=\dfrac{1}{h_iA_i}+\dfrac{R_{f,i}}{A_i}+\dfrac{\ln(r_o/r_i)}{2\pi kL}+\dfrac{R_{f,o}}{A_o}+\dfrac{1}{h_oA_o}$.

## 2. LMTD (sizing)

Because the stream temperatures change exponentially along the length, the right average temperature difference is logarithmic:

$$
\Delta T_{lm}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)},\qquad
\begin{cases}\text{counterflow: }\Delta T_1=T_{h,in}-T_{c,out},\ \Delta T_2=T_{h,out}-T_{c,in}\\
\text{parallel flow: }\Delta T_1=T_{h,in}-T_{c,in},\ \Delta T_2=T_{h,out}-T_{c,out}\end{cases}
$$

For crossflow and multipass shell-and-tube exchangers multiply by a correction factor $F<1$ from charts: $Q=UAF\,\Delta T_{lm,\,cf}$. **Counterflow gives the largest $\Delta T_{lm}$** for given terminal temperatures, so the smallest area.

**Example.** Hot oil ($\dot m=2$ kg/s, $c_p=2100$) cooled from 120 to 70 °C by water ($\dot m=2.5$, $c_p=4180$) entering at 20 °C; $U=400$ W/m²K.

$$
Q=2(2100)(50)=210\ \text{kW},\qquad T_{c,out}=20+\frac{210\,000}{2.5\times4180}=40.1^\circ\text{C}
$$

| | $\Delta T_1$ | $\Delta T_2$ | $\Delta T_{lm}$ | Area $A=Q/(U\Delta T_{lm})$ |
| --- | --- | --- | --- | --- |
| counterflow | 79.9 | 50.0 | **63.8 K** | **8.23 m²** |
| parallel flow | 100.0 | 29.9 | 58.1 K | 9.04 m² |

Parallel flow needs 10 % more area for the same duty, and can never bring the cold stream above the hot outlet.

## 3. $\varepsilon$–NTU (rating)

Let $C_{min}=\min(C_h,C_c)$, $C_r=C_{min}/C_{max}$, and

$$
\varepsilon=\frac{Q}{Q_{max}}=\frac{Q}{C_{min}(T_{h,in}-T_{c,in})},\qquad NTU=\frac{UA}{C_{min}}
$$

| Flow arrangement | $\varepsilon(NTU,C_r)$ |
| --- | --- |
| Counterflow | $\dfrac{1-e^{-NTU(1-C_r)}}{1-C_re^{-NTU(1-C_r)}}$ ($C_r=1$: $\dfrac{NTU}{1+NTU}$) |
| Parallel flow | $\dfrac{1-e^{-NTU(1+C_r)}}{1+C_r}$ |
| Any exchanger, $C_r=0$ (boiling or condensing) | $1-e^{-NTU}$ |

Then $Q=\varepsilon\,C_{min}(T_{h,in}-T_{c,in})$ and the outlet temperatures follow from the energy balances, **with no iteration**, which is the point of the method.

**Same example, rated.** $C_h=4200$ (this is $C_{min}$), $C_c=10\,450$ W/K, $C_r=0.402$, $A=8.23$ m² gives $NTU=0.784$, counterflow $\varepsilon=\mathbf{0.50}$, so $Q=0.50(4200)(100)=210$ kW ✓ and the oil leaves at $120-210/4.2=70$ °C ✓. The two methods agree.

![[HT-7-exchangers.png]]

On the left, the $\varepsilon$ curves flatten at large NTU: doubling the area at $NTU=3$ buys almost nothing. For $C_r=1$ and $NTU=1$, counterflow gives only 0.50.

## 4. Choosing the method

| Known | Unknown | Use |
| --- | --- | --- |
| all four temperatures and $U$ | area | LMTD |
| inlet temperatures, $UA$, flow rates | outlet temperatures, $Q$ | NTU |
| inlet temperatures, required duty | area | NTU (find $NTU$ from $\varepsilon$) |

> [!warning] Traps
> - Using the arithmetic mean temperature difference: it overestimates $Q$ when $\Delta T_1/\Delta T_2$ is large.
> - Writing $\Delta T_1,\Delta T_2$ for counterflow as in parallel flow.
> - Taking $C_{min}$ as the lower flow rate rather than the lower $\dot mc_p$: water and oil have different $c_p$.
> - Applying $\varepsilon$ formulas for counterflow to a crossflow exchanger.
> - Leaving out fouling resistance when the question gives it.

> [!question]- Predict first: condensing steam at 100 °C heats water. $C_r$? Does the flow arrangement matter?
> The steam has $C\to\infty$ so $C_{min}$ is the water and $C_r=0$. Then $\varepsilon=1-e^{-NTU}$ for **every** arrangement; the steam temperature stays at 100 °C, so parallel, counter and cross flow perform identically.

> [!question]- Why is the LMTD smaller than the arithmetic mean?
> The temperature difference falls exponentially, so the average of the logarithmic profile lies below the straight-line mean. The two are equal only when $\Delta T_1=\Delta T_2$.

## 5. Connections

- [[Heat Transfer - MOC]] — pulls together conduction (wall), convection (films) and boiling or condensation (latent streams).
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — the stream temperatures approach each other exponentially along the length: $NTU$ is the number of "time constants" in the exchanger.
- [[Steady Conduction and Thermal Resistance Networks]] — the $UA$ chain is a series resistance network.
- [[Foundations of Thermal Engineering - MOC]] — condensers, boilers and regenerators in cycles are heat exchangers; intercoolers and recuperators in a Brayton cycle use exactly this.
- [[Forced Convection Correlations]] — tube-side $h$ for the films.
