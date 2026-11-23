---
tags: [EE1100, tutorial-solution, DC-circuits, dependent-source, power]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q4: Dependent Current Source and Power Balance

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q3 - Current Sources and Power]] · Next: [[T1-Q5 - Maximum Power with a Dependent Source]]

> [!question] A 12 V source, $R_1=6\ \Omega$, a dependent current source $K\,I$ (where $I$ is the current in $R_1$), and $R_2=3\ \Omega$ are all in parallel. Find the power absorbed by each element for (a) $K=2$, (b) $K=-2$. *[Sheet: (a) 24, 24, 48, 48 W; (b) 120, 24, $-48$, 48 W]*

**Tests:** [[Concepts#Kirchhoff's Laws|KCL]], dependent sources, power sign convention.

## Given
Voltage source $E=12$ V; $R_1=6\ \Omega$ with current $I$ (downwards); dependent source delivering $KI$ upwards; $R_2=3\ \Omega$; $I_1$ is the source current.

## Principle and why it applies
Everything is in parallel, so **all four elements have 12 V across them**; the voltage source fixes it. Hence $I=12/6=2$ A *regardless of $K$*, and the dependent source then simply injects $KI$. The only thing left to find is the current the 12 V source must supply, from KCL.

## Diagram
![[T1-Q4-circuit.png]]

## Solution
$$I=\frac{12}{6}=2\ \text{A},\qquad I_{R_2}=\frac{12}{3}=4\ \text{A},\qquad KI=2K\ \text{A (upward)}.$$
KCL at the top node, $I_1+KI=I+I_{R_2}$:
$$I_1=2+4-2K.$$

| | $K=2$ | $K=-2$ |
|---|---|---|
| $KI$ | $+4$ A | $-4$ A |
| $I_1$ | $2$ A | $10$ A |
| $P_{12\text{V}}$ delivered $=12I_1$ | **24 W** | **120 W** |
| $P_{6\Omega}=12^2/6$ | **24 W** | **24 W** |
| $P_{3\Omega}=12^2/3$ | **48 W** | **48 W** |
| dependent source, delivered $=12\,KI$ | **48 W** | **$-48$ W** |

## Result
(a) 24 W (source), 24 W, 48 W (resistors), the dependent source **delivers** 48 W. (b) The 12 V source delivers 120 W, the resistors still absorb 24 W and 48 W, and the dependent source **absorbs** 48 W ($-48$ W delivered).

## Check
(a) $24+48=72=24+48$ ✓. (b) $120=24+48+48$ ✓ (the source feeds the resistors *and* the dependent source).

## Trap / alternative
A **dependent source is not "free"**: its sign depends on $K$ and it can sink power as in (b). The resistor powers do not change with $K$, because the 12 V source pins the voltage. Do not try to switch the dependent source off (superposition) here.

## Concepts used
- Dependent sources, KCL, Tellegen power balance ([[Theory - Circuit Laws and Network Theorems]])
