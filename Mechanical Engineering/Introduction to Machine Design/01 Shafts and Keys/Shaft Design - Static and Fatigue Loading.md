---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Shaft design, DE-Goodman, ASME elliptic, Fluctuating loads, Rotating shaft fatigue]
---

# Shaft Design — Static and Fatigue Loading

> [!abstract] In one breath
> A transmission shaft sees **bending that is fully reversed** (every point on the surface passes through tension and compression each turn) and **torsion that is steady**. So the bending stress is the *alternating* stress and the torsion is the *mean* stress. Fatigue, not yield, almost always sets the diameter.

Part of [[Introduction to Machine Design - MOC]]. Next: [[Keys and Couplings]]. Failure and fatigue background: [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] and [[Static Failure Theories - Tresca and von Mises]].

## 1. Loads on the shaft

Power $P$ at speed $n$ gives torque $T=P/\omega$. A spur gear of pitch diameter $D_g$ delivers a tangential force $F_t=T/(D_g/2)$ and a radial force $F_r=F_t\tan\phi$; their resultant $F$ bends the shaft. For a shaft on two bearings with the gear at mid-span, $M_{max}=FL/4$. Find bending moments in two planes and combine them by the Pythagorean sum.

## 2. Stresses at a point on the surface

With the stress concentration factors $K_f$ (bending) and $K_{fs}$ (torsion) from the fillet or keyway:

$$
\sigma_a=\frac{32K_fM_a}{\pi d^3},\qquad
\sigma_m=\frac{32K_fM_m}{\pi d^3},\qquad
\tau_a=\frac{16K_{fs}T_a}{\pi d^3},\qquad
\tau_m=\frac{16K_{fs}T_m}{\pi d^3}
$$

Combine with the von Mises idea separately for the alternating and mean parts:

$$
\sigma_a'=\sqrt{\sigma_a^2+3\tau_a^2},\qquad \sigma_m'=\sqrt{\sigma_m^2+3\tau_m^2}
$$

For this shaft $M_m=0$ and $T_a=0$, so $\sigma_a'=\sigma_a$ (from bending) and $\sigma_m'=\sqrt3\,\tau_m$ (from torsion).

## 3. The endurance limit of this shaft

$S_e=k_ak_bk_ck_dk_e\,S_e'$, with $S_e'=0.5S_{ut}$ for steels up to about 1400 MPa and the Marin factors for surface $k_a=aS_{ut}^b$ (machined: $a=4.51$, $b=-0.265$ with $S_{ut}$ in MPa), size $k_b=1.24d^{-0.107}$ ($d$ in mm, 2.79–51 mm), load $k_c=1$ (bending), temperature $k_d=1$ and reliability $k_e=0.814$ (99 %).

## 4. Design equation (DE-Goodman, safety factor $n$)

$$
\frac1n=\frac{\sigma_a'}{S_e}+\frac{\sigma_m'}{S_{ut}}\ \Longrightarrow\
d=\Bigg\{\frac{16n}{\pi}\Bigg[\frac{2K_fM_a}{S_e}+\frac{\sqrt3\,K_{fs}T_m}{S_{ut}}\Bigg]\Bigg\}^{1/3}
$$

(the second form for fully reversed bending plus steady torsion). Because $S_e$ depends on $d$ through $k_b$, iterate: guess $d$, compute $S_e$, find $d$, repeat; it converges in three steps. Check yielding too: $n_y=S_y/\sigma'_{max}$ with $\sigma'_{max}=\sqrt{(\sigma_a+\sigma_m)^2+3(\tau_a+\tau_m)^2}$.

## 5. Worked example

15 kW at 1000 rpm through a spur gear of $D_g=120$ mm (20° pressure angle), bearings 300 mm apart with the gear at mid-span. Steel $S_{ut}=630$ MPa, $S_y=530$ MPa; fillet $K_f=1.6$, $K_{fs}=1.4$; $n=2$.

| Step | Result |
| --- | --- |
| torque $T=15\,000/104.7$ | 143 N·m |
| $F_t=T/0.06$, $F_r=F_t\tan20^\circ$, $F$ | 2387 N, 869 N, 2540 N |
| $M=FL/4$ | 190.5 N·m |
| $k_a$, $k_b$ (iterated), $S_e$ | 0.817, 0.845, **178 MPa** |
| DE-Goodman diameter | **34.3 mm** |
| choose standard | **Ø36 mm** |
| $\sigma_a'$, $\tau_m$, $\sigma_m'$ | 66.6, 21.9, 37.9 MPa |
| fatigue factor of safety at Ø36 | $n_f=2.29$ |
| first-cycle yield factor $n_y=S_y/(\sigma_a+\sigma_m')$ | 5.1 |

For comparison a **static** design with the maximum-shear theory, $d=\big(32n\sqrt{M^2+T^2}/\pi S_y\big)^{1/3}$, gives only 20.9 mm. Fatigue demands a shaft 64 % thicker: this is why static sizing of a rotating shaft is unsafe.

![[MD-1-shaft-goodman.png]]

The orange point is the load state; the Goodman line is the safe boundary. Scaling the load by 2.29 moves the point along the radial line to the boundary (purple cross).

## 6. Practical points

- Reduce stress concentration with generous fillet radii; each shoulder changes $K_f$ (1.5–2.5 typical).
- Use the **ASME elliptic** or **Soderberg** criteria when more conservatism is needed; Gerber is closer to the data for ductile steel.
- Check **deflection and slope** at gears and bearings, and the **critical speed** (the lowest bending natural frequency): see [[Vibration of Particles and Rigid Bodies]].

> [!warning] Traps
> - Treating the bending stress as steady: on a rotating shaft it is **fully reversed**, so it is the alternating stress.
> - Using $k_b$ from the guessed diameter and never iterating.
> - Taking the maximum bending moment from one plane only.
> - Forgetting that a keyway has its own $K_f$.

> [!question]- Predict first: the same shaft, but the bending moment is steady (a bevel pinion loaded in a fixed direction on a *non-rotating* shaft). What changes?
> The bending stress becomes **mean** stress, not alternating, so $\sigma_a'\approx0$ and the fatigue limit stops mattering: the shaft is sized by the static yield criterion. Rotation of the shaft is what makes bending fully reversed.

> [!question]- Does a smoother surface let you use a smaller shaft?
> Yes, through $k_a$: grinding raises $k_a$ from 0.82 to about 0.91 (for $S_{ut}=630$), a gain of 12 % in $S_e$. Since the bending term dominates and $d\propto S_e^{-1/3}$, that is about 4 % off the diameter.

## 7. Connections

- [[Torsion of Circular Shafts]] and [[Power Transmission by Shafts]] — $T=P/\omega$ and $\tau=16T/\pi d^3$.
- [[Flexure Formula]] and [[Shear Force and Bending Moment Diagrams]] — the bending moment and $\sigma=32M/\pi d^3$.
- [[Plane Stress Transformation]] and [[Mohr's Circle for Stress]] — why combined bending and torsion needs a failure theory.
- [[Gear Formula Bank]] — $F_t$ and $F_r$ from the pressure angle.
- [[Gears, Transformers and Reflected Impedance]] — torque and speed change through a gear pair like voltage and current through a transformer.
