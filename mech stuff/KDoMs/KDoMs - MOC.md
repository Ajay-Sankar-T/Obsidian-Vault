---
tags: [MOC, course, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
status: active
---

# KDoMs — Map of Content

Part of [[Home|Ajay's Engineering Wiki]]. Edit rules: [[LLM Wiki Guide]].

Kinematics and dynamics of machinery (ME 2201). Source text: *Theory of Mechanisms and Machines* (Ghosh & Mallik) — the PDF is local only (git-ignored). Each bank below is a formula sheet with equation numbers from the book, worked benchmarks, figures in its own `assets/` folder, and Python/HTML tools for checking numbers.

## Main spine

1. **Velocity and acceleration of a mechanism** — find motion of every link, given the input
   - [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Analytical Method|Analytical method]] — loop closure, differentiated; linear in the unknowns
   - [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Graphical Methods (Polygons)|Graphical methods (polygons)]] — velocity/acceleration polygons, images, instantaneous centres
2. **Synthesis** — design a mechanism to meet a motion requirement
   - [[KDoMs/Synthesis-Formula-Bank/Motion and Path Generation - Graphical Methods|Graphical synthesis]] — inversion, poles, three/four positions
   - [[KDoMs/Synthesis-Formula-Bank/Motion and Path Generation - Analytical Methods|Analytical synthesis]] — dyads, Chebyshev spacing, Freudenstein
3. **Gears** — [[KDoMs/Formula-Bank/Gear Formula Bank|Gear Formula Bank]] — involute geometry, interference, contact ratio, gear trains, epicyclic trains
4. **Cams, flywheels and balancing** — motion from a prescribed law, and smoothing or cancelling the forces it causes
   - [[Cam Motion Laws and the Flat-Face Follower]] — cycloidal law, profile, curvature, driving-effort eccentricity
   - [[Flywheel Sizing from the Turning-Moment Diagram]] — mean torque, $\Delta E$, $C_s$, mass
   - [[Balancing of Rotors - Static and Dynamic]] — force and couple polygons, two-plane replacement

```text
Mechanism given ──► Velocity / acceleration analysis ──► (loads, power)
Motion required ──► Synthesis ──► mechanism ──► analysis to check
Speed ratio required ──► Gears ──► train value ──► torques
```

## Method selector

| I need… | Use |
| --- | --- |
| Link velocities/accelerations at one configuration, by hand | [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Graphical Methods (Polygons)|Polygons]] |
| Velocities/accelerations over a whole cycle, or in a program | [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Analytical Method|Analytical]] |
| A sliding joint on a rotating link (Coriolis) | Coincident-point relation in either method; [[KDoMs/Problem-2.19-solution|Problem 2.19]] |
| Design a linkage through 3 positions of a body | [[KDoMs/Synthesis-Formula-Bank/Motion and Path Generation - Graphical Methods|Graphical synthesis]] → [[KDoMs/Tutorial-solutions/Tutorial-6-solution|Tutorial 6]] |
| Exact, programmable synthesis | [[KDoMs/Synthesis-Formula-Bank/Motion and Path Generation - Analytical Methods|Analytical synthesis]] |
| Tooth numbers, interference, centre distance | [[KDoMs/Formula-Bank/Gear Formula Bank|Gear Formula Bank]] → [[KDoMs/Tutorial-solutions/Tutorial-7-solution|Tutorial 7]] |
| Speeds and torques in a planetary train | Gear Formula Bank §11–12 |
| Cam profile for a given lift law, or check curvature and jamming | [[Cam Motion Laws and the Flat-Face Follower]] → [[KDoMs/Tutorial-solutions/Tutorial-9-solution|Tutorial 9]] |
| Flywheel mass for a given speed band | [[Flywheel Sizing from the Turning-Moment Diagram]] → [[KDoMs/Tutorial-solutions/Tutorial-10-solution|Tutorial 10 Q1]] |
| Add or remove mass to balance a rotor in chosen planes | [[Balancing of Rotors - Static and Dynamic]] → [[KDoMs/Tutorial-solutions/Tutorial-10-solution|Tutorial 10 Q2]] |

## Tutorials and problems

| Item | Tests | Source |
| --- | --- | --- |
| [[KDoMs/Problem-2.19-solution|Problem 2.19 — quick-return (slotted lever)]] | coincident points, Coriolis, velocity + acceleration | Ghosh & Mallik |
| [[KDoMs/Tutorial-solutions/Tutorial-5-solution|Tutorial 5 — Atkinson engine mechanism]] | velocity/acceleration analysis, instant centre | `Tutorial 5.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-6-solution|Tutorial 6 — tipper-dumper]] | three-position rigid-body guidance, inversion | `Tutorial 6.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-7-solution|Tutorial 7 — involute gears]] | interference, centre distance, tooth data | `Tutorial 7.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-9-solution|Tutorial 9 — flat-face cam, cycloidal motion]] | [[Cam Motion Laws and the Flat-Face Follower]]: profile, graphical construction, $v_{\max}$, $a_{\max}$, $\rho$, driving-effort eccentricity | `Tutorial 9.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-10-solution|Tutorial 10 — flywheel and two-plane balancing]] | [[Flywheel Sizing from the Turning-Moment Diagram]], [[Balancing of Rotors - Static and Dynamic]] | `Tutorial 10.pdf` (Mallik & Ghosh 7.14) |

The statements are in the `Tutorials/` folder (`Tutorial 1.pdf`–`Tutorial 10.pdf`). Tutorials 5–7, 9 and 10 are solved above; Tutorials 1–4 and 8 are not yet solved in the vault.

### Exam patterns
- **Cam, "draw profile / find $v$, $a$, $\rho$"** — recognise by a lift table plus a named law. Needs $s,s',s''$ at one angle; flat face: $\rho=R_0+s+s''$, $\varepsilon=s'-e$. Offset never changes a flat-face outline.
- **Flywheel from a torque diagram** — recognise by triangle areas and a scale. Needs $T_{\text{mean}}=W/(\text{cycle angle})$, then the area above the mean line, then $I=\Delta E/(\omega^2C_s)$.
- **Balance "in other planes"** — recognise by trial masses or inaccessible planes. Needs a couple polygon about one plane, a force polygon for the other, and care with add versus remove.

### Problem coverage
| Concept | Problems | Status |
| --- | --- | --- |
| Cycloidal cam, flat-face follower | Tutorial 9 | solved |
| Flywheel sizing | Tutorial 10 Q1 | solved |
| Two-plane balancing | Tutorial 10 Q2 | solved |

## Tools

Verification scripts and browser explorers sit beside each bank: `va_core.py`, `synth_core.py`, `gear_core.py` (numbers) · `*_viz.py` (figures) · `va-explorer.html`, `va-polygons.html`, `synthesis-explorer.html`, `gear-explorer.html` (interactive). Same pattern as `Fluid Mechanics/Tools/`.

## Cross-domain links

- [[Cross-Domain Synthesis/Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — gear train ↔ ideal transformer ↔ lever; the same power-conservation ratio rules
- [[Cross-Domain Synthesis/Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors — Phasors, Velocity Polygons and Complex Kinematics]] — $\omega\times r$ is multiplication by $j\omega$; a velocity polygon is a phasor diagram
- [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]] — mechanism dynamics with compliance and inertia land here
- [[Strength of materials/03 Torsion/Power Transmission by Shafts|Power Transmission by Shafts]] — what the gear train's torques do to a shaft

## Status

- [x] Velocity/acceleration banks
- [x] Synthesis banks
- [x] Gear bank
- [x] Cam, flywheel and balancing notes; Tutorials 9 and 10 solved
- [ ] Tutorials 2–4 and 8 solved

## Continues in
- [[Introduction to Machine Design - MOC]] — gear design and mechanism loads.
- [[Manufacturing Technology - MOC]] — machine-tool kinematics, CNC and robotics.
- [[Computer Aided Machine Drawing - MOC]] — drawing the mechanisms and assemblies.
