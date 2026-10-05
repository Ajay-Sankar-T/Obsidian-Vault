---
tags: [EE1100, week1, DC-circuits]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
next: "[[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis]]"
---

# Week 1 — Basic Concepts and Basic Laws

← up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]] · next: [[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis|Week 2 →]]

Playlist: lectures 1–10 of [Fundamentals of Electrical Engineering](https://www.youtube.com/playlist?list=PLbRMhDVUMngfdEXVcdf_ijj2Eub-UHs_y).

## Overview
The vocabulary and two conservation laws that every later technique in this course is built from. Nothing here is optional — [[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis|nodal/mesh analysis]], [[EE1100 Basic Electrical Engineering/03 DC Network Theorems|network theorems]], and even the AC phasor methods in [[EE1100 Basic Electrical Engineering/07 AC Circuit Analysis and Network Theorems|Week 7]] are just this week's laws applied more cleverly.

## Charge, current, voltage, power, energy

- **Current** i = dq/dt: rate of charge flow (amps). Conventional current flows from + to − *outside* a source, and from − to + *inside* it.
- **Voltage** v: energy per unit charge between two points (volts) — always defined *across* two nodes, never "at" a single point without a reference.
- **Power** p = vi (watts): rate of energy transfer. **Passive sign convention**: if current enters an element's + terminal, positive p means the element *absorbs* power; negative p means it *delivers* power (i.e., it's acting as a source).
- **Energy** w = ∫p dt (joules).

## Circuit elements

- **Independent sources:** ideal voltage source (fixed V regardless of current drawn) or ideal current source (fixed I regardless of voltage across it) — their value doesn't depend on anything else in the circuit.
- **Dependent (controlled) sources:** value is proportional to some *other* voltage or current elsewhere in the circuit (e.g. the `K·I` current source in [[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] Q4, or the `10i1` voltage source in Q5). These still count as "linear" for [[EE1100 Basic Electrical Engineering/Concepts#Network Theorems|network theorems]] purposes, but they can never be "killed" the way independent sources are during superposition — they stay active.
- **Resistors:** obey [[EE1100 Basic Electrical Engineering/Concepts#Ohm's Law|Ohm's Law]].

## Nodes, branches, loops

- **Node:** a point where two or more elements connect.
- **Branch:** a single element (or a group in series) between two nodes.
- **Loop:** any closed path through the circuit that doesn't repeat a node.

## Kirchhoff's Current and Voltage Laws

See [[EE1100 Basic Electrical Engineering/Concepts#Kirchhoff's Laws|Kirchhoff's Laws]] for the full statement and diagram. In short: KCL balances current at a node, KVL balances voltage around a loop — together they're always enough to solve any resistive circuit, just tediously if done element-by-element (which is exactly the motivation for [[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis|Week 2]]'s systematic methods).

## Series/parallel combinations and divider rules

- Series/parallel resistor reduction: see [[Series-Parallel Resistance Reduction]].
- **Voltage divider:** see [[EE1100 Basic Electrical Engineering/Voltage Divider Rule|Voltage Divider Rule]] — built while solving the R-2R ladder in [[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] Q1.
- **Current divider** (the dual): for two resistors in parallel, the current through R1 is I_total × R2/(R1+R2) — note it's the *other* resistor on top, the opposite of the voltage divider's own-resistor-on-top form.

## Worked in
[[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] Q1–Q5 use these laws directly (R-2R ladder, KVL loop currents, power absorbed with dependent sources).

## Related
- [[EE1100 Basic Electrical Engineering/Concepts|Concepts glossary]]
- [[EE1100 Basic Electrical Engineering/02 Methods of Circuit Analysis|Week 2 — Methods of Circuit Analysis]]
