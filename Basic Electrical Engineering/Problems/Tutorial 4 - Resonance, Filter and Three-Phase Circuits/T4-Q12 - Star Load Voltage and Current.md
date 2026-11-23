---
tags: [EE1100, tutorial-solution, three-phase, star-connection, phasors]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q12 - Star Load Voltage and Current"]
---

# T4-Q12: Star Load: Phase Currents and Line Voltage

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Three-Phase Circuits]] · Previous: [[T4-Q11 - Star Load Impedance from Power]] · Next tutorial: [[Tutorial 5 - Diode Circuits and Applications]]

> [!question] A balanced three-phase star-connected load has an impedance of $4\angle60^\circ\ \Omega$ from line to neutral, and $\bar V_{an}=20\angle30^\circ$ V. (a) The currents in phases $a$, $b$, $c$. (b) The voltage from line $b$ to neutral. (c) The phasor $\bar V_{ac}$. *[Sheet: $5\angle-30^\circ$, $5\angle-150^\circ$, $5\angle90^\circ$ A; $20\angle-90^\circ$ V; $34.64\angle0^\circ$ V]*

**Tests:** [[Theory - Three-Phase Circuits#2. Star (Y) connection|star connection]], $\pm120^\circ$ symmetry, line voltage $=\sqrt3\times$ phase voltage at a $30^\circ$ shift.

## Given
$Z=4\angle60^\circ\ \Omega$ in each phase (the printed tutorial text reads "$4\,|60^\circ$"), $\bar V_{an}=20\angle30^\circ$ V, abc sequence.

## Principle and why it applies
Each phase of a star load is a plain single-phase circuit: $\bar I_a=\bar V_{an}/Z$. The balanced source gives $\bar V_{bn}$ and $\bar V_{cn}$ by shifting $-120^\circ$ and $+120^\circ$, and the *line* voltage is a difference of phase voltages: $\bar V_{ac}=\bar V_{an}-\bar V_{cn}$.

## Diagram
![[T4-Q9-Q10-Q12-phasors.png]]

## Solution
**(a)**
$$\bar I_a=\frac{20\angle30^\circ}{4\angle60^\circ}=\mathbf{5\angle-30^\circ\ A},\qquad \bar I_b=5\angle(-30^\circ-120^\circ)=\mathbf{5\angle-150^\circ\ A},\qquad\bar I_c=5\angle(-30^\circ+120^\circ)=\mathbf{5\angle90^\circ\ A}.$$
**(b)** $\bar V_{bn}=20\angle(30^\circ-120^\circ)=\mathbf{20\angle-90^\circ\ V}$ (and $\bar V_{cn}=20\angle150^\circ$ V).

**(c)** $\bar V_{ac}=\bar V_{an}-\bar V_{cn}=(17.32+j10)-(-17.32+j10)=34.64+j0=\mathbf{34.64\angle0^\circ\ V}$. In magnitude $V_L=\sqrt3\,V_p=\sqrt3\times20=34.64$ V.

## Result
$$\boxed{\bar I_a=5\angle-30^\circ,\ \bar I_b=5\angle-150^\circ,\ \bar I_c=5\angle90^\circ\ \text{A};\quad\bar V_{bn}=20\angle-90^\circ\ \text{V};\quad\bar V_{ac}=34.64\angle0^\circ\ \text{V}}$$

## Check
The three phase currents sum to zero: $5\angle-30^\circ+5\angle-150^\circ+5\angle90^\circ=(4.33-j2.5)+(-4.33-j2.5)+(0+j5)=0$ ✓ (no neutral current). Power: $P=3I^2R=3\times25\times4\cos60^\circ=150$ W $=\sqrt3\times34.64\times5\times0.5$ ✓.

## Trap / alternative
- An earlier version of this note read the impedance as $46\angle0^\circ\ \Omega$ (a misreading of "$4\,|60^\circ$") and so could not reproduce the printed answers; with $Z=4\angle60^\circ\ \Omega$ every printed answer is reproduced exactly.
- $\bar V_{ac}$ points the **opposite** way to $\bar V_{ca}$: $\bar V_{ca}=\bar V_{cn}-\bar V_{an}=34.64\angle180^\circ$, so $\bar V_{ac}=34.64\angle0^\circ$.
- In a star, the line voltage leads the phase voltage by $30^\circ$ only for the *right pair* ($\bar V_{ab}$ leads $\bar V_{an}$); $\bar V_{ac}$ lags $\bar V_{an}$ by $30^\circ$ here ($0^\circ$ against $30^\circ$).

## Concepts used
- Star connection, balanced phasors, line voltages ([[Theory - Three-Phase Circuits]], [[09 Three Phase Circuits and Power Measurement]])
