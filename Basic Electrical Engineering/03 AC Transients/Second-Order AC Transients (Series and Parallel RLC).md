---
tags:
  - EE1100
  - AC-circuits
  - transients
  - second-order
  - RLC
up: "[[AC Transients]]"
---

# Second-Order AC Transients (Series and Parallel RLC)

← up: [[AC Transients|AC Transients]] · builds on: [[Concepts#RC/RL Transients and Time Constant|RC/RL Transients and Time Constant]] (damping cases), [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] Q10–Q12

## Structure of the response

$$\boxed{\text{Complete response} = \text{AC steady state} + \text{natural RLC response}}$$

The natural part's *type* (over/critical/underdamped) is a property of the circuit alone (R, L, C values), independent of whether the drive is DC or AC — this is exactly the same classification Tutorial 2 builds for DC-switched RLC circuits; only the forced term changes from a constant to a sinusoid.

## Series RLC characteristic equation

$$LC\frac{d^2i}{dt^2}+RC\frac{di}{dt}+i=0 \quad\Longrightarrow\quad s^2+\frac RLs+\frac1{LC}=0$$

Define $\alpha=\dfrac{R}{2L}$ (damping coefficient) and $\omega_n=\dfrac1{\sqrt{LC}}$ (undamped natural frequency — the same $\omega_n$ that sets the resonant frequency in [[08 Resonance and Magnetically Coupled Circuits|Week 8]]):

$$s^2+2\alpha s+\omega_n^2=0,\qquad \zeta=\frac{\alpha}{\omega_n}=\frac R2\sqrt{\frac CL}\ \text{(damping ratio)}$$

## Three damping cases

**Overdamped** ($\zeta>1$, $\alpha>\omega_n$): real distinct roots $s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_n^2}$,
$$x_n(t)=Ae^{s_1t}+Be^{s_2t}\quad(\text{no oscillation})$$

**Critically damped** ($\zeta=1$, $\alpha=\omega_n$): repeated root $s=-\alpha$,
$$x_n(t)=(A+Bt)e^{-\alpha t}\quad(\text{fastest non-oscillatory decay})$$

**Underdamped** ($\zeta<1$, $\alpha<\omega_n$), with damped frequency $\omega_d=\sqrt{\omega_n^2-\alpha^2}$:
$$x_n(t)=e^{-\alpha t}\big[A\cos\omega_dt+B\sin\omega_dt\big]\quad(\text{decaying sinusoid})$$

**Critical resistance** (boundary between over/underdamped, $\alpha=\omega_n$):
$$R_c=2\sqrt{\frac LC} \qquad\Rightarrow\qquad R>R_c:\text{overdamped},\quad R=R_c:\text{critical},\quad R<R_c:\text{underdamped}$$

This matches the classification already used for the DC-switched RLC example in [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] Q10 ($R_c=89.44\ \Omega$, $\zeta=0.559$, $\omega_n=447.2\ \text{rad/s}$, $\omega_d=370.8\ \text{rad/s}$, underdamped).

## Complete response under AC drive (underdamped case)

$$\boxed{x(t)=x_{ss,AC}(t)+e^{-\alpha t}\big[A\cos\omega_dt+B\sin\omega_dt\big]}$$

e.g. $i(t)=I_m\sin(\omega t+\phi)+e^{-\alpha t}[A\cos\omega_dt+B\sin\omega_dt]$, where $I_m,\phi$ come from ordinary phasor analysis ([[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]) and $\alpha,\omega_d$ come from the natural-response analysis above. $A,B$ are found from $i(0^+)$ and $\dot i(0^+)$ (two initial conditions are needed for a second-order system, unlike the single condition for first order).

## The transient frequency is NOT the source frequency

If the source drives at $\omega=1000\ \text{rad/s}$ but the circuit's own $\omega_d=500\ \text{rad/s}$, the response contains **both**: a forced oscillation at $1000\ \text{rad/s}$ that persists forever, and a decaying transient oscillation at $500\ \text{rad/s}$ that dies out:

$$i(t)=I_m\sin(1000t+\phi)+e^{-\alpha t}[A\cos500t+B\sin500t]$$

The transient frequency is a property of the circuit's own $L,C,R$ ($\omega_d$), completely independent of the driving frequency $\omega$ — easy to conflate the two since both are angular frequencies in rad/s.

## Parallel RLC

Natural equation for the node voltage:
$$\frac{d^2v}{dt^2}+\frac1{RC}\frac{dv}{dt}+\frac1{LC}v=0 \quad\Longrightarrow\quad \alpha=\frac1{2RC},\qquad \omega_n=\frac1{\sqrt{LC}}$$
with $\omega_d=\sqrt{\omega_n^2-\alpha^2}$ and $\zeta=\dfrac1{2R}\sqrt{L/C}$ computed the same way as series RLC, just with $\alpha$ built from $1/(2RC)$ instead of $R/(2L)$ — note $R$ appears in the *denominator* of $\alpha$ for parallel RLC (a large $R$ under-damps a parallel circuit) versus the *numerator* for series RLC (a large $R$ over-damps a series circuit) — a frequent sign-confusion trap.

## Series vs parallel RLC cheat table

| Quantity | Series RLC | Parallel RLC |
|---|---:|---:|
| $\omega_n$ | $1/\sqrt{LC}$ | $1/\sqrt{LC}$ |
| $\alpha$ | $R/(2L)$ | $1/(2RC)$ |
| $\omega_d$ | $\sqrt{\omega_n^2-\alpha^2}$ | same form |
| $\zeta$ | $\frac R2\sqrt{C/L}$ | $\frac1{2R}\sqrt{L/C}$ |
| Large $R$ effect | more damping (overdamped) | less damping (underdamped) |

## Switching rules recap

$$v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-)$$

but $i_C$, $v_L$ may jump — see [[AC Transients|AC Transients]] for the full continuity discussion, and the connection to buckling-type ODEs (a different physical system with the same $s^2+2\alpha s+\omega_n^2=0$ mathematical skeleton) in [[Euler Buckling of Columns|Euler Buckling of Columns]] in the Strength of Materials vault.

## Related
- [[RLC Circuits - Responses|Plotted graphs of all these damping cases (series and parallel, DC and AC)]]
- [[The Universal Second-Order Linear System|Cross-domain: this equation is literally column buckling and any spring-mass-damper]]
- [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2 — DC RLC transients]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]] ($\omega_n$ reappears as the resonant frequency)
- [[First-Order AC Transients (RC and RL)|First-Order AC Transients (RC and RL)]]

## See also
- [[Frequency Response and Resonance Curves]] — sharpness in frequency and ringing in time are two views of the same damping.
- [[Series vs Parallel RLC - Key Distinctions]] — series/parallel duality table.
