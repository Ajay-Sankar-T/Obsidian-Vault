---
tags: [EE1100, tutorial-solution, DC-circuits, kirchhoff]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q2: KVL with Three Batteries

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q1 - R-2R Ladder]] · Next: [[T1-Q3 - Current Sources and Power]]

> [!question] Using KVL, find the current in every resistor of the circuit with $E_1=E_2=E_3=10$ V and resistors $3,8,6,12\ \Omega$. *[Sheet: $I_{3}=I_{8}=I_{6}=0$, $I_{12}=0.833$ A]*

**Tests:** [[Concepts#Kirchhoff's Laws|KVL / KCL]], reading polarity, an "all-currents-vanish" check.

## Given
$E_1=10$ V (left, in series with the $3\ \Omega$), $E_2=10$ V (in series with the $8\ \Omega$), $E_3=10$ V (right, across node B), $6\ \Omega$ between nodes A and B, $12\ \Omega$ from B to the common wire. All sources have their $+$ terminal at the top.

## Principle and why it applies
Three branches meet at A, three at B, so KCL gives two equations and two independent loops give two KVL equations. There are four unknown currents and a fifth through $E_3$. The structure is special: **every battery has the same EMF**, so a single node potential might satisfy all branches at once. KVL decides whether it does.

## Diagram
![[T1-Q2-circuit.png]]

## Solution
Let $I_1$ be the current in the $3\ \Omega$ (left to right), $I_2$ in the $8\ \Omega$ (downward), $I_3$ in the $6\ \Omega$ (towards B), $I_4$ in the $12\ \Omega$ (downward), $I_5$ the current $E_3$ pushes into node B.

**KCL.** At A: $I_1=I_2+I_3$. At B: $I_3+I_5=I_4$.

**KVL.**
- Loop $E_1$–$3\ \Omega$–$8\ \Omega$–$E_2$: $\ 10-3I_1-8I_2-10=0\ \Rightarrow\ 3I_1+8I_2=0.$
- Loop $E_2$–$8\ \Omega$–$6\ \Omega$–$E_3$: $\ -8I_2-10+10+6I_3=0\ \Rightarrow\ 6I_3=8I_2.$
- Loop $E_3$–$12\ \Omega$: $\ 10-12I_4=0\ \Rightarrow\ I_4=\dfrac{10}{12}=0.833\ \text{A}.$

From the first two, $I_1=-\tfrac83I_2$ and $I_3=\tfrac43I_2$. KCL at A then gives $-\tfrac83I_2=I_2+\tfrac43I_2=\tfrac73I_2$, so $-8I_2=7I_2$ and

$$I_2=0\ \Rightarrow\ I_1=0,\ I_3=0,\qquad I_5=I_4=0.833\ \text{A}.$$

## Result
$$\boxed{I_{3\Omega}=I_{8\Omega}=I_{6\Omega}=0,\qquad I_{12\Omega}=0.833\ \text{A (top to bottom)}}$$
$E_3$ alone supplies the $12\ \Omega$; $E_1$ and $E_2$ float.

## Check
Both nodes sit at $10$ V: A is held at $E_1=10$ V (no drop in the $3\ \Omega$) and at $E_2=10$ V, so the $8\ \Omega$ has $0$ V across it; likewise A and B are at the same potential so the $6\ \Omega$ carries nothing. Power: $E_3$ delivers $10\times0.833=8.33$ W $=I_4^2\times12=8.33$ W ✓.

## Trap / alternative
Do not assume currents must be non-zero because there are three batteries. A faster route is **nodal** (Millman): $V_A,V_B$ with $V_A=\dfrac{E_1/3+E_2/8+V_B/6}{1/3+1/8+1/6}$ etc. gives $V_A=V_B=10$ V in two lines. The lesson is that **equal EMFs in parallel branches produce no circulating current**; with unequal EMFs you would get circulating currents in the $E_1$–$E_2$ loop.

## Concepts used
- KVL, KCL, nodal check ([[Theory - Circuit Laws and Network Theorems]])
