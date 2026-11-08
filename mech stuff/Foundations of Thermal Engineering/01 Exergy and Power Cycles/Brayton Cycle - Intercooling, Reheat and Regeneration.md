---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME2102)"
aliases: [Brayton cycle, Gas turbine cycle, Joule cycle, Intercooling, Regenerator, Recuperator, Air-standard cycle, Pressure ratio]
---

# Brayton Cycle — Intercooling, Reheat and Regeneration

> [!abstract] In one breath
> A gas turbine compresses air, burns fuel in it, expands the hot gas through a turbine, and exhausts. The **air-standard** model treats the working fluid as a perfect gas. The simple cycle's efficiency depends only on the **pressure ratio**: $\eta=1-r_p^{-(\gamma-1)/\gamma}$. Net work peaks at an optimum pressure ratio. **Intercooling and reheat raise work, regeneration raises efficiency**.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Rankine Cycle - Superheat, Reheat and Regeneration]]. Next: [[Vapour-Compression Refrigeration and Heat Pumps]].

## 1. The simple cycle

Compressor 1→2 (isentropic), heat addition 2→3 at constant pressure, turbine 3→4 (isentropic), heat rejection 4→1.

$$
\frac{T_2}{T_1}=\frac{T_3}{T_4}=r_p^{(\gamma-1)/\gamma},\qquad
w_c=c_p(T_2-T_1),\ \ w_t=c_p(T_3-T_4),\ \ q_{in}=c_p(T_3-T_2)
$$

$$
\eta_{th}=1-\frac{1}{r_p^{(\gamma-1)/\gamma}},\qquad \text{back-work ratio }\frac{w_c}{w_t}=\frac{T_1}{T_3}\,r_p^{(\gamma-1)/\gamma}
$$

The back-work ratio is large (40–60 %): a gas turbine spends half of its turbine work on the compressor, unlike the 1 % of a steam plant (compressing a gas is expensive, a liquid cheap).

**Optimum pressure ratio for maximum net work** (fixed $T_1$, $T_3$): $r_{p,opt}=(T_3/T_1)^{\gamma/[2(\gamma-1)]}$.

## 2. Worked example: $T_1=300$ K, $T_3=1400$ K, $r_p=10$, air ($c_p=1.005$, $\gamma=1.4$)

| Cycle | $w_c$ | $w_t$ | net work (kJ/kg) | $q_{in}$ | $\eta$ |
| --- | --- | --- | --- | --- | --- |
| **Simple** ($T_2=579$ K, $T_4=725$ K) | 281 | 678 | **398** | 825 | **0.482** |
| + **regenerator**, $\varepsilon=0.8$ ($T_5=696$ K) | 281 | 678 | 398 | 708 | **0.562** |
| + **intercooling** (2 stages, $r=\sqrt{10}$ each, back to 300 K) and **reheat** (to 1400 K), no regenerator | 235 | 789 | **554** | 1382 | 0.401 |
| all three | | | 554 | | **0.610** |
| Simple with $\eta_c=0.85$, $\eta_t=0.88$ | | | 267 | | 0.344 |

Net work is maximised at $r_p=14.8$ for this temperature pair.

![[FTE-2-brayton.png]]

## 3. Why each modification does what it does

- **Regeneration:** the turbine exhaust (725 K) is hotter than the compressor outlet (579 K), so use it to preheat the air before the combustor. Heat addition falls from 825 to 708 kJ/kg at the same work: efficiency rises. It only works if $T_4>T_2$, i.e. at low pressure ratios; at high $r_p$ the exhaust is cooler than the compressed air and a regenerator would cool it.
- **Intercooling:** cooling between compressor stages brings the air back toward $T_1$, so the later stage needs less work (the compressor work falls from 281 to 235 kJ/kg). The optimal split is equal pressure ratios, $r_1=r_2=\sqrt{r_p}$. It *raises net work* but, alone, *lowers efficiency* because more heat must be added (the air enters the combustor cooler).
- **Reheat:** burning more fuel between turbine stages raises turbine work (678 → 789 kJ/kg) for the same reason (equal stage ratios), again at the cost of more heat added.
- Intercooling and reheat are therefore used **with regeneration**: the extra exhaust heat is recovered. That is the path toward the Ericsson cycle (isothermal compression and expansion), which approaches Carnot efficiency.

## 4. Real gas turbines

Component efficiencies of 0.85–0.90 cut the efficiency from 0.48 to 0.34 in the example. Turbine inlet temperature is limited by blade materials and cooling (about 1500–1700 K in modern engines); higher $T_3$ raises both work and efficiency. **Jet engines** expand only partway in the turbine (enough to drive the compressor) and use the rest of the pressure to accelerate the gas through a nozzle ([[Isentropic Nozzle Flow and Choking]]). **Combined cycles** use the hot exhaust to raise steam for a Rankine cycle: over 55 % overall.

> [!warning] Traps
> - Using $T$ in Celsius in the isentropic relations.
> - Calling the Brayton efficiency independent of $T_3$: true only for the *simple ideal* cycle; the *work* depends strongly on $T_3$.
> - Assuming that adding intercooling raises the efficiency by itself.
> - Using a regenerator when $T_4<T_2$.
> - Mixing the cold-air-standard $\gamma=1.4$ with hot-gas properties: real turbine gas has $\gamma\approx1.33$ and a larger $c_p$.

> [!question]- Predict first: increase the turbine inlet temperature from 1400 K to 1600 K at $r_p=10$. Does $\eta$ change in the ideal simple cycle?
> No: $\eta=1-r_p^{-0.286}$ depends only on $r_p$. But the net work rises sharply ($\propto T_3-T_4-\dots$), so the machine is smaller per kW. In real cycles the efficiency also rises because component losses are a smaller fraction of a larger work.

> [!question]- Why do gas turbines have a back-work ratio of about 0.4 while a steam plant has 0.01?
> Compressing a gas takes $\int v\,dP$ with a large specific volume; compressing liquid water takes the same integral with a volume a thousand times smaller. Gas turbines therefore need a large turbine to drive the compressor.

## 5. Connections

- [[Exergy and Reversible Work]] — regeneration reduces the temperature difference over which heat is exchanged.
- [[Rankine Cycle - Superheat, Reheat and Regeneration]] — the analogous improvements in the steam cycle; the same ideas, different fluid.
- [[Turbomachines - Euler Equation and Velocity Triangles]] — the compressor and the turbine themselves.
- [[Heat Exchangers - LMTD and NTU]] — the regenerator is a counterflow heat exchanger with effectiveness $\varepsilon$.
