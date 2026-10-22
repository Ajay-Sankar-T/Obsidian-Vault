---
tags:
  - EE1100
  - week9
  - AC-circuits
  - three-phase
up: "[[EE1100 MOC]]"
prev: "[[08 Resonance and Magnetically Coupled Circuits]]"
next: "[[10 Single Phase Transformers]]"
---

# Week 9 — Three Phase Circuits and Power Measurement

← prev: [[08 Resonance and Magnetically Coupled Circuits|Week 8]] · up: [[EE1100 MOC|MOC]] · next: [[10 Single Phase Transformers|Week 10 →]]

Playlist: lectures covering three-phase systems in [Fundamentals of Electrical Engineering](https://www.youtube.com/playlist?list=PLbRMhDVUMngfdEXVcdf_ijj2Eub-UHs_y).

## Overview
Definitions of star/delta connection and the line-vs-phase relations are in [[Concepts#Three-Phase Systems|Three-Phase Systems]]. Practically, three-phase analysis is just single-phase [[06 Sinusoidal Steady-State Analysis|phasor analysis]] applied per phase, exploiting symmetry.

## Why three phases at all
Three sources 120° apart, feeding a balanced load, deliver **constant instantaneous power** (the three individual pulsating powers sum to a constant), unlike single-phase power which pulsates at 2× the supply frequency. This is the core reason power grids and industrial machines are three-phase.

## Solving a balanced three-phase problem
1. Identify the connection (star or delta) of *both* source and load.
2. Convert everything to an equivalent single "per-phase" star circuit (a delta load can be converted to an equivalent star via Z_star = Z_delta/3 for balanced loads).
3. Solve one phase using ordinary single-phase phasor analysis (with the neutral as reference, even if it's not physically present).
4. Use the ±120° symmetry to write down the other two phases without recomputation.
5. Convert back to line quantities using V_L = √3 V_ph (star) or I_L = √3 I_ph (delta) as needed.

```mermaid
flowchart LR
    A["Balanced 3-phase source + load\n(star or delta)"] --> B["Convert delta load → star\n(Z_Y = Z_Δ / 3)"] --> C["Solve ONE phase\n(single-phase phasor analysis)"] --> D["Other two phases:\nsame magnitude, ±120° shifted"] --> E["Convert back to\nline quantities if needed"]
```

## Power measurement — two-wattmeter method
Two wattmeters, connected with their current coils in two of the three lines and voltage coils referenced to the third line, together read the **total** three-phase power regardless of load balance or power factor: P_total = W1 + W2. Bonus: the *individual* readings reveal the power factor angle via tan φ = √3(W1−W2)/(W1+W2) — notably, at pf = 0.5 (φ=60°) one wattmeter reads exactly zero, and below pf = 0.5 one reading goes *negative* (must be reversed to read, then subtracted).

## Related
- [[Concepts|Concepts glossary]]
- [[06 Sinusoidal Steady-State Analysis|Week 6 — AC Power]]
- [[11 Three Phase Induction Machines|Week 11 — Three Phase Induction Machines]]
