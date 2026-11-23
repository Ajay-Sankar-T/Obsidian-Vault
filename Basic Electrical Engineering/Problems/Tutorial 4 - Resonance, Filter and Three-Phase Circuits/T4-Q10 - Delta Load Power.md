---
tags: [EE1100, tutorial-solution, three-phase, delta-connection, power]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q10 - Delta Load Power"]
---

# T4-Q10: Delta Load, Phase and Line Currents, and Why Their Sum Is Zero

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Three-Phase Circuits]] · Previous: [[T4-Q9 - Balanced Delta Load]] · Next: [[T4-Q11 - Star Load Impedance from Power]]

> [!question] The delta-connected load of Fig. 1 (same arrangement as Q9, 220 V line-to-line) has a phase impedance of $15+j20\ \Omega$ in each phase. (a) Find the phasor current in each line. (b) The power consumed per phase. (c) The phasor sum of the three line currents, and why. *[Sheet: $8.8\angle-53.13^\circ$, $8.8\angle-173.13^\circ$, $8.8\angle66.86^\circ$ A; $1161.6$ W, $1548.8$ VAr; $0$ A. The three currents the sheet prints are the **phase** currents; see below.]*

**Tests:** [[Theory - Three-Phase Circuits#3. Delta (Δ) connection|delta connection]], phase versus line current, the zero-sum property of balanced three-phase quantities.

## Given
$Z_p=15+j20=25\angle53.13^\circ\ \Omega$ in each delta arm. The question does not restate the supply; the printed answers imply the same $V_L=220$ V as Q9, which is assumed here ($\bar V_{ab}=220\angle0^\circ$, abc sequence).

## Principle and why it applies
In a delta, each arm is across a line voltage, so $I_p=V_L/|Z_p|$ and the line current is $\sqrt3I_p$ at $-30^\circ$ from the phase current. Balanced three-phase quantities are three equal-magnitude phasors $120^\circ$ apart, whose sum is **zero**.

## Diagram
![[T4-Q9-Q10-Q12-phasors.png]]

## Solution
**(a) Phase currents:** $I_p=\dfrac{220}{25}=8.8$ A, lagging $\bar V_{ab}$ by $53.13^\circ$:
$$\bar I_{ab}=8.8\angle-53.13^\circ,\quad\bar I_{bc}=8.8\angle-173.13^\circ,\quad\bar I_{ca}=8.8\angle+66.87^\circ\ \text{A}$$
(these are exactly the three phasors the sheet lists). **Line currents** $\bar I_a=\bar I_{ab}-\bar I_{ca}=\sqrt3\,\bar I_{ab}\angle-30^\circ$:
$$\bar I_a=15.24\angle-83.13^\circ,\quad\bar I_b=15.24\angle-203.13^\circ\ (=156.87^\circ),\quad\bar I_c=15.24\angle-323.13^\circ\ (=36.87^\circ)\ \ \text{A}.$$

**(b) Power per phase:**
$$P_{ph}=I_p^2R=8.8^2\times15=\mathbf{1161.6\ W},\qquad Q_{ph}=I_p^2X=8.8^2\times20=\mathbf{1548.8\ VAr\ (lag)},$$
so $S_{ph}=1936$ VA, $pf=0.6$ lagging. (Total: $P=3485$ W, $Q=4646$ VAr, $S=5808$ VA $=\sqrt3\,V_LI_L$ ✓.)

**(c)** $\bar I_a+\bar I_b+\bar I_c=\mathbf{0}$. *Why:* the three line currents are equal in magnitude and $120^\circ$ apart, $15.24\,[1\angle\theta+1\angle(\theta-120^\circ)+1\angle(\theta+120^\circ)]=0$; equivalently, by KCL on the delta (no neutral) the three line currents must sum to zero. This is why a balanced three-wire system needs no neutral conductor.

## Result
$$\boxed{I_p=8.8\ \text{A},\ I_L=15.24\ \text{A};\ \ P_{ph}=1161.6\ \text{W},\ Q_{ph}=1548.8\ \text{VAr};\ \ \bar I_a+\bar I_b+\bar I_c=0}$$

## Check
The sheet quotes the **phase** currents under the heading "line current": a delta line current must be $\sqrt3$ larger (15.24 A), and it is $I_L=S/(\sqrt3V_L)=5808/(\sqrt3\times220)=15.24$ A ✓. Powers: $3\times1161.6=3485$ W $=\sqrt3\times220\times15.24\times0.6$ ✓.

## Trap / alternative
If the question asks for **line** currents in a delta circuit, give $\sqrt3I_p$ with a $30^\circ$ shift, not $I_p$. The assumption $V_L=220$ V must be stated because the problem does not supply it here. The star equivalent confirms it: $Z_Y=Z_\Delta/3=5+j6.67\ \Omega$ ($|Z_Y|=8.33\ \Omega$), $V_{an}=220/\sqrt3=127$ V, so $I_L=127/8.33=15.24$ A ✓.

## Concepts used
- Delta connection, line/phase currents, balanced-phasor sum ([[Theory - Three-Phase Circuits]], [[09 Three Phase Circuits and Power Measurement]])
