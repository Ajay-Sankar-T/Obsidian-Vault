---
tags: [EE1100, tutorial-solution, DC-circuits, current-source, power]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q3: Two Current Sources, One Node Pair

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q2 - KVL with Three Batteries]] · Next: [[T1-Q4 - Dependent Source and Power Balance]]

> [!question] Find $V_0$, $I_1$, $I_2$ and the power in the $6\ \Omega$ resistor. An 8 A source drives current downward, a 2 A source drives current upward, with $6\ \Omega$ and $3\ \Omega$ in parallel. *[Sheet: $V_0=-6$ V, $I_1=-2$ A, $I_2=-4$ A, $P_{6\Omega}=24$ W; see the note on $V_0$ below]*

**Tests:** KCL at a node pair, [[Concepts#Ohm's Law|Ohm's law]], power sign convention.

## Given
Four elements in parallel between the top and bottom rails: current source 8 A (arrow downwards), $6\ \Omega$ ($I_1$ downwards), $3\ \Omega$ ($I_2$ downwards), current source 2 A (arrow upwards). $V_0$ is the voltage of the top rail with respect to the bottom.

## Principle and why it applies
Everything is in parallel, so there is **one unknown voltage**, $V_0$, and one KCL equation. Current sources fix currents, not voltages; the resistors then convert the net source current into a voltage.

## Diagram
![[T1-Q3-circuit.png]]

## Solution
The 2 A source pushes $2$ A **into** the top node, the 8 A source pulls $8$ A **out** of it. The net current the sources deliver into the top node is $2-8=-6$ A, and it must leave through the two resistors:
$$\frac{V_0}{6}+\frac{V_0}{3}=2-8\ \Rightarrow\ \frac{V_0}{2}=-6\ \Rightarrow\ V_0=-12\ \text{V}.$$
$$I_1=\frac{V_0}{6}=-2\ \text{A},\qquad I_2=\frac{V_0}{3}=-4\ \text{A},\qquad P_{6\Omega}=I_1^2\cdot6=24\ \text{W}.$$

The negative signs mean the actual currents flow **upwards** through the resistors; the 8 A source takes more out of the top node than the 2 A source puts in, so the top rail sits at a *lower* potential than the bottom.

## Result
$$\boxed{V_0=-12\ \text{V},\quad I_1=-2\ \text{A},\quad I_2=-4\ \text{A},\quad P_{6\Omega}=24\ \text{W}}$$

> [!warning] The printed $V_0=-6$ V
> The sheet's $I_1=-2$ A and $P_{6\Omega}=24$ W both require $V_0=6\,I_1=-12$ V; with $-6$ V the $6\ \Omega$ would dissipate $6^2/6=6$ W. $V_0=-6$ V looks like a misprint (it is half the right value). All three other answers agree with $-12$ V.

## Check
Energy balance with signs. Resistors absorb $24+48=72$ W ($3\ \Omega$: $I_2^2\cdot3=48$ W). The 8 A source: current flows down through it, voltage drop in that direction is $V_0=-12$ V, so it absorbs $V_0\times8=-96$ W, i.e. **delivers 96 W**. The 2 A source: current flows up, voltage rise $V_0=-12$ V, delivered $=2\times(-12)=-24$ W, i.e. **absorbs 24 W**. Delivered $96=72+24$ absorbed ✓.

## Trap / alternative
A current source can *absorb* power; do not assume a source always supplies. And a current source in series with a resistor is irrelevant to the voltage across the parallel combination, only the parallel elements matter.

## Concepts used
- KCL at a node pair, power sign convention ([[Theory - Circuit Laws and Network Theorems]])
