---
tags: [EE1100, tutorial-solution, DC-circuits, mesh-analysis, current-source]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q7: Mesh Analysis When Current Sources Sit on the Edge

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q6 - Superposition]] · Next: [[T1-Q8 - Thevenin Equivalent]]

> [!question] (a) How many meshes? (b) Mesh currents of the inner and outer meshes? (c) All mesh currents? (d) $V_1$ and $V_2$? The circuit has a 10 A source, $1\ \Omega$, $2.5\ \Omega$, $0.5\ \Omega$ and a 4 A source. *[Sheet: 3 meshes; $10$ and $-4$ A (clockwise); $10,2,-4$ A; $V_1=8$ V, $V_2=3$ V]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#6. Mesh analysis|mesh analysis]] with current sources, shared branches.

## Given
Left mesh: 10 A source (upward) and the $1\ \Omega$ shunt. Middle mesh: $1\ \Omega$, the $2.5\ \Omega$ series resistor and the $0.5\ \Omega$ shunt. Right mesh: the $0.5\ \Omega$ shunt and the 4 A source (upward). $V_1$ and $V_2$ are the voltages across the two shunt resistors.

## Principle and why it applies
**(a)** Meshes = branches $-$ nodes $+1$. Here there are three windows, so **3 meshes**. In a mesh that contains a current source *only on its outer edge*, the mesh current **is** the source current (up to sign), which removes two unknowns. A source on the outer edge needs no supermesh.

## Diagram
![[T1-Q7-circuit.png]]

## Solution
**(b)** Take all mesh currents clockwise. The 10 A source points up on the left edge, the direction a clockwise current takes there, so $I_a=+10$ A. The 4 A source points up on the *right* edge, where a clockwise current goes *down*, so $I_c=-4$ A. These are the "inner/outer" mesh currents of the question: $10$ A and $-4$ A.

**(c)** Only the middle mesh needs a KVL. The $1\ \Omega$ carries $I_a-I_b$ (down), the $0.5\ \Omega$ carries $I_b-I_c$ (down), the $2.5\ \Omega$ carries $I_b$:
$$2.5I_b+0.5(I_b-I_c)+1\,(I_b-I_a)=0\ \Rightarrow\ 4I_b=I_a+0.5I_c=10-2=8\ \Rightarrow\ I_b=2\ \text{A}.$$

**(d)** $V_1$ is the drop in the $1\ \Omega$: $V_1=1\times(I_a-I_b)=1\times(10-2)=8$ V. $V_2$ is the drop in the $0.5\ \Omega$: $V_2=0.5\times(I_b-I_c)=0.5\times(2+4)=3$ V.

## Result
$$\boxed{3\ \text{meshes};\ \ I_a=10,\ I_b=2,\ I_c=-4\ \text{A (clockwise)};\ \ V_1=8\ \text{V},\ V_2=3\ \text{V}}$$

## Check
KCL at node $V_1$: 10 A enters from the source, $8$ A leaves through the $1\ \Omega$, so $2$ A leaves through the $2.5\ \Omega$ ✓ ($I_b=2$ A). At node $V_2$: $2$ A arrives, $4$ A is injected by the 4 A source, and $6$ A leaves through the $0.5\ \Omega$ ($V_2/0.5=6$) ✓.

## Trap / alternative
The sign of $I_c$: it is negative only because the mesh is taken **clockwise** while the source points the other way round the loop. Nodal analysis needs only two unknowns ($V_1,V_2$) and is just as quick here: $\frac{V_1}{1}+\frac{V_1-V_2}{2.5}=10$, $\frac{V_2}{0.5}+\frac{V_2-V_1}{2.5}=4$ gives the same $8$ V and $3$ V. When the sources are all current sources, nodal is usually the better choice.

## Concepts used
- Mesh analysis, shared branches, current sources on the boundary ([[Theory - Circuit Laws and Network Theorems]])
