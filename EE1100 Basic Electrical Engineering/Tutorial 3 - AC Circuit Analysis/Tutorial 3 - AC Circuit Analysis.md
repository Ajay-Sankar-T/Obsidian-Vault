---
tags: [EE1100, tutorial, AC-circuits, phasors]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
---

# Tutorial 3 — AC Circuit Analysis

← up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]] · builds on: [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] · followed by: [[EE1100 Basic Electrical Engineering/AC Transients/AC Transients|AC Transients]]

Twelve questions (Q1–Q12) covering the full arc of single-phase AC analysis: from a raw sinusoidal waveform down to complex power and network theorems. The whole tutorial is one repeated reduction chain:

$$
\boxed{\text{Time-domain signal} \rightarrow \text{RMS} \rightarrow \text{Phasor} \rightarrow \text{Impedance} \rightarrow \text{Circuit analysis} \rightarrow \text{Power}}
$$

For $v(t)=V_m\sin(\omega t+\theta_v)$, the RMS phasor is $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta_v$, and every subsequent step uses the AC form of Ohm's law $\bar V=\bar I Z$ — see [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra|Phasors and Complex Algebra]].

## Concept map (Q1–Q12)

| Q | Main concept | Note |
|---|---|---|
| Q1 | Average & RMS of a waveform | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Sinusoidal Waveforms, RMS and Average Value\|Sinusoidal Waveforms, RMS and Average Value]] |
| Q2 | RMS of a stepped/piecewise waveform | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Sinusoidal Waveforms, RMS and Average Value\|Sinusoidal Waveforms, RMS and Average Value]] |
| Q3 | RL series circuit, current lag | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q4 | RC phasor voltage diagram | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q5 | RC impedance and power | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/AC Power and Power Factor\|AC Power and Power Factor]] |
| Q6 | Adding parallel branch currents | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra\|Phasors and Complex Algebra]] |
| Q7 | Series RLC, voltage magnification | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q8 | Complex power $S=P+jQ$ | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/AC Power and Power Factor\|AC Power and Power Factor]] |
| Q9 | Nodal analysis in the phasor domain | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Nodal and Mesh Analysis (AC)\|Nodal and Mesh Analysis (AC)]] |
| Q10 | Power factor correction | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Power Factor Correction\|Power Factor Correction]] |
| Q11 | Mesh analysis, shared-branch current | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Nodal and Mesh Analysis (AC)\|Nodal and Mesh Analysis (AC)]] |
| Q12 | AC maximum power transfer | [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Thevenin, Norton and Maximum Power Transfer (AC)\|Thevenin, Norton and Maximum Power Transfer (AC)]] |

## Universal solution workflow

1. **Frequency.** Read $\omega$ off the source, or compute $\omega=2\pi f$.
2. **Impedances.** $Z_R=R,\ Z_L=j\omega L,\ Z_C=-j/(\omega C)$ — see [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]].
3. **Source to RMS phasor.** $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta$.
4. **Reduce the circuit.** Series/parallel Z, or nodal/mesh ([[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Nodal and Mesh Analysis (AC)|Nodal and Mesh Analysis (AC)]]), or Thevenin ([[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin/Norton (AC)]]) — pick by circuit shape, exactly as for DC ([[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis|Week 2]], [[EE1100 Basic Electrical Engineering/03 DC Network Theorems|Week 3]]).
5. **Solve for current/voltage.** $\bar I=\bar V/Z$.
6. **Power.** $\bar S=\bar V\bar I^{*}=P+jQ$ — [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/AC Power and Power Factor|AC Power and Power Factor]].

This is the same six-step reduction as [[EE1100 Basic Electrical Engineering/06 Sinusoidal Steady-State Analysis|Week 6]]/[[EE1100 Basic Electrical Engineering/07 AC Circuit Analysis and Network Theorems|Week 7]] cover conceptually — this tutorial is where it gets applied to twelve concrete problems.

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

That single idea is why every theorem from [[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] survives into this tutorial unchanged in structure.

## Related
- [[EE1100 Basic Electrical Engineering/Concepts|Concepts glossary]]
- [[EE1100 Basic Electrical Engineering/05 Sinusoids and Phasors|Week 5]] · [[EE1100 Basic Electrical Engineering/06 Sinusoidal Steady-State Analysis|Week 6]] · [[EE1100 Basic Electrical Engineering/07 AC Circuit Analysis and Network Theorems|Week 7]]
- Next: [[EE1100 Basic Electrical Engineering/AC Transients/AC Transients|AC Transients]] — what happens when a switch closes on an AC-driven circuit
