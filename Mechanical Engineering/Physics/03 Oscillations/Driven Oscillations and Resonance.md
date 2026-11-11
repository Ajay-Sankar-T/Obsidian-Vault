---
tags: [concept, physics-1, PH1010, oscillations, resonance, driven]
status: draft
up: "[[Physics I - MOC]]"
aliases: [forced oscillations, driven harmonic oscillator, resonance, steady state, transient, LCR circuit, amplitude resonance]
---

# Driven Oscillations and Resonance

> [!abstract] The big idea
> Push a damped oscillator with $F_0\cos\omega t$ and the answer splits in two: a **transient** that rings at the system's own frequency and fades, and a **steady state** that oscillates at the *driver's* frequency forever. The steady-state amplitude is huge when you drive near $\omega_0$ (**resonance**), and the narrower the peak, the less damping the system has.

## Governing relation

$$\ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}{m}\cos\omega t$$

General solution = homogeneous (the damped solution from [[Damped Oscillations]]) + one particular solution. Try $x_p=D\cos(\omega t-\delta)$; the amplitude and phase come out as

$$D(\omega)=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}},\qquad\tan\delta=\frac{2\beta\omega}{\omega_0^2-\omega^2}$$

- **Low frequency** ($\omega\ll\omega_0$): $D\to F_0/k$ (static deflection), $\delta\to0$: the mass follows the push.
- **Resonance** ($\omega\approx\omega_0$): $\delta=90^\circ$, $D\approx\dfrac{F_0}{2m\beta\omega_0}=Q\dfrac{F_0}{k}$.
- **High frequency** ($\omega\gg\omega_0$): $D\to F_0/m\omega^2\to0$, $\delta\to180^\circ$: the mass cannot keep up and sits in anti-phase.

The amplitude peak is at $\omega_r=\sqrt{\omega_0^2-2\beta^2}$, slightly below $\omega_0$; for light damping the difference is negligible.

## Visual

![[PH-driven-resonance.png]]

**Figure:** Left, amplitude relative to the static deflection $F_0/k$ for several quality factors; the dots mark each peak. Right, the phase lag always passes $90^\circ$ at $\omega=\omega_0$, switching faster for higher $Q$.

![[PH-driven-transient.png]]

**Figure:** Starting from rest, the response first beats (own frequency fighting the driver's), then the transient decays and only the steady oscillation at amplitude $2.62$ remains. On the phase plane the path spirals out onto a closed **limit cycle** (the dashed ellipse).

> [!question]- 🎯 Predict first: halve the damping at resonance. What happens to the peak amplitude?
> It doubles. At resonance $D\propto1/\beta$. This is the practical meaning of "high $Q$ means a tall, narrow peak": soldiers break step on bridges for this reason.

> [!tip]- 🎢 The swing and the radio
> Pushing a child on a swing works because you push *in phase with the velocity* (that is the $\delta=90^\circ$ lag of displacement). Tuning a radio is the same plot: you slide $\omega_0=1/\sqrt{LC}$ until it sits on the station's frequency and the stations next to it fall on the steep skirts of the peak.

## Method

1. **Write the equation** with the force on the right and identify $\beta,\omega_0,\omega,F_0/m$.
2. **Steady state:** substitute $x_p=D\cos(\omega t-\delta)$ (or use complex $\hat x=\hat F/(\omega_0^2-\omega^2+2i\beta\omega)$) and read $D,\delta$.
3. **Add the transient** $x_h(t)$ and fix its two constants from the initial conditions applied to the *total* solution.
4. **Resonance questions:** peak at $\omega_r$, width $\Delta\omega\approx2\beta=\omega_0/Q$, peak height $QF_0/k$.
5. **Check:** $\omega\to0$ gives static deflection; $\beta\to0$ at $\omega=\omega_0$ gives infinite amplitude.

## Common traps

> [!warning]- ⚠️ Applying initial conditions to the particular solution
> $x_p$ alone does not satisfy $x(0)=x_0$. The constants $C_1,C_2$ live in the *homogeneous* part but must be solved using $x_h+x_p$ together.

> [!warning]- ⚠️ "Resonance means infinite amplitude"
> Only with zero damping. Any real damping caps the peak at $QF_0/k$.

> [!danger]- 💥 The steady state forgets the initial conditions
> After the transient fades, where you started is irrelevant. Two oscillators started differently converge to the *same* motion. That is what "attractor" means for the limit cycle.

## Worked example

> [!example]- 🔬 $\omega_0=10$ rad/s, $\beta=0.5$ s$^{-1}$, $F_0/m=1$ m/s². Find the peak amplitude, $Q$, and the amplitude when driven at $\omega=5$ and $\omega=20$
> $Q=\omega_0/2\beta=10$. Static deflection $F_0/k=(F_0/m)/\omega_0^2=0.01$ m. At resonance $D=Q\cdot0.01=0.10$ m (ten times static).
> At $\omega=5$: $D=\dfrac{1}{\sqrt{(100-25)^2+(2\cdot0.5\cdot5)^2}}=\dfrac{1}{\sqrt{5625+25}}=0.0133$ m, barely above static.
> At $\omega=20$: $D=\dfrac{1}{\sqrt{(100-400)^2+400}}=0.0033$ m, well below static.
> **Check:** the three values $0.0133,\;0.10,\;0.0033$ trace the peak in the figure.

## Quick quiz

> [!question]- Q1. What is the phase lag at resonance, and why does power transfer peak there?
> $90^\circ$ lag of displacement, so the *velocity* is exactly in phase with the force, and power $F\dot x$ is positive at all times.

> [!question]- Q2. A system has bandwidth $\Delta\omega=2$ rad/s around $\omega_0=100$ rad/s. What is $Q$?
> $Q=\omega_0/\Delta\omega=50$. Narrow peak, high $Q$.

> [!question]- Q3. Why does a car's suspension feel awful on a washboard road at one particular speed?
> The bumps arrive at a fixed spacing; at the speed where their frequency matches the suspension's $\omega_0$ you drive the system at resonance.

## Connections

### Prerequisites
- [[Damped Oscillations]], [[Simple Harmonic Motion]]

### Next
- [[Phase Space and Phase Portraits]]: the limit cycle is a phase-space picture of steady state.

### Cross-domain links
- [[Frequency Response and Resonance Curves]] and [[Series vs Parallel RLC - Key Distinctions]]: the RLC current peak at $1/\sqrt{LC}$ with bandwidth $R/L$ is this curve with $L\leftrightarrow m$, $R\leftrightarrow b$.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]]: structures fail when a load frequency lands on a natural frequency, the same peak.
- [[Undetermined Coefficients]]: finding $x_p$ for a $\cos\omega t$ right-hand side is exactly this method.
- [[The Universal Second-Order Linear System]] and [[Measurements, Instrumentation and Control - MOC]]: sensors and controllers are designed around this response.

## Self-check
- [ ] I can write $D(\omega)$ and $\delta(\omega)$ and sketch both.
- [ ] I can separate transient from steady state and say which depends on the initial conditions.
- [ ] I can relate $Q$ to peak height and bandwidth.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Physics I - MOC]]
