---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Rolling element bearings, Ball bearing life, L10 life, Journal bearing, Petroff equation, Stribeck curve, Sommerfeld number]
---

# Bearings — Rolling Selection and Sliding Lubrication

> [!abstract] In one breath
> A bearing lets a shaft turn while carrying a load. **Rolling bearings** are bought from a catalogue: pick one whose **dynamic load rating $C$** gives the required life, $L_{10}=(C/P)^p$. **Sliding (journal) bearings** are designed: a film of oil, dragged into the wedge between shaft and bush, carries the load, and the friction is set by viscosity, speed and pressure through the **Sommerfeld number**.

Part of [[Introduction to Machine Design - MOC]]. Previous: [[Keys and Couplings]]. Next: [[Spur Gear Design - Lewis Bending and Surface Stress]].

## 1. Rolling-element bearings

| Type | Carries | Notes |
| --- | --- | --- |
| Deep-groove ball | radial and some axial | most common, quiet, cheap |
| Angular-contact ball | radial plus large one-way axial | used in pairs |
| Cylindrical roller | large radial | no axial |
| Tapered roller | radial and axial together | gearboxes, wheels, adjustable preload |
| Spherical roller, self-aligning | radial, tolerates misalignment | heavy machinery |
| Thrust ball or roller | axial only | |

**Life.** The **basic rating life** $L_{10}$ is the number of revolutions that 90 % of a group of identical bearings complete before the first sign of fatigue (flaking) appears. With the **dynamic load rating** $C$ (the load for $L_{10}=10^6$ rev) and the **equivalent radial load** $P$:

$$
L_{10}=\Big(\frac{C}{P}\Big)^{p}\ \text{million revolutions},\quad p=3\ (\text{ball}),\ \tfrac{10}{3}\ (\text{roller}),\qquad
L_{10h}=\frac{10^6\,L_{10}}{60\,n}\ \text{hours}
$$

$$
P=XF_r+YF_a\qquad(X,Y\text{ from the catalogue; }X=1,\ Y=0\text{ for a pure radial load})
$$

For a reliability above 90 %, multiply by $a_1$: 0.64 (95 %), 0.55 (96 %), 0.47 (97 %), 0.37 (98 %), 0.25 (99 %).

**Example.** Deep-groove ball bearing with $C=32$ kN under $F_r=4$ kN at 1000 rpm:

$$
L_{10}=(32/4)^3=\mathbf{512\ Mrev},\quad L_{10h}=\frac{512\times10^6}{60\times1000}=\mathbf{8530\ h};\quad 99\%\ \text{reliable: }0.25\times8530=2130\ \text{h}
$$

Doubling the load to 8 kN cuts the life by $2^3=8$: $L_{10}=64$ Mrev. The cube is why oversizing a bearing pays so well.

![[MD-3-bearings.png]]

**Selection steps.** (1) Equivalent load $P$; (2) required life $L_{10h}$ (hours: 8000 for intermittent machinery, 20 000 for continuous, 50 000+ for critical); (3) required $C=P(L_{10})^{1/p}$; (4) pick the bore from the shaft, choose the catalogue size with $C\ge C_{req}$; (5) check static load $C_0$ if the speed is very low.

## 2. Sliding (journal) bearings

The shaft sits eccentrically in the bush; its rotation drags oil into the converging wedge, where the pressure rises and floats the shaft. A full film exists when the film thickness exceeds the surface roughness.

**Petroff's equation** (the bearing treated as lightly loaded, concentric): shear of the oil film $\tau=\mu U/c$ over the journal surface gives

$$
f=2\pi^2\frac{\mu N}{P}\frac rc,\qquad P=\frac{W}{2rL}\ (\text{pressure on projected area}),\quad N\ \text{in rev/s}
$$

with radial clearance $c$ and journal radius $r$. The **Sommerfeld number** $S=(r/c)^2\mu N/P$ collects the design variables (for a loaded bearing the eccentricity ratio and film thickness are read from charts against $S$).

**Example.** Ø50 × 50 mm journal, $c=0.05$ mm, SAE oil $\mu=0.03$ Pa·s, 1500 rpm, load $W=2$ kN:

| Quantity | Value |
| --- | --- |
| $P=W/(dL)$ | 0.80 MPa |
| $S=(r/c)^2\mu N/P$ | **0.234** |
| $f=2\pi^2(\mu N/P)(r/c)$ | **0.0093** |
| friction torque $fWr$ | 0.463 N·m |
| power loss $T\omega$ | **73 W** |

The friction coefficient of a full-film bearing is below 0.01 against 0.1–0.3 for dry sliding. The right panel shows the **Stribeck curve**: friction falls as $\mu N/P$ rises (more film), reaches a minimum, then rises slowly with viscous shear (the Petroff line). Below the minimum, surfaces touch and wear.

**Design points.** Choose a lubricant viscosity to keep $S$ in the range 0.1–1; avoid starts and stops under load (boundary lubrication: use a bearing metal such as babbitt or bronze); remove the heat (the oil temperature sets $\mu$, and $\mu$ drops as it warms).

> [!warning] Traps
> - Using the catalogue $C$ with $C/P<1$: the rated life would be less than a million revolutions.
> - Using $p=3$ for a roller bearing: $p=10/3$.
> - Mixing rev/min and rev/s: Petroff's $N$ is in **rev/s**.
> - Forgetting that $L_{10}$ is the life of 90 % of bearings; a single bearing fails earlier with 10 % probability.
> - Taking $P=W/(\pi dL)$ for the film pressure: the projected area $dL$ is used.

> [!question]- Predict first: a ball bearing is run at 60 % of its load. By how much does the life increase?
> $(1/0.6)^3=4.6$ times. The roller exponent 10/3 gives 5.5 times.

> [!question]- Why does a journal bearing start with high friction?
> At zero speed there is no film: metal touches metal (boundary lubrication, $f\approx0.1$). Speed builds the film; the friction drops along the Stribeck curve to its minimum. That is why oil pumps and low starting loads are used in big machines.

## 3. Connections

- [[Viscosity and Newton's Law of Viscosity]] and [[Newtonian and Non-Newtonian Fluids]] — $\tau=\mu U/c$ is Newton's law of viscosity across the film.
- [[Viscous Flow and Exact Solutions - Formula Bank]] — the oil film is the Couette–Poiseuille flow of the dashpot problem: a moving wall plus a pressure gradient in a thin gap.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — the oil film adds stiffness and damping to the shaft; at high speed a journal bearing can show oil whirl, an instability of the rotor–film system.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — rolling-bearing life is a contact-fatigue life, and the exponent $p=3$ is the slope of the $S$–$N$ curve in disguise.
