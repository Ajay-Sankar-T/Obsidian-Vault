---
tags: [EE1100, tutorial-solution, DC-circuits, nodal-analysis, supernode]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q11: Two Supernodes

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q10 - Maximum Power Transfer and Half Power]] · Next: [[T1-Q12 - Mesh Analysis and Power Balance]]

> [!question] Find the currents in all branches and the voltage $v_4$. (Hint: nodes $a$ and $c$, and $b$ and $d$, form supernodes.) *[Sheet: $I_{ac}=8.063$, $I_{ba}=3.063$, $I_{da}=5$ (given), $I_{cd}=0.586$, $I_{ce}=7.477$, $I_{bd}=6.937$, $I_{de}=2.523$, $I_{eb}=10$ (given) A; $v_4=63.06$ V]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#5. Nodal analysis|nodal analysis with supernodes]].

## Given
Five nodes $a,b,c,d,e$. 100 V battery between $c$ and $a$ ($+$ at $a$); 5 A source from $d$ to $a$; $12.5\ \Omega$ between $a$ and $b$; $20\ \Omega$ between $c$ and $d$; 150 V battery between $d$ and $b$ ($+$ at $b$); $25\ \Omega$ between $d$ and $e$ (voltage $v_4=V_d-V_e$); $10\ \Omega$ between $c$ and $e$; 10 A source from $e$ to $b$.

## Principle and why it applies
A battery between two non-reference nodes has **no current expressed through its voltage**, so nodal analysis cannot write KCL at either of its nodes separately. The remedy (theory §5) is to merge each battery's two nodes into a **supernode**, write KCL for the whole supernode and use the battery as the constraint $V_a-V_c=100$, $V_b-V_d=150$. Choose $e$ as ground; the unknowns reduce to $V_c$ and $V_d$.

## Diagram
![[T1-Q11-circuit.png]]

## Solution
Constraints: $V_a=V_c+100$, $V_b=V_d+150$.

**KCL for the supernode $\{a,c\}$** (currents leaving $=0$; the 5 A source *enters* at $a$):
$$\frac{V_a-V_b}{12.5}+\frac{V_c-V_d}{20}+\frac{V_c}{10}=5.$$
**KCL for $\{b,d\}$** (the 10 A source enters at $b$, the 5 A source leaves at $d$):
$$\frac{V_b-V_a}{12.5}+\frac{V_d-V_c}{20}+\frac{V_d}{25}+5=10.$$
Let $x=V_c-V_d$. Substituting the constraints ($V_a-V_b=x-50$):
$$0.13\,x+0.1\,V_c=9,\qquad -0.17\,x+0.04\,V_c=1\ \Rightarrow\ x=11.712\ \text{V},\ V_c=74.775\ \text{V},\ V_d=63.063\ \text{V}.$$

So $v_4=V_d-V_e=\mathbf{63.06\ V}$, and $V_a=174.775$ V, $V_b=213.063$ V.

**Branch currents:**
$$I_{cd}=\frac{x}{20}=0.586\ \text{A},\quad I_{ce}=\frac{V_c}{10}=7.477\ \text{A},\quad I_{de}=\frac{V_d}{25}=2.523\ \text{A},\quad I_{ba}=\frac{V_b-V_a}{12.5}=3.063\ \text{A}.$$
Through the batteries (from KCL, since a battery's current is not given by its voltage): at $a$: $5=I_{ab}+I_{ac}$ with $I_{ab}=-3.063$, so $I_{ac}=\mathbf{8.063\ A}$; at $b$ (10 A enters, $I_{ab}$ is $-3.063$ A into $b$ from $a$): $I_{bd}=10-3.063=\mathbf{6.937\ A}$.

## Result
$$\boxed{v_4=63.06\ \text{V};\quad I_{ac}=8.063,\ I_{ba}=3.063,\ I_{cd}=0.586,\ I_{ce}=7.477,\ I_{bd}=6.937,\ I_{de}=2.523\ \text{A}}$$

## Check
KCL at $c$: $8.063$ A arrives through the 100 V source and leaves as $0.586+7.477=8.063$ ✓. At $d$: the current arriving is $0.586$ (from $c$) $+\,6.937$ (from $b$ through the 150 V source) $=7.523$ A, and it leaves as $2.523$ (through the $25\ \Omega$) $+\,5$ (through the 5 A source) $=7.523$ A ✓.

## Trap / alternative
Do **not** try to write the battery current as $(V_a-V_c)/R$ (there is no resistor). And remember that the current *given* sources ($5$ A, $10$ A) enter the KCL with fixed signs. A mesh solution is longer here: the two current sources are on interior branches (supermesh needed).

## Concepts used
- Nodal analysis, supernodes, KCL ([[Theory - Circuit Laws and Network Theorems]])
