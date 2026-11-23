---
tags: [EE1100, tutorial-solution, DC-circuits, norton]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q9: Norton Equivalent Seen by R_L

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q8 - Thevenin Equivalent]] · Next: [[T1-Q10 - Maximum Power Transfer and Half Power]]

> [!question] By direct application of Norton's theorem find the Norton equivalent seen by $R_L$ in the circuit with sources 120 V, 40 V and 10 V and resistors $30,60,10,30\ \Omega$. *[Sheet: $I_N=I_{sc}=4.67$ A, $R_N=15\ \Omega$]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#8. Thevenin and Norton equivalents|Norton's theorem]]: short the load for $I_N$, kill sources for $R_N$.

## Given
120 V ($+$ at top) → $30\ \Omega$ → node X, with a $60\ \Omega$ shunt to ground; the 40 V source ($-$ left, $+$ right) in series with a $10\ \Omega$ → node $a$, with a $30\ \Omega$ shunt; then $R_L$ to $b$, which connects to ground through a 10 V source with its $+$ terminal at the bottom (so $b$ sits $10$ V *below* ground).

## Principle and why it applies
Norton's theorem is the current-source form of Thevenin: $I_N=i_{sc}$ (short $a$-$b$), $R_N=R_{th}$ (sources off). "Direct application" means we literally **short the load** and find the current. Since the $10$ V source is in the load branch it counts as part of the *circuit seen by $R_L$*, so it must be included.

## Diagram
![[T1-Q9-circuit.png]]

## Solution
**Short-circuit current.** Collapse the left part step by step with Thevenin reductions.
- Node X: $120$ V behind $30\ \Omega$ with $60\ \Omega$ to ground: $V_X=120\cdot\dfrac{60}{90}=80$ V behind $30\parallel60=20\ \Omega$.
- Add the 40 V source (it raises the potential by 40 V going to the right): $120$ V behind $20\ \Omega$.
- Add the $10\ \Omega$: $120$ V behind $30\ \Omega$ seen at node $a$.
- Node $a$ also has the $30\ \Omega$ shunt: $V_{a,oc}=120\cdot\dfrac{30}{30+30}=60$ V behind $30\parallel30=15\ \Omega$.
- With the load terminals shorted, the load branch has the 10 V source in series, adding to the driving voltage: $60-(-10)=70$ V behind $15\ \Omega$.
$$I_N=I_{sc}=\frac{70}{15}=4.67\ \text{A}.$$

**Norton resistance** (all sources off): $120$ V shorted → $30\parallel60=20\ \Omega$; $40$ V shorted → in series with $10\ \Omega$ gives $30\ \Omega$; in parallel with the $30\ \Omega$ shunt:
$$R_N=30\parallel30=15\ \Omega.$$

## Result
$$\boxed{I_N=4.67\ \text{A},\qquad R_N=15\ \Omega}$$
(equivalently $V_{th}=I_NR_N=70$ V: the open-circuit voltage between $a$ and $b$).

## Check
Voltage across $a$-$b$ open-circuit: $V_a-V_b=60-(-10)=70$ V and $70/15=4.67$ A ✓ (`Tools/ee_t1_t4_t8.py` solves the shorted circuit directly and gets $4.667$ A).

## Trap / alternative
- Forgetting the 10 V source in the load branch gives $I_N=4$ A.
- The direction of the 40 V source matters: it *adds* to the 80 V at node X.
- Norton and Thevenin are interchangeable: here $V_{th}=70$ V, $R_{th}=15\ \Omega$; with $R_L$ attached $I_L=70/(15+R_L)$.

## Concepts used
- Norton's theorem, source transformation, successive Thevenin reduction ([[Theory - Circuit Laws and Network Theorems]])
