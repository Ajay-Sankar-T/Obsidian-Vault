---
tags:
  - EE1100
  - RLC
  - series
  - graphs
up: "[[RLC Circuits - Responses]]"
---

# Series RLC Natural Response — Damping Cases

← up: [[RLC Circuits - Responses|RLC Circuits — Responses]] · builds on: [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients]]

## Circuit and governing equation

A series RLC loop (source, $R$, $L$, $C$ in one series path) driven by a DC step of magnitude $V_f$, with initial conditions $i(0)=0$ and $v_C(0)=0$:

$$LC\frac{d^2v_C}{dt^2}+RC\frac{dv_C}{dt}+v_C=V_f$$

$$\alpha=\frac{R}{2L}\ (\text{damping coefficient}),\qquad \omega_n=\frac1{\sqrt{LC}}\ (\text{undamped natural frequency}),\qquad \zeta=\frac\alpha{\omega_n}=\frac R2\sqrt{\frac CL}$$

Critical resistance: $R_c=2\sqrt{L/C}$ (the value of $R$ at which $\alpha=\omega_n$, i.e. $\zeta=1$).

## The graph

![Series RLC step response, three damping cases](series_rlc_step_damping_cases.png)

All three curves solve the *same* circuit topology with the *same* $L,C$ (hence the same $\omega_n$) and only $R$ changed, expressed as a multiple of $R_c$.

## Reading the three curves

**Underdamped ($R=0.3R_c$, $\zeta<1$, blue):** $v_C(t)$ overshoots the final value and **rings** — decaying oscillation at $\omega_d=\sqrt{\omega_n^2-\alpha^2}$ before settling. This is the regime most real circuits with light resistance fall into, and the one where "ringing" and "overshoot" become practical design concerns (e.g. in switching power supplies).

**Critically damped ($R=R_c$, $\zeta=1$, green):** the fastest possible approach to the final value **without** overshoot — the boundary case, $v_C(t)=V_f\left[1-e^{-\alpha t}(1+\alpha t)\right]$. This is the design target for systems (servo controls, some measurement instruments) where speed matters but overshoot is unacceptable.

**Overdamped ($R=3R_c$, $\zeta>1$, red):** approaches the final value slowly and monotonically, with **no** oscillation — the large resistance dissipates energy fast enough that the circuit never "rings."

## Why all three eventually reach the same final value

Regardless of $R$, as $t\to\infty$ the capacitor charges to the full source voltage $V_f$ (the inductor eventually behaves as a short in true DC steady state, and no current flows through the loop once $v_C=V_f$, so there's no steady voltage drop across $R$ or $L$) — $R$ only controls **how** the circuit gets there, never **where** it ends up. This is the practical illustration of [[The Universal Second-Order Linear System|The Universal Second-Order Linear System]]'s point that damping never moves the system's equilibrium/eigenvalue location, only the *path* to it.

## Related
- [[Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response — Damping Cases]]
- [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients]]
