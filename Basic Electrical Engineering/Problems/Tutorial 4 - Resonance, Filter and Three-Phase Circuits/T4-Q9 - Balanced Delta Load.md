---
tags: [EE1100, tutorial-solution, three-phase, delta-connection, power]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q9 - Balanced Delta Load"]
---

# T4-Q9: Balanced Delta Load: Phase Currents, Line Currents and Power

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Three-Phase Circuits]] · Previous: [[T4-Q8 - FM Receiver Band-Pass Design]] · Next: [[T4-Q10 - Delta Load Power]]

> [!question] A 220 V (line-to-line) three-phase balanced supply feeds a balanced delta load; the phase current between $a$ and $b$ is $\bar I_{ab}=10\angle-30^\circ$ A. (a) Find the phase and line currents and draw the phasor diagram. (b) The total power received. (c) The resistive part of the phase impedance. *[Sheet: $10\angle-30^\circ$, $10\angle-150^\circ$, $10\angle90^\circ$ A; line currents 17.32 A at $-60^\circ,-180^\circ,-300^\circ$; $P=5715.6$ W, $Q=2857.8$ VAr (see note); $R=19.05\ \Omega$]*

**Tests:** [[Theory - Three-Phase Circuits#3. Delta (Δ) connection|delta connection]]: $V_L=V_p$, $I_L=\sqrt3I_p$ with a $30^\circ$ shift; $P=\sqrt3V_LI_L\cos\phi$.

## Given
Balanced delta load, $V_L=V_p=220$ V (so $\bar V_{ab}=220\angle0^\circ$, abc sequence); $\bar I_{ab}=10\angle-30^\circ$ A.

## Principle and why it applies
In a delta each load sits directly across a line-to-line voltage, so the **phase voltage is the line voltage**. The current $\bar I_{ab}$ lags $\bar V_{ab}$ by $30^\circ$, so the phase impedance has angle $+30^\circ$ (inductive). Because the system is balanced, the other phase currents follow by $\mp120^\circ$ and each *line* current is the difference of two phase currents.

## Diagram
![[T4-Q9-Q10-Q12-phasors.png]]

## Solution
**(a) Phase currents** (abc sequence):
$$\bar I_{ab}=10\angle-30^\circ,\quad\bar I_{bc}=10\angle-150^\circ,\quad\bar I_{ca}=10\angle+90^\circ\ \ \text{A}.$$
**Line currents:** $\bar I_a=\bar I_{ab}-\bar I_{ca}=\sqrt3\,\bar I_{ab}\angle-30^\circ$:
$$\bar I_a=17.32\angle-60^\circ,\quad\bar I_b=17.32\angle-180^\circ,\quad\bar I_c=17.32\angle-300^\circ\ (=60^\circ)\ \ \text{A}.$$
(Magnitude $I_L=\sqrt3\times10=17.32$ A; each line current lags its phase current by $30^\circ$.)

**(b) Power.** The phase impedance angle is $\phi=30^\circ$ (the angle between $\bar V_{ab}$ and $\bar I_{ab}$):
$$S=\sqrt3V_LI_L=\sqrt3\times220\times17.32=6600\ \text{VA},$$
$$P=S\cos30^\circ=\mathbf{5715.8\ W}\ (\text{sheet }5715.6),\qquad Q=S\sin30^\circ=\mathbf{3300\ VAr\ (lagging)}.$$
(The sheet's $2857.8$ VAr is exactly $P/2$; with $\phi=30^\circ$ the reactive power is $S\sin30^\circ=3300$ VAr.)

**(c)** $|Z_p|=\dfrac{V_p}{I_p}=\dfrac{220}{10}=22\ \Omega$ at $+30^\circ$: $R=22\cos30^\circ=\mathbf{19.05\ \Omega}$, $X=22\sin30^\circ=11\ \Omega$ (inductive).

## Result
$$\boxed{I_L=17.32\ \text{A};\ \ P=5715.8\ \text{W},\ Q=3300\ \text{VAr}\ (\text{lag});\ \ R_{ph}=19.05\ \Omega,\ X_{ph}=11\ \Omega}$$

## Check
$P=3I_p^2R=3\times100\times19.05=5715$ W ✓. $Q=3I_p^2X=3\times100\times11=3300$ VAr ✓. $\sqrt{5715.8^2+3300^2}=6600$ VA ✓.

## Trap / alternative
- The angle in $P=\sqrt3V_LI_L\cos\phi$ is the **impedance angle $30^\circ$**, even though the line current is at $-60^\circ$ relative to $\bar V_{ab}$; $-60^\circ$ is the angle to a different (line) voltage reference.
- The printed $2857.8$ VAr comes from $P\times0.5$ rather than $P\tan30^\circ=P\times0.577$.
- In a delta the line current is the *larger* one; in a star it equals the phase current.

## Concepts used
- Delta connection, line/phase relations, three-phase power ([[Theory - Three-Phase Circuits]], [[09 Three Phase Circuits and Power Measurement]])
