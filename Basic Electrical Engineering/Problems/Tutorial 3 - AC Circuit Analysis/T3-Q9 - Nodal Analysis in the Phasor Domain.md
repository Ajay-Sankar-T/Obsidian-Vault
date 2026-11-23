---
tags: [EE1100, tutorial-solution, AC-circuits, nodal-analysis, phasors]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q9: Nodal Analysis in the Phasor Domain

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Nodal and Mesh Analysis (AC)]] · Previous: [[T3-Q8 - Complex Power of a Series RLC]] · Next: [[T3-Q10 - Making the Source Current In Phase]]

> [!question] In the network of Fig. 3 ($\bar V_1=100\angle0^\circ$ V, $\bar V_2=100\angle-60^\circ$ V, $Z_1=6+j8$, $Z_2=6-j8$, $Z_3=j10\ \Omega$) find the current through $Z_3$ using the nodal method. *[Sheet: $\bar I=11.774\angle-80.2^\circ$ A]*

**Tests:** [[Nodal and Mesh Analysis (AC)|nodal analysis]] with complex admittances; the one-node (Millman) shortcut.

## Given
Two sources feed a common node N through $Z_1$ and $Z_2$; $Z_3=j10\ \Omega$ (an ideal inductor) connects N to the common wire. Only N is an unknown node.

## Principle and why it applies
Nodal analysis is exactly the DC method of [[Theory - Circuit Laws and Network Theorems]] with $R\to Z$, $1/R\to Y=1/Z$. With one unknown node it reduces to the *weighted-average* formula (Millman):
$$\bar V_N=\frac{\bar V_1Y_1+\bar V_2Y_2}{Y_1+Y_2+Y_3}.$$
Using admittances avoids dividing complex numbers repeatedly.

## Diagram
![[T3-Q9-circuit.png]]

## Solution
**Admittances:**
$$Y_1=\frac1{6+j8}=\frac{6-j8}{100}=0.06-j0.08,\quad Y_2=\frac1{6-j8}=0.06+j0.08,\quad Y_3=\frac1{j10}=-j0.1\ \ (\text{S}).$$
$$Y_1+Y_2+Y_3=0.12-j0.10\ \text{S}.$$
**Source terms:**
$$\bar V_1Y_1=100(0.06-j0.08)=6-j8,\qquad \bar V_2Y_2=(50-j86.60)(0.06+j0.08)=9.928-j1.196,$$
$$\text{sum}=15.928-j9.196.$$
**Node voltage:**
$$\bar V_N=\frac{15.928-j9.196}{0.12-j0.10}=116.0+j20.05=117.7\angle9.8^\circ\ \text{V}.$$
**Current in $Z_3$:**
$$\bar I_3=\frac{\bar V_N}{Z_3}=\frac{117.7\angle9.8^\circ}{10\angle90^\circ}=\mathbf{11.774\angle-80.2^\circ\ A}.$$

## Result
$$\boxed{\bar I_{Z_3}=11.77\angle-80.2^\circ\ \text{A}}$$
(and $\bar V_N=117.7\angle9.8^\circ$ V).

## Check
KCL at N: the currents delivered by the two sources are $\bar I_1=\dfrac{\bar V_1-\bar V_N}{Z_1}=2.57\angle178.2^\circ$ A and $\bar I_2=\dfrac{\bar V_2-\bar V_N}{Z_2}=12.54\angle-68.6^\circ$ A; their sum is $2.01-j11.60=11.77\angle-80.2^\circ$ A, equal to $\bar I_3$ ✓ (`Tools/ee_t1_t4_t8.py`). An independent check is mesh analysis, as in [[T3-Q11 - Mesh, Nodal and Thevenin for Two Sources]], which has the same structure.

## Trap / alternative
- Write KCL with a **consistent** current direction at N (all leaving), then $Y_3$ has a *positive* coefficient on $\bar V_N$ with no source term.
- Keep $\bar V_2$ at $-60^\circ$ in rectangular form $(50-j86.6)$ before multiplying.
- Mesh analysis has two unknowns and gives the same answer; nodal has only one here.

## Concepts used
- Phasor nodal analysis, admittance, Millman's theorem ([[Nodal and Mesh Analysis (AC)]], [[Phasors and Complex Algebra]])
