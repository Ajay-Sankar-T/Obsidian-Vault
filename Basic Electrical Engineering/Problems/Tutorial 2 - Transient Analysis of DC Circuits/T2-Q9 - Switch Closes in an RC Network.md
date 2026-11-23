---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RC-circuit, switching]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q9: Switch Closes in an RC Network

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q8 - Switch Opens in an RC Network]] · Next: [[T2-Q10 - Series RLC Step Response]]

> [!question] Same network as Q8, but the switch is **closed** at $t=0$ after having been open for a long time. Determine $v_C$ and $v_o$ at (a) $t=0^-$, (b) $t=0^+$, (c) $t=1.3$ ms. *[Sheet: $0,0$ V; $0,38.4$ V; $70.0,38.4$ V. The $v_C$ at 1.3 ms is revised below.]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#3. First-order circuits (one storage element)|first-order charging]], Thevenin resistance seen by the capacitor with an *ideal* source attached.

## Given
Same circuit as [[T2-Q8 - Switch Opens in an RC Network]]: the 120 V source in a switched vertical branch at the node between $250\ \Omega$ and $600\ \Omega$, with $4\ \mu$F ∥ $1250\ \Omega$ on the left and $2\ \text{k}\Omega$, $100\ \Omega$, $400\ \Omega$ on the right.

## Principle and why it applies
For $t<0$ the source is disconnected, so with nothing driving it the capacitor is uncharged: $v_C(0^-)=0$. At $t=0^+$ the voltage $v_C$ stays $0$ but the ideal source **clamps the middle node at 120 V** instantly, so the right-hand network sees a fixed 120 V and $v_o$ jumps to its steady value at once. The capacitor then charges through the Thevenin resistance of the left-hand network.

## Diagram
![[T2-Q8-circuit.png]]

## Solution
**(a) $t=0^-$:** the source is disconnected and the circuit has no stored energy: $v_C=0$, $v_o=0$.

**(b) $t=0^+$.** $v_C=0$. The middle node is at 120 V, so $v_o$ is exactly the DC value found in Q8:
$$v_o(0^+)=120\cdot\frac{400}{600+400}\cdot\frac{400}{500}=\mathbf{38.4\ V}.$$
The source clamps the node, so $v_o$ is **independent of the capacitor** for all $t\ge0^+$ (the left and right halves are decoupled by the ideal source): $v_o=38.4$ V for all $t>0$.

**(c) $t=1.3$ ms.** Seen from the capacitor, the left-hand network is the $1250\ \Omega$ in parallel with the $250\ \Omega$ to the 120 V node (clamped, so it acts like a $250\ \Omega$ to a 120 V source):
$$V_{th}=120\cdot\frac{1250}{1250+250}=100\ \text{V},\quad R_{th}=1250\parallel250=208.3\ \Omega,\quad \tau=208.3\times4\times10^{-6}=0.833\ \text{ms}.$$
$$v_C(t)=100\big(1-e^{-t/0.833\,\text{ms}}\big)\ \Rightarrow\ v_C(1.3\ \text{ms})=100(1-e^{-1.56})=\mathbf{78.99\ V}.$$

## Result
| | $v_C$ | $v_o$ |
|---|---|---|
| $0^-$ | 0 | 0 |
| $0^+$ | 0 | 38.4 V |
| 1.3 ms | **78.99 V** | 38.4 V |

![[T2-Q8-Q9-response.png]]

> [!warning] The sheet's $v_C(1.3\ \text{ms})=70.0$ V
> With the time constant $\tau=0.833$ ms that follows from the circuit, $100(1-e^{-1.3/0.833})=78.99$ V; $70.0$ V would need $\tau=1.08$ ms ($R=270\ \Omega$), which no combination of the given resistors produces. The Q8 value $59.45$ V matches its time constant exactly, so the circuit reading is right and the printed $70.0$ is taken as a slip. The final value $100$ V and $v_o=38.4$ V agree with the sheet.

## Check
The final value 100 V equals $v_C(0^-)$ of Q8 (same DC steady state with the source connected) ✓. At 5τ = 4.2 ms the capacitor is at 99.3 V. The charging current at $0^+$ is $V_{th}/R_{th}=100/208.3=0.48$ A.

## Trap / alternative
- With an **ideal voltage source** across the middle node, $v_o$ cannot depend on $C$ for $t>0$; students often make $v_o$ vary.
- The initial $v_C=0$ is only valid because the circuit has been open "for a long time": a long-open switch means all stored energy has leaked away.
- The time constant uses the Thevenin resistance with the source *killed* (short), which is why the $250\ \Omega$ ends up in parallel with the $1250\ \Omega$ here (in Q8 it was in series).

## Concepts used
- Thevenin resistance, first-order charging, ideal source clamping ([[Theory - Transients in RL, RC and RLC Circuits]])
