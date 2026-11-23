---
title: Tutorial 3 - AC Circuit Analysis
course: EE1100 Basic Electrical Engineering
tutorial: 3
tags:
  - EE1100
  - tutorial
  - AC-circuits
  - phasors
source: "[[Tutorial 3 on Analysis of AC Circuits.pdf]]"
aliases:
  - EE1100 Tutorial 3
up: "[[EE1100 MOC]]"
---

# EE1100 Tutorial 3: AC Circuit Analysis

← up: [[EE1100 MOC|MOC]] · [[Problems - MOC|all tutorials]] · builds on: [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] · Source: [[Tutorial 3 on Analysis of AC Circuits.pdf]] · followed by: [[AC Transients|AC Transients]] and [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits|Tutorial 4]]

Twelve questions covering the full arc of single-phase AC analysis: from a raw waveform down to complex power and network theorems. The whole tutorial is one repeated reduction chain:

$$
\boxed{\text{Time-domain signal} \rightarrow \text{RMS} \rightarrow \text{Phasor} \rightarrow \text{Impedance} \rightarrow \text{Circuit analysis} \rightarrow \text{Power}}
$$

For $v(t)=V_m\sin(\omega t+\theta_v)$, the RMS phasor is $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta_v$, and every subsequent step uses the AC form of Ohm's law $\bar V=\bar I Z$, see [[Phasors and Complex Algebra]].

> [!abstract] How this folder is organised
> One note per question (`T3-Q1` … `T3-Q12`) with the diagram, the principle and why it applies, the full solution, a check and a trap. The **theory notes** the questions lean on live in `Theory/` (seven atomic notes listed below). Every number is recomputed in `../../Tools/ee_t1_t4_t8.py`; `python ee_figs_t3_t4.py` redraws the figures.

## Questions

| Q | Topic | Answer | Note |
|---|---|---|---|
| 1 | average and rms of square waves | (a) 0, $I_m$ (b) $I_m/2$, $I_m/\sqrt2$ | [[T3-Q1 - Average and RMS of Square Waves]] |
| 2 | rms of a staircase wave, power | 10 V, 12.91 V, 16.67 W | [[T3-Q2 - RMS of a Staircase Waveform]] |
| 3 | RL series: $Z$, $v(t)$, $L$ | $9+j12$; $424.5\sin(377t+53.13^\circ)$; 31.83 mH | [[T3-Q3 - RL Series Circuit Impedance]] |
| 4 | RC series voltage drops from the angle | $104.1\angle30^\circ$, $60.1\angle-60^\circ$ V | [[T3-Q4 - RC Series Voltage Drops]] |
| 5 | RC series: current, $S$, $pf$, $C$ | 9.97 A; $596.4-j795.2$ VA; $pf=0.6$ lead; 331.6 µF | [[T3-Q5 - RC Circuit Power and Power Factor]] |
| 6 | adding parallel currents | $39.39\sin(\omega t+15.10^\circ)$ A | [[T3-Q6 - Adding Parallel Branch Currents]] |
| 7 | series RLC voltages | 2.12 A; $V_L,V_C>V$ | [[T3-Q7 - Series RLC Voltage Magnification]] |
| 8 | complex power of that RLC | 180 W, 135 VAr, $pf=0.8$ lag | [[T3-Q8 - Complex Power of a Series RLC]] |
| 9 | nodal analysis (phasors) | $11.77\angle-80.2^\circ$ A | [[T3-Q9 - Nodal Analysis in the Phasor Domain]] |
| 10 | reactance for unity power factor | $Z_{ab}=11.77+j47.06$; $C=53.13\ \mu$F | [[T3-Q10 - Making the Source Current In Phase]] |
| 11 | mesh, nodal, Thevenin | $4.83\angle-75^\circ$ A | [[T3-Q11 - Mesh, Nodal and Thevenin for Two Sources]] |
| 12 | source powers; max power | $Z_3=1\ \Omega$, 46.65 W | [[T3-Q12 - AC Maximum Power Transfer]] |

## Theory notes (in `Theory/`)

| Theory note | Questions |
|---|---|
| [[Sinusoidal Waveforms, RMS and Average Value]] | Q1, Q2 |
| [[Phasors and Complex Algebra]] | Q3, Q6, Q9 |
| [[Impedance and Series-Parallel AC Circuits]] | Q3, Q4, Q5, Q7, Q10 |
| [[AC Power and Power Factor]] | Q5, Q8, Q12 |
| [[Nodal and Mesh Analysis (AC)]] | Q9, Q11 |
| [[Thevenin, Norton and Maximum Power Transfer (AC)]] | Q11, Q12 |
| [[Power Factor Correction]] | Q10 |

## Universal solution workflow

1. **Frequency.** Read $\omega$ off the source, or compute $\omega=2\pi f$.
2. **Impedances.** $Z_R=R,\ Z_L=j\omega L,\ Z_C=-j/(\omega C)$, see [[Impedance and Series-Parallel AC Circuits]].
3. **Source to RMS phasor.** $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta$.
4. **Reduce the circuit.** Series/parallel $Z$, or nodal/mesh ([[Nodal and Mesh Analysis (AC)]]), or Thevenin ([[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin/Norton (AC)]]); pick by circuit shape, exactly as for DC ([[02 Methods of Circuit Analysis|Week 2]], [[03 DC Network Theorems|Week 3]]).
5. **Solve for current/voltage.** $\bar I=\bar V/Z$.
6. **Power.** $\bar S=\bar V\bar I^{*}=P+jQ$, see [[AC Power and Power Factor]].

This is the same six-step reduction that [[06 Sinusoidal Steady-State Analysis|Week 6]]/[[07 AC Circuit Analysis and Network Theorems|Week 7]] cover conceptually; this tutorial applies it to twelve concrete problems.

## The master memory map

If you remember only one thing, remember this chain:

$$
R\to0^\circ,\quad L\to+j\omega L\to+90^\circ,\quad C\to-\frac{j}{\omega C}\to-90^\circ
\ \Rightarrow\
\bar V=\bar I Z
\ \Rightarrow\
Z=R+j(X_L-X_C)
\ \Rightarrow\
\bar S=\bar V\bar I^{*}=P+jQ
\ \Rightarrow\
pf=\cos\phi
$$

$$
\boxed{\text{AC circuits = DC circuit laws + complex numbers}}
$$

That single idea is why every theorem from [[Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] survives into this tutorial unchanged in structure.

## Pattern recognition

| You see | Do |
|---|---|
| a non-sinusoidal periodic wave | integrate $i$ (average) and $i^2$ (rms) over a period (Q1, Q2) |
| "$i(t)=\ldots\sin$, find $v(t)$" | peak phasor, multiply by $Z$, shift the angle (Q3) |
| angle between $V$ and $I$ given, no component values | right-triangle of $V_R$, $V_X$ (Q4) |
| sines and cosines mixed | convert everything to sine, then phasors (Q6) |
| series RLC, "compare element voltages with the source" | magnification, $L$ and $C$ cancel (Q7) |
| "real/reactive power, power factor" | $P=I^2R$, $Q=I^2X$, $pf=P/|S|$, and say lead or lag (Q5, Q8) |
| one unknown node, two sources | Millman/nodal (Q9) |
| "make the current in phase" | cancel the imaginary part of the total $Z$ (Q10) |
| a load fed by a complicated network | Thevenin; conjugate matching for max power (Q11, Q12) |

## Exam-pattern hints
Marks are lost on (i) **peak versus rms**, (ii) **lead versus lag** words, (iii) the **sign of $Q$** for capacitors, and (iv) adding **magnitudes** instead of phasors. Q10 is the representative "design" question: *the unknown reactance must cancel the imaginary part*.

## Sheet answers that differ from a direct calculation
- **Q5:** printed $pf=0.596$; exact $0.600$ (the power factor of $6-j8$).
- **Q7, Q8:** the printed $389.75$ V, $179.79$ W, $449.72$/$584.27$ VAr come from rounding $I$ to $2.12$ A; exact $390.0$ V, $180$ W, $450$/$585$ VAr.
- **Q4:** printed $60.14$ V; exact $60.10$ V.
- **Q12:** the printed $Q_1=26$ VAr, $S_1=60.5$ VA and $Q_2=-13.73$ VAr, $S_2=15.85$ VA are swapped between the sources (correct: source 1 $-13.73$ VAr, $15.85$ VA; source 2 $+26.23$ VAr, $60.55$ VA); "$P_1=P_2=23.32$ W at maximum power" is each source's share of the *load* power, each actually delivers $37.5$ W.
- All other printed answers match.

## Related
- [[Concepts|Concepts glossary]]
- [[05 Sinusoids and Phasors|Week 5]] · [[06 Sinusoidal Steady-State Analysis|Week 6]] · [[07 AC Circuit Analysis and Network Theorems|Week 7]]
- Next: [[AC Transients|AC Transients]] (what happens when a switch closes on an AC-driven circuit), then [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits|Tutorial 4]]
