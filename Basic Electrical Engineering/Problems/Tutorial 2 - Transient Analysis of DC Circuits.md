---
tags:
  - EE1100
  - tutorial
  - DC-circuits
  - transients
up: "[[EE1100 MOC]]"
---

# Tutorial 2 — Transient Analysis of DC Circuits

← up: [[EE1100 MOC|MOC]] · builds on: [[Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]]

Covers first-order (single L or C) and second-order (RLC) transient response — switching circuits into a new state and finding how voltage/current evolve afterward.

## Core concepts used

- [[Concepts#Capacitors and Inductors|Capacitors and Inductors]] — v-i relations, energy storage, continuity of v_C and i_L
- [[Concepts#RC/RL Transients and Time Constant|RC/RL Transients and Time Constant]] — the x(t) = x_∞ + (x_0−x_∞)e^(−t/τ) template, and second-order damping (over/critical/underdamped)
- [[Concepts#Network Theorems|Thevenin's theorem]] — used to reduce the resistive network around the storage element down to a single R_th before computing τ

## Related

- [[04 Capacitors, Inductors and First Order Circuits|Week 4 — Capacitors, Inductors and First-Order Circuits]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]] (the AC steady-state cousin of second-order damping)
- [[Concepts|Concepts glossary]]
- What changes when the source is AC instead of DC: [[AC Transients|AC Transients]] (bridges directly into [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]])
