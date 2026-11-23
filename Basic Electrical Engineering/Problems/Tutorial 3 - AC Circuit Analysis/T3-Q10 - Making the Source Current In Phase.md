---
tags: [EE1100, tutorial-solution, AC-circuits, impedance, power-factor, reactance]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q10: Finding the Reactance That Puts the Source Current in Phase

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Impedance and Series-Parallel AC Circuits]], [[Power Factor Correction]] · Previous: [[T3-Q9 - Nodal Analysis in the Phasor Domain]] · Next: [[T3-Q11 - Mesh, Nodal and Thevenin for Two Sources]]

> [!question] For the circuit of Fig. 4 ($R_1=3\ \Omega$ in series with an unknown reactance $X$, feeding between $a$-$b$ the combination: ($R_2=100\ \Omega$ in series with $C=25\ \mu$F) in parallel with $L=0.1$ H; $e(t)=141\sin400t$): (a) the equivalent impedance to the right of $a$-$b$; (b) the $X$ that makes the source current in phase with the source voltage; (c) is $X$ inductive or capacitive, and its value; (d) the effective source current. *[Sheet: $Z_{ab}=11.7647+j47.05\ \Omega$; $X=-j47.05\ \Omega$; capacitive, $C=53.13\ \mu$F; $i=9.5487\sin400t$ A]*

**Tests:** [[Impedance and Series-Parallel AC Circuits|series-parallel impedance]], the condition for unity power factor, [[Power Factor Correction|reactive compensation]].

## Given
$\omega=400$ rad/s. $X_L=\omega L=40\ \Omega$; $X_C=\dfrac1{\omega C}=\dfrac1{400\times25\times10^{-6}}=100\ \Omega$. The middle branch is $R_2+(-jX_C)=100-j100\ \Omega$ and the right branch is $jX_L=j40\ \Omega$.

## Principle and why it applies
The source current is in phase with the source voltage when the *total* impedance seen by the source is **purely real** (zero imaginary part): then $pf=1$. The unknown element $X$ is in series, so its reactance simply has to cancel the imaginary part of $Z_{ab}$.

## Diagram
![[T3-Q10-circuit.png]]

## Solution
**(a)** Parallel combination of $Z_1'=100-j100$ and $Z_2'=j40$:
$$Y_{ab}=\frac1{100-j100}+\frac1{j40}=\frac{100+j100}{20\,000}-j0.025=0.005+j0.005-j0.025=0.005-j0.020\ \text{S},$$
$$Z_{ab}=\frac1{Y_{ab}}=\frac{0.005+j0.020}{0.005^2+0.020^2}=\frac{0.005+j0.020}{0.000425}=\mathbf{11.765+j47.06\ \Omega}.$$
(inductive: the right branch dominates).

**(b), (c)** Total impedance seen by the source: $Z=R_1+jX+Z_{ab}=(3+11.765)+j(X+47.06)$. Unity power factor needs
$$X+47.06=0\ \Rightarrow\ X=-47.06\ \Omega:\quad\text{a negative reactance, i.e. }\mathbf{capacitive}.$$
Only a capacitor is needed (no $L$): $X_C=47.06=\dfrac1{\omega C}\Rightarrow C=\dfrac1{400\times47.06}=\mathbf{53.13\ \mu F}$.

**(d)** At unity power factor the total impedance is $14.765\ \Omega$ (real):
$$I_m=\frac{141}{14.765}=\mathbf{9.55\ A}\ (\text{peak}),\qquad I_{rms}=6.75\ \text{A},\qquad i(t)=9.55\sin400t\ \text{A (in phase with }e).$$

## Result
$$\boxed{Z_{ab}=11.765+j47.06\ \Omega;\quad X=-j47.06\ \Omega\ (C=53.13\ \mu\text{F});\quad I=9.55\sin400t\ \text{A}\ (6.75\ \text{A rms})}$$

## Check
With $X=-j47.06$: $Z_{total}=14.765+j0$ ✓. The reactive power of the whole circuit is zero: the capacitor's $Q=-I^2\cdot47.06$ cancels the $+I^2\cdot47.06$ of $Z_{ab}$ ✓. Note $R_2$ (and the $11.765\ \Omega$) are the only dissipators, so the power delivered is $I_{rms}^2\times14.765=673$ W.

## Trap / alternative
- Cancelling the **imaginary part of $Z_{ab}$ only**: $R_1$ is real and plays no role.
- Don't compute $Z_{ab}$ with $R_2\parallel C\parallel L$ (all three in parallel): the figure has $R_2$ in **series** with $C$.
- This is a *series* compensation (reactance in the line); [[Power Factor Correction]] normally uses a *shunt* capacitor across the load. Both zero the net reactance, but the voltages inside the circuit differ.

## Concepts used
- Series-parallel impedance, unity-power-factor condition ([[Impedance and Series-Parallel AC Circuits]], [[Power Factor Correction]])
