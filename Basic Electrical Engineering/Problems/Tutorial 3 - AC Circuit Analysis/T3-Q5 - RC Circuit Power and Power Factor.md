---
tags: [EE1100, tutorial-solution, AC-circuits, impedance, power, power-factor]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q5: RC Series Circuit: Impedance, Current, Power and Capacitance

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[AC Power and Power Factor]], [[Impedance and Series-Parallel AC Circuits]] · Previous: [[T3-Q4 - RC Series Voltage Drops]] · Next: [[T3-Q6 - Adding Parallel Branch Currents]]

> [!question] A circuit has $R=6\ \Omega$ in series with a capacitive reactance of $8\ \Omega$; $e(t)=141\sin377t$. (a) Complex impedance. (b) rms and instantaneous current. (c) Power factor and power delivered. (d) The capacitance. *[Sheet: $Z=6-j8=10\angle-53.13^\circ$; $I_{rms}=9.97$ A, $i=14.1\sin(377t+53.13^\circ)$; $pf=0.596$ leading, $S=596.41-j795.2$ VA; $C=331.56\ \mu$F]*

**Tests:** [[Impedance and Series-Parallel AC Circuits|series RC impedance]], complex power $\bar S=\bar V\bar I^*$, [[AC Power and Power Factor|power factor]].

## Given
$R=6\ \Omega$, $X_C=8\ \Omega$ (so $Z_C=-j8\ \Omega$), $e(t)=141\sin377t$: $V_m=141$ V, $V_{rms}=141/\sqrt2=99.7$ V, $\omega=377$ rad/s.

## Principle and why it applies
A capacitor's impedance is $-jX_C$ (current leads voltage by $90^\circ$), so a series RC has a **negative** impedance angle and the current **leads** the voltage by that angle. Real power is dissipated only in $R$ ($P=I^2R$); the capacitor supplies reactive power, counted **negative** ($Q=-I^2X_C$) in the convention where inductive $Q$ is positive. So $\bar S=P+jQ$ has a negative imaginary part.

## Solution
**(a)** $Z=6-j8=\mathbf{10\angle-53.13^\circ\ \Omega}$.

**(b)** $I_{rms}=\dfrac{V_{rms}}{|Z|}=\dfrac{99.7}{10}=\mathbf{9.97\ A}$; peak $I_m=14.1$ A. The current leads the voltage by $53.13^\circ$:
$$\mathbf{i(t)=14.1\sin(377t+53.13^\circ)\ A}.$$

**(c)** The power factor is $\cos\phi=\dfrac{R}{|Z|}=\dfrac{6}{10}=\mathbf{0.6\ leading}$ (the sheet prints $0.596$, which looks like $P/1000$ rather than $P/|S|$; the exact value is $0.600$). Powers:
$$P=I_{rms}^2R=9.97^2\times6=596.4\ \text{W},\qquad Q=-I_{rms}^2X_C=-9.97^2\times8=-795.2\ \text{VAr},$$
$$\bar S=\bar V\bar I^*=99.7\angle0^\circ\times9.97\angle-53.13^\circ=\mathbf{596.4-j795.2\ VA},\qquad |S|=994\ \text{VA}.$$

**(d)** $X_C=\dfrac1{\omega C}\Rightarrow C=\dfrac1{377\times8}=\mathbf{331.6\ \mu F}$.

## Result
$$\boxed{Z=10\angle-53.13^\circ\ \Omega;\ I_{rms}=9.97\ \text{A};\ pf=0.6\ \text{leading};\ \bar S=596.4-j795.2\ \text{VA};\ C=331.6\ \mu\text{F}}$$

## Check
$pf=P/|S|=596.4/994=0.600$ ✓. $\sqrt{596.4^2+795.2^2}=994$ ✓. The sign of $Q$ matches a capacitive load, and $\tan\phi=Q/P=-1.333=-8/6$ ✓.

## Trap / alternative
- **Leading versus lagging** must always be stated: $\cos\phi=0.6$ alone is ambiguous. A capacitive circuit has a *leading* power factor.
- Use **rms** in $P=VI\cos\phi$; using peak values overstates power by 2.
- Only $R$ dissipates, so $P=I^2R$ is a shortcut that avoids the angle altogether.

## Concepts used
- Series RC impedance, complex power, power factor ([[AC Power and Power Factor]], [[Impedance and Series-Parallel AC Circuits]])
