---
tags: [EE1100, tutorial-solution, DC-circuits, star-delta, resistor-networks]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q13: Resistance Between A and B by Star–Delta Reduction

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q12 - Mesh Analysis and Power Balance]] · Next: [[T1-Q14 - Bridge Network Three Ways]]

> [!question] Find the resistance between points A and B of the network shown (values in ohms). *[Sheet: $R_{AB}=2.5\ \Omega$]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#10. Star–delta (Y–Δ) transformation|Y–Δ transformation]], series/parallel simplification.

## Given
An outer triangle $A$-$B$-$C$ with $5\ \Omega$ on each side. Inside it, an inner triangle $A'B'C'$ with $R_{A'B'}=1\ \Omega$, $R_{A'C'}=1.5\ \Omega$, $R_{B'C'}=2.5\ \Omega$, joined to the corners by $R_{AA'}=4.75\ \Omega$, $R_{BB'}=4.5\ \Omega$, $R_{CC'}=3.25\ \Omega$.

## Principle and why it applies
There is no pair of resistors in series or parallel to start with, so the network has to be simplified with **Y–Δ transformations**, which replace a three-terminal resistor network by an equivalent one (same resistance between every pair of terminals) and so create new series/parallel pairs. Strategy: convert the inner delta to a star so that each leg joins a corner leg in series; then the inner part becomes a three-terminal star in parallel with the outer delta between the same three terminals $A,B,C$; convert it to a delta and combine in parallel.

## Diagram
![[T1-Q13-circuit.png]]

## Solution
**Step 1: inner delta → star.** With $R_{A'B'}=1$, $R_{A'C'}=1.5$, $R_{B'C'}=2.5$ (sum $5\ \Omega$), each star leg is the product of the two adjacent delta arms over the sum:
$$R_{A'}=\frac{1\times1.5}{5}=0.3,\qquad R_{B'}=\frac{1\times2.5}{5}=0.5,\qquad R_{C'}=\frac{1.5\times2.5}{5}=0.75\ \ (\Omega).$$
**Step 2: add the corner legs in series.** $\ R_A=4.75+0.3=5.05,\ \ R_B=4.5+0.5=5,\ \ R_C=3.25+0.75=4\ \Omega$. This is a star between $A,B,C$.

**Step 3: star → delta** (sum of products over the opposite leg): $\ \Sigma=5.05\cdot5+5\cdot4+4\cdot5.05=65.45$,
$$R_{AB}^{Y}=\frac{65.45}{4}=16.36,\qquad R_{AC}^{Y}=\frac{65.45}{5}=13.09,\qquad R_{BC}^{Y}=\frac{65.45}{5.05}=12.96\ \ (\Omega).$$
**Step 4: parallel with the outer triangle** ($5\ \Omega$ each side):
$$R_{AB}'=16.36\parallel5=3.83,\qquad R_{AC}'=13.09\parallel5=3.62,\qquad R_{BC}'=12.96\parallel5=3.61\ \ (\Omega).$$
**Step 5: terminals A and B.** The direct arm $R_{AB}'$ is in parallel with the path through $C$:
$$R_{AB}=3.83\parallel(3.62+3.61)=3.83\parallel7.23=2.50\ \Omega.$$

## Result
$$\boxed{R_{AB}\approx2.50\ \Omega}$$
(exactly $2.503\ \Omega$; the sheet quotes $2.5\ \Omega$.)

## Check
`Tools/ee_t1_t4_t8.py` solves the nine-resistor network by nodal analysis, injecting 1 A at A and removing it at B: $V_A-V_B=2.5031\ \Omega$ ✓. Plausibility: $R_{AB}$ is smaller than the direct $5\ \Omega$ arm alone ✓.

## Trap / alternative
The usual mistake is applying the *sum over the adjacent* formula (instead of "product of adjacent over the sum") when going Δ→Y. A nodal solution (five unknowns) works but is far longer by hand. Also, **only convert one three-terminal block at a time**; the final step compares two networks in parallel between the *same* three terminals.

## Concepts used
- Star–delta transformation, series/parallel reduction ([[Theory - Circuit Laws and Network Theorems]], [[Series-Parallel Resistance Reduction]])
