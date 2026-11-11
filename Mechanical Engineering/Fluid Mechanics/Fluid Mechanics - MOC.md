---
tags:
  - fluid-mechanics
  - MOC
  - course
course: AM2530 Fluid Mechanics
instructor: Dr. Anubhab Roy
---

# Fluid Mechanics — Map of Content

Part of [[Home|Ajay's Engineering Wiki]]. For future LLM-assisted edits, follow [[LLM Wiki Guide]].

This is the index note for the course, reorganized into topic folders (previously a single flat, partly-empty "Lecture 1" folder). Every note links back here and to its neighbors, and cross-links into [[Strength of Materials - MOC|Strength of Materials]], [[EE1100 MOC|EE1100]], and [[ODE (Ordinary Differential Equations)|Differential Equations]] wherever the same underlying mathematics reappears — see [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the fully worked-out connections.

## 00 Introduction and Fundamental Concepts
- [[Introduction|Introduction]]
- [[Fluids and Solids|Fluids and Solids]]
- [[Static Equilibrium|Static Equilibrium]]
- [[Continuum Concept|Continuum Concept]]
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Ideal Fluid|Ideal Fluid]]

## 01 Dimensionless Numbers
- [[Buckingham Pi Theorem|Buckingham π Theorem]] — the general method that produces every dimensionless number below (Re, Fr, We, Eu, Ma, Kn, De)
- [[Knudsen Number|Knudsen Number]]
- [[Deborah Number|Deborah Number]]

## 02 Fluid Statics
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
- [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]
- [[Manometers|Manometers]]
- [[Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]
- [[Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]]
- [[Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]]
- [[Stability of Floating Bodies - Metacentre|Stability of Floating Bodies — Metacentre]]

## 03 Fluid Kinematics
- [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[Streamlines, Pathlines, Streaklines and Timelines|Streamlines, Pathlines, Streaklines and Timelines]]

## 04 Control Volume Analysis
- [[System and Control Volume|System and Control Volume]]
- [[Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Conservation of Mass (Continuity Equation)|Conservation of Mass (Continuity Equation)]]
- [[Linear Momentum Equation|Linear Momentum Equation]]
- [[Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications — Jets, Vanes, Bends]]

## 05 Centroids and Centre of Mass
- [[Centre of Mass and Centroids|Centre of Mass and Centroids]]
- [[Composite Bodies and Cutouts|Composite Bodies and Cutouts]]
- [[Second Moments of Area|Second Moments of Area]]

## 06 Dimensional Analysis and Similitude
- [[Dimensional Analysis and Similitude - Formula Bank|Dimensional Analysis and Similitude — Formula Bank]] — homogeneity, Π theorem, repeating variables, Re/Fr/Ma/We/… table, geometric/kinematic/dynamic similarity, model laws
- [[Dimensional Analysis and Similitude - Solved Problems|Solved Problems]] — capillary rise, pump and wave groups, sphere→balloon, aircraft altitude, car drag at altitude, hydraulic models

## 07 Differential Kinematics and Mass Conservation
- [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Differential Mass Conservation and Fluid Kinematics — Formula Bank]] — differential continuity, stream function, translation/rotation/deformation, vorticity, circulation, potential
- [[Differential Mass Conservation and Fluid Kinematics - Solved Problems|Solved Problems]] — acceleration, continuity, ψ and φ, deforming element, vortices

## 08 Incompressible Inviscid Flow
- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Incompressible Inviscid Flow and Bernoulli — Formula Bank]] — Euler's equations, Bernoulli (derivation, restrictions), static/stagnation/dynamic pressure, Pitot, wall tap
- [[Incompressible Inviscid Flow and Bernoulli - Solved Problems|Solved Problems]] — fire hose, venturi, blimp, wind tunnel, Pitot readings, tank draining, unsteady pipe start-up, channel step

## 09 Pipe Flow and Losses
- [[Pipe Flow and Losses - Formula Bank|Pipe Flow and Losses — Formula Bank]] — energy equation with losses, Darcy–Weisbach, friction factor (laminar, Colebrook, Haaland, fully rough), Moody chart, minor losses and equivalent lengths, the three pipe problems
- [[Pipe Flow and Losses - Solved Problems|Solved Problems (GPS 7 & 8)]] — house water supply with booster or larger pipe, gravity drainpipes, industrial supply line, Roman nozzle with diffuser, scaled water main, laminar tube from a tank

## 10 Viscous Flow and Exact Solutions
- [[Viscous Flow and Exact Solutions - Formula Bank|Viscous Flow and Exact Solutions — Formula Bank]] — the one-ODE recipe for unidirectional flow, plane Couette and Poiseuille, film flow, Hagen–Poiseuille, annulus, stress tensor, creeping flow
- [[Viscous Flow and Exact Solutions - Solved Problems|Solved Problems (GPS 9 & 10)]] — flow chamber, lava film, stagnation-point flow, wire coating, dashpot, syringe, siphon with cavitation limit, pump with parallel or larger pipe

*Tools:* `Tools/fm_core.py` (checks every number and Π group), `Tools/fm_viz.py` (figures in `assets/`), `Tools/fm_pipe.py` (pipe-flow solutions and Moody-chart figures), `Tools/fm_gps9_10.py` (viscous-flow solutions, siphon and pump numbers, figures `FM-V*`).

## The four biggest problem-solving ideas

$$\boxed{\text{Hydrostatics: }P=\rho gh}\qquad\boxed{\text{Curved surface: }H\to\text{projection},\ V\to\text{imaginary-fluid weight}}$$
$$\boxed{\text{Mass: Inflow}-\text{Outflow}=\text{Accumulation}}\qquad\boxed{\text{Momentum: Force}=\text{Momentum out}-\text{Momentum in}}$$

And for floating-body stability: $I_O\to BM=\dfrac{I_O}{V_{\rm sub}}\to GM=BM-BG\to\boxed{GM>0\Rightarrow\text{stable}}$.

## Cross-domain synthesis

Continuity ↔ KCL, momentum/RTT ↔ Reynolds Transport bookkeeping shared with circuit nodal analysis, metacentric stability ↔ column buckling, centroids/second moments of area shared directly with beam bending — see [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the fully worked connections across all vaults. Most relevant here: [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] (continuity, Bernoulli ↔ KCL, KVL), [[Second Moments of Area - One Integral, Many Jobs|Second Moments of Area]] (centre of pressure, metacentre), and [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] (viscosity vs shear modulus, Deborah number).

## Study log
- [ ] Introduction and Fundamental Concepts
- [ ] Dimensionless Numbers
- [ ] Fluid Statics
- [ ] Fluid Kinematics
- [ ] Control Volume Analysis
- [ ] Centroids and Centre of Mass

## Continues in
- [[Heat Transfer - MOC]] — boundary layers and convection reuse the dimensionless-number method.
- [[Foundations of Thermal Engineering - MOC]] — turbomachines and compressible flow extend control-volume analysis.
