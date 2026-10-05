---
tags: [EE1100, week2, DC-circuits]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
prev: "[[EE1100 Basic Electrical Engineering/01 Basic Concepts and Basic Laws]]"
next: "[[EE1100 Basic Electrical Engineering/03 DC Network Theorems]]"
---

# Week 2 — Methods of Circuit Analysis

← prev: [[EE1100 Basic Electrical Engineering/01 Basic Concepts and Basic Laws|Week 1]] · up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]] · next: [[EE1100 Basic Electrical Engineering/03 DC Network Theorems|Week 3 →]]

Playlist: lectures 11–18 of [Fundamentals of Electrical Engineering](https://www.youtube.com/playlist?list=PLbRMhDVUMngfdEXVcdf_ijj2Eub-UHs_y).

## Overview
[[EE1100 Basic Electrical Engineering/01 Basic Concepts and Basic Laws|Week 1]]'s [[EE1100 Basic Electrical Engineering/Concepts#Kirchhoff's Laws|KCL/KVL]] work on *any* circuit, but applying them element-by-element gets unmanageable fast. This week turns them into two systematic algorithms — see [[EE1100 Basic Electrical Engineering/Concepts#Nodal and Mesh Analysis|Nodal and Mesh Analysis]] for the core explanation and diagram.

## Nodal analysis, step by step
1. Pick a reference (ground) node — usually the one with the most connections.
2. Label every other node's voltage as an unknown.
3. At each unknown node, write KCL: sum of currents leaving = 0, expressing each branch current via Ohm's law as (V_node − V_neighbor)/R.
4. If a voltage source connects two non-reference nodes, don't write separate KCL for each — merge them into a **supernode**: write one combined KCL equation for the pair, plus a constraint equation V_a − V_b = source value.
5. Solve the resulting linear system.

## Mesh analysis, step by step
1. Confirm the circuit is planar; identify independent meshes (the "window panes").
2. Assign a clockwise mesh current to each.
3. Write KVL around each mesh, expressing resistor drops via Ohm's law in terms of the mesh currents (a shared resistor's drop involves the *difference* of the two adjacent mesh currents).
4. If a current source lies on the shared boundary of two meshes, form a **supermesh**: skip individual KVL for those two meshes, write one KVL around their combined outer loop, plus a constraint equation from the current source value.
5. Solve.

## Choosing between them
Nodal is usually less work when the circuit has few nodes but many branches (lots of parallel paths); mesh is usually less work when it has few independent loops. Current sources are "free" in nodal analysis (they just add a constant to KCL) but force a supermesh in mesh analysis, and vice versa for voltage sources — factor that in when picking a method.

## Worked in
[[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]]: Q7 (basic mesh currents), Q11 (nodal with two supernodes), Q12 (mesh with a supermesh, then verified via power balance), Q14 (same circuit solved three ways — star-delta, mesh, *and* nodal — to build confidence they agree).

## Related
- [[EE1100 Basic Electrical Engineering/Concepts|Concepts glossary]]
- [[EE1100 Basic Electrical Engineering/03 DC Network Theorems|Week 3 — DC Network Theorems]]
- [[EE1100 Basic Electrical Engineering/07 AC Circuit Analysis and Network Theorems|Week 7 — AC Circuit Analysis]] (identical procedure, phasor arithmetic)
