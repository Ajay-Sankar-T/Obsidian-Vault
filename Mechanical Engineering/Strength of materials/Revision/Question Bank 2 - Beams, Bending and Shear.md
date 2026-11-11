---
title: Question Bank 2 – Beams, Bending and Shear
tags: [strength-of-materials, question-bank, tutorial]
up: "[[Strength of Materials - Question Bank]]"
aliases: [SoM question bank 2, beam practice problems, bending stress problems]
---

# Question Bank 2 — Beams, Bending and Shear

Part of [[Strength of Materials - Question Bank]] · formulas: [[Strength of Materials - Formula Bank]] (§4–§6) · theory: [[Shear Force and Bending Moment Diagrams]], [[Relations Between Load, Shear, and Moment]], [[Flexure Formula]], [[Unsymmetric and Combined Bending]], [[Shear Stress Formula for Beams]]

> [!abstract] What is here
> Twelve conceptual questions and nine numerical problems (Q1–Q9): diagrams, flexure in a T-section and a composite beam, shear in an I-section, nail spacing, inclined loads, eccentric loading and a sizing problem. Numbers from `Tools/sm_bank_core.py` (`p2_n1` … `p2_n9`).

## Part A — Conceptual questions

> [!question]- A1. State the differential relations between $w$, $V$ and $M$ and what each tells you about the diagrams.
> $dV/dx=-w$ and $dM/dx=V$. The slope of the shear diagram is minus the load intensity; the slope of the moment diagram is the shear. A point load makes $V$ jump by $-P$ and gives $M$ a kink; a UDL makes $V$ linear and $M$ parabolic; $M$ is stationary where $V=0$; and the change in $M$ between two sections is the area under the $V$ diagram.

> [!question]- A2. What is a point of contraflexion and why does the designer care?
> A section where $M$ changes sign (the beam changes curvature from sagging to hogging). The bending moment there is zero, so the beam is not stressed in bending; reinforcement or splices can change there, and the deflected shape has an inflection. In an overhanging beam it lies in the span between the supports when the overhang loading is large enough.

> [!question]- A3. List the assumptions of the flexure formula.
> Straight prismatic beam with a symmetric section (or loads in a principal plane); plane sections remain plane and perpendicular to the axis (Euler–Bernoulli); linear elastic, same $E$ in tension and compression; small deflections; pure bending, or slender enough that shear can be neglected ($L/h>10$); load not close to the section (Saint-Venant).

> [!question]- A4. Why does the neutral axis pass through the centroid?
> No net axial force: $\int\sigma\,dA=-\frac{E}{\rho}\int y\,dA=0$, so the first moment of area about the neutral axis vanishes, which is the definition of the centroid. For a composite or bimodular beam the stress is not proportional to $y$ alone, so the axis moves: $\sum E_i\int_{A_i}y\,dA=0$.

> [!question]- A5. What is the section modulus, and why is an I-beam better than a rectangle of the same area?
> $S=I/c$, the strength of the section in bending: $M_{allow}=\sigma_{all}S$. An I-section puts most of the area far from the neutral axis, where the stress is highest, so $I$ and $S$ are much larger for the same area (and weight). The thin web does little in bending but carries the shear.

> [!question]- A6. Where is the bending stress largest and where is the shear stress largest in a rectangular beam?
> Bending: at the top and bottom fibres, zero on the neutral axis. Shear: at the neutral axis, $\tau_{max}=1.5V/A$, parabolic to zero at the free surfaces. So the points of worst bending and worst shear are different, and each must be checked.

> [!question]- A7. What is shear flow, and how is it used to space nails or bolts?
> $q=VQ/I$ is the horizontal shear force per unit length at a given level, with $Q$ the first moment of the area beyond that level. A fastener line must resist $q$ over its pitch: $s=nF/q$ for $n$ fasteners per cross-section of capacity $F$ each. Choose the level of the joint when you compute $Q$.

> [!question]- A8. How is a beam of two materials analysed?
> By the transformed section: convert the second material into an equivalent width $nb$ of the first, with $n=E_2/E_1$ (the stiffer material becomes wider). Find the centroid and $I$ of the transformed section; compute $\sigma$ in material 1 as $My/I_{tr}$ and in material 2 as $nMy/I_{tr}$. Strain is continuous across the interface, stress jumps by $n$.

> [!question]- A9. For unsymmetric bending (inclined load), where is the neutral axis relative to the load direction?
> It is **not** perpendicular to the load unless $I_y=I_z$. The neutral axis makes an angle with the principal axis with $\tan\alpha=(I_z/I_y)\tan\theta$, so it turns toward the weak axis: a small inclination of the load produces a large inclination of the neutral axis and a large increase in the peak stress.

> [!question]- A10. What is the kern of a section? State it for a rectangle and a circle.
> The region within which an axial load can be applied without causing tension anywhere in the section. Rectangle $b\times h$: the rhombus with half-diagonals $h/6$ and $b/6$ (the middle third). Circle of diameter $d$: radius $d/8$. It matters for masonry, brick and concrete columns and for bolted flanges, which carry no tension.

> [!question]- A11. What is a beam of uniform strength?
> A beam whose section is changed so that $\sigma_{max}=M(x)/S(x)$ is the same at every section. Examples: the leaf spring, a cantilever with a depth varying as $\sqrt x$, a diving-board taper. It uses the least material for a given moment diagram, but is harder to make.

> [!question]- A12. When can shear deformation or shear stress in a beam not be neglected?
> For short, deep beams ($L/h<5$ to $10$), thin-walled sections and wood or composites with a low $G$. Shear then adds to the deflection (roughly $E/\kappa G\,(h/L)^2$ of the bending deflection, below 1 % for slender steel beams) and the web may govern the design. For a slender solid beam bending governs by a wide margin.

## Q1 — Simply supported beam, UDL plus a point load (easy)

![[SM-QB-2a-sfd-bmd.png]]

A simply supported beam of span 8 m carries a UDL of 10 kN/m over the whole span and a point load of 20 kN at 3 m from the left support $A$. Find the reactions, draw the shear-force and bending-moment diagrams, and find the maximum bending moment and where it occurs.

> [!tip]- Hint
> Reactions by moments about $A$. The maximum moment is where $V=0$, which is **not** under the point load in general: it is in the segment where $V$ changes sign.

> [!success]- Solution
> $R_B=\dfrac{80(4)+20(3)}{8}=\mathbf{47.5}$ kN, $R_A=100-47.5=\mathbf{52.5}$ kN.
> $V(x)=52.5-10x$ for $x<3$: $52.5\to22.5$ kN at the load; then $2.5-10(x-3)$: $V$ jumps down by 20 to $2.5$ kN just right of the load and falls to $-47.5$ kN at $B$.
> $V=0$ at $x=\dfrac{52.5-20}{10}=\mathbf{3.25}$ m.
> $M(3)=52.5(3)-10(3)^2/2=112.5$ kN·m; $M_{max}=M(3.25)=52.5(3.25)-20(0.25)-5(3.25)^2=\mathbf{112.8}$ kN·m.
> **Check:** the area of the shear diagram from 0 to 3.25 m is $112.8$ ✓, and $M(8)=0$ ✓.

## Q2 — Overhanging beam: contraflexion (medium)

![[SM-QB-2b-overhang.png]]

A beam $ADC$ rests on supports at $A$ and $C$ (6 m apart) and overhangs 2 m beyond $C$ to $D$. A UDL of 12 kN/m acts on $AC$ and a 18 kN point load acts downward at $D$. Find the reactions, the maximum positive and negative moments, and the point of contraflexion.

> [!tip]- Hint
> Moments about $A$ for $R_C$. Contraflexion is where $M=0$ between the supports; use $M(x)=R_Ax-wx^2/2$.

> [!success]- Solution
> $R_C=\dfrac{12(6)(3)+18(8)}{6}=\mathbf{60}$ kN, $R_A=72+18-60=\mathbf{30}$ kN.
> Span: $V=30-12x$, zero at $x=2.5$ m, $M_{max}^+=30(2.5)-6(2.5)^2=\mathbf{37.5}$ kN·m.
> At $C$: $V$ jumps from $-42$ to $+18$ kN, and $M_C=-18(2)=\mathbf{-36}$ kN·m (the largest negative moment).
> Contraflexion: $30x-6x^2=0$ gives $x=\mathbf{5}$ m from $A$.
> **Check:** the area of $V$ over $CD$ is $18\times2=36$ ✓ (going from $M=-36$ to $0$). Both signs of moment occur, so the beam needs strength on **both** faces at different places.

## Q3 — T-section in cast iron: which way up? (medium)

![[SM-QB-2c-sections.png]]

A T-beam has a flange $120\times20$ mm on top of a web $20\times100$ mm (overall depth 120 mm). (a) Find the neutral axis and $I$. (b) For a sagging moment of 8 kN·m, find the extreme stresses. (c) If it is cast iron with allowable stresses 30 MPa in tension and 90 MPa in compression, find the largest sagging moment for the section upright and for it inverted.

> [!tip]- Hint
> $\bar y$ from the bottom, then $I$ by parallel axes. Sagging puts the top in compression. For cast iron, put the **long** side of the section (large $c$) on the **compression** side.

> [!success]- Solution
> $A=2400+2000=4400$ mm². $\bar y=\dfrac{2400(110)+2000(50)}{4400}=\mathbf{82.7}$ mm from the bottom.
> $I=\dfrac{120(20)^3}{12}+2400(27.3)^2+\dfrac{20(100)^3}{12}+2000(32.7)^2=\mathbf{5.674\times10^6}$ mm⁴.
> Top fibre ($c=37.3$ mm): $\sigma=-\dfrac{8\times10^6(37.3)}{5.674\times10^6}=\mathbf{-52.6}$ MPa (C). Bottom fibre ($c=82.7$ mm): $\sigma=\mathbf{+116.6}$ MPa (T).
> Upright: tension at the bottom, $M\le30I/82.7=2.06$ kN·m; compression limit $90I/37.3=13.7$ kN·m. **Tension governs: 2.06 kN·m.**
> Inverted: tension at the top ($c=37.3$): $M\le30I/37.3=4.57$ kN·m; compression at the bottom: $90I/82.7=6.17$ kN·m. **Governs: 4.57 kN·m.**
> Inverting the section more than **doubles** the capacity (factor 2.2): the long web is in compression, where cast iron is strong.

## Q4 — Shear stress in an I-section (medium)

A built-up I-section has flanges $100\times12$ mm and a web $10\times150$ mm (overall depth 174 mm). It carries $V=60$ kN. Find $\tau$ at the neutral axis, at the top of the web and just inside the flange, and the fraction of $V$ carried by the web.

> [!tip]- Hint
> $Q$ is the first moment of the area **above** the level considered. At the flange–web junction $Q$ is just the flange. The jump in $\tau$ between web and flange is the thickness ratio.

> [!success]- Solution
> $I=\dfrac{10(150)^3}{12}+2\Big[\dfrac{100(12)^3}{12}+100(12)(81)^2\Big]=\mathbf{1.859\times10^7}$ mm⁴.
> Flange: $Q_f=100(12)(81)=97\,200$ mm³. At the neutral axis: $Q=97\,200+10(75)(37.5)=125\,325$ mm³.
> $\tau_{NA}=\dfrac{60\,000(125\,325)}{1.859\times10^7(10)}=\mathbf{40.5}$ MPa.
> Top of web: $\tau=\dfrac{60\,000(97\,200)}{1.859\times10^7(10)}=\mathbf{31.4}$ MPa; just inside the flange: $\tau=31.4\times\dfrac{10}{100}=\mathbf{3.14}$ MPa.
> Integrating $\tau$ over the web: $V_{web}=56.1$ kN $=\mathbf{93.6}$ % of $V$. The simple estimate $V/(t_wh_w)=40.0$ MPa is within 1 % of the true peak.
> **Use:** design the web for $V/(t_wh_w)$ and the flanges for $M/S$.

## Q5 — Wood beam with a steel plate: transformed section (hard)

A wooden beam $100\times200$ mm ($E_w$) has a $100\times10$ mm steel plate attached to its underside ($E_s=20E_w$). It carries a sagging moment of 12 kN·m. Find the stresses at the top of the wood, at the wood–steel interface in each material, and at the bottom of the steel. Compare with the wood alone.

> [!tip]- Hint
> Transform the steel into wood: width $20\times100=2000$ mm, thickness 10 mm. Find the new centroid, $I_{tr}$, then multiply the steel stress by $n=20$.

> [!success]- Solution
> Transformed areas: wood $20\,000$ mm² at 110 mm above the bottom; steel $20\,000$ mm² at 5 mm. $\bar y=\dfrac{20\,000(110)+20\,000(5)}{40\,000}=\mathbf{57.5}$ mm above the bottom: the neutral axis is **inside the wood**, 47.5 mm above the interface.
> $I_{tr}=\dfrac{100(200)^3}{12}+20\,000(52.5)^2+\dfrac{2000(10)^3}{12}+20\,000(52.5)^2=\mathbf{1.771\times10^8}$ mm⁴.
> Wood top ($y=152.5$): $\sigma=-\dfrac{12\times10^6(152.5)}{1.771\times10^8}=\mathbf{-10.3}$ MPa (C).
> Wood at the interface ($y=47.5$): $+3.2$ MPa (T). Steel at the interface: $20\times3.2=\mathbf{64.4}$ MPa. Steel bottom ($y=57.5$): $20\times\dfrac{12\times10^6(57.5)}{1.771\times10^8}=20\times3.90=\mathbf{77.9}$ MPa (T).
> Wood alone: $\sigma=\dfrac{12\times10^6(100)}{6.667\times10^7}=18.0$ MPa. The plate cuts the peak wood stress by **43 %**.
> **Trap:** using the wood centroid (at 100 mm) ignores the plate; always recompute the neutral axis.

## Q6 — Nailed T-beam (medium)

A T-beam is made of two $150\times25$ mm planks: one flat (flange) nailed to the edge of the other (web, 150 mm deep). The shear force is 3 kN and each nail carries 700 N in shear. Find the nail spacing along the beam with one nail per cross-section and with two.

> [!tip]- Hint
> The nails sit at the joint. $Q$ is the first moment of the **flange** about the neutral axis of the whole section.

> [!success]- Solution
> Flange area $3750$ mm² at $162.5$ mm from the bottom; web $3750$ mm² at 75 mm: $\bar y=\mathbf{118.75}$ mm. $I=\mathbf{2.158\times10^7}$ mm⁴.
> $Q=3750(162.5-118.75)=164\,062$ mm³. $q=\dfrac{VQ}{I}=\dfrac{3000(164\,062)}{2.158\times10^7}=\mathbf{22.8}$ N/mm.
> One nail per section: $s=700/22.8=\mathbf{30.7}$ mm. Two nails: $s=\mathbf{61.4}$ mm.
> **Check:** $q$ is a force per millimetre, so $s=F/q$ comes out in millimetres ✓. Round **down** to the next practical spacing.

## Q7 — Inclined tip load on a cantilever (unsymmetric bending) (medium)

A cantilever of rectangular section 60 mm (width, $z$) $\times$ 120 mm (depth, $y$) is 1.2 m long. A 2 kN load at the free end acts at $20^\circ$ to the vertical. Find the greatest bending stress at the root and the orientation of the neutral axis.

> [!tip]- Hint
> Resolve the load into the two principal planes; the moments are $M_z=P\cos\theta\,L$ and $M_y=P\sin\theta\,L$. The extreme stress is at a corner.

> [!success]- Solution
> $I_z=\dfrac{60(120)^3}{12}=8.64\times10^6$ mm⁴, $I_y=\dfrac{120(60)^3}{12}=2.16\times10^6$ mm⁴.
> $M_z=2000\cos20^\circ(1200)=2.255\times10^6$ N·mm, $M_y=2000\sin20^\circ(1200)=0.821\times10^6$ N·mm.
> Corner: $\sigma=\dfrac{M_z(60)}{I_z}+\dfrac{M_y(30)}{I_y}=15.66+11.40=\mathbf{27.1}$ MPa.
> Vertical load only: $\sigma=\dfrac{2.4\times10^6(60)}{8.64\times10^6}=16.7$ MPa. The $20^\circ$ tilt raises the peak stress by **62 %**.
> Neutral axis: $\tan\alpha=\dfrac{I_z}{I_y}\tan20^\circ=4(0.364)=1.456$, so $\alpha=\mathbf{55.5^\circ}$ from the horizontal axis (it would be $0^\circ$ for a vertical load).
> **Lesson:** a deep, narrow section is very sensitive to side loads. That is why purlins and joists are braced.

## Q8 — Eccentric axial load on a short column (medium)

A short column of $150\times200$ mm section carries 240 kN at $e=40$ mm from the centre along the 200 mm side. Find the extreme stresses and the depth of any tension zone. What is the largest $e$ that avoids tension?

> [!tip]- Hint
> $\sigma=P/A\pm Pe\,c/I$. Compare $e$ with the kern limit $h/6$.

> [!success]- Solution
> $A=30\,000$ mm², $I=150(200)^3/12=10^8$ mm⁴. $P/A=8.0$ MPa; $Pec/I=\dfrac{240\,000(40)(100)}{10^8}=9.6$ MPa.
> $\sigma_{max}=-(8.0+9.6)=\mathbf{-17.6}$ MPa (C); opposite face $=-8.0+9.6=\mathbf{+1.6}$ MPa (T).
> The neutral axis is at $y_0=r^2/e=\dfrac{200^2/12}{40}=83.3$ mm from the centre, so tension occupies $100-83.3=\mathbf{16.7}$ mm of the 200 mm depth.
> Kern: $e\le h/6=\mathbf{33.3}$ mm for no tension (at that $e$ the stress is $-16.0$ and $0$ MPa).
> **Application:** masonry piers, bolt groups and foundations are checked for $e\le h/6$.

## Q9 — Sizing a beam: circle against rectangle (medium)

A simply supported beam of span 6 m carries a central load of 24 kN. The allowable bending stress is 120 MPa. Find the diameter of a solid circular section and the size of a rectangle with $h=2b$. Compare their areas and check the shear stress.

> [!tip]- Hint
> $S_{req}=M_{max}/\sigma_{all}$. For the circle $S=\pi d^3/32$; for $h=2b$: $S=bh^2/6=h^3/12$.

> [!success]- Solution
> $M_{max}=PL/4=36$ kN·m, so $S_{req}=\dfrac{36\times10^6}{120}=\mathbf{3.0\times10^5}$ mm³.
> Circle: $d=(32S/\pi)^{1/3}=\mathbf{145.1}$ mm, $A=16\,539$ mm².
> Rectangle: $h=(12S)^{1/3}=\mathbf{153.3}$ mm, $b=76.6$ mm, $A=11\,745$ mm².
> The circle is **41 %** heavier for the same bending strength.
> Shear ($V=12$ kN): circle $\tau_{max}=\dfrac{4V}{3A}=0.97$ MPa, rectangle $\dfrac{3V}{2A}=1.53$ MPa, a hundred times below any allowable. Bending governs.
> **Note:** the rectangle on edge ($h=2b$) is stiff about the horizontal axis but would buckle sideways if unbraced (lateral-torsional buckling).

## Cross-links
Tutorial versions: [[Tutorial 7 - Bending and Shear Stresses|Tutorial 7]] · before: [[Question Bank 1 - Stress, Axial Loading and Torsion]] · next: [[Question Bank 3 - Stress Transformation and Pressure Vessels]]
