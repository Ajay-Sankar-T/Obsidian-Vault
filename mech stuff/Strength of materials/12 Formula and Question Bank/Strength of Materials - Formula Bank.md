---
title: Strength of Materials – Formula Bank
tags: [strength-of-materials, formula-bank, concept]
up: "[[Strength of Materials - MOC]]"
aliases: [SoM formulas, Strength of Materials formula sheet, AM2200 formula sheet, Mechanics of materials formulas]
---

# Strength of Materials – Formula Bank

Part of [[Strength of Materials - MOC]] · practice: [[Strength of Materials - Question Bank]] · lab-flavoured exams: [[Applied Mechanics Lab - Mock Papers]]

> [!abstract] How to use it
> One page for the whole course: eleven chapters in the order of the MOC, then the lab formulas that the AM2540 paper asks, then a "which method?" table. Each row says **what it gives and when it holds**. Every number in the [[Strength of Materials - Question Bank]] is recomputed in `Tools/sm_bank_core.py`. Units: N, mm, MPa ($=$ N/mm²) unless stated. Rule of thumb for any answer: units, then sign, then a limiting case.

## 0. Notation, constants, signs

| Symbol | Meaning | Symbol | Meaning |
|---|---|---|---|
| $\sigma,\ \tau$ | normal, shear stress | $\varepsilon,\ \gamma$ | normal, shear strain |
| $E,\ G,\ \nu,\ K$ | Young's, shear, bulk modulus; Poisson's ratio | $\alpha$ | thermal expansion coefficient |
| $A,\ I,\ J,\ S$ | area, second moment, polar moment, section modulus | $r=\sqrt{I/A}$ | radius of gyration |
| $\sigma_Y,\ \sigma_u$ | yield, ultimate strength | $FS$ | factor of safety $=$ failure load / allowable load |

| Material | $E$ (GPa) | $G$ (GPa) | $\nu$ | $\alpha$ ($10^{-6}$/°C) | strength (MPa) |
|---|---|---|---|---|---|
| Mild steel | 200–210 | 79–80 | 0.30 | 12 | $\sigma_Y\approx250$, $\sigma_u\approx400$ |
| Aluminium alloy | 70 | 26 | 0.33 | 23 | $\sigma_Y\approx95$–$270$ |
| Copper | 110–120 | 44 | 0.34 | 17 | $\sigma_Y\approx70$ |
| Brass | 100 | 38 | 0.34 | 19 | $\sigma_Y\approx100$–$200$ |
| Cast iron | 100–170 | 40–65 | 0.26 | 10 | $\sigma_{u,T}\approx150$–$250$, $\sigma_{u,C}\approx600$ |
| Concrete | 25–30 | 10–12 | 0.2 | 10 | $\sigma_{u,C}\approx20$–$40$, tension $\approx0$ |

**Sign conventions.** Tension $+$. Sagging bending moment $+$ (top fibre in compression). Shear force $+$ when it turns a beam element clockwise. In Mohr's circle, plot $\tau$ clockwise-positive *downwards*. Torque $+$ by the right-hand rule pointing out of the cut face.

**Section properties** (centroidal axis, $b$ width, $h$ depth):

| Section | $A$ | $I$ | $S=I/c$ | note |
|---|---|---|---|---|
| Rectangle | $bh$ | $bh^3/12$ | $bh^2/6$ | $r=h/\sqrt{12}$ |
| Circle, $d$ | $\pi d^2/4$ | $\pi d^4/64$ | $\pi d^3/32$ | $J=\pi d^4/32=2I$, $r=d/4$ |
| Hollow circle | $\tfrac\pi4(d_o^2-d_i^2)$ | $\tfrac\pi{64}(d_o^4-d_i^4)$ | $I/(d_o/2)$ | $J=2I$ |
| Thin tube (mean radius $R$, wall $t$) | $2\pi Rt$ | $\pi R^3t$ | | $J=2\pi R^3t$ |
| Triangle (base $b$, height $h$) | $bh/2$ | $bh^3/36$ about the centroid, $bh^3/12$ about the base | | centroid $h/3$ from the base |
| Semicircle, $R$ | $\pi R^2/2$ | $0.1098\,R^4$ about the centroid | | centroid $4R/3\pi$ from the flat |

Parallel axis: $I=I_c+Ad^2$. Composite: find $\bar y=\sum A_iy_i/\sum A_i$ first. $I\propto h^3$: doubling the depth multiplies the stiffness by 8.

## 1. Stress and strain

| Quantity | Formula | Remark |
|---|---|---|
| Normal / shear stress | $\sigma=P/A$, $\tau=V/A$ | area **perpendicular** to the force |
| Bearing stress | $\sigma_b=P/(d\,t)$ | projected area of a pin or rivet |
| Strains | $\varepsilon=\delta/L$, $\gamma=\tan\gamma\approx\gamma$ (rad) | $\mu\varepsilon=10^{-6}$ |
| Hooke's law | $\sigma=E\varepsilon$, $\ \tau=G\gamma$ | linear range only |
| Poisson's ratio | $\nu=-\varepsilon_{lat}/\varepsilon_{ax}$ | $0<\nu<0.5$ for ordinary solids |
| Moduli relation | $G=\dfrac{E}{2(1+\nu)}$, $\ K=\dfrac{E}{3(1-2\nu)}$ | $\nu=0.5$ means incompressible ($K\to\infty$) |
| Generalised Hooke | $\varepsilon_x=\dfrac{\sigma_x-\nu(\sigma_y+\sigma_z)}{E}$ and cyclic | add $\alpha\Delta T$ if heated |
| Plane stress ($\sigma_z=0$) | $\varepsilon_z=-\dfrac{\nu}{E}(\sigma_x+\sigma_y)$ | thickness changes |
| Plane strain ($\varepsilon_z=0$) | $\sigma_z=\nu(\sigma_x+\sigma_y)$ | thick or confined body |
| Volumetric strain | $e=\varepsilon_x+\varepsilon_y+\varepsilon_z=\dfrac{1-2\nu}{E}(\sigma_x+\sigma_y+\sigma_z)$ | $=\sigma_m/K$ for pressure $p$: $e=-p/K$ |
| Resilience | $u_r=\sigma_Y^2/2E$ | area under the curve to yield |
| Toughness | $u_t=\int\sigma\,d\varepsilon$ | area to fracture |
| True stress / strain | $\sigma_t=S(1+e),\ \ \varepsilon_t=\ln(1+e)$ | only up to necking |
| Ductility | $\%EL=\dfrac{L_f-L_0}{L_0}$, $\ \%RA=\dfrac{A_0-A_f}{A_0}$ | $\%EL$ depends on gauge length |
| Allowable stress | $\sigma_{all}=\sigma_Y/FS$ (ductile), $\sigma_u/FS$ (brittle) | |

![[SM-FB-1-stress-strain.png]]

**Figure:** the labelled engineering curve of mild steel and the brittle contrast. The elastic part is exaggerated. The $0.2\%$ offset line gives the yield strength when there is no plateau. Unloading is **parallel to the elastic line**, so a permanent set remains.

## 2. Axial loading and thermal effects

| Case | Formula |
|---|---|
| Prismatic bar | $\delta=\dfrac{PL}{AE}$, stiffness $k=\dfrac{AE}{L}$ |
| Several segments | $\delta=\sum\dfrac{P_iL_i}{A_iE_i}$ ($P_i$ is the internal force in segment $i$) |
| Varying section or load | $\delta=\displaystyle\int_0^L\dfrac{P(x)}{A(x)E}\,dx$ |
| Self-weight (uniform bar) | $\delta=\dfrac{\gamma L^2}{2E}=\dfrac{WL}{2AE}$; stress at the support $=(P+W)/A$ |
| Tapered round bar ($d_1\to d_2$) | $\delta=\dfrac{4PL}{\pi Ed_1d_2}$ |
| Thermal strain | $\varepsilon_T=\alpha\Delta T$, free elongation $\alpha\Delta TL$ |
| Fully restrained bar | $\sigma=-E\alpha\Delta T$ (compression on heating) |
| Wall gap $g$ | stress only if $\alpha\Delta TL>g$; then $\sigma=E(\alpha\Delta TL-g)/L$ |
| Parallel members (same $\delta$) | $\dfrac{F_1}{k_1}=\dfrac{F_2}{k_2}$, $F_1+F_2=P$; stiffnesses add |
| Series members (same $F$) | flexibilities add: $1/k=\sum1/k_i$ |
| Misfit or tightened nut | compatibility: $\delta_1+\delta_2=\Delta_{fit}$ (nut advance $=$ turns $\times$ pitch) |

**Indeterminate recipe (three steps):** equilibrium, compatibility (relate the deformations), force–deformation law (insert $\delta=FL/AE+\alpha\Delta TL$). Solve. Check that the answer satisfies the compatibility equation you did not use last.

## 3. Torsion

| Quantity | Formula |
|---|---|
| Shear stress | $\tau=\dfrac{Tr}{J}$, $\ \tau_{max}=\dfrac{Tc}{J}=\dfrac{T}{S_p}$ |
| Polar moment | solid $\dfrac{\pi d^4}{32}$; hollow $\dfrac{\pi(d_o^4-d_i^4)}{32}=\dfrac{\pi d_o^4}{32}(1-k^4)$, $k=d_i/d_o$ |
| Angle of twist | $\phi=\dfrac{TL}{GJ}$, $\ \phi=\sum\dfrac{T_iL_i}{G_iJ_i}$, $\ \phi=\displaystyle\int\dfrac{T\,dx}{GJ}$ |
| Torsional stiffness | $k_t=GJ/L$ |
| Power | $P=T\omega=\dfrac{2\pi NT}{60}$ ($N$ rpm, $T$ in N·m, $P$ in W) |
| Strength design | $d_o^3=\dfrac{16T}{\pi\tau_{all}(1-k^4)}$ |
| Stiffness design | $d_o^4=\dfrac{32T}{\pi G\theta_{all}(1-k^4)}$ ($\theta$ in rad per unit length); **take the larger** |
| Hollow vs solid, same torque and $\tau$ | $\dfrac{d_o}{d}=(1-k^4)^{-1/3}$; mass ratio $=\dfrac{1-k^2}{(1-k^4)^{2/3}}<1$ |
| Same material, same mass | $T_{hollow}/T_{solid}=\dfrac{1-k^4}{(1-k^2)^{3/2}}$ |
| Two shafts in series | same $T$, twists add |
| Two shafts in parallel (composite) | same $\phi$: $\dfrac{T_1}{G_1J_1}=\dfrac{T_2}{G_2J_2}$, $T_1+T_2=T$ |
| Fixed–fixed, torque $T_0$ at $a$ from $A$ ($b=L-a$) | $T_A=T_0b/L$, $T_B=T_0a/L$ |
| Gear pair | $T_2/T_1=N_1/N_2$ (speed ratio inverted), $P$ unchanged |
| Thin closed tube | $\tau=\dfrac{T}{2A_mt}$, $\ \phi=\dfrac{TL}{4A_m^2G}\oint\dfrac{ds}{t}$ |
| Strain energy | $U=\dfrac{T^2L}{2GJ}$ |

The torsion formula needs a **circular** section (plane sections stay plane, radial lines stay straight), a linear elastic material and a prismatic shaft away from the ends. Non-circular sections warp: do not use $J$.

## 4. Shear force and bending moment

$$\frac{dV}{dx}=-w,\qquad \frac{dM}{dx}=V,\qquad \Delta V=-P\text{ at a point load},\qquad \Delta M=+M_0\text{ at an applied clockwise couple}$$

| Rule | Meaning |
|---|---|
| $V_2-V_1=-\int w\,dx$ | change in shear $=-$ area of the load diagram |
| $M_2-M_1=\int V\,dx$ | change in moment $=$ area of the shear diagram |
| $V=0$ | $M$ is a maximum or minimum |
| $M=0$ with a sign change | point of contraflexion |
| Degree | $w$ constant $\Rightarrow$ $V$ linear, $M$ parabolic; point load $\Rightarrow$ $V$ steps, $M$ has a kink |

Procedure: reactions from $\sum F=0$, $\sum M=0$; then cut, or integrate. Closing check: $V$ and $M$ return to zero at a free end and $M=0$ at a pin.

![[SM-FB-3-beam-cases.png]]

**Figure:** the four loadings that appear most; the labelled values are the ones to know cold (see §8 for the deflections).

## 5. Bending stresses

| Quantity | Formula |
|---|---|
| Curvature | $\dfrac1\rho=\dfrac{M}{EI}$ |
| Flexure formula | $\sigma=\dfrac{My}{I}$, $\ \sigma_{max}=\dfrac{M}{S}$ ($y$ from the centroidal neutral axis) |
| Section modulus design | $S_{req}=M_{max}/\sigma_{all}$; circle: $d=(32S/\pi)^{1/3}$; $1\!:\!2$ rectangle: $h=(12S)^{1/3}$ |
| Beam of uniform strength | $S(x)\propto M(x)$ |
| Composite beam (transformed section) | $n=E_2/E_1$; replace material 2 by width $nb$; $\sigma_1=-My/I_{tr}$, $\sigma_2=-nMy/I_{tr}$ |
| Unsymmetric bending (principal axes) | $\sigma=-\dfrac{M_zy}{I_z}+\dfrac{M_yz}{I_y}$; neutral axis $\tan\alpha=\dfrac{I_z}{I_y}\tan\theta$ ($\theta$ = load angle from the $y$ axis) |
| Axial plus bending | $\sigma=\dfrac PA\pm\dfrac{My}{I}$ |
| Eccentric load $P$ at $e$ | $\sigma=\dfrac PA\Big(1\pm\dfrac{ec}{r^2}\Big)$; no tension if $e\le$ kern |
| Kern (core) | rectangle $h/6$ each way (middle third); circle $d/8$ ($=$ one quarter of the radius) |
| Neutral axis for eccentric load | $y_0=r^2/e$ from the centroid |

Plane sections stay plane, so strain is linear in $y$ and the neutral axis passes through the **centroid** only for homogeneous beams with no axial force. For a bimodular or composite beam it shifts: find it from $\sum E_i\int y\,dA=0$.

## 6. Shear stress in beams

$$\tau=\frac{VQ}{It},\qquad Q=\int_{A'}y\,dA=A'\bar y',\qquad q=\tau t=\frac{VQ}{I}\ \text{(shear flow)}$$

| Section | $\tau_{max}$ (at the neutral axis) | Ratio to $V/A$ |
|---|---|---|
| Rectangle | $\dfrac{3V}{2A}$, parabolic, zero at top and bottom | 1.5 |
| Solid circle | $\dfrac{4V}{3A}$ | 1.33 |
| Thin circular tube | $\dfrac{2V}{A}$ | 2 |
| I-section | web carries $\approx$ 90–95 % of $V$; $\tau_{web}\approx V/(t_wh_w)$ | slightly above 1 |

| Use | Formula |
|---|---|
| Glue line or weld | $\tau_{glue}=\dfrac{VQ}{Ib_{glue}}$ with $Q$ of the part on one side of the joint |
| Fasteners (nails, bolts, rivets) | spacing $s=\dfrac{nF}{q}=\dfrac{nFI}{VQ}$ ($n$ fasteners per cross-section, $F$ their shear capacity) |
| Jump at a flange–web joint | $\tau$ in the flange is $t_w/b_f$ times $\tau$ in the web (same $q$) |

Shear is largest where bending is zero (neutral axis) and zero where bending is largest (extreme fibre): check both for short, deep or built-up beams. For slender beams bending governs.

## 7. Transformation of stress and strain

| Quantity | Formula |
|---|---|
| Stress on a plane at $\theta$ (counter-clockwise from $x$) | $\sigma_\theta=\dfrac{\sigma_x+\sigma_y}{2}+\dfrac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$ |
| | $\tau_\theta=-\dfrac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta$ |
| Invariant | $\sigma_x+\sigma_y=\sigma_\theta+\sigma_{\theta+90^\circ}$ |
| Principal stresses | $\sigma_{1,2}=\dfrac{\sigma_x+\sigma_y}{2}\pm R$, $\ R=\sqrt{\Big(\dfrac{\sigma_x-\sigma_y}{2}\Big)^2+\tau_{xy}^2}$ |
| Principal angle | $\tan2\theta_p=\dfrac{2\tau_{xy}}{\sigma_x-\sigma_y}$ (principal planes have $\tau=0$) |
| In-plane max shear | $\tau_{max}=R=\dfrac{\sigma_1-\sigma_2}{2}$ on planes at $45^\circ$ to principal, with $\sigma_{avg}$ on them |
| Absolute max shear | $\tau_{abs}=\dfrac{\sigma_{max}-\sigma_{min}}{2}$ over the **three** principal stresses (include $\sigma_3=0$) |
| Strain on a plane | same equations with $\sigma\to\varepsilon$, $\tau\to\gamma/2$ |
| Principal strains | $\varepsilon_{1,2}=\dfrac{\varepsilon_x+\varepsilon_y}2\pm\sqrt{\Big(\dfrac{\varepsilon_x-\varepsilon_y}2\Big)^2+\Big(\dfrac{\gamma_{xy}}2\Big)^2}$ |
| Rosette $0^\circ/45^\circ/90^\circ$ | $\varepsilon_x=\varepsilon_a$, $\varepsilon_y=\varepsilon_c$, $\gamma_{xy}=2\varepsilon_b-\varepsilon_a-\varepsilon_c$ |
| Rosette $0^\circ/60^\circ/120^\circ$ | $\varepsilon_x=\varepsilon_a$, $\varepsilon_y=\dfrac{2(\varepsilon_b+\varepsilon_c)-\varepsilon_a}{3}$, $\gamma_{xy}=\dfrac{2(\varepsilon_b-\varepsilon_c)}{\sqrt3}$ |
| Strain $\to$ stress (plane stress) | $\sigma_x=\dfrac{E}{1-\nu^2}(\varepsilon_x+\nu\varepsilon_y)$, $\ \tau_{xy}=G\gamma_{xy}$ |
| Shaft: bending $\sigma$ + torsion $\tau$ | $\sigma_{1,2}=\dfrac\sigma2\pm\sqrt{(\sigma/2)^2+\tau^2}$ |

![[SM-FB-2-mohr-circle.png]]

**Figure:** the circle for $\sigma_x=80$, $\sigma_y=-40$, $\tau_{xy}=30$ MPa. A rotation of the plane by $\theta$ is a rotation of $2\theta$ on the circle, in the same sense. $X$ and $Y$ are diametrically opposite.

**Failure criteria** (plane stress, principal stresses $\sigma_1\ge\sigma_2$, yield $\sigma_Y$):

| Theory | Safe if | For a shaft ($\sigma$, $\tau$) | Best for |
|---|---|---|---|
| Max normal stress (Rankine) | $\sigma_1\le\sigma_u$ | | brittle |
| Max shear (Tresca) | $\sigma_1-\sigma_2\le\sigma_Y$ (with $\sigma_3=0$ included) | $\sqrt{\sigma^2+4\tau^2}\le\sigma_Y$ | ductile, conservative |
| Distortion energy (von Mises) | $\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}\le\sigma_Y$ | $\sqrt{\sigma^2+3\tau^2}\le\sigma_Y$ | ductile, most accurate |

Ductile metals fail by **shear** (slip planes at $45^\circ$ in tension), brittle ones by **normal stress**: see [[Failure Planes - Ductile and Brittle Fracture]].

## 8. Deflection of beams

$$EI\frac{d^4v}{dx^4}=w,\qquad EI\frac{d^3v}{dx^3}=V,\qquad EI\frac{d^2v}{dx^2}=M,\qquad \theta=\frac{dv}{dx}$$

(With $v$ measured **upward** and sagging $M$ positive. Many problems use deflection downward: keep one convention.)

**Moment-area:** $\theta_{B/A}=\displaystyle\int_A^B\frac{M}{EI}dx$ (area of the $M/EI$ diagram); $t_{B/A}=$ moment of that area about $B$ (deviation of $B$ from the tangent at $A$). **Macaulay:** write $M$ with $\langle x-a\rangle^n$ terms, extend a UDL to the end and cancel it with a negative one; integrate twice; two boundary conditions fix $C_1$, $C_2$.

| Beam and load | Max deflection | Slope |
|---|---|---|
| Cantilever, tip load $P$ | $PL^3/3EI$ | $PL^2/2EI$ |
| Cantilever, UDL $w$ | $wL^4/8EI$ | $wL^3/6EI$ |
| Cantilever, tip couple $M_0$ | $M_0L^2/2EI$ | $M_0L/EI$ |
| Cantilever, load $P$ at $a$ from the wall | tip: $\dfrac{Pa^2(3L-a)}{6EI}$ | $Pa^2/2EI$ beyond $a$ |
| Cantilever, triangular ($w_0$ at the wall, 0 at tip) | $w_0L^4/30EI$ | $w_0L^3/24EI$ |
| Simply supported, central $P$ | $PL^3/48EI$ at the centre | $PL^2/16EI$ |
| Simply supported, UDL | $5wL^4/384EI$ at the centre | $wL^3/24EI$ |
| Simply supported, $P$ at $a$ ($b=L-a$) | under load $\dfrac{Pa^2b^2}{3EIL}$; with $b$ the **shorter** distance, max $\dfrac{Pb(L^2-b^2)^{3/2}}{9\sqrt3EIL}$ at $x=\sqrt{(L^2-b^2)/3}$ from the support at the far end of the longer segment | $\theta_A=\dfrac{Pab(L+b)}{6EIL}$ |
| Simply supported, end couple $M_0$ | $\dfrac{M_0L^2}{9\sqrt3EI}$ at $0.577L$ | $\theta_{near}=\dfrac{M_0L}{3EI}$, $\theta_{far}=\dfrac{M_0L}{6EI}$ |
| Overhang $a$, tip load $P$ (span $L$) | tip $\dfrac{Pa^2(L+a)}{3EI}$; span rises $\dfrac{PaL^2}{16EI}$ at the middle | $\theta_{support}=\dfrac{PaL}{3EI}$ |
| Fixed–fixed, central $P$ | $PL^3/192EI$; $M_{end}=M_{mid}=PL/8$ | |
| Fixed–fixed, UDL | $wL^4/384EI$; $M_{end}=wL^2/12$, $M_{mid}=wL^2/24$ | |
| Propped cantilever (fixed A, prop B), UDL | $\approx wL^4/185EI$ at $0.579L$ from A; $R_B=3wL/8$, $M_A=wL^2/8$ | |
| Propped cantilever, central $P$ | $R_B=5P/16$, $M_A=3PL/16$ | |

Stiffness $k=P/\delta$: simply supported centre $48EI/L^3$, cantilever tip $3EI/L^3$, fixed–fixed centre $192EI/L^3$. **Superposition** holds for linear materials and small deflections: split the load, add the deflections. **How to reduce a deflection** without changing load, span or material: increase $I$ ($\propto bh^3$; an I-section or a deeper beam), restrain the ends ($48\to192$), add a support, or move overhangs so that their weight hogs the span. Shear deflection is negligible for $L/h>10$.

## 9. Columns and buckling

$$P_{cr}=\frac{\pi^2EI}{(KL)^2},\qquad \sigma_{cr}=\frac{\pi^2E}{\lambda^2},\qquad \lambda=\frac{KL}{r},\qquad r=\sqrt{\frac IA}$$

| Ends | $K$ | Ends | $K$ |
|---|---|---|---|
| pinned–pinned | 1 | fixed–pinned | 0.7 (0.699) |
| fixed–free | 2 | fixed–fixed | 0.5 |
| fixed–fixed, one end free to sway | 1 | | |

| Item | Formula |
|---|---|
| Euler assumptions | straight, homogeneous, perfectly elastic, axial load through the centroid, small deflections, ideal supports, $\sigma_{cr}\le$ proportional limit |
| Axis | buckles about the axis of **least** $I$ (compute each axis with its own $K$; take the smaller $P_{cr}$) |
| Euler valid for | $\lambda\ge\lambda_c=\pi\sqrt{2E/\sigma_Y}$ (steel $\sigma_Y=250$: $\lambda_c=126$); sometimes $\lambda_p=\pi\sqrt{E/\sigma_p}$ |
| Johnson parabola ($\lambda<\lambda_c$) | $\sigma_{cr}=\sigma_Y\Big[1-\dfrac{\sigma_Y\lambda^2}{4\pi^2E}\Big]$ |
| Rankine–Gordon | $P=\dfrac{\sigma_cA}{1+a\lambda^2}$; mild steel $\sigma_c=330$ MPa, $a=1/7500$ (hinged) |
| Secant formula (eccentric $e$) | $\sigma_{max}=\dfrac PA\Big[1+\dfrac{ec}{r^2}\sec\Big(\dfrac{KL}{2r}\sqrt{\dfrac P{EA}}\Big)\Big]$, solve for $P$ iteratively |
| Allowable load | $P_{all}=P_{cr}/FS$ |
| Short columns | crush: $P=\sigma_YA$, no stability issue ($\lambda<30$ or so) |
| Section shape | for equal area, a **tube** or a square beats a thin strip; $P_{cr}\propto I_{min}$ |

![[SM-FB-4-columns.png]]

**Figure:** left, buckled shapes and $K$ (the distance between inflection points is $KL$). Right, the column curve: Euler for slender columns, Johnson for intermediate ones, crushing for short ones. Buckling depends on $E$ and $I$, **not** on strength: a stronger steel does not raise $P_{cr}$.

## 10. Energy methods

| Quantity | Formula |
|---|---|
| Strain energy density | $u=\dfrac{\sigma^2}{2E}+\dfrac{\tau^2}{2G}$ |
| Axial | $U=\dfrac{P^2L}{2AE}=\displaystyle\int\dfrac{P^2dx}{2AE}$ |
| Torsion | $U=\dfrac{T^2L}{2GJ}$ |
| Bending | $U=\displaystyle\int\dfrac{M^2dx}{2EI}$ |
| Shear (beam) | $U=\displaystyle\int\dfrac{f_sV^2dx}{2GA}$ ($f_s=1.2$ rectangle, 10/9 circle) |
| Work and energy | $U=\tfrac12P\delta$ for a single gradually applied load |
| Castigliano (2nd) | $\delta_i=\dfrac{\partial U}{\partial P_i}=\displaystyle\int\dfrac{M}{EI}\dfrac{\partial M}{\partial P_i}dx+\int\dfrac{T}{GJ}\dfrac{\partial T}{\partial P_i}dx+\sum\dfrac{PL}{AE}\dfrac{\partial P}{\partial P_i}$ |
| Dummy load | no load at the point wanted? add $Q$, differentiate, then set $Q=0$ |
| Redundants | $\partial U/\partial R=0$ (rigid support), or equals the settlement |
| Maxwell reciprocity | $\delta_{ij}=\delta_{ji}$: deflection at $i$ due to unit load at $j$ |
| Suddenly applied load | $\delta=2\delta_{st}$, stress $=2\sigma_{st}$ |
| Falling weight $W$ from $h$ above the contact | $\delta_{max}=\delta_{st}\Big(1+\sqrt{1+\dfrac{2h}{\delta_{st}}}\Big)$; impact factor $n=\delta_{max}/\delta_{st}\approx\sqrt{2h/\delta_{st}}$ |

Energy is **not** additive across loads (it is quadratic): never add $U_1+U_2$ for two loads on the same member, add the deflections instead. One equation only: use Castigliano for the deflection at the load, a dummy load for anywhere else.

## 11. Thin-walled pressure vessels

Thin means $r/t>10$. Internal gauge pressure $p$, mean radius $r$, wall $t$:

| Vessel | Stress | Strains and changes |
|---|---|---|
| Cylinder, hoop | $\sigma_h=\dfrac{pr}{t}=\dfrac{pd}{2t}$ | $\varepsilon_h=\dfrac{\sigma_h-\nu\sigma_L}{E}=\dfrac{pr}{2tE}(2-\nu)$ |
| Cylinder, longitudinal | $\sigma_L=\dfrac{pr}{2t}=\dfrac{pd}{4t}$ | $\varepsilon_L=\dfrac{pr}{2tE}(1-2\nu)$ |
| Sphere | $\sigma=\dfrac{pr}{2t}=\dfrac{pd}{4t}$ (equal in all directions) | $\varepsilon=\dfrac{pr}{2tE}(1-\nu)$ |
| Cylinder volume | | $\dfrac{\Delta V}{V}=2\varepsilon_h+\varepsilon_L=\dfrac{pr}{2tE}(5-4\nu)$; $\ \delta d=\varepsilon_hd$ |
| Radial stress | $\sigma_r\approx0$ (outer) to $-p$ (inner): neglected | |
| Max shear | in-plane $=\dfrac{\sigma_h-\sigma_L}{2}=\dfrac{pr}{4t}$; **absolute** $=\dfrac{\sigma_h}{2}=\dfrac{pr}{2t}$ (with $\sigma_3=0$) | sphere in-plane $=0$, absolute $=\dfrac{pr}{4t}$ |
| Joint efficiency $\eta$ | thickness from the **seam**: $t=\dfrac{pd}{2\sigma_{all}\eta_l}$ (hoop, longitudinal seam), $t=\dfrac{pd}{4\sigma_{all}\eta_c}$ (axial, girth seam); take the larger | |
| Strain gauge at $\theta$ to the axis | $\varepsilon_\theta=\varepsilon_L\cos^2\theta+\varepsilon_h\sin^2\theta$ | |

The vessel splits **along** its length first because $\sigma_h=2\sigma_L$. A spherical vessel needs half the wall of a cylinder of the same radius and pressure (no seam penalty).

## 12. Formulas the lab paper asks (AM2540)

| Topic | Formula | Note |
|---|---|---|
| Gauge factor | $GF=\dfrac{\Delta R/R}{\varepsilon}$ | $\approx2$ for foil gauges |
| Wheatstone bridge, output | quarter $\dfrac{V_{ex}\,GF\,\varepsilon}4$, half $\dfrac{V_{ex}\,GF\,\varepsilon}{2}$, full $V_{ex}\,GF\,\varepsilon$ | adjacent arms subtract, opposite arms add |
| Temperature compensation | dummy gauge (same material, same temperature, unstrained) in the adjacent arm, or two active gauges in adjacent arms | $\Delta R_T$ cancels |
| Cantilever surface stress | $\sigma=\dfrac{6PL}{bt^2}$, $\ \varepsilon=\sigma/E$ | $L$ from the load to the gauge |
| Mirror and scale (twist) | $\tan2\phi=\dfrac{s}{D}$, so $\phi=\tfrac12\arctan\dfrac sD\approx\dfrac{s}{2D}$ | reflected ray turns twice as much as the mirror |
| Photoelastic law | $\sigma_1-\sigma_2=\dfrac{Nf_\sigma}{t}$ | $f_\sigma$ in N/mm/fringe, $t$ specimen thickness |
| Diametral disk (load $P$, diameter $D$) | $\sigma_1-\sigma_2\big|_{centre}=\dfrac{8P}{\pi Dt}$, so $N=\dfrac{8P}{\pi Df_\sigma}$ | $N\propto1/f_\sigma$ |
| Pure bending, birefringence | fringe order is linear in $y$ and zero at the neutral axis; extreme fibre $\sigma=Nf_\sigma/t$ | one principal stress is zero |
| Three-point bend, stress | $\sigma_{max}=\dfrac{3PL}{2bh^2}$ | bottom face, under the load |
| Three-point bend, $E$ | $E=\dfrac{PL^3}{4bh^3\delta}=\dfrac{L^3m}{4bh^3}$ | $m=P/\delta$ is the slope |
| Tensile specimens, $d$ vs $2d$ | load $\propto A\propto d^2$ (4 times), $\delta\propto L_0$; stress–strain curve is **identical** | size-independent material property |
| Torsion test | $G=\dfrac{TL}{J\phi}$ | $J=\pi d^4/32$ |

Theory behind these: [[Lab - Strain Gauge Measurement on a Cantilever Beam]], [[Lab - Photoelasticity - Fringes and Stress]], [[Lab - Torsion of Circular Shafts]], [[Lab - Deflection of Beams (Three-Point Bending)]], [[Lab - Buckling of Struts]].

## 13. Which method?

| The problem says | Use |
|---|---|
| Bar, several loads or materials, find the elongation | $\sum PL/AE$ with **internal** forces |
| Two members share a deflection, load unknown split | compatibility + $\delta=FL/AE$ |
| Heated, ends fixed or a gap | $\alpha\Delta TL$ vs the gap |
| Shaft: power, rpm, allowable stress and twist | $T=P/\omega$, strength and stiffness design, take the larger |
| Shaft fixed at both ends, torque in the middle | compatibility $\phi_A+\phi_B=0$ |
| Max moment, contraflexion | reactions, then $V=0$ and $M=0$ |
| Max stress in a beam | $M_{max}$, $\sigma=M/S$, then check $V$ |
| Unsymmetric section or inclined load | principal axes, $\sigma=M_zy/I_z+M_yz/I_y$ |
| Glued or nailed built-up beam | $q=VQ/I$ |
| Stress on an inclined plane, max shear | transformation or Mohr's circle |
| Gauge readings given | rosette formulas $\to$ strain circle $\to$ Hooke $\to$ stress |
| Deflection of a standard loading | table (§8) and superposition |
| Deflection, several loads, discontinuity | Macaulay |
| Slope or deflection at a point from a $M$ diagram | moment-area |
| Indeterminate beam or frame, deflection at a load | Castigliano |
| Falling load, sudden load | $\delta_{st}$, then $n$ |
| Slender strut | Euler $\pi^2EI/(KL)^2$ with the weak axis; check $\lambda\ge\lambda_c$ |
| Intermediate strut | Johnson |
| Pressure vessel wall | $pr/t$ and $pr/2t$, joint efficiency |

## 14. Self-checks before you write the answer

- Units: N and mm give MPa; kN and m give kPa; $E$ in GPa $=10^3$ MPa.
- **Limiting cases:** $E\to\infty$ gives zero deflection; a thin wall gives $\sigma\propto1/t$; $e\to0$ in the secant formula gives Euler.
- **Orders of magnitude:** steel at 150 MPa strains $750\ \mu\varepsilon$; a 1 m steel bar changes length by 0.75 mm.
- **Sum rules:** $\sigma_x+\sigma_y$ is the same on every plane; shear flow into a joint equals the flow out; reactions satisfy $\sum F=\sum M=0$.
- Never use $\sigma=P/A$ at a point load, and never use the beam formulas within one depth of it (Saint-Venant).

## Related
[[Stress-Strain Transformation Analogy]] (the mnemonic that ties §1, §7 and the strain formulas together) · [[Second Moments of Area - One Integral, Many Jobs]] · [[Energy Methods - A Unified View]] · [[Fluid Mechanics/10 Viscous Flow and Exact Solutions/Viscous Flow and Exact Solutions - Formula Bank|the fluid-mechanics bank]] for the same layout.
