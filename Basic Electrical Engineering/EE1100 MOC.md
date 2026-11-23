---
tags: [EE1100, MOC, course]
course: EE1100 - Basic Electrical Engineering
instructor: Prof. Debapriya Das, IIT Kharagpur
playlist_url: https://www.youtube.com/playlist?list=PLbRMhDVUMngfdEXVcdf_ijj2Eub-UHs_y
---

# EE1100: Basic Electrical Engineering — Map of Content

Part of [[Home|Ajay's Engineering Wiki]]. For future LLM-assisted edits, follow [[LLM Wiki Guide]].

Source playlist: [Fundamentals of Electrical Engineering — Prof. Debapriya Das (NPTEL, IIT Kharagpur)](https://www.youtube.com/playlist?list=PLbRMhDVUMngfdEXVcdf_ijj2Eub-UHs_y)

This is the index note for the course. Every week note links back here, and links forward/backward to adjacent weeks so the graph view shows a clean spine. Recurring atomic concepts (laws, theorems, quantities) live in [[Concepts]] and are linked from every week that uses them — that's what makes the graph a real web instead of a chain.

## Weekly spine

1. [[01 Basic Concepts and Basic Laws|Week 1 — Basic Concepts and Basic Laws]]
2. [[02 Methods of Circuit Analysis|Week 2 — Methods of Circuit Analysis]]
3. [[03 DC Network Theorems|Week 3 — DC Network Theorems]]
4. [[04 Capacitors, Inductors and First Order Circuits|Week 4 — Capacitors, Inductors and First-Order Circuits]]
5. [[05 Sinusoids and Phasors|Week 5 — Sinusoids and Phasors]]
6. [[06 Sinusoidal Steady-State Analysis|Week 6 — Sinusoidal Steady-State Analysis]]
7. [[07 AC Circuit Analysis and Network Theorems|Week 7 — AC Circuit Analysis and Network Theorems]]
8. [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance and Magnetically Coupled Circuits]]
9. [[09 Three Phase Circuits and Power Measurement|Week 9 — Three Phase Circuits and Power Measurement]]
10. [[10 Single Phase Transformers|Week 10 — Single Phase Transformers]]
11. [[11 Three Phase Induction Machines|Week 11 — Three Phase Induction Machines]]
12. [[12 DC Machines|Week 12 — DC Machines]]

## By theme

- **DC circuits:** Weeks 1–4 → [[Concepts#Ohm's Law|Ohm's Law]], [[Concepts#Kirchhoff's Laws|KVL/KCL]], [[Concepts#Network Theorems|network theorems]]
- **AC circuits:** Weeks 5–9 → [[Concepts#Phasors|phasors]], [[Concepts#Impedance and Admittance|impedance]], [[Concepts#Power in AC Circuits|AC power]]
- **Machines:** Weeks 10–12 → transformers, induction machines, DC machines, all built on [[Concepts#Magnetic Coupling|magnetic coupling]] from Week 8

## Concept index

See [[Concepts]] for the full glossary (laws, theorems, quantities, with diagrams) shared across weeks. A few concepts also have their own standalone atomic notes, built while solving tutorials:
- [[Voltage Divider Rule|Voltage Divider Rule]]
- [[Series-Parallel Resistance Reduction|Series-Parallel Resistance Reduction]]

## Tutorials

All eight tutorial sheets are solved, one note per question, with the theory explained first: see [[Problems - MOC]] for the full map, the concept-coverage table and the list of printed answers that differ from a direct calculation.

| # | Tutorial | Weeks | Qs | Theory |
|---|---|---|---|---|
| 1 | [[Tutorial 1 - Circuit Laws and Theorems|Circuit Laws and Theorems]] | 1–3 | 14 | [[Theory - Circuit Laws and Network Theorems]] |
| 2 | [[Tutorial 2 - Transient Analysis of DC Circuits|Transient Analysis of DC Circuits]] | 4 | 12 | [[Theory - Transients in RL, RC and RLC Circuits]] |
| 3 | [[Tutorial 3 - AC Circuit Analysis|AC Circuit Analysis]] | 5–7 | 12 | [[Phasors and Complex Algebra]], [[Impedance and Series-Parallel AC Circuits]], [[AC Power and Power Factor]], [[Nodal and Mesh Analysis (AC)]], [[Thevenin, Norton and Maximum Power Transfer (AC)]], [[Power Factor Correction]], [[Sinusoidal Waveforms, RMS and Average Value]] |
| 4 | [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits|Resonance, Filter and Three-Phase Circuits]] | 8–9 | 12 | [[Theory - Resonance and Passive Filters]], [[Theory - Three-Phase Circuits]] |
| 5 | [[Tutorial 5 - Diode Circuits and Applications|Diode Circuits and Applications]] | diodes | 21 | [[Theory - Diode Models and Circuit Analysis]] |
| 6 | [[Tutorial 6 - Operational Amplifiers|Operational Amplifiers]] | op-amps | 12 | [[Theory - Operational Amplifiers]] |
| 7 | [[Tutorial 7 - Transformers|Transformers]] | 10 | 10 | [[10 Single Phase Transformers]] |
| 8 | [[Tutorial 8 - Induction Machines|Induction Machines]] | 11 | 11 | [[Theory - Three-Phase Induction Machines]] |

Building blocks that came out of solving the tutorials: [[Voltage Divider Rule]], [[Series-Parallel Resistance Reduction]].

Companion notes that bridge the tutorials:
- [[AC Transients|AC Transients]]: the bridge between Tutorial 2 (DC transients) and Tutorial 3 (AC steady state):
  - [[First-Order AC Transients (RC and RL)|First-Order AC Transients (RC and RL)]]
  - [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients (Series and Parallel RLC)]]
- [[RLC Circuits - Responses|RLC Circuits — Responses]]: series vs parallel, DC vs AC, step vs steady-state, all with plotted graphs:
  - [[Series RLC Natural Response - Damping Cases|Series RLC Natural Response — Damping Cases]]
  - [[Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response — Damping Cases]]
  - [[Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]]
  - [[DC Step Response of RLC Circuits|DC Step Response of RLC Circuits]]
  - [[AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response of RLC Circuits]]
  - [[Frequency Response and Resonance Curves|Frequency Response and Resonance Curves]]

### Exam / revision map
- **Network theorems and two-terminal reduction** (Tutorial 1 Q5, Q8–Q10; Tutorial 3 Q11, Q12): remove the load, $V_{oc}$ then $R_{th}$, finish in one line; conjugate match for AC maximum power.
- **Switching circuits** (Tutorial 2): initial condition from $v_C$ or $i_L$, $\tau$ from the *new* circuit; second-order by $R$ against $2\sqrt{L/C}$.
- **Phasor questions** (Tutorial 3): peak versus rms, lead versus lag, sign of $Q$.
- **Resonance and filters** (Tutorial 4 Q1–Q8): $\omega_0,\ Q,\ BW$, exact band edges at low $Q$, $-20$ dB design.
- **Three-phase** (Tutorial 4 Q9–Q12): which of $V$ or $I$ carries the $\sqrt3$ in star and delta.
- **Machines** (Tutorial 7, 8): equivalent circuit, power flow ($P_g:P_{cu2}:P_{mech}=1:s:1-s$), $s_m=r_2'/Z_k$.

## Transformers and induction machines (Lectures 35–41)

Concept notes built from the lecture slides, to be read with [[10 Single Phase Transformers|Week 10]] and [[11 Three Phase Induction Machines|Week 11]]:
- [[Transformer Voltage Regulation and Efficiency]] — Lecture 39: regulation, zero-regulation angle, maximum efficiency, worked example
- [[Induction Machines - Types, Construction and Applications]] — Lecture 40: classification, squirrel-cage vs slip-ring, NEMA classes, efficiency
- [[Revolving Magnetic Field and Synchronous Speed]] — Lecture 41: $\tfrac32F_m\sin(\omega t-\alpha)$, $n_s=120f/P$
- [[Induction Motor - Slip, Rotor Circuit and Power Flow]] — Lecture 41: slip, $f_2=sf_1$, $r_2/s$, $P_g:P_{cu}:P_{em}=1:s:(1-s)$

Interactive animations: [Three-phase revolving field](revolving%20field%20animation.html) · [Transformer current and flux](transformer-current-flux-animation.html).

## Cross-domain synthesis

The same RLC/impedance/resonance machinery reappears — in different notation — in [[Strength of Materials - MOC|Strength of Materials]] (buckling, energy methods, stress transformation) and in [[2nd Order ODEs - MOC|Differential Equations]]. See [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the eleven explicit connections. Newest EE-relevant ones: [[Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] (Weeks 10 and 12), [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors]] (Week 5 phasors), and [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] (KCL/KVL beyond circuits).

## Study log

- [ ] Week 1
- [ ] Week 2
- [ ] Week 3
- [ ] Week 4
- [ ] Week 5
- [ ] Week 6
- [ ] Week 7
- [ ] Week 8
- [ ] Week 9
- [ ] Week 10
- [ ] Week 11
- [ ] Week 12

## Continues in
- [[Measurements, Instrumentation and Control - MOC]] — op-amps, filters and bridges used for signal conditioning.
