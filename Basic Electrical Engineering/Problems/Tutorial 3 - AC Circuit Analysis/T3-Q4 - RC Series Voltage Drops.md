---
tags: [EE1100, tutorial-solution, AC-circuits, impedance, RC-circuit, phasors]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q4: Voltage Drops in an RC Series Circuit from the Phase Angle

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Impedance and Series-Parallel AC Circuits]], [[Phasors and Complex Algebra]] · Previous: [[T3-Q3 - RL Series Circuit Impedance]] · Next: [[T3-Q5 - RC Circuit Power and Power Factor]]

> [!question] An RC series circuit is driven by $170\sin\omega t$ V and the steady-state current leads the voltage by $30^\circ$. Find the effective voltage drops across the resistive and reactive elements. *[Sheet: $\bar V_R=104.103\angle30^\circ$ V, $\bar V_{X_C}=60.14\angle-60^\circ$ V]*

**Tests:** [[Impedance and Series-Parallel AC Circuits|phasor voltage triangle]]; $V_R$ in phase with $I$, $V_C$ lagging $I$ by $90^\circ$.

## Given
$e(t)=170\sin\omega t$ (peak 170 V, so rms $V=170/\sqrt2=120.2$ V), $I$ leads $V$ by $30^\circ$. Neither $R$, $C$ nor $\omega$ is given: the **angle alone** fixes the split.

## Principle and why it applies
In a series circuit the same current flows in both elements. $V_R$ is **in phase with $I$**, $V_C$ **lags $I$ by $90^\circ$**, and KVL says the phasor sum is the source: $\bar V=\bar V_R+\bar V_C$. So $\bar V_R$ and $\bar V_C$ are the two legs of a **right triangle** with hypotenuse $\bar V$, and the angle between $V$ and $I$ (which is $-30^\circ$ relative to $I$) fixes both legs.

## Diagram
![[T3-Q4-Q6-Q7-phasors.png]]

## Solution
Take $\bar V=120.2\angle0^\circ$ as reference, so $\bar I$ is at $+30^\circ$.
$$V_R=V\cos30^\circ=120.2\times0.866=104.1\ \text{V},\qquad \bar V_R=104.1\angle+30^\circ\ \text{V}\ (\text{same angle as }I),$$
$$V_C=V\sin30^\circ=120.2\times0.5=60.1\ \text{V},\qquad \bar V_C=60.1\angle(30^\circ-90^\circ)=60.1\angle-60^\circ\ \text{V}.$$

## Result
$$\boxed{\bar V_R=104.1\angle30^\circ\ \text{V},\qquad \bar V_{X_C}=60.1\angle-60^\circ\ \text{V}}$$
(effective values; the sheet prints $60.14$ V, exactly $60.10$ V.)

## Check
Phasor sum in rectangular form: $104.1\angle30^\circ=90.15+j52.05$ and $60.1\angle-60^\circ=30.05-j52.05$; the sum is $120.2+j0$ ✓ $=\bar V$. The magnitudes obey $V^2=V_R^2+V_C^2$: $104.1^2+60.1^2=14\,450=120.2^2$ ✓. Also $X_C/R=\tan30^\circ=0.577$ and $pf=\cos30^\circ=0.866$ leading.

## Trap / alternative
- **Effective** means rms: divide the 170 V peak by $\sqrt2$ *before* splitting.
- The *scalar* sum $104.1+60.1=164.2$ V does not equal the source; voltages in $R$ and $C$ add as phasors, 90° apart.
- If the current *lagged* by $30^\circ$ the element would be inductive and $\bar V_L$ would be at $+120^\circ$.

## Concepts used
- Series impedance, phasor diagram, rms ([[Impedance and Series-Parallel AC Circuits]], [[Phasors and Complex Algebra]])
