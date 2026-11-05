---
tags: [concept, engineering-mechanics, AM1100, dynamics, inertia, radius-of-gyration]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [mass moment of inertia, radius of gyration, parallel axis theorem, rotational inertia, moment of inertia of a body]
---

# Mass Moments of Inertia

> [!abstract] The big idea
> **Mass** resists changes in translational motion; the **mass moment of inertia** $I=\int r^2\,dm$ resists changes in rotation. It depends on *where* the mass is: mass far from the axis counts with the **square** of its distance. Do not confuse it with the **area** moment of inertia of a beam cross-section: same $r^2$ weighting, different object.

## Definition and the two theorems

$$I=\int r^2\,dm,\qquad k=\sqrt{I/m}\ (\text{radius of gyration}),\qquad I=I_G+md^2\ (\text{parallel-axis}).$$
$r$ is the perpendicular distance from the axis. The parallel-axis theorem moves $I$ from an axis through the centre of mass G to a parallel axis a distance $d$ away; $I_G$ is always the **smallest** value.

![[EM-inertia-table.png]]

**Figure:** Standard results. A thin rod is $\tfrac1{12}mL^2$ about its centre and $\tfrac13mL^2$ about its end (the end is $L/2$ away: $\tfrac1{12}+\tfrac14=\tfrac13$ ✓ the parallel-axis theorem). A hoop has all its mass at $R$ and so the largest $k$.

> [!question]- 🎯 Predict first: a hollow tube and a solid rod have the same mass and outer radius. Which is harder to spin?
> The **tube**: its mass is farther from the axis ($I=\tfrac12m(R^2+r^2)>\tfrac12mR^2$). This is why flywheels are rims with spokes and why a figure skater pulls her arms in to spin faster.

## Method
1. **Identify** the axis and the body (decompose into rods, disks, cylinders if composite).
2. **Look up** $I_G$ for each piece about its own centre of mass.
3. **Shift** each to the common axis with $I=I_G+md^2$ and **add** (subtract holes).
4. **Quote** $k=\sqrt{I/m}$ if the problem uses radius of gyration.

## Worked examples
> [!example]- 🔬 Uniform rod, $m=2$ kg, $L=1$ m, about one end
> $I_G=\tfrac1{12}(2)(1)^2=0.1667$ kg·m²; $d=0.5$ m: $I=0.1667+2(0.25)=0.667$ kg·m² $=\tfrac13mL^2$ ✓. $k=\sqrt{I/m}=0.577$ m.

> [!example]- 🔬 Rod as a physical pendulum, pivoted at one end
> Period $T=2\pi\sqrt{\dfrac{I}{mgd}}=2\pi\sqrt{\dfrac{\tfrac13mL^2}{mg(L/2)}}=2\pi\sqrt{\dfrac{2L}{3g}}=1.64$ s for $L=1$ m. (Compare a simple pendulum of the same length: $2.01$ s; the rod swings like a pendulum of length $2L/3$.)

> [!warning]- ⚠️ Adding $I$ about different axes
> $I$ values add only if they are about the **same axis**. First shift each piece to the common axis with the parallel-axis theorem.

> [!danger]- 💥 Using the parallel-axis theorem between two non-centroidal axes
> $I=I_G+md^2$ goes **from the centre of mass** to another axis. To go between two off-centre axes, first drop to $I_G$ (subtract $md_1^2$), then add $md_2^2$.

## Quick quiz
> [!question]- Q1. By what factor does $I$ of a disk change if its radius doubles (same mass)? If its mass doubles (same radius)?
> $I=\tfrac12mR^2$: radius $\times2\Rightarrow4\times$; mass $\times2\Rightarrow2\times$.

> [!question]- Q2. Two $1$ kg masses sit at the ends of a light $1$ m rod. $I$ about the centre vs about one end?
> Centre: $2(1)(0.5)^2=0.5$ kg·m². End: $1(0)^2+1(1)^2=1$ kg·m² ($=0.5+2(0.5)^2$ by the theorem ✓).

## Connections
- **Prerequisites:** [[Centre of Mass and Centroids]]
- **Used by:** [[Plane Kinetics of Rigid Bodies]], [[Vibration of Particles and Rigid Bodies]]
- **Cross-domain:** [[Second Moments of Area]] and [[Second Moments of Area - One Integral, Many Jobs]] (the area analogue $\int y^2\,dA$ governs beam bending; same parallel-axis theorem); [[Lab - Variable g Pendulum]] (the compound pendulum measures $k$).

## Self-check
- [ ] I can recall $I$ for rod, disk, ring and sphere.
- [ ] I can apply the parallel-axis theorem correctly.
- [ ] I can explain the difference from the area moment of inertia.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Engineering Mechanics - MOC]]
