---
tags: [EE1100, diodes, tutorial-solution, clipper]
---

# B-Q3 — Diode in Series with a Battery (shifted half-wave rectifier)

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q2 - Diode OR Gate]] · Next: [[B-Q4 - Diode AND Gate]]

> [!question] Fig. 3: $V_i=20\sin\omega t$ drives a 5 V battery (minus terminal towards the source, plus terminal towards the diode), an ideal diode, and load $R$ to ground. Sketch $V_0$.

## 1. Theory

The battery is in series with the diode, so the voltage at the diode anode is $V_i+5$ (going from the source through the battery from − to +). An ideal diode conducts when its anode voltage is positive (more than 0):

$$V_0=\begin{cases}V_i+5,&V_i+5>0\ (V_i>-5\ \text{V})\\0,&V_i\le-5\ \text{V}\end{cases}$$

The battery acts as a **forward bias** (it lowers the input level needed to turn the diode on), so the diode conducts for more than half a cycle.

## 2. Solution

$V_i=20\sin\omega t$. The diode turns ON when $20\sin\omega t>-5$, i.e. $\sin\omega t>-0.25$:

$$\omega t_{ON}=-14.48^\circ\ (=345.52^\circ),\qquad \omega t_{OFF}=180^\circ+14.48^\circ=194.48^\circ$$

| Interval | Diode | $V_0$ |
|---|---|---|
| $345.52^\circ\to360^\circ$ and $0^\circ\to194.48^\circ$ | ON | $20\sin\omega t+5$ |
| $194.48^\circ\to345.52^\circ$ | OFF | $0$ |

Peak output: $V_{0,max}=20+5=25$ V at $\omega t=90^\circ$; the output starts the conducting interval at 0 V (at $\omega t=-14.48^\circ$) because $V_i=-5$ there.

![[B3-waveform.png]]

> [!success] Result
> $V_0$ is the input shifted **up** by 5 V, with the part below 0 V removed ("clipped to zero"): positive peak 25 V, conduction for $208.96^\circ$ (58 %) of each cycle.
> Check: a numerical simulation of the circuit reproduces $\max(20\sin\omega t+5,0)$ to within $2.5\times10^{-5}$ V.
