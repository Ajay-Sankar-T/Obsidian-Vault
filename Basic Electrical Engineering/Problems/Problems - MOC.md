---
tags: [EE1100, MOC, tutorial]
course: EE1100 - Basic Electrical Engineering
up: "[[EE1100 MOC]]"
aliases:
  - EE1100 Problems
  - EE1100 Tutorials
---

# EE1100 Problems: Map of Content

← up: [[EE1100 MOC|EE1100 MOC]] · tutorial sheets: `Resources/Tutorial Sheets/` · scripts: `Tools/`

All eight tutorial sheets are solved, **one note per question**, each following the same pattern: *what is tested → given → principle and why it applies → diagram → solution → result → check → trap → concepts used*. Every tutorial folder has an index (`Tutorial N - Title`), a theory note (or notes) that explains the ideas before the questions use them, and an `assets/` folder with the redrawn circuits, waveforms, phasor diagrams and response plots.

## The eight tutorials

| # | Tutorial | Weeks | Questions | Theory note(s) | Sheet |
|---|---|---|---|---|---|
| 1 | [[Tutorial 1 - Circuit Laws and Theorems]] | 1–3 | 14 | [[Theory - Circuit Laws and Network Theorems]] | [[Tutorial 1_Circuit Laws and Theorems.pdf]] |
| 2 | [[Tutorial 2 - Transient Analysis of DC Circuits]] | 4 | 12 | [[Theory - Transients in RL, RC and RLC Circuits]] | [[Tutorial 2 on Transient and steady state analysis of DC circuits.pdf]] |
| 3 | [[Tutorial 3 - AC Circuit Analysis]] | 5–7 | 12 | seven atomic notes in `Theory/` ([[Phasors and Complex Algebra]], [[Impedance and Series-Parallel AC Circuits]], [[AC Power and Power Factor]], …) | [[Tutorial 3 on Analysis of AC Circuits.pdf]] |
| 4 | [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] | 8–9 | 12 | [[Theory - Resonance and Passive Filters]], [[Theory - Three-Phase Circuits]] | [[Tutorial 4  on Resonance and  Three phase Circuits.pdf]] |
| 5 | [[Tutorial 5 - Diode Circuits and Applications]] | diodes | 21 (A1–A9, B1–B12) | [[Theory - Diode Models and Circuit Analysis]] | [[Tutorial 5 on Diode Circuits and Applications.pdf]] |
| 6 | [[Tutorial 6 - Operational Amplifiers]] | op-amps | 12 | [[Theory - Operational Amplifiers]] | [[Tutorial 6 on OP-AMP.pdf]] |
| 7 | [[Tutorial 7 - Transformers]] | 10 | 10 | [[10 Single Phase Transformers]], [[Transformer Voltage Regulation and Efficiency]] | [[Tutorial 7 on Transformer.pdf]] |
| 8 | [[Tutorial 8 - Induction Machines]] | 11 | 11 | [[Theory - Three-Phase Induction Machines]] | [[Tutorial 8 on Induction Machine new.pdf]] |

## Folder layout

```
Problems/
  Problems - MOC.md                         this page
  Tutorial N - <title>/
    Tutorial N - <title>.md                 index: question table, concept map, pattern recognition, exam hints
    Theory - <topic>.md                     the explained theory the questions rely on
    TN-Qk - <short title>.md                one solved question (T5 uses T5-A-Qk / T5-B-Qk)
    assets/                                 redrawn circuits, waveforms, phasor diagrams, plots
Tools/                                      ee_t1_t4_t8.py, ee_t6_t7.py (numbers), ee_figs_*.py (figures), ee_draw.py (schematic helpers)
```
Notes are linked by basename, so a note can move without breaking links; renamed notes keep their old names as `aliases`.

## Concept coverage

| Concept | Where it is explained | Problems that use it |
|---|---|---|
| KCL, KVL, series/parallel, dividers | [[Theory - Circuit Laws and Network Theorems]] | T1 Q1–Q3, Q7, Q13 |
| nodal, mesh, supernode, supermesh | same | T1 Q7, Q11, Q12, Q14; T3 Q9, Q11 |
| superposition | same | T1 Q6 |
| Thevenin / Norton, maximum power | same; [[Thevenin, Norton and Maximum Power Transfer (AC)]] | T1 Q5, Q8–Q10; T3 Q11, Q12; T8 Q5, Q11 |
| star–delta | same; [[Theory - Three-Phase Circuits]] | T1 Q13, Q14; T4 Q9–Q12 |
| $C$ and $L$ laws, DC steady state, energy | [[Theory - Transients in RL, RC and RLC Circuits]] | T2 Q1–Q4 |
| first-order switching | same | T2 Q4–Q6, Q8, Q9 |
| second-order RLC, damping | same; [[RLC Circuits - Responses]] | T2 Q7, Q10–Q12 |
| rms, phasors, impedance | [[Sinusoidal Waveforms, RMS and Average Value]], [[Phasors and Complex Algebra]], [[Impedance and Series-Parallel AC Circuits]] | T3 Q1–Q7, Q9, Q10 |
| complex power, power factor | [[AC Power and Power Factor]], [[Power Factor Correction]] | T3 Q5, Q8, Q10, Q12; T4 Q9–Q11 |
| resonance, $Q$, bandwidth, filters | [[Theory - Resonance and Passive Filters]] | T4 Q1–Q8 |
| three-phase star/delta, power | [[Theory - Three-Phase Circuits]] | T4 Q9–Q12 |
| diode models, rectifiers, clippers | [[Theory - Diode Models and Circuit Analysis]] | T5 |
| ideal op-amp circuits | [[Theory - Operational Amplifiers]] | T6 |
| transformer equivalent circuit, regulation, efficiency | [[10 Single Phase Transformers]], [[Transformer Voltage Regulation and Efficiency]] | T7 |
| revolving field, slip, torque–slip, equivalent circuit | [[Theory - Three-Phase Induction Machines]] | T8 |

## Verification
Every number in tutorials 1–4 and 8 is recomputed by `Tools/ee_t1_t4_t8.py` (183 comparisons with the printed answers: 175 agree, 8 differ and each is explained in the note); tutorials 6 and 7 by `Tools/ee_t6_t7.py`. Circuits and plots are redrawn by `Tools/ee_figs_t1.py`, `ee_figs_t2.py`, `ee_figs_t3_t4.py`, `ee_figs_t8.py` (shared helpers in `ee_draw.py`).

## Where the printed sheet answers differ from a direct calculation
These are not errors in the notes: each is shown in the question note with the computation.

| Tutorial | Question | Printed | Computed | Why |
|---|---|---|---|---|
| 1 | Q3 | $V_0=-6$ V | $-12$ V | contradicts the sheet's own $I_1=-2$ A and $P=24$ W |
| 1 | Q6 | 10.4 V | 10.33 V | rounding |
| 2 | Q8 | $v_o(1.3\ \text{ms})=25.6$ V | 15.2 V | output decays with $\tau=2.5$ ms |
| 2 | Q9 | $v_C(1.3\ \text{ms})=70.0$ V | 78.99 V | $\tau=0.833$ ms |
| 2 | Q7 | figure and text values differ | text solved | answer matches the text |
| 3 | Q12 | $Q$, $S$ entries swapped; "23.32 W each" | $-13.73$ VAr/15.85 VA (source 1); each source delivers 37.5 W | bookkeeping |
| 4 | Q6 | $\omega_2=1818$ | 1618 | typo |
| 4 | Q9 | $Q=2857.8$ VAr | 3300 VAr | $P/2$ used |
| 4 | Q10 | "line currents" 8.8 A | line 15.24 A, phase 8.8 A | phase currents printed |
| 8 | Q10 | $\eta=89.6\ \%$ | 90.2 % (89.7 % with full-$I_1$ copper loss) | loss bookkeeping |

## Related
- [[EE1100 MOC]] · [[Concepts]] · [[Wiki Maintenance Log]]
