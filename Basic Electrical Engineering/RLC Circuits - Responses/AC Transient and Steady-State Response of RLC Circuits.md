---
tags:
  - EE1100
  - RLC
  - AC
  - transient
  - graphs
up: "[[RLC Circuits - Responses]]"
---

# AC Transient and Steady-State Response of RLC Circuits

← up: [[RLC Circuits - Responses|RLC Circuits — Responses]] · builds on: [[AC Transients|AC Transients]]

## The defining difference from a DC step

$$\boxed{x(t)=\underbrace{x_{ss}(t)}_{\text{permanent sinusoid, from phasor analysis}}+\underbrace{x_n(t)}_{\text{decaying, from }\alpha,\omega_d}}$$

Unlike the [[DC Step Response of RLC Circuits|DC step response]], the "final value" here is **not a constant** — it's a sinusoid that persists forever, computed by ordinary phasor analysis ([[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]). Only the transient term $x_n(t)$ decays away.

## The graph

![AC transient response vs steady-state only](dc_vs_ac_step_response.png)

*(right panel)* — the gray dashed curve is the steady-state sinusoid alone ($i_{ss}(t)=I_m\sin(\omega t+\phi)$, what phasor analysis by itself gives you); the red curve is the **complete** response, $i_{ss}(t)+Ae^{-t/\tau}$, showing how the true response starts away from the pure sinusoid right after switching and converges onto it as the transient dies out. This is the single most important picture for understanding why "phasor analysis alone" answers a different question than "what happens right after the switch closes" — see [[AC Transients|AC Transients]]'s explicit warning about this.

## Reading the gap between the two curves

At $t=0$, the complete response and the steady-state-only curve are generally **not equal** — the gap between them at $t=0$ is exactly the initial value of the transient term, $x(0^+)-x_{ss}(0^+)$, fixed by the circuit's continuity conditions ($v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$). As $t$ grows past a few time constants $\tau$ (or $1/\alpha$ for second order), the gap shrinks to zero and the two curves become indistinguishable — this is literally what "steady state" means.

## Second-order AC case: transient oscillates at a *different* frequency than the source

For an RLC circuit (not just RC/RL), the transient term itself can be a decaying sinusoid at $\omega_d$, generally **different** from the source's own driving frequency $\omega$:

$$i(t)=I_m\sin(\omega t+\phi)+e^{-\alpha t}[A\cos\omega_dt+B\sin\omega_dt]$$

— two genuinely different oscillation frequencies superposed, one permanent (driven by the source) and one decaying (a property of the circuit's own $L,C,R$), exactly as detailed in [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients]]'s "transient frequency is NOT the source frequency" warning.

## Related
- [[AC Transients|AC Transients]]
- [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients (Series and Parallel RLC)]]
- [[DC Step Response of RLC Circuits|DC Step Response of RLC Circuits]]
