---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RL-circuit, switching]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q5: RL Circuit with a Switch That Opens at t = 0

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q4 - Source-Free RL Decay]] · Next: [[T2-Q6 - RC Circuit with a Two-Position Switch]]

> [!question] Find $v(t)$ for $t>0$ (the voltage across the $0.5$ H inductor). Hint: the current source may be converted to an equivalent voltage source. The circuit has a 2 A source with $12\ \Omega$, a switch at $t=0$, $20\ \Omega$, $6\ \Omega$, $5\ \Omega$, a 20 V source and $L=0.5$ H. *[Sheet: $v=v_L=-4e^{-20t}$ V]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#3. First-order circuits (one storage element)|the five-step switching recipe]], Thevenin equivalent seen by $L$, source transformation.

## Given
2 A source in parallel with $12\ \Omega$; the switch connects this pair to node S; at S: $20\ \Omega$ to ground, $5\ \Omega$ in series with a 20 V source ($+$ at top) to ground, and the branch $6\ \Omega$ + $L$ (voltage $v$, $+$ at top). The switch has been **closed for a long time** and **opens at $t=0$** (this reading reproduces the sheet's answer; a switch that closed at $t=0$ would give a different time constant).

## Principle and why it applies
$i_L$ cannot jump, so the story is: find $i_L(0^-)$ in the closed-switch DC steady state; find the final value and $\tau$ in the *new* (open-switch) circuit; then $i_L(t)=i_\infty+[i_L(0^+)-i_\infty]e^{-t/\tau}$ and $v=L\,di_L/dt$. After the switch opens, the 2 A source and its $12\ \Omega$ are disconnected and drop out entirely.

## Diagram
![[T2-Q5-circuit.png]]

## Solution
**Before ($t<0$, switch closed, $L$ a short):** all of S's neighbours act at once. KCL at S ($V_S$ unknown, the $6\ \Omega$ ends on the shorted inductor):
$$2=\frac{V_S}{12}+\frac{V_S}{20}+\frac{V_S-20}{5}+\frac{V_S}{6}\ \Rightarrow\ 0.5V_S=6\ \Rightarrow\ V_S=12\ \text{V},\qquad i_L(0^-)=\frac{12}{6}=2\ \text{A}.$$
(The hint gives the same $V_S$: the source transformation of 2 A ∥ 12 Ω is 24 V in series with $12\ \Omega$.)

**After ($t>0$, switch open):** the inductor sees $6\ \Omega$ in series with the Thevenin equivalent of $20\ \Omega$ and ($5\ \Omega$ + 20 V):
$$R_{th}=20\parallel5=4\ \Omega,\qquad V_{th}=20\cdot\frac{20}{20+5}=16\ \text{V}.$$
$$R_{tot}=6+4=10\ \Omega,\qquad \tau=\frac{L}{R_{tot}}=\frac{0.5}{10}=0.05\ \text{s},\qquad i_\infty=\frac{16}{10}=1.6\ \text{A}.$$
$$i_L(t)=1.6+(2-1.6)e^{-20t}=1.6+0.4e^{-20t}\ \text{A}.$$
$$v(t)=L\frac{di_L}{dt}=0.5\times(-20)(0.4)e^{-20t}=\mathbf{-4e^{-20t}\ V}.$$

## Result
$$\boxed{v(t)=v_L(t)=-4e^{-20t}\ \text{V},\qquad t>0}$$

![[T2-Q5-response.png]]

## Check
At $t=0^+$ the inductor current is still 2 A but the new circuit would settle at 1.6 A, so the inductor must **push back** with a negative voltage: $v(0^+)=-4$ V. KVL at $0^+$: the Thevenin source (16 V) minus the drop across $10\ \Omega$ ($2\times10=20$ V) leaves $-4$ V across $L$ ✓.

## Trap / alternative
- The inductor voltage is **not continuous**: it was $0$ V (a short) before and jumps to $-4$ V.
- Don't include the $2$ A source and $12\ \Omega$ in the post-switch circuit; the open switch isolates them.
- Equally valid: write $L\,di/dt+10i=16$ and solve the first-order ODE directly.

## Concepts used
- Continuity of $i_L$, Thevenin equivalent seen by the storage element, first-order response ([[Theory - Transients in RL, RC and RLC Circuits]], [[Theory - Circuit Laws and Network Theorems]])
