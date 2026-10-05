---
tags: [EE1100, concept, DC-circuits]
---

# Voltage Divider Rule

## The idea
When two resistors R_a and R_b are in series across a source V, and no current is drawn from the middle node (or whatever is downstream from R_b is *represented as R_b itself*, i.e. it's already been reduced to a single equivalent resistor), the voltage across R_b is:

**V_b = V × R_b / (R_a + R_b)**

The voltage splits in proportion to resistance. Bigger resistor gets the bigger share.

**Special case (the one that matters for R-2R ladders):** if R_a = R_b, the node voltage is exactly **half** of the source voltage — no computation needed, just recognize the symmetry.

## Why it works
Same current I flows through both series resistors (that's what "series" means). By Ohm's Law, V_a = I·R_a and V_b = I·R_b. Since I is common, the two voltages are in direct proportion to the two resistances. V = V_a + V_b, so V_b = V·R_b/(R_a+R_b) falls straight out.

## Precondition — you must reduce first
The rule only works cleanly when whatever sits "downstream" of R_b has already been collapsed into a single equivalent resistance. In a ladder network (like an R-2R DAC ladder) this means: before you can say "the voltage halves at this node," you must first confirm the resistance looking into the rest of the network from that node. See [[Series-Parallel Resistance Reduction]] for how that's done stage-by-stage.

## Where this shows up
Used in [[EE1100 Basic Electrical Engineering/Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]], Q1 (R-2R ladder network): because the ladder is self-similar, the resistance looking right from every internal node is always 2R — the same as the shunt resistor at that node — so **every stage is a 50/50 divider**, and the voltage exactly halves node to node: V1 → V2 → V3 → V4.
