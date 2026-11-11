---
tags: [applied-mechanics-lab, AM2540, exam-prep, tutorial]
up: "[[Applied Mechanics Lab - Mock Papers]]"
aliases: [AM2540 mock paper 1, Applied Mechanics Lab mock exam 1]
---

# Mock Paper 1 — Strain Gauge, Torsion and Beams

Part of [[Applied Mechanics Lab - Mock Papers]] · pattern: [[Applied Mechanics Lab - Past Paper Pattern and Model Answers]] · formulas: [[Strength of Materials - Formula Bank]] (§12)

> [!abstract] Paper details
> **AM2540 Applied Mechanics Lab: mock end-semester paper 1.** Maximum marks 60. Time 45 minutes. All questions are mandatory. Assume a suitable value for any missing data. The structure and the weights follow the pattern of the real paper (13 questions: 6, 4, 4, 5, 6, 4, 9, 2, 2, 3, 5, 5, 5). Attempt it **without notes in one sitting**, then open the model answers. Every number is computed in `Tools/aml_mock_core.py`.

## Q1 — Strain gauge on a cantilever (6 marks)

A steel cantilever (width 25 mm, thickness 6 mm, $E=200$ GPa) carries a load of 20 N at its free end. A foil strain gauge ($R=120\ \Omega$, gauge factor 2.1) is bonded on the top surface at the root, 300 mm from the load. The bridge excitation is 5 V.
(a) Which arrangement of gauges makes the reading independent of temperature and doubles the output? Give the reason. (2)
(b) Find the strain at the gauge, the change in gauge resistance, and the bridge output for the quarter bridge (with a dummy) and for your arrangement. (3)
(c) Define the gauge factor. (1)

> [!success]- Model answer
> **(a)** A second gauge on the **underside**, both gauges in **adjacent** arms (half bridge). A temperature change alters both resistances equally and cancels in $\varepsilon_1-\varepsilon_2$; bending gives $+\varepsilon$ and $-\varepsilon$, which add: output doubled.
> **(b)** $\sigma=\dfrac{6PL}{bt^2}=\dfrac{6(20)(300)}{25(36)}=40$ MPa; $\varepsilon=\dfrac{40}{200\,000}=\mathbf{200\ \mu\varepsilon}$; $\Delta R=GF\,R\,\varepsilon=2.1(120)(200\times10^{-6})=\mathbf{0.0504\ \Omega}$.
> Quarter bridge: $V_o=\dfrac{V_{ex}GF\varepsilon}{4}=\dfrac{5(2.1)(200\times10^{-6})}{4}=\mathbf{0.525}$ mV; half bridge: $\mathbf{1.05}$ mV.
> **(c)** $GF=\dfrac{\Delta R/R}{\varepsilon}$.
> ![[AML-bridge-configs.png]]

## Q2 — Hollow against solid shaft, same mass (4 marks)

A hollow shaft with $d_i/d_o=0.5$ and a solid shaft of the same material, length and **weight**. Compare their torque capacities (equal allowable shear stress) and torsional stiffnesses.

> [!success]- Model answer
> Same weight means the same area: $d^2=d_o^2(1-k^2)$, so $d=0.866\,d_o$ ($k=0.5$).
> Torque capacity $T=\dfrac{\pi\tau}{16}\times$ (diameter$^3$, with the hollow factor $1-k^4$): $\dfrac{T_h}{T_s}=\dfrac{d_o^3(1-k^4)}{d^3}=\dfrac{0.9375}{0.866^3}=\mathbf{1.44}$.
> Stiffness $GJ$: $\dfrac{J_h}{J_s}=\dfrac{d_o^4(1-k^4)}{d^4}=\dfrac{0.9375}{0.866^4}=\mathbf{1.67}$.
> The hollow shaft carries **44 % more torque** and is **67 % stiffer** for the same weight, because the material is moved to the large radius where $\tau$ is highest.

## Q3 — Mirror and scale in the torsion experiment (4 marks)

A small mirror is fixed to the shaft. A scale at 1.0 m from the mirror shows a shift of 30 mm of the reflected spot when a torque of 1.0 N·m acts on a steel rod of diameter 8 mm and length 500 mm. (a) Derive the relation between the shift and the angle of twist. (b) Find the twist and the shear modulus.

> [!success]- Model answer
> **(a)** A mirror rotated through $\phi$ rotates the reflected ray through $2\phi$; the spot on a scale at distance $D$ moves by $s=D\tan2\phi$, so $\phi=\tfrac12\arctan(s/D)\approx s/2D$.
> **(b)** $\phi=\tfrac12\arctan(0.03)=\mathbf{0.0150}$ rad $=0.859^\circ$ (small-angle: $0.0150$). $J=\dfrac{\pi(8)^4}{32}=402.1$ mm⁴.
> $G=\dfrac{TL}{J\phi}=\dfrac{(1000\ \text{N·mm})(500)}{402.1(0.0150)}=82\,900$ MPa $=\mathbf{82.9}$ GPa, within 4 % of 79.6 GPa for steel.
> ![[AML-mirror-twist.png]]

## Q4 — The stress–strain diagram (5 marks)

(a) Sketch the engineering stress–strain curve of mild steel and mark the proportional limit, elastic limit, yield, ultimate and fracture points. (3)
(b) Why does the engineering curve fall after the ultimate point while the true curve keeps rising? (1)
(c) How is yield strength found for aluminium, which has no yield plateau? (1)

> [!success]- Model answer
> **(a)** ![[SM-FB-1-stress-strain.png]]
> **(b)** After necking begins, the load falls because the neck area shrinks, but engineering stress divides by the original area $A_0$; the true stress uses the actual (smaller) area and so keeps rising with strain hardening.
> **(c)** The $0.2\%$ offset method: draw a line parallel to the elastic slope through $\varepsilon=0.002$; its intersection with the curve is $\sigma_{0.2}$.

## Q5 — Failure of brittle and ductile materials (6 marks)

Sketch the fracture surfaces of a ductile material (mild steel) and a brittle one (cast iron) under (i) compression, (ii) torsion, (iii) three-point bending, and give the reason in each case.

> [!success]- Model answer
> ![[SM-FP-failure-planes.png]]
>
> | Load | Mild steel | Cast iron |
> |---|---|---|
> | Compression | squashes and **barrels** (flows sideways), does not fracture | shear fracture on an oblique plane ($\approx45^\circ$ or steeper), or splitting |
> | Torsion | shears on the **cross-section** | **$45^\circ$ helix** |
> | 3-point bending | bends, no fracture | crack from the tension face at mid-span, vertical |
>
> **Reason:** steel is weaker in shear (fails where $\tau$ is greatest); cast iron is weaker in tension (fails normal to $\sigma_1$), and is three to five times stronger in compression. See [[Failure Planes - Ductile and Brittle Fracture]].

## Q6 — Gauge length (4 marks)

Two tensile specimens of the same material and diameter have gauge lengths $L_0$ and $2L_0$. Sketch the load–extension and stress–strain curves and explain. Does the percentage elongation at fracture agree?

> [!success]- Model answer
> The stress–strain curves coincide up to necking (same $E$, $\sigma_Y$, $\sigma_u$), and the load–extension curves have the same load at every point but the extension at a given strain is **twice** as large for $2L_0$.
> The percentage elongation does **not** agree: after necking the extra extension is concentrated in the neck, a fixed amount $\Delta_{neck}$, so $\%EL=e_u+\Delta_{neck}/L_0$ is smaller for the longer gauge length. Example: $e_u=16\%$ and a 5 mm neck: $L_0=50$ mm gives $26\%$, $L_0=100$ mm gives $21\%$. Standards fix $L_0=5.65\sqrt{A_0}$ for this reason.

## Q7 — Buckling of struts (9 marks)

(a) State the assumptions in Euler's theory of buckling. (3)
(b) A steel strip 20 mm wide, 3 mm thick and 600 mm long ($E=210$ GPa) is used as a strut. Find the Euler load for pinned–pinned, fixed–pinned ($K\approx0.7$) and fixed–fixed ends. About which axis does it buckle? (3)
(c) A column of square section $b\times b$ and one of circular section have the same cross-sectional area, length, material and end conditions. Which has the larger critical load? (3)

> [!success]- Model answer
> **(a)** Straight, homogeneous and linearly elastic column; axial load through the centroid; ideal end supports; small deflections; $\sigma_{cr}$ below the proportional limit; no initial stress or crookedness.
> **(b)** It buckles about the axis of **minimum** $I$: $I=\dfrac{20(3)^3}{12}=45$ mm⁴ (the thin direction).
> Pinned–pinned: $P_{cr}=\dfrac{\pi^2(210\,000)(45)}{600^2}=\mathbf{259}$ N. Fixed–pinned ($L_e=420$): $\mathbf{529}$ N. Fixed–fixed ($L_e=300$): $\mathbf{1036}$ N. (Check: $\lambda=L/r=693$, $\sigma_{cr}=4.3$ MPa $\ll\sigma_Y$, so Euler applies.)
> **(c)** $P_{cr}\propto I$. For area $A$: $I_{square}=\dfrac{A^2}{12}=0.0833A^2$, $I_{circle}=\dfrac{A^2}{4\pi}=0.0796A^2$: the **square** is larger, by a factor $\pi/3=1.05$ (about 5 %). With equal *perimeter* the circle would win ($1.55\times$): read which quantity is held constant.

## Q8 — Photoelastic disk (2 marks)

The load on a disk in diametral compression is doubled. The number of fringes at the centre: (a) remains the same (b) halves (c) doubles (d) cannot be predicted.

> [!success]- Model answer
> **(c).** $N_c=8P/(\pi Df_\sigma)\propto P$.

## Q9 — Isoclinics (2 marks)

Isoclinics are: (a) loci of points with the same principal-stress difference (b) loci of points where a principal-stress direction is parallel to the polariser axis (c) loci of equal principal stress sum (d) lines of zero shear in the beam.

> [!success]- Model answer
> **(b).** Isochromatics (a) depend on $\sigma_1-\sigma_2$ and stay fixed when the polarisers rotate; isoclinics move.

## Q10 — Fringe order in a bent beam (3 marks)

A rectangular beam of thickness 6 mm and depth 20 mm is in pure bending in a circular polariscope. The fringe order at the extreme fibre is 6; $f_\sigma=10.5$ N/mm per fringe. Find the maximum stress, the bending moment, and the fringe order at a quarter depth from the neutral axis.

> [!success]- Model answer
> $\sigma_{max}=\dfrac{Nf_\sigma}{t}=\dfrac{6(10.5)}{6}=\mathbf{10.5}$ MPa. $M=\sigma\dfrac{td^2}{6}=10.5\times\dfrac{6(20)^2}{6}=\mathbf{4200}$ N·mm. $N$ is linear in $y$ and zero on the neutral axis: at half the distance to the edge ($y=h/4$) $N=\mathbf3$.
> ![[AML-photoelastic-fringes.png]]

## Q11 — Steel flat against aluminium on edge (5 marks)

Two simply supported beams of the same length carry the same central load. Beam S is steel ($E=200$ GPa), a $20\times10$ mm bar laid **flat** (20 mm wide, 10 mm deep). Beam A is aluminium ($E=70$ GPa) of the same section but turned **on edge** (10 mm wide, 20 mm deep). Compare the central deflections and draw a conclusion.

> [!success]- Model answer
> $I_S=\dfrac{20(10)^3}{12}=1667$ mm⁴, $I_A=\dfrac{10(20)^3}{12}=6667$ mm⁴, a ratio of 4.
> $\dfrac{\delta_A}{\delta_S}=\dfrac{E_SI_S}{E_AI_A}=\dfrac{200(1667)}{70(6667)}=\mathbf{0.71}$.
> The aluminium beam on edge deflects **29 % less** than the steel beam laid flat, although aluminium is $2.9$ times less stiff. (Laid flat, aluminium would deflect $2.86$ times as much as the steel.) **Conclusion:** the section's orientation, which enters as $I\propto h^3$, matters more than the choice of material; stiffness is $EI$, not $E$.

## Q12 — Reducing deflection (5 marks)

A simply supported strip of $25\times3$ mm section carries a central load. Without changing the material, length or load, give three ways of reducing the central deflection by a factor of four or more, with the reduction in each case.

> [!success]- Model answer
> $\delta=\dfrac{PL^3}{48EI}$: raise $I$ or restrain the ends.
> 1. **Turn it on edge** (25 mm deep, 3 mm wide): $I$ rises by $(25/3)^2=\mathbf{69}$ times.
> 2. **Clamp both ends:** $\delta=\dfrac{PL^3}{192EI}$, **one quarter**.
> 3. **Use a deeper section of the same area** (75 mm², e.g. 6.25 mm wide $\times$ 12 mm deep): $I=\dfrac{6.25(12)^3}{12}=900$ mm⁴ against $56$ mm⁴, so $\delta$ falls **16 times**; an **I-section** does better still by putting the material at the outer fibres.
> Example: doubling the depth alone gives $\delta/8$.

## Q13 — Overhangs loaded at the tips (5 marks)

A beam is supported at two points 600 mm apart and overhangs 200 mm on each side. Equal loads $P=50$ N act at both free ends. The beam is aluminium, $25\times6$ mm ($E=70$ GPa). Sketch the deflected shape, state where the bending moment is constant, and find the deflection at mid-span and at the tips.

> [!success]- Model answer
> ![[AML-mock-overhangs.png]]
> The moment in the span is **constant**, $M=-Pa=-50(200)=-10\,000$ N·mm (hogging), so the span bends into a **circular arc** that arches **upward**: $\delta_{mid}=\dfrac{PaL^2}{8EI}=\dfrac{50(200)(600)^2}{8(3.15\times10^7)}=\mathbf{14.3}$ mm **up**. The slope at each support is $\theta=\dfrac{PaL}{2EI}=0.095$ rad.
> The tips go **down**: $\delta_{tip}=\theta a+\dfrac{Pa^3}{3EI}=19.05+4.23=\mathbf{23.3}$ mm. No point of contraflexion: the curvature has the same sign throughout. This is the arrangement of a **four-point bend** test: pure bending between the inner supports.

## Marking summary

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marks | 6 | 4 | 4 | 5 | 6 | 4 | 9 | 2 | 2 | 3 | 5 | 5 | 5 | **60** |

Next: [[Mock Paper 2 - Tensile Tests, DIC and Buckling]]
