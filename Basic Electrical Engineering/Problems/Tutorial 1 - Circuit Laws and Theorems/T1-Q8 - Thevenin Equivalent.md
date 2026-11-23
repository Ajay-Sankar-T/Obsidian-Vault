---
tags: [EE1100, tutorial-solution, DC-circuits, thevenin]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q8: Thevenin Equivalent Seen by the 20 Ω Resistor

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q7 - Mesh Analysis with Current Sources]] · Next: [[T1-Q9 - Norton Equivalent]]

> [!question] Find the Thevenin equivalent seen by the $20\ \Omega$ resistor between $a$ and $b$ in the network with sources of 45 V, 120 V and 20 V and resistors $10,5,5,15\ \Omega$. *[Sheet: $V_{th}=63$ V, $R_{th}=4.67\ \Omega$]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#8. Thevenin and Norton equivalents|Thevenin's theorem]]: remove the load, find $V_{oc}$, kill sources for $R_{th}$.

## Given
The 45 V source (positive at the top) joins the top rail $a$ to the left node $L$. The 120 V source (positive on the left) joins $a$ to the top-right corner, then $15\ \Omega$ down to the right node $R$. $10\ \Omega$ from $L$ to $b$ and $5\ \Omega$ from $b$ to $R$ along the middle. Along the bottom: the 20 V source (positive on the left) and a $5\ \Omega$ from $L$ round to $R$. The $20\ \Omega$ load sits between $a$ and $b$.

## Principle and why it applies
The load is one element in a linear network; everything else can be collapsed into $V_{th}$ and $R_{th}$ **as seen from $a$-$b$** (see theory §8). Step 1 remove the $20\ \Omega$; step 2 compute the open-circuit voltage; step 3 switch the independent sources off and compute the resistance between $a$ and $b$.

## Diagram
![[T1-Q8-circuit.png]]

## Solution
**Open-circuit voltage.** Take $b$ as the reference (0 V). Let the left node be at $V_L$ and the right node at $V_R$. The top rail is $V_a=V_L+45$ and the top-right corner is $V_a-120=V_L-75$. Currents: through the $15\ \Omega$ (downwards) $\dfrac{V_L-75-V_R}{15}$; through the $10\ \Omega$ $\dfrac{V_L}{10}$; through the lower branch (20 V source then $5\ \Omega$) $\dfrac{V_L-20-V_R}{5}$; through the middle $5\ \Omega$ (from $R$ to $b$) $\dfrac{V_R}{5}$.

KCL at $R$: $\ \dfrac{V_L-75-V_R}{15}+\dfrac{V_L-20-V_R}{5}=\dfrac{V_R}{5}\ \Rightarrow\ 4V_L-7V_R=135.$

KCL at $L$ (the 45 V source delivers the same current as the 120 V source and $15\ \Omega$): $\ \dfrac{V_L}{10}+\dfrac{V_L-20-V_R}{5}+\dfrac{V_L-75-V_R}{15}=0\ \Rightarrow\ 11V_L-8V_R=270.$

Solving: $V_R=-9$ V, $V_L=18$ V. So
$$V_{th}=V_a-V_b=(18+45)-0=63\ \text{V}.$$

**Thevenin resistance** (all three sources shorted). The shorted 45 V source ties $a$ to $L$ and the shorted 120 V source ties $a$ to the top-right corner, so $a$, $L$ and that corner are one node. From it to $R$ there are two parallel paths: the $15\ \Omega$ and the lower $5\ \Omega$ (the 20 V source is shorted): $15\parallel5=3.75\ \Omega$. Looking from $a$ to $b$: the $10\ \Omega$ (directly from $L=a$ to $b$) is in parallel with ($5\ \Omega$ from $b$ to $R$ in series with $3.75\ \Omega$ back to $a$):
$$R_{th}=10\parallel(5+3.75)=\frac{10\times8.75}{18.75}=4.67\ \Omega.$$

## Result
$$\boxed{V_{th}=63\ \text{V},\qquad R_{th}=4.67\ \Omega}$$
The $20\ \Omega$ load would then draw $63/(4.67+20)=2.55$ A and drop $51$ V.

## Check
`Tools/ee_t1_t4_t8.py` solves the original circuit (with the $20\ \Omega$ removed) by modified nodal analysis and also gets $V_a-V_b=63.0$ V. Dimensionally $R_{th}<10\ \Omega$ (it must be below the smallest direct path) ✓.

## Trap / alternative
Don't leave the $20\ \Omega$ in when computing $V_{oc}$; and when finding $R_{th}$, remember that a shorted ideal voltage source merges nodes, which is what makes the diagram collapse. An alternative route to $V_{th}$ is a single mesh/nodal solve of the loaded circuit followed by $V_{th}=V_{ab}(1+R_{th}/20)$.

## Concepts used
- Thevenin's theorem, nodal analysis, source shorting ([[Theory - Circuit Laws and Network Theorems]])
