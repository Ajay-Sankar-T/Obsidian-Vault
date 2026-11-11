---
tags: [EE1100, op-amp, tutorial-solution, design, summing-amplifier, instrumentation]
---

# T6-Q12 — Bridge Weighing Circuit

Hub: [[Tutorial 6 on OP-AMP]] · Previous: [[T6-Q11 - Design for z = 2x - 3y]]

> [!question] A historic bridge allows only cars lighter than 1600 kg. A four-pad weighing system gives four independent voltage signals, one per wheel pad, with 1 mV = 1 kg. Design a circuit that gives a **positive** voltage for a DMM, representing the total weight with 1 mV = 1 kg. The wheel-pad signals need no buffering.

**Tests:** [[Theory - Operational Amplifiers#3. The standard circuits|summing amplifier]], sign and scaling of a design, [[Voltage Divider Rule]].

## Given
$v_1,\dots,v_4$ (mV per kg), want $v_o=v_1+v_2+v_3+v_4$ with a positive sign and unity weight on each.

## Principle and why it applies
The total weight is the **sum** of the four pad voltages, with **gain +1** each. An inverting summer gives $-\sum v_k$ (wrong sign); a **non-inverting summer** gives the right sign in one stage. Equal resistors $R$ from each source to the $+$ input make $v_+$ the **average** of the four (the sources are low-impedance, so the average is not loaded down):
$$v_+=\frac{v_1+v_2+v_3+v_4}{4}\quad(\text{no current into }+\text{ input}),$$
then a non-inverting stage of gain 4 restores the sum.

## Solution
$$v_o=\Big(1+\frac{R_f}{R_g}\Big)v_+=4v_+\quad\Longrightarrow\quad\frac{R_f}{R_g}=3.$$
Standard values: four inputs through $R=10$ kΩ each to the $+$ input; $R_g=10$ kΩ, $R_f=30$ kΩ. Then $v_o=v_1+v_2+v_3+v_4$ (1 mV per kg).

![[T6-Q12-summer.png]]

**Alternative (two inverting stages).** Inverting summer with $R=R_f=10$ kΩ: $-\sum v_k$; followed by an inverter ($10$ kΩ, $10$ kΩ): $+\sum v_k$. This costs two op-amps but each input sees a defined resistance $R$ to a virtual ground, so the channels do not interact.

**Alarm threshold.** $1600$ kg corresponds to $v_o=1.6$ V: a comparator against 1.6 V flags overweight vehicles.

## Result
**Non-inverting summing amplifier:** four $10$ kΩ input resistors to the $+$ terminal, $R_g=10$ kΩ, $R_f=30$ kΩ, giving $v_o=v_1+v_2+v_3+v_4$ (positive, 1 mV/kg); 1600 kg gives 1.6 V.

## Check
Four pads each at 400 mV: $v_+=400$ mV, $v_o=1.6$ V ✓. One pad at 1600 mV, others 0: $v_+=400$ mV, $v_o=1.6$ V ✓ (the circuit weights every pad equally, as required).

## Trap / alternative
- Using an inverting summer alone: the DMM would read $-1.6$ V.
- **Source resistance matters in the non-inverting summer:** the average depends on equal total resistance in each branch, so if the pad sources have different output resistances the weights drift; the problem's "no need to buffer" assumption removes this.

## Concepts used
- [[Theory - Operational Amplifiers]]
