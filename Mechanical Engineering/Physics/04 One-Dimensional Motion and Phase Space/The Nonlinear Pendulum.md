---
tags: [concept, physics-1, PH1010, pendulum, nonlinear, phase-space]
status: draft
up: "[[Physics I - MOC]]"
aliases: [plane pendulum, large-amplitude pendulum, pendulum period, separatrix, libration, rotation]
---

# The Nonlinear Pendulum

> [!abstract] The big idea
> A real pendulum has $\ddot\theta=-\omega_0^2\sin\theta$, not $-\omega_0^2\theta$. The $\sin$ saturates, so large swings take **longer**, the time-trace is no longer a cosine, and the phase portrait has a new feature the oscillator never had: a **separatrix** that splits back-and-forth swinging from going round and round.

## Governing relation

Lagrangian-free derivation: tangential equation $mL\ddot\theta=-mg\sin\theta$ and energy

$$E=\tfrac12mL^2\dot\theta^2-mgL\cos\theta=\text{const},\qquad\omega_0^2=g/L$$

**Period for amplitude $\theta_0$** (from the energy integral):

$$T(\theta_0)=\frac{4}{\omega_0}K\!\big(\sin\tfrac{\theta_0}{2}\big)=T_0\Big(1+\frac{\theta_0^2}{16}+\frac{11\,\theta_0^4}{3072}+\cdots\Big),\qquad T_0=2\pi\sqrt{L/g}$$

where $K$ is the complete elliptic integral of the first kind. As $\theta_0\to\pi$ (balanced upside down) $T\to\infty$.

## Visual

![[PH-phase-pendulum.png]]

**Figure:** Phase portrait ($\dot\theta/\omega_0$ vs $\theta$). Around $\theta=0$ the closed loops are **libration** (swinging). The red curve is the **separatrix** at $E=mgL$ through the unstable upside-down points $\pm\pi$. Above it, $\dot\theta$ never changes sign: the pendulum **rotates** over the top. Periodic in $\theta$ with period $2\pi$.

![[PH-pendulum-period.png]]

**Figure:** Left, $T/T_0$ rises from 1 and diverges as $\theta_0\to180^\circ$; the first correction $1+\theta_0^2/16$ is good to $\sim1\%$ below $90^\circ$ but not beyond. Right, large swings are flattened and slowed near their turning points.

> [!question]- 🎯 Predict first: a pendulum is released from $90^\circ$. By what percentage is its period longer than the small-angle value?
> About $18\%$ ($T/T_0=1.180$). For $10^\circ$ it is only $0.2\%$; for $150^\circ$ it is $76\%$. This is why "the period does not depend on amplitude" is only a small-angle statement.

> [!tip]- 🎢 The knife-edge
> Just *below* the separatrix the pendulum climbs almost to the top and hangs there for a long time before falling back; just *above* it, it creeps over the top and spins. A tiny change in energy sends it into a completely different regime: that is what "extremely sensitive to initial conditions" means in the portrait.

## Regimes

| Energy | Motion | Phase curve |
|---|---|---|
| $E=-mgL$ | at rest at the bottom | the point $(0,0)$ |
| $-mgL<E<mgL$ | libration, period $T(\theta_0)$ | closed loop around $(0,0)$ |
| $E=mgL$ | takes infinite time to reach the top | separatrix |
| $E>mgL$ | rotation, passes the top with $\dot\theta\neq0$ | open wavy line |
| with damping | spirals into $(0,0)$ | decaying spiral (stays a spiral down to the centre) |

## Method

1. **Write the energy:** $E=\tfrac12mL^2\dot\theta^2-mgL\cos\theta$.
2. **Compare $E$ with $mgL$** to decide libration or rotation.
3. **Find the amplitude** from $E=-mgL\cos\theta_0$.
4. **Small amplitude?** Use $T_0$; moderate? use $T_0(1+\theta_0^2/16)$; large? use $K$.
5. **Check:** $\theta_0\to0$ recovers SHM; $E=mgL$ gives $\theta_0=\pi$ and $T\to\infty$.

## Common traps

> [!warning]- ⚠️ Applying the $\theta_0^2/16$ correction in degrees
> $\theta_0$ is in **radians** in the series. $90^\circ=1.571$ rad gives $1+0.154=1.154$ (versus the exact $1.180$).

> [!warning]- ⚠️ Confusing the pendulum's angle $\theta$ with the phase of SHM
> $\theta$ is the physical angle; in SHM the phase is $\omega_0t+\varphi$. In the nonlinear pendulum $\theta(t)$ is *not* $\theta_0\cos\omega t$.

> [!danger]- 💥 Forgetting a rotating pendulum is also "periodic"
> A pendulum with $E>mgL$ goes round with a repeating $\dot\theta(t)$, but its angle just keeps increasing. In the portrait it is an open curve; in a cylinder-shaped phase space (identify $\theta$ and $\theta+2\pi$) it is a closed loop.

## Worked example

> [!example]- 🔬 $L=1$ m pendulum released from rest at $90^\circ$. Find the period; check it against the series
> $T_0=2\pi\sqrt{1/9.81}=2.006$ s. Exact: $T/T_0=\tfrac{2}{\pi}K(\sin45^\circ)=1.1803$, so $T=2.368$ s.
> Series: $1+\theta_0^2/16=1+(\pi/2)^2/16=1.154$; adding the next term $\tfrac{11}{3072}\theta_0^4=0.0218$ gives $1.176$, within $0.4\%$ of exact.
> At the bottom: $v=\sqrt{2gL}=4.43$ m/s ($\dot\theta=4.43$ rad/s), and $E=-mgL\cos90^\circ=0$, below the separatrix value $mgL$.

## Quick quiz

> [!question]- Q1. At what speed at the bottom does a pendulum of length $L$ just reach the top?
> It needs $E=mgL$ at the bottom: $\tfrac12mv^2-mgL=mgL\Rightarrow v=2\sqrt{gL}$. (For a rod; a string needs more, because it goes slack.)

> [!question]- Q2. In the portrait, why are $(\pm\pi,0)$ saddles?
> They are the inverted positions: equilibria with $U''=mgL\cos\pi<0$, unstable.

> [!question]- Q3. How does damping change the portrait?
> Loops become spirals into $(0,0)$. A pendulum that starts above the separatrix first spins several times, loses energy, then drops below the separatrix and starts swinging.

## Connections

### Prerequisites
- [[Phase Space and Phase Portraits]], [[Newton's Second Law in Polar Coordinates]], [[Simple Harmonic Motion]]

### Next
- [[Euler-Lagrange Equations]]: the pendulum is the standard first Lagrangian example.

### Cross-domain links
- [[Euler Buckling of Columns]]: large-deflection (elastica) buckling gives the same elliptic integrals as the large-amplitude pendulum.
- [[Energy Methods - A Unified View]]: $E=\tfrac12 I\dot\theta^2+U(\theta)$ is the energy method applied to a rotor.
- [[The Universal Second-Order Linear System]]: valid only for amplitudes small enough to linearise, as here.

## Self-check
- [ ] I can compute the period for any amplitude using the series or $K$.
- [ ] I can sketch the full portrait and label libration, rotation and separatrix.
- [ ] I can say what happens to $T$ and the portrait with damping.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate–advanced
- **Course map:** [[Physics I - MOC]]
