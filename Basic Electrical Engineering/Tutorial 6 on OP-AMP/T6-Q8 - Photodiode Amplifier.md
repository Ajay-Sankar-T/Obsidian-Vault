---
tags: [EE1100, op-amp, tutorial-solution, photodiode, transimpedance]
---

# T6-Q8 — Photodiode Amplifier

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q7 - Follower with Finite Gain]] · Next: [[T6-Q9 - Differential Circuit Analysis]]

> [!question] A photodiode has a sensitivity of 10 µA per mW of incident radiation. In the circuit of Fig. 8, if $V_0=8$ V, find the input radiation power. $R_f=10$ kΩ, $R_1=75\ \Omega$, $R_2=1$ kΩ. *[sheet answer: "6 Watt"]*

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|transimpedance amplifier]], cascaded inverting stages.

## Given
Stage 1: photodiode current $i_i$ into the inverting node, $R_f=10$ kΩ. Stage 2: inverting amplifier $R_1=75\ \Omega$ in, $R_2=1$ kΩ feedback. Responsivity $10\ \mu\text{A/mW}$, $V_0=8$ V.

## Principle and why it applies
The first op-amp holds its inverting node at virtual ground, so all of the photocurrent flows through $R_f$: $V_1=-R_fi_i$. The second stage is a standard inverting amplifier of gain $-R_2/R_1$.

![[T6-Q8-circuit.png]]

## Solution
$$V_0=-\frac{R_2}{R_1}V_1=\frac{R_2}{R_1}R_fi_i=\frac{1000}{75}(10\ \text{k}\Omega)\,i_i=133.3\ \text{k}\Omega\times i_i.$$
$$i_i=\frac{8\ \text{V}}{133.33\ \text{k}\Omega}=60\ \mu\text{A},\qquad P=\frac{60\ \mu\text{A}}{10\ \mu\text{A/mW}}=6\ \text{mW}.$$

## Result
$$i_i=60\ \mu\text{A}\ \Rightarrow\ P=\boxed{6\ \text{mW}}$$

## Check
$V_1=-60\ \mu\text{A}\times10\ \text{k}\Omega=-0.6$ V; second stage gain $-13.33$: $V_0=+8$ V ✓. The sheet states "6 Watt": that is a **unit slip**. 60 µA at 10 µA/mW is 6 mW; 6 W would need 60 A of photocurrent.

## Trap / alternative
Forgetting that the two stages **multiply** (and both invert, giving a positive output). The first stage alone gives only $-0.6$ V. Do not include a series resistor in the first stage: the photodiode is a current source, so the first stage's gain is $R_f$ (in V/A), not a dimensionless ratio.

## Concepts used
- [[Theory - Operational Amplifiers]]
