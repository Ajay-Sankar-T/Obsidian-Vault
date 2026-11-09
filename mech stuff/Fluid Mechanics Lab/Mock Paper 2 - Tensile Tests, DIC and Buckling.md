---
tags: [applied-mechanics-lab, AM2540, exam-prep, tutorial]
up: "[[Applied Mechanics Lab - Mock Papers]]"
aliases: [AM2540 mock paper 2, Applied Mechanics Lab mock exam 2]
---

# Mock Paper 2 — Tensile Tests, DIC and Buckling

Part of [[Applied Mechanics Lab - Mock Papers]] · previous: [[Mock Paper 1 - Strain Gauge, Torsion and Beams]] · experiments: [[Lab - Tensile Test of Mild Steel with DIC]], [[Lab - Tensile Test on the ES6 Tester]], [[Lab - Buckling of Struts]]

> [!abstract] Paper details
> **AM2540 Applied Mechanics Lab: mock end-semester paper 2.** Maximum marks 60. Time 45 minutes. All questions are mandatory. Assume a suitable value for any missing data. Marks per question: 6, 4, 4, 5, 6, 4, 9, 2, 2, 3, 5, 5, 5. This paper leans on the tensile and buckling experiments. Numbers: `Tools/aml_mock_core.py` (`m2`).

## Q1 — Digital image correlation (6 marks)

(a) Explain how digital image correlation (DIC) measures strain on a tensile specimen. (2)
(b) Give two advantages over a clip-on extensometer. (2)
(c) Why must the speckle pattern be random and fine? (1)
(d) Two subset centres 20 mm apart move apart by 0.060 mm during loading. What is the strain between them? (1)

> [!success]- Model answer
> **(a)** A random speckle pattern is applied to the surface. A camera records images before and during loading. The software divides the image into small **subsets**, finds each subset in the later image by maximising the correlation of the grey-level pattern, and so obtains the **displacement field**. Strain is the gradient of displacement between neighbouring subsets.
> **(b)** **Full field:** it shows the strain everywhere, including the localised strain in the neck, which an extensometer averages away. **Non-contact:** no knife-edges to slip, damage the specimen or be destroyed at fracture; it can follow the specimen up to failure. (Also: it gives the true local strain and the Poisson contraction.)
> **(c)** Random so that every subset has a **unique** pattern (no ambiguity in the match); fine so that each subset contains enough features and the spatial resolution is high.
> **(d)** $\varepsilon=\dfrac{0.060}{20}=0.003=\mathbf{3000\ \mu\varepsilon}$.

## Q2 — Shaft diameter and length (4 marks)

A solid shaft transmits a torque $T$. (a) If its diameter is halved, by what factors do the maximum shear stress and the angle of twist change? (b) If instead its length is doubled, what happens? (c) What happens to the torque it can carry if the diameter is halved?

> [!success]- Model answer
> $\tau_{max}=\dfrac{16T}{\pi d^3}\propto d^{-3}$ and $\phi=\dfrac{TL}{GJ}\propto\dfrac{L}{d^4}$.
> **(a)** $\tau$ rises **8 times**; $\phi$ rises **16 times**.
> **(b)** $\tau$ is unchanged (it does not depend on $L$); $\phi$ doubles.
> **(c)** At the same allowable stress the capacity $T=\tau_{all}\pi d^3/16$ falls to **$1/8$**.

## Q3 — The ES6 hand-cranked tester (4 marks)

On the ES6 tester a spring pack of combined rate 100 N/mm is compressed by the pull; a dial gauge measures the compression. For one reading the nut has moved 3.20 mm and the dial reads 2.90 mm. The thin section of the specimen has $A_0=9$ mm² and $L_0=31$ mm. Find the force, the extension of the specimen, the stress and the strain, and say why the nut movement is not the extension.

> [!success]- Model answer
> $F=2.90\times100=\mathbf{290}$ N. Extension $=3.20-2.90=\mathbf{0.30}$ mm (the springs absorb the rest). $\sigma=\dfrac{290}{9}=\mathbf{32.2}$ MPa, $\varepsilon=\dfrac{0.30}{31}=\mathbf{0.0097}$.
> The nut movement is the sum of the spring compression **and** the specimen extension; here the springs take $2.90/3.20=91\%$ of it. Using the nut reading alone would over-estimate the strain by a factor of about 10.

## Q4 — True stress and true strain (5 marks)

A tensile bar of 10 mm diameter reaches an engineering stress of 400 MPa at an engineering strain of 0.18, before necking. Find the true stress, the true strain and the current cross-sectional area. Up to what point are these relations valid, and what is needed after it?

> [!success]- Model answer
> $\sigma_t=S(1+e)=400(1.18)=\mathbf{472}$ MPa; $\varepsilon_t=\ln(1+e)=\ln1.18=\mathbf{0.166}$; $A=\dfrac{A_0}{1+e}=\dfrac{78.5}{1.18}=\mathbf{66.6}$ mm² (volume constant). The true stress is $18\%$ above the engineering stress.
> Valid only **up to the onset of necking** (uniform deformation, volume constant). After necking the strain is concentrated in the neck: the true stress needs the **neck's** current area (measured diameter), and the true strain $2\ln(d_0/d_{neck})$.

## Q5 — Failure of timber (6 marks)

A clear wooden specimen is tested in (i) tension along the grain, (ii) compression along the grain, (iii) torsion, (iv) three-point bending. Describe the failure of each and explain.

> [!success]- Model answer
> Wood is strongly **anisotropic**: strong along the fibres, weak in shear along the grain and in tension across it.
>
> | Test | Failure | Reason |
> |---|---|---|
> | Tension along the grain | splintered, jagged fracture; fibres pull out | high strength along the fibres, final failure is fibre rupture and pull-out |
> | Compression along the grain | **crushing**: fibres buckle and kink in a band at about $45^\circ$ | compressive strength is about half the tensile; the thin fibre walls buckle |
> | Torsion | **splits along the grain** | the complementary shear stress acts on planes **parallel** to the grain, the weakest shear plane |
> | Bending | compression wrinkles on the top face first, the neutral axis shifts down, then the tension fibres fracture at the bottom | compression yields before tension fails |
>
> Compare the isotropic case in [[Failure Planes - Ductile and Brittle Fracture]].

## Q6 — Steel against PVC (4 marks)

On the same axes sketch the engineering stress–strain curves of mild steel and PVC from the tensile test, and explain the differences in stiffness, strain at failure and sensitivity to the loading rate.

> [!success]- Model answer
> ![[AML-tensile-curves.png]]
> **Stiffness:** steel $E\approx200$ GPa, PVC $\approx3$ GPa: the PVC curve rises about $70$ times less steeply. **Strain at failure:** steel necks and fails at 20–30 %; PVC stretches by tens of millimetres (very large strains) after a low yield (about 40–60 MPa). **Rate:** PVC is **viscoelastic**: a faster test gives a higher modulus and strength, and at constant load it creeps; steel at room temperature is almost rate-insensitive. This is why the manual asks for a consistent loading rate.

## Q7 — Euler buckling (9 marks)

(a) Derive Euler's critical load for a pin-ended column. (5)
(b) A steel strip, 25 mm wide, 3 mm thick and 400 mm long ($E=210$ GPa) is tested. Find the Euler load for pinned–pinned ends and for fixed–pinned ends ($K=0.7$). In the fixed–pinned test the clamp shortens the free length by 20 mm: what load do you predict? (2)
(c) Give two reasons why the measured buckling load is lower than the Euler value. (2)

> [!success]- Model answer
> **(a)** Let the column deflect slightly by $v(x)$. The moment at a section is $M=-Pv$, and $EIv''=M$, so $EIv''+Pv=0$. With $k^2=P/EI$: $v=A\sin kx+B\cos kx$. Boundary conditions $v(0)=0\Rightarrow B=0$, $v(L)=0\Rightarrow A\sin kL=0$. A non-trivial ($A\ne0$) solution requires $\sin kL=0$, $kL=n\pi$. The smallest is $n=1$: $P_{cr}=\dfrac{\pi^2EI}{L^2}$, with the half-sine shape.
> **(b)** $I=\dfrac{25(3)^3}{12}=56.25$ mm⁴ (weak axis). Pinned–pinned: $P_{cr}=\dfrac{\pi^2(210\,000)(56.25)}{400^2}=\mathbf{729}$ N. Fixed–pinned, $L=400$: $\mathbf{1487}$ N. With the free length $380$ mm: $\dfrac{\pi^2EI}{(0.7\times380)^2}=\mathbf{1648}$ N.
> **(c)** Initial crookedness of the strip; load eccentricity or an end that is not a perfect pin (friction in the notch); the clamped end not perfectly rigid; $E$ from the handbook rather than the strip. Each reduces $P_{exp}$ below $P_{Euler}$.
> ![[AML-buckling-vs-length.png]]

## Q8 — Gauge factor (2 marks)

The gauge factor of a metal foil strain gauge is about: (a) 0.2 (b) 2 (c) 20 (d) 200.

> [!success]- Model answer
> **(b).** $GF=(\Delta R/R)/\varepsilon\approx2$; semiconductor gauges reach 100 or more.

## Q9 — The circular polariscope (2 marks)

A circular polariscope is used because: (a) the light is monochromatic (b) it removes the isoclinics so that only isochromatics remain (c) it doubles the fringe order (d) it removes the temperature effect.

> [!success]- Model answer
> **(b).** The quarter-wave plates make the light circularly polarised, so extinction no longer depends on the angle between the polarisers and the principal stress axes.

## Q10 — Properties from a tensile test (3 marks)

A round bar of 10 mm diameter and 50 mm gauge length yields at 19.6 kN, carries a maximum load of 31.4 kN, and after fracture the gauge length is 63 mm and the neck diameter is 6 mm. Find the yield strength, the ultimate strength, the percentage elongation and the percentage reduction in area.

> [!success]- Model answer
> $A_0=78.5$ mm². $\sigma_Y=\dfrac{19\,600}{78.5}=\mathbf{250}$ MPa; $\sigma_u=\dfrac{31\,400}{78.5}=\mathbf{400}$ MPa; $\%EL=\dfrac{63-50}{50}=\mathbf{26\%}$; $\%RA=\dfrac{10^2-6^2}{10^2}=\mathbf{64\%}$. Both ductility measures are high: the bar is a ductile mild steel.

## Q11 — Deflection with the load off-centre (5 marks)

In the three-point-bending experiment the load $P$ is moved from mid-span to a quarter of the span from one support. (a) Compare the deflection under the load with the central deflection in the first test. (2) (b) Where is the largest deflection, and how large is it compared with the central deflection of the first test? (3)

> [!success]- Model answer
> Central load: $\delta_c=\dfrac{PL^3}{48EI}=0.02083\dfrac{PL^3}{EI}$.
> **(a)** Under a load at $a=L/4$ ($b=3L/4$): $\delta=\dfrac{Pa^2b^2}{3EIL}=\dfrac{9}{768}\dfrac{PL^3}{EI}=0.01172\dfrac{PL^3}{EI}=\mathbf{0.56}\,\delta_c$ (exactly $9/16$).
> **(b)** The maximum is in the **longer** segment, **not** under the load: at a distance $x=\sqrt{(L^2-a^2)/3}=0.559L$ from the far support, i.e. $\mathbf{0.441L}$ from the near support. Its value is $\delta_{max}=\dfrac{Pa(L^2-a^2)^{3/2}}{9\sqrt3EIL}=0.01456\dfrac{PL^3}{EI}=\mathbf{0.70}\,\delta_c$. This is why the manual places gauges at several points.

## Q12 — Stiffening a cantilever (5 marks)

An aluminium cantilever deflects 4.0 mm at its tip under a given load. Without changing the load, find the new deflection if (a) the beam is made 20 % shorter, (b) its depth is increased by 20 %, (c) both, (d) it is replaced by an identical steel one ($E_s=3E_{Al}$).

> [!success]- Model answer
> $\delta=\dfrac{PL^3}{3EI}\propto\dfrac{L^3}{Ebh^3}$.
> (a) $4.0(0.8)^3=\mathbf{2.05}$ mm. (b) $\dfrac{4.0}{1.2^3}=\mathbf{2.31}$ mm. (c) $4.0\times\dfrac{0.8^3}{1.2^3}=\mathbf{1.19}$ mm. (d) $\dfrac{4.0}{3}=\mathbf{1.33}$ mm.
> A 20 % change in length or depth is worth as much as a change of material: the cubes make geometry the cheap way to stiffen a beam.

## Q13 — The overhang with self-weight (5 marks)

The aluminium beam of the three-point-bending lab ($25\times6$ mm, $E=70$ GPa, span $L=400$ mm) carries a central load $W=24.5$ N and overhangs 60 mm beyond each support. The overhangs have weight (density 2700 kg/m³). By how much do they change the central deflection? Sketch the deflected shape for $l=0$ and $l\ne0$.

> [!success]- Model answer
> ![[AML-real-q13-overhang.png]]
> $EI=3.15\times10^7$ N·mm². Weight per length $w=2700(150\times10^{-6})(9.81)=3.97$ N/m $=0.00397$ N/mm.
> Central load: $\dfrac{WL^3}{48EI}=1.037$ mm. Self-weight of the span: $\dfrac{5wL^4}{384EI}=0.042$ mm. The overhang weight gives each support a hogging moment $M_0=\dfrac{wl^2}{2}=7.15$ N·mm, which **reduces** the span deflection by $\dfrac{M_0L^2}{8EI}=0.0045$ mm. Net with overhang: $1.075$ mm against $1.079$ mm without: a change of $\mathbf{0.4\%}$.
> The overhang is **straight** if weightless and tilts upward by $\theta l=\dfrac{WL^2}{16EI}l=0.47$ mm at the tips. **Conclusion:** the overhang matters only through its weight (or a load on it); it is negligible here but it would not be for a long, heavy or loaded overhang (compare Mock Paper 1, Q13).

## Marking summary

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marks | 6 | 4 | 4 | 5 | 6 | 4 | 9 | 2 | 2 | 3 | 5 | 5 | 5 | **60** |

Next: [[Mock Paper 3 - Bending, Photoelasticity and Instruments]]
