---
tags: [concept, physics-1, PH1010, newton, polar-coordinates, pendulum]
status: draft
up: "[[Physics I - MOC]]"
aliases: [polar coordinates, radial and transverse acceleration, circular pendulum, conical pendulum, plane pendulum]
---

# Newton's Second Law in Polar Coordinates

> [!abstract] The big idea
> When a problem has a centre (a pendulum, an orbit, a spinning bead) Cartesian axes fight you. Polar axes $\hat r,\hat\phi$ follow the particle, so *radial* force and *tangential* force separate cleanly. The price is that the unit vectors themselves turn, and that turning is where the "extra" acceleration terms $-r\dot\phi^2$ and $2\dot r\dot\phi$ come from.

## Visual

![[PH-polar-basis.png]]

**Figure:** Moving along the red arc turns both unit vectors. The rule $d\hat r/dt=\dot\phi\,\hat\phi$ and $d\hat\phi/dt=-\dot\phi\,\hat r$ is the whole source of the extra terms below.

## Governing relation

Differentiate $\mathbf r=r\hat r$ twice, using those two rules:

$$\mathbf v=\dot r\,\hat r+r\dot\phi\,\hat\phi,\qquad \mathbf a=\underbrace{(\ddot r-r\dot\phi^{2})}_{a_r}\hat r+\underbrace{(r\ddot\phi+2\dot r\dot\phi)}_{a_\phi}\hat\phi$$

so Newton's law splits into two scalar equations:

$$F_r=m(\ddot r-r\dot\phi^2),\qquad F_\phi=m(r\ddot\phi+2\dot r\dot\phi)$$

Read the terms: $-r\dot\phi^2$ is the inward (centripetal) acceleration of circular motion; $2\dot r\dot\phi$ is the Coriolis-type term that appears when radius and angle change together.

> [!question]- 🎯 Predict first: a puck on a string is pulled in so $r$ halves. Does $\dot\phi$ increase, decrease or stay?
> It *increases four-fold*. With $F_\phi=0$ we get $\frac{d}{dt}(mr^2\dot\phi)=0$, so $r^2\dot\phi$ is constant: halve $r$ and $\dot\phi$ grows by $4$. A skater pulling in her arms is the same equation.

## Three classic systems

### 1. Plane pendulum

![[PH-pendulum-forces.png]]

**Figure:** Left, only $mg\sin\theta$ (green) acts along the arc. Right, $\sin\theta$ and $\theta$ agree to within 1% below about $14^\circ$.

With $r=L$ fixed, the tangential equation is $mL\ddot\theta=-mg\sin\theta$. For small angles $\sin\theta\approx\theta$ and it becomes the simple-harmonic equation $\ddot\theta=-(g/L)\theta$ with $\omega=\sqrt{g/L}$. The radial equation gives the string tension, $T=mg\cos\theta+mL\dot\theta^2$, which is larger at the bottom than at rest.

### 2. Conical (circular) pendulum

![[PH-conical-pendulum.png]]

**Figure:** The bob moves in a horizontal circle of radius $R=L\sin\alpha$. Vertical forces balance, $T\cos\alpha=mg$; the horizontal component supplies the centripetal force, $T\sin\alpha=mR\omega^2$.

Dividing the two gives $\tan\alpha=R\omega^2/g$, i.e. $\omega=\sqrt{g/(L\cos\alpha)}$. For small $\alpha$ this tends to $\sqrt{g/L}$, the plane-pendulum frequency.

### 3. Block sliding on a rotating arm, or a bead on a hoop

Whenever a constraint fixes $r$ (or $\phi$), one of the two equations becomes a *reaction-force* equation and the other is the true equation of motion.

## Method

1. **Place the origin at the centre** of the motion and draw $\hat r,\hat\phi$ **at the particle**.
2. **Resolve every force** into $\hat r$ and $\hat\phi$ components.
3. **Write $F_r=m(\ddot r-r\dot\phi^2)$ and $F_\phi=m(r\ddot\phi+2\dot r\dot\phi)$** and drop terms the constraint kills.
4. **Identify which equation is the motion and which the reaction** (tension, normal force).
5. **Check:** $\dot r=\dot\phi=0$ must give static equilibrium; small-angle limits must give SHM.

## Common traps

> [!warning]- ⚠️ Forgetting $-r\dot\phi^2$ in the radial equation
> Even constant-speed circular motion has $a_r=-r\dot\phi^2\neq0$. "Constant speed so no acceleration" is wrong; the direction is changing.

> [!warning]- ⚠️ Treating $\sin\theta\approx\theta$ as an exact equality
> It is a linearisation near $\theta=0$. At $\theta_0=90^\circ$ the true period is $1.18$ times longer (see [[The Nonlinear Pendulum]]).

> [!tip]- 🧠 Why $2\dot r\dot\phi$?
> If you move outward ($\dot r>0$) while rotating, you reach regions that move faster tangentially, so you need extra tangential acceleration just to keep up with the rotation. It is the same effect that deflects a ball rolled across a merry-go-round.

## Worked example

> [!example]- 🔬 A $1$ m conical pendulum has $\alpha=35^\circ$. Find $\omega$, the period and the tension for $m=0.5$ kg
> $\omega=\sqrt{g/(L\cos\alpha)}=\sqrt{9.81/(1\cdot0.819)}=3.46$ rad/s, so the period is $2\pi/\omega=1.82$ s.
> $T=mg/\cos\alpha=0.5(9.81)/0.819=5.99$ N, about $22\%$ more than the weight $4.91$ N.
> **Check:** horizontally, $T\sin\alpha=5.99(0.574)=3.44$ N and $mR\omega^2=0.5(0.574)(11.98)=3.44$ N ✓.

## Quick quiz

> [!question]- Q1. In the conical pendulum, what happens to $\omega$ as $\alpha\to90^\circ$?
> $\cos\alpha\to0$ so $\omega\to\infty$: you would need infinite speed to hold the string horizontal against gravity.

> [!question]- Q2. A bead is forced along a radial rod at constant $\dot r=v$ and rotates at constant $\dot\phi=\Omega$. What force does the rod exert transverse to itself?
> $F_\phi=m(0+2v\Omega)=2mv\Omega$. This is the Coriolis force in the language of the rotating rod.

## Connections

### Prerequisites
- [[Vectors - Dot and Cross Products]], [[Newton's Laws as Differential Equations]]

### Next
- [[Simple Harmonic Motion]]: the small-angle limit of the pendulum.
- [[Central Forces and the Effective Potential]]: the $\phi$-equation becomes conservation of angular momentum.
- [[Curvilinear Coordinates - Cylindrical and Spherical]]: polar coordinates extended to 3-D.

### Cross-domain links
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]]: $\hat r$ and $\hat\phi$ are $e^{i\phi}$ and $ie^{i\phi}$; differentiating them is the same rotation.
- [[Velocity and Acceleration - Analytical Method]]: the Coriolis term $2\dot r\dot\phi$ is exactly the Coriolis component of a slider on a rotating link in a mechanism.

## Self-check
- [ ] I can derive $\mathbf a$ in polar form from $d\hat r/dt=\dot\phi\hat\phi$.
- [ ] I can set up the plane and conical pendulum without a textbook.
- [ ] I can say which equation is the motion and which is the reaction force.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Physics I - MOC]]
