---
tags: [concept, physics-1, PH1010, kepler, orbits, gravity]
status: draft
up: "[[Physics I - MOC]]"
aliases: [Kepler's laws, Kepler's three laws, orbit equation, ellipse, conic sections, vis-viva, escape velocity, semi-latus rectum]
---

# Kepler's Laws and Orbits

> [!abstract] The big idea
> Three empirical rules found by Kepler from Tycho Brahe's data turn out to be *theorems* of Newtonian gravity. The orbit is a conic section with the Sun at one **focus** (I), the line to the planet sweeps equal areas in equal times (II, which is just angular momentum conservation), and $T^2\propto a^3$ (III). Together with the vis-viva equation they answer almost every orbital question in a line.

> [!quote] 🪐 Kepler, 1619
> "I have stolen the golden vessels of the Egyptians... My book is written. To be read either now or by posterity, I care not which. It may well wait a century for a reader, as God has waited six thousand years for an observer."

## Governing relations

With $u=1/r$ the orbit equation for $V=-k/r$ is $u''+u=mk/L^2$, giving

$$r(\phi)=\frac{\ell}{1+e\cos\phi},\qquad\ell=\frac{L^2}{mk},\quad e=\sqrt{1+\frac{2EL^2}{mk^2}}$$

| $e$ | $E$ | Orbit |
|---|---|---|
| $0$ | $-mk^2/2L^2$ (minimum) | circle |
| $0<e<1$ | $E<0$ | ellipse |
| $1$ | $E=0$ | parabola |
| $>1$ | $E>0$ | hyperbola |

**Ellipse geometry** (semi-major $a$, semi-minor $b=a\sqrt{1-e^2}$): $\ell=a(1-e^2)$, pericentre $r_p=a(1-e)$, apocentre $r_a=a(1+e)$, area $\pi ab$, energy $E=-\dfrac{k}{2a}$.

## The three laws

![[PH-conics.png]]

**Figure:** The same focus and semi-latus rectum $\ell$; increasing $e$ stretches the circle into ellipses, the parabola and the hyperbola.

![[PH-kepler-laws.png]]

**Figure:** Left, Kepler I and II for $e=0.6$: the blue wedge near the Sun and the orange wedge far away have equal areas and take equal times, so the planet is **fast near the Sun, slow far away**. Right, Kepler III: $T$ against $a$ for the eight planets falls on a straight line of slope $1.500$ on log–log axes.

1. **First law:** orbit is an ellipse with the Sun at one focus.
2. **Second law:** $\dfrac{dA}{dt}=\dfrac12r^2\dot\phi=\dfrac{L}{2m}=\text{const}$.
3. **Third law:** $T^2=\dfrac{4\pi^2}{GM}a^3$ (for $m\ll M$).

**Vis-viva** (energy conservation at any point of an orbit of semi-major axis $a$):

$$v^2=GM\Big(\frac2r-\frac1a\Big)$$

Circular orbit ($r=a$): $v=\sqrt{GM/r}$. Escape ($a\to\infty$): $v_{\rm esc}=\sqrt{2GM/r}$.

> [!question]- 🎯 Predict first: where in its orbit is a planet fastest, and by what ratio compared with the slowest point?
> At pericentre. Angular momentum gives $r_pv_p=r_av_a$, so $v_p/v_a=r_a/r_p=\dfrac{1+e}{1-e}$. For Earth ($e=0.0167$) that is only $1.034$; for Halley's comet ($e=0.967$) it is $59$.

## Method

1. **Find $E$ and $L$** from the speed and direction at one point (or find $a$ and $e$ directly).
2. **Pick the question:** shape $\to e$; timing $\to$ Kepler III; speed at a given $r\to$ vis-viva; closest/farthest $\to r_p,r_a$.
3. **Apply the formula** and convert units ($1$ AU for $a$, years for $T$ is the quickest, since $T^2=a^3$).
4. **Check:** $T^2=a^3$ for the Sun reproduces Earth ($a=1$, $T=1$); $v_pr_p=v_ar_a$.

## Common traps

> [!warning]- ⚠️ The Sun is at a focus, not the centre
> The centre of the ellipse is empty. The Sun–planet distance ranges from $a(1-e)$ to $a(1+e)$.

> [!warning]- ⚠️ Kepler III uses the semi-major axis, not the average radius
> $a$ is half the long axis. The *time-averaged* distance is $a(1+e^2/2)$, slightly different for eccentric orbits.

> [!danger]- 💥 Thinking a faster satellite "goes higher"
> A satellite given a forward burn does rise, but on the *opposite* side of its new orbit; on a circular orbit, a higher orbit is *slower*. The speed $v=\sqrt{GM/r}$ falls as $r$ grows. This is why catching up to a satellite means dropping to a lower orbit first.

## Worked examples

> [!example]- 🔬 Halley's comet has period $75.3$ yr and $e=0.967$. Find $a$, perihelion and aphelion
> Kepler III in AU and years: $a=T^{2/3}=75.3^{2/3}=17.8$ AU.
> $r_p=a(1-e)=17.8(0.033)=0.59$ AU (between Mercury and Venus), $r_a=a(1+e)=35.1$ AU (beyond Neptune).
> **Check:** $r_p+r_a=2a=35.7$ AU ✓.

> [!example]- 🔬 What is the escape speed from Earth's orbit around the Sun?
> Earth's orbital speed is $29.78$ km/s, so $v_{\rm esc}=\sqrt2\times29.78=42.1$ km/s. A spacecraft leaving Earth already shares Earth's $29.8$ km/s, so to leave the Solar System it needs only $42.1-29.8=12.3$ km/s *relative to Earth* once clear of Earth's own gravity (launched along Earth's motion).

## Quick quiz

> [!question]- Q1. Mars has $a=1.524$ AU. What is its year?
> $T=1.524^{3/2}=1.88$ years (687 days).

> [!question]- Q2. Which law is angular momentum conservation?
> The second: $dA/dt=L/2m$. It holds for *any* central force, not only gravity.

> [!question]- Q3. A comet's speed at $r=1$ AU is $50$ km/s. Is it bound to the Sun?
> Escape from $1$ AU is $42.1$ km/s; $50>42.1$ so $E>0$: a hyperbolic, unbound orbit.

## Connections

### Prerequisites
- [[Central Forces and the Effective Potential]]

### Next
- [[Two-Body Problem and Hohmann Transfer]]

### Cross-domain links
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]]: an ellipse is the sum of two counter-rotating circles, the same decomposition used for elliptic polarisation and Lissajous figures.
- [[Second Moments of Area - One Integral, Many Jobs]]: the ellipse integrals ($\pi ab$) are the same geometry as the area integrals there.

## Self-check
- [ ] I can derive $r(\phi)$ and read $e$ from $E$ and $L$.
- [ ] I can use Kepler III and vis-viva without looking them up.
- [ ] I can explain why the Sun is at a focus and why speed varies around the orbit.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** advanced
- **Course map:** [[Physics I - MOC]]
