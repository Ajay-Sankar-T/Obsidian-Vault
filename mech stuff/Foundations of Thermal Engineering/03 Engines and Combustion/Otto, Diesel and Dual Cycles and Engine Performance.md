---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME3105)"
aliases: [Otto cycle, Diesel cycle, Dual cycle, IC engine, Mean effective pressure, bmep, Brake power, Compression ratio, Four-stroke engine, Engine performance, bsfc]
---

# Otto, Diesel and Dual Cycles and Engine Performance

> [!abstract] In one breath
> The **air-standard** cycles model an internal-combustion engine as air receiving heat. In the **Otto** (spark-ignition) cycle heat is added at constant volume: $\eta=1-r^{1-\gamma}$. In the **Diesel** cycle it is added at constant pressure, so at the same compression ratio it is less efficient, but diesel engines run at a much higher compression ratio and win. The **dual** cycle splits the heat. Performance of a real engine is measured by **brake power**, **bmep** and **brake specific fuel consumption**.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Psychrometrics and Air-Conditioning Processes]]. Next: [[Combustion - Stoichiometry, Heating Value and Flame Temperature]].

## 1. The cycles

| Cycle | Heat addition | Efficiency (cold-air standard) |
| --- | --- | --- |
| **Otto** | constant volume | $\eta=1-\dfrac{1}{r^{\gamma-1}}$ |
| **Diesel** | constant pressure, cut-off ratio $r_c=v_3/v_2$ | $\eta=1-\dfrac{1}{r^{\gamma-1}}\,\dfrac{r_c^{\gamma}-1}{\gamma(r_c-1)}$ |
| **Dual** | constant volume, then constant pressure; pressure ratio $\alpha=p_3/p_2$ | $\eta=1-\dfrac{1}{r^{\gamma-1}}\,\dfrac{\alpha r_c^{\gamma}-1}{(\alpha-1)+\gamma\alpha(r_c-1)}$ |

The factor $(r_c^\gamma-1)/[\gamma(r_c-1)]>1$ makes the Diesel less efficient than an Otto of the same $r$; it tends to 1 as $r_c\to1$ and the cycles coincide.

Spark-ignition engines are limited to $r\approx8$–12 by **knock** (the air-fuel mixture would self-ignite on compression); diesel engines compress air only and inject the fuel at the top, so $r=14$–22.

![[FTE-5-engines.png]]

## 2. Worked examples

**Otto, $r=9$, $\gamma=1.4$:** $\eta=1-9^{-0.4}=\mathbf{0.585}$. With $T_1=300$ K, $p_1=100$ kPa, heat added $q_{in}=1800$ kJ/kg ($c_v=0.718$):

$$
T_2=300(9)^{0.4}=722\ \text{K},\quad T_3=722+\frac{1800}{0.718}=3229\ \text{K},\quad T_4=3229/9^{0.4}=1341\ \text{K}
$$

$$
w_{net}=q_{in}-c_v(T_4-T_1)=\mathbf{1053\ kJ/kg},\quad
\text{mep}=\frac{w_{net}}{v_1-v_2}=\frac{1053}{0.861-0.0957}=\mathbf{1375\ kPa},\quad p_{max}=9690\ \text{kPa}
$$

The mean effective pressure (the constant pressure that would give the same work over the swept volume) is the right way to compare engines of different sizes.

**Diesel, $r=18$, $r_c=2$:** $\eta=\mathbf{0.632}$; an Otto at the same $r=18$ would give 0.685, but cannot run there. **Dual** with $r=18$, $r_c=2$, $\alpha=1.5$: $\eta=\mathbf{0.642}$, with a lower peak pressure than constant-volume heating.

## 3. Real engines: four-stroke operation

Intake, compression, power, exhaust: two crankshaft revolutions per cycle ($n_R=2$; a two-stroke has $n_R=1$). **Valve timing** (intake opens before TDC, closes after BDC; exhaust opens before BDC) and the **port timing** of a two-stroke are drawn on a circular diagram. Real efficiencies are 25–35 % (petrol), 35–45 % (diesel), well below the air-standard values because of heat loss, finite burn time, incomplete combustion, friction and gas exchange.

**Performance parameters:**

$$
P_b=2\pi N T_b,\qquad \text{bmep}=\frac{P_b\,n_R}{V_dN},\qquad \eta_b=\frac{P_b}{\dot m_fQ_{LHV}},\qquad \text{bsfc}=\frac{\dot m_f}{P_b},\qquad \eta_{mech}=\frac{P_b}{P_{ind}}
$$

($N$ in rev/s, $V_d$ the displaced volume, $T_b$ the brake torque.)

**Example.** 4-stroke, 2.0 L, 4000 rpm, brake torque 180 N·m, fuel 5.0 g/s with LHV 44 MJ/kg:

| Quantity | Value |
| --- | --- |
| brake power | **75.4 kW** |
| bmep | $75.4\times10^3(2)/(2\times10^{-3}\times66.7)=\mathbf{1.13\ MPa}$ |
| brake thermal efficiency | $75.4/(0.005\times44\,000)=\mathbf{0.343}$ |
| bsfc | $5.0\times3600/75.4=\mathbf{239\ g/kWh}$ |

## 4. Emissions and alternatives

Pollutants: **CO** and **HC** (rich or incomplete burn), **NOₓ** (high temperature, lean), **soot/particulates** (diesel), CO₂. Three-way catalysts need stoichiometric operation. **Alternate fuels:** ethanol and biodiesel (renewable, lower energy density), natural gas, **hydrogen** (high flame speed, wide flammability, NOₓ and storage issues). **Hybrid electric vehicles** use the engine at its efficient operating points and recover braking energy.

> [!warning] Traps
> - Using the Otto formula for a Diesel engine.
> - Comparing Otto and Diesel at the same compression ratio and concluding Otto is better in practice.
> - Taking $n_R=1$ for a four-stroke: it is 2.
> - Mixing indicated and brake values: bmep uses **brake** power.
> - Using LHV and HHV interchangeably in $\eta_b$ (quote which).

> [!question]- Predict first: increase the Otto compression ratio from 9 to 11. How much does the ideal efficiency rise?
> $\eta=1-11^{-0.4}=0.617$, from 0.585: **+3.2 points**. Diminishing returns: knock and heat loss stop the real gain.

> [!question]- Why can a diesel engine run at a higher compression ratio than a petrol engine?
> It compresses only air; there is no fuel to knock. Fuel is injected near top dead centre and ignites on contact with the hot compressed air.

## 5. Connections

- [[Combustion - Stoichiometry, Heating Value and Flame Temperature]] — the heat input $q_{in}$ and the fuel energy.
- [[Kinetics of Particles - Work-Energy and Impulse-Momentum]] and [[Mass Moments of Inertia]] — the crank mechanism and flywheel smooth the power pulses: [[Flywheel Sizing from the Turning-Moment Diagram]].
- [[Balancing of Rotors - Static and Dynamic]] — engine balancing of reciprocating masses.
- [[Kinematic Inversion - Slider-Crank and Double-Slider Families]] — the slider-crank is the engine's kinematics.
