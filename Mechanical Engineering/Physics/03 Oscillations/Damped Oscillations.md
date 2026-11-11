---
tags: [concept, physics-1, PH1010, oscillations, damping]
status: draft
up: "[[Physics I - MOC]]"
aliases: [damped harmonic oscillator, underdamped, overdamped, critical damping, quality factor, logarithmic decrement]
---

# Damped Oscillations

> [!abstract] The big idea
> Add a drag force $-b\dot x$ to the spring and the equation stays linear, so the answer is still $e^{rt}$ with two roots. What changes is the *kind* of roots: complex (the motion rings and fades), repeated (the fastest fade without overshoot) or real and negative (a slow creep). One parameter, $\beta/\omega_0$, picks the regime.

## Governing relation

$$m\ddot x=-kx-b\dot x\;\Longrightarrow\;\ddot x+2\beta\dot x+\omega_0^2x=0,\qquad\beta=\frac{b}{2m},\quad\omega_0=\sqrt{\frac km}$$

Try $x=e^{rt}$: $r^2+2\beta r+\omega_0^2=0$, so $r_\pm=-\beta\pm\sqrt{\beta^2-\omega_0^2}$.

| Regime | Condition | Roots | Motion |
|---|---|---|---|
| **Underdamped** | $\beta<\omega_0$ | $-\beta\pm i\omega_1$, $\ \omega_1=\sqrt{\omega_0^2-\beta^2}$ | $e^{-\beta t}\cos(\omega_1t+\varphi)$: rings and fades |
| **Critical** | $\beta=\omega_0$ | $-\beta$ (double) | $(C_1+C_2t)e^{-\beta t}$: fastest return, no overshoot |
| **Overdamped** | $\beta>\omega_0$ | two real, both negative | $C_1e^{r_+t}+C_2e^{r_-t}$: slow creep |

## Visual

![[PH-damped-regimes.png]]

**Figure:** Left, releases from rest for $\beta=0.1\omega_0$ (rings inside the dotted envelope $e^{-\beta t}$), $\beta=\omega_0$ (green, fastest) and $\beta=3\omega_0$ (orange, slowest to settle). Right, the roots travel around a circle of radius $\omega_0$ as $\beta$ grows, collide on the real axis at $\beta=\omega_0$ and then split apart; the slow root $-\beta+\sqrt{\beta^2-\omega_0^2}\to0$ is why heavy damping is sluggish.

> [!question]- 🎯 Predict first: is *more* damping always faster to settle?
> No. Past critical damping the slow root $r_+=-\beta+\sqrt{\beta^2-\omega_0^2}$ moves *towards zero*, so the system takes longer. Door closers and car dampers are tuned near critical for exactly this reason: below it you bounce, above it you creep.

## Quality factor

$$Q=\frac{\omega_0}{2\beta}=\frac{\sqrt{km}}{b},\qquad \text{energy lost per cycle}\approx\frac{2\pi}{Q}E,\qquad \text{ring-down time}\approx\frac{2Q}{\omega_0}\ \ (\text{amplitude falls to }1/e\text{ in }1/\beta)$$

High $Q$ means many oscillations before decay (a tuning fork, $Q\sim10^3$); low $Q$ means the oscillation dies quickly. Underdamped systems satisfy $Q>\tfrac12$; critical damping is $Q=\tfrac12$.

## Method

1. **Write the equation in standard form** $\ddot x+2\beta\dot x+\omega_0^2x=0$ and read off $\beta,\omega_0$.
2. **Compare $\beta$ with $\omega_0$** to choose the regime.
3. **Write the roots** and the matching solution.
4. **Fix the two constants** from $x(0)$ and $\dot x(0)$.
5. **Check:** $\beta\to0$ must return plain SHM; $x\to0$ as $t\to\infty$ in every case.

## Common traps

> [!warning]- ⚠️ The damped frequency is not $\omega_0$
> The ringing is at $\omega_1=\sqrt{\omega_0^2-\beta^2}<\omega_0$. Damping lowers the frequency slightly (a barely audible drop for a bell, large when $\beta\to\omega_0$).

> [!warning]- ⚠️ Peaks do not sit on the envelope exactly
> For a general $\varphi$ the maxima fall a little *inside* $\pm e^{-\beta t}$. The envelope is a bound, not a path.

> [!danger]- 💥 Mixing up $b$, $\beta$ and $\gamma$
> Books use $\gamma=b/m=2\beta$ or $\beta=b/2m$. Check the definition before comparing with a formula sheet: critical damping is $b=2\sqrt{km}$, $\beta=\omega_0$, $\gamma=2\omega_0$.

## Worked example

> [!example]- 🔬 $m=0.2$ kg, $k=20$ N/m, $b=0.8$ kg/s. Which regime? How long for the amplitude to fall to $1/e$? What $b$ makes it critical?
> $\omega_0=\sqrt{20/0.2}=10$ rad/s and $\beta=0.8/0.4=2$ s$^{-1}$, so $\beta<\omega_0$: **underdamped**.
> $\omega_1=\sqrt{100-4}=9.80$ rad/s. The envelope $e^{-\beta t}$ falls to $1/e$ in $1/\beta=0.5$ s. $Q=\omega_0/2\beta=2.5$.
> Critical: $b_c=2\sqrt{km}=2\sqrt{4}=4$ kg/s, five times larger.
> **Check:** at $b_c$, $\beta=b_c/2m=10=\omega_0$ ✓.

## Quick quiz

> [!question]- Q1. A swing's amplitude halves every 3 swings. Roughly what is $Q$?
> Halving in 3 periods means $e^{-\beta\cdot3T}=\tfrac12$, so $\beta T=\ln2/3=0.231$. Since $T\approx2\pi/\omega_0$, $Q=\omega_0/2\beta=\pi/(\beta T)=\pi/0.231\approx13.6$.

> [!question]- Q2. Which regime returns to equilibrium fastest from a *non-zero* start, without crossing it?
> Critical damping (for most initial conditions). Underdamped crosses and overshoots; overdamped is slower.

> [!question]- Q3. In the root plot, what do the two points on the real axis for $\beta=3\omega_0$ tell you?
> They are $-0.17\omega_0$ (slow, dominates the long-time behaviour) and $-5.83\omega_0$ (fast, dies almost at once). The motion is mostly the slow mode.

## Connections

### Prerequisites
- [[Simple Harmonic Motion]]

### Next
- [[Driven Oscillations and Resonance]]
- [[Phase Space and Phase Portraits]]: damped motion spirals into the origin.

### Cross-domain links
- [[Series RLC Natural Response - Damping Cases]] and [[Parallel RLC Natural Response - Damping Cases]]: identical regimes with $R/2L$ in place of $\beta$.
- [[2nd Order Linear ODE with Constant Coefficients]]: the three root cases (complex, repeated, distinct real) are the three regimes.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]]: the envelope $e^{-\beta t}$ is a time-constant decay with $\tau=1/\beta$.
- [[The Universal Second-Order Linear System]]: $\zeta=\beta/\omega_0$ here; it is the same $\zeta$ in control and circuit theory.

## Self-check
- [ ] I can classify a damped oscillator from $m,k,b$ and write its solution.
- [ ] I can explain why critical damping is not the slowest, and why overdamping is slow.
- [ ] I can estimate $Q$ from how many swings the amplitude takes to fall.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Physics I - MOC]]
