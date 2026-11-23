---
tags: [EE1100, tutorial-theory, DC-circuits, network-theorems]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# Theory: Circuit Laws and Network Theorems

← up: [[Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]] · lectures: [[Lecture 3 Kirchhoff_s Laws.pdf]], [[Lecture 4 Mesh and Modal Methods for Circuit Analysis.pdf]], [[Lecture 5 Node Pair Methods, Thevenin and Norton_s Theorems.pdf]], [[Lecture 6 Thevenin, Norton, Maximum Power Transfer and Star-Delta Transformation.pdf]], [[Lecture 7 Dependent Sources, Concept of Super Nodes, Super meshes.pdf]] · weeks: [[01 Basic Concepts and Basic Laws]], [[02 Methods of Circuit Analysis]], [[03 DC Network Theorems]]

> [!abstract] The one-paragraph version
> A lumped circuit is a graph whose edges obey two kinds of equations: **element laws** (one per branch: $v=Ri$, or a source's value) and **conservation laws** (KCL at nodes, KVL around loops). Every analysis method in this tutorial is a way of choosing unknowns so that the two kinds of equations collapse into a small linear system. The network theorems then say that, *because the system is linear*, a complicated network can be replaced, as seen from two terminals, by one source and one resistor.

## 1. Variables and sign conventions

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| charge | $q$ | | C |
| current | $i=dq/dt$ | rate of charge flow through a cross-section | A |
| voltage | $v_{ab}=V_a-V_b$ | energy per unit charge to move $+q$ from $b$ to $a$ | V |
| power | $p=vi$ | rate of energy transfer | W |

**Passive sign convention.** If the current $i$ enters the terminal marked $+$ of an element, then $p=vi>0$ means the element **absorbs** power. For a resistor this is automatic, $p=i^2R\ge 0$. A source can have either sign: a battery being charged absorbs power, a dependent source can absorb too. Every "power delivered by a source" figure in this tutorial uses the opposite statement: **delivered** $=v\,i$ with $i$ *leaving* the $+$ terminal.

$$\sum_{\text{all elements}} p_{\text{absorbed}}=0\qquad\text{(Tellegen / conservation of energy)}$$

This is the check used in Q3, Q4, Q12 and Q14: total delivered by the sources equals total absorbed by the resistors, *with signs*. It catches almost every sign error.

## 2. The two conservation laws

**KCL** (Kirchhoff's current law): $\sum i_{\text{leaving a node}}=0$. Why: a node is a point, it cannot store charge, so whatever flows in must flow out. (The same statement as $\nabla\cdot\mathbf J=0$ in steady state, or fluid continuity at a pipe junction; see [[Conservation Laws and Flow Networks]].)

**KVL** (Kirchhoff's voltage law): $\sum v_{\text{around a loop}}=0$. Why: the electric field in a lumped circuit is conservative, so the work done on a unit charge around any closed path is zero; equivalently every node has one well-defined potential.

**Ohm's law** $v=Ri$ with $R=\rho L/A$; conductance $G=1/R$.

*Counting.* A connected circuit with $b$ branches and $n$ nodes has $n-1$ independent KCL equations and $b-n+1$ independent KVL equations (the number of meshes if the circuit is planar). With the $b$ element equations they fix the $2b$ unknowns ($b$ currents and $b$ voltages). Nodal analysis reduces the work to $n-1$ unknowns, mesh analysis to $b-n+1$.

## 3. Series, parallel, dividers

$$R_{\text{series}}=\sum R_k,\qquad \frac1{R_\parallel}=\sum\frac1{R_k},\qquad R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}.$$

**Voltage divider** (same current through both): $v_k=v\,R_k/\sum R$. **Current divider** (same voltage across both): $i_1=i\,R_2/(R_1+R_2)$, the *other* resistor in the numerator. See [[Voltage Divider Rule]] and [[Series-Parallel Resistance Reduction]]; the R-2R ladder of Q1 is the cleanest example of reducing from the far end.

## 4. Sources

- **Ideal voltage source:** fixes $v$; the current is whatever the rest of the circuit demands. Setting it to 0 V (a short circuit) is "turning it off".
- **Ideal current source:** fixes $i$; the voltage is whatever the rest demands. Setting it to 0 A (an open circuit) is "turning it off".
- **Dependent (controlled) source:** its value is a multiple of a voltage or current elsewhere ($v=\mu v_x$, $i=\beta i_x$, $v=r\,i_x$, $i=g\,v_x$), drawn as a diamond. It is **not** an independent excitation, so it can never be switched off in superposition, and it makes the Thevenin resistance non-trivial (Q4, Q5).

## 5. Nodal analysis

1. Choose a reference node (ground); call the other node potentials $V_1,\dots,V_{n-1}$.
2. At each node write KCL with every branch current as $(V_{\text{this}}-V_{\text{other}})/R$.
3. Solve the system $\mathbf G\mathbf V=\mathbf I_s$. $\mathbf G$ is symmetric: diagonal = total conductance at the node, off-diagonal = minus the conductance between two nodes.

**Supernode.** A voltage source between two non-reference nodes has no defined branch current, so enclose it: treat the two nodes as one supernode, write one KCL for the whole group, and add the constraint $V_a-V_b=E$. This is Q11, which has two supernodes at once.

Use nodal analysis when there are **few nodes** or many current sources.

## 6. Mesh analysis

1. Draw one clockwise loop current per mesh (planar circuits).
2. Write KVL around each mesh: $\sum R\,I_{\text{own}}-\sum R_{\text{shared}}I_{\text{neighbour}}=\sum E_{\text{rises}}$.
3. A branch shared by two meshes carries the **difference** of the two mesh currents.

**Supermesh.** A current source shared by two meshes has an unknown voltage; remove it, write one KVL around the combined outer loop, and add the constraint $I_a-I_b=I_s$. A current source on the outside edge of one mesh simply fixes that mesh current (Q7, Q12).

Use mesh analysis when there are **few meshes** or many voltage sources.

## 7. Superposition

Because every element equation is linear, the response to several independent sources is the sum of the responses to each source acting alone, with the others turned off (voltage sources shorted, current sources opened). **Dependent sources stay in every sub-circuit.** It applies to currents and voltages but **not to power** ($p=i^2R$ is quadratic, so cross-terms survive). It is slower than nodal analysis when there are many sources, but it wins when the sources are of different kinds or you want each source's contribution (Q6).

## 8. Thevenin and Norton equivalents

Any linear two-terminal network is equivalent, as seen from its terminals, to a **voltage source $V_{th}$ in series with $R_{th}$**, or to a **current source $I_N$ in parallel with $R_N=R_{th}$**, with

$$V_{th}=v_{oc},\qquad I_N=i_{sc},\qquad R_{th}=\frac{v_{oc}}{i_{sc}}.$$

*Why it works:* with a load attached the terminal relation is linear, $v=V_{th}-R_{th}i$, a straight line; two points ($v_{oc}$ at $i=0$ and $i_{sc}$ at $v=0$) fix it. Three ways to get $R_{th}$:

1. **Turn off the independent sources** and combine resistances as seen from the terminals (only valid when there are **no dependent sources**): Q8, Q9, Q10.
2. **Test source:** with the independent sources off, connect $v_t$ (or $i_t$) at the terminals and compute $R_{th}=v_t/i_t$. Always works and is **needed with dependent sources** (Q5).
3. **$v_{oc}/i_{sc}$.**

Source transformation ($E$ with $R$ in series $\leftrightarrow$ $E/R$ with $R$ in parallel) is the local version of the same equivalence (it is the hint for Tutorial 2, Q5).

## 9. Maximum power transfer

Load $R_L$ on a Thevenin source:
$$P_L=\frac{V_{th}^2R_L}{(R_{th}+R_L)^2},\qquad \frac{dP_L}{dR_L}=0\ \Rightarrow\ R_L=R_{th},\qquad P_{\max}=\frac{V_{th}^2}{4R_{th}}.$$

At that point the *efficiency* (power in the load over power from the source) is only 50 %: matching is for signals, where you want the most power, not for power systems, where you want efficiency. The curve is flat-topped, and $P_L=P_{\max}/2$ has **two** solutions, from $R_L^2-6R_{th}R_L+R_{th}^2=0$, i.e. $R_L=(3\pm2\sqrt2)R_{th}$, one above and one below $R_{th}$ (Q10).

## 10. Star–delta ($\mathrm{Y}$–$\Delta$) transformation

Two three-terminal resistor networks are equivalent if every pair of terminals sees the same resistance with the third terminal left open.

$$\Delta\to Y:\ \ R_a=\frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}\ \ (\text{product of the two adjacent}),\qquad
Y\to\Delta:\ \ R_{ab}=\frac{R_aR_b+R_bR_c+R_cR_a}{R_c}\ \ (\text{sum of products over the opposite}).$$

For a balanced network $R_Y=R_\Delta/3$. Use it when a bridge has no series or parallel pair (Q13, Q14). The same transformation reappears in the three-phase loads of [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]].

## Choosing a method

| The circuit has | Prefer |
|---|---|
| few nodes, current sources | nodal |
| few meshes, voltage sources | mesh |
| a floating voltage source | supernode |
| a current source shared by two meshes | supermesh |
| one load whose value changes, or "what does this part look like" | Thevenin / Norton |
| mixed sources, "contribution of each" | superposition |
| a bridge with no series/parallel pair | star–delta, or nodal |
| dependent sources | nodal or mesh with the control variable written in terms of the unknowns; Thevenin by test source |

## Common traps
- Getting the **sign** of a source wrong in a loop equation (write "rise" for $-\to+$ in the direction of travel).
- Switching off a **dependent** source in superposition or in a Thevenin calculation.
- Quoting power for a source without saying *delivered* or *absorbed*.
- Using the current divider with the wrong resistor in the numerator.
- Forgetting that a shared branch carries $I_1-I_2$.

## Cross-domain links
- [[Conservation Laws and Flow Networks]]: KCL and KVL are the electrical case of "flow conserved at junctions, potential single-valued around loops"; the same linear system solves pipe networks.
- [[Gears, Transformers and Reflected Impedance]]: Thevenin/Norton and impedance matching are the DC seed of the AC maximum-power condition $Z_L=Z_{th}^*$ ([[T3-Q12 - AC Maximum Power Transfer]]).
