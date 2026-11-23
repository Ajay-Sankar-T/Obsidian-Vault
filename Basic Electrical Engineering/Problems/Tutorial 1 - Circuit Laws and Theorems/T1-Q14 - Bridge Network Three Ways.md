---
tags: [EE1100, tutorial-solution, DC-circuits, star-delta, mesh-analysis, nodal-analysis]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q14: A Bridge Network, Solved Three Ways

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q13 - Star-Delta Reduction]] · Next tutorial: [[Tutorial 2 - Transient Analysis of DC Circuits]]

> [!question] For the circuit (180 V source feeding the bridge $R_{ca}=15,R_{ab}=20,R_{bc}=35,R_{cd}=8,R_{bd}=25\ \Omega$) find the current in every element and the current supplied by the source using (i) star–delta transformation, (ii) mesh analysis, (iii) nodal analysis, and prove that the power consumed equals the power supplied. *[Sheet: $I_{ac}=7.573$, $I_{ab}=4.405$, $I_{bc}=0.729$, $I_{cd}=8.301$, $I_{bd}=3.676$, $I_{source}=11.978$ A; $P\approx2156$ W]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#10. Star–delta (Y–Δ) transformation|Y–Δ]], [[Theory - Circuit Laws and Network Theorems#6. Mesh analysis|mesh]], [[Theory - Circuit Laws and Network Theorems#5. Nodal analysis|nodal]]; choosing a method.

## Given
The source $E=180$ V ($+$ at $a$) is connected between $a$ and $d$. Resistors: $c$–$a$ 15 Ω, $a$–$b$ 20 Ω, $c$–$b$ 35 Ω, $c$–$d$ 8 Ω, $b$–$d$ 25 Ω. No two resistors are in series or parallel (a Wheatstone-type bridge with $R_{bc}$ as the unbalance branch).

## Principle and why it applies
This is the classic case where **series/parallel reduction fails**, and all three general methods succeed. They are equivalent: they solve the same linear system, just with different unknowns. The question tests which is shortest (nodal: two unknowns) and that all three agree.

## Diagram
![[T1-Q14-circuit.png]]

## Solution
**(i) Star–delta.** Convert the triangle $a$-$b$-$c$ ($15,20,35$; sum $70\ \Omega$) to a star with centre $O$:
$$R_a=\frac{15\times20}{70}=4.286,\quad R_b=\frac{20\times35}{70}=10,\quad R_c=\frac{15\times35}{70}=7.5\ \ (\Omega).$$
Now from $O$ to $d$ there are two parallel paths: $R_b+R_{bd}=35\ \Omega$ and $R_c+R_{cd}=15.5\ \Omega$, giving $35\parallel15.5=10.743\ \Omega$. Total
$$R_{tot}=4.286+10.743=15.028\ \Omega,\qquad I_{source}=\frac{180}{15.028}=11.978\ \text{A}.$$
$V_O=180-11.978\times4.286=128.67$ V; the path currents are $128.67/35=3.676$ A (through $R_{bd}$) and $128.67/15.5=8.301$ A (through $R_{cd}$) ✓. Then in the original delta $V_b=3.676\times25=91.9$ V and $V_c=8.301\times8=66.4$ V, so $I_{ab}=(180-91.9)/20=4.405$ A, $I_{ac}=(180-66.4)/15=7.573$ A, $I_{bc}=(91.9-66.4)/35=0.729$ A.

**(ii) Mesh** (clockwise; $I_1$ = left face through the source, $I_2$ = top triangle, $I_3$ = bottom triangle). The shared branches carry differences of mesh currents:
$$15(I_1-I_2)+8(I_1-I_3)=180,$$
$$20I_2+35(I_2-I_3)+15(I_2-I_1)=0,$$
$$25I_3+8(I_3-I_1)+35(I_3-I_2)=0.$$
Solving the $3\times3$ system: $I_1=11.978$, $I_2=4.405$, $I_3=3.676$ A. Hence $I_{ac}=I_1-I_2=7.573$, $I_{cd}=I_1-I_3=8.302$, $I_{cb}=I_3-I_2=-0.729$ A (i.e. $0.729$ A flows from $b$ to $c$).

**(iii) Nodal** (two unknowns because $V_a=180$ and $V_d=0$ are known):
$$\frac{V_c-180}{15}+\frac{V_c-V_b}{35}+\frac{V_c}{8}=0,\qquad \frac{V_b-180}{20}+\frac{V_b-V_c}{35}+\frac{V_b}{25}=0$$
$$\Rightarrow\ 0.2202V_c-0.0286V_b=12,\quad 0.1186V_b-0.0286V_c=9\ \Rightarrow\ V_b=91.91\ \text{V},\ V_c=66.41\ \text{V}.$$
The branch currents follow from Ohm's law as above.

**Power balance.**

| Resistor | $I$ (A) | $P=I^2R$ (W) |
|---|---|---|
| $R_{ca}=15$ | 7.573 | 860.2 |
| $R_{ab}=20$ | 4.405 | 388.0 |
| $R_{bc}=35$ | 0.729 | 18.6 |
| $R_{cd}=8$ | 8.301 | 551.3 |
| $R_{bd}=25$ | 3.676 | 337.9 |
| **total absorbed** | | **2156.0** |

Source: $P=EI=180\times11.978=2156.0$ W ✓.

## Result
$$\boxed{I_{ac}=7.573,\ I_{ab}=4.405,\ I_{bc}=0.729\ (b\to c),\ I_{cd}=8.301,\ I_{bd}=3.676,\ I_{source}=11.978\ \text{A};\ \ P_{\text{supplied}}=P_{\text{consumed}}=2156\ \text{W}}$$

## Check
All three methods agree; KCL at $c$: $7.573+0.729=8.302$ ✓. The bridge is **unbalanced** ($15/20\neq8/25$), which is why $R_{bc}$ carries a current at all; it would carry zero if $R_{ca}R_{bd}=R_{ab}R_{cd}$.

## Trap / alternative
Compare effort: star–delta needs one transformation and one reduction; nodal needs two equations; mesh needs three. Nodal wins here because the source fixes two node voltages. In (i), convert the triangle **whose resistors are all external to the source terminals** (a-b-c); converting the other triangle (b-c-d) is equally valid but the bookkeeping is messier.

## Concepts used
- Star–delta transformation, mesh and nodal analysis, power balance ([[Theory - Circuit Laws and Network Theorems]])
