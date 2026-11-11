---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Fatigue, S-N curve, Endurance limit, Marin factors, Goodman diagram, Stress-life, High-cycle fatigue, Mean stress, Gerber, Soderberg]
---

# Fatigue Failure — S–N Curve, Marin Factors and Goodman Diagram

> [!abstract] In one breath
> A part loaded again and again fails at stresses far below its static strength: a **crack starts at a surface flaw, grows each cycle, and the section finally breaks suddenly**. **High-cycle fatigue** is handled by the **S–N curve** (stress amplitude against life), an **endurance limit** corrected by Marin factors for your part, and a **mean-stress correction** (Goodman).

Part of [[Materials and Design - MOC]]. Previous: [[Fracture Mechanics - Stress Intensity and Griffith]]. Next: [[Fatigue Crack Growth - Paris Law]]. Applied in: [[Shaft Design - Static and Fatigue Loading]], [[Helical Springs]], [[Bolted Joints - Preload and Joint Stiffness]].

## 1. Stress cycle

A cycle between $\sigma_{max}$ and $\sigma_{min}$:

$$
\sigma_m=\frac{\sigma_{max}+\sigma_{min}}2,\quad \sigma_a=\frac{\sigma_{max}-\sigma_{min}}2,\quad R=\frac{\sigma_{min}}{\sigma_{max}}
$$

Fully reversed: $\sigma_m=0$, $R=-1$ (rotating shaft in bending). Repeated: $R=0$.

## 2. The S–N curve

A fatigue test cycles specimens at several amplitudes and records cycles to failure $N$. For steels the curve flattens at about $10^6$ cycles into the **endurance limit** $S_e$ (non-ferrous alloys have no true limit; quote the strength at $5\times10^8$ cycles).

- **Low cycle** ($N<10^3$): plastic strain controls life (strain-life).
- **High cycle** ($10^3<N<10^6$): stress-life, a straight line on log–log axes (Basquin): $S_f=aN^b$.
- **Infinite life** ($N>10^6$): $\sigma_a<S_e$.

For steels, with $S_e'$ the specimen endurance limit:

$$
S_e'=0.5\,S_{ut}\ (S_{ut}\le1400\ \text{MPa}),\qquad S_f(10^3)=f\,S_{ut}\ (f\approx0.9),\qquad
a=\frac{(fS_{ut})^2}{S_e},\ \ b=-\frac13\log_{10}\frac{fS_{ut}}{S_e}
$$

## 3. Marin factors

The laboratory $S_e'$ is for a polished 7.5 mm specimen. For a real part:

$$
S_e=k_ak_bk_ck_dk_e\,S_e'
$$

| Factor | Effect | Typical value |
| --- | --- | --- |
| $k_a$ surface | rougher surface, earlier crack | machined: $4.51S_{ut}^{-0.265}$; ground $1.58S_{ut}^{-0.085}$; hot-rolled $57.7S_{ut}^{-0.718}$ ($S_{ut}$ in MPa) |
| $k_b$ size | more volume, more flaws | $1.24d^{-0.107}$ (2.79–51 mm), 1 for axial |
| $k_c$ load | bending 1, axial 0.85, torsion 0.59 | |
| $k_d$ temperature | | 1 at room temperature |
| $k_e$ reliability | scatter | 50 %: 1; 90 %: 0.897; 99 %: 0.814; 99.9 %: 0.753 |

Also stress concentration: use the fatigue concentration $K_f=1+q(K_t-1)$ with notch sensitivity $q\le1$ on the **alternating** stress.

## 4. Mean stress

A tensile mean stress lowers the allowed amplitude. Plot $\sigma_a$ against $\sigma_m$: the endurance limit $S_e$ on the vertical axis, the tensile strength $S_{ut}$ on the horizontal, and a failure line between them.

| Criterion | Line | Safety factor $n$ |
| --- | --- | --- |
| **Goodman** | straight line $\sigma_a/S_e+\sigma_m/S_{ut}=1$ | $\dfrac1n=\dfrac{\sigma_a}{S_e}+\dfrac{\sigma_m}{S_{ut}}$ |
| Gerber | parabola $\sigma_a/S_e+(\sigma_m/S_{ut})^2=1$ | $n=\dfrac12\Big(\dfrac{S_{ut}}{\sigma_m}\Big)^2\dfrac{\sigma_a}{S_e}\Big[-1+\sqrt{1+\Big(\dfrac{2\sigma_mS_e}{S_{ut}\sigma_a}\Big)^2}\Big]$ |
| Soderberg | line to $S_y$ instead of $S_{ut}$ | $\dfrac1n=\dfrac{\sigma_a}{S_e}+\dfrac{\sigma_m}{S_y}$ |
| Langer (first-cycle yield) | $\sigma_a+\sigma_m=S_y$ | |

Goodman is the usual choice for design (conservative against the data, which scatter between Goodman and Gerber). **Compressive mean stress** is not harmful: use $\sigma_m=0$. **Multiaxial** stress: replace $\sigma_a,\sigma_m$ by the von Mises values $\sigma_a',\sigma_m'$ (as in the shaft note).

## 5. Worked example

$S_{ut}=800$ MPa steel, machined surface, $d\approx30$ mm ($k_b=0.85$), 99 % reliability, bending.

$$
k_a=4.51(800)^{-0.265}=0.767,\ \ S_e=0.767(0.85)(0.814)(0.5\times800)=\mathbf{212\ MPa}
$$

$$
a=\frac{(0.9\times800)^2}{212}=2442,\quad b=-\frac13\log\frac{720}{212}=-0.177
$$

**Life at a given amplitude.** $\sigma_a=300$ MPa fully reversed: $N=(300/2442)^{1/(-0.177)}=\mathbf{1.4\times10^5}$ cycles.

**Mean stress.** $\sigma_a=150$, $\sigma_m=100$ MPa: Goodman $n=1/(150/212+100/800)=\mathbf{1.20}$; Gerber $n=1.37$. The equivalent fully reversed amplitude is $\sigma_{ar}=\sigma_a/(1-\sigma_m/S_{ut})=171$ MPa, whose finite-life value from the S–N line would be $3.4\times10^6$ cycles ($>10^6$: effectively infinite).

![[MAT-6-fatigue.png]]

## 6. Improving fatigue strength

Polish the surface or peen it (**shot peening** puts the surface in compression), cold-roll fillets and threads, reduce stress concentrations (fillet radii, relief grooves), avoid corrosion (corrosion fatigue has no endurance limit), and keep tensile mean stresses low (bolt preload keeps the amplitude small: [[Bolted Joints - Preload and Joint Stiffness]]).

> [!warning] Traps
> - Using $S_e=0.5S_{ut}$ **without** Marin factors for a real part (the answer is often 2× too optimistic).
> - Applying $K_f$ to the mean stress of a ductile steel (usually applied to the alternating stress only).
> - Treating a compressive mean stress as harmful.
> - Applying the S–N endurance limit to aluminium (no limit): use the strength at $5\times10^8$ cycles.
> - Comparing $\sigma_{max}$ with $S_e$: it is the **amplitude** that matters, together with the mean.

> [!question]- Predict first: a rotating shaft's bending stress is steady in space (the load direction is fixed). Is it a fatigue problem?
> Yes. The shaft turns, so each surface point goes from tension to compression every revolution: $\sigma_m=0$, $\sigma_a=\sigma_{max}$. A **non-rotating** shaft under a steady load is a static problem.

> [!question]- Two parts have the same $S_{ut}$. One is ground, one rough machined. By how much does $S_e$ differ?
> $k_a=0.90$ (ground) against $0.77$ (machined) for $S_{ut}=800$ MPa: the ground part is 17 % stronger in fatigue, at the same static strength.

## 7. Connections

- [[Tensile Test, True Stress-Strain and Hardness]] — $S_{ut}$ is the starting point, and hardness gives a quick $S_{ut}$.
- [[Mohr's Circle for Stress]] — combined loading for the equivalent stresses.
- [[Fatigue Crack Growth - Paris Law]] — what happens after a crack exists; the S–N approach lumps initiation and growth together.
- [[Dislocations, Slip and Strengthening]] — fatigue cracks nucleate in persistent slip bands, where cyclic slip roughens the surface.
