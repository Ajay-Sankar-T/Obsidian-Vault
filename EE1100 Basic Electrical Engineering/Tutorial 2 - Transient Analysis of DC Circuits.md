---
tags: [EE1100, tutorial, DC-circuits, transients]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
---

# Tutorial 2 — Transient Analysis of DC Circuits

← up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]] · builds on: [[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]]

Covers first-order (single L or C) and second-order (RLC) transient response — switching circuits into a new state and finding how voltage/current evolve afterward.

## Core concepts used

- [[EE1100 Basic Electrical Engineering/Concepts#Capacitors and Inductors|Capacitors and Inductors]] — v-i relations, energy storage, continuity of v_C and i_L
- [[EE1100 Basic Electrical Engineering/Concepts#RC/RL Transients and Time Constant|RC/RL Transients and Time Constant]] — the x(t) = x_∞ + (x_0−x_∞)e^(−t/τ) template, and second-order damping (over/critical/underdamped)
- [[EE1100 Basic Electrical Engineering/Concepts#Network Theorems|Thevenin's theorem]] — used to reduce the resistive network around the storage element down to a single R_th before computing τ

## Related

- [[EE1100 Basic Electrical Engineering/04 Capacitors, Inductors and First Order Circuits|Week 4 — Capacitors, Inductors and First-Order Circuits]]
- [[EE1100 Basic Electrical Engineering/08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]] (the AC steady-state cousin of second-order damping)
- [[EE1100 Basic Electrical Engineering/Concepts|Concepts glossary]]
- What changes when the source is AC instead of DC: [[EE1100 Basic Electrical Engineering/AC Transients/AC Transients|AC Transients]] (bridges directly into [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]])
