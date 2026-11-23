---
tags: [EE1100, tutorial-solution, machines, induction-machine, rotating-field, three-phase]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q2: What a Revolving Field Is, and Proof That Three-Phase Windings Create One

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]], [[Revolving Magnetic Field and Synchronous Speed]] · Previous: [[T8-Q1 - Operating Principle of the Induction Machine]] · Next: [[T8-Q3 - Synchronous Speed]]

> [!question] What is a revolving field? Prove that a three-phase winding carrying three-phase currents in the stator creates a revolving field in the air gap. Write the expression of the revolving field in terms of the stator MMF (ampere-turns) and the space angle $\alpha$.

**Tests:** [[Revolving Magnetic Field and Synchronous Speed|rotating-field derivation]], trigonometric identities, the cancellation of three phasors $120^\circ$ apart.

## Given
Three identical stator windings $a$, $b$, $c$ displaced $120^\circ$ in **space**, each of $N_{ph}$ turns, carrying balanced currents displaced $120^\circ$ in **time**:
$$i_a=I_m\sin\omega t,\qquad i_b=I_m\sin(\omega t-120^\circ),\qquad i_c=I_m\sin(\omega t+120^\circ).$$

## Principle and why it applies
**Definition.** A *revolving (rotating) field* is a magnetic field of **constant magnitude whose axis rotates at constant angular speed**, here in the air gap. It is the sum of the three MMFs: each winding alone produces only a **pulsating** MMF along a fixed axis (zero at some instants), but three such pulsating fields, displaced in both space and time, add to one constant-amplitude field that turns.

Each winding is assumed to give a sinusoidal **space distribution** of MMF about its own axis (distributed winding). With $\alpha$ measured from the axis of phase $a$, and $F_m=N_{ph}I_m$ the peak MMF of one phase:
$$F_a=F_m\sin\omega t\cos\alpha,\quad F_b=F_m\sin(\omega t-120^\circ)\cos(\alpha-120^\circ),\quad F_c=F_m\sin(\omega t+120^\circ)\cos(\alpha+120^\circ).$$

## Diagram
![[T8-Q2-revolving-field.png]]

**Figure:** the three currents are $120^\circ$ apart (left). The resultant MMF (right) has the **same height $1.5F_m$ at every instant**; its crest simply moves to larger $\alpha$ as $\omega t$ increases: a field rotating at $\omega$.

## Solution (proof)
Use $\sin A\cos B=\tfrac12[\sin(A-B)+\sin(A+B)]$ on each term:
$$F_a=\tfrac{F_m}2\big[\sin(\omega t-\alpha)+\sin(\omega t+\alpha)\big],$$
$$F_b=\tfrac{F_m}2\big[\sin(\omega t-\alpha)+\sin(\omega t+\alpha-240^\circ)\big],$$
$$F_c=\tfrac{F_m}2\big[\sin(\omega t-\alpha)+\sin(\omega t+\alpha+240^\circ)\big].$$
Add. The three $\sin(\omega t-\alpha)$ terms are **identical** and add; the three $\sin(\omega t+\alpha\ldots)$ terms are equal-amplitude sinusoids phased $0^\circ$, $-240^\circ$, $+240^\circ$ apart (that is $120^\circ$ apart) and **sum to zero**:
$$\sin(\theta)+\sin(\theta-240^\circ)+\sin(\theta+240^\circ)=\sin\theta\,\big[1+2\cos240^\circ\big]=0.$$
Hence
$$\boxed{F_R(\alpha,t)=F_a+F_b+F_c=\tfrac32\,F_m\,\sin(\omega t-\alpha)=\tfrac32N_{ph}I_m\sin(\omega t-\alpha)}.$$
**Interpretation:** this is a **travelling wave**: its crest ($\sin=1$) is at $\alpha=\omega t-90^\circ$, which moves with angular speed $d\alpha/dt=\omega$ in the direction of increasing $\alpha$ (the sequence $a\to b\to c$). The amplitude $\tfrac32F_m$ is constant, one and a half times the peak of a single phase.

## Result
$$\boxed{F_R(\alpha,t)=\tfrac32F_m\sin(\omega t-\alpha),\quad F_m=N_{ph}I_m:\quad\text{constant amplitude},\ \text{rotating at }\omega\ \text{(electrical)}}$$
For $P$ poles the mechanical speed is $n_s=120f/P$ ([[T8-Q3 - Synchronous Speed]]); reversing two supply leads reverses the rotation.

## Check
At $\omega t=0$: $F_a=0$, $F_b=F_m\sin(-120^\circ)\cos(\alpha-120^\circ)$, etc.; take $\alpha=-90^\circ$: $F_R=\tfrac32F_m\sin(0+90^\circ)=1.5F_m$ ✓ and the figure shows that crest at $-90^\circ$. At $\omega t=90^\circ$ the crest has moved to $\alpha=0$ (the axis of phase $a$, where $i_a$ is at its peak) ✓.

## Trap / alternative
- With **two** phases $90^\circ$ apart the same method also gives a rotating field (two-phase motor); with a **single** phase $F=F_m\sin\omega t\cos\alpha$ is only a *pulsating* field (equal to two counter-rotating fields of half amplitude), which has no starting torque.
- A **phasor/vector proof**: each winding's MMF is a vector of length $F_m\sin(\omega t-k120^\circ)$ along its own axis; at any instant the resultant of the three is $1.5F_m$ pointing in a direction that advances with $\omega t$.
- Don't confuse the **electrical** speed $\omega$ with the mechanical speed: they differ by the number of pole pairs.

## Concepts used
- Rotating MMF, balanced three-phase currents ([[Revolving Magnetic Field and Synchronous Speed]], [[Theory - Three-Phase Circuits]], [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]])
