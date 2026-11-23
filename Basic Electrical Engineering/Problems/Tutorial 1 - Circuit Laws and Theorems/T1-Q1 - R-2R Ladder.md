---
tags: [EE1100, tutorial-solution, DC-circuits, resistor-networks]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q1: The R-2R Ladder

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Next: [[T1-Q2 - KVL with Three Batteries]]

> [!question] The R-2R network used in D-A converters is driven by $V_R$. Find $V_1,V_2,V_3,V_4$ in terms of $V_R$, the input resistance $R_{in}$, and $I_1,\dots,I_4$. *[Sheet: $V_R,\ V_R/2,\ V_R/4,\ V_R/8$; $R_{in}=2R$; $V_R/2R,\ V_R/4R,\ V_R/8R,\ V_R/16R$]*

**Tests:** [[Series-Parallel Resistance Reduction]], [[Voltage Divider Rule]], KCL.

## Given
Source $V_R$ across the input. Series arms $R$ (carrying $I_1\ldots I_4$), shunt legs $2R,2R,2R$ at nodes $V_2,V_3,V_4$, and a final resistor $R$ at the far end. All values in terms of $R$.

## Principle and why it applies
The network is a **ladder**: the same two-resistor cell repeats. The efficient method is to **reduce from the far end towards the source**, replacing everything to the right of a node by one equivalent resistance, then to **work forward** with Ohm's law and KVL. The point of the R-2R design is that the equivalent resistance looking right from *every* node is the same, $R$ at the shunt nodes, so each node splits its current in half.

## Diagram
![[T1-Q1-circuit.png]]

## Solution
**Step 1, reduce from the right.** At node $V_4$: the shunt $2R$ is in parallel with ($R$ in series with $R$) $=2R$:
$$2R\parallel 2R=R.$$
At node $V_3$: the arm $R$ in series with that $R$ gives $2R$, in parallel with the shunt $2R$ gives $R$ again. Same at $V_2$. Finally from the source: the first arm $R$ in series with $R$:
$$\boxed{R_{in}=R+R=2R}$$

**Step 2, work forward.** The source current is
$$I_1=\frac{V_R}{R_{in}}=\frac{V_R}{2R}.$$
Voltage at the next node: $V_2=V_R-I_1R=\dfrac{V_R}{2}$. Node $V_2$ sees the shunt $2R$ in parallel with the rest of the ladder $2R$, so $I_1$ splits equally, or directly $I_2=V_2/(R+R)=V_R/4R$. Repeating:
$$V_3=V_2-I_2R=\frac{V_R}{4},\ \ I_3=\frac{V_3}{2R}=\frac{V_R}{8R},\qquad V_4=V_3-I_3R=\frac{V_R}{8},\ \ I_4=\frac{V_4}{2R}=\frac{V_R}{16R}.$$

## Result
$$V_1=V_R,\ V_2=\tfrac{V_R}{2},\ V_3=\tfrac{V_R}{4},\ V_4=\tfrac{V_R}{8};\qquad R_{in}=2R;\qquad I_k=\frac{V_R}{2^{k}R}.$$

## Check
KCL at $V_2$: $I_1=\dfrac{V_2}{2R}+I_2\Rightarrow \dfrac{V_R}{2R}=\dfrac{V_R}{4R}+\dfrac{V_R}{4R}$ ✓. Power: source $V_RI_1=V_R^2/2R$; dissipated in the arms and shunts adds to the same.

## Trap / alternative
- Looking at the ladder **from the source side** gives an ever-growing nested fraction; always start from the far end.
- Alternatively use the divider rule at each node: $V_{k+1}=V_k\cdot\dfrac{R_{\text{right}}}{R+R_{\text{right}}}=V_k\cdot\dfrac{R}{R+R}$ with $R_{\text{right}}=R$ at every shunt node. Each node halves the voltage: this is exactly why a ladder DAC produces **binary-weighted** voltages and currents.

## Concepts used
- [[Series-Parallel Resistance Reduction]] · [[Voltage Divider Rule]] · KCL ([[Theory - Circuit Laws and Network Theorems]])
