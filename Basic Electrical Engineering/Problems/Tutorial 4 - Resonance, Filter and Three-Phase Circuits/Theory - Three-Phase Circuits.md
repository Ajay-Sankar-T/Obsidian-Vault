---
tags: [EE1100, tutorial-theory, AC-circuits, three-phase]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
---

# Theory: Balanced Three-Phase Circuits

← up: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits|Tutorial 4]] · lectures: [[Lecture 23 Three-phase Circuits.pdf]], [[Lecture 24 Three-phase Systems (Contd…).pdf]], [[Lecture 25 Three-phase Systems - Examples.pdf]] · week: [[09 Three Phase Circuits and Power Measurement]] · glossary: [[Concepts#Three-Phase Systems|Three-Phase Systems]]

> [!abstract] The idea in one paragraph
> Three sinusoidal sources of equal magnitude, $120^\circ$ apart, driving a balanced load, deliver **constant** instantaneous power and need no return current in the neutral. A balanced problem is solved by analysing **one phase** with ordinary single-phase phasors and writing the other two down by the $\pm120^\circ$ symmetry; the connection (star or delta) only changes how line quantities relate to phase quantities.

## 1. Balanced sources and phase sequence

For the usual positive (**abc**) sequence, phase voltages (line to neutral):
$$\bar V_{an}=V_p\angle0^\circ,\qquad \bar V_{bn}=V_p\angle-120^\circ,\qquad \bar V_{cn}=V_p\angle+120^\circ,\qquad \bar V_{an}+\bar V_{bn}+\bar V_{cn}=0.$$
The vanishing sum is the reason a **balanced** system needs no neutral current, and why in Q10(c) the sum of the line currents is zero.

## 2. Star ($\mathrm Y$) connection
Each load sits between a line and the neutral. **Line current $=$ phase current** ($I_L=I_p$). The **line voltage** is the difference of two phase voltages:
$$\bar V_{ab}=\bar V_{an}-\bar V_{bn}=\sqrt3\,V_p\angle(\theta+30^\circ),\qquad V_L=\sqrt3\,V_p.$$
So in star the line voltages are $\sqrt3$ larger than the phase voltages and lead the corresponding phase voltage by $30^\circ$ (Q11, Q12).

## 3. Delta ($\Delta$) connection
Each load sits between two lines. **Line voltage $=$ phase voltage** ($V_L=V_p$). The **line current** is the difference of two phase currents:
$$\bar I_a=\bar I_{ab}-\bar I_{ca}=\sqrt3\,I_p\angle(\theta_{ab}-30^\circ),\qquad I_L=\sqrt3\,I_p.$$
(Q9, Q10.) A balanced delta load $Z_\Delta$ is equivalent, for the line quantities, to a star load $Z_Y=Z_\Delta/3$ (the same Y–Δ rule as for resistors, [[Theory - Circuit Laws and Network Theorems]] §10).

| | star | delta |
|---|---|---|
| $V_L$ vs $V_p$ | $V_L=\sqrt3V_p$, leads by $30^\circ$ | $V_L=V_p$ |
| $I_L$ vs $I_p$ | $I_L=I_p$ | $I_L=\sqrt3I_p$, lags by $30^\circ$ |
| phase impedance | $Z_p=V_p/I_p=\dfrac{V_L}{\sqrt3\,I_L}$ | $Z_p=V_p/I_p=\dfrac{\sqrt3\,V_L}{I_L}$ |

## 4. Power

For a balanced load with phase impedance angle $\phi$ (the angle between the **phase voltage and phase current**, i.e. the angle of $Z_p$):
$$P=3V_pI_p\cos\phi=\sqrt3\,V_LI_L\cos\phi,\qquad Q=\sqrt3\,V_LI_L\sin\phi,\qquad S=\sqrt3\,V_LI_L=3V_pI_p.$$
The formula in line quantities holds for **both** star and delta, and $\phi$ is the *load's* impedance angle, not the angle between a line voltage and a line current (those differ by $30^\circ$). $P$ is constant in time, unlike single-phase power which pulsates at $2f$.

## 5. Solution procedure
1. Fix the connection of the load (and source) and the stated voltage (line-to-line unless said otherwise: "220 V three-phase" means $V_L=220$ V).
2. Pick the reference ($\bar V_{an}$ or $\bar V_{ab}$ at $0^\circ$) and the sequence (abc).
3. Phase impedance and phase current: $\bar I_p=\bar V_p/Z_p$.
4. Line current from the connection rule of §2 or §3; use $\pm120^\circ$ for the other phases.
5. Power from §4. Check with $P=3I_p^2R_p$.

Phasor diagrams for Q9, Q10 and Q12 are in [[T4-Q9 - Balanced Delta Load]], [[T4-Q10 - Delta Load Power]] and [[T4-Q12 - Star Load Voltage and Current]]. For measuring $P$ with two wattmeters see [[09 Three Phase Circuits and Power Measurement]].

## 6. Common traps
- Using $V_L$ as the phase voltage in a star circuit (or $I_L$ as the phase current in a delta).
- Using the angle between **line** quantities in $\cos\phi$.
- Treating "220 V" as a phase voltage; three-phase ratings are line-to-line.
- Forgetting the $30^\circ$ phase shift between line and phase quantities when asked for phasors.
- Reporting **phase** currents when the question asks for **line** currents (a delta load has $I_L=\sqrt3I_p$); see Q10.

## 7. Cross-domain links
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]]: three phasors $120^\circ$ apart that sum to zero are the same geometry as the balanced rotating vectors that produce the **revolving field** of [[Revolving Magnetic Field and Synchronous Speed]] (Tutorial 8).
- [[Conservation Laws and Flow Networks]]: a constant total from three pulsating powers that are $120^\circ$ apart is a conservation-of-flow statement: the three ripples cancel exactly, as in three evenly phased pumps feeding one pipe.
