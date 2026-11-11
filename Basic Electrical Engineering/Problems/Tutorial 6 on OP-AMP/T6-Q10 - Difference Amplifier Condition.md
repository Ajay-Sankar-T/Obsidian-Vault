---
tags: [EE1100, op-amp, tutorial-solution, difference-amplifier, design]
---

# T6-Q10 — Resistor Condition for $V_o=V_2-V_1$

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q9 - Differential Circuit Analysis]] · Next: [[T6-Q11 - Design for z = 2x - 3y]]

> [!question] Fig. 10: find the condition on the resistances for $v_0=v_2-v_1$. ($v_1$ through $R_1$ to the inverting input, feedback $R_2$; $v_2$ through $R_3$ to the non-inverting input, $R_4$ to ground; load $R_L$.)

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|difference amplifier]], superposition, design condition.

## Given
General resistors $R_1,R_2,R_3,R_4$; ideal op-amp (so $R_L$ does not matter: the output is a voltage source).

## Principle and why it applies
Superposition on the linear network, with the ideal-op-amp rules for each source separately.

## Solution
- $v_2=0$: inverting stage, $v_0'=-\dfrac{R_2}{R_1}v_1$.
- $v_1=0$: $v_+=\dfrac{R_4}{R_3+R_4}v_2$ and non-inverting gain $1+\dfrac{R_2}{R_1}$, so $v_0''=\Big(1+\dfrac{R_2}{R_1}\Big)\dfrac{R_4}{R_3+R_4}v_2$.
$$v_0=\Big(1+\frac{R_2}{R_1}\Big)\frac{R_4}{R_3+R_4}v_2-\frac{R_2}{R_1}v_1.$$
**Condition for equal and opposite weights:** the coefficient of $v_2$ must equal that of $-v_1$:
$$\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}=\frac{R_2}{R_1}\ \Longrightarrow\ R_1R_4+R_2R_4=R_2R_3+R_2R_4\ \Longrightarrow\ \boxed{\frac{R_2}{R_1}=\frac{R_4}{R_3}}$$
Then $v_0=\dfrac{R_2}{R_1}(v_2-v_1)$. For **unit** gain, $v_0=v_2-v_1$ exactly:
$$\boxed{R_1=R_2,\quad R_3=R_4}.$$

![[T6-Q10-Q11-circuits.png]]

## Result
$v_0=v_2-v_1$ requires $\dfrac{R_2}{R_1}=\dfrac{R_4}{R_3}=1$, i.e. $R_1=R_2$ and $R_3=R_4$ (any $R_L$).

## Check
With $R_1=R_2=R_3=R_4=R$: $v_+=v_2/2$, non-inverting gain $2$ gives $v_2$; inverting stage gives $-v_1$ ✓. With unequal ratios, a common-mode input ($v_1=v_2=v$) gives $v_0\ne0$: the circuit then also amplifies the common-mode voltage.

## Trap / alternative
Requiring $R_1=R_3$ and $R_2=R_4$ is a **sufficient** special case but not necessary: only the ratios need to match ($R_2/R_1=R_4/R_3$) for a pure difference; the second condition fixes the gain.

## Concepts used
- [[Theory - Operational Amplifiers]] · [[Voltage Divider Rule]]
