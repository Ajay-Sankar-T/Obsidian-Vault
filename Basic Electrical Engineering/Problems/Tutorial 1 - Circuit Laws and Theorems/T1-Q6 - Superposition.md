---
tags: [EE1100, tutorial-solution, DC-circuits, superposition]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q6: Superposition

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q5 - Maximum Power with a Dependent Source]] · Next: [[T1-Q7 - Mesh Analysis with Current Sources]]

> [!question] Use superposition to find $V_x$ (the voltage across the $20\ \Omega$ resistor, positive on the left) in a circuit with a 24 V source, a 2 A current source and a 48 V source. *[Sheet: $V_x=10.4$ V; exact value 10.33 V, see below]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#7. Superposition|superposition]], turning sources off correctly, dividers.

## Given
$24$ V source → $10\ \Omega$ → node 1 (with the $2$ A source pushing up into it) → $20\ \Omega$ ($V_x$, $+$ on the left) → node 2 (with a $30\ \Omega$ to ground) → $45\ \Omega$ → $48$ V source ($+$ at top).

## Principle and why it applies
The circuit is linear, so $V_x=V_x^{(24)}+V_x^{(2A)}+V_x^{(48)}$ where each term is computed with the other two sources turned off: a switched-off **voltage** source becomes a **short**, a switched-off **current** source becomes an **open**. Three simpler circuits replace one three-source circuit.

## Diagram
![[T1-Q6-circuit.png]]

## Solution
**(i) 24 V alone** (2 A opened, 48 V shorted). One series loop: $10+20+(30\parallel45=18)=48\ \Omega$, so $I=24/48=0.5$ A through the $20\ \Omega$, from left to right:
$$V_x^{(24)}=+0.5\times20=+10\ \text{V}.$$

**(ii) 48 V alone** (24 V shorted, 2 A opened). Node 2 sees $30\ \Omega$ to ground and $(20+10)=30\ \Omega$ to ground through the left branch, i.e. $30\parallel30=15\ \Omega$; by the voltage divider $V_2=48\cdot\dfrac{15}{45+15}=12$ V. The current through the $20\ \Omega$ flows from node 2 towards node 1, $12/30=0.4$ A, which is *against* the reference direction of $V_x$:
$$V_x^{(48)}=-0.4\times20=-8\ \text{V}.$$

**(iii) 2 A alone** (both voltage sources shorted). Node 1 sees $10\ \Omega$ to ground in parallel with $20+(30\parallel45=18)=38\ \Omega$: $R=10\parallel38=7.917\ \Omega$, so $V_1=2\times7.917=15.83$ V. Current through the $20\ \Omega$: $15.83/38=0.4167$ A left to right:
$$V_x^{(2A)}=+0.4167\times20=+8.33\ \text{V}.$$

**Sum:**
$$V_x=10-8+8.33=10.33\ \text{V}.$$

## Result
$$\boxed{V_x\approx10.33\ \text{V}}\quad(\text{sheet: }10.4\ \text{V})$$

## Check
Direct nodal analysis (two unknowns): at node 1 $\dfrac{V_1-24}{10}+\dfrac{V_1-V_2}{20}=2$, at node 2 $\dfrac{V_2-V_1}{20}+\dfrac{V_2}{30}+\dfrac{V_2-48}{45}=0$ gives $V_1=38.83$ V, $V_2=28.50$ V, so $V_x=V_1-V_2=10.333$ V (`Tools/ee_t1_t4_t8.py`). The sheet's 10.4 V is within 0.7 % and looks like a rounded intermediate; the exact value is $10\tfrac13$ V.

## Trap / alternative
- Keep the polarity bookkeeping: contribution (ii) is **negative** because the 48 V source drives current through the $20\ \Omega$ in the opposite direction.
- Never add **powers** from the three sub-circuits; only voltages and currents superpose.
- Nodal analysis is quicker here (two equations); superposition shows *who contributes what*.

## Concepts used
- Superposition, voltage divider, series/parallel reduction ([[Theory - Circuit Laws and Network Theorems]], [[Voltage Divider Rule]])
