---
title: Question Bank 4 – Deflection, Energy and Columns
tags: [strength-of-materials, question-bank, tutorial]
up: "[[Strength of Materials - Question Bank]]"
aliases: [SoM question bank 4, beam deflection problems, Castigliano problems, buckling problems]
---

# Question Bank 4 — Deflection, Energy and Columns

Part of [[Strength of Materials - Question Bank]] · formulas: [[Strength of Materials - Formula Bank]] (§8–§10) · theory: [[Double Integration and Macaulay's Method]], [[Moment-Area Method]], [[Strain Energy and Castigliano's Theorem]], [[Euler Buckling of Columns]]

> [!abstract] What is here
> Twelve conceptual questions and ten numerical problems (Q1–Q10): standard deflections, moment-area, an overhang, a propped cantilever, Macaulay with two loads, a Castigliano frame, impact, Euler and Johnson columns and the secant formula. Numbers from `Tools/sm_bank_core.py` (`p4_n1` … `p4_n10`); deflections were also checked by numerical double integration.

## Part A — Conceptual questions

> [!question]- A1. Which boundary conditions does the double-integration method need, and how many constants are there?
> Two constants per segment. Pinned or roller support: $v=0$. Fixed end: $v=0$ and $\theta=0$. Free end: $M=0$ and $V=0$ (no condition on $v$). At a junction between segments, $v$ and $\theta$ are continuous. Macaulay's method removes the junction conditions and leaves only the two end conditions.

> [!question]- A2. What is the rule for Macaulay's brackets?
> Write $M$ using terms $\langle x-a\rangle^n$ that are zero for $x<a$. Integrate each term as a whole (the bracket is carried through the integration). A UDL that stops before the end is extended to the end and cancelled by an opposite UDL starting at the stopping point. One equation then covers the whole beam.

> [!question]- A3. State the two moment-area theorems.
> (1) The change in slope between $A$ and $B$ equals the area of the $M/EI$ diagram between them. (2) The vertical deviation of $B$ from the tangent at $A$ equals the moment of that area about $B$. Positive $M$ makes the beam sag, and the areas are signed.

> [!question]- A4. When can deflections be superposed?
> When the material is linear elastic and the deflections are small, so that the equations are linear in the loads and the geometry does not change appreciably. It fails for large deflections, for buckling (the axial load changes the stiffness) and for materials that yield.

> [!question]- A5. State Maxwell's reciprocal theorem and one use.
> The deflection at $A$ due to a unit load at $B$ equals the deflection at $B$ due to a unit load at $A$ ($\delta_{AB}=\delta_{BA}$). Use: measure the deflection curve of a beam by moving a dial gauge instead of the load (the three-point-bending lab moves the load to $L/4$ and $3L/4$ and the readings reciprocate).

> [!question]- A6. Why can't strain energies of two loads simply be added?
> $U$ is quadratic in the loads, so $U(P_1+P_2)=U_1+U_2+\text{cross term}$. Only for loads that do no work on each other's deflections (e.g. axial and bending in a straight beam, or loads in orthogonal planes) does it separate. For a single load, $U=\frac12P\delta$ gives $\delta$ directly but only at the load point and in the load direction.

> [!question]- A7. How does Castigliano's second theorem give a deflection at a point where there is no load?
> Place a fictitious (dummy) load $Q$ at that point and in the wanted direction, write $M$ (and $T$, $N$) including $Q$, differentiate $U$ with respect to $Q$, and then set $Q=0$. Since $\partial M/\partial Q$ is needed before $Q$ is set to zero, only the derivative is carried, which is the moment due to a unit load there.

> [!question]- A8. What is the impact factor?
> $n=\delta_{max}/\delta_{st}$, the ratio of the dynamic to the static deflection (and stress) for the same weight. A weight dropped from $h$ gives $n=1+\sqrt{1+2h/\delta_{st}}$; a suddenly applied load ($h=0$) gives $n=2$. A softer structure (large $\delta_{st}$) has a smaller $n$, which is why shock absorbers are compliant.

> [!question]- A9. List the assumptions of Euler's column theory.
> Perfectly straight, homogeneous and linearly elastic column; load exactly axial and through the centroid; ideal end conditions; small deflections ($1/\rho\approx v''$); no residual stress or initial crookedness; and $\sigma_{cr}$ below the proportional limit. Real columns fail below the Euler load because none of these holds exactly.

> [!question]- A10. What is effective length, and why is $K=0.5$ for a fixed–fixed column?
> $L_e=KL$ is the length of the equivalent pin-ended column, i.e. the distance between inflection points of the buckled shape. A fixed–fixed column buckles in a full sine wave with two inflection points at $L/4$ and $3L/4$, so the middle half behaves like a pin-ended column of length $L/2$.

> [!question]- A11. Why does Euler's formula fail for short columns, and what replaces it?
> Euler gives $\sigma_{cr}=\pi^2E/\lambda^2$, which exceeds the yield stress for small $\lambda$, which is impossible. For $\lambda<\lambda_c=\pi\sqrt{2E/\sigma_Y}$ the column yields before it buckles elastically, and a parabola (Johnson) or a straight line joins the yield cut-off to the Euler curve at $\sigma_Y/2$.

> [!question]- A12. Will using a higher-strength steel raise the buckling load of a slender column?
> No. $P_{cr}=\pi^2EI/(KL)^2$ contains $E$ and $I$ only, and all steels have $E\approx200$ GPa. Strength matters only for short and intermediate columns. To raise $P_{cr}$: increase $I$ (tube instead of bar), shorten $L$, brace the middle or restrain the ends.

## Q1 — Simply supported beam, UDL (easy)

A simply supported beam of span 5 m, $EI=16\,000$ kN·m² ($E=200$ GPa, $I=80\times10^6$ mm⁴), carries a UDL of 12 kN/m. Find the central deflection and the end slope, and compare with $L/360$.

> [!tip]- Hint
> $M=\dfrac{wLx}{2}-\dfrac{wx^2}{2}$, integrate twice with $v(0)=v(L)=0$, or use the standard result.

> [!success]- Solution
> Take $v$ upward, so $EIv''=M=\dfrac w2(Lx-x^2)$. Integrate twice and use $v(0)=v(L)=0$:
> $EIv=\dfrac{w}{24}\big(2Lx^3-x^4-L^3x\big)$. At $x=L/2$ this is $v=-\dfrac{5wL^4}{384EI}$ (downward), and the end slope has magnitude $\dfrac{wL^3}{24EI}$.
> $y_{max}=\dfrac{5(12)(5)^4}{384(16\,000)}=\mathbf{6.10}$ mm, $\theta=\dfrac{12(125)}{24(16\,000)}=3.91\times10^{-3}$ rad $=\mathbf{0.224^\circ}$.
> $L/y_{max}=819$, comfortably within the $L/360$ limit (13.9 mm).

## Q2 — Cantilever with a load at mid-span (moment-area) (easy–medium)

A cantilever of length 3 m, $EI=12\,000$ kN·m², carries 10 kN at mid-span. Find the slope and deflection at the free end.

> [!tip]- Hint
> Beyond the load the cantilever is unloaded and straight. Slope at the load, then deflection there, then add the straight run.

> [!success]- Solution
> With $a=1.5$ m: $\theta_a=\dfrac{Pa^2}{2EI}=\dfrac{10(2.25)}{2(12\,000)}=9.375\times10^{-4}$ rad. This slope is the slope at the tip too.
> $y_a=\dfrac{Pa^3}{3EI}=0.9375$ mm. Tip: $y_{tip}=y_a+\theta_a(L-a)=0.9375+1.406=\mathbf{2.34}$ mm.
> Closed form $\dfrac{5PL^3}{48EI}=2.34$ mm ✓. Moment-area: the area of $M/EI$ is the triangle $\tfrac12\cdot\dfrac{Pa}{EI}\cdot a$; its moment about the tip, with centroid $a/3$ from the load plus $a$, gives the same.

## Q3 — Overhanging beam, tip deflection (medium)

A beam $ABC$ of span $AB=4$ m rests on supports at $A$ and $B$ and overhangs to $C$ by 1.5 m. A 20 kN load acts at $C$. $EI=12\,000$ kN·m². Find the deflection at $C$ and at mid-span.

> [!tip]- Hint
> Treat the overhang as a cantilever of length $a$ on a rotating support. The moment $M_0=Pa$ at $B$ bends the span, so the span rises.

> [!success]- Solution
> $M_0=20(1.5)=30$ kN·m. Span $AB$ under an end moment: $\theta_B=\dfrac{M_0L}{3EI}=\dfrac{30(4)}{3(12\,000)}=3.33\times10^{-3}$ rad.
> Tip: $y_C=\theta_Ba+\dfrac{Pa^3}{3EI}=5.00+1.875=\mathbf{6.88}$ mm down.
> Mid-span: $y=-\dfrac{M_0L^2}{16EI}=\mathbf{-2.50}$ mm, i.e. the span moves **up** 2.5 mm.
> Numerical integration of $EIv''=M$ gives $6.876$ mm and $-2.500$ mm ✓.

## Q4 — Propped cantilever with a UDL (medium–hard)

A cantilever of length 6 m, fixed at $A$, carries 15 kN/m and is propped at the free end $B$ (rigid prop). Find the reactions, the maximum positive bending moment and its location, the point of contraflexion, and where the deflection is largest.

> [!tip]- Hint
> One redundant: remove the prop and demand that its deflection from the UDL, $wL^4/8EI$, equals that from $R_B$, $R_BL^3/3EI$.

> [!success]- Solution
> $\dfrac{R_BL^3}{3EI}=\dfrac{wL^4}{8EI}$ gives $R_B=\dfrac{3wL}{8}=\mathbf{33.75}$ kN, $R_A=90-33.75=\mathbf{56.25}$ kN, $M_A=\dfrac{wL^2}{8}=\mathbf{67.5}$ kN·m (hogging).
> $M(x)=-67.5+56.25x-7.5x^2$ from $A$: zero at $x=\mathbf{1.5}$ m $(=L/4)$, the point of contraflexion.
> $V=0$ at $x=3.75$ m from $A$ ($=5L/8$): $M_{max}^+=\dfrac{9wL^2}{128}=\mathbf{37.97}$ kN·m.
> Largest deflection where $\theta=0$: $x=0.5785L=\mathbf{3.47}$ m from the wall (checked by integration: 3.471 m), with $y_{max}\approx wL^4/185EI$.
> **Check:** the propped cantilever is statically indeterminate to the first degree: the moment at the wall is 2.25 times the maximum span moment, so design for the hogging moment at $A$.

## Q5 — Macaulay's method with two loads (medium–hard)

![[SM-QB-4-curves.png]]

A simply supported beam of span 8 m carries a 30 kN point load at 3 m from $A$ and a UDL of 10 kN/m from 5 m to 8 m. $EI=40\,000$ kN·m². Find the reactions, the deflection at 4 m and the position and size of the maximum deflection.

> [!tip]- Hint
> $M=R_Ax-30\langle x-3\rangle-5\langle x-5\rangle^2$. Integrate twice, $v(0)=0$ gives $C_2=0$, $v(8)=0$ gives $C_1$.

> [!success]- Solution
> $R_B=\dfrac{30(3)+30(6.5)}{8}=\mathbf{35.625}$ kN, $R_A=\mathbf{24.375}$ kN.
> With $v$ upward, $EIv''=M$, so $EIv=\dfrac{R_Ax^3}{6}-5\langle x-3\rangle^3-\dfrac{5}{12}\langle x-5\rangle^4+C_1x$ (and $C_2=0$ from $v(0)=0$).
> $v(8)=0$ gives $C_1=-177.66$ kN·m². Slope at $A$: $C_1/EI=-4.44\times10^{-3}$ rad (the beam leaves $A$ sloping downward).
> At 4 m: $v=-11.39$ mm, i.e. **11.39 mm downward**. The slope is zero at $x=\mathbf{3.97}$ m, where the maximum deflection is $\mathbf{11.39}$ mm (essentially the same as at 4 m, because the maximum is so flat).
> **Check:** a numerical double integration of $M(x)/EI$ gives $11.391$ mm at 4 m and a maximum of $11.392$ mm ✓.

## Q6 — Castigliano on an L-shaped frame (medium)

A frame has a vertical column of height $h=2$ m fixed at the base and a horizontal arm of length $a=1.5$ m. A load $P=5$ kN acts vertically downward at the free end of the arm. $EI=8000$ kN·m² throughout. Find the vertical deflection of the load point (bending only).

> [!tip]- Hint
> Write $M$ in each member in terms of $P$, then $\delta=\partial U/\partial P=\sum\int\dfrac M{EI}\dfrac{\partial M}{\partial P}dx$.

> [!success]- Solution
> Arm (from the tip): $M=Px$, $\partial M/\partial P=x$. Column: $M=Pa$ (constant), $\partial M/\partial P=a$.
> $\delta=\dfrac1{EI}\Big[\int_0^aPx^2dx+\int_0^hPa^2dy\Big]=\dfrac{Pa^3}{3EI}+\dfrac{Pa^2h}{EI}$.
> $=\dfrac{5(3.375)}{3(8000)}+\dfrac{5(2.25)(2)}{8000}=0.703+2.813=\mathbf{3.52}$ mm.
> The column contributes four times the arm: the column rotates by $Pah/EI$ and the arm lever amplifies it.
> **Neglected:** axial energy in the column, $Ph/AE$, which is about $10^{-3}$ of the total for a slender section.

## Q7 — Impact on a beam (medium)

A mass of 20 kg falls 100 mm onto the middle of a simply supported steel beam, 40 mm square and 1 m long ($E=200$ GPa), striking it from rest. Find the maximum deflection and stress, and compare with the static values. Neglect the beam's mass.

> [!tip]- Hint
> $k=48EI/L^3$, $\delta_{st}=W/k$, then $\delta_{max}=\delta_{st}\big(1+\sqrt{1+2h/\delta_{st}}\big)$. Stress follows from the equivalent static force $k\delta_{max}$.

> [!success]- Solution
> $I=40^4/12=2.133\times10^5$ mm⁴, $S=40^3/6=10\,667$ mm³, $k=\dfrac{48(200\,000)(2.133\times10^5)}{1000^3}=2048$ N/mm. $W=196.2$ N.
> $\delta_{st}=0.0958$ mm. $\delta_{max}=0.0958\Big(1+\sqrt{1+\dfrac{2(100)}{0.0958}}\Big)=\mathbf{4.47}$ mm, an impact factor $n=\mathbf{46.7}$.
> $F=k\delta_{max}=9.16$ kN, $M=FL/4=2.29$ kN·m, $\sigma=\dfrac{2.29\times10^6}{10\,667}=\mathbf{215}$ MPa (static: 4.6 MPa).
> Energy check: $W(h+\delta)=\tfrac12k\delta^2$ gives $\delta=4.474$ mm ✓.
> **Insight:** a 20 kg mass that is harmless when set down gently stresses the bar to 86 % of yield when dropped 10 cm. A softer beam (smaller $k$) lowers $n$ and the stress.

## Q8 — Euler or not? A tube with four end conditions (medium–hard)

A steel tube, 60 mm outside diameter and 4 mm wall, is 3 m long ($E=200$ GPa, $\sigma_Y=250$ MPa). Find the critical load for pinned–pinned, fixed–pinned, fixed–fixed and fixed–free ends, using the correct formula in each case, and the allowable load with $FS=2.5$.

> [!tip]- Hint
> Compute $r$ and $\lambda=KL/r$ first. Euler holds only if $\lambda\ge\lambda_c=\pi\sqrt{2E/\sigma_Y}$.

> [!success]- Solution
> $A=703.7$ mm², $I=2.773\times10^5$ mm⁴, $r=19.85$ mm, $\lambda_c=125.7$, yield load $\sigma_YA=175.9$ kN.
>
> | Ends | $K$ | $\lambda$ | Euler $P_{cr}$ (kN) | Governing formula | $P_{cr}$ (kN) | $P_{all}$ (kN) |
> |---|---|---|---|---|---|---|
> | pinned–pinned | 1 | 151 | 60.8 | Euler ($\lambda>\lambda_c$) | **60.8** | 24.3 |
> | fixed–pinned | 0.70 | 106 | 124.5 | Johnson | **113.8** | 45.5 |
> | fixed–fixed | 0.5 | 75.6 | 243.2 | Johnson | **144.1** | 57.6 |
> | fixed–free | 2 | 302 | 15.2 | Euler | **15.2** | 6.1 |
>
> Euler would over-estimate the fixed–fixed column by **69 %**: its $\sigma_{cr}=346$ MPa is above the yield stress. Johnson gives $\sigma_{cr}=250[1-250(75.6)^2/(4\pi^2\cdot200\,000)]=204.8$ MPa.
> **Lesson:** clamping the ends raises the load by about 2.4 (not 4) because the column becomes intermediate, and slenderness, not the end condition alone, decides the formula.

## Q9 — Euler, Johnson and Rankine compared (medium)

A steel column ($E=200$ GPa, $\sigma_Y=250$ MPa) has radius of gyration $r=20$ mm. Find the critical stress for effective lengths 1.2, 1.6, 2.4 and 4.0 m using Euler and Johnson (and Rankine with $\sigma_c=330$ MPa, $a=1/7500$), and say which governs.

> [!tip]- Hint
> $\lambda=L_e/r$, with transition at $\lambda_c=125.7$.

> [!success]- Solution
> | $L_e$ (m) | $\lambda$ | Euler (MPa) | Johnson (MPa) | Rankine (MPa) | governs |
> |---|---|---|---|---|---|
> | 1.2 | 60 | 548 | **221.5** | 223.0 | Johnson |
> | 1.6 | 80 | 308 | **199.3** | 178.1 | Johnson |
> | 2.4 | 120 | 137 | **136.0** | 113.0 | Johnson |
> | 4.0 | 200 | **49.3** | (negative: invalid) | 52.1 | Euler |
>
> At $\lambda_c$ the two curves meet at $\sigma_Y/2=125$ MPa with equal slope. Rankine is a single empirical formula that is *safe* (lower) in the intermediate range and approaches Euler at large $\lambda$; its constants are material-specific.
> **Lesson:** never apply Euler without checking $\lambda$ first. At $\lambda=60$ the Euler value is $2.5\times$ the true capacity.

## Q10 — Eccentric column: the secant formula (hard)

A pinned–pinned steel column of length 2.4 m has a $100\times60$ mm section and carries a load at an eccentricity $e=6$ mm in the 60 mm direction (bending about the weak axis). $E=200$ GPa, $\sigma_Y=250$ MPa. Find the load at which the maximum stress reaches yield, and compare with the Euler load and with a linear estimate.

> [!tip]- Hint
> $\sigma_{max}=\dfrac PA\Big[1+\dfrac{ec}{r^2}\sec\Big(\dfrac L{2r}\sqrt{\dfrac P{EA}}\Big)\Big]$; solve numerically for $\sigma_{max}=\sigma_Y$.

> [!success]- Solution
> $A=6000$ mm², $I=1.8\times10^6$ mm⁴, $r^2=300$ mm², $c=30$ mm, $ec/r^2=0.6$, $\lambda=138.6$, $P_E=\dfrac{\pi^2EI}{L^2}=\mathbf{616.9}$ kN.
> Solving $\sigma_{max}(P)=250$ MPa gives $P=\mathbf{437}$ kN.
> Linear estimate ignoring the extra moment $Pv$: $P=\dfrac{\sigma_YA}{1+ec/r^2}=937.5$ kN: **more than twice too high**. Yield load without eccentricity: 1500 kN.
> At half that load ($218$ kN) $\sigma_{max}=73$ MPa; doubling the load more than triples the stress, because the deflection grows as $P\to P_E$.
> **Lesson:** for eccentric columns the allowable load is set by yielding well below $P_E$, and the stress grows faster than the load, so apply the factor of safety to the **load**, not to the stress.

## Cross-links
Tutorial versions: [[Tutorial 8 - Deflection of Beams|Tutorial 8]], [[Tutorial 9 - Columns|Tutorial 9]] · lab: [[Lab - Deflection of Beams (Three-Point Bending)]], [[Lab - Buckling of Struts]] · before: [[Question Bank 3 - Stress Transformation and Pressure Vessels]]
