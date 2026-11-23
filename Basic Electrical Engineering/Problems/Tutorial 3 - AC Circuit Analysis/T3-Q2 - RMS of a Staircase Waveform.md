---
tags: [EE1100, tutorial-solution, AC-circuits, rms, waveforms, power]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q2: RMS of a Staircase Waveform, and the Power It Dissipates

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Sinusoidal Waveforms, RMS and Average Value]] · Previous: [[T3-Q1 - Average and RMS of Square Waves]] · Next: [[T3-Q3 - RL Series Circuit Impedance]]

> [!question] A voltage wave steps through $0\to10\to20$ V (each for 1 s, repeating every 3 s). Find the average and rms values; if applied to $10\ \Omega$, the power dissipated. *[Sheet: $V_{avg}=10$ V, $V_{rms}=10\sqrt{15}/3=12.909$ V, $P=16.667$ W]*

**Tests:** rms of a piecewise-constant wave, power in a resistor from the rms value.

## Given
Period $T=3$ s: $v=0$ on $0<t<1$, $v=10$ V on $1<t<2$, $v=20$ V on $2<t<3$. Load $R=10\ \Omega$.

## Principle and why it applies
For a piecewise-constant waveform the integrals reduce to sums over segments weighted by their duration. The power in a resistor depends on the **mean square**, $P=\dfrac{V_{rms}^2}{R}$, which is exactly what the rms value packages. (The average value is only the DC component, not the heating.)

## Diagram
![[T3-Q1-Q2-waveforms.png]]

## Solution
$$V_{avg}=\frac{0\cdot1+10\cdot1+20\cdot1}{3}=\mathbf{10\ V},$$
$$V_{rms}^2=\frac{0^2\cdot1+10^2\cdot1+20^2\cdot1}{3}=\frac{500}{3}=166.67\ \text{V}^2\ \Rightarrow\ V_{rms}=\sqrt{166.67}=\mathbf{12.91\ V}=\frac{10\sqrt{15}}{3}.$$
$$P=\frac{V_{rms}^2}{R}=\frac{166.67}{10}=\mathbf{16.67\ W}.$$

## Result
$$\boxed{V_{avg}=10\ \text{V},\quad V_{rms}=12.91\ \text{V},\quad P=16.67\ \text{W}}$$

## Check
Time-average of the instantaneous power: $\dfrac1T\sum\dfrac{v^2}{R}\Delta t=\dfrac{1}{3}\Big[\dfrac{0}{10}+\dfrac{100}{10}+\dfrac{400}{10}\Big]=\dfrac{50}{3}=16.67$ W ✓. And $V_{rms}^2=V_{avg}^2+\sigma^2$ with variance $\sigma^2=\tfrac13[(−10)^2+0+10^2]=66.7$: $100+66.7=166.7$ ✓.

## Trap / alternative
Using $V_{avg}^2/R=100/10=10$ W for the power is the classic error: it ignores the AC component and **underestimates** the heating ($10$ W against $16.67$ W). Likewise $\sqrt{(0+10+20)/3}$ is not the rms. Always average the *squares*.

## Concepts used
- RMS of a general periodic waveform, power in a resistor ([[Sinusoidal Waveforms, RMS and Average Value]], [[AC Power and Power Factor]])
