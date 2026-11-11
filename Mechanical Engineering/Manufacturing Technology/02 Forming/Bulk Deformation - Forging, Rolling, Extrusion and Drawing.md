---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Forging, Rolling, Extrusion, Wire drawing, Bulk forming, Flow stress, Hot working, Cold working, Upsetting]
---

# Bulk Deformation — Forging, Rolling, Extrusion and Drawing

> [!abstract] In one breath
> Bulk forming squeezes a solid billet **plastically** into a new shape: the volume stays constant, the shape changes, and the force is the **flow stress** times the area, plus extra for friction. A tensile test supplies the flow stress law $\sigma_f=K\varepsilon^n$; plasticity supplies the strains.

Part of [[Manufacturing Technology - MOC]]. Previous: [[Casting - Solidification Time and Riser Design]]. Next: [[Sheet Metal Forming - Blanking, Bending and Deep Drawing]].

## 1. Ingredients

- **True strain** $\varepsilon=\ln(h_0/h_1)$ for compression (height), $\ln(A_0/A_1)$ for extrusion and drawing. Constant volume: $A_0h_0=A_1h_1$. See [[Tensile Test, True Stress-Strain and Hardness]].
- **Flow stress** $\sigma_f=K\varepsilon^n$ (cold). The *mean* flow stress over a deformation from 0 to $\varepsilon$: $\bar\sigma_f=\dfrac{K\varepsilon^n}{1+n}$.
- **Cold working** (below about $0.3T_m$): strain hardening, good finish and tolerance, higher forces. **Hot working** (above recrystallisation, about $0.5$–$0.7\,T_m$): no hardening, low force, large deformation, scale and rough surface.
- **Friction** raises the force: sticking at the die faces makes the mid-height bulge and the pressure rises towards the centre (**friction hill**).

## 2. Forging (open-die upsetting)

$$
F=\bar\sigma_f\,A_1\Big(1+\frac{2\mu r_1}{3h_1}\Big)\qquad(\text{approximate friction correction for a cylinder})
$$

**Example.** Steel billet Ø50 × 60 mm upset cold to 30 mm ($K=600$ MPa, $n=0.2$, $\mu=0.1$):

| Step | Value |
| --- | --- |
| $\varepsilon=\ln(60/30)$ | 0.693 |
| mean flow stress | $600(0.693)^{0.2}/1.2=\mathbf{465\ MPa}$ |
| final area (volume const.) | 3927 mm² ($D_1=70.7$ mm) |
| frictionless force | 1.82 MN |
| with friction | **1.97 MN** (+8 %) |

The force climbs steeply at the end because $A_1$ grows while $h_1$ shrinks. Closed-die forging, with flash, needs far more force (up to 3–5 times) to fill the die.

![[MFG-2-bulk.png]]

## 3. Rolling

A strip of thickness $h_0$ is drawn between rolls of radius $R$ to $h_1$. The draft $\Delta h=h_0-h_1$. The projected contact length is $L=\sqrt{R\,\Delta h}$.

**Bite condition:** friction must pull the strip in: $\tan\alpha\le\mu$ with the bite angle $\alpha$, giving the **maximum draft** $\Delta h_{max}=\mu^2R$.

**Example.** $R=250$ mm, $\mu=0.15$: $\Delta h_{max}=0.0225\times250=5.6$ mm. A pass of $10\to8$ mm ($\Delta h=2$ mm) is within it, with $L=22.4$ mm. Larger rolls and rougher rolls take bigger drafts; hot rolling has higher $\mu$ (0.3–0.5) so reductions of 30–50 % are possible.

Rolling force $F\approx\bar\sigma_f\,w\,L$ (with $w$ the width) times a friction factor; the **power** is $F\cdot L/2$ per roll times the angular velocity.

## 4. Extrusion and drawing

**Extrusion** pushes a billet through a die. Extrusion ratio $r_x=A_0/A_f$; ideal true strain $\varepsilon=\ln r_x$; ideal pressure $p=\bar\sigma_f\ln r_x$ (friction and redundant work add a further 30–100 %).

**Drawing** pulls the material through a die (wire, rod, tube); only a tensile pull is applied, so it is limited by the strength of the drawn section.

**Example.** Wire Ø6 mm drawn to Ø4 mm ($K=500$ MPa, $n=0.15$):

$$
\text{area ratio }2.25\ (\text{reduction }55.6\ \%),\quad \varepsilon=\ln2.25=0.811,\quad \bar\sigma_f=\frac{500(0.811)^{0.15}}{1.15}=421\ \text{MPa},\quad \sigma_d=\bar\sigma_f\,\varepsilon=\mathbf{342\ MPa}
$$

The ideal drawing stress cannot exceed the flow stress of the *exit* wire. With no hardening, $\sigma_d=\sigma_f\ln(A_0/A_f)$ equals $\sigma_f$ at $\ln=1$: **maximum reduction per pass $=63$ %** ($A_0/A_f=e=2.72$). Real passes use 20–40 %, with annealing between multiple passes.

## 5. Defects

| Process | Defect |
| --- | --- |
| Forging | laps (folded surface), cold shuts, incomplete die fill |
| Rolling | edge cracks, alligatoring, waviness from roll deflection |
| Extrusion | centre-burst (chevron) cracking, surface tearing, piping |
| Drawing | centre-burst, seams |

> [!warning] Traps
> - Using engineering strain: forming strains are large, so use true strain.
> - Using the final flow stress in a force formula where the *average* is needed.
> - Forgetting friction in forging and rolling (it can double the load at large $r/h$).
> - Applying the cold flow stress law to a hot-working problem (at high temperature it depends on strain rate: $\sigma_f=C\dot\varepsilon^m$).
> - Taking the maximum reduction as 100 %: drawing is limited to $\ln(A_0/A_f)\le1$ at best.

> [!question]- Predict first: upsetting a billet to half its height. How does the true strain compare with the engineering strain?
> Engineering strain 50 % (reduction in height) but true strain $\ln2=0.693$. Cutting the height by half again gives true strain 1.386 (additive), whereas engineering strains do not add. True strains in a sequence of passes add.

> [!question]- Why is cold rolling used for the last passes of sheet?
> It gives close tolerance, smooth finish and added strength from strain hardening. Hot rolling does the bulk reduction because the force is low; scale and dimensional variation make it unsuitable for finishing.

## 6. Connections

- [[Dislocations, Slip and Strengthening]] — work hardening in cold forming, recrystallisation in hot forming.
- [[Tensile Test, True Stress-Strain and Hardness]] — the flow-stress law and $n$ determine the forming force and the limit before necking.
- [[Kinetics of Particles - Work-Energy and Impulse-Momentum]] — forming energy is plastic work: force times distance, $W=\int F\,dx=\bar\sigma_fV\varepsilon$ for ideal deformation.
- [[Casting - Solidification Time and Riser Design]] — wrought products start as cast ingots, whose pores are closed by hot work.
