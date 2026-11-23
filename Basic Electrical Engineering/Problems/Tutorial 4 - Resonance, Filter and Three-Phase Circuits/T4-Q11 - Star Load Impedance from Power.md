---
tags: [EE1100, tutorial-solution, three-phase, star-connection, power, impedance]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q11 - Star Connection Impedance"]
---

# T4-Q11: Star-Load Impedance from Total Power and Line Current

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Three-Phase Circuits]] · Previous: [[T4-Q10 - Delta Load Power]] · Next: [[T4-Q12 - Star Load Voltage and Current]]

> [!question] A three-phase 208 V generator supplies a total of 1800 W at a line current of 10 A when three identical impedances are connected in star across its line terminals. Find the resistive and reactive components of each phase impedance. *[Sheet: $6\ \Omega$ and $\pm10.39\ \Omega$]*

**Tests:** [[Theory - Three-Phase Circuits#2. Star (Y) connection|star connection]], $P=\sqrt3V_LI_L\cos\phi$, recovering $R$ and $X$ from $P$ and $|Z|$.

## Given
$V_L=208$ V, $I_L=10$ A, $P_{total}=1800$ W; star load, so $I_p=I_L=10$ A and $V_p=V_L/\sqrt3$.

## Principle and why it applies
Total real power is dissipated only in the three phase resistances, so $P=3I_p^2R$ gives $R$ **directly**; the magnitude $|Z|=V_p/I_p$ then fixes $X$ through $X^2=|Z|^2-R^2$. The sign of $X$ cannot be told from power alone, hence the $\pm$.

## Diagram
Per-phase equivalent: $V_{p}=120.1$ V across $Z=R\pm jX$, current $10$ A.

## Solution
$$V_p=\frac{208}{\sqrt3}=120.1\ \text{V},\qquad |Z|=\frac{V_p}{I_p}=\frac{120.1}{10}=12.01\ \Omega.$$
$$R=\frac{P}{3I_p^2}=\frac{1800}{3\times100}=\mathbf{6\ \Omega},\qquad X=\sqrt{|Z|^2-R^2}=\sqrt{144.2-36}=\mathbf{10.40\ \Omega}\ (\text{sheet }10.39).$$
Equivalently from the power factor: $\cos\phi=\dfrac{P}{\sqrt3V_LI_L}=\dfrac{1800}{3602.2}=0.4997\approx0.5$, $\phi=60^\circ$, $R=|Z|\cos\phi=6$, $X=|Z|\sin\phi=10.39$.

## Result
$$\boxed{Z_p=6\pm j10.39\ \Omega\quad(|Z_p|=12\ \Omega,\ \phi=\pm60^\circ)}$$
$+j$ if the load is inductive (lagging current), $-j$ if capacitive (leading current): the power data cannot distinguish them.

## Check
$P=3I_p^2R=3\times100\times6=1800$ W ✓ and $S=\sqrt3V_LI_L=3602$ VA, $Q=S\sin60^\circ=3120$ VAr $=3I_p^2X=3\times100\times10.4$ ✓.

## Trap / alternative
- Using $V_L$ (208 V) as the phase voltage gives $|Z|=20.8\ \Omega$, which is the delta value; in a **star** load $V_p=V_L/\sqrt3$.
- Assuming the load is inductive is a guess; the question only supports "reactive component of $\pm10.39\ \Omega$".
- If the same three impedances were connected in **delta**, each would carry $V_L=208$ V and the line current would be three times as large.

## Concepts used
- Star connection, three-phase power, phase impedance ([[Theory - Three-Phase Circuits]], [[09 Three Phase Circuits and Power Measurement]])
