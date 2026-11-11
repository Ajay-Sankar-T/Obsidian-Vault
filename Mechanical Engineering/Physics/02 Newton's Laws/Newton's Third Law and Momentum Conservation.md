---
tags: [concept, physics-1, PH1010, newton, momentum, conservation]
status: draft
up: "[[Physics I - MOC]]"
aliases: [third law, action reaction, conservation of momentum, centre of mass, collision]
---

# Newton's Third Law and Momentum Conservation

> [!abstract] The big idea
> If every force has an equal and opposite partner, the partners cancel in the total, so **the total momentum of an isolated system cannot change**. Momentum conservation is not a fourth law; it is the third law summed over all the particles. Its power is that it ignores the messy internal forces completely.

## Visual

![[PH-momentum-collision.png]]

**Figure:** A 2 kg mass meets a 1 kg mass in a head-on elastic collision. Left, their paths bend at the collision but the centre of mass (dashed) is a straight line. Right, $p_1$ and $p_2$ jump in opposite directions by the same amount, so $p_1+p_2$ stays at $3$.

## Governing relation

For two particles with only mutual forces, $\mathbf F_{12}=-\mathbf F_{21}$, so

$$\frac{d}{dt}(\mathbf p_1+\mathbf p_2)=\mathbf F_{12}+\mathbf F_{21}=\mathbf 0\;\Rightarrow\;\mathbf P=\sum_i m_i\mathbf v_i=\text{const}$$

For $N$ particles, $\dot{\mathbf P}=\mathbf F_{\rm ext}$. Equivalently the **centre of mass** $\mathbf R=\sum m_i\mathbf r_i/M$ obeys $M\ddot{\mathbf R}=\mathbf F_{\rm ext}$: it moves as if all the mass sat there and only external forces acted.

**Component form:** momentum is a vector, so it is conserved *component by component*. If the external force vanishes only along $x$, then $P_x$ is conserved even though $P_y$ is not.

> [!question]- 🎯 Predict first: a firework flying in a parabola explodes mid-air. Where does the centre of mass of all the fragments go?
> It carries on along the *same parabola*, as if nothing had happened. The explosion forces are internal; only gravity is external. Fragments fly apart symmetrically about that moving point.

## Method

1. **Draw the system boundary** so the interesting forces are internal.
2. **Check what is external** along each axis (gravity, normal force, friction, a wall).
3. **Write $P_{x,\text{before}}=P_{x,\text{after}}$** for each conserved component.
4. **Add energy** only if the collision is elastic (kinetic energy conserved). Otherwise use a restitution coefficient.
5. **Check:** the CM velocity before and after must match.

## Collision cheat sheet

| Type | Momentum | Kinetic energy | Final velocities |
|---|---|---|---|
| Elastic | conserved | conserved | $u_1=\frac{(m_1-m_2)v_1+2m_2v_2}{m_1+m_2}$, $u_2=\frac{(m_2-m_1)v_2+2m_1v_1}{m_1+m_2}$ |
| Perfectly inelastic | conserved | maximum loss | one common $u=\frac{m_1v_1+m_2v_2}{m_1+m_2}$ |
| General | conserved | partly lost | $u_2-u_1=-e\,(v_2-v_1)$, $0\le e\le1$ |

## Common traps

> [!warning]- ⚠️ "Action and reaction cancel, so nothing can ever move"
> They act on *different bodies*. Your push on a wall and the wall's push on you cancel in a total, but each only changes the momentum of the body it acts on.

> [!warning]- ⚠️ Treating energy as conserved in every collision
> Momentum is always conserved when external forces are negligible. Kinetic energy is conserved only in elastic collisions; a car crash converts it to heat and deformation.

> [!tip]- 🧠 Where does the third law break down?
> For forces that travel at finite speed or are carried by fields. Two moving charges exert forces on each other that are not equal and opposite at the same instant; the missing momentum is stored in the electromagnetic field. Momentum is still conserved, but only if you count the field.

## Worked example

> [!example]- 🔬 $m_1=2$ kg at $+2$ m/s hits $m_2=1$ kg at $-1$ m/s, elastically. Find both velocities afterwards
> Total momentum $=2(2)+1(-1)=3$ kg·m/s, so $v_{\rm cm}=3/3=1$ m/s.
> $u_1=\frac{(2-1)(2)+2(1)(-1)}{3}=0$ and $u_2=\frac{(1-2)(-1)+2(2)(2)}{3}=3$ m/s.
> **Check:** momentum after $=0+1(3)=3$ ✓. Kinetic energy before $\tfrac12(2)(4)+\tfrac12(1)(1)=4.5$ J; after $0+\tfrac12(1)(9)=4.5$ J ✓. In the CM frame each ball simply reverses its velocity.

## Quick quiz

> [!question]- Q1. You step off a $20$ kg boat at rest onto a dock at $2$ m/s ($m=60$ kg). How fast does the boat recoil?
> $P=0$ before, so $20v_b+60(2)=0$ and $v_b=-6$ m/s. The boat is lighter, so it moves faster.

> [!question]- Q2. Two skaters push off each other. Is their total kinetic energy conserved?
> No: it goes from $0$ to positive, supplied by their muscles. Their total *momentum* is still zero.

## Connections

### Prerequisites
- [[Newton's Laws as Differential Equations]]

### Next
- [[Two-Body Problem and Hohmann Transfer]]: the centre of mass and the *reduced mass* turn two bodies into one.
- [[Cyclic Coordinates and Conservation Laws]]: momentum conservation re-derived as a symmetry (translation invariance).

### Cross-domain links
- [[Momentum Equation Applications - Jets, Vanes, Bends]]: a jet hitting a vane is momentum conservation applied to a control volume.
- [[Linear Momentum Equation]]: the fluid version, $\sum\mathbf F=\dot{\mathbf P}_{\rm cv}+\ldots$, is this law written for flowing mass.
- [[Conservation Laws and Flow Networks]]: all conservation laws share the "what goes in must come out" bookkeeping.

## Self-check
- [ ] I can derive momentum conservation from the third law in two lines.
- [ ] I can apply conservation along one axis only.
- [ ] I can find both outgoing velocities of an elastic 1-D collision and verify them two ways.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner–intermediate
- **Course map:** [[Physics I - MOC]]
