---
tags: [EE1100, op-amp, tutorial-solution, design, analog-computer]
---

# T6-Q11 — Op-Amp Circuit for $z=2x-3y$

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q10 - Difference Amplifier Condition]] · Next: [[T6-Q12 - Weighing Summer]]

> [!question] A physical system is described by $z=2x-3y$ where $x,y$ are voltages within the op-amp's range. Draw an op-amp circuit with $z$ as the output, using standard resistor values.

**Tests:** [[T6-Q10 - Difference Amplifier Condition|difference-amplifier weights]], [[Theory - Operational Amplifiers|summer / subtractor design]].

## Given
Output $z=2x-3y$: weight $+2$ on $x$, $-3$ on $y$.

## Principle and why it applies
In the difference amplifier the inverting input has weight $-R_2/R_1$ and the non-inverting input has weight $\big(1+\frac{R_2}{R_1}\big)\frac{R_4}{R_3+R_4}$, so both weights are set by resistor ratios. The two weights are independent knobs: $R_2/R_1$ and $R_4/(R_3+R_4)$.

## Solution
**One-stage design.**
1. $y$ goes to the inverting input with weight $-3$: $\dfrac{R_2}{R_1}=3$. Take $R_1=10$ kΩ, $R_2=30$ kΩ (both standard E24 values).
2. $x$ goes to the non-inverting input with weight $+2$: $\Big(1+\dfrac{R_2}{R_1}\Big)\dfrac{R_4}{R_3+R_4}=4\cdot\dfrac{R_4}{R_3+R_4}=2\Rightarrow\dfrac{R_4}{R_3+R_4}=\dfrac12\Rightarrow R_3=R_4$. Take $R_3=R_4=10$ kΩ.
$$z=4\cdot\tfrac12\,x-3y=2x-3y\ \checkmark$$

![[T6-Q10-Q11-circuits.png]]

**Alternative (two op-amps, easier to adjust the weights independently).** Stage 1: inverting amplifier on $x$ with gain $-2$ ($R=10$ kΩ in, $20$ kΩ feedback) gives $-2x$. Stage 2: inverting summer with $R_f=30$ kΩ, the output of stage 1 through $30$ kΩ (weight 1) and $y$ through $10$ kΩ (weight 3): $z=-\big(1\cdot(-2x)+3y\big)=2x-3y$. The one-stage circuit saves an op-amp but ties the $x$ weight to the $y$ weight through $R_2/R_1$.

## Result
**One op-amp difference amplifier:** $R_1=10$ kΩ, $R_2=30$ kΩ (on $y$), $R_3=R_4=10$ kΩ (on $x$): $z=2x-3y$.

## Check
$x=1$, $y=0$: $v_+=0.5$, gain $1+3=4$, $z=2$ ✓. $x=0$, $y=1$: $z=-3$ ✓. Source loading: $x$ sees $R_3+R_4=20$ kΩ, $y$ sees $R_1=10$ kΩ: sources must have much lower output resistance (or add voltage followers).

## Trap / alternative
Setting $R_3=R_4$ out of habit (from the unit-gain subtractor) gives the $x$-weight $\frac12\big(1+\frac{R_2}{R_1}\big)$, which equals 2 here only because $R_2/R_1=3$. In general solve the two weights separately. Also note the limitation of one stage: the $x$-weight is $\big(1+\frac{R_2}{R_1}\big)\frac{R_4}{R_3+R_4}$, so for a given $y$-weight it can be made anything from 0 up to $1+\frac{R_2}{R_1}$, but never above that.

## Concepts used
- [[Theory - Operational Amplifiers]]
