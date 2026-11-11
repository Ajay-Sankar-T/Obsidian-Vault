---
tags: [EE1100, op-amp, tutorial-solution, nodal-analysis]
---

# T6-Q9 — Op-Amp Circuit with a Single Source

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q8 - Photodiode Amplifier]] · Next: [[T6-Q10 - Difference Amplifier Condition]]

> [!question] Fig. 9: find $V_0$ and $i_0$. A 3 V source drives a 2 kΩ resistor to the inverting node $v_a$ and a 5 kΩ resistor to the non-inverting node $v_b$; 10 kΩ from $v_b$ to ground; 8 kΩ feedback; 4 kΩ load. *[$V_0=-2$ V, $i_0=-1$ mA]*

**Tests:** ideal op-amp rules with both inputs driven; KCL.

## Given
Source 3 V; $R=2$ kΩ ($v_a$), $5$ kΩ ($v_b$), $10$ kΩ ($v_b$ to ground), $8$ kΩ (feedback), $4$ kΩ (load).

## Principle and why it applies
No current enters the inputs, so $v_b$ is a pure voltage divider, and negative feedback forces $v_a=v_b$.

![[T6-Q9-circuit.png]]

## Solution
1. Divider at the $+$ input: $v_b=3\times\dfrac{10}{5+10}=2$ V.
2. Virtual short: $v_a=v_b=2$ V.
3. KCL at $v_a$ (no input current): $\dfrac{3-v_a}{2\ \text{k}}=\dfrac{v_a-V_0}{8\ \text{k}}$, i.e. $\dfrac{3-2}{2}=\dfrac{2-V_0}{8}$ mA, so $2-V_0=4$, $\boxed{V_0=-2\ \text{V}}$.
4. Currents at the output: through the load, $\dfrac{V_0}{4\ \text{k}}=-0.5$ mA (downwards). Through the feedback resistor, $\dfrac{v_a-V_0}{8\ \text{k}}=\dfrac{4}{8}=0.5$ mA flows **into** the output node from $v_a$.
KCL at the output node: the op-amp output current $i_0=\dfrac{V_0}{4\,\text{k}}-\dfrac{v_a-V_0}{8\,\text{k}}=-0.5-0.5=-1$ mA.

## Result
$$V_0=-2\ \text{V},\qquad i_0=-1\ \text{mA}$$
($i_0$ is the current the op-amp **output** delivers: it sinks 1 mA, 0.5 mA to the load side and 0.5 mA through the feedback resistor.)

## Check
Node $v_a$ currents: $+0.5$ mA in from the source branch, $0.5$ mA out through the 8 kΩ: balance ✓. The op-amp sinks current at its output: it is pulling the output negative, which matches $V_0<0$. The 4 kΩ load alone would take only $-0.5$ mA; the answer $-1$ mA in the sheet is the *total* output current.

## Trap / alternative
Taking $i_0$ as the load current only ($V_0/4$ k $=-0.5$ mA). The arrow for $i_0$ in the figure is on the op-amp output lead, upstream of the feedback tap, so it includes the feedback current.

## Concepts used
- [[Theory - Operational Amplifiers]] · [[Voltage Divider Rule]]
