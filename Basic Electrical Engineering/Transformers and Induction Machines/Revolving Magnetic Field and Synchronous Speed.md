---
title: Revolving Magnetic Field and Synchronous Speed
tags: [EE1100, concept, induction-machine, rotating-field, three-phase]
source: "[[Lecture 41 Induction Machine-Circuit Representation.pdf]], [[Lecture 40 Electric Machines.pdf]]"
---

Related: [[11 Three Phase Induction Machines]] · [[Concepts#Rotating Magnetic Field|Rotating magnetic field (glossary)]] · [[09 Three Phase Circuits and Power Measurement]] · [[Induction Motor - Slip, Rotor Circuit and Power Flow]] · animation: [Three-phase revolving field](revolving%20field%20animation.html)

## What it is
Three identical stator windings placed $120^\circ$ apart in space and fed by three currents $120^\circ$ apart in time produce a **magnetic field of constant magnitude that rotates** at a fixed speed, the **synchronous speed** $n_s$. This is why a three-phase induction motor needs no moving contact and is self-starting.

## Derivation (Lecture 41)
Currents $i_a=I_m\sin\omega t$, $i_b=I_m\sin(\omega t-120^\circ)$, $i_c=I_m\sin(\omega t+120^\circ)$ in windings of $N_{ph}$ turns. Each winding produces a sinusoidally **space-distributed** MMF along its own axis. With $\alpha$ the angle measured from the axis of phase $a$ and $F_m=N_{ph}I_m$:
$$F_a=F_m\sin\omega t\,\cos\alpha,\quad F_b=F_m\sin(\omega t-120^\circ)\cos(\alpha-120^\circ),\quad F_c=F_m\sin(\omega t+120^\circ)\cos(\alpha+120^\circ).$$
Add them. Using $2\sin A\cos B=\sin(A-B)+\sin(A+B)$,
$$F_R=F_a+F_b+F_c=\frac{F_m}{2}\Big[\underbrace{\sin(\omega t-\alpha)+\sin(\omega t-\alpha)+\sin(\omega t-\alpha)}_{3\ \text{equal terms}}+\underbrace{\sin(\omega t+\alpha)+\sin(\omega t+\alpha-240^\circ)+\sin(\omega t+\alpha+240^\circ)}_{=0}\Big]$$
$$\boxed{F_R(\alpha,t)=\tfrac32F_m\sin(\omega t-\alpha)}$$
The backward-travelling terms $\sin(\omega t+\alpha+\dots)$ are three phasors $120^\circ$ apart and cancel. What is left is a **single travelling wave**: at $\omega t=0$ the peak is at $\alpha=-90^\circ$, at $\omega t=45^\circ$ it has moved by $45^\circ$, and so on. The pattern rotates at angular speed $\omega$ (electrical) with constant peak $\frac32F_m$.

## Synchronous speed
For $P$ poles (pole pairs $P/2$), one electrical cycle moves the field by one pole pair:
$$\theta_{elec}=\frac P2\,\theta_{mech},\qquad \omega_{elec}=\frac P2\,\omega_{mech},\qquad f=\frac P2\,n_s\ (n_s\text{ in rev/s}),$$
$$\boxed{n_s=\frac{120f}{P}\ \text{rpm}}\qquad(50\ \text{Hz}:\ P=2,4,6\Rightarrow3000,1500,1000\ \text{rpm}).$$

**Direction.** Interchanging any two phase connections reverses the sequence ($b\leftrightarrow c$) and the field rotates the other way: the standard way to reverse a three-phase motor.

**Single-phase machines.** One winding gives a *pulsating* field, equal to two counter-rotating fields of half amplitude, with no net starting torque. A second winding with a phase shift ($25^\circ$–$30^\circ$ in a split-phase motor, helped by a capacitor in a capacitor-start motor) makes the field rotate during starting ([[Induction Machines - Types, Construction and Applications]]).

> [!warning] Traps
> - $n_s=120f/P$ uses the number of **poles**, not pole pairs ($P=2p$).
> - The speed is fixed by the **supply frequency** only. The load does not change $n_s$; it changes the rotor speed (slip).
> - The amplitude is $\frac32F_m$ (one and a half times the single-phase amplitude), not $3F_m$.

## Cross-domain links
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] — a phasor $e^{j\omega t}$ is a rotating vector; here three alternating quantities, each the projection of a rotating vector, combine into one genuinely rotating field. The cancellation of the backward terms is the sum of the three cube roots of unity being zero.
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — the three-phase currents are the projections of a vector rotating at $\omega$; the $120^\circ$ symmetry is what makes the resulting rotation uniform.
