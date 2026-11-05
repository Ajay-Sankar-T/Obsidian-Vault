---
tags: [concept, physics-1, PH1010, oscillations, SHM]
status: draft
up: "[[Physics I - MOC]]"
aliases: [SHM, simple harmonic oscillator, harmonic oscillator, spring-mass system, small oscillations]
---

# Simple Harmonic Motion

> [!abstract] The big idea
> A restoring force proportional to displacement, $F=-kx$, gives $\ddot x=-\omega_0^2x$ and a pure sinusoid whose **frequency depends only on the system, never on how hard you start it**. Almost every stable system, near its equilibrium, looks like this: the potential well is a parabola up close. That is why SHM is the most reused model in physics.

> [!tip]- 🎢 Why it is everywhere
> Expand any smooth potential about a minimum: $U(x)=U_0+\tfrac12U''(x_0)(x-x_0)^2+\dots$. The linear term vanishes (it is an equilibrium), so the first thing left is a parabola, i.e. a spring. Atoms in a crystal, a bridge in the wind, a pendulum, an LC circuit: all the same equation at small amplitude.

## Visual

![[PH-shm-signals.png]]

**Figure:** Displacement, velocity and acceleration are the same wave shifted: velocity leads displacement by a quarter cycle, and acceleration is always opposite to displacement. Right, SHM is the shadow of uniform circular motion.

## Governing relation

$$m\ddot x=-kx\;\Longrightarrow\;\ddot x+\omega_0^2x=0,\qquad\omega_0=\sqrt{k/m},\quad T=\frac{2\pi}{\omega_0}$$

General solution (two constants, as for any second-order ODE):

$$x(t)=C_1\cos\omega_0t+C_2\sin\omega_0t=A\cos(\omega_0t+\varphi)=\operatorname{Re}\!\big[\,Ce^{i\omega_0t}\big]$$

The constants come from the start: $x(0)=x_0,\ \dot x(0)=0$ gives $A=x_0,\ \varphi=0$; $x(0)=0,\ \dot x(0)=v_0$ gives $x=(v_0/\omega_0)\sin\omega_0t$. In general $A=\sqrt{x_0^2+(v_0/\omega_0)^2}$.

> [!question]- 🎯 Predict first: you double the amplitude of a spring-mass oscillation. What happens to the period?
> Nothing. $T=2\pi\sqrt{m/k}$ has no $A$ in it. A pendulum clock keeps time whether the swing is small or a bit larger, to first approximation (see [[The Nonlinear Pendulum]] for when this breaks).

## Energy

![[PH-shm-energy.png]]

**Figure:** Left, potential and kinetic energy trade places twice per cycle while the total stays at $\tfrac12kA^2$. Right, at every position the gap between the energy line and the parabola is the kinetic energy; the turning points are where the line meets the parabola.

$$E=\tfrac12m\dot x^2+\tfrac12kx^2=\tfrac12kA^2=\tfrac12m\omega_0^2A^2,\qquad v_{\max}=A\omega_0,\quad a_{\max}=A\omega_0^2$$

## Method

1. **Find the restoring force** (or the potential) and check it is $-kx$ about the equilibrium.
2. **Read off $\omega_0^2$** as (coefficient of $x$) / (coefficient of $\ddot x$).
3. **Fix $A,\varphi$** from the initial position and velocity.
4. **Quote energy** as $\tfrac12kA^2$ for any later question.
5. **Check:** units of $\omega_0$ are s$^{-1}$; $v_{\max}=A\omega_0$ must beat any speed in the problem.

## Common traps

> [!warning]- ⚠️ Taking "$\omega$" for the number of cycles per second
> $\omega_0$ is in rad/s; the frequency is $f=\omega_0/2\pi$ in Hz. A factor $2\pi$ error is the most common SHM slip.

> [!warning]- ⚠️ Vertical spring: forgetting the offset
> Hanging a mass shifts the equilibrium to $x_{\rm eq}=mg/k$, but $\omega_0=\sqrt{k/m}$ is unchanged. Measure $x$ from the *new* equilibrium and gravity disappears from the equation.

> [!danger]- 💥 "Small oscillations" is not a courtesy phrase
> It is the assumption that lets $\sin\theta\approx\theta$ (or $U\approx$ parabola). Without it, the period depends on amplitude.

## Worked example

> [!example]- 🔬 A $0.5$ kg mass on a $200$ N/m spring is pulled $5$ cm and released. Find $T$, $v_{\max}$, $a_{\max}$ and $E$
> $\omega_0=\sqrt{200/0.5}=20$ rad/s, so $T=2\pi/20=0.314$ s.
> $v_{\max}=A\omega_0=0.05\cdot20=1.0$ m/s and $a_{\max}=A\omega_0^2=0.05\cdot400=20$ m/s².
> $E=\tfrac12kA^2=\tfrac12(200)(0.05)^2=0.25$ J.
> **Check:** $\tfrac12mv_{\max}^2=\tfrac12(0.5)(1)^2=0.25$ J ✓. All the energy is kinetic at the centre.

## Quick quiz

> [!question]- Q1. Where is the speed of an SHM oscillator largest, and where is the acceleration largest?
> Speed is largest at the equilibrium ($x=0$); acceleration is largest at the turning points ($x=\pm A$). They are never largest at the same place.

> [!question]- Q2. Two springs of constant $k$ in *parallel* carry a mass $m$. What is the new $\omega_0$?
> Parallel springs add, $k_{\rm eff}=2k$, so $\omega_0=\sqrt{2k/m}$, a factor $\sqrt2$ faster. In *series* the stiffness halves instead.

> [!question]- Q3. Why is the phase $\varphi$ needed if $C_1,C_2$ already give two constants?
> $A$ and $\varphi$ are the polar form of $(C_1,C_2)$: $C_1=A\cos\varphi$, $C_2=-A\sin\varphi$. Both forms hold the same two numbers.

## Connections

### Prerequisites
- [[Newton's Laws as Differential Equations]], [[Newton's Second Law in Polar Coordinates]] (pendulum)

### Next
- [[Damped Oscillations]]: add friction.
- [[Driven Oscillations and Resonance]]: add a push.
- [[Energy and Equilibrium in One Dimension]]: why the parabola is universal.

### Cross-domain links
- [[2nd Order Linear ODE with Constant Coefficients]]: $r^2+\omega_0^2=0$ has purely imaginary roots $\pm i\omega_0$.
- [[The Universal Second-Order Linear System]]: spring-mass, series LC and torsion pendulum are one system with relabelled symbols.
- [[The Mechanical-Electrical Analogy (Impedance Analogy)]]: mass ↔ inductance, spring ↔ 1/capacitance, so $\omega_0=1/\sqrt{LC}$ is the same formula.
- [[Euler Buckling of Columns]]: a column's first mode is an oscillator with the sign of $k$ flipped.

## Self-check
- [ ] I can derive $\omega_0=\sqrt{k/m}$ and say why $T$ ignores the amplitude.
- [ ] I can find $A$ and $\varphi$ from $x_0$ and $v_0$.
- [ ] I can sketch $x$, $v$ and $a$ on one axis with the right phase shifts.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner
- **Course map:** [[Physics I - MOC]]
