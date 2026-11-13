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
- [[Density, Specific Weight and Compressibility|Density, Specific Weight and Compressibility]] — $\rho$, $\gamma$, SG, bulk modulus, speed of sound, when flow is incompressible
- [[Surface Tension and Capillarity|Surface Tension and Capillarity]] — Young–Laplace pressure jump, contact angle, capillary rise
- [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]] — $p_v(T)$, cavitation number, NPSH, siphon limit

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
- [[Moving and Accelerating Control Volumes|Moving and Accelerating Control Volumes]] — relative velocity, the inertial term, moving vanes and rockets
- [[Angular Momentum Principle|Angular Momentum Principle]] — torque on a control volume, sprinkler, Euler turbomachine equation

## 05 Centroids and Centre of Mass
- [[Centre of Mass and Centroids|Centre of Mass and Centroids]]
- [[Composite Bodies and Cutouts|Composite Bodies and Cutouts]]
- [[Second Moments of Area|Second Moments of Area]]

## 06 Dimensional Analysis and Similitude
- [[Dimensional Analysis and Similitude - Formula Bank|Dimensional Analysis and Similitude — Formula Bank]] — homogeneity, Π theorem, repeating variables, Re/Fr/Ma/We/… table, geometric/kinematic/dynamic similarity, model laws
- [[Dimensional Analysis and Similitude - Solved Problems|Solved Problems]] — capillary rise, pump and wave groups, sphere→balloon, aircraft altitude, car drag at altitude, hydraulic models
- [[Important Dimensionless Groups|Important Dimensionless Groups]] — Re, Fr, We, Eu, Ma, Ca, St as force ratios, which one to use when
- [[Flow Similarity and Model Studies|Flow Similarity and Model Studies]] — geometric/kinematic/dynamic similarity, Froude and Reynolds scaling, incomplete similarity

## 07 Differential Kinematics and Mass Conservation
- [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Differential Mass Conservation and Fluid Kinematics — Formula Bank]] — differential continuity, stream function, translation/rotation/deformation, vorticity, circulation, potential
- [[Differential Mass Conservation and Fluid Kinematics - Solved Problems|Solved Problems]] — acceleration, continuity, ψ and φ, deforming element, vortices
- [[Differential Continuity Equation|Differential Continuity Equation]] — $\partial_t\rho+\nabla\cdot(\rho\mathbf V)=0$, incompressible $\nabla\cdot\mathbf V=0$, finding a missing component
- [[Motion of a Fluid Element|Motion of a Fluid Element]] — translation, rotation, linear and angular deformation, strain rate
- [[Vorticity and Circulation|Vorticity and Circulation]] — $\zeta=\nabla\times\mathbf V$, $\Gamma=\oint\mathbf V\cdot d\mathbf l$, Rankine vortex
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]] — potential $\phi$, stream function $\psi$, Laplace's equation

## 08 Incompressible Inviscid Flow
- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Incompressible Inviscid Flow and Bernoulli — Formula Bank]] — Euler's equations, Bernoulli (derivation, restrictions), static/stagnation/dynamic pressure, Pitot, wall tap
- [[Incompressible Inviscid Flow and Bernoulli - Solved Problems|Solved Problems]] — fire hose, venturi, blimp, wind tunnel, Pitot readings, tank draining, unsteady pipe start-up, channel step
- [[Euler's Equations of Fluid Motion|Euler's Equations of Fluid Motion]] — $\rho D\mathbf V/Dt=-\nabla p+\rho\mathbf g$, streamline coordinates, accelerating and rotating tanks
- [[Bernoulli Equation|Bernoulli Equation]] — derivation, six restrictions, forms, Torricelli and venturi
- [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]] — $p_0=p+\tfrac12\rho V^2$, $C_p$, compressibility correction
- [[Pitot Tube and Pressure Measurement|Pitot Tube and Pressure Measurement]] — Pitot-static probe, wall taps, manometer readings

## 09 Pipe Flow and Losses
- [[Pipe Flow and Losses - Formula Bank|Pipe Flow and Losses — Formula Bank]] — energy equation with losses, Darcy–Weisbach, friction factor (laminar, Colebrook, Haaland, fully rough), Moody chart, minor losses and equivalent lengths, the three pipe problems
- [[Pipe Flow and Losses - Solved Problems|Solved Problems (GPS 7 & 8)]] — house water supply with booster or larger pipe, gravity drainpipes, industrial supply line, Roman nozzle with diffuser, scaled water main, laminar tube from a tank
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] — Reynolds' regimes, profiles, Reynolds stress, entry length
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]] — Bernoulli plus pump, turbine and friction; EGL and HGL; power
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]] — major losses, Colebrook, Haaland, hydraulic diameter
- [[Moody Chart|Moody Chart]] — laminar, smooth, transition and fully rough regions, how to read it
- [[Minor Losses|Minor Losses]] — $K$ and $L_e/D$, Borda–Carnot expansion, entrances and exits
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]] — series, parallel, find $Q$ or $D$, pump operating point

## 10 Viscous Flow and Exact Solutions
- [[Viscous Flow and Exact Solutions - Formula Bank|Viscous Flow and Exact Solutions — Formula Bank]] — the one-ODE recipe for unidirectional flow, plane Couette and Poiseuille, film flow, Hagen–Poiseuille, annulus, stress tensor, creeping flow
- [[Viscous Flow and Exact Solutions - Solved Problems|Solved Problems (GPS 9 & 10)]] — flow chamber, lava film, stagnation-point flow, wire coating, dashpot, syringe, siphon with cavitation limit, pump with parallel or larger pipe
- [[Stress in a Moving Fluid|Stress in a Moving Fluid]] — traction $\boldsymbol\sigma\cdot\mathbf n$, $\sigma_{ij}=-p\delta_{ij}+\tau_{ij}$, Cauchy's equation
- [[Newtonian Constitutive Relation|Newtonian Constitutive Relation]] — $\tau_{ij}=2\mu\dot\varepsilon_{ij}$, Stokes' hypothesis, bulk viscosity
- [[Navier-Stokes Equations|Navier-Stokes Equations]] — derivation, terms, cylindrical form, vorticity form
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]] — no-slip, free surface, interface, symmetry
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]] — scaled N–S, Stokes flow, boundary-layer thickness
- [[Plane Couette Flow|Plane Couette Flow]] — shear-driven flow, journal bearing, Couette–Poiseuille
- [[Plane Poiseuille Flow|Plane Poiseuille Flow]] — pressure-driven channel flow, cubic law
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] — laminar pipe flow, $Q\propto D^4$, $f=64/Re$

*Tools:* `Tools/fm_core.py` (checks every number and Π group), `Tools/fm_viz.py` (figures in `assets/`), `Tools/fm_pipe.py` (pipe-flow solutions and Moody-chart figures), `Tools/fm_gps9_10.py` (viscous-flow solutions, siphon and pump numbers, figures `FM-V*`), `Tools/fm_concepts_viz.py` (figures `FM-N*` for the concept notes), `Tools/fm_concepts_check.py` (recomputes every worked number in them).

## Syllabus coverage

Where each topic of the course outline is covered (formula bank for the equations, concept note for the explanation).

| Syllabus topic | Concept notes | Formula bank |
|---|---|---|
| Fluid properties, continuum, density, compressibility, viscosity, non-Newtonian fluids, surface tension, vapour pressure, cavitation | [[Continuum Concept]], [[Density, Specific Weight and Compressibility]], [[Viscosity and Newton's Law of Viscosity]], [[Newtonian and Non-Newtonian Fluids]], [[Surface Tension and Capillarity]], [[Vapour Pressure and Cavitation]] | — |
| Fluid statics, pressure, manometry, hydrostatic forces, buoyancy, stability | [[Pressure and the Hydrostatic Equation]], [[Absolute, Gauge and Vacuum Pressure]], [[Manometers]], [[Hydrostatic Force on Plane Surfaces and Centre of Pressure]], [[Hydrostatic Force on Curved Surfaces]], [[Buoyancy and Archimedes' Principle]], [[Stability of Floating Bodies - Metacentre]] | — |
| Kinematics: velocity and acceleration fields, line families | [[Lagrangian and Eulerian Descriptions]], [[Material Derivative and Fluid Acceleration]], [[Streamlines, Pathlines, Streaklines and Timelines]] | [[Differential Mass Conservation and Fluid Kinematics - Formula Bank]] |
| Control-volume analysis: RTT, mass, linear and angular momentum, moving and accelerating CVs | [[System and Control Volume]], [[Reynolds Transport Theorem]], [[Conservation of Mass (Continuity Equation)]], [[Linear Momentum Equation]], [[Moving and Accelerating Control Volumes]], [[Angular Momentum Principle]] | — |
| Dimensional analysis and similitude | [[Buckingham Pi Theorem]], [[Important Dimensionless Groups]], [[Flow Similarity and Model Studies]] | [[Dimensional Analysis and Similitude - Formula Bank]] |
| Differential mass conservation, element motion, vorticity, circulation | [[Differential Continuity Equation]], [[Motion of a Fluid Element]], [[Vorticity and Circulation]], [[Rotational and Irrotational Flow]] | [[Differential Mass Conservation and Fluid Kinematics - Formula Bank]] |
| Inviscid flow: Euler, Bernoulli, static/stagnation/dynamic pressure, Pitot | [[Euler's Equations of Fluid Motion]], [[Bernoulli Equation]], [[Static, Stagnation and Dynamic Pressure]], [[Pitot Tube and Pressure Measurement]] | [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] |
| Stress, constitutive law, Navier–Stokes, boundary conditions, Reynolds number | [[Stress in a Moving Fluid]], [[Newtonian Constitutive Relation]], [[Navier-Stokes Equations]], [[Boundary Conditions in Fluid Flow]], [[Nondimensionalisation and the Reynolds Number]] | [[Viscous Flow and Exact Solutions - Formula Bank]] |
| Exact solutions: Couette, Poiseuille, Hagen–Poiseuille | [[Plane Couette Flow]], [[Plane Poiseuille Flow]], [[Hagen-Poiseuille Flow]] | [[Viscous Flow and Exact Solutions - Formula Bank]] |
| Internal flows: regimes, energy equation with head loss, major and minor losses, pipe systems | [[Laminar and Turbulent Flow]], [[Energy Equation with Head Loss]], [[Darcy-Weisbach Equation and Friction Factor]], [[Moody Chart]], [[Minor Losses]], [[Pipe Systems and the Three Problems]] | [[Pipe Flow and Losses - Formula Bank]] |

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
