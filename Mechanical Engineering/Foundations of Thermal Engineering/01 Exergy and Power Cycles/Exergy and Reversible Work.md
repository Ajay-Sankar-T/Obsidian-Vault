---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME2102)"
aliases: [Exergy, Availability, Reversible work, Exergy destruction, Second-law efficiency, Dead state, Gouy-Stodola]
---

# Exergy and Reversible Work

> [!abstract] In one breath
> The first law counts energy; it cannot tell a joule of electricity from a joule of lukewarm water. **Exergy** is the *useful* part: the maximum work you can get from a system as it comes to equilibrium with the environment (the **dead state**, $T_0,P_0$). Every irreversibility destroys exergy in proportion to the entropy it generates: $X_{dest}=T_0S_{gen}$.

Part of [[Foundations of Thermal Engineering - MOC]]. Next: [[Rankine Cycle - Superheat, Reheat and Regeneration]].

## 1. Definitions

With the environment at $T_0=298$ K, $P_0=101.3$ kPa:

| Quantity | Exergy |
| --- | --- |
| Heat $Q$ at constant $T$ | $X_Q=Q\Big(1-\dfrac{T_0}{T}\Big)$ (the work of a reversible engine between $T$ and $T_0$) |
| Flowing fluid (**flow exergy**, per mass) | $\psi=(h-h_0)-T_0(s-s_0)+\dfrac{V^2}{2}+gz$ |
| Closed system | $\phi=(u-u_0)-T_0(s-s_0)+P_0(v-v_0)$ |
| Shaft work | all of it is exergy |

**Exergy balance** for a control volume at steady state:

$$
0=\sum\Big(1-\frac{T_0}{T_k}\Big)\dot Q_k-\dot W+\sum\dot m_{in}\psi_{in}-\sum\dot m_{out}\psi_{out}-\dot X_{dest},\qquad \dot X_{dest}=T_0\dot S_{gen}\ge0
$$

**Second-law efficiency:** $\eta_{II}=\dfrac{\text{exergy recovered}}{\text{exergy supplied}}=1-\dfrac{X_{dest}}{X_{in}}$. A turbine's isentropic efficiency is a measure of the same loss.

## 2. Worked examples

**Heat is not all work.** 1000 kJ of heat at 1000 K has exergy $1000(1-298/1000)=\mathbf{702\ kJ}$: no engine can turn it into more than 702 kJ of work with the environment at 298 K.

**Destroyed by heat transfer.** Move 1000 kJ from a reservoir at 1000 K to one at 500 K. Energy is conserved, but

$$
S_{gen}=Q\Big(\frac1{500}-\frac1{1000}\Big)=1.0\ \text{kJ/K},\qquad X_{dest}=T_0S_{gen}=\mathbf{298\ kJ}
$$

The exergy of the heat fell from 702 to 404 kJ; the difference, 298 kJ, is the work potential thrown away by letting heat flow across a finite temperature difference.

**Flow exergy of steam.** Steam at 5 MPa, 400 °C: $h-h_0=3092$ kJ/kg against liquid at 25 °C, yet $\psi=\mathbf{1219\ kJ/kg}$: only 39 % of the enthalpy can be turned into work.

**Throttling** that steam to 1 MPa: $h$ is unchanged, but entropy rises and $\mathbf{213\ kJ/kg}$ of exergy is destroyed: a valve is a pure exergy loss.

**An adiabatic turbine**, 5 MPa/400 °C to 10 kPa, with isentropic efficiency 0.85: ideal work 1091, actual **928 kJ/kg**, exergy destroyed $T_0(s_2-s_1)=\mathbf{153\ kJ/kg}$, second-law efficiency $928/(928+153)=\mathbf{0.858}$ (equal to $\eta_s$ here).

## 3. Where exergy is destroyed in practice

| Process | Cause | Typical share |
| --- | --- | --- |
| Combustion | chemical energy to heat at a finite $T$ | 25–30 % of fuel exergy in a power plant |
| Heat transfer across a finite $\Delta T$ | boiler, condenser | 10–20 % |
| Friction, throttling, mixing | pressure drop, expansion without work | few % each |
| Turbine, compressor | irreversibility | 5–10 % |

**Design rule:** reduce irreversibility where it is cheap to do so: feed water heaters (smaller $\Delta T$ for heat addition), reheat, intercooling, regeneration. Each cycle improvement in the following notes is a reduction in $\Delta T$ across which heat is exchanged.

> [!warning] Traps
> - Using the **hot-body** temperature instead of the *environment's* $T_0$ in $T_0S_{gen}$.
> - Treating exergy as conserved: energy is, exergy is not.
> - Using kelvin only in $T_0/T$ and Celsius elsewhere.
> - Calling the first-law efficiency of a heat pump or refrigerator the second-law one: $\eta_{II}=COP/COP_{rev}$.
> - Forgetting that the exergy of low-temperature heat near $T_0$ is almost zero.

> [!question]- Predict first: heat at 330 K (hot water, 30 K above the environment). How much of 1000 kJ is exergy?
> $1000(1-298/330)=\mathbf{97\ kJ}$: about 10 %. Warm water holds plenty of energy but almost no work potential. This is why low-grade waste heat is hard to use.

> [!question]- Why does a throttling valve destroy exergy but not energy?
> $h_{in}=h_{out}$ (energy is conserved), but the pressure falls and the entropy rises ($s_{out}>s_{in}$): $X_{dest}=T_0\,\Delta s\,\dot m>0$. The pressure drop could have driven a turbine.

## 4. Connections

- [[Energy Methods - A Unified View]] — exergy is energy with a quality weighting.
- [[Reynolds Transport Theorem]] and [[Conservation of Mass (Continuity Equation)]] — the control-volume framework that the exergy balance uses.
- [[Heat Exchangers - LMTD and NTU]] — exergy destroyed in a heat exchanger grows with the temperature difference: balanced counterflow destroys the least.
- [[Kinetics of Particles - Work-Energy and Impulse-Momentum]] — mechanical energy (kinetic, potential) is pure exergy; thermal energy is not.
