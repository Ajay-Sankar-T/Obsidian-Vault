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

## Tutorials and problems

| Item | Tests | Source |
| --- | --- | --- |
| [[KDoMs/Problem-2.19-solution|Problem 2.19 — quick-return (slotted lever)]] | coincident points, Coriolis, velocity + acceleration | Ghosh & Mallik |
| [[KDoMs/Tutorial-solutions/Tutorial-5-solution|Tutorial 5 — Atkinson engine mechanism]] | velocity/acceleration analysis, instant centre | `Tutorial 5.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-6-solution|Tutorial 6 — tipper-dumper]] | three-position rigid-body guidance, inversion | `Tutorial 6.pdf` |
| [[KDoMs/Tutorial-solutions/Tutorial-7-solution|Tutorial 7 — involute gears]] | interference, centre distance, tooth data | `Tutorial 7.pdf` |

The statements are in `Tutorial 2.pdf`–`Tutorial 7.pdf` in this folder; Tutorials 2–4 are not yet solved in the vault.

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
- [ ] Tutorials 2–4 solved
