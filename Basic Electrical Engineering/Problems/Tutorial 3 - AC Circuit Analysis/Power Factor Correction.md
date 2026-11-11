---
tags:
  - EE1100
  - AC-circuits
  - power-factor-correction
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# Power Factor Correction

← up: [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[AC Power and Power Factor|AC Power and Power Factor]], [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]

## The goal (Q10 pattern)

Find a reactance to add to a circuit so that the **source current ends up in phase with the source voltage** — i.e. drive the net power factor to unity.

## Derivation

From $\bar I=\bar V/Z$, $I$ and $V$ are in phase exactly when $\angle Z=0°$, i.e. when

$$\operatorname{Im}(Z)=0$$

So whatever reactance $X$ the existing circuit presents, an equal-and-opposite reactance $-X$ must be added in series to cancel it (or, in parallel form, an admittance chosen to cancel $\operatorname{Im}(Y)$):

- **Inductive circuit** ($Z=R+jX$, $X>0$): needs a **capacitor** in series (or parallel, depending on configuration) to contribute $-jX$.
- **Capacitive circuit** ($X<0$): needs an **inductor** to contribute $+j|X|$.

In practice almost all correction is capacitive, because almost all real inductive loads (motors, transformers, fluorescent ballasts) present a lagging power factor that needs cancelling — this is *why* power factor correction is essentially synonymous with "add a capacitor bank" in industrial practice.

## Sizing the capacitor

If the required capacitive reactance is $X_C$:

$$X_C=\frac1{\omega C}\qquad\Longrightarrow\qquad C=\frac1{\omega X_C}$$

**Worked example (Q10):** existing inductive reactance is cancelled by adding $X=-j47.05\ \Omega$, giving $C=53.13\ \mu\text{F}$ at the circuit's operating frequency, and unity power factor at the source.

## Why this matters (beyond the algebra)

Reactive power $Q$ doesn't do useful work but still draws current through the supply, transformers, and wiring (see [[AC Power and Power Factor|AC Power and Power Factor]] — $|S|=\sqrt{P^2+Q^2}$ always $\ge P$). Utilities size and rate equipment by **apparent power** $|S|$, not real power $P$, so a poor power factor forces oversized (and more expensive) generation, transmission, and switchgear for the same useful $P$ delivered — the economic reason correction capacitors are installed at industrial sites with large motor loads.

## Relation to conjugate matching

Power-factor correction and [[Thevenin, Norton and Maximum Power Transfer (AC)|AC maximum power transfer]] both use "add a reactance to cancel another reactance," but for opposite purposes: correction cancels the **load's own** reactance to make the source see a purely resistive (efficient) circuit; conjugate matching chooses the **load's** reactance to cancel the **source's** internal reactance, maximizing power delivered to that load (often at the cost of efficiency, since half the power is dissipated in $R_{\rm Th}$ itself) — don't confuse the two design goals.

## Related
- [[AC Power and Power Factor|AC Power and Power Factor]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]] (unity power factor at resonance is the same $\operatorname{Im}(Z)=0$ condition, arising from frequency choice instead of added components)
