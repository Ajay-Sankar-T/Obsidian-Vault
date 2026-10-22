---
tags:
  - EE1100
  - RLC
  - DC
  - step-response
  - graphs
up: "[[RLC Circuits - Responses]]"
---

# DC Step Response of RLC Circuits

← up: [[RLC Circuits - Responses|RLC Circuits — Responses]] · builds on: [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]]

## What "DC step response" means

A DC source is suddenly switched on (or a switch changes the circuit configuration) at $t=0$, and the source value is **constant** thereafter. The response is entirely: initial condition → transient (natural response, shaped by $\alpha,\omega_n$) → **constant** final value.

$$\boxed{x(t)=x_\infty+(x_0-x_\infty)e^{-t/\tau}\ \ \text{(first order)}}\qquad\boxed{x(t)=x_\infty+x_n(t)\ \ \text{(second order, }x_n\text{ from the damping-case table)}}$$

## The graph

![DC step response, RC circuit](dc_vs_ac_step_response.png)

*(left panel)* — the classic single-exponential rise to a constant final value $x_\infty$, from [[04 Capacitors, Inductors and First Order Circuits|Week 4]]'s three-value recipe. For a second-order (RLC) DC step, see the damping-case graphs in [[Series RLC Natural Response - Damping Cases|Series RLC Natural Response]] and [[Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response]] — same idea, just the transient can now *overshoot and ring* before settling, which a first-order RC/RL circuit can never do (a first-order system has only one time constant and no oscillatory mode).

## Why DC step response can never oscillate for first-order, but can for second-order

A first-order circuit's characteristic equation is linear in $s$ ($s+1/\tau=0$) — exactly **one** real root, exactly one exponential mode, no possibility of a complex-conjugate pair and hence no oscillation. A second-order circuit's characteristic equation ($s^2+2\alpha s+\omega_n^2=0$) can have a complex-conjugate root pair whenever $\zeta<1$, and it's precisely that complex pair that produces the $\cos\omega_dt,\sin\omega_dt$ oscillatory terms. This is why **ringing is fundamentally a two-(or-more)-storage-element phenomenon** — you need at least one $L$ *and* one $C$ (or two of the same kind coupled) for a circuit to be capable of oscillating at all, DC or AC.

## The DC step procedure (recap, generalized to second order)

1. Find $x(0^+)$ from continuity ($v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$).
2. Find $x(\infty)$ by re-solving the circuit in **true DC steady state** (capacitor → open, inductor → short — valid here *because* the source is genuinely DC, unlike the AC case in [[AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response]]).
3. Find $\alpha,\omega_n$ (or $\tau$ for first order) from the circuit's own $R,L,C$.
4. Classify the damping case and write the matching template from the damping-case notes.
5. Apply initial conditions to solve for the remaining constants.

## Related
- [[04 Capacitors, Inductors and First Order Circuits|Week 4 — First-order DC transients]]
- [[Series RLC Natural Response - Damping Cases|Series RLC Natural Response — Damping Cases]]
- [[AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response of RLC Circuits]]
