---
title: Pipe Flow and Losses – Solved Problems (GPS 7 & 8)
tags: [fluid-mechanics, tutorial, pipe-flow, moody-chart, friction-factor, minor-losses]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
source: "[[GPS_7_8.pdf]]"
---

# Pipe Flow and Losses – Solved Problems (GPS 7 & 8)

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · formulas: [[Pipe Flow and Losses - Formula Bank]] · source: [[GPS_7_8.pdf]] · all numbers recomputed in `Tools/fm_pipe.py`

Data from the sheet: $g=9.81$ m/s²; water at 20 °C $\rho=998$, $\nu=1.01\times10^{-6}$ m²/s; at 15 °C $\rho=999$, $\nu=1.14\times10^{-6}$. Friction factors come from Colebrook (the chart) unless the sheet says Haaland.

| # | Problem | Concept | Result |
|---|---|---|---|
| 1 | [[#1. House water: improve the flow to the top floor]] | find $Q$; fully rough pipe | 6.8 → 33.8 (Option 1) vs 13.9 L/min (Option 2) |
| 2 | [[#2. Drainpipes: one working pipe]] | gravity-driven full pipe, $H$ cancels | 85.8 mm/h; 75 mm: 250 mm/h |
| 3 | [[#3. Industrial supply line]] | find $D$; elbows as $L_e$ | $D_{min}=132.3$ mm → 6 in |
| 4 | [[#4. Roman nozzle with a diffuser]] | energy equation with $K$ | 2.61 → 3.47 L/s (+32.8 %) |
| 5 | [[#5. Scaled water main]] | $\Delta p$ and $Q$ as the bore shrinks | 106 → 659 kPa; 4.0 L/s |
| 6 | [[#6. Laminar flow from a tank through thin tubing]] | $Re=2300$ limit, $\alpha=2$ | 5.80 mL/s, $h=3.73$ m |

> [!abstract] Pattern
> Every problem is the energy equation of the [[Pipe Flow and Losses - Formula Bank#1. Energy equation with losses|formula bank]] written between the free surface or inlet and the outlet, with $h_{lT}=\big(fL/D+\sum K\big)V^2/2$. Decide first which of **$\Delta p$, $Q$, $D$** is unknown (formula bank §5); all six problems differ only in that and in the minor losses.

---

## 1. House water: improve the flow to the top floor

**Concept.** Unknown flow rate in a fully rough pipe. Pump or bigger pipe?

**Given.** Meter pressure 200 kPa gauge, tap 15 m above, route 7 m + 15 m + 1 m $=23$ m. Existing: $D=12.7$ mm, $e/D=0.05$. Option 1: new smooth $D=19$ mm, same route. Option 2: old pipe, pump at the foot of the riser giving 300 kPa gauge, so the pipe after the pump is $15+1=16$ m.

**Principle.** Energy equation from the meter (or pump outlet) to the tap. Velocities are equal at both ends, tap at atmosphere:
$$\frac{p_1}{\rho}-gH=f\frac{L}{D}\frac{V^2}{2}\ \ \Rightarrow\ \ V=\sqrt{\frac{2\,(p_1/\rho-gH)}{f\,L/D}}$$
$f$ depends on $V$ through $Re$, so iterate (start from the fully rough $f$).

**(a) Existing pipe.** Driving energy $200\,000/998-9.81(15)=53.25$ J/kg, $L/D=1811$. Fully rough $f=[-2\log_{10}(0.05/3.7)]^{-2}=0.0716$ gives $V=0.906$ m/s; then $Re=11\,200$, Colebrook $f=0.0736$ and
$$V=0.894\ \text{m/s},\qquad Q=VA=1.13\times10^{-4}\ \text{m}^3/\text{s}=\boxed{6.8\ \text{L/min}}$$

**(b) Options.**

| | $p_1$ | $L/D$ | driving J/kg | $f$ | $Re$ | $V$ (m/s) | $Q$ (L/min) |
|---|---|---|---|---|---|---|---|
| existing | 200 kPa | 1811 | 53.3 | 0.0736 | 11 200 | 0.894 | **6.8** |
| Option 1: 19 mm smooth | 200 kPa | 1211 | 53.3 | 0.0223 | 37 400 | 1.99 | **33.8** |
| Option 2: pump | 300 kPa | 1260 | 153.5 | 0.0725 | 23 000 | 1.83 | **13.9** |

**Option 1 is far more effective**: ×5.0 against ×2.0.

**(c) Why the booster helps so little.** On the Moody chart (figure below) the existing pipe and Option 2 sit on the same $e/D=0.05$ curve, where it is almost flat ($f=0.074$ against 0.073). With $f$ fixed, $V\propto\sqrt{\Delta p/(fL/D)}$. The driving energy rises 2.9× (53 → 153 J/kg) and the pipe is 30 % shorter, yet $V$ only goes $0.894\to1.83$ m/s, ×2.05: friction is proportional to $V^2$, so every extra kPa buys a shrinking amount of flow. The *pipe* is the bottleneck. Option 1 moves the operating point **down** the chart: the wall is smooth (the $e/D=0.05$ curve is replaced by the smooth curve) and the larger $D$ also lowers $V$ for a given $Q$. $f$ drops by 3.3×, and $Q\propto D^{2}\sqrt{D/f}$ rises with it.

> [!tip] Figure
> ![[FM-P1-moody-operating-points.png]]
> The three operating points. Red and orange differ in $Re$ only; green sits on the smooth curve.

**Trap.** Taking the pipe before the pump into account for Option 2: the 7 m run is upstream of the booster, so the pump delivers the stated 300 kPa to the pipe that follows (16 m). Do not add the 7 m again.

---

## 2. Drainpipes: one working pipe

**Concept.** A full vertical pipe with both ends at atmosphere is driven by gravity alone.

**Given.** $D=50$ mm galvanized iron ($e=0.15$ mm, $e/D=0.003$), height $H=5$ m, roof 500 m², water 20 °C, one pipe working.

**Principle.** Same pressure and velocity at top and bottom, so only $gz$ and friction remain:
$$gH=f\frac{H}{D}\frac{V^2}{2}\ \Longrightarrow\ V=\sqrt{\frac{2gD}{f}}$$

**(a)** Iterate with Colebrook: $V=6.07$ m/s, $Re=3.0\times10^5$, $f=0.0266$,
$$Q=VA=0.01192\ \text{m}^3/\text{s}.$$
Rainfall rate that fills the pipe: $\dfrac{Q}{A_{roof}}=2.38\times10^{-5}$ m/s $=\boxed{85.8\ \text{mm/h}}$ (using 1 mm/h $=2.78\times10^{-7}$ m/s). Heavier rain than that floods the roof.

**(b)** $H$ cancelled in $gH=f(H/D)V^2/2$: the answer is the same for 2 m, 5 m or 20 m (checked numerically: $V=6.0705$ m/s in all three). Physically, the weight of water in the column grows with height exactly as the wall friction on it does; the pressure is atmospheric at both ends, so the water falls at a terminal velocity set by $D$ and roughness alone, like a skydiver.

**(c)** 75 mm: $e/D=0.002$, $V=7.87$ m/s, $f=0.0237$, $Q=0.0348$ m³/s, $\boxed{250\ \text{mm/h}}$.
The capacity rises by **2.92** against an area ratio of 2.25. Because $V=\sqrt{2gD/f}$ itself grows: $\sqrt{1.5}=1.22$ from the bigger $D$, and a further $\sqrt{0.0266/0.0237}=1.06$ because $e/D$ is smaller so $f$ falls. $Q\propto D^{5/2}/\sqrt f$.

**Trap.** Inventing a pressure difference to drive the flow. Both ends are at atmosphere, so gravity is the only driver and the whole $gH$ goes into friction.

---

## 3. Industrial supply line

**Concept.** Unknown diameter, $\Delta p$ fixed; fittings via equivalent length.

**Given.** $Q=5.7$ m³/min $=0.095$ m³/s, main 800 kPa gauge, plant needs 500 kPa, so $\Delta p=300$ kPa. $L=65$ m galvanized iron, four standard 90° elbows ($L_e/D=30$ each), water 15 °C, no elevation change, Haaland $f$.

**Principle.**
$$\Delta p=\rho f\Big(\frac{L}{D}+4\frac{L_e}{D}\Big)\frac{V^2}{2},\qquad V=\frac{4Q}{\pi D^2}$$
Both $V$ and $f$ depend on $D$, so solve numerically.

**(a)** $\boxed{D_{min}=132.3\ \text{mm}}$ (Colebrook gives the same to 0.01 mm).

**(b)** Nominal sizes:

| size | $D$ (mm) | $V$ (m/s) | $Re$ | $f$ | $\Delta p$ (kPa) | plant pressure (kPa) |
|---|---|---|---|---|---|---|
| 4 in | 102.3 | 11.56 | $1.04\times10^6$ | 0.0218 | 1101 | **negative** |
| 5 in | 128.2 | 7.36 | $8.3\times10^5$ | 0.0207 | 352 | 448 (< 500) |
| **6 in** | 154.1 | 5.09 | $6.9\times10^5$ | 0.0199 | 140 | **660** |

The 5 in pipe is smaller than $D_{min}$ and fails. **Install 6 in**: the plant gets $\boxed{660\ \text{kPa}}$ at $V=5.09$ m/s.

**(c)** With no elbows $D_{min}=126.9$ mm, so the **5 in** pipe ($D=128.2$ mm, $\Delta p=284$ kPa, plant 516 kPa) would pass; the elbows force the 6 in pipe. Four elbows add $4\times30\,D=15$ m of equivalent length to the 65 m (+24 %), which lifts $\Delta p$ from 284 to 352 kPa.
Scaling: $\Delta p\propto fLQ^2/D^5$. One step in standard size, $154.1/128.2=1.20$, changes the pressure drop by $1.2^{5}=2.5$: the steps are coarse in $\Delta p$ because $D$ enters to the fifth power. A 5 in pipe is marginal even without elbows (284 against 300 kPa), so any added length tips it over.

**Trap.** Rounding **down** to the nearest standard size. Always round up: a smaller bore costs more than it saves.

---

## 4. Roman nozzle with a diffuser

**Concept.** Energy equation with two $K$ values. $K$'s are based on the nozzle exit velocity $V_1$.

**Given.** Head $z_0=1.5$ m above the nozzle, exit $D=25$ mm, $K=0.04$ (rounded entrance). Diffuser: $A_2/A_1=2$, $K_d=0.30$. Water to atmosphere, no pipe friction.

**(a) Nozzle alone.** Free surface to exit: $gz_0=\dfrac{V_1^2}{2}(1+K)$ (the "1" is the exit kinetic energy):
$$V_1=\sqrt{\frac{2gz_0}{1+K}}=\sqrt{\frac{29.43}{1.04}}=5.32\ \text{m/s},\qquad Q=V_1A_1=\boxed{2.61\ \text{L/s}}$$

**(b) With the diffuser.** Continuity: $V_2=V_1/2$. The exit kinetic energy is now $V_2^2/2=V_1^2/8$:
$$gz_0=\frac{V_1^2}{2}\Big(\frac1{AR^2}+K+K_d\Big)=\frac{V_1^2}{2}(0.25+0.04+0.30)$$
$$V_1=\sqrt{\frac{29.43}{0.59}}=7.06\ \text{m/s},\qquad Q=\boxed{3.47\ \text{L/s}\ (+32.8\,\%)}$$

**(c) Pressure at the diffuser inlet.** Energy from the free surface to the nozzle exit (section 1):
$$\frac{p_1}{\rho}=gz_0-\frac{V_1^2}{2}(1+K)=14.72-24.94(1.04)=-11.2\ \text{J/kg}\ \Rightarrow\ \boxed{p_1=-11.2\ \text{kPa (gauge)}}$$
**Why it helps.** The diffuser lowers the exit velocity, so less energy is lost as exit kinetic energy; the pressure at the nozzle exit falls **below atmospheric** (the flow is partly sucked), which raises the pressure difference across the nozzle and so the flow. Pressure is recovered inside the diffuser, where $V$ falls from $V_1$ to $V_1/2$.

**Trap.** Applying the exit $K$ to the wrong velocity: both $K$'s use $V_1$, not $V_2$. Also the diffuser only works if it does not stall ($K_d=0.30$ is for a gentle cone).

---

## 5. Scaled water main

**Concept.** Which diameter enters each group, and how the bore and the roughness separately raise $\Delta p$.

**Given.** $L=500$ m horizontal, $Q=10$ L/s, water 20 °C, Haaland $f$. New: $D=100$ mm, $e=0.26$ mm. After 40 years: scale 10 mm thick, **clear bore** $D=80$ mm, scale surface $e=2$ mm.

**(a) New.** $V=1.273$ m/s, $Re=1.26\times10^5$, $e/D=0.0026$, $f=0.0262$, $L/D=5000$:
$$\Delta p=\rho f\frac LD\frac{V^2}{2}=\boxed{106\ \text{kPa}}$$

**(b) After 40 years.** The flow only passes through the open bore, so **the 80 mm diameter enters all four**: $V=4Q/\pi D^2=1.989$ m/s, $Re=VD/\nu=1.58\times10^5$, $e/D=2/80=0.025$, $L/D=6250$. $f=0.0534$:
$$\Delta p=\boxed{659\ \text{kPa}}\quad(6.2\times\text{ the original})$$

**(c) Bore against roughness.**

| case | $D$ (mm) | $e$ (mm) | $f$ | $\Delta p$ (kPa) | factor |
|---|---|---|---|---|---|
| new | 100 | 0.26 | 0.0262 | 106 | 1 |
| smaller bore only | 80 | 0.26 | 0.0275 | 340 | **3.2** |
| rougher wall only | 100 | 2.0 | 0.0490 | 198 | 1.9 |
| both (old main) | 80 | 2.0 | 0.0534 | 659 | 6.2 |

The smaller bore matters more: $\Delta p\propto fLQ^2/D^5$ gives $(100/80)^5=3.1$ before $f$ changes at all. The rough wall alone changes only $f$ (×1.9). The effects multiply, not add: $3.2\times1.94=6.2$.

**(d) Flow at the original $\Delta p$.** Solve $\Delta p(Q)=106$ kPa for the 80 mm main:
$$\boxed{Q=4.0\ \text{L/s}}\quad(\text{40 \% of design; }V=0.80\text{ m/s},\ Re=6.3\times10^4,\ f=0.0537).$$

**Trap.** Using $D=100$ mm for $V$ and $Re$ but 80 mm for $L/D$ (or the reverse). One diameter for the whole calculation.

---

## 6. Laminar flow from a tank through thin tubing

**Concept.** Limit of laminar flow, energy equation with $\alpha=2$ and an entrance loss.

**Given.** Smooth plastic tubing $D=3.18$ mm, $L=15.3$ m, horizontal at the tank base, water 20 °C, $K_{ent}=1.4$, $\alpha=2$ at the outlet. The tank is large, so $V_1\approx0$.

**(a)** The flow stays laminar up to $Re=2300$:
$$V_{max}=\frac{2300\,\nu}{D}=\frac{2300(1.01\times10^{-6})}{0.00318}=0.730\ \text{m/s},\qquad Q=V_{max}\frac{\pi D^2}4=\boxed{5.80\ \text{mL/s}}$$

**(b)** Energy equation, free surface to exit, $f=64/Re=0.0278$, $L/D=4811$:
$$gh=\frac{V^2}{2}\Big(\alpha+K_{ent}+f\frac LD\Big)=\frac{V^2}{2}\,(2+1.4+133.9)$$
$$h=\frac{0.730^2}{2(9.81)}(137.3)=\boxed{3.73\ \text{m}}$$
For depths below 3.73 m the flow is laminar.

**(c)** Friction takes $133.9/137.3=\boxed{97.5\,\%}$ of the depth; the exit kinetic energy ($\alpha=2$) takes 1.5 % and the entrance 1.0 %. The operating point is $Re=2300$, $f=0.0278$, on the laminar line at its right end.

> [!tip] Figure
> ![[FM-P6-laminar-point.png]]

**Trap.** Using $\alpha=1$ for the exit kinetic energy. In laminar flow the parabolic profile gives $\alpha=2$. It matters little here (friction dominates) but it is not 1.

---

## Check
$\Delta p$ and $Q$ were recomputed with `scipy.optimize.brentq` and agree with the hand estimates to the digits quoted. Colebrook and Haaland differ by under 1 % in every problem (e.g. $D_{min}$ 132.32 vs 132.33 mm).

## Concepts used
- [[Pipe Flow and Losses - Formula Bank]] — all equations and tables used above
- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] — the lossless limit of the energy equation
- [[Absolute, Gauge and Vacuum Pressure]] — gauge pressure at the outlet and the sub-atmospheric nozzle exit in Q4
- [[Viscosity and Newton's Law of Viscosity]] — the origin of the friction factor and of $64/Re$
- [[Dimensional Analysis and Similitude - Formula Bank]] — why $f=f(Re,e/D)$
