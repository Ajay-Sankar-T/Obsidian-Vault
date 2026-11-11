---
tags:
  - EE1100
  - AC-circuits
  - phasors
  - complex-numbers
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# Phasors and Complex Algebra

← up: [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[05 Sinusoids and Phasors|Week 5]], [[Sinusoidal Waveforms, RMS and Average Value|RMS and Average Value]]

## Why phasors exist

In the time domain, RLC element equations are differential ($v_L=L\,di/dt$, $i_C=C\,dv/dt$) — solving a circuit means solving simultaneous ODEs. A phasor freezes a sinusoid's amplitude and phase into a single complex number, turning differentiation/integration into multiplication/division by $j\omega$, and turning circuit analysis into ordinary complex-number algebra:

$$\bar V=\bar I Z$$

exactly like Ohm's law — see [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]] for why $Z$ absorbs the $j\omega$ entirely, leaving this one algebraic relation for R, L, and C alike.

## Definition

$$v(t)=V_m\sin(\omega t+\theta)\quad\longrightarrow\quad \bar V=\frac{V_m}{\sqrt2}\angle\theta$$

(RMS magnitude — see [[Sinusoidal Waveforms, RMS and Average Value|RMS and Average Value]] — with $\omega t$ dropped since it is common to every quantity in a fixed-frequency circuit).

## Polar ↔ rectangular conversion

**Polar → rectangular:** $A\angle\theta = A\cos\theta+jA\sin\theta = x+jy$.

**Rectangular → polar:** for $z=x+jy$, magnitude $|z|=\sqrt{x^2+y^2}$, angle $\theta=\tan^{-1}(y/x)$ — **always check the quadrant** of $(x,y)$ before trusting the calculator's principal value of $\tan^{-1}$; it silently drops $180°$ when $x<0$.

## The imaginary unit $j$

$$j=\sqrt{-1},\qquad j^2=-1,\qquad \frac1j=-j,\qquad j=e^{j90^\circ}$$

Powers cycle with period 4: $j^0=1,\ j^1=j,\ j^2=-1,\ j^3=-j,\ j^4=1,\ldots$ — this cycling is exactly why multiplying by $j$ is a $90°$ rotation, the geometric fact underlying every "$L$ leads by $90°$" / "$C$ lags by $90°$" statement.

## Phasor addition — vectors, not scalars

Phasors add as vectors, **not** as magnitudes:

$$\text{wrong: } I=I_1+I_2+I_3 \text{ (magnitudes)}\qquad\qquad \text{correct: } \bar I=\bar I_1+\bar I_2+\bar I_3\text{ (complex numbers)}$$

Procedure: convert every phasor to rectangular form, add real parts and imaginary parts separately, convert the sum back to polar. This is the mechanism behind combining parallel branch currents (KCL, see [[Nodal and Mesh Analysis (AC)|Nodal and Mesh Analysis (AC)]]) and series element voltages ($\bar V=\bar V_R+\bar V_L+\bar V_C$, see [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]).

**Worked pattern (Q6-style):** given $i(t)=I_m\sin(\omega t+\theta)$, convert to $\bar I=\frac{I_m}{\sqrt2}\angle\theta$; if a branch current is given as a cosine, first use $\cos\theta=\sin(\theta+90°)$ (see RMS note) before writing the phasor, then add rectangular components.

## Division of phasors (AC Ohm's law, polar shortcut)

If $V=V\angle\theta_V$ and $Z=Z\angle\theta_Z$:

$$I=\frac VZ=\frac{|V|}{|Z|}\angle(\theta_V-\theta_Z)\qquad\Longrightarrow\qquad \theta_I=\theta_V-\theta_Z$$

This single relation answers most "does current lead or lag" questions directly, without separately reasoning about each element — the sign of $\theta_Z$ (from $Z=R+jX$) tells you everything: $\theta_Z>0$ (inductive) means $I$ lags $V$; $\theta_Z<0$ (capacitive) means $I$ leads $V$.

## Converting back to the time domain

If $\bar X=X\angle\theta$ is an RMS phasor, the corresponding time-domain signal is

$$x(t)=\sqrt2\,X\sin(\omega t+\theta)$$

## Related
- [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]
- [[AC Power and Power Factor|AC Power and Power Factor]]
