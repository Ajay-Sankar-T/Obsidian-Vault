---
tags: [applied-mechanics-lab, AM2540, exam-prep, tutorial]
up: "[[Applied Mechanics Lab - Mock Papers]]"
aliases: [AM2540 mock paper 3, Applied Mechanics Lab mock exam 3]
---

# Mock Paper 3 — Bending, Photoelasticity and Instruments

Part of [[Applied Mechanics Lab - Mock Papers]] · previous: [[Mock Paper 2 - Tensile Tests, DIC and Buckling]] · experiments: [[Lab - Deflection of Beams (Three-Point Bending)]], [[Lab - Photoelasticity - Fringes and Stress]], [[Lab - Strain Gauge Measurement on a Cantilever Beam]]

> [!abstract] Paper details
> **AM2540 Applied Mechanics Lab: mock end-semester paper 3.** Maximum marks 60. Time 45 minutes. All questions are mandatory. Assume a suitable value for any missing data. Marks per question: 6, 4, 4, 5, 6, 4, 9, 2, 2, 3, 5, 5, 5. This paper leans on bending, photoelasticity and the instruments (dial gauge, spring pack, strain gauge). Numbers: `Tools/aml_mock_core.py` (`m3`).

## Q1 — Three-point bending recall (6 marks)

(a) In the three-point-bending experiment why are the dial gauges zeroed *after* the self-weight of the beam has settled? (2)
(b) An aluminium beam, 25 mm wide and 6 mm thick ($E=70$ GPa), spans 400 mm and carries a 2.5 kg mass at mid-span. Find the central deflection, the stiffness, and the maximum bending stress. (3)
(c) Give one reason why the measured deflection could be larger and one why smaller than the theoretical value. (1)

> [!success]- Model answer
> **(a)** The beam already sags under its own weight. The theory ($PL^3/48EI$) gives only the deflection due to the **added** load; zeroing with the self-weight in place removes the self-weight sag and, because the response is linear, the readings then correspond exactly to the added load.
> **(b)** $P=2.5(9.81)=24.5$ N, $I=\dfrac{25(6)^3}{12}=450$ mm⁴. $\delta=\dfrac{PL^3}{48EI}=\dfrac{24.5(400)^3}{48(70\,000)(450)}=\mathbf{1.04}$ mm; stiffness $k=P/\delta=\mathbf{23.6}$ N/mm; $\sigma_{max}=\dfrac{3PL}{2bt^2}=\dfrac{3(24.5)(400)}{2(25)(36)}=\mathbf{16.4}$ MPa (far below yield).
> **(c)** Larger: shear deformation, support settlement, indentation at the load point. Smaller: friction at the supports, an overhang's weight (a hogging moment), or a thickness measured too large ($I\propto t^3$). (Any one of each.)

## Q2 — Shaft from power and speed (4 marks)

A solid steel shaft transmits 5 kW at 1500 rpm. The allowable shear stress is 40 MPa. Find the torque and the minimum diameter. What would the diameter be at 750 rpm?

> [!success]- Model answer
> $T=\dfrac{P}{\omega}=\dfrac{5000(60)}{2\pi(1500)}=\mathbf{31.8}$ N·m. $d=\Big(\dfrac{16T}{\pi\tau}\Big)^{1/3}=\Big(\dfrac{16(31\,830)}{\pi(40)}\Big)^{1/3}=\mathbf{15.9}$ mm, say 16 mm.
> At 750 rpm the torque doubles to $63.7$ N·m, so $d$ rises by $2^{1/3}=1.26$ to $\mathbf{20.1}$ mm: the same power at half the speed needs a shaft 26 % thicker.

## Q3 — Torsion of three materials (4 marks)

Under the same torque, a steel rod of given length and diameter twists $0.86^\circ$. Find the twist of identical rods of brass ($G=38$ GPa) and aluminium ($G=25.5$ GPa) ($G_{steel}=79.6$ GPa). How would the twist change if the length were doubled and the diameter doubled?

> [!success]- Model answer
> $\phi=\dfrac{TL}{GJ}\propto\dfrac1G$. Brass: $0.86\times\dfrac{79.6}{38}=\mathbf{1.80^\circ}$. Aluminium: $0.86\times\dfrac{79.6}{25.5}=\mathbf{2.68^\circ}$.
> Length doubled: $\phi\times2$; diameter doubled: $J\times16$, so $\phi\times\tfrac1{16}$. Both together: $\phi\times\tfrac18$ (twist falls to one eighth).

## Q4 — Poisson's ratio with two gauges (5 marks)

A steel bar ($E=210$ GPa) in tension carries one gauge along the axis and one across it. They read $+500\ \mu\varepsilon$ and $-150\ \mu\varepsilon$. (a) Why are two gauges needed? (1) (b) Find Poisson's ratio and the axial stress. (2) (c) The two gauges are placed in adjacent arms of a bridge. By what factor is the output larger than a quarter bridge with the axial gauge alone? (2)

> [!success]- Model answer
> **(a)** The transverse contraction is $-\nu\times$ the axial strain; reading both gives the ratio, which a single gauge cannot.
> **(b)** $\nu=-\dfrac{\varepsilon_t}{\varepsilon_a}=\dfrac{150}{500}=\mathbf{0.30}$; $\sigma=E\varepsilon_a=210\,000(500\times10^{-6})=\mathbf{105}$ MPa.
> **(c)** In adjacent arms $V_o\propto\varepsilon_1-\varepsilon_2=\varepsilon_a-\varepsilon_t=\varepsilon_a(1+\nu)$: the output is **$1+\nu=1.3$ times** the quarter-bridge value (and temperature cancels).

## Q5 — Resolution of the ES6 tester (6 marks)

The ES6 tester's dial resolves 0.01 mm on a thin specimen section of 31 mm gauge length. (a) What is the smallest strain it can show, and what stress does it correspond to in steel ($E=200$ GPa) and aluminium ($E=70$ GPa)? (3) (b) Compare with the yield stress of mild steel (250 MPa) and say what this means for the elastic part of the steel test. (2) (c) Name one better method. (1)

> [!success]- Model answer
> **(a)** $\varepsilon_{min}=\dfrac{0.01}{31}=3.2\times10^{-4}$. Steel: $\sigma=200\,000(3.2\times10^{-4})=\mathbf{64.5}$ MPa; aluminium: $70\,000(3.2\times10^{-4})=\mathbf{22.6}$ MPa.
> **(b)** One dial division in steel is already $26\%$ of the yield stress, so the elastic region is only **three or four points**; together with the grip and spring play, the apparent modulus will be much lower than 200 GPa. The tester is good for the shape of the curve (yield, hardening, necking) and for PVC, not for the modulus of steel.
> **(c)** An extensometer or digital image correlation ([[Lab - Tensile Test of Mild Steel with DIC]]) measures the strain directly on the specimen.

## Q6 — When is the strut an Euler strut? (4 marks)

A steel strip 25 mm wide and 3 mm thick ($E=210$ GPa, proportional limit 200 MPa) is tested as a pin-ended strut. Below what length does the Euler formula stop applying, and what is the load there? Compare with the Euler load at 400 mm.

> [!success]- Model answer
> $r=t/\sqrt{12}=0.866$ mm. Euler holds for $\lambda\ge\lambda_p=\pi\sqrt{E/\sigma_p}=\pi\sqrt{210\,000/200}=101.8$. So $L_{min}=\lambda_pr=101.8(0.866)=\mathbf{88}$ mm.
> At that length the strip is at its proportional limit: $P=\sigma_pA=200(75)=\mathbf{15}$ kN. At 400 mm: $P_{cr}=\dfrac{\pi^2EI}{L^2}=\mathbf{729}$ N, twenty times smaller. Below 88 mm the strip squashes rather than buckles. See the yield line in the figure of [[Lab - Buckling of Struts]].

## Q7 — Photoelasticity (9 marks)

(a) State the stress-optic law and define the material fringe value. (3)
(b) Distinguish isoclinics from isochromatics. (2)
(c) A polycarbonate disk of diameter 40 mm and thickness 6 mm ($f_\sigma=8$ N/mm per fringe) is loaded diametrically by 600 N. How many fringes are there at the centre? (2)
(d) What happens to this number if the load is doubled, and if the disk is made of polyurethane ($f_\sigma=0.2$)? (2)

> [!success]- Model answer
> **(a)** Under stress the material becomes birefringent; the relative retardation is proportional to the thickness and to the principal-stress difference, $\Delta=Ct(\sigma_1-\sigma_2)$. In terms of the fringe order $N=\Delta/\lambda$: $\sigma_1-\sigma_2=\dfrac{Nf_\sigma}{t}$. The **material fringe value** $f_\sigma=\lambda/C$ (N/mm per fringe) is the stress-times-thickness needed to produce one fringe: small $f_\sigma$ means a sensitive material.
> **(b)** Isochromatics: loci of equal $\sigma_1-\sigma_2$ (colour or dark bands, fixed for a given load). Isoclinics: loci where a principal stress direction is parallel to the polariser axis (black bands that move when the polarisers are rotated together; removed by the circular polariscope).
> **(c)** $N_c=\dfrac{8P}{\pi Df_\sigma}=\dfrac{8(600)}{\pi(40)(8)}=\mathbf{4.8}$ fringes (so the centre is just past the fourth dark band).
> **(d)** Doubling $P$: $N_c=\mathbf{9.5}$. Polyurethane: $N_c=\dfrac{8(600)}{\pi(40)(0.2)}=\mathbf{191}$, forty times more (too many to count: it would be loaded much less).
> ![[AML-photoelastic-fringes.png]]

## Q8 — What a tensile test cannot give (2 marks)

Which of these is **not** obtained from a standard tensile test? (a) Young's modulus (b) yield strength (c) ultimate tensile strength (d) fatigue limit.

> [!success]- Model answer
> **(d).** The fatigue limit needs a rotating-bending or axial fatigue test over millions of cycles.

## Q9 — Effective length (2 marks)

For a fixed–free column the Euler load is: (a) $\pi^2EI/L^2$ (b) $\pi^2EI/4L^2$ (c) $4\pi^2EI/L^2$ (d) $2\pi^2EI/L^2$.

> [!success]- Model answer
> **(b).** $K=2$, $L_e=2L$, $P_{cr}=\pi^2EI/(2L)^2$.

## Q10 — Young's modulus from the load–deflection slope (3 marks)

In a three-point-bending test on a rectangular beam of $25\times6$ mm section, span 400 mm, the load–deflection line has a slope of 23.6 N/mm. Find $E$.

> [!success]- Model answer
> $k=\dfrac{48EI}{L^3}$, so $E=\dfrac{kL^3}{48I}=\dfrac{23.6(400)^3}{48(450)}=\mathbf{69\,900}$ MPa $\approx\mathbf{70}$ GPa: aluminium. Using the slope rather than a single reading cancels a zero offset.

## Q11 — Same area, different shape (5 marks)

Beam A has width $b$ and depth $h$. Beam B has the same material and length, the same cross-sectional area, width $2b$ and depth $h/2$. Both are simply supported with the same central load. Compare the central deflections and the maximum bending stresses.

> [!success]- Model answer
> $I_A=\dfrac{bh^3}{12}$, $I_B=\dfrac{2b(h/2)^3}{12}=\dfrac{bh^3}{48}=\dfrac{I_A}{4}$. So $\delta_B=\mathbf{4}\delta_A$.
> $S_A=\dfrac{bh^2}{6}$, $S_B=\dfrac{2b(h/2)^2}{6}=\dfrac{bh^2}{12}=\dfrac{S_A}{2}$. So $\sigma_B=\mathbf{2}\sigma_A$.
> **Same weight, same area, but the shallower beam deflects four times as much and is stressed twice as much**: depth is the design variable, because $I\propto h^3$ and $S\propto h^2$.

## Q12 — The ruler (5 marks)

A steel ruler is 25 mm wide and 3 mm thick. Compare its bending stiffness and strength when it is loaded flat and on edge. Why is the on-edge ruler not used that way in practice?

> [!success]- Model answer
> Flat: $I=\dfrac{25(3)^3}{12}=56.3$ mm⁴, $S=\dfrac{25(3)^2}{6}=37.5$ mm³. On edge: $I=\dfrac{3(25)^3}{12}=3906$ mm⁴, $S=\dfrac{3(25)^2}{6}=312.5$ mm³.
> Stiffness ratio $=\left(\dfrac{25}{3}\right)^2=\mathbf{69}$; strength ratio $=\dfrac{25}{3}=\mathbf{8.3}$.
> A thin, deep strip loaded on edge is **laterally unstable**: it twists and buckles sideways (lateral–torsional buckling) long before it reaches its strength. Narrow deep beams need bracing, which is why a ruler is used flat and joists are stiffened by sheathing.

## Q13 — Loads at the centre and on an overhang (5 marks)

A beam $ABC$ is supported at $A$ and $B$, 800 mm apart, and overhangs 200 mm to $C$. A load $P$ acts at the middle of $AB$ and an equal load $P$ acts at $C$. Sketch the bending-moment diagram and the deflected shape, and find the point of contraflexion. (Aluminium, $25\times6$ mm, $P=50$ N, $E=70$ GPa.)

> [!success]- Model answer
> ![[AML-mock-overhangs.png]]
> Moments about $B$: $R_A\cdot800=P(400)-P(200)$, so $R_A=\dfrac P4=12.5$ N and $R_B=87.5$ N.
> $M$ at mid-span (sagging) $=R_A(400)=5000$ N·mm; $M_B=-P(200)=-10\,000$ N·mm (hogging, the maximum).
> $M=0$ in the second half-span at $12.5x=50(x-400)$, so $x=\mathbf{533}$ mm $=\dfrac{2L}{3}$ from $A$: the **point of contraflexion**.
> Deflected shape: the span sags (largest sag $\approx\mathbf{4.6}$ mm at 330 mm from $A$); beyond the contraflexion point the curvature reverses (hogging) and the beam arches **above** the support line near $B$ (a small rise of $0.8$ mm at about 720 mm); the tip $C$ goes **down by 8.5 mm**. The deflection curve has its inflexion at $x=533$ mm, where $M=0$.

## Marking summary

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marks | 6 | 4 | 4 | 5 | 6 | 4 | 9 | 2 | 2 | 3 | 5 | 5 | 5 | **60** |

Back to [[Applied Mechanics Lab - Mock Papers]]
