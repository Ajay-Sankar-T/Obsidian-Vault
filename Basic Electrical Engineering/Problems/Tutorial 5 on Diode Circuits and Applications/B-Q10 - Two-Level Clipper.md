---
tags: [EE1100, diodes, tutorial-solution, clipper]
---

# B-Q10 — Two-Level Clipper (Slicer)

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q9 - Battery Charging Rectifier Circuit]] · Next: [[B-Q11 - Full-Wave Rectifier with Battery]]

> [!question] Diodes $D_1,D_2$ ideal, $v_i=10\sin\omega t$ V, $f=1$ kHz, $R_i=1$ kΩ, $V_{R1}=-4$ V, $V_{R2}=+6$ V.
> (a) Condition for neither diode to conduct and $v_o$ there. (b) $\omega t$ at which $D_1$ turns on and off; $v_o$ in that interval. (c) The same for $D_2$. (d) Sketch $v_o(t)$. (e) With cut-in voltage 0.7 V for each diode: clipping levels and switching points.

![[B10-clipper.png]]

## 1. Theory

$D_2$ (anode on the output node, cathode on $V_{R2}$) conducts when the output node would exceed $V_{R2}$; $D_1$ (anode on $V_{R1}$, cathode on the output node) conducts when the node would go below $V_{R1}$. In between, both diodes are OFF and $v_o=v_i$ (no current in $R_i$). When a diode conducts, it clamps $v_o$ to its reference voltage (ideal) or to the reference $\pm V_\gamma$ (practical), and $R_i$ carries the excess.

## 2. Solution

### (a) Neither diode conducts
$$\boxed{-4\ \text{V}<v_i<6\ \text{V}}\quad(V_{R1}<v_i<V_{R2}),\qquad v_o=v_i$$

### (b) $D_1$ (on when $v_i<-4$ V)
$10\sin\omega t=-4\Rightarrow\sin\omega t=-0.4$:
$$\omega t_{ON}=180^\circ+23.58^\circ=\boxed{203.58^\circ}\ (3.5531\ \text{rad}),\qquad \omega t_{OFF}=360^\circ-23.58^\circ=\boxed{336.42^\circ}\ (5.8717\ \text{rad})$$
$$v_o=\boxed{-4\ \text{V}}\ \text{throughout},\qquad i_{R_i}=\frac{v_i+4}{R_i}\ (\text{up to }-6\ \text{mA at }270^\circ)$$

### (c) $D_2$ (on when $v_i>6$ V)
$10\sin\omega t=6\Rightarrow\sin\omega t=0.6$:
$$\omega t_{ON}=\boxed{36.87^\circ}\ (0.6435\ \text{rad}),\qquad\omega t_{OFF}=180^\circ-36.87^\circ=\boxed{143.13^\circ}\ (2.4981\ \text{rad})$$
$$v_o=\boxed{+6\ \text{V}}\ \text{throughout},\qquad i_{R_i}=\frac{v_i-6}{R_i}\ (\text{up to }4\ \text{mA at }90^\circ)$$

### (d) Output waveform

| $\omega t$ | $v_o$ |
|---|---|
| $0^\circ\to36.87^\circ$ | $10\sin\omega t$ (rising $0\to6$ V) |
| $36.87^\circ\to143.13^\circ$ | flat $+6$ V ($D_2$ ON) |
| $143.13^\circ\to203.58^\circ$ | $10\sin\omega t$ (falling $6\to-4$ V) |
| $203.58^\circ\to336.42^\circ$ | flat $-4$ V ($D_1$ ON) |
| $336.42^\circ\to360^\circ$ | $10\sin\omega t$ (rising $-4\to0$ V) |

See the middle panel of the figure (switching angles marked on the $\omega t$ axis). At 1 kHz one cycle lasts 1 ms, so the angles correspond to times $t=\omega t/(2\pi)\times1\ \text{ms}$ (e.g. $D_2$ turns on at 0.102 ms).

### (e) Cut-in voltage $V_\gamma=0.7$ V
Each diode starts to conduct 0.7 V beyond its reference:
- $D_2$ on when $v_o>V_{R2}+0.7=6.7$ V, clip level $\boxed{+6.7\ \text{V}}$:
$$\omega t_{ON}=\sin^{-1}0.67=\boxed{42.07^\circ},\qquad \omega t_{OFF}=180^\circ-42.07^\circ=\boxed{137.93^\circ}$$
- $D_1$ on when $v_o<V_{R1}-0.7=-4.7$ V, clip level $\boxed{-4.7\ \text{V}}$:
$$\omega t_{ON}=180^\circ+\sin^{-1}0.47=\boxed{208.03^\circ},\qquad\omega t_{OFF}=360^\circ-28.03^\circ=\boxed{331.97^\circ}$$

| | ideal | $V_\gamma=0.7$ V |
|---|---|---|
| upper clip level | $+6$ V | $+6.7$ V |
| lower clip level | $-4$ V | $-4.7$ V |
| $D_2$ on / off | 36.87° / 143.13° | 42.07° / 137.93° |
| $D_1$ on / off | 203.58° / 336.42° | 208.03° / 331.97° |

> [!success] A circuit simulation (sweeping $\omega t$ in 0.1° steps and testing all diode states) reproduces all of these switching points.
