---
title: Question Bank 3 – Stress Transformation and Pressure Vessels
tags: [strength-of-materials, question-bank, tutorial]
up: "[[Strength of Materials - Question Bank]]"
aliases: [SoM question bank 3, Mohr circle problems, rosette problems, pressure vessel problems]
---

# Question Bank 3 — Stress Transformation and Pressure Vessels

Part of [[Strength of Materials - Question Bank]] · formulas: [[Strength of Materials - Formula Bank]] (§7, §11) · theory: [[Plane Stress Transformation]], [[Mohr's Circle for Stress]], [[Strain Transformation and Rosettes]], [[Stress-Strain Transformation Analogy]], [[Thin Cylindrical and Spherical Pressure Vessels]], [[Failure Planes - Ductile and Brittle Fracture]]

> [!abstract] What is here
> Twelve conceptual questions and eight numerical problems (Q1–Q8): the state of stress at a point, a shaft under combined loads with two failure criteria, a strain rosette, a strain gauge on a cylinder, wall thickness with joint efficiency, dimensional changes, absolute maximum shear and a strain circle. Numbers from `Tools/sm_bank_core.py` (`p3_n1` … `p3_n8`).

## Part A — Conceptual questions

> [!question]- A1. What are principal planes and principal stresses?
> Principal planes are the two (in 2-D) perpendicular planes on which the shear stress is zero; the normal stresses on them, $\sigma_1\ge\sigma_2$, are the **extreme** normal stresses at the point. They are the eigenvalues of the stress tensor and the planes are its eigenvectors. In 3-D there are three.

> [!question]- A2. Why does a plane rotated by $\theta$ appear at $2\theta$ on Mohr's circle?
> The transformation equations contain $\cos2\theta$ and $\sin2\theta$: the pair $(\sigma_\theta,\tau_\theta)$ traces a circle as $2\theta$ goes round it. Physically, the planes at $\theta=0^\circ$ and $90^\circ$ carry the same invariant and are diametrically opposite ($180^\circ$ apart on the circle), and principal planes ($\theta_p$) are $90^\circ$ apart on the body but $180^\circ$ on the circle.

> [!question]- A3. What is the sign convention used when plotting a Mohr's circle?
> Tension positive on the $\sigma$ axis. For $\tau$: a shear that tends to rotate the element **clockwise** is plotted **downward** (the one on the $x$-face is the point $X$, on the $y$-face the point $Y$ with opposite sign). Angles on the circle go the same way as the rotation of the plane on the element (counter-clockwise $\theta$ is counter-clockwise $2\theta$). Whatever you choose, be consistent and check with one plane you can compute directly.

> [!question]- A4. Show that pure shear is the same as equal tension and compression at $45^\circ$.
> For $\sigma_x=\sigma_y=0$, $\tau_{xy}=\tau$: $R=\tau$ and centre $0$, so $\sigma_{1,2}=\pm\tau$ on planes at $\pm45^\circ$. A shaft in torsion therefore has its **tension** on a $45^\circ$ helix; brittle shafts (chalk, cast iron) crack along it, ductile ones shear on the cross-section.

> [!question]- A5. Why can the in-plane maximum shear stress be smaller than the true maximum shear?
> The in-plane value $(\sigma_1-\sigma_2)/2$ is the largest shear among planes parallel to the $z$ axis. Planes tilted about $\sigma_1$ or $\sigma_2$ feel $(\sigma_1-\sigma_3)/2$ and $(\sigma_2-\sigma_3)/2$. If $\sigma_1,\sigma_2$ have the same sign and $\sigma_3=0$, the largest one involves the third direction: e.g. a pressure vessel wall has $\tau_{abs}=\sigma_h/2$, twice the in-plane value.

> [!question]- A6. Why does a strain rosette use three gauges?
> A 2-D strain state has three independent components, $\varepsilon_x$, $\varepsilon_y$, $\gamma_{xy}$, and a gauge measures only the normal strain along its own axis. Three gauges in three known directions give three equations. A single gauge is enough only if the principal directions are known (e.g. on the axis of a bar or at a free edge).

> [!question]- A7. Compare plane stress and plane strain.
> Plane stress: $\sigma_z=\tau_{xz}=\tau_{yz}=0$ (thin plates, free surfaces); $\varepsilon_z\ne0$. Plane strain: $\varepsilon_z=\gamma_{xz}=\gamma_{yz}=0$ (a long body such as a dam or a long cylinder); $\sigma_z=\nu(\sigma_x+\sigma_y)\ne0$. The transformation formulas for the in-plane stresses are the same in both.

> [!question]- A8. State the Tresca and von Mises criteria. When would you use each?
> Tresca: yield when $\tau_{max}=\sigma_Y/2$, i.e. when the largest of $\lvert\sigma_1-\sigma_2\rvert$, $\lvert\sigma_2-\sigma_3\rvert$, $\lvert\sigma_3-\sigma_1\rvert$ reaches $\sigma_Y$. Von Mises: yield when $\sqrt{\tfrac12[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2]}=\sigma_Y$ (equal distortion energy). Von Mises fits experiments on ductile metals best; Tresca is simpler and **conservative** (by up to 15 %, in pure shear). Neither applies to brittle materials, which follow the maximum normal stress criterion.

> [!question]- A9. Why does a pressurised cylinder split along its length rather than around?
> Because $\sigma_h=pr/t$ is twice $\sigma_L=pr/2t$. The hoop stress acts across the longitudinal section, so the crack opens along the axis (sausage skins and cans split lengthwise). The girth seams are loaded by only half as much.

> [!question]- A10. What does "thin-walled" mean and why is the radial stress neglected?
> $r/t>10$. Then the hoop stress is taken as uniform through the thickness (the error is about $t/2r<5$ %) and the radial stress, which varies from $-p$ inside to $0$ outside, is at most $p$, which is smaller than $\sigma_h$ by the factor $t/r$. For thicker walls use Lamé's equations.

> [!question]- A11. For equal radius, pressure and allowable stress, how do the wall thicknesses of a sphere and a cylinder compare?
> $t_{sphere}=pr/2\sigma_{all}$ and $t_{cyl}=pr/\sigma_{all}$: the sphere needs **half** the wall, because it carries $pr/2t$ in both directions while the cylinder carries $pr/t$ in one. That is why gas bubbles, LPG tanks and the ends of boilers are spherical or nearly so.

> [!question]- A12. What is joint efficiency?
> The ratio of the strength of a welded or riveted seam to that of the solid plate ($\eta\le1$). The wall thickness is computed from the stress across the seam: $t=pd/2\sigma_{all}\eta_l$ for the hoop stress acting across the longitudinal seam and $t=pd/4\sigma_{all}\eta_c$ for the axial stress across the girth seam. Use the larger.

## Q1 — State of stress at a point (easy)

![[SM-QB-3-mohr.png]]

At a point in a plate, $\sigma_x=80$ MPa, $\sigma_y=-40$ MPa and $\tau_{xy}=30$ MPa. Find the principal stresses and their orientation, the maximum in-plane shear stress, and the stresses on a plane rotated $30^\circ$ counter-clockwise from the $x$ axis.

> [!tip]- Hint
> Centre $=(\sigma_x+\sigma_y)/2$ and radius $R=\sqrt{((\sigma_x-\sigma_y)/2)^2+\tau_{xy}^2}$; then $\sigma_{1,2}=\text{centre}\pm R$.

> [!success]- Solution
> Centre $=20$ MPa, $R=\sqrt{60^2+30^2}=67.08$ MPa.
> $\sigma_1=\mathbf{87.1}$ MPa, $\sigma_2=\mathbf{-47.1}$ MPa, $\tau_{max}=R=\mathbf{67.1}$ MPa with $\sigma_{avg}=20$ MPa.
> $\tan2\theta_p=\dfrac{2(30)}{120}=0.5$, so $\theta_p=\mathbf{13.28^\circ}$ counter-clockwise from $x$ to the $\sigma_1$ plane; the maximum-shear planes are $45^\circ$ further, at $58.3^\circ$.
> At $\theta=30^\circ$: $\sigma=20+60\cos60^\circ+30\sin60^\circ=\mathbf{76.0}$ MPa; $\tau=-60\sin60^\circ+30\cos60^\circ=\mathbf{-37.0}$ MPa (magnitude 37.0). On the perpendicular plane ($120^\circ$): $\sigma=20-30-26.0=\mathbf{-36.0}$ MPa.
> **Check:** $76.0+(-36.0)=40=\sigma_x+\sigma_y$ ✓.

## Q2 — Shaft under axial load and torque (medium)

A solid steel shaft of 50 mm diameter ($\sigma_Y=280$ MPa) carries an axial tension of 60 kN and a torque of 1.2 kN·m. Find the principal stresses, the maximum shear stress, and the factor of safety by the Tresca and von Mises criteria. What would the maximum-normal-stress theory say?

> [!tip]- Hint
> $\sigma=P/A$ and $\tau=16T/\pi d^3$ at the surface. Then $\sigma_1,\sigma_2$ from Mohr's circle with $\sigma_y=0$.

> [!success]- Solution
> $A=1963.5$ mm², $\sigma=60\,000/1963.5=30.56$ MPa; $\tau=\dfrac{16(1.2\times10^6)}{\pi(50)^3}=48.89$ MPa.
> $\sigma_{1,2}=\dfrac{30.56}2\pm\sqrt{15.28^2+48.89^2}=15.28\pm51.22$, so $\sigma_1=\mathbf{66.5}$ MPa, $\sigma_2=\mathbf{-35.9}$ MPa; $\tau_{max}=\mathbf{51.2}$ MPa; $\theta_p=36.3^\circ$.
> Tresca: $\sigma_1-\sigma_2=102.4$ MPa, so $FS=280/102.4=\mathbf{2.73}$ (check also $\sigma_1-0$ and $0-\sigma_2$: smaller).
> Von Mises: $\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}=90.0$ MPa, so $FS=\mathbf{3.11}$. Shortcut: $\sqrt{\sigma^2+3\tau^2}=\sqrt{30.56^2+3(48.89)^2}=90.0$ ✓.
> Maximum normal stress: $FS=280/66.5=4.2$. For a **ductile** steel this is unsafe-sided: it ignores the shear that drives yielding.
> **Trap:** when $\sigma_1$ and $\sigma_2$ have the **same** sign, include $\sigma_3=0$ in the Tresca check (Q7). Here they have opposite signs, so $\sigma_1-\sigma_2$ is the governing difference.

## Q3 — Strain rosette (medium)

A 45° rosette on a steel surface ($E=200$ GPa, $\nu=0.3$) reads $\varepsilon_a=620$ ($0^\circ$), $\varepsilon_b=280$ ($45^\circ$), $\varepsilon_c=-150$ ($90^\circ$) in $\mu\varepsilon$. Find the principal strains and directions, the maximum shear strain, and the principal stresses. (Plane stress.)

> [!tip]- Hint
> $\varepsilon_x=\varepsilon_a$, $\varepsilon_y=\varepsilon_c$, $\gamma_{xy}=2\varepsilon_b-\varepsilon_a-\varepsilon_c$. Then use the strain circle, and Hooke's law in plane stress.

> [!success]- Solution
> $\gamma_{xy}=2(280)-620+150=\mathbf{90}\ \mu\varepsilon$. Centre $=235$, $R=\sqrt{385^2+45^2}=387.6$.
> $\varepsilon_1=\mathbf{622.6}$, $\varepsilon_2=\mathbf{-152.6}\ \mu\varepsilon$; $\tan2\theta_p=\gamma_{xy}/(\varepsilon_x-\varepsilon_y)=0.117$, so $\theta_p=\mathbf{3.3^\circ}$ from the $a$ axis. $\gamma_{max}=2R=\mathbf{775}\ \mu\varepsilon$.
> $\sigma_1=\dfrac{E}{1-\nu^2}(\varepsilon_1+\nu\varepsilon_2)=\dfrac{200\,000}{0.91}(622.6-45.8)\times10^{-6}=\mathbf{126.8}$ MPa; $\sigma_2=\dfrac{200\,000}{0.91}(-152.6+186.8)\times10^{-6}=\mathbf{7.5}$ MPa.
> Also $\tau_{xy}=G\gamma_{xy}=6.9$ MPa and thickness strain $\varepsilon_z=-\dfrac{\nu}{1-\nu}(\varepsilon_1+\varepsilon_2)=-201\ \mu\varepsilon$.
> **Check:** the gauges nearly coincide with the principal directions ($3.3^\circ$), so $\varepsilon_a\approx\varepsilon_1$ and $\varepsilon_c\approx\varepsilon_2$ ✓.

## Q4 — A strain gauge on a pressure vessel (medium)

A thin steel cylinder ($r=250$ mm, $t=5$ mm, $E=200$ GPa, $\nu=0.3$) has a gauge bonded at $30^\circ$ to the axis. It reads $300\ \mu\varepsilon$ under pressure. Find the pressure, the stresses and the hoop and axial strains.

> [!tip]- Hint
> Write $\varepsilon_h$ and $\varepsilon_L$ per unit pressure, then $\varepsilon_\theta=\varepsilon_L\cos^2\theta+\varepsilon_h\sin^2\theta$.

> [!success]- Solution
> Per MPa: $\sigma_h=r/t=50$, $\sigma_L=25$. $\varepsilon_h=\dfrac{50-0.3(25)}{200\,000}=212.5\ \mu\varepsilon$, $\varepsilon_L=\dfrac{25-0.3(50)}{200\,000}=50.0\ \mu\varepsilon$.
> $\varepsilon_{30}=50\cos^230^\circ+212.5\sin^230^\circ=37.5+53.1=90.6\ \mu\varepsilon$ per MPa.
> $p=300/90.6=\mathbf{3.31}$ MPa. $\sigma_h=\mathbf{165.5}$ MPa, $\sigma_L=\mathbf{82.8}$ MPa; $\varepsilon_h=703\ \mu\varepsilon$, $\varepsilon_L=166\ \mu\varepsilon$.
> **Check:** $r/t=50>10$, so the thin-wall theory is fine, and $\sigma_h=165$ MPa is below the yield of mild steel ✓.

## Q5 — Wall thickness with joint efficiency (medium)

A cylindrical vessel of inside diameter 1.2 m works at 2.5 MPa. The allowable stress is 110 MPa; the efficiency of the longitudinal seam is 0.7 and of the circumferential (girth) seam 0.5. Find the thickness. Compare with a seamless cylinder and a seamless sphere of the same diameter.

> [!tip]- Hint
> Hoop stress acts across the **longitudinal** seam, axial stress across the **girth** seam. Compute both and take the larger.

> [!success]- Solution
> Hoop: $t=\dfrac{pd}{2\sigma_{all}\eta_l}=\dfrac{2.5(1200)}{2(110)(0.7)}=\mathbf{19.5}$ mm.
> Axial: $t=\dfrac{pd}{4\sigma_{all}\eta_c}=\dfrac{2.5(1200)}{4(110)(0.5)}=13.6$ mm. **Use 20 mm** (the hoop condition governs).
> Seamless cylinder: $\dfrac{pd}{2\sigma_{all}}=13.6$ mm. Seamless sphere: $\dfrac{pd}{4\sigma_{all}}=\mathbf{6.8}$ mm, exactly half.
> **Insight:** the 30 % welded-joint penalty on the longitudinal seam costs 6 mm of steel. The sphere is the cheapest shape per unit volume.

## Q6 — Dimensional changes of a cylinder (medium)

A thin cylinder ($d=800$ mm, $t=8$ mm, $L=2$ m, $E=200$ GPa, $\nu=0.28$) is pressurised to 1.6 MPa. Find the stresses, the changes in diameter and length, the volume change, and the maximum shear stresses.

> [!tip]- Hint
> Use Hooke's law with the two stresses. $\Delta V/V=2\varepsilon_h+\varepsilon_L$.

> [!success]- Solution
> $\sigma_h=\dfrac{1.6(800)}{2(8)}=\mathbf{80}$ MPa, $\sigma_L=\mathbf{40}$ MPa.
> $\varepsilon_h=\dfrac{80-0.28(40)}{200\,000}=344\ \mu\varepsilon$, $\varepsilon_L=\dfrac{40-0.28(80)}{200\,000}=88\ \mu\varepsilon$.
> $\delta d=344\times10^{-6}(800)=\mathbf{0.275}$ mm, $\delta L=88\times10^{-6}(2000)=\mathbf{0.176}$ mm.
> $\dfrac{\Delta V}{V}=2(344)+88=776\ \mu\varepsilon$; $V=1005.3$ L, so $\Delta V=\mathbf{0.78}$ L (extra water to raise the pressure).
> In-plane max shear $=(80-40)/2=\mathbf{20}$ MPa; **absolute** maximum $=80/2=\mathbf{40}$ MPa (planes at $45^\circ$ about the longitudinal axis, between $\sigma_h$ and $\sigma_3=0$ at the free outer surface).

## Q7 — Absolute maximum shear (medium)

At a free surface $\sigma_x=-60$, $\sigma_y=-20$ and $\tau_{xy}=-25$ MPa. Find the in-plane principal stresses and both the in-plane and absolute maximum shear stresses.

> [!tip]- Hint
> Include $\sigma_3=0$ (free surface) when you order the three principal stresses.

> [!success]- Solution
> Centre $-40$ MPa, $R=\sqrt{20^2+25^2}=32.0$ MPa. $\sigma_1=\mathbf{-8.0}$, $\sigma_2=\mathbf{-72.0}$ MPa; $\theta_p=-64.3^\circ$ for $\sigma_1$.
> In-plane $\tau_{max}=\mathbf{32.0}$ MPa.
> Ordered: $0>-8.0>-72.0$, so $\tau_{abs}=\dfrac{0-(-72.0)}{2}=\mathbf{36.0}$ MPa, larger than the in-plane value because both in-plane principal stresses have the same sign.
> **Rule:** whenever $\sigma_1\sigma_2>0$ in plane stress, the true maximum shear is $\max(\lvert\sigma_1\rvert,\lvert\sigma_2\rvert)/2$.

## Q8 — Strain circle (easy)

A state of plane strain is $\varepsilon_x=400$, $\varepsilon_y=-200$, $\gamma_{xy}=300$ ($\mu\varepsilon$). Find the principal strains, the maximum shear strain and the normal strain along a direction $30^\circ$ counter-clockwise from $x$.

> [!tip]- Hint
> Same equations as stress, with $\gamma/2$ in place of $\tau$.

> [!success]- Solution
> Centre $=100$, $R=\sqrt{300^2+150^2}=335.4$. $\varepsilon_1=\mathbf{435}$, $\varepsilon_2=\mathbf{-235}\ \mu\varepsilon$; $\theta_p=\mathbf{13.3^\circ}$; $\gamma_{max}=2R=\mathbf{671}\ \mu\varepsilon$.
> $\varepsilon_{30}=100+300\cos60^\circ+150\sin60^\circ=\mathbf{380}\ \mu\varepsilon$.
> **Note:** this is Q1's stress state with every number multiplied by 5 ($\gamma/2$ in the place of $\tau$), so the circle has the same shape and the same $\theta_p=13.28^\circ$. That is the point of [[Stress-Strain Transformation Analogy]].

## Cross-links
Tutorial-style material: [[Principal Stresses to Principal Strains]] · before: [[Question Bank 2 - Beams, Bending and Shear]] · next: [[Question Bank 4 - Deflection, Energy and Columns]]
