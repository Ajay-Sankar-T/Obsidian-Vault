---
tags: [EE1100, tutorial-solution, AC-circuits, impedance, RL-circuit, phasors]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q3: RL Series Circuit, Complex Impedance and the Applied Voltage

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Impedance and Series-Parallel AC Circuits]], [[Phasors and Complex Algebra]] · Previous: [[T3-Q2 - RMS of a Staircase Waveform]] · Next: [[T3-Q4 - RC Series Voltage Drops]]

> [!question] A circuit has $R=9\ \Omega$ in series with an inductive reactance of $12\ \Omega$. The steady-state current is $i(t)=28.3\sin377t$. (a) Complex impedance? (b) Time expression for the applied voltage? (c) The inductance in henrys? *[Sheet: $Z=9+j12\ \Omega$; $v(t)=424.5\sin(377t+53.13^\circ)$ V; $L=31.83$ mH]*

**Tests:** [[Impedance and Series-Parallel AC Circuits|impedance]] of a series RL, converting a sinusoid to a phasor and back.

## Given
$R=9\ \Omega$, $X_L=12\ \Omega$, $i(t)=28.3\sin(377t)$ A, so $\omega=377$ rad/s ($f=60$ Hz), $I_m=28.3$ A, current phase $0^\circ$.

## Principle and why it applies
In sinusoidal steady state every voltage and current is a sinusoid at the same $\omega$, so each can be represented by a **phasor** (magnitude and phase) and the circuit obeys $\bar V=\bar I\,Z$ with a *complex* $Z=R+jX$. An inductor's impedance is $+jX_L$ (voltage leads current by $90^\circ$), so a series RL has $Z=R+jX_L$ with a **positive** angle, and the applied voltage **leads** the current by that angle.

## Solution
**(a)** $Z=R+jX_L=\mathbf{(9+j12)\ \Omega}=15\angle53.13^\circ\ \Omega$ ($|Z|=\sqrt{81+144}=15$, $\theta=\arctan\frac{12}{9}$).

**(b)** Using peak phasors: $\bar I_m=28.3\angle0^\circ$, so
$$\bar V_m=\bar I_mZ=28.3\times15\ \angle(0^\circ+53.13^\circ)=424.5\angle53.13^\circ\ \text{V}\ \Rightarrow\ \mathbf{v(t)=424.5\sin(377t+53.13^\circ)\ V}.$$
(In rms terms: $I=20\angle0^\circ$ A, $V=300\angle53.13^\circ$ V.)

**(c)** $X_L=\omega L\Rightarrow L=\dfrac{12}{377}=\mathbf{31.83\ mH}$.

## Result
$$\boxed{Z=9+j12\ \Omega=15\angle53.13^\circ\ \Omega;\quad v(t)=424.5\sin(377t+53.13^\circ)\ \text{V};\quad L=31.83\ \text{mH}}$$

## Check
Phase: $\tan\theta=X_L/R=1.333\Rightarrow53.13^\circ$ (inductive, voltage leads). Real power $P=I_{rms}^2R=400\times9=3600$ W and $S=V_{rms}I_{rms}=300\times20=6000$ VA give $pf=0.6$ lagging $=\cos53.13^\circ$ ✓.

## Trap / alternative
- Voltage **leads** current in an inductor; writing $-53.13^\circ$ is the capacitive case.
- Keep **peak** and **rms** straight: the printed $424.5$ V is a peak value ($=15\times28.3$).
- $L$ is $X_L/\omega$ with $\omega=377$ rad/s, not $X_L/f$.

## Concepts used
- Impedance, phasors, inductive reactance ([[Impedance and Series-Parallel AC Circuits]], [[Phasors and Complex Algebra]])
