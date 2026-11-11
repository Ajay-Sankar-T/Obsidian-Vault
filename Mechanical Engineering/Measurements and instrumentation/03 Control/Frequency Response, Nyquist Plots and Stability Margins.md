---
tags: [concept, instrumentation]
course: "Measurements, Instrumentation and Control (ME2400)"
aliases: [Frequency response, Bode plot, Nyquist plot, Nyquist criterion, Gain margin, Phase margin, Stability margin, Loop gain]
---

# Frequency Response, Nyquist Plots and Stability Margins

> [!abstract] In one breath
> Feed a sine into a stable linear system and the steady output is a sine of the same frequency with a different **amplitude and phase**: the complex number $G(j\omega)$. Plotting it against frequency (**Bode**) or as a curve in the complex plane (**Nyquist**) shows **how close a closed loop is to instability**: the distance to the critical point $-1$, measured as the **gain and phase margins**.

Part of [[Measurements, Instrumentation and Control - MOC]]. Previous: [[PID Control and Tuning]]. Building blocks: [[First-Order Systems - Time Constant and Response]], [[Second-Order Systems - Damping and Overshoot]].

## 1. Frequency response

$$
G(j\omega)=|G|\,e^{j\angle G},\qquad y_{ss}=|G|\sin(\omega t+\angle G)\ \text{for input }\sin\omega t
$$

**Bode plot:** $20\log_{10}|G|$ (dB) and $\angle G$ against $\log\omega$. The log scale turns products into sums, so a Bode plot is built by adding the plots of the factors: each pole contributes $-20$ dB/decade after its corner and up to $-90^\circ$; each zero the opposite; an integrator $1/s$ is $-20$ dB/dec and $-90^\circ$ at all frequencies; a pure delay adds only phase lag ($-\omega T_d$).

**Nyquist plot:** $L(j\omega)=\text{Re}+j\,\text{Im}$ for $\omega$ from 0 to $\infty$ (and its mirror image for negative $\omega$).

## 2. Nyquist stability criterion

For the loop gain $L(s)=G_c(s)G(s)H(s)$ with no right-half-plane poles, the closed loop $1/(1+L)$ is stable if and only if the Nyquist plot of $L(j\omega)$ **does not encircle the point $-1$**. Intuition: a signal going round the loop with gain 1 and phase $-180^\circ$ reinforces itself (negative feedback becomes positive) and grows.

**Margins** (how far from $-1$):

| Margin | Definition | Rule of thumb |
| --- | --- | --- |
| **Gain margin** GM | factor by which the gain can rise at the **phase crossover** $\omega_{pc}$ ($\angle L=-180^\circ$) before $|L|=1$: $GM=1/|L(j\omega_{pc})|$ | GM > 2 (6 dB) |
| **Phase margin** PM | extra phase lag allowed at the **gain crossover** $\omega_{gc}$ ($|L|=1$): $PM=180^\circ+\angle L(j\omega_{gc})$ | PM > 30°–45° |

Phase margin correlates with damping: $\zeta\approx PM/100$ for PM below about 60°, so PM = 45° gives $\zeta\approx0.45$ and about 20 % overshoot (see the table in [[Second-Order Systems - Damping and Overshoot]]). The crossover frequency sets the closed-loop speed.

## 3. Worked example

$L(s)=\dfrac{K}{s(s+1)(s+2)}$:

- **Phase crossover:** $\angle L=-90^\circ-\tan^{-1}\omega-\tan^{-1}(\omega/2)=-180^\circ$ at $\omega_{pc}=\sqrt2=1.41$ rad/s, where $|L|=K/\big[\omega\sqrt{1+\omega^2}\sqrt{4+\omega^2}\big]=K/6$.
- **Critical gain $K_u=6$:** the Nyquist curve passes through $-1$ (marginal stability): the loop oscillates at $\omega=\sqrt2$.
- For $K=2$: $GM=6/2=\mathbf{3}$ (**9.5 dB**), $\omega_{gc}=0.75$ rad/s, $PM=\mathbf{32.6^\circ}$.
- For $K=3$: $GM=2$ (6.0 dB), $PM=20^\circ$ (a poorly damped loop).

![[MIC-6-nyquist.png]]

The gain $K=2$ is 3 times below the instability: robust to a three-fold change in plant gain, but with only 33° of phase margin the step response overshoots by roughly 35 %.

## 4. Design with Bode: shape the loop

Aim for: **high gain at low frequency** (accuracy, disturbance rejection), a **−20 dB/decade slope through the crossover** (phase margin about 90° from the last pole), and **low gain at high frequency** (noise rejection, robustness to unmodelled dynamics). PID is a loop-shaping tool: **I** raises low-frequency gain, **D** adds phase lead near crossover, **P** sets the overall level. A **lead** compensator adds phase near crossover; a **lag** compensator raises DC gain without touching crossover.

> [!warning] Traps
> - Reading the margin at the wrong crossover: GM at the **phase** crossover, PM at the **gain** crossover.
> - Applying the Nyquist criterion to an open-loop-unstable system without counting encirclements properly.
> - Quoting margins for a delay-free model when the loop has dead time: add the delay's phase $-\omega T_d$.
> - Assuming a large gain margin implies a good phase margin (a loop with PM = 5° and GM = 10 dB oscillates).
> - Forgetting that the frequency response only describes the stable, linear, steady-state response.

> [!question]- Predict first: add a pure time delay of 0.3 s to the loop above ($K=2$). Which margin is hurt, and by how much?
> Phase margin: the delay adds $-\omega_{gc}T_d=-0.75(0.3)=-0.225$ rad $=-12.9^\circ$ at the gain crossover, so PM falls from 32.6° to about 19.7°. The gain crossover itself is unchanged (a delay has unit gain).

> [!question]- Why does the Nyquist curve at high $\omega$ approach the origin?
> The plant has more poles than zeros, so $|L|\to0$ as $\omega\to\infty$; physical systems cannot respond to arbitrarily fast inputs, which is also why loops lose gain at high frequency.

## 5. Connections

- [[Frequency Response and Resonance Curves]] and [[Filter Theory]] — Bode plots of RLC circuits and filters, the same building blocks.
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] — $G(j\omega)$ as a rotating phasor: amplitude and phase.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — instability at a critical parameter, here the critical gain $K_u$.
- [[PID Control and Tuning]] — $K_u$ and $P_u$ in Ziegler–Nichols are the gain and period at the phase crossover.
- [[Feedback, Block Diagrams and Transfer Functions]] — the closed-loop transfer function whose poles Nyquist tests indirectly.
