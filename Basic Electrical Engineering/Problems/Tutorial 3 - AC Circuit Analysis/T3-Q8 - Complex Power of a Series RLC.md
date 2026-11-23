---
tags: [EE1100, tutorial-solution, AC-circuits, power, power-factor, complex-power]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q8: Complex Power in the Series RLC of Q7

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[AC Power and Power Factor]] · Previous: [[T3-Q7 - Series RLC Voltage Magnification]] · Next: [[T3-Q9 - Nodal Analysis in the Phasor Domain]]

> [!question] For the circuit of Q7 find (a) the real and reactive power supplied by the source, (b) the reactive power supplied by the source, (c) the reactive power of the capacitor, (d) the reactive power of the inductor, (e) the power factor. *[Sheet: $P_S=179.79$ W, $Q_S=134.8$ VAr lagging; $Q_C=449.72$ VAr leading; $Q_L=584.27$ VAr lagging; $pf=0.8$ lagging]*

**Tests:** [[AC Power and Power Factor|real, reactive and apparent power]], sign conventions for $Q$, power balance.

## Given
From [[T3-Q7 - Series RLC Voltage Magnification]]: $R=40\ \Omega$, $X_L=130\ \Omega$, $X_C=100\ \Omega$, $I=2.121$ A rms ($I^2=4.5$ A²), $V=106.07$ V rms, $Z=50\angle36.87^\circ\ \Omega$.

## Principle and why it applies
The three powers are $P=I^2R$ (only the resistor dissipates), $Q_L=+I^2X_L$ (inductors absorb reactive power, taken as positive), $Q_C=-I^2X_C$ (capacitors *supply* it, negative), and for the whole circuit $\bar S=\bar V\bar I^*=P+jQ$ with $Q=Q_L+Q_C$. The same current flows through all three elements, so each power is just $I^2$ times the element's resistance or reactance, no angles needed.

## Diagram
![[T3-Q8-power-triangle.png]]

## Solution
$I^2=(2.1213)^2=4.5\ \text{A}^2$.
$$P=I^2R=4.5\times40=\mathbf{180\ W},\qquad Q_L=I^2X_L=4.5\times130=\mathbf{+585\ VAr\ (lagging)},\qquad Q_C=-I^2X_C=-4.5\times100=\mathbf{-450\ VAr\ (leading)}.$$
$$Q_S=Q_L+Q_C=585-450=\mathbf{135\ VAr\ lagging},\qquad |S|=\sqrt{180^2+135^2}=225\ \text{VA},\qquad pf=\frac{P}{|S|}=\mathbf{0.8\ lagging}.$$
Check from the source: $\bar S=V_{rms}\,I^*=106.07\angle0^\circ\times2.1213\angle+36.87^\circ=225\angle36.87^\circ=180+j135$ VA ✓.

## Result
$$\boxed{P=180\ \text{W},\ Q_S=135\ \text{VAr lag},\ Q_C=-450\ \text{VAr},\ Q_L=+585\ \text{VAr},\ pf=0.8\ \text{lag}}$$
(The sheet's $179.79$, $449.72$, $584.27$ come from rounding $I$ to $2.12$ A.)

## Check
Conservation: source $Q$ equals the sum of element $Q$s ✓; source $P$ equals resistor $P$ ✓ (no real power in $L$ and $C$). The reactive powers of $L$ and $C$ largely **cancel each other** (585 against −450), which is why the source delivers only 135 VAr; at resonance they would cancel exactly and $pf=1$ (this is the principle of [[Power Factor Correction]]).

## Trap / alternative
- Don't give $Q_C$ a positive sign when asked for "reactive power of the capacitor": it is **negative** (or "leading") in the standard convention; the sheet quotes the magnitude and the word "leading".
- $pf=0.8$ lagging, not leading: the net reactance is inductive ($X_L>X_C$).

## Concepts used
- Complex power, power triangle, sign of $Q$ ([[AC Power and Power Factor]], [[Power Factor Correction]])
