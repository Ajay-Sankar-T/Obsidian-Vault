---
tags: [concept, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
aliases: [Kinematic inversion, Slider-crank inversions, Quick return mechanism, Scotch yoke, Elliptic trammel, Oldham coupling]
---

# Kinematic Inversion — Slider-Crank and Double-Slider Families

> [!abstract] In one breath
> **Kinematic inversion** means fixing a different link of the same chain. Relative motion between links does not change, but the absolute motion, and therefore the machine, does. One chain of three revolutes and a slider (3R-1P) gives engines, quick-return drives and pumps. One chain of two revolutes and two sliders (RRPP) gives the Scotch yoke, the elliptic trammel and the Oldham coupling.

Part of [[KDoMs - MOC]]. Previous: [[Grashof Criterion and Four-Bar Inversions]]. Both chains have $n=4$, $j=4$, so $M=3(3)-8=1$ ([[Mobility - Kutzbach Equation and Exceptions]]).

## 1. The idea

Number the links 1 to 4 around the loop. Relative position and orientation of any one link fixes those of every other link in a constrained chain, so relative motion is the same whichever link is the frame. Choose the frame to choose the application.

## 2. The 3R-1P chain (slider-crank and relatives)

Links: **1** guide, **2** crank, **3** connecting rod, **4** slider. Pairs: R at 1-2, 2-3, 3-4 and P at 4-1.

| Fixed link | Mechanism | Used in |
| --- | --- | --- |
| 1 (guide) | **slider-crank** | engines, compressors, pumps |
| 2 (crank) | **Whitworth quick return** (slotted link turns fully) · rotary engine | shapers, slotters |
| 3 (rod) | **crank and slotted lever** (lever oscillates) · oscillating-cylinder engine | shapers, steam engines |
| 4 (slider) | **hand pump / pendulum pump** | pumps |

![[FND-5-slider-crank.png]]

**Left.** The slider's displacement is a cosine distorted by the finite rod: the shorter $\ell/r$, the more lopsided the curve, and the stroke is $2r$ for an in-line crank. Offsetting the guide by $e$ shifts the whole curve and changes the stroke slightly.

**Right.** Quick return needs a mechanism that sweeps the crank through unequal angles for the two strokes. With $\alpha$ the angle between the two dead-centre crank positions the **time ratio** is $(180^\circ+\alpha)/(180^\circ-\alpha)$:

$$
\text{Whitworth: } \frac{360^\circ-2\beta}{2\beta},\ \beta=\cos^{-1}\frac rd,\qquad
\text{offset slider-crank: }\alpha=\sin^{-1}\frac{e}{\ell-r}-\sin^{-1}\frac{e}{\ell+r}
$$

($r$ = crank, $d$ = distance between the two fixed pivots.) Examples: Whitworth with $r/d=0.5$: $\beta=60^\circ$, ratio $\mathbf{2.00}$; $r/d=0.8$: $3.88$. An offset slider-crank with $r=1,\ \ell=4,\ e=2.5$ only reaches $\alpha=26.4^\circ$, ratio $1.34$. A slotted-lever drive reaches larger ratios than an offset slider-crank for the same size.

## 3. The double-slider chain (RRPP)

Pairs in cyclic order R, R, P, P. Three inversions are standard:

| Fixed link | Mechanism | Output |
| --- | --- | --- |
| frame with a slider guide for the yoke | **Scotch yoke** | yoke moves as $x=r\cos\theta$ |
| frame with two perpendicular slots | **elliptic trammel** | a point on the bar traces an ellipse |
| frame carrying two parallel shafts | **Oldham coupling** | joins parallel offset shafts, same speed |

![[FND-7-double-slider.png]]

- **Scotch yoke.** The slider-crank without rod-obliquity: the yoke's motion is an exact sine, so its velocity and acceleration are exact harmonics. This is why it is used in valve actuators and test shakers.
- **Elliptic trammel.** A bar of length $a+b$ has its ends in two perpendicular slots. A point at distance $a$ from one end and $b$ from the other has coordinates $(a\cos t,\ b\sin t)$: an ellipse with semi-axes $a$ and $b$. At $a=b$ it is a circle (the bar's midpoint).
- **Oldham coupling.** Two shafts with parallel axes offset by $e$ drive an intermediate disc through perpendicular slots. The two slot lines are always perpendicular, one through each shaft axis, so they cross on the circle of diameter $e$ (Thales): the disc centre goes round it **twice per shaft turn** at constant speed, and the shafts turn at equal speed. The discs absorb the offset by sliding.

A fourth member, **RPRP**, appears as automobile steering linkage (Davis-type).

> [!warning] Traps
> - Calling a quick-return mechanism "a four-bar": it is a slider chain; the time ratio comes from a crank angle, not from link lengths.
> - Writing $\alpha$ for the stroke angle instead of the *excess* of the working stroke over $180^\circ$.
> - Assuming an offset always helps: $e$ raises the return ratio only a little and changes the stroke.

> [!question]- Predict first: a Whitworth drive with $r/d=0.5$. How much faster is the return stroke?
> $\beta=\cos^{-1}0.5=60^\circ$, so the crank sweeps $120^\circ$ during the return and $240^\circ$ during the cut: the return is **twice as fast**.

> [!question]- Why does the Scotch yoke give a pure sine but the slider-crank doesn't?
> The yoke has no connecting rod, so the slider's position depends on the crank angle only through $r\cos\theta$. In the slider-crank the rod's angle also changes with $\theta$ and adds the second-harmonic term ($\approx\frac{r^2}{4\ell}\cos2\theta$).

## 4. Connections

- [[Kinematic Pairs, Links and Chains]] — the R and P pairs that make up each chain.
- [[Velocity and Acceleration - Analytical Method]] — the slider-crank analysis, with the $r/\ell$ expansion behind the second harmonic.
- [[Velocity and Acceleration - Graphical Methods (Polygons)]] — the slotted-lever case uses the coincident-point (Coriolis) construction: [[Problem-2.19-solution]].
- [[The Universal Second-Order Linear System]] — the Scotch yoke's exact sine is the input a spring-mass system sees in a forced-vibration test.
