---
tags:
  - EE1100
  - AC-circuits
  - nodal-analysis
  - mesh-analysis
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# Nodal and Mesh Analysis (AC)

← up: [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[02 Methods of Circuit Analysis|Week 2]], [[07 AC Circuit Analysis and Network Theorems|Week 7]], [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]

Both methods are structurally identical to their DC versions in [[Concepts#Nodal and Mesh Analysis|Nodal and Mesh Analysis]] — replace $R\to Z$ and $1/R\to Y=1/Z$ throughout, and solve the resulting linear system with complex arithmetic.

## Nodal analysis (Q9 pattern)

**Branch current** between nodes $a$ and $b$ through impedance $Z$:

$$I_{ab}=\frac{V_a-V_b}{Z}=Y(V_a-V_b)$$

**KCL** at every non-reference node: $\sum I_{\rm leaving}=0$ (equivalently, leaving = entering).

### One-node shortcut

If a single unknown node voltage $V$ connects to three known potentials $V_1,V_2,V_3$ through $Z_1,Z_2,Z_3$:

$$\frac{V-V_1}{Z_1}+\frac{V-V_2}{Z_2}+\frac{V-V_3}{Z_3}=0 \quad\Longrightarrow\quad V=\frac{Y_1V_1+Y_2V_2+Y_3V_3}{Y_1+Y_2+Y_3}$$

— a weighted average by admittance, the AC analogue of the DC current-divider-style node formula; extremely fast for single-unknown-node problems.

## Mesh analysis (Q11 pattern)

Write KVL around every independent mesh:

$$\sum ZI=\sum V$$

For two meshes sharing a common impedance $Z_c$:

$$(Z_1+Z_c)I_1-Z_cI_2=V_1,\qquad -Z_cI_1+(Z_2+Z_c)I_2=V_2$$

**Memory:** diagonal = sum of impedances around that mesh; off-diagonal = negative of the shared impedance — exactly the DC mesh-matrix pattern, just with complex entries.

### Current through a shared branch

If mesh currents $I_1,I_2$ both traverse a common element but in opposite assumed directions:

$$I_{\rm branch}=I_1-I_2$$

This is why Q11-style problems require subtracting the two mesh-current solutions to get the physical current through the shared impedance — a step easy to skip if you stop at "solve for $I_1,I_2$" without asking what physical branch current was actually requested.

## Choosing nodal vs mesh

Same rule of thumb as DC ([[02 Methods of Circuit Analysis|Week 2]]): fewer nodes → nodal is faster; fewer meshes → mesh is faster; a circuit with a load fed through a complicated sub-network is often faster via [[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin reduction]] instead of writing out full nodal/mesh equations for the whole thing.

## Related
- [[Reynolds Transport Theorem|Cross-domain: Reynolds Transport Theorem — KCL is the fluid-mechanics "accumulation = inflow − outflow" law applied to a circuit node]]
- [[Concepts#Nodal and Mesh Analysis|Concepts glossary — Nodal and Mesh Analysis (DC)]]
- [[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin, Norton and Maximum Power Transfer (AC)]]
