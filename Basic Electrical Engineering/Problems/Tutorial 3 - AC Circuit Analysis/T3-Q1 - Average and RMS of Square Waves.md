---
tags: [EE1100, tutorial-solution, AC-circuits, rms, waveforms]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q1: Average and RMS of Square Waves

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Sinusoidal Waveforms, RMS and Average Value]] · Next: [[T3-Q2 - RMS of a Staircase Waveform]]

> [!question] Find the average and effective (rms) values of each wave-shape: (a) a square wave switching between $+I_m$ and $-I_m$ with 50 % duty; (b) a unipolar rectangular wave between $0$ and $I_m$ with 50 % duty. *[Sheet: (a) $I_{avg}=0$, $I_{rms}=I_m$; (b) $I_{avg}=I_m/2$, $I_{rms}=I_m/\sqrt2$]*

**Tests:** definitions of average and rms values, [[Sinusoidal Waveforms, RMS and Average Value]].

## Given
Period $T$. (a) $i=+I_m$ for $0<t<T/2$ and $-I_m$ for $T/2<t<T$. (b) $i=I_m$ for $0<t<T/2$ and $0$ for $T/2<t<T$.

## Principle and why it applies
$$I_{avg}=\frac1T\int_0^Ti\,dt\quad(\text{the DC component}),\qquad I_{rms}=\sqrt{\frac1T\int_0^Ti^2\,dt}.$$
The rms is defined by *heating*: the rms value of a current is the DC current that dissipates the same average power in a resistor, $P=I_{rms}^2R=\dfrac1T\displaystyle\int i^2R\,dt$. That is why it is built from $i^2$ (always positive), while the average keeps the sign.

## Diagram
![[T3-Q1-Q2-waveforms.png]]

## Solution
**(a)** $\displaystyle I_{avg}=\frac1T\Big[I_m\frac T2-I_m\frac T2\Big]=\mathbf{0}$. Since $i^2=I_m^2$ at every instant, $\displaystyle I_{rms}=\sqrt{\frac1T\,I_m^2T}=\mathbf{I_m}$.

**(b)** $\displaystyle I_{avg}=\frac1T\Big[I_m\frac T2\Big]=\frac{I_m}{2}$. $\ \displaystyle I_{rms}=\sqrt{\frac1T\,I_m^2\frac T2}=\frac{I_m}{\sqrt2}$.

## Result
$$\boxed{\text{(a) }I_{avg}=0,\ I_{rms}=I_m;\qquad\text{(b) }I_{avg}=\frac{I_m}2,\ I_{rms}=\frac{I_m}{\sqrt2}}$$

## Check
Wave (b) is wave (a) shifted up by $I_m/2$ and halved in amplitude: $\tfrac{I_m}2+\tfrac{I_m}2\,\text{sq}(t)$. Its rms must satisfy $I_{rms}^2=I_{avg}^2+(\text{rms of the AC part})^2=\big(\tfrac{I_m}2\big)^2+\big(\tfrac{I_m}2\big)^2=\tfrac{I_m^2}{2}$ ✓. (A pure sinusoid of amplitude $I_m$ also has $I_{rms}=I_m/\sqrt2$, the same *heating* as wave (b), but a different shape.)

## Trap / alternative
- **Average over a full cycle of a symmetric AC wave is zero**; for rectified waves quote the average of the *rectified* wave (which for (a) would be $I_m$). The question wants the plain average.
- Never average first and square: $I_{rms}\neq I_{avg}$; $I_{rms}^2$ is the average of the square.
- For (b) the *form factor* $I_{rms}/I_{avg}=\sqrt2$ and for (a) it is undefined (zero average).

## Concepts used
- Average and rms of periodic waveforms ([[Sinusoidal Waveforms, RMS and Average Value]])
