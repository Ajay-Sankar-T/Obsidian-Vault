---
tags: [concept, physics-lab, PH1030, strain-gauge, wheatstone-bridge, youngs-modulus, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [strain gauge experiment, Young's modulus of wood, Wheatstone bridge strain, gauge factor, half bridge]
---

# Lab - Young's Modulus of Wood by Strain Gauge

> [!abstract] The experiment in one line
> Bend a half-metre wooden scale by hanging weights on its free end; two strain gauges (one stretched, one squeezed) unbalance a Wheatstone bridge by a voltage proportional to the load, and that slope gives Young's modulus.

## Aim and apparatus
**Aim:** determine Young's modulus of a half-metre wooden scale. **Apparatus:** the scale with a strain gauge on its top and bottom faces near the clamped end, a Wheatstone-bridge circuit board, constant-current source, digital millivoltmeter, hanger and slotted weights, calipers, screw gauge, rheostats.

## Theory

**Strain gauge.** A metallic foil grid bonded to the specimen changes resistance in proportion to strain; the **gauge factor** $\lambda=(\Delta R/R)/\varepsilon$ is about $2$ for metals, so $\Delta R=R_G\lambda\varepsilon$.

**Wheatstone bridge.** Four resistive arms with excitation $V_{ex}$ give an output
$$V_o=\Big[\frac{R_3}{R_3+R_4}-\frac{R_2}{R_1+R_2}\Big]V_{ex},$$
zero when $R_1/R_2=R_4/R_3$ (**balanced**). Any change in an arm unbalances it, so tiny $\Delta R$ become measurable voltages. A **dummy gauge** (transverse to the strain) cancels temperature drift because it changes with temperature equally.

**Half bridge.** In bending, the top fibres are in tension and the bottom in compression. Putting one gauge on each face makes the bridge respond to $+\Delta R$ and $-\Delta R$: **twice the output**, still linear, and temperature-compensated.

![[PL-young-wood.png]]

**Figure:** Left, unbalanced voltage against load for an illustrative run: loading and unloading points agree to the noise and a line through the origin has slope $dV/M=0.0079$ mV/g. Right, a half bridge gives twice the quarter-bridge signal.

**Bending.** For a rectangular beam (breadth $b$, thickness $d$) loaded by $Mg$ at distance $L$ from the gauge, the surface stress is $\sigma=6MgL/(bd^2)$, so the strain is $\varepsilon=6MgL/(Ybd^2)$. Combining with the bridge sensitivity, the manual's result is
$$Y=\frac{6\,g\,L\,\lambda\,R\,I}{b\,d^2\,\big[1+(R/P)\big]\,(dV/M)},$$
with $I$ the source current, $R$ the gauge resistance and $P$ the fixed bridge resistor (use consistent units: $M$ in kg and $dV$ in volts, unless your sheet states otherwise). Background: [[Flexure Formula]] and [[Stress-Strain Diagram and Hooke's Law]].

> [!question]- 🎯 Predict first: you replace the wood by an aluminium bar of the same size. Does $dV/M$ get bigger or smaller?
> **Smaller.** $\varepsilon\propto1/Y$, and aluminium ($70$ GPa) is about seven times stiffer than wood ($\sim10$ GPa), so the same load strains it seven times less and the bridge signal is seven times smaller. The same reasoning is why strain gauges on steel structures need sensitive amplifiers.

## Procedure (condensed)
1. Clamp the beam so the gauges are near the clamped end; load and unload a few times to settle it.
2. Wire the bridge, switch on the source and meter, **balance at no load** with the variable resistor.
3. Hang $m$, read the DPM (average the flickering last digit); go up in steps $m,2m,\dots,5m$ and then back down; repeat for reproducibility.
4. Compute $dV/M$ at each load and combine; plot $dV$ against $M$ with the fitted line.
5. Measure $L$ (gauge centre to load), $b$ (slide calipers) and $d$ (screw gauge, several places).

## Worked example
> [!example]- 🔬 Illustrative numbers: $L=0.40$ m, $b=30$ mm, $d=2.5$ mm, $\lambda=2.1$, $R=P=120\ \Omega$, $I=5$ mA, $dV/M=7.9$ mV/kg
> $\displaystyle Y=\frac{6(9.81)(0.40)(2.1)(120)(0.005)}{(0.03)(0.0025)^2(1+1)(7.9\times10^{-3})}=1.0\times10^{10}$ Pa $=10$ GPa, typical of wood along the grain.
> **Check:** $d$ enters squared, so a $0.05$ mm error in $d$ (2%) gives a 4% error in $Y$: the screw gauge matters most.

> [!warning]- ⚠️ Not balancing at zero load
> A nonzero offset adds a constant to every reading and shows up as an intercept in the $dV$–$M$ plot. Fit a line with intercept to check; physics says it must pass through the origin.

> [!danger]- 💥 Touching the beam or the leads during a reading
> Body heat and moving leads change gauge resistance faster than the strain does. Read steadily, away from the wires.

## Questions
> [!question]- Why two gauges, one on each face?
> They double the sensitivity and cancel common-mode effects (temperature) because tension and compression act in opposite arms.

> [!question]- Why average the loading and unloading readings?
> Hysteresis and creep make the two differ slightly; the mean cancels the first-order effect and their difference estimates reproducibility.

## Connections
- **Theory:** [[Flexure Formula]], [[Strain Transformation and Rosettes]] (rosettes are strain gauges at several angles), [[Stress-Strain Diagram and Hooke's Law]].
- **Cross-domain:** [[Series-Parallel Resistance Reduction]] and [[03 DC Network Theorems]] (the bridge is a resistive network); [[Measurements, Instrumentation and Control - MOC]] (strain gauges are standard sensors).
- **Related lab:** [[Lab - Deflection of Beams (Three-Point Bending)]] measures the same $E$ with dial gauges.

## Self-check
- [ ] I can say how the bridge turns $\Delta R$ into voltage and why it starts balanced.
- [ ] I can explain why a half bridge doubles the output and compensates temperature.
- [ ] I can compute $Y$ from $dV/M$ and the dimensions, and say which dimension matters most.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]
