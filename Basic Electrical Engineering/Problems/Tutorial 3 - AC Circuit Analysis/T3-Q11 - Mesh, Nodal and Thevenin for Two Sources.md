---
tags: [EE1100, tutorial-solution, AC-circuits, mesh-analysis, nodal-analysis, thevenin]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q11: A Two-Source AC Circuit, Solved by Mesh, Nodal and Thevenin

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Nodal and Mesh Analysis (AC)]], [[Thevenin, Norton and Maximum Power Transfer (AC)]] · Previous: [[T3-Q10 - Making the Source Current In Phase]] · Next: [[T3-Q12 - AC Maximum Power Transfer]]

> [!question] For the circuit of Fig. 5 ($\bar V_1=10\angle0^\circ$, $\bar V_2=10\angle-60^\circ$ V, $Z_1=1+j1$, $Z_2=1-j1$, $Z_3=1+j2\ \Omega$): (a) find the mesh currents $\bar I_1,\bar I_2$ and the current through $Z_3$ by the mesh method; (b) repeat by the nodal method; (c) find the current through $Z_3$ using Thevenin's equivalent. *[Sheet: $\bar I_1=1.58\angle60^\circ$, $\bar I_2=6.05\angle94.3^\circ$, $\bar I_{Z_3}=4.82\angle-75^\circ$ A]*

**Tests:** three methods on one circuit: [[Nodal and Mesh Analysis (AC)|mesh, nodal]], [[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin]]; they must agree.

## Given
Left mesh: $\bar V_1$, $Z_1=R_1+jX_1=1+j1$, shared $Z_3=R_3+jX_3=1+j2$. Right mesh: $Z_2=R_2-jX_2=1-j1$, $\bar V_2$ ($+$ at top), shared $Z_3$. Both mesh currents are drawn **clockwise**.

## Principle and why it applies
The circuit has two meshes and two nodes (a, b) so it is a fair test of choosing a method; all three give identical $\bar I_{Z_3}$ because they solve the same linear system. The phasor methods are the DC methods with $R\to Z$ ([[Theory - Circuit Laws and Network Theorems]]).

## Diagram
![[T3-Q11-circuit.png]]

## Solution
**(a) Mesh.** Both currents clockwise: the shared $Z_3$ carries $\bar I_1-\bar I_2$ downward; $\bar V_2$ is traversed from its $+$ terminal to $-$, a voltage *drop*:
$$(Z_1+Z_3)\bar I_1-Z_3\bar I_2=\bar V_1:\qquad(2+j3)\bar I_1-(1+j2)\bar I_2=10,$$
$$-Z_3\bar I_1+(Z_2+Z_3)\bar I_2=-\bar V_2:\qquad-(1+j2)\bar I_1+(2+j1)\bar I_2=-5+j8.66.$$
Determinant $\Delta=(2+j3)(2+j1)-(1+j2)^2=(1+j8)-(-3+j4)=4+j4=5.657\angle45^\circ$. Cramer's rule:
$$\bar I_1=\frac{10(2+j1)+(1+j2)(-5+j8.66)}{\Delta}=\frac{-2.32+j8.66}{4+j4}=\mathbf{1.585\angle60^\circ\ A},$$
$$\bar I_2=\frac{(2+j3)(-5+j8.66)+10(1+j2)}{\Delta}=\frac{-25.98+j22.32}{4+j4}=\mathbf{6.055\angle94.3^\circ\ A}.$$
Current through $Z_3$ (top to bottom):
$$\bar I_{Z_3}=\bar I_1-\bar I_2=\mathbf{4.83\angle-75^\circ\ A}.$$

**(b) Nodal** (unknown $\bar V_a$, $b$ = reference). $Y_1=0.5-j0.5$, $Y_2=0.5+j0.5$, $Y_3=\dfrac1{1+j2}=0.2-j0.4$ S:
$$\bar V_a=\frac{\bar V_1Y_1+\bar V_2Y_2}{Y_1+Y_2+Y_3}=\frac{(5-j5)+(6.83-j1.83)}{1.2-j0.4}=\frac{11.83-j6.83}{1.2-j0.4}=10.80\angle-11.6^\circ\ \text{V},$$
$$\bar I_{Z_3}=\frac{\bar V_a}{Z_3}=\frac{10.80\angle-11.6^\circ}{2.236\angle63.4^\circ}=\mathbf{4.83\angle-75^\circ\ A}\ \ \checkmark.$$

**(c) Thevenin** (remove $Z_3$; looking into $a$-$b$):
$$Z_{th}=Z_1\parallel Z_2=\frac{(1+j1)(1-j1)}{2}=1\ \Omega,\qquad \bar V_{th}=\frac{\bar V_1Z_2+\bar V_2Z_1}{Z_1+Z_2}=13.66\angle-30^\circ\ \text{V}$$
(explicitly: $\bar V_1Z_2=10-j10$, $\bar V_2Z_1=(5-j8.66)(1+j)=13.66-j3.66$; the sum is $23.66-j13.66$ and half of it is $11.83-j6.83=13.66\angle-30^\circ$). Then
$$\bar I_{Z_3}=\frac{\bar V_{th}}{Z_{th}+Z_3}=\frac{13.66\angle-30^\circ}{2+j2}=\frac{13.66\angle-30^\circ}{2.828\angle45^\circ}=\mathbf{4.83\angle-75^\circ\ A}\ \ \checkmark.$$

## Result
$$\boxed{\bar I_1=1.58\angle60^\circ,\ \bar I_2=6.05\angle94.3^\circ,\ \bar I_{Z_3}=4.83\angle-75^\circ\ \text{A (by all three methods)}}$$
(the sheet prints $4.82$; the exact magnitude is $4.830$.)

## Check
Three independent routes give the same $4.83\angle-75^\circ$ A, which is itself the check. Dimensionally, at node $a$: the current $\bar I_1$ arrives from the left, $\bar I_2$ is the (clockwise) current of the right mesh arriving at $a$ from $Z_3$'s side, and the difference $\bar I_1-\bar I_2$ flows down through $Z_3$ ✓.

## Trap / alternative
- The mesh equation for mesh 2 has $-\bar V_2$ on the right because the source is traversed against its polarity; mis-signing it changes the answer completely.
- $\bar I_{Z_3}=\bar I_1-\bar I_2$, **not** $\bar I_1+\bar I_2$ (both clockwise meshes pass through $Z_3$ in opposite directions).
- For a circuit with a load that changes, the Thevenin route (one $Z_{th}$, $\bar V_{th}$, then divide) is the fastest; it also sets up [[T3-Q12 - AC Maximum Power Transfer]].

## Concepts used
- AC mesh, nodal and Thevenin analysis ([[Nodal and Mesh Analysis (AC)]], [[Thevenin, Norton and Maximum Power Transfer (AC)]])
