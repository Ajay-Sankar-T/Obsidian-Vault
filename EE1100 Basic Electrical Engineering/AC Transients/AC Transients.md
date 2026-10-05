---
tags: [EE1100, AC-circuits, transients]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
---

# AC Transients

← up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]] · bridges: [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2 (DC transients)]] and [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3 (AC steady state)]]

The EE1100 syllabus lists DC transients (RL, RC, RLC, parallel RLC — [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]]) and single-phase AC/phasors/impedance/resonance ([[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]]) as separate units, without a dedicated "AC transient" topic. This folder is the natural bridge: what happens when a switch operates on a circuit that has an **AC source**, combining the time-constant/damping machinery of Tutorial 2 with the phasor/impedance machinery of Tutorial 3.

## The big idea

$$\boxed{\text{Complete response} = \text{Transient response} + \text{Steady-state response}}$$

or

$$x(t)=x_{\rm forced}(t)+x_{\rm natural}(t)$$

For a DC source (Tutorial 2), $x_{\rm forced}$ is a constant. For an AC source, $x_{\rm forced}$ is itself a sinusoid — the phasor-domain steady-state solution:

$$x(t)=x_{ss,AC}(t)+x_{\rm transient}(t)$$

As $t\to\infty$, the transient decays to zero and $x(t)\to x_{ss,AC}(t)$ — the pure AC steady-state answer that [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]]'s phasor methods compute directly.

## Why phasors alone are not enough

Phasor analysis ([[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra|Phasors and Complex Algebra]]) gives **only** the steady-state part $x_{ss,AC}(t)$. It says nothing about what happens in the first few time constants after a switch operates — that information lives entirely in the natural (transient) term, found the same way as in [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]]: set independent sources to zero and analyze the resulting RC/RL/RLC decay.

## Two sub-topics

- [[EE1100 Basic Electrical Engineering/AC Transients/First-Order AC Transients (RC and RL)|First-Order AC Transients (RC and RL)]] — single storage element, exponential transient added to a sinusoidal steady state.
- [[EE1100 Basic Electrical Engineering/AC Transients/Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients (Series and Parallel RLC)]] — both $L$ and $C$ present, transient is itself a decaying sinusoid at a **different** frequency from the source.

## Universal workflow

1. **Initial conditions.** Find $v_C(0^-)$, $i_L(0^-)$ from the pre-switch circuit (steady state — DC or AC as applicable), then apply continuity: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$.
2. **AC steady-state solution.** Solve the post-switch circuit by phasors exactly as in [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]] — $Z_R=R,\ Z_L=j\omega L,\ Z_C=1/(j\omega C)$ — to get $x_{ss}(t)$.
3. **Natural response.** Deactivate independent sources (as in [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin reduction]]) and find $\tau$ (first order) or $\alpha,\omega_n,\omega_d$ (second order) exactly as in [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]].
4. **Complete response.** Add the forms — see the two sub-notes for the exact templates.
5. **Apply initial conditions** from step 1 to solve for the unknown constants.
6. **Sanity check:** the exponential/decaying part must vanish as $t\to\infty$, leaving exactly the steady-state sinusoid from step 2.

## Two switching rules that never change

$$\boxed{v_C(0^+)=v_C(0^-)}\qquad\qquad \boxed{i_L(0^+)=i_L(0^-)}$$

**C → voltage stays, L → current stays.** These continuity rules hold regardless of whether the source is DC or AC — they follow purely from $i_C=C\,dv_C/dt$ and $v_L=L\,di_L/dt$ being finite (an instantaneous jump would need infinite current/voltage). By contrast, $i_C$ and $v_L$ themselves **can** jump discontinuously at switching.

## A trap worth flagging explicitly

At $t\to\infty$ you **cannot** use the DC shortcuts "capacitor → open, inductor → short" for an AC-driven circuit — those apply only to true DC steady state. For AC steady state you must use the actual impedances $Z_L=j\omega L$, $Z_C=1/(j\omega C)$, exactly as [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]] defines them.

## Related
- [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2 — Transient Analysis of DC Circuits]]
- [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3 — AC Circuit Analysis]]
- [[EE1100 Basic Electrical Engineering/08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]] (the RLC natural frequency $\omega_n=1/\sqrt{LC}$ reappears here as the transient's own oscillation frequency)
