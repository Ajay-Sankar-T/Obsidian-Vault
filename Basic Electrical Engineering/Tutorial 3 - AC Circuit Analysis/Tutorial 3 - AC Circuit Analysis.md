---
tags:
  - EE1100
  - tutorial
  - AC-circuits
  - phasors
up: "[[EE1100 MOC]]"
---

# Tutorial 3 — AC Circuit Analysis

← up: [[EE1100 MOC|MOC]] · builds on: [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] · followed by: [[AC Transients|AC Transients]]

Twelve questions (Q1–Q12) covering the full arc of single-phase AC analysis: from a raw sinusoidal waveform down to complex power and network theorems. The whole tutorial is one repeated reduction chain:

$$
\boxed{\text{Time-domain signal} \rightarrow \text{RMS} \rightarrow \text{Phasor} \rightarrow \text{Impedance} \rightarrow \text{Circuit analysis} \rightarrow \text{Power}}
$$

For $v(t)=V_m\sin(\omega t+\theta_v)$, the RMS phasor is $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta_v$, and every subsequent step uses the AC form of Ohm's law $\bar V=\bar I Z$ — see [[Phasors and Complex Algebra|Phasors and Complex Algebra]].

## Concept map (Q1–Q12)

| Q | Main concept | Note |
|---|---|---|
| Q1 | Average & RMS of a waveform | [[Sinusoidal Waveforms, RMS and Average Value\|Sinusoidal Waveforms, RMS and Average Value]] |
| Q2 | RMS of a stepped/piecewise waveform | [[Sinusoidal Waveforms, RMS and Average Value\|Sinusoidal Waveforms, RMS and Average Value]] |
| Q3 | RL series circuit, current lag | [[Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q4 | RC phasor voltage diagram | [[Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q5 | RC impedance and power | [[AC Power and Power Factor\|AC Power and Power Factor]] |
| Q6 | Adding parallel branch currents | [[Phasors and Complex Algebra\|Phasors and Complex Algebra]] |
| Q7 | Series RLC, voltage magnification | [[Impedance and Series-Parallel AC Circuits\|Impedance and Series-Parallel AC Circuits]] |
| Q8 | Complex power $S=P+jQ$ | [[AC Power and Power Factor\|AC Power and Power Factor]] |
| Q9 | Nodal analysis in the phasor domain | [[Nodal and Mesh Analysis (AC)\|Nodal and Mesh Analysis (AC)]] |
| Q10 | Power factor correction | [[Power Factor Correction\|Power Factor Correction]] |
| Q11 | Mesh analysis, shared-branch current | [[Nodal and Mesh Analysis (AC)\|Nodal and Mesh Analysis (AC)]] |
| Q12 | AC maximum power transfer | [[Thevenin, Norton and Maximum Power Transfer (AC)\|Thevenin, Norton and Maximum Power Transfer (AC)]] |

## Universal solution workflow

1. **Frequency.** Read $\omega$ off the source, or compute $\omega=2\pi f$.
2. **Impedances.** $Z_R=R,\ Z_L=j\omega L,\ Z_C=-j/(\omega C)$ — see [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]].
3. **Source to RMS phasor.** $\bar V=\dfrac{V_m}{\sqrt2}\angle\theta$.
4. **Reduce the circuit.** Series/parallel Z, or nodal/mesh ([[Nodal and Mesh Analysis (AC)|Nodal and Mesh Analysis (AC)]]), or Thevenin ([[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin/Norton (AC)]]) — pick by circuit shape, exactly as for DC ([[02 Methods of Circuit Analysis|Week 2]], [[03 DC Network Theorems|Week 3]]).
5. **Solve for current/voltage.** $\bar I=\bar V/Z$.
6. **Power.** $\bar S=\bar V\bar I^{*}=P+jQ$ — [[AC Power and Power Factor|AC Power and Power Factor]].

This is the same six-step reduction as [[06 Sinusoidal Steady-State Analysis|Week 6]]/[[07 AC Circuit Analysis and Network Theorems|Week 7]] cover conceptually — this tutorial is where it gets applied to twelve concrete problems.

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

## Related
- [[Concepts|Concepts glossary]]
- [[05 Sinusoids and Phasors|Week 5]] · [[06 Sinusoidal Steady-State Analysis|Week 6]] · [[07 AC Circuit Analysis and Network Theorems|Week 7]]
- Next: [[AC Transients|AC Transients]] — what happens when a switch closes on an AC-driven circuit
