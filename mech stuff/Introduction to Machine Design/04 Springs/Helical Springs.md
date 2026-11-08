---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Helical compression spring, Wahl factor, Spring index, Spring rate, Spring design]
---

# Helical Springs

> [!abstract] In one breath
> A coil spring is a **twisted wire**: pushing the coil down twists the wire, so the wire is loaded in **torsion** and the spring rate is a torsion formula in disguise. The one correction that matters is the **Wahl factor** $K_w$, which accounts for the extra stress on the inside of tight coils.

Part of [[Introduction to Machine Design - MOC]]. Previous: [[Spur Gear Design - Lewis Bending and Surface Stress]]. Next: [[Bolted Joints - Preload and Joint Stiffness]].

## 1. Why torsion

A force $F$ along the axis of a coil of mean diameter $D$ gives a torque $T=FD/2$ on every cross-section of the wire (diameter $d$), plus a direct shear $F/A$. For the wire, with $C=D/d$ the **spring index** (usually 4–12):

$$
\tau=K_w\frac{8FD}{\pi d^3},\qquad
K_w=\frac{4C-1}{4C-4}+\frac{0.615}{C}
$$

$K_w$ includes direct shear and the stress concentration from curvature. (Shigley's $K_s=1+0.5/C$ covers only direct shear, used for static loads; for fatigue $K_w$ or the Bergsträsser factor.) For a very small spring index the inside fibre stress is much more than $8FD/\pi d^3$.

## 2. Deflection and rate

Twist of the wire over its active length $\pi DN_a$ gives

$$
\delta=\frac{8FD^3N_a}{Gd^4},\qquad k=\frac{F}{\delta}=\frac{Gd^4}{8D^3N_a}
$$

with $N_a$ the **active** turns (total turns less end turns that do not deflect: $N_a=N_t-2$ for squared-and-ground ends). Spring rate falls with the cube of the coil diameter and rises with the fourth power of the wire diameter.

**Combinations.** Parallel: $k=k_1+k_2$. Series: $1/k=1/k_1+1/k_2$.

## 3. Worked example

Music-wire spring, $d=4$ mm, $D=30$ mm ($C=7.5$), $N_a=8$, $G=79.3$ GPa, loaded to $F_{max}=250$ N.

| Quantity | Value |
| --- | --- |
| $K_w$ | **1.197** |
| $\tau_{max}$ | **357 MPa** |
| rate $k$ | **11.7 N/mm** |
| deflection at 250 N | 21.3 mm |
| $S_{ut}=2211/d^{0.145}$ (A228 music wire) | 1808 MPa |
| $S_{sy}\approx0.45S_{ut}$ | 814 MPa |
| static factor of safety $S_{sy}/\tau$ | **2.28** |

**Fatigue.** The spring cycles between 100 N and 250 N, so $F_a=75$ N and $F_m=175$ N: $\tau_a=107$ MPa, $\tau_m=250$ MPa. Unpeened music wire (Zimmerli) has an alternating strength $S_{sa}=241$ MPa at $S_{sm}=379$ MPa; with $S_{su}=0.67S_{ut}=1212$ MPa the Goodman endurance strength is $S_{se}=S_{sa}/(1-S_{sm}/S_{su})=351$ MPa, and

$$
n_f=\Big[\frac{\tau_a}{S_{se}}+\frac{\tau_m}{S_{su}}\Big]^{-1}=\mathbf{1.95}
$$

Fatigue life of springs is governed by the *range* of stress, so shot peening raises $S_{sa}$ and is standard practice for valve springs.

![[MD-5-springs.png]]

## 4. Other checks

- **Solid length** $=N_td$ (the coils touching): design so the working load leaves at least 10–15 % of the deflection in reserve before solid.
- **Buckling** of a long spring: free length over mean diameter $L_0/D>4$ needs a guide or a check against the critical deflection.
- **Surge** (a stress wave running along the coil at the spring's natural frequency): the lowest surge frequency should be 13–20 times the operating frequency.
- **Extension springs** have hooks with stress concentrations; **torsion springs** are bent in bending, not torsion.

> [!warning] Traps
> - Using the coil diameter $D$ where the wire diameter $d$ belongs in $d^4$ or $d^3$.
> - Counting all coils in the deflection: only the active turns deflect.
> - Using $K_s$ for fatigue: use the Wahl factor.
> - Taking $G$ equal to $E/2$: $G=E/[2(1+\nu)]\approx0.385E$ for steel (79 GPa).
> - Setting the loads to the solid height, so no margin remains.

> [!question]- Predict first: halve the coil diameter at the same wire. How does the rate change?
> $k\propto1/D^3$, so the rate rises **8 times**. The stress at a given force halves ($\tau\propto D$) but $K_w$ rises (C falls to 3.75: $K_w\approx1.4$).

> [!question]- Two identical springs in series carrying 250 N. What deflection?
> Each carries 250 N, so each deflects 21.3 mm and the pair deflects 42.6 mm: equivalent rate $k/2$. In parallel the load splits 125 N each and the deflection is 10.6 mm.

## 5. Connections

- [[Torsion of Circular Shafts]] — the wire is a shaft in torsion: $\tau=16T/\pi d^3$ with $T=FD/2$ gives $8FD/\pi d^3$.
- [[Strain Energy and Castigliano's Theorem]] — the deflection formula follows from torsion strain energy (differentiate $U=\int T^2ds/2GJ$ with respect to $F$).
- [[Vibration of Particles and Rigid Bodies]] — $k$ here is the stiffness in $\omega_n=\sqrt{k/m}$.
- [[The Universal Second-Order Linear System]] — springs set the stiffness term; surge is a spring's own standing-wave resonance.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — the Goodman line used in the fatigue example, applied in shear.
