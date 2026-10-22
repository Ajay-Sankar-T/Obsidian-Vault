---
tags: [EE1100, diodes, tutorial-solution, clipper]
---

# B-Q9 — Rectifier Charging a Battery

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[B-Q8 - Half-Wave Rectifier with Series Resistor]] · Next: [[B-Q10 - Two-Level Clipper]]

> [!question] Fig. 9: $V_m\sin\omega t$, switch $S$, ideal diode ($v_D$), resistor $R$ ($v_R$) and battery $E$ in series; $v_0$ is the voltage across $R$ and $E$ together. Plot $v_0$, the battery current and the diode voltage $v_D$.

![[B9-circuit-waveforms.png]]

> [!note] Assumptions
> $S$ is closed. The battery's **+ terminal is at the top** (towards $R$), as drawn, so a current flowing down through $R$ enters the + terminal (the battery is being charged). $0<E<V_m$. The plots use $V_m=10$ V, $E=4$ V, $R=100\ \Omega$ as an example.

## 1. Theory

KVL: $V_m\sin\omega t=v_D+v_R+E$. The diode is ON only when the source exceeds the battery voltage, i.e. the battery acts as a **reverse bias / threshold** for the diode:
$$V_m\sin\omega t>E\ \Longleftrightarrow\ \alpha<\omega t<\pi-\alpha,\qquad \alpha=\sin^{-1}\frac E{V_m}.$$

## 2. Solution

**Diode ON** ($\alpha<\omega t<\pi-\alpha$): $v_D=0$,
$$i=\frac{V_m\sin\omega t-E}{R},\qquad v_R=V_m\sin\omega t-E,\qquad v_0=v_R+E=V_m\sin\omega t.$$

**Diode OFF** (rest of the cycle, including the negative half): $i=0$, $v_R=0$,
$$v_0=E,\qquad v_D=V_m\sin\omega t-E\ (<0).$$

| Quantity | ON interval | OFF interval |
|---|---|---|
| $v_0$ | $V_m\sin\omega t$ | $E$ |
| battery current (charging) | $(V_m\sin\omega t-E)/R$ | 0 |
| $v_D$ | 0 | $V_m\sin\omega t-E$ (min $-(V_m+E)$ at $\omega t=270^\circ$) |

**Example** ($V_m=10$ V, $E=4$ V, $R=100\ \Omega$): $\alpha=23.58^\circ$; conduction from $23.58^\circ$ to $156.42^\circ$; peak current $(10-4)/100=60$ mA at $90^\circ$ (simulation: 59.9994 mA); PIV $=V_m+E=14$ V.

**Average charging current:**
$$I_{avg}=\frac1{2\pi R}\Big[2V_m\cos\alpha-E(\pi-2\alpha)\Big]=\frac{18.33-9.28}{2\pi(100)}=14.4\ \text{mA}$$

> [!success] Waveforms
> $v_0$ follows the sine peaks above $E$ and sits at $E$ otherwise (a clipper at level $E$). The battery current is one pulse per cycle of the shape $(V_m\sin\omega t-E)/R$ (between $\alpha$ and $\pi-\alpha$), and the diode voltage is zero while conducting and the (negative) difference $V_m\sin\omega t-E$ while blocking.
