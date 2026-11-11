---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Lewis equation, Spur gear strength, Gear tooth bending, Contact stress, Hertz stress in gears, AGMA]
---

# Spur Gear Design — Lewis Bending and Surface Stress

> [!abstract] In one breath
> A gear tooth fails two ways: it **breaks at the root** (bending fatigue, checked by the **Lewis equation**) or its **flank pits** (contact fatigue, checked by the **Hertz stress**). The geometry comes from [[Gear Formula Bank]]; here we need the load on the tooth and two stresses.

Part of [[Introduction to Machine Design - MOC]]. Previous: [[Bearings - Rolling Selection and Sliding Lubrication]]. Next: [[Helical Springs]].

## 1. Tooth load

Power $P$ at pitch-line velocity $V=\pi dn/60$ gives the **transmitted (tangential) load** $W_t=P/V=2T/d$. The tooth also carries a radial component $W_r=W_t\tan\phi$ (pressure angle $\phi$), so the normal load is $W_t/\cos\phi$. Only $W_t$ transmits power.

## 2. Lewis bending equation

Model the tooth as a cantilever of root thickness $t$ and height $h$ loaded at the tip with $W_t$:

$$
\sigma=\frac{6W_th}{bt^2}=\frac{W_t}{b\,m\,Y}\ \Rightarrow\
\sigma=K_v\frac{W_t}{b\,m\,Y},\qquad Y=\frac{t^2}{6hm}
$$

$b$ is the face width, $m$ the module, $Y$ the **Lewis form factor** (depends on tooth number and pressure angle: 20° full-depth: $N=17$: 0.303; 20: 0.322; 30: 0.359; 50: 0.409; 100: 0.447; rack 0.485). $K_v$ is the **velocity (dynamic) factor** that allows for impact as teeth engage:

$$
K_v=\frac{6.1+V}{6.1}\ (\text{cut or milled, }V\text{ in m/s}),\qquad
K_v=\frac{3.05+V}{3.05}\ (\text{cast})
$$

Full AGMA design multiplies by overload, size, load-distribution and rim factors and compares with a corrected bending strength; Lewis with $K_v$ is the first estimate. **Always check the weaker of pinion and gear**: they carry the same $W_t$, but the pinion has fewer teeth (smaller $Y$) so usually a higher stress.

## 3. Surface (contact) stress

Two teeth in contact at the pitch point act like two cylinders of radii $\rho_1=\tfrac{d_1}2\sin\phi$ and $\rho_2=\tfrac{d_2}2\sin\phi$ pressed with the normal load $F_n=W_t/\cos\phi$ over width $b$:

$$
\sigma_H=\sqrt{\frac{F_n}{\pi b}\,\frac{\dfrac1{\rho_1}+\dfrac1{\rho_2}}{\dfrac{1-\nu_1^2}{E_1}+\dfrac{1-\nu_2^2}{E_2}}}
$$

For through-hardened steel the allowable contact stress is roughly $\sigma_{H,all}\approx2.76\,H_B-70$ MPa for $10^7$ cycles. Durability (pitting) often governs before bending.

## 4. Worked example

Pinion $N_1=20$, gear $N_2=40$, $m=4$ mm, 20° full depth, face width $b=40$ mm, 7.5 kW at 1450 rpm (cut gears, steel).

| Quantity | Value |
| --- | --- |
| $d_1=mN_1$, $d_2$, centre distance | 80 mm, 160 mm, 120 mm |
| $V=\pi d_1n/60$ | 6.07 m/s |
| $W_t=P/V$ | **1235 N** |
| $K_v=(6.1+6.07)/6.1$ | 2.00 |
| $Y(20)=0.322$ | |
| Lewis $\sigma=K_vW_t/(bmY)$ | **47.8 MPa** |
| $\rho_1,\rho_2$ | 13.7 mm, 27.4 mm |
| normal load $W_t/\cos20^\circ$ | 1314 N |
| Hertz $\sigma_H$ ($E=207$ GPa, $\nu=0.3$) | **361 MPa** |

Bending is comfortable (48 MPa against hundreds). The contact stress of 361 MPa is within the roughly 620 MPa that a steel of 250 Brinell can take. Face width $b$ appears in both stresses: widening the gear is the cheap way to buy durability.

![[MD-4-gears.png]]

**Design loop.** Choose the module from the required centre distance and strength; use at least 17–18 teeth on the pinion to avoid undercutting (interference limits are in the [[Gear Formula Bank]]); take a face width of about 8–12 modules ($3$–$5$ circular pitches); then check bending and contact for **both** pinion and gear.

> [!warning] Traps
> - Using the power-dependent $W_t$ with the *normal* load in the Lewis formula: Lewis uses $W_t$ only.
> - Taking $Y$ from the gear, not the pinion, when finding the weakest tooth (compute both).
> - Using $V$ in ft/min with the SI $K_v$ formula.
> - Treating $\sigma_H$ as a bending-type stress: it is a compressive contact stress below the surface.
> - Forgetting that $m$ in the Lewis formula is in metres when $b$ and $W_t$ are in newtons and metres.

> [!question]- Predict first: double the face width. What happens to the Lewis stress and the Hertz stress?
> Lewis stress is $\propto1/b$: halves. Hertz stress is $\propto1/\sqrt b$: falls by 29 %. Contact stress is less sensitive to width.

> [!question]- Why does the pinion usually fail first?
> It has fewer teeth (so a smaller $Y$ and a thinner root), it rotates faster so its teeth see more stress cycles, and it has a smaller radius of curvature, raising the contact stress. Pinions are usually made harder.

## 5. Connections

- [[Gear Formula Bank]] and [[Tutorial-7-solution]] — tooth geometry, interference and contact ratio (the load is shared by $m_c>1$ pairs, which lowers the real load).
- [[Plane Stress Transformation]] — Hertz stress is a subsurface shear problem: the maximum shear lies below the surface.
- [[Shaft Design - Static and Fatigue Loading]] — $W_t$ and $W_r$ load the shaft.
- [[Gears, Transformers and Reflected Impedance]] — $W_tV=P$ is power conservation, the same statement as $VI$ across an ideal transformer.
