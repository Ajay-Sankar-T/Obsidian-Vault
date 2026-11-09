---
tags: [applied-mechanics-lab, AM2540, exam-prep, MOC]
up: "[[Applied Mechanics Lab - MOC]]"
aliases: [AM2540 mock exams, Applied Mechanics Lab exam preparation, Applied Mechanics Lab mock questions]
---

# Applied Mechanics Lab — Mock Papers

Part of [[Applied Mechanics Lab - MOC]] · theory behind it: [[Strength of Materials - Formula Bank]] · long-form practice: [[Strength of Materials - Question Bank]]

> [!abstract] What is here
> Three full mock papers in the style of the AM2540 end-semester paper (60 marks, 45 minutes, 13 compulsory questions, short conceptual answers with a few numericals) and the real 2023 paper analysed and answered. Each question has a folded model answer with the marks split. The experiments that the paper covers but the manuals do not (strain gauges, photoelasticity, the mirror-and-scale twist) now have their own notes.

## The papers

| Paper | Emphasis | Best used |
|---|---|---|
| [[Applied Mechanics Lab - Past Paper Pattern and Model Answers]] | what the examiner asks, and the length of answer that earns the marks | first, to calibrate |
| [[Mock Paper 1 - Strain Gauge, Torsion and Beams]] | the 2023 pattern with new data: bridges, hollow shafts, mirror-and-scale, failure planes, struts, fringes, steel-against-aluminium, overhangs | sit it timed |
| [[Mock Paper 2 - Tensile Tests, DIC and Buckling]] | tensile experiments: DIC, ES6 tester, true stress, timber, PVC, Euler derivation, gauge length, overhang self-weight | after the tensile and buckling notes |
| [[Mock Paper 3 - Bending, Photoelasticity and Instruments]] | three-point bending, photoelastic disk, Poisson ratio by gauges, instrument resolution, same-area shapes | last, as a check |

## How the three papers cover the experiments

| Experiment | Note | Paper 1 | Paper 2 | Paper 3 | 2023 |
|---|---|---|---|---|---|
| Strain gauge / bridge | [[Lab - Strain Gauge Measurement on a Cantilever Beam]] | Q1 | | Q4 | Q1 |
| Torsion | [[Lab - Torsion of Circular Shafts]] | Q2, Q3 | Q2 | Q2, Q3 | Q2, Q3 |
| Tension (ES6, DIC) | [[Lab - Tensile Test on the ES6 Tester]], [[Lab - Tensile Test of Mild Steel with DIC]] | Q4, Q6 | Q1, Q3, Q4, Q6, Q10 | Q5, Q8 | Q4, Q6 |
| Failure planes | [[Failure Planes - Ductile and Brittle Fracture]] | Q5 | Q5 | | Q5 |
| Buckling | [[Lab - Buckling of Struts]] | Q7 | Q7 | Q6, Q9 | Q7 |
| Photoelasticity | [[Lab - Photoelasticity - Fringes and Stress]] | Q8, Q9, Q10 | Q9 | Q7 | Q8, Q9, Q10 |
| Beam bending and deflection | [[Lab - Deflection of Beams (Three-Point Bending)]] | Q11, Q12, Q13 | Q11, Q12, Q13 | Q1, Q10, Q11, Q12, Q13 | Q11, Q12, Q13 |

## Scaling laws: the cheat-sheet for "what happens if…"

Most of the short questions are answered by an exponent. Know these cold.

| Quantity | Depends on | Question it answers |
|---|---|---|
| Shear stress in a shaft | $\tau\propto T/d^3$ | diameter halved: $\times8$ |
| Twist of a shaft | $\phi\propto TL/(Gd^4)$ | length doubled $\times2$; diameter doubled $\times\tfrac1{16}$; brass against steel $\times G_s/G_b$ |
| Beam deflection | $\delta\propto PL^3/(EI)$, $I\propto bh^3$ | depth doubled $\times\tfrac18$; flat to on edge $\times\tfrac1{(h/b)^2}$; steel to aluminium $\times3$ |
| Beam stress | $\sigma\propto M/S$, $S\propto bh^2$ | depth doubled $\times\tfrac14$ |
| Cantilever against simple beam | $k=3EI/L^3$ against $48EI/L^3$ | clamped ends: $\times\tfrac14$ (centre load) |
| Euler load | $P_{cr}\propto EI/(KL)^2$ | clamp both ends $\times4$; fixed–pinned $\times2$; length doubled $\times\tfrac14$ |
| Gauge bridge output | quarter $V_{ex}GF\varepsilon/4$ | half bridge $\times2$, full $\times4$; temperature cancels in adjacent arms |
| Photoelastic fringes | $N=8P/(\pi Df_\sigma)$ for a disk | load doubled $\times2$; material $f_\sigma$ halved $\times2$ |
| Tensile specimens | load $\propto d^2$, extension $\propto L_0$ | $d\to2d$: load $\times4$, curve of stress against strain unchanged |
| Mirror and scale | $\phi\approx s/2D$ | doubling $D$ halves the angle for the same reading |

## How to write a 4–9 mark answer

1. **Say the principle in one line** (the equation or the definition).
2. **Draw** a labelled sketch if the question says "sketch", "explain with a diagram" or concerns a pattern (curves, fracture, fringes, shapes).
3. **Give the reason**, in terms of a physical quantity ($\tau_{max}$ against $\sigma_1$, $I\propto h^3$, the adjacent arm of the bridge).
4. **Put a number** if data are given, with units, and check the order of magnitude.
5. **State the conclusion** in one sentence (which is larger, by how much, why).

## Common slips in this exam

- Answering from the manual's procedure instead of the physics: the question usually asks *why*.
- Writing a ratio of deflections with $E$ only, forgetting $I$ (Q11 of 2023, Q11 of Paper 1).
- Using the wrong thickness/width for $I$: $I=bh^3/12$ with $h$ the dimension **in the bending direction**.
- Leaving out the unit (N/mm/fringe) or the temperature argument (adjacent arms).
- Sketching the failure planes without saying which stress governs.
- Confusing polarisation with refraction, diffraction or scattering (the wrong options in the real MCQ).

## Plan for 45 minutes

| Minutes | What |
|---|---|
| 0–8 | the four MCQ/one-line questions (Q8, Q9, Q10 and Q2 or Q3): about 13 marks |
| 8–30 | the sketch and reasoning questions (Q4, Q5, Q6, Q11, Q12, Q13): about 30 marks |
| 30–42 | the long recall question (Q7) and Q1 |
| 42–45 | check units and that every sketch is labelled |

## Related
[[Strength of Materials - MOC]] · [[Euler Buckling of Columns]] · [[Torsion of Circular Shafts]] · [[Flexure Formula]] · [[Mohr's Circle for Stress]]
