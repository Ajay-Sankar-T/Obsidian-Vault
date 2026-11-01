---
tags: [EE1100, op-amp, tutorial-solution, amplifier, linearity]
---

# T6-Q1 — Amplifier Gain, Linearity and Design

Hub: [[Tutorial 6 on OP-AMP]] · Next: [[T6-Q2 - Inverting Amplifier]] · Theory: [[Theory - Operational Amplifiers]]

> [!question] The input and output of an amplifier are shown (Fig. 1): the input is a triangular wave between 0 and 2 mV, the output the same shape between 0 and 4 V. Find the voltage gain. Is it linear? Design the op-amp circuit with suitable components. *[Gain 2000; linear]*

**Tests:** voltage gain from waveforms, linearity, [[Theory - Operational Amplifiers#3. The standard circuits|non-inverting amplifier]], choosing resistors.

## Given
$v_i$: $0\to2$ mV, $v_o$: $0\to4$ V, same times of the peaks and zeros ($t=0,1,2,4,5\ \mu$s).

## Principle and why it applies
Gain $=v_o/v_i$ read at corresponding instants. An amplifier is **linear** if $v_o=Av_i$ with a constant $A$ at every instant (the output is a scaled copy; superposition holds). The output has the **same polarity** and shape as the input, so the stage is non-inverting.

## Solution
**Gain.** Peak: $\dfrac{4\ \text{V}}{2\ \text{mV}}=2000$. Mid-points agree: at the time when $v_i=1$ mV, $v_o=2$ V, ratio 2000.

**Linearity.** The pairs $(0,0)$, $(1,2000)$, $(2,4000)$ mV lie on a straight line through the origin, and the output follows every straight segment of the input with the same ratio. So $v_o=2000\,v_i$ at all instants: **linear** (no distortion, no offset, no clipping since 4 V is within the supply rail).

**Design.** Non-inverting amplifier with $A=1+\dfrac{R_f}{R_g}=2000$, so $R_f=1999\,R_g$. Take $R_g=1\ \text{k}\Omega$: $R_f=1.999\ \text{M}\Omega$. With the standard value $R_f=2\ \text{M}\Omega$ the gain is $2001$ (0.05 % error).

![[T6-Q1-design.png]]
![[T6-Q1-waveforms.png]]

## Result
**Gain $=2000$, linear.** Design: non-inverting op-amp, $R_g=1\ \text{k}\Omega$, $R_f\approx2\ \text{M}\Omega$ (or $1.999$ M).

## Check
Output swing $2000\times2\ \text{mV}=4$ V ✓. A $\pm12$ V supply leaves room. The ideal-op-amp assumption needs the open-loop gain $A\gg2000$.

## Trap / alternative
- A single stage of gain 2000 needs a gain–bandwidth product above $2000\times$ the signal bandwidth. The waveform has 1 µs edges (bandwidth about 0.35 MHz), so a real 1 MHz op-amp would not deliver this gain; in practice split into two stages of $\approx45$ each (e.g. $1+\frac{44\,\text{k}}{1\,\text{k}}$ twice, $\approx2025$).
- An **inverting** stage ($-R_f/R_1$) would give the correct magnitude but flip the polarity: the output would go negative.

## Concepts used
- [[Theory - Operational Amplifiers]]
