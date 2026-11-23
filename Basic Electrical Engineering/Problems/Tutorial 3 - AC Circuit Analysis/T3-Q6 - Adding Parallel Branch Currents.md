---
tags: [EE1100, tutorial-solution, AC-circuits, phasors, KCL]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q6: Adding Sinusoidal Branch Currents with Phasors

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[Phasors and Complex Algebra]] · Previous: [[T3-Q5 - RC Circuit Power and Power Factor]] · Next: [[T3-Q7 - Series RLC Voltage Magnification]]

> [!question] A sinusoidal voltage drives three parallel branches with currents $i_1=14.14\sin(\omega t-45^\circ)$, $i_2=28.3\cos(\omega t-60^\circ)$, $i_3=7.07\sin(\omega t+60^\circ)$ A. (a) Find the complete time expression for the source current. (b) Draw the phasor diagram with the voltage as reference. *[Sheet: $i(t)=39.39\sin(\omega t+15.10^\circ)$ A; $\bar I_1=10\angle-45^\circ$, $\bar I_2=20\angle30^\circ$, $\bar I_3=5\angle60^\circ$, $\bar I=27.85\angle15.10^\circ$ A]*

**Tests:** [[Phasors and Complex Algebra|phasor conversion]] (sin vs cos), KCL with phasors.

## Given
Three sinusoids at the same $\omega$ (they are all measured relative to the same voltage reference). One is written as a **cosine**, the others as sines.

## Principle and why it applies
KCL at the supply node says $i=i_1+i_2+i_3$ at every instant. Adding sinusoids of the *same frequency* in the time domain is messy (trigonometric identities); the **phasor** representation turns it into complex addition because the sum of two same-frequency sinusoids is another sinusoid of that frequency. Convert every term to the same trigonometric form (here **sine**), then to a phasor.

## Diagram
![[T3-Q4-Q6-Q7-phasors.png]]

## Solution
**Convert to a common form** using $\cos(x)=\sin(x+90^\circ)$:
$$i_2=28.3\cos(\omega t-60^\circ)=28.3\sin(\omega t+30^\circ).$$
**Phasors** (rms $=$ peak$/\sqrt2$, angle = the phase in the sine form):
$$\bar I_1=10\angle-45^\circ=7.071-j7.071,\quad \bar I_2=20\angle30^\circ=17.321+j10,\quad \bar I_3=5\angle60^\circ=2.5+j4.330\ \ \text{A}.$$
**Sum:**
$$\bar I=\bar I_1+\bar I_2+\bar I_3=26.892+j7.259=27.85\angle15.10^\circ\ \text{A (rms)}.$$
**Back to time** (peak $=\sqrt2\times27.85=39.39$ A):
$$\mathbf{i(t)=39.39\sin(\omega t+15.10^\circ)\ A}.$$

## Result
$$\boxed{\bar I=27.85\angle15.10^\circ\ \text{A (rms)},\qquad i(t)=39.39\sin(\omega t+15.10^\circ)\ \text{A}}$$
Phasor diagram: $\bar V$ along the real axis; $\bar I_1$ below it (lagging, inductive branch), $\bar I_2$ and $\bar I_3$ above it (leading, capacitive branches), and the resultant at $+15.1^\circ$.

## Check
Add the peak values the long way at $\omega t=0$: $14.14\sin(-45^\circ)+28.3\sin30^\circ+7.07\sin60^\circ=-10+14.15+6.12=10.27$ A, and $39.39\sin15.10^\circ=10.26$ A ✓.

## Trap / alternative
- **Mixing sine and cosine** is the standard error: $28.3\cos(\omega t-60^\circ)$ is at $+30^\circ$ in the *sine* convention, not $-60^\circ$.
- Don't add the magnitudes ($10+20+5=35$ A); only the phasors add.
- Stay in **rms** or **peak** throughout; the sheet's phasors are rms and the final time expression converts back to peak.

## Concepts used
- Phasors and complex algebra, KCL ([[Phasors and Complex Algebra]])
