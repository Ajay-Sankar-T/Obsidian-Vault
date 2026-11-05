---
tags: [concept, engineering-mechanics, AM1100, dynamics, kinematics, projectile]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [particle kinematics, rectilinear motion, projectile motion, normal and tangential components, curvilinear motion, constant acceleration]
---

# Particle Kinematics - Rectilinear and Curvilinear Motion

> [!abstract] The big idea
> Kinematics describes *how* a point moves without asking *why*. Position, velocity and acceleration are linked by calculus ($\mathbf v=\dot{\mathbf r}$, $\mathbf a=\dot{\mathbf v}$). Choose coordinates to suit the path: **Cartesian** for projectiles, **normal–tangential** ($n$–$t$) for a path with a known shape, **polar** when motion is about a centre. Dynamics (Newton's second law) then uses these accelerations.

## Rectilinear motion
$$v=\frac{ds}{dt},\quad a=\frac{dv}{dt}=v\frac{dv}{ds};\qquad\text{constant }a:\ v=v_0+at,\ \ s=s_0+v_0t+\tfrac12at^2,\ \ v^2=v_0^2+2a(s-s_0).$$
The identity $a=v\,dv/ds$ is the key when acceleration is given as a function of **position** (springs, gravity far from Earth).

## Curvilinear motion: three coordinate systems

| System | Velocity | Acceleration | Use when |
|---|---|---|---|
| Cartesian | $(\dot x,\dot y)$ | $(\ddot x,\ddot y)$ | projectiles, straight-line components |
| Normal–tangential | $v\,\hat e_t$ | $a_t=\dot v,\ \ a_n=v^2/\rho$ | the path's shape (radius of curvature $\rho$) is known |
| Polar | $\dot r\hat r+r\dot\theta\hat\theta$ | $(\ddot r-r\dot\theta^2)\hat r+(r\ddot\theta+2\dot r\dot\theta)\hat\theta$ | motion about a point, rotating arm |

The polar and $n$–$t$ derivations are done in [[Newton's Second Law in Polar Coordinates]] and [[Curvilinear Coordinates - Cylindrical and Spherical]]. In $n$–$t$ the **tangential** acceleration changes the **speed**, the **normal** acceleration (towards the centre of curvature) changes the **direction**.

![[EM-projectile.png]]

**Figure:** Left, trajectories of a $30$ m/s projectile at several launch angles (no air): complementary angles ($20^\circ,70^\circ$) have equal range. Right, $R=v_0^2\sin2\theta/g$ peaks at $45^\circ$ with $v_0^2/g=91.7$ m.

> [!question]- 🎯 Predict first: at the top of a projectile's path, what is its acceleration?
> **Still $g$ downward**, $9.81$ m/s². The *velocity* is horizontal and at its minimum, but acceleration is constant throughout flight. Zero velocity component $\neq$ zero acceleration; the same confusion appears when a ball is thrown straight up.

## Method
1. **Pick the coordinate system** that matches how the motion is described.
2. **Write the knowns** and which of $s,v,a,t$ are given.
3. **Rectilinear:** choose $a=dv/dt$, $v\,dv/ds$, or the constant-acceleration formulas.
4. **Projectile:** treat $x$ and $y$ independently ($a_x=0$, $a_y=-g$), linked by the common time.
5. **$n$–$t$:** $a_t=\dot v$, $a_n=v^2/\rho$; total $a=\sqrt{a_t^2+a_n^2}$.
6. **Check** with limits: $\rho\to\infty$ (straight path) gives $a_n\to0$.

## Worked examples
> [!example]- 🔬 Projectile launched at $30$ m/s, $40^\circ$ above the horizontal (flat ground)
> $v_{0x}=22.98$, $v_{0y}=19.28$ m/s. Time of flight $2v_{0y}/g=3.93$ s. Range $=v_{0x}t=90.4$ m. Maximum height $v_{0y}^2/2g=18.95$ m.
> **Check:** $R=v_0^2\sin80^\circ/g=900(0.985)/9.81=90.35$ m ✓; the same range as $50^\circ$.

> [!example]- 🔬 Car on a curve, $n$–$t$ components
> Speed $20$ m/s on a curve of radius $100$ m: $a_n=v^2/\rho=4$ m/s² (towards the centre). If it also speeds up at $a_t=3$ m/s², the total acceleration is $\sqrt{4^2+3^2}=5$ m/s².

> [!warning]- ⚠️ Using $a=v^2/r$ with the wrong radius
> $\rho$ is the **radius of curvature of the path at that point**, not the distance from some origin. For a circular path they agree; for a parabola they do not.

> [!danger]- 💥 Constant-acceleration formulas when $a$ varies
> $s=s_0+v_0t+\tfrac12at^2$ is only for **constant** $a$. A drag force, a spring or a rocket needs integration ($a=v\,dv/ds$ or $dv/dt$).

## Quick quiz
> [!question]- Q1. A stone is dropped from $80$ m. How long to hit, and how fast?
> $t=\sqrt{2s/g}=4.04$ s, $v=gt=39.6$ m/s.

> [!question]- Q2. A particle's acceleration is $a=-4s$ (m/s²). Find $v(s)$ if $v=2$ m/s at $s=0$.
> $v\,dv=-4s\,ds\Rightarrow v^2=4-4s^2$: SHM with $\omega=2$, amplitude $1$ m.

## Connections
- **Prerequisites:** [[Vectors - Dot and Cross Products]], [[Newton's Laws as Differential Equations]]
- **Next:** [[Kinetics of Particles - Work-Energy and Impulse-Momentum]]
- **Cross-domain:** [[Velocity and Acceleration - Analytical Method]] (relative motion for mechanisms builds on this), [[Material Derivative and Fluid Acceleration]] (acceleration of a fluid parcel is the same kinematics with $\partial/\partial t$ added).

## Self-check
- [ ] I can pick a coordinate system and write $\mathbf v,\mathbf a$ in it.
- [ ] I can solve projectile and $n$–$t$ problems.
- [ ] I know when $a=v\,dv/ds$ helps.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner–intermediate
- **Course map:** [[Engineering Mechanics - MOC]]
