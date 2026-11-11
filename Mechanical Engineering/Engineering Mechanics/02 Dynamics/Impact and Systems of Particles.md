---
tags: [concept, engineering-mechanics, AM1100, dynamics, impact, restitution, systems-of-particles]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [impact, coefficient of restitution, central impact, oblique impact, systems of particles, centre of mass motion]
---

# Impact and Systems of Particles

> [!abstract] The big idea
> In a collision the forces are huge, brief and unknown, so you cannot use $F=ma$. But the forces are **internal** to the colliding pair, so **momentum is conserved**. One extra fact is needed to fix the outcome: the **coefficient of restitution** $e$, a number between $0$ (perfectly plastic, they stick) and $1$ (perfectly elastic), which compares the speed of separation to the speed of approach.

## Central impact (along the line of centres)

$$m_1v_1+m_2v_2=m_1v_1'+m_2v_2'\quad(\text{momentum}),\qquad e=\frac{v_2'-v_1'}{v_1-v_2}\quad(\text{restitution}).$$
Solving for the final velocities:
$$v_1'=\frac{(m_1-em_2)v_1+m_2(1+e)v_2}{m_1+m_2},\qquad v_2'=\frac{(m_2-em_1)v_2+m_1(1+e)v_1}{m_1+m_2}.$$
Equivalently, find the velocity of the centre of mass $v_{cm}=\dfrac{m_1v_1+m_2v_2}{m_1+m_2}$: relative to it, each body's velocity is **reversed and scaled by $e$**. The kinetic energy lost is $\Delta T=\tfrac12\mu(1-e^2)(v_1-v_2)^2$ with reduced mass $\mu=\dfrac{m_1m_2}{m_1+m_2}$.

**Oblique impact:** along the common tangent (smooth surfaces) each body's velocity component is unchanged; apply momentum and restitution along the line of centres only.

![[EM-bounce.png]]

**Figure:** A ball dropped from $2$ m with $e=0.8$. Each bounce keeps $e$ of the speed and $e^2$ of the height: $h_n=h_0e^{2n}$. Right, the geometric decay on a log scale for three values of $e$: the ball with $e=0.5$ loses $99.9\%$ of its height by the fifth bounce.

> [!question]- 🎯 Predict first: a ball with $e=0.8$ bounces from $2$ m. How high is the second bounce?
> $2\times0.8^4=\mathbf{0.82}$ m (heights multiply by $e^2=0.64$ each bounce: $1.28$, then $0.82$). People often use $e$ instead of $e^2$: height scales with *speed squared*.

## Method
1. **Identify the impact line** (line of centres) and resolve velocities along it and across it.
2. **Momentum along the line:** $m_1v_1+m_2v_2=m_1v_1'+m_2v_2'$.
3. **Restitution along the line:** $e(v_1-v_2)=v_2'-v_1'$.
4. **Solve** the two equations for $v_1',v_2'$.
5. **Transverse components** (smooth surfaces): unchanged.
6. **Energy lost** from before and after; it must be $\ge0$.

## Worked examples
> [!example]- 🔬 $m_1=2$ kg at $3$ m/s hits $m_2=1$ kg at rest, $e=0.5$
> $v_{cm}=2$ m/s. Momentum: $2(3)=2v_1'+v_2'$ and restitution: $v_2'-v_1'=0.5(3)=1.5$. Then $v_1'=1.5$, $v_2'=3$ m/s.
> **Check:** momentum $2(1.5)+3=6$ ✓. Kinetic energy: before $9$ J; after $2.25+4.5=6.75$ J; lost $2.25$ J. Formula: $\tfrac12\mu(1-e^2)(3)^2=\tfrac12(\tfrac23)(0.75)(9)=2.25$ J ✓.

> [!example]- 🔬 Ball dropped from $2$ m, $e=0.8$, onto a fixed floor
> Impact speed $\sqrt{2gh}=6.26$ m/s; rebound speed $ev=5.01$ m/s; rebound height $e^2h=1.28$ m. Energy lost per bounce: $1-e^2=36\%$.
> **Check:** for the fixed floor $m_2\to\infty$, $v_2=0$: $e=-v_1'/v_1$ ✓.

> [!warning]- ⚠️ Using conservation of energy when $e<1$
> Only $e=1$ conserves kinetic energy. For $e<1$ use **momentum + restitution**; energy is lost to deformation and heat.

> [!danger]- 💥 Applying restitution to the wrong components
> $e$ applies only along the **line of centres**; tangential components (smooth contact) pass through unchanged. Using $e$ on the full velocity vectors gives an impossible deflection angle.

## Systems of particles (briefly)
The centre of mass obeys $\sum\mathbf F_{\rm ext}=m\ddot{\mathbf r}_{cm}$ whatever happens inside; the total momentum $\mathbf G=m\mathbf v_{cm}$ changes only through external impulse; and the total angular momentum about a fixed point changes only through external moments. These are the justification for treating a complex object as a point at its centre of mass.

## Quick quiz
> [!question]- Q1. Two equal masses collide head-on elastically ($e=1$). What happens?
> They **exchange velocities**. With equal masses the relative-to-CM velocities simply reverse.

> [!question]- Q2. A perfectly plastic collision ($e=0$): where does all the lost energy go?
> Into deformation and heat; the bodies move together at $v_{cm}$ afterwards, with $\Delta T=\tfrac12\mu(v_1-v_2)^2$, the **maximum** possible loss.

## Connections
- **Prerequisites:** [[Kinetics of Particles - Work-Energy and Impulse-Momentum]], [[Newton's Third Law and Momentum Conservation]]
- **Next:** [[Plane Kinematics of Rigid Bodies]]
- **Cross-domain:** [[Newton's Third Law and Momentum Conservation]] (the elastic case in Physics I); [[Two-Body Problem and Hohmann Transfer]] (reduced mass appears in both).

## Self-check
- [ ] I can use momentum and restitution along the line of impact.
- [ ] I can find energy loss and bounce heights.
- [ ] I can explain why the CM motion ignores internal forces.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Engineering Mechanics - MOC]]
