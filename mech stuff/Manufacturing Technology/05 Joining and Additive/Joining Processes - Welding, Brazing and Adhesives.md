---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Welding, Arc welding, MIG, TIG, Resistance welding, Brazing, Soldering, Adhesive bonding, Heat input, Heat affected zone, Weldability]
---

# Joining Processes — Welding, Brazing and Adhesives

> [!abstract] In one breath
> Joining processes fall into three families by what happens to the base metal: **fusion welding** melts it, **solid-state welding** joins it below the melting point with pressure or friction, and **brazing, soldering and adhesives** leave it solid and add a filler. The heat of welding is what damages the metal next to the joint, so **heat input** $=\eta VI/v$ is the number to control.

Part of [[Manufacturing Technology - MOC]]. Previous: [[Metrology and GD&T - Form, Position and Gauging]]. Next: [[Additive Manufacturing - Processes and Design Rules]]. Weld and rivet symbols as drawn: [[Keys, Rivets and Welds]].

## 1. The families

| Family | Process | Idea | Typical use |
| --- | --- | --- | --- |
| **Fusion (arc)** | SMAW (stick), **GMAW (MIG/MAG)**, **GTAW (TIG)**, SAW (submerged arc), FCAW | an electric arc melts base and filler | structures, pipes, vessels |
| Fusion (high energy) | laser, electron beam | focused beam, deep narrow weld | automotive, aerospace |
| Fusion (gas) | oxy-acetylene | flame | repair, thin sheet, cutting |
| **Resistance** | spot, seam, projection | $I^2Rt$ heating at the interface under force | car body sheet |
| **Solid state** | friction, **friction stir**, ultrasonic, explosion, forge welding | pressure and relative motion, no melting | aluminium, dissimilar metals |
| **Brazing** | filler above 450 °C, base below its melting point | capillary action fills the gap | heat exchangers, carbide tips |
| **Soldering** | filler below 450 °C | capillary action | electronics, plumbing |
| **Adhesive bonding** | epoxy, acrylic, cyanoacrylate | polymer cures between surfaces | composites, aircraft, light assemblies |
| Mechanical | bolts, rivets | | see [[Bolted Joints - Preload and Joint Stiffness]] |

Joint types: **butt, lap, T, corner, edge**; weld types: groove (butt), fillet, plug, spot. In a **fillet weld** the throat is $0.707\times$ leg length, so a 6 mm leg has a 4.2 mm throat and the load is carried in shear on that throat.

## 2. Arc welding heat input

The energy delivered to the joint per unit length:

$$
HI=\frac{\eta\,V\,I}{v}\qquad[\text{J/mm}]
$$

($V$ arc voltage, $I$ current, $v$ travel speed, $\eta$ arc efficiency: about 0.8 for MIG, 0.6 for TIG, 0.9–1 for submerged arc).

**Example.** MIG: 25 V, 200 A, 5 mm/s, $\eta=0.8$:

$$
HI=\frac{0.8\times25\times200}{5}=\mathbf{800\ J/mm}\ (0.8\ \text{kJ/mm})
$$

At 2.5 mm/s it doubles to 1.6 kJ/mm. More heat input gives a wider weld, a wider **heat-affected zone (HAZ)** and a **slower cooling rate** (cooling rate falls roughly as $1/HI$).

## 3. The HAZ and weldability

Beside the weld, the base metal is heated but not melted: its microstructure is changed. For steel the HAZ is a band whose temperature passed above $A_1$, so on cooling it forms **pearlite, bainite or martensite** depending on the cooling rate and composition (see [[Heat Treatment of Steel - TTT and CCT Diagrams]]): a fast cooling rate (low heat input, thick plate, cold plate) makes hard, brittle martensite that can crack with hydrogen (**cold cracking**).

**Carbon equivalent** estimates the hardenability and so the risk:

$$
CE=C+\frac{Mn}6+\frac{Cr+Mo+V}5+\frac{Ni+Cu}{15}
$$

A steel with 0.20 C, 1.2 Mn, 0.1 Cr, 0.05 Mo, 0.1 Ni has $CE=0.20+0.20+0.03+0.007=\mathbf{0.44}$: above about 0.40 it needs **preheat** (100–200 °C) to slow the cooling, low-hydrogen electrodes and possibly **post-weld heat treatment**.

Other issues: **residual stress and distortion** (the weld shrinks as it cools against the cold plate), porosity (dirty or damp), lack of fusion, undercut, cracks (hot cracking in the weld pool), and in aluminium the high thermal conductivity and oxide film.

## 4. Brazing, soldering, adhesives

- **Brazing / soldering:** the joint **gap** is 0.05–0.15 mm so that capillary action draws the molten filler in; the filler *wets* the clean base metal (flux or atmosphere removes oxide). Strength comes from the filler's strength and the thin-film constraint.
- **Adhesive:** loads should be carried in **shear or compression**, not peel or cleavage; bond **area** is large, stress is spread evenly, and dissimilar materials do not gall or corrode. Surface preparation is critical; temperature limits are low; inspection is hard.

> [!warning] Traps
> - Using heat input without the efficiency $\eta$.
> - Assuming the weld, not the HAZ, is the weak point: in hardened or cold-worked material the HAZ is.
> - Designing adhesive joints in peel.
> - Treating the fillet-weld leg as the load-bearing size: the **throat** is.
> - Forgetting that a brazed joint's strength depends on gap size.

> [!question]- Predict first: weld a thick plate at 0 °C versus the same plate preheated to 150 °C. Which cools faster in the HAZ?
> The cold plate: a larger temperature difference to the surroundings and no stored heat give a faster cooling rate, more martensite and a higher crack risk. Preheating reduces the cooling rate without changing the heat input.

> [!question]- Why is friction stir welding favoured for aluminium?
> It never melts the metal, so none of the porosity, hot cracking or solidification defects of fusion welding appear, and the HAZ is narrow and fine-grained. The strong oxide film is stirred and broken up.

## 5. Connections

- [[Heat Transfer - MOC]] — welding is a moving heat source; the cooling rate follows from conduction (Rosenthal) with heat input as the source strength.
- [[Thermal Stresses]] — restrained thermal contraction produces residual stress and distortion.
- [[Phase Diagrams - Lever Rule and the Iron-Carbide Diagram]] — the microstructure of the weld metal and HAZ.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — a weld toe is a severe stress concentration and a fatigue crack site.
