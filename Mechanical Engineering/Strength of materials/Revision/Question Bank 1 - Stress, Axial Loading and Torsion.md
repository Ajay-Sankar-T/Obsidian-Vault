---
title: Question Bank 1 – Stress, Axial Loading and Torsion
tags: [strength-of-materials, question-bank, tutorial]
up: "[[Strength of Materials - Question Bank]]"
aliases: [SoM question bank 1, axial and torsion practice problems]
---

# Question Bank 1 — Stress, Axial Loading and Torsion

Part of [[Strength of Materials - Question Bank]] · formulas: [[Strength of Materials - Formula Bank]] (§1–§3) · theory: [[Concept of Stress]], [[Axial Deformation]], [[Statically Indeterminate Axial Members]], [[Thermal Stresses]], [[Torsion of Circular Shafts]], [[Power Transmission by Shafts]]

> [!abstract] What is here
> Twelve short conceptual questions (Part A) and nine numerical problems (Q1–Q9). Try each on paper first; open **Hint** only if stuck, then check **Solution**. Every number is recomputed in `Tools/sm_bank_core.py` (functions `p1_n1` … `p1_n9`).

## Part A — Conceptual questions

> [!question]- A1. Define normal, shear and bearing stress. Which area is used in each?
> Normal $\sigma=P/A$ uses the area **perpendicular** to $P$; shear $\tau=V/A$ uses the area **parallel** to $V$ (the sheared plane); bearing $\sigma_b=P/(dt)$ uses the **projected** contact area of a pin or rivet in its hole. All are force per area (N/mm² = MPa).

> [!question]- A2. Engineering stress against true stress: how do they differ, and when are they equal?
> Engineering $S=P/A_0$ (original area), true $\sigma=P/A$ (current area). Before necking, with volume conserved, $\sigma=S(1+e)$ and $\varepsilon_t=\ln(1+e)$. They agree to a few percent below $e\approx0.05$. After necking the engineering curve falls (the neck carries the load on a shrinking area) while the true curve keeps rising.

> [!question]- A3. Distinguish proportional limit, elastic limit and yield strength. Why is the $0.2\%$ offset method used?
> Proportional limit: end of the straight line ($\sigma\propto\varepsilon$). Elastic limit: the largest stress with no permanent set on unloading (almost equal to the proportional limit for steel). Yield: the stress where large plastic strain starts. Aluminium and high-strength steels have no plateau, so yield is *defined* as the stress where a line parallel to the elastic line, offset by $\varepsilon=0.002$, meets the curve.

> [!question]- A4. Show that $G=E/2(1+\nu)$ follows from pure shear, and state the range of $\nu$.
> Pure shear $\tau$ is equivalent to $\sigma_1=\tau$, $\sigma_2=-\tau$ on planes at $45^\circ$. Then $\varepsilon_1=\dfrac{\tau(1+\nu)}{E}$, and the shear strain is $\gamma=2\varepsilon_1$ (the diagonal stretches while the square distorts), so $\gamma=\dfrac{2(1+\nu)}{E}\tau=\tau/G$. For a stable material $K>0$ and $G>0$ require $-1<\nu<0.5$; ordinary solids have $0.2$–$0.35$, rubber $\approx0.5$ (incompressible).

> [!question]- A5. A steel bar is heated while free to expand. What stress develops, and what changes if the ends are fixed?
> None when it is free: $\varepsilon=\alpha\Delta T$ is a free strain and produces no stress. With fixed ends the net strain must be zero, so $\sigma=-E\alpha\Delta T$ (for steel, $\approx-2.4$ MPa per °C). Thermal stress needs restraint, in the form of a wall, a different material alongside, or a temperature gradient.

> [!question]- A6. Resilience against toughness: define both, and say which one matters for a spring and which for a crash barrier.
> Resilience $u_r=\sigma_Y^2/2E$: energy per volume absorbed and **returned** (area to the yield point). Toughness: total area under the curve to fracture. A spring needs high resilience (high $\sigma_Y$, low $E$); a barrier needs high toughness (large strain to failure at good stress).

> [!question]- A7. State the three-step method for a statically indeterminate axial problem.
> (1) Equilibrium. (2) Compatibility: write how the deformations must fit together. (3) Force–deformation law ($\delta=FL/AE+\alpha\Delta TL$) to turn compatibility into an equation in the unknown forces. Solve, then check the result against any equation you did not use.

> [!question]- A8. List the assumptions of the torsion formula $\tau=Tr/J$.
> Circular section (solid or hollow), prismatic shaft, torque applied at the ends or uniformly, plane cross-sections remain plane and undistorted, radial lines remain straight, linear elastic material ($\tau<\tau_Y$, Hooke's law), small twist. Away from the loaded ends (Saint-Venant).

> [!question]- A9. Why does a non-circular shaft not obey the torsion formula?
> Sections **warp**: they do not stay plane, so $\gamma$ is not proportional to $r$ and $J$ is the wrong constant. A square shaft has a larger peak stress and smaller stiffness than its inscribed circle formula suggests. Thin-walled tubes use $\tau=T/2A_mt$ instead.

> [!question]- A10. A solid shaft's diameter is doubled for the same torque. By what factors do $\tau_{max}$ and $\phi$ change?
> $\tau_{max}=16T/\pi d^3$ falls by $2^3=8$. $\phi=TL/GJ\propto d^{-4}$ falls by $2^4=16$. The shaft gets stronger by 8 and stiffer by 16.

> [!question]- A11. Why is a hollow shaft more economical than a solid one of the same strength?
> Shear stress is proportional to $r$: the core carries little stress yet adds mass. Moving the material outward raises $J$ per unit area. At $k=d_i/d_o=0.6$, a hollow shaft of the same torsional strength has $d_o/d=1.047$ and only about 70 % of the solid shaft's mass (the saving grows with $k$). The limit is wall buckling and cost.

> [!question]- A12. Why do engines and gearboxes use a high-speed shaft with a small diameter and a low-speed shaft with a large one?
> $P=T\omega$ is the same on both shafts (ignoring losses). At higher $\omega$, $T=P/\omega$ is smaller, and the torsional strength needs $d^3\propto T$. A gear reduction of 5:1 multiplies $T$ by 5 and the diameter by $5^{1/3}=1.71$.

## Q1 — Stepped bar, two materials (easy)

![[SM-QB-1-setups.png]]

A steel bar $AB$ (Ø40 mm, 800 mm, $E=200$ GPa) is joined to an aluminium bar $BC$ (Ø25 mm, 600 mm, $E=70$ GPa) and fixed at $A$. A 100 kN force pulls the junction $B$ away from the wall; a 60 kN force pushes $C$ toward the wall. Find the stress in each part and the displacement of $C$.

> [!tip]- Hint
> Draw the internal force in each segment by cutting through it and balancing the loads **beyond** the cut. Then $\delta=\sum P_iL_i/A_iE_i$.

> [!success]- Solution
> $A_{AB}=\pi(40)^2/4=1256.6$ mm², $A_{BC}=\pi(25)^2/4=490.9$ mm².
> Segment $BC$ carries $-60$ kN (compression). Segment $AB$ carries $+100-60=+40$ kN (tension).
> $\sigma_{AB}=40\,000/1256.6=\mathbf{31.8}$ MPa (T); $\sigma_{BC}=-60\,000/490.9=\mathbf{-122.2}$ MPa (C).
> $\delta_{AB}=\dfrac{40\,000\times800}{1256.6\times200\,000}=+0.1273$ mm; $\delta_{BC}=\dfrac{-60\,000\times600}{490.9\times70\,000}=-1.0477$ mm.
> $\delta_C=0.1273-1.0477=\mathbf{-0.920}$ mm: $C$ moves **0.92 mm toward the wall**.
> **Check:** the compressed aluminium is short and soft ($70$ GPa, smaller area), so it dominates, and the net movement has the sign of the 60 kN force.

## Q2 — Rigid bar on two wires (medium)

A rigid bar is pinned at $A$ and hangs from a steel wire (Ø6 mm, 2 m, $E=200$ GPa) at 1 m and an aluminium wire (Ø8 mm, 1.5 m, $E=70$ GPa) at 2 m from $A$. A load $P=8$ kN acts at 3 m. Find the wire forces, stresses and the displacement of the load.

> [!tip]- Hint
> Moment about $A$ gives one equation. The bar rotates rigidly, so the wire stretches are in the ratio 1:2. Write each stretch as $FL/AE$.

> [!success]- Solution
> $A_1=28.27$ mm², $A_2=50.27$ mm². Stiffnesses $k=AE/L$: $k_1=2827$ N/mm, $k_2=2346$ N/mm.
> Equilibrium: $F_1(1)+F_2(2)=8(3)=24$ kN·m.
> Compatibility: rotation $\theta$ at $A$ gives stretches $1000\theta$ and $2000\theta$, so $F_1=k_1(1000\theta)$, $F_2=k_2(2000\theta)$.
> Substituting: $\theta\,[k_1(1000)^2+k_2(2000)^2]=8000\times3000$, so $\theta=1.966\times10^{-3}$ rad.
> $F_1=\mathbf{5.56}$ kN, $F_2=\mathbf{9.22}$ kN. $\sigma_1=\mathbf{196.6}$ MPa, $\sigma_2=\mathbf{183.5}$ MPa.
> Stretches: $1.966$ mm and $3.931$ mm; the load point moves $3000\theta=\mathbf{5.90}$ mm down.
> **Check:** $5.56+2(9.22)=24.0$ ✓. The outer wire takes more load because it stretches twice as much and is nearly as stiff as the inner one; an equal split would violate compatibility.

## Q3 — Steel rod in a copper tube: load plus heating (medium–hard)

A steel rod (Ø20 mm, $E=200$ GPa, $\alpha=12\times10^{-6}$/°C) fits inside a copper tube ($A=600$ mm², $E=110$ GPa, $\alpha=17\times10^{-6}$/°C). Both are 400 mm long and joined by rigid end plates that carry a compressive load $P=80$ kN. The temperature then rises by 40 °C. Find the stress in each material and the change in length.

> [!tip]- Hint
> Equilibrium $F_s+F_c=-P$. Compatibility: equal total strain. Include $\alpha\Delta T$ on both sides of the force–deformation law.

> [!success]- Solution
> $A_s=314.16$ mm². Compatibility: $\dfrac{F_s}{A_sE_s}+\alpha_s\Delta T=\dfrac{F_c}{A_cE_c}+\alpha_c\Delta T$.
> With $F_s=-P-F_c$ this is linear in $F_c$: $F_c=\mathbf{-47.42}$ kN, $F_s=\mathbf{-32.58}$ kN.
> $\sigma_s=-103.7$ MPa, $\sigma_c=-79.0$ MPa (both compressive).
> Length change: $\Big(\dfrac{-32\,580}{314.16\times200\,000}+12\times10^{-6}\times40\Big)(400)=\mathbf{-0.0154}$ mm.
> **Check by superposition.** Load alone shares by stiffness: $A_sE_s=62.8$ MN, $A_cE_c=66.0$ MN, so steel takes 48.8 %, i.e. $-39.0$ kN. Heating alone: copper wants to expand more, so the steel is pulled into tension by $+6.44$ kN and the copper into compression by the same amount. $-39.0+6.44=-32.6$ kN ✓.

## Q4 — Bar heated against a gap (easy–medium)

A steel bar ($E=200$ GPa, $\alpha=12\times10^{-6}$/°C, $A=500$ mm², $L=2$ m) is placed between rigid walls with a 1.0 mm gap at one end. It is heated by 80 °C. Find the wall force.

> [!tip]- Hint
> Compare the free expansion with the gap first. Only the excess is resisted.

> [!success]- Solution
> Free expansion $\alpha\Delta TL=12\times10^{-6}\times80\times2000=1.92$ mm $>1.0$ mm, so it touches the wall (at $\Delta T=41.7$ °C).
> Compressed length $=1.92-1.00=0.92$ mm, so $\varepsilon=0.92/2000=4.6\times10^{-4}$.
> $\sigma=E\varepsilon=\mathbf{92}$ MPa (compressive), $F=\sigma A=\mathbf{46}$ kN.
> **Trap:** using $\sigma=E\alpha\Delta T=192$ MPa ignores the gap and over-estimates by more than twice.

## Q5 — Hanging rod with self-weight (easy)

A vertical steel rod ($\rho=7850$ kg/m³, $E=200$ GPa) of length 15 m and diameter 12 mm hangs from a ceiling and carries 8 kN at its lower end. Find the maximum stress and the total elongation.

> [!tip]- Hint
> The axial force is largest at the top: load plus the entire weight. The weight acts at the centre of gravity of the rod, so its elongation is half that of the same load at the tip.

> [!success]- Solution
> $A=113.1$ mm², $W=\rho gAL=130.6$ N.
> $\sigma_{max}=(8000+130.6)/113.1=\mathbf{71.9}$ MPa at the top.
> $\delta=\dfrac{PL}{AE}+\dfrac{WL}{2AE}=5.305+0.043=\mathbf{5.35}$ mm.
> **Check:** the weight is only $1.6$ % of the load, so it adds $0.8$ % to $\delta$ ✓.

## Q6 — Plate in plane stress, then plane strain (medium)

A steel plate ($E=200$ GPa, $\nu=0.3$) is $100\times50\times10$ mm. It carries $\sigma_x=120$ MPa (tension), $\sigma_y=-40$ MPa and $\sigma_z=0$. Find the three strains, the change in thickness, the change in volume, and the $\sigma_z$ that would appear if the thickness were held fixed.

> [!tip]- Hint
> Use the generalised Hooke's law with all three normal stresses.

> [!success]- Solution
> $\varepsilon_x=\dfrac{120-0.3(-40)}{200\,000}=\mathbf{660}\ \mu\varepsilon$; $\varepsilon_y=\dfrac{-40-0.3(120)}{200\,000}=\mathbf{-380}\ \mu\varepsilon$; $\varepsilon_z=\dfrac{-0.3(120-40)}{200\,000}=\mathbf{-120}\ \mu\varepsilon$.
> $\Delta t=-120\times10^{-6}\times10=\mathbf{-0.0012}$ mm.
> $e=660-380-120=+160\ \mu\varepsilon$, so $\Delta V=160\times10^{-6}\times50\,000=\mathbf{8.0}$ mm³. (Check: $e=\dfrac{1-2\nu}{E}\sum\sigma=\dfrac{0.4}{200\,000}(80)=160\times10^{-6}$ ✓.)
> Plane strain, $\varepsilon_z=0$: $\sigma_z=\nu(\sigma_x+\sigma_y)=\mathbf{24}$ MPa (tension).
> Moduli: $G=76.9$ GPa, $K=166.7$ GPa.

## Q7 — Hollow shaft: power, strength and twist (medium)

A hollow steel shaft with $d_i/d_o=0.6$ transmits 60 kW at 300 rpm. Allowable shear stress 60 MPa, allowable twist 1° per metre, $G=80$ GPa. Find the outer diameter, and compare with a solid shaft meeting both limits.

> [!tip]- Hint
> $T=P/\omega$. Compute $d_o$ from strength and from twist separately, then take the larger.

> [!success]- Solution
> $T=\dfrac{60\,000\times60}{2\pi\times300}=1909.9$ N·m $=1.910\times10^6$ N·mm.
> Strength: $d_o^3=\dfrac{16T}{\pi\tau(1-k^4)}=\dfrac{16(1.910\times10^6)}{\pi(60)(0.8704)}$, so $d_o=57.1$ mm.
> Stiffness ($\theta=1^\circ/\text{m}=1.745\times10^{-5}$ rad/mm): $d_o^4=\dfrac{32T}{\pi G\theta(1-k^4)}$, so $d_o=63.25$ mm.
> **Twist governs:** $d_o=\mathbf{63.3}$ mm, $d_i=38.0$ mm (use 64 mm and 38 mm in practice). Actual $\tau=44.2$ MPa, well below 60.
> Solid shaft: strength needs 54.5 mm, twist needs 61.1 mm, so $d=61.1$ mm. Hollow mass / solid mass $=\mathbf{0.69}$: 31 % lighter for the same twist.
> **Trap:** checking only the stress. Long shafts are almost always governed by twist.

## Q8 — Shaft fixed at both ends (medium)

A solid steel shaft (Ø40 mm, $G=80$ GPa, $L=1.5$ m) is fixed at $A$ and $B$. A torque of 800 N·m acts at $C$, 0.6 m from $A$. Find the end reactions, the peak shear stress in each part and the rotation of $C$.

> [!tip]- Hint
> Equilibrium: $T_A+T_B=800$. Compatibility: the twist of $AC$ plus the twist of $CB$ equals zero (both ends are fixed).

> [!success]- Solution
> $J=\pi(40)^4/32=2.513\times10^5$ mm⁴. Compatibility (the two segments twist in opposite senses): $\dfrac{T_Aa}{GJ}=\dfrac{T_Bb}{GJ}$ with $a=0.6$, $b=0.9$.
> $T_A=800\times\dfrac{0.9}{1.5}=\mathbf{480}$ N·m, $T_B=\mathbf{320}$ N·m. The nearer support takes more.
> $\tau_{AC}=\dfrac{16(480\,000)}{\pi(40)^3}=\mathbf{38.2}$ MPa, $\tau_{CB}=\mathbf{25.5}$ MPa.
> $\phi_C=\dfrac{T_Aa}{GJ}=\dfrac{480\,000\times600}{80\,000\times2.513\times10^5}=0.01432$ rad $=\mathbf{0.82^\circ}$. Check from the other side: $T_Bb/GJ=0.01432$ ✓.

## Q9 — Composite shaft: steel tube bonded to a brass core (hard)

A steel tube (outer Ø50 mm, inner Ø40 mm, $G_s=80$ GPa) is bonded over a solid brass core (Ø40 mm, $G_b=38$ GPa). The shaft carries a torque of 1.5 kN·m. Find the share of torque and the maximum shear stress in each material, and the twist per metre.

> [!tip]- Hint
> Same twist per unit length for both: $T_s/G_sJ_s=T_b/G_bJ_b$, then $T_s+T_b=T$.

> [!success]- Solution
> $J_s=\pi(50^4-40^4)/32=3.623\times10^5$ mm⁴, $J_b=\pi(40)^4/32=2.513\times10^5$ mm⁴.
> $T_s=T\dfrac{G_sJ_s}{G_sJ_s+G_bJ_b}=1500\times\dfrac{28.98}{28.98+9.55}=\mathbf{1128}$ N·m, $T_b=\mathbf{372}$ N·m.
> $\tau_{s,max}=\dfrac{1128\,000\times25}{3.623\times10^5}=\mathbf{77.9}$ MPa (outer surface); $\tau_{b,max}=\dfrac{372\,000\times20}{2.513\times10^5}=\mathbf{29.6}$ MPa.
> Twist: $\phi/L=\dfrac{T_s}{G_sJ_s}=3.89\times10^{-5}$ rad/mm $=\mathbf{2.23^\circ/\text{m}}$.
> **Insight:** shear **strain** is continuous across the bond, shear **stress** is not. At $r=20$ mm the steel has $\tau=62.3$ MPa and the brass $29.6$ MPa, in the ratio $G_s/G_b=2.1$ ✓.

## Cross-links
Elastic constants and 3-D Hooke: [[Generalized Hooke's Law and Poisson's Ratio]] · tutorial versions: [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4]], [[Q1 - Axially Loaded Member|Tutorial 5]], [[Tutorial 6 - Torsional Members|Tutorial 6]] · next: [[Question Bank 2 - Beams, Bending and Shear]]
