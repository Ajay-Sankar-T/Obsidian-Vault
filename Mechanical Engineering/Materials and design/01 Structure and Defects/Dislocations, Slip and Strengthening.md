---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Dislocations, Slip systems, Schmid's law, CRSS, Hall-Petch, Work hardening, Strengthening mechanisms, Imperfections in solids]
---

# Dislocations, Slip and Strengthening

> [!abstract] In one breath
> Real crystals are **thousands of times weaker** than perfect ones because plastic flow does not slide whole planes: it moves **line defects (dislocations)** one row of atoms at a time. Every way of strengthening a metal is a way of **blocking dislocations**: grain boundaries, solute atoms, precipitates, and other dislocations.

Part of [[Materials and Design - MOC]]. Previous: [[Crystal Structures and Packing]]. Next: [[Tensile Test, True Stress-Strain and Hardness]].

## 1. Imperfections

| Dimension | Defect | Example |
| --- | --- | --- |
| 0-D (point) | vacancy, self-interstitial, substitutional or interstitial impurity | carbon in iron (interstitial), Zn in Cu (substitutional) |
| 1-D (line) | **dislocation**: edge (extra half-plane) or screw | carries plastic deformation |
| 2-D (interfacial) | grain boundary, twin boundary, free surface, stacking fault | grain size |
| 3-D (volume) | pores, cracks, inclusions, precipitates, second phases | |

An **edge dislocation** is the edge of an extra half-plane of atoms; the **Burgers vector** $\mathbf b$ is the lattice displacement it carries, perpendicular to the line for an edge and parallel for a screw. Slip happens when the dislocation glides, one bond at a time, along its **slip plane** in a **slip direction** (the slip system, see the table in [[Crystal Structures and Packing]]). The stress to glide a dislocation is far less than the stress to shear the whole plane at once, which is why metals are ductile and soft.

## 2. Schmid's law

A crystal loaded in tension $\sigma$ yields when the **resolved shear stress** on a slip system reaches a material constant, the **critical resolved shear stress (CRSS)**:

$$
\tau_R=\sigma\cos\phi\cos\lambda,\qquad \sigma_y=\frac{\tau_{CRSS}}{\cos\phi\cos\lambda}
$$

$\phi$ is the angle between the load axis and the slip-plane **normal**, $\lambda$ the angle between the load axis and the slip **direction**. The Schmid factor $\cos\phi\cos\lambda\le0.5$, reached at $\phi=\lambda=45^\circ$.

**Example.** Copper single crystal ($\tau_{CRSS}=0.48$ MPa), $\phi=60^\circ$, $\lambda=35^\circ$:

$$
\sigma_y=\frac{0.48}{\cos60^\circ\cos35^\circ}=\frac{0.48}{0.5(0.819)}=\mathbf{1.17\ MPa}
$$

Orientation matters by up to a factor of infinity (if $\phi$ or $\lambda$ is $90^\circ$ no slip system is stressed). **Polycrystals** average over random orientations: yield stress is about $2$–$3\times\tau_{CRSS}$.

![[MAT-2-slip.png]]

## 3. Strengthening = obstructing dislocations

| Mechanism | How it blocks | Formula or effect |
| --- | --- | --- |
| **Grain-size refinement** | boundaries stop slip; dislocations pile up | Hall–Petch $\sigma_y=\sigma_0+kd^{-1/2}$ |
| **Solid solution** | solute atoms strain the lattice and snag dislocations | $\Delta\sigma\propto\sqrt{c}$ (brass is stronger than copper) |
| **Strain (work) hardening** | dislocations multiply and tangle | Taylor: $\Delta\sigma=\alpha Gb\sqrt\rho$ |
| **Precipitation** | particles must be cut or bypassed | Orowan: $\Delta\tau\approx Gb/L$ ($L$ = particle spacing) |

**Hall–Petch.** For a mild steel with $\sigma_0=70$ MPa and $k=0.6$ MPa√m: grain size 100 µm gives **130 MPa**, 10 µm gives **260 MPa**, 1 µm gives **670 MPa**: refining grains is the one mechanism that also improves toughness.

**Taylor hardening.** Copper ($G=48$ GPa, $b=0.256$ nm, $\alpha=0.5$): dislocation density $10^{12}$ m⁻² (annealed) gives 6 MPa; $10^{14}$ gives **61 MPa**; $10^{15}$ (heavily cold-worked) gives **194 MPa**.

**Recovery, recrystallisation, grain growth.** Cold work stores dislocations; heating relieves stress (recovery, 0.3 $T_m$), forms new strain-free grains (recrystallisation, about $0.4T_m$), then the grains coarsen. Hot working and annealing exploit this.

> [!warning] Traps
> - Measuring $\phi$ from the slip *plane* instead of its normal.
> - Applying Hall–Petch to nanometre grains (below about 20 nm grain-boundary sliding makes it reverse).
> - Thinking strength comes only from adding alloying elements: processing (grain size, work hardening, heat treatment) changes it by factors of 5–10.
> - Expecting both high strength and ductility from work hardening: ductility falls.

> [!question]- Predict first: a metal is cold-worked and then heated to 600 °C for an hour. Stronger or weaker?
> Weaker, if the temperature is above the recrystallisation temperature: new, dislocation-free grains replace the work-hardened ones and the strength returns almost to the annealed value while ductility recovers.

> [!question]- Why are single crystals of HCP metals so anisotropic?
> They have only one close-packed plane (basal) and three slip directions in it. A load nearly perpendicular to that plane resolves almost no shear ($\phi\approx0$) and the crystal is hard; a 45° load is very soft.

## 4. Connections

- [[Mohr's Circle for Stress]] — the resolved shear stress $\sigma\cos\phi\cos\lambda$ is the stress transformation of [[Plane Stress Transformation]] onto the slip plane.
- [[Tensile Test, True Stress-Strain and Hardness]] — work hardening is the slope of the true stress–strain curve.
- [[Heat Treatment of Steel - TTT and CCT Diagrams]] — martensite is the hardest steel because carbon in solution and a huge dislocation density block slip.
- [[Torsion of Circular Shafts]] — shear yielding on the 45° plane and the CRSS idea in a polycrystal.
