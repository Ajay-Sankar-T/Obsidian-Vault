---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Tresca, von Mises, Maximum shear stress theory, Distortion energy, Maximum normal stress, Coulomb-Mohr, Failure theories, Yield criteria]
---

# Static Failure Theories — Tresca and von Mises

> [!abstract] In one breath
> A tensile test gives one number ($S_y$). A real part has a **combined** stress state. A failure theory converts the combined state into an equivalent tension and compares it with the test value. **Ductile** metals yield by shear: use **Tresca** (conservative, simple) or **von Mises** (closer to the data). **Brittle** materials crack in tension: use **maximum normal stress** or **Coulomb–Mohr** with the very different tensile and compressive strengths.

Part of [[Materials and Design - MOC]]. Previous: [[Tensile Test, True Stress-Strain and Hardness]]. Next: [[Fracture Mechanics - Stress Intensity and Griffith]], [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]].

## 1. First find the principal stresses

For plane stress ($\sigma_x,\sigma_y,\tau_{xy}$), with the Mohr's-circle centre and radius:

$$
\sigma_{1,2}=\frac{\sigma_x+\sigma_y}{2}\pm R,\qquad R=\sqrt{\Big(\frac{\sigma_x-\sigma_y}{2}\Big)^2+\tau_{xy}^2},\qquad \sigma_3=0
$$

Order them $\sigma_1\ge\sigma_2\ge\sigma_3$ (including the zero third stress).

## 2. Ductile materials

| Theory | Condition | Plane-stress form | Safety factor |
| --- | --- | --- | --- |
| **Tresca** (max shear) | yield when $\tau_{max}=S_y/2$, i.e. $\sigma_1-\sigma_3=S_y$ | $\max(|\sigma_1|,|\sigma_2|,|\sigma_1-\sigma_2|)=S_y$ | $n=S_y/(\sigma_1-\sigma_3)$ |
| **von Mises** (distortion energy) | yield when the distortion energy equals that at yield in tension | $\sigma'=\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}=S_y$; with $\tau$: $\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}$ | $n=S_y/\sigma'$ |

Both ignore the **hydrostatic** part of the stress (equal tension or compression on all sides does not yield metals). von Mises is the smooth ellipse through the corners of Tresca's hexagon; they agree in uniaxial tension and in equal biaxial tension and differ most (by 15 %) in pure shear:

$$
\text{pure shear: Tresca } \tau_y=0.5S_y,\qquad \text{von Mises } \tau_y=0.577S_y
$$

Experiments on ductile steels lie closer to von Mises; Tresca is used when a conservative design is wanted or hand calculation is quick.

## 3. Brittle materials

Brittle materials (cast iron, ceramics, glass) have $S_{uc}\gg S_{ut}$.

| Theory | Condition |
| --- | --- |
| Maximum normal stress (Rankine) | fracture when $\sigma_1=S_{ut}$ or $\sigma_3=-S_{uc}$ |
| **Coulomb–Mohr** | $\sigma_1\ge0\ge\sigma_3$: $\dfrac{\sigma_1}{S_{ut}}-\dfrac{\sigma_3}{S_{uc}}=\dfrac1n$ |
| Modified Mohr | like Coulomb–Mohr but in quadrant IV follows the experimental line from $(S_{ut},0)$ through $(S_{ut},-S_{ut})$ |

## 4. Worked example

Plane stress $\sigma_x=100$, $\sigma_y=-60$, $\tau_{xy}=40$ MPa.

$$
\text{centre }20,\ R=\sqrt{80^2+40^2}=89.4\ \Rightarrow\ \sigma_1=109.4,\ \sigma_2=-69.4\ \text{MPa},\ \tau_{max}=89.4
$$

| Material | Theory | Equivalent stress | Safety factor |
| --- | --- | --- | --- |
| Steel, $S_y=300$ MPa | Tresca | $\sigma_1-\sigma_2=178.9$ | **1.68** |
| Steel, $S_y=300$ MPa | von Mises | $\sigma'=156.2$ | **1.92** |
| Cast iron, $S_{ut}=200$, $S_{uc}=700$ MPa | Coulomb–Mohr | | **1.55** |
| Cast iron | maximum normal stress | | 1.83 (unconservative) |

For the steel the two theories differ by 14 %: Tresca is the conservative one. For the cast iron the compressive $\sigma_2$ weakens the part (a compressive second stress lowers the tension needed to fracture), which Coulomb–Mohr sees and maximum normal stress misses.

![[MAT-4-failure.png]]

Inside the curve is safe. The hexagon (Tresca) lies inside the ellipse (von Mises), so it is the more conservative.

## 5. Method

1. Draw the stress element and compute $\sigma_x,\sigma_y,\tau_{xy}$ (use $T$, $M$, $P$ and the section: [[Shaft Design - Static and Fatigue Loading]]).
2. Principal stresses (or Mohr's circle).
3. Ductile: Tresca or von Mises. Brittle: maximum normal or Coulomb–Mohr.
4. Compare with $S_y$ (ductile) or $S_{ut},S_{uc}$ (brittle); apply the safety factor.

> [!warning] Traps
> - Forgetting the third principal stress $\sigma_3=0$ in Tresca: with $\sigma_1,\sigma_2>0$ the largest difference is $\sigma_1-0$.
> - Using von Mises with *signed* components wrong: the cross term $-\sigma_1\sigma_2$ is **negative** for tension–tension and **positive** for tension–compression (so tension–compression is worse).
> - Applying a ductile theory to cast iron, or Coulomb–Mohr to steel.
> - Using $S_{ut}$ in compression for brittle materials.
> - Treating failure theories as exact: they are fits.

> [!question]- Predict first: a thin-walled sealed tube under internal pressure has $\sigma_\theta=2\sigma_a=\sigma$. Does von Mises or Tresca allow a higher pressure?
> von Mises: $\sigma'=\sqrt{\sigma^2-\sigma\cdot\sigma/2+\sigma^2/4}=0.866\sigma$, so yield at $\sigma=1.155S_y$. Tresca: largest difference is $\sigma_\theta-0=\sigma$ (third stress, radial, $\approx0$), so yield at $\sigma=S_y$. von Mises permits **15 % more** pressure.

> [!question]- Why does hydrostatic pressure not yield a metal?
> Equal all-round pressure changes volume but not shape, and slip needs shear. Both Tresca (differences of principal stresses) and von Mises (differences again) contain only differences, so a shift of all three stresses by the same amount changes nothing.

## 6. Connections

- [[Mohr's Circle for Stress]] and [[Plane Stress Transformation]] — the principal stresses used here.
- [[Thin Cylindrical and Spherical Pressure Vessels]] — hoop and axial stresses in the worked prediction above.
- [[Torsion of Circular Shafts]] — pure shear: $\tau_y=0.5S_y$ (Tresca) or $0.577S_y$ (von Mises).
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — the principal stresses are eigenvalues of the stress tensor; the invariants are what the theories use.
- [[Energy Methods - A Unified View]] — von Mises is an energy criterion: distortion energy per volume.
