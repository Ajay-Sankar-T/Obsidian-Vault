---
tags: [applied-mechanics-lab, AM2540, exam-prep, tutorial]
up: "[[Applied Mechanics Lab - Mock Papers]]"
aliases: [AM2540 past paper, AML 2023 end semester, Applied Mechanics Lab end sem solutions]
---

# Applied Mechanics Lab — Past Paper Pattern and Model Answers

Part of [[Applied Mechanics Lab - Mock Papers]] · lab MOC: [[Applied Mechanics Lab - MOC]] · formulas: [[Strength of Materials - Formula Bank]] (§12)

> [!abstract] What this is
> The AM2540 end-semester paper of November 2023 (60 marks, 45 minutes, 13 questions, all compulsory), analysed question by question and answered in the length that earns the marks. The questions are **paraphrased** (the original PDF is not reproduced); the numbers are the paper's. The three [[Mock Paper 1 - Strain Gauge, Torsion and Beams|mock]] [[Mock Paper 2 - Tensile Tests, DIC and Buckling|papers]] [[Mock Paper 3 - Bending, Photoelasticity and Instruments|follow this pattern]].

## The pattern

| Q | Topic | Experiment | Marks | Type |
|---|---|---|---|---|
| 1 | strain gauge on a cantilever: temperature compensation, gauge factor | strain gauge | 6 | recall |
| 2 | hollow shaft ($d_i/d_o=0.6$) against a solid shaft of equal strength | torsion | 4 | short numerical |
| 3 | mirror and scale: twist from a 5 mm shift at 50 mm | torsion | 4 | numerical |
| 4 | yield, proportional, elastic, ultimate and fracture points on the stress–strain curve | tensile test | 5 | sketch and define |
| 5 | failure planes of brittle and ductile materials in tension, torsion, three-point bending | tensile, torsion, bending | 6 | sketch and reason |
| 6 | load–displacement and stress–strain curves for specimens of diameter $d$ and $2d$ | tensile test | 4 | reasoning |
| 7 | Euler's assumptions, failure criteria of columns, circle against rectangle of equal perimeter | buckling | 9 | recall and reasoning |
| 8 | disk in diametral compression, $f_\sigma=0.2$ against $8$: fringes? | photoelasticity | 2 | MCQ |
| 9 | definition of polarisation | photoelasticity | 2 | MCQ |
| 10 | circular polariscope, bending beam, fringe order 2, $t=5$ mm, $f_\sigma=8$: stress | photoelasticity | 3 | numerical |
| 11 | steel beam against a half-width brass beam turned $90^\circ$, $E_s=2E_b$: deflection | bending | 5 | reasoning |
| 12 | how to reduce a simply supported beam's deflection without changing $E$, $L$ or load | bending | 5 | reasoning with a formula |
| 13 | overhanging portion: effect on deflection, sketch for $l=0$ and $l\ne0$ | bending | 5 | sketch |

**What the examiner rewards.**
1. **Understanding the experiment, not the manual.** Most questions begin "recall the experiment on…". A one-line statement of the principle, a sketch and the governing equation earn most of the marks.
2. **Ratios, not numbers.** Q2, Q6, Q8, Q11, Q12 are answered by scaling laws ($D^3$, $D^4$, $1/f_\sigma$, $bh^3$). Know the exponent for each formula.
3. **Sketches count.** Q4, Q5, Q6, Q13 each need a labelled figure.
4. **Spread of topics:** gauge/bridge 6, torsion 8, tension 9, columns 9, photoelasticity 7, beams 15, other 6. Beams and photoelasticity were the largest blocks; photoelasticity has no experiment note in the manuals, see [[Lab - Photoelasticity - Fringes and Stress]].
5. **Time:** 45 minutes for 60 marks is 45 seconds per mark. Do the MCQs and the one-line numericals first (13 marks in 8 minutes).

## Model answers

## Q1 — Strain-gauge cantilever (6 marks)

*Single gauge at the root of a cantilever loaded at the free end: (a) what modification makes the result independent of temperature, and why? (b) define the gauge factor.*

> [!success]- Model answer
> **(a)** Put a **second gauge** on the opposite (lower) face and connect the two in **adjacent arms** of the Wheatstone bridge (half bridge); alternatively add an identical **dummy gauge**, unstrained and at the same temperature, in the adjacent arm. A temperature change alters each gauge's resistance by the same $\Delta R_T$; in adjacent arms $V_o\propto\varepsilon_1-\varepsilon_2$ so the thermal parts cancel. The bending strain is $+\varepsilon$ on top and $-\varepsilon$ below, so with the half bridge it **adds**: the output is doubled, $V_o=V_{ex}GF\varepsilon/2$.
> **(b)** $GF=\dfrac{\Delta R/R}{\varepsilon}$: the fractional change of resistance per unit strain, about 2 for foil gauges.
> ![[AML-bridge-configs.png]]
> See [[Lab - Strain Gauge Measurement on a Cantilever Beam]].

## Q2 — Hollow against solid shaft (4 marks)

*$d_i/d_o=0.6$. A solid shaft has the same torsional strength. Find $d_o/d$.*

> [!success]- Model answer
> Same torque and same $\tau_{max}$: $\dfrac{\pi}{16}d^3=\dfrac{\pi}{16}d_o^3(1-k^4)$ with $k=0.6$, $k^4=0.1296$.
> $\dfrac{d_o}{d}=(1-k^4)^{-1/3}=0.8704^{-1/3}=\mathbf{1.047}$.
> The hollow shaft is about 5 % larger in diameter, but its area is $(1-k^2)(d_o/d)^2=0.64\times1.097=0.70$ of the solid shaft's: **30 % lighter** for the same strength.

## Q3 — Mirror and scale (4 marks)

*Use ray optics to find the angle of twist if the reading moves by 5 mm and the scale is 50 mm from the mirror.*

> [!success]- Model answer
> A mirror turned through $\phi$ turns the reflected ray through $2\phi$ (the angle of incidence and of reflection each change by $\phi$). The spot moves by $s$ on a scale at distance $D$: $\tan2\phi=s/D=5/50=0.1$.
> $2\phi=5.71^\circ$, so $\phi=\mathbf{2.86^\circ}=0.0498$ rad. (Small-angle: $\phi\approx s/2D=0.050$ rad.)
> Figure and discussion: [[Lab - Torsion of Circular Shafts]] (mirror and scale).

## Q4 — Points on the stress–strain curve (5 marks)

*Explain yield point, proportional limit, elastic limit, ultimate stress point and breaking point with a diagram.*

> [!success]- Model answer
> ![[SM-FB-1-stress-strain.png]]
> - **Proportional limit (A):** the highest stress for which $\sigma\propto\varepsilon$ (Hooke's law); the slope up to here is $E$.
> - **Elastic limit:** the highest stress from which the material returns to zero strain on unloading; for steel it is only slightly above the proportional limit.
> - **Yield point (B):** the stress at which strain increases without more load (upper and lower yield in mild steel); where there is no plateau, the $0.2\%$ offset stress.
> - **Ultimate stress point (C):** the maximum engineering stress $P_{max}/A_0$; necking starts here.
> - **Fracture or breaking point (D):** the stress at which the specimen separates; on the engineering curve it is lower than the ultimate stress because the area is no longer $A_0$.

## Q5 — Failure planes (6 marks)

*Describe the failure planes of brittle and ductile materials in axial tension, torsion and three-point bending.*

> [!success]- Model answer
> ![[SM-FP-failure-planes.png]]
>
> | Load | Ductile | Brittle |
> |---|---|---|
> | Tension | cup-and-cone: neck, flat core, $45^\circ$ shear lips (max shear) | flat, $90^\circ$ to the axis (max normal stress) |
> | Torsion | transverse (cross-section) plane (max shear) | $45^\circ$ helix (max tensile stress) |
> | 3-point bending | yields and bends; no fracture | crack from the tension face under the load, perpendicular to the axis |
>
> **Reason:** ductile metals are weaker in shear, so they fail where $\tau$ is greatest; brittle materials are weaker in tension and fail normal to $\sigma_1$. Full discussion: [[Failure Planes - Ductile and Brittle Fracture]].

## Q6 — Specimens of diameter $d$ and $2d$ (4 marks)

*Sketch the load–displacement and stress–strain curves for a tensile test on two round specimens of diameters $d$ and $2d$.*

> [!success]- Model answer
> ![[AML-tensile-size-effect.png]]
> The material is the same, so **stress against strain is the same curve** ($E$, $\sigma_Y$, $\sigma_u$ and the elongation are properties of the material). The load is stress times area, so at the same strain the load is **four times** larger for $2d$ ($A\propto d^2$). The extension is $\varepsilon L_0$: with the same gauge length it is the same; with geometrically similar specimens ($L_0\propto d$) it is doubled.

## Q7 — Euler buckling (9 marks)

*(a) Assumptions in Euler's theory. (b) Failure criteria for columns. (c) A rectangular shaft $b\times d$ and a circular shaft of diameter $D$ have equal perimeters; which has the larger critical load for the same length and material?*

> [!success]- Model answer
> **(a)** Column perfectly straight and homogeneous; linear elastic ($\sigma_{cr}$ below the proportional limit); load axial through the centroid; ideal (pinned, fixed or free) ends; small deflections ($v''\approx1/\rho$); no initial stress or crookedness; plane sections remain plane.
> **(b)** Two criteria: **crushing** (the stress $P/A$ reaches the yield or compressive strength, governing short columns) and **buckling** (the load reaches $P_{cr}=\pi^2EI/(KL)^2$, governing slender columns, $\lambda\ge\lambda_c$). Intermediate columns fail by their interaction (Johnson, Rankine), and an eccentric load or an initial crookedness lowers the capacity (secant formula).
> **(c)** $P_{cr}\propto I_{min}$ (same $E$, $L$, ends). Perimeter $p$: circle $D=p/\pi$, $I_c=\dfrac{\pi D^4}{64}=\dfrac{p^4}{64\pi^3}=\dfrac{p^4}{1984}$. Rectangle $2(b+d)=p$ with $b\le d$: $I_{min}=\dfrac{db^3}{12}$, largest for the square $b=d=p/4$: $I=\dfrac{p^4}{3072}$. So the **circle** wins: $1.55\times$ the best rectangle, and $3.9\times$ a $2\!:\!1$ rectangle.
> (If instead the *areas* were equal, the square would win by $\pi/3=1.05$: read which is held constant.)

## Q8–Q9 — Photoelasticity MCQs (2 + 2 marks)

> [!success]- Answers
> **Q8:** **(c) increases.** For a disk, $N=8P/(\pi Df_\sigma)\propto1/f_\sigma$: polyurethane ($f_\sigma=0.2$) has $8/0.2=40$ times as many fringes as polycarbonate ($f_\sigma=8$) at the same load. **Q9:** **(b)**, the process of making the tip of the light vector follow a definite law (e.g. a line or circle); (a) is refraction, (c) diffraction, (d) scattering.

## Q10 — Fringe order to stress (3 marks)

*Rectangular beam in pure bending in a circular polariscope; at point $L$ the fringe order is 2 (rose red to green), $t=5$ mm, $f_\sigma=8$ N/mm/fringe. Normal stress?*

> [!success]- Model answer
> $\sigma_1-\sigma_2=\dfrac{Nf_\sigma}{t}=\dfrac{2(8)}{5}=\mathbf{3.2}$ MPa. In pure bending the state is uniaxial ($\sigma_2=0$), so the normal stress at $L$ is **3.2 MPa**. (Rose red to green is the second tint of passage, $N=2$.)

## Q11 — Steel against brass, turned $90^\circ$ (5 marks)

*Equal dimensions except the brass beam is half the width, and its cross-section is rotated $90^\circ$. Simply supported, point load, $E_s=2E_b$: compare the deflections.*

> [!success]- Model answer
> Steel: width $b$, depth $h$, $EI_s=2E_b\dfrac{bh^3}{12}$. Brass, after turning: width $h$, depth $b/2$, $EI_b=E_b\dfrac{h(b/2)^3}{12}=E_b\dfrac{hb^3}{96}$.
> $\dfrac{\delta_{brass}}{\delta_{steel}}=\dfrac{EI_s}{EI_b}=\dfrac{2bh^3/12}{hb^3/96}=\mathbf{16\Big(\dfrac hb\Big)^2}$.
> For a beam deeper than wide ($h>b$) the brass beam deflects **more than 16 times** as much (e.g. $h=2b$: 64 times); it would only match the steel beam if $h=b/4$. **Conclusion:** the depth enters as $h^3$ and wins over the modulus ($2\times$) and the width ($\tfrac12$): orientation matters far more than material.

## Q12 — Reducing deflection (5 marks)

> [!success]- Model answer
> $\delta=\dfrac{PL^3}{48EI}$ (centre load) and $E$, $L$, $P$ are fixed, so increase $I$ or change the supports.
> - **Deepen the section:** $I=bh^3/12$; doubling $h$ cuts $\delta$ eight-fold; a 25×3 mm strip on edge instead of flat is $(25/3)^2=69$ times stiffer. An I-section puts the same area farther from the neutral axis.
> - **Restrain the ends:** clamping both ends changes the central deflection from $PL^3/48EI$ to $PL^3/192EI$, a quarter.
> - **Add a support** (continuous beam) or move the supports so that overhanging weight relieves the span.
> **Example:** a $20\times10$ mm bar laid flat deflects $4\times$ the same bar on edge ($I$ ratio $(20/10)^2$).

## Q13 — The overhang (5 marks)

*How does the overhanging portion in a beam affect deflection? Sketch the curves for $l=0$ and $l\ne0$ (central point load, supports set in from the ends).*

> [!success]- Model answer
> ![[AML-real-q13-overhang.png]]
> **Weightless overhang** (left): the overhang carries no load, so the bending moment in it is zero and it stays **straight**, continuing along the tangent at the support. The deflection of the span is **identical** to $l=0$; the tips **rise** by $\theta l=\dfrac{PL^2}{16EI}\,l$ (because the supports slope upward outward from the sagging span).
> **Self-weight** (right, exaggerated): the weight $wl$ of each overhang acts as a hogging moment $M_0=wl^2/2$ at the supports, which **reduces** the span deflection by $\dfrac{M_0L^2}{8EI}$; the tips then rise less, or fall, depending on the size of $wl^2$. For a light beam the correction is tiny (see [[Mock Paper 2 - Tensile Tests, DIC and Buckling]], Q13: $0.4\%$). A **loaded** overhang reverses the span's curvature and the central deflection goes upward ([[Mock Paper 1 - Strain Gauge, Torsion and Beams]], Q13).

## Cross-links
Experiments: [[Lab - Deflection of Beams (Three-Point Bending)]], [[Lab - Buckling of Struts]], [[Lab - Torsion of Circular Shafts]], [[Lab - Tensile Test of Mild Steel with DIC]], [[Lab - Strain Gauge Measurement on a Cantilever Beam]], [[Lab - Photoelasticity - Fringes and Stress]]
