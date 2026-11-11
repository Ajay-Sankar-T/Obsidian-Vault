---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Sheet metal, Blanking, Piercing, Bending, Springback, Bend allowance, Deep drawing, Limiting draw ratio, Stamping]
---

# Sheet Metal Forming — Blanking, Bending and Deep Drawing

> [!abstract] In one breath
> Sheet-metal parts come from three basic moves: **shear** the sheet (blanking, piercing), **bend** it, or **draw** it into a cup. Each has one governing number: **cutting clearance**, **bend allowance** (flat length), and **draw ratio** (how much blank diameter you can pull in).

Part of [[Manufacturing Technology - MOC]]. Previous: [[Bulk Deformation - Forging, Rolling, Extrusion and Drawing]]. Next: [[Orthogonal Cutting - Merchant's Shear Plane Model]].

## 1. Blanking and piercing

A punch pushes through the sheet against a die: the metal yields, then fractures. *Blanking* keeps the cut-out piece, *piercing* keeps the sheet with the hole.

$$
F=\tau\,L\,t\approx0.7\,\text{TS}\;L\,t\qquad(L=\text{cut perimeter})
$$

**Clearance** $c$ between punch and die is typically 5–10 % of the thickness per side. Too little: secondary shear and fast die wear. Too much: burrs and a rolled edge. For blanking, the **die** is made to the part size and the punch smaller; for piercing, the **punch** is the hole size and the die larger.

**Example.** A Ø40 hole in 2 mm sheet, TS $=400$ MPa: $L=\pi(40)=125.7$ mm, $F=0.7(400)(125.7)(2)=\mathbf{70\ kN}$, clearance $7.5\,\%\times2=0.15$ mm per side. Shear (angled) edges on the punch spread the cut over a longer time and lower the peak force.

## 2. Bending

The outside of a bend is stretched and the inside compressed; between them lies a **neutral axis**, whose length does not change, at a distance $Kt$ from the inside ($K\approx0.33$ for tight bends, 0.5 for large radii).

**Bend allowance** (arc length of the neutral axis, the flat length used by the bend):

$$
BA=\alpha\,(R+Kt),\qquad\alpha\ \text{in radians}
$$

Flat blank length = sum of straight segments + all bend allowances. Example: $t=2$ mm, inner radius $R=4$ mm, $K=0.4$, 90°: $BA=\tfrac\pi2(4+0.8)=\mathbf{7.54\ mm}$.

**Minimum bend radius** (to avoid cracking the outside): about $R_{min}\ge$ 0.5t–2t for annealed ductile metals, more for hard tempers and along the rolling direction.

**Springback.** Elastic recovery after the load is removed opens the angle. The part must be **over-bent** by the springback angle, which is larger for high yield stress and a large $R/t$ ratio:

$$
\frac{R_i}{R_f}=4\Big(\frac{R_iS_y}{Et}\Big)^3-3\Big(\frac{R_iS_y}{Et}\Big)+1
$$

($R_i$ before, $R_f$ after unloading; a tighter bend springs back less.)

**V-bending force:** $F=\dfrac{k\,\text{TS}\,w\,t^2}{D}$ with $k\approx1.33$ for a V-die, $D$ the die opening (typically $16t$) and $w$ the bend length. Example: $t=2$ mm, $w=100$ mm, $D=32$ mm, TS $=400$ MPa: $F=1.33(400)(100)(4)/32=\mathbf{6.65\ kN}$.

## 3. Deep drawing

A flat blank is drawn by a punch through a die into a cup. The **blank holder** presses the flange to stop wrinkles. The wall is under tension and the flange under compression and shear.

**Blank diameter** from constant surface area (thickness unchanged): for a cylindrical cup of diameter $d$ and height $h$,

$$
\frac{\pi D_0^2}{4}=\frac{\pi d^2}{4}+\pi dh\ \Rightarrow\ D_0=\sqrt{d^2+4dh}
$$

**Draw ratio** $DR=D_0/d$; the limiting value for a single draw is $LDR\approx2.0$ (the wall cannot carry more force than the cup base can transmit, so it tears). Drawing force:

$$
F=\pi d\,t\,\text{TS}\,\Big(\frac{D_0}{d}-0.7\Big)
$$

**Example.** Cup $d=50$ mm, $h=40$ mm, $t=1$ mm, TS $=300$ MPa: $D_0=\sqrt{50^2+4(50)(40)}=\mathbf{102.5\ mm}$ (blank area equals the cup area, $8247$ mm²), $DR=2.05$ (just above the limit: use a second draw, or reduce $h$), $F=\pi(50)(1)(300)(2.05-0.7)=\mathbf{63.6\ kN}$.

![[MFG-3-sheet.png]]

**Other sheet processes.** Stretch forming (strains the whole sheet over a die), spinning, hydroforming, and incremental forming. **Formability** is shown by the **forming limit diagram**: the major and minor true strains at which necking starts. A high strain-hardening exponent $n$ and high plastic anisotropy $R$ help stretching and drawing respectively.

> [!warning] Traps
> - Measuring the neutral axis from the outside of the bend: $Kt$ is measured from the **inside** surface.
> - Using the tensile strength for blanking: the cut is shear, $\approx0.7$ TS.
> - Leaving the cup base out of the blank-area balance: the blank area equals the base plus the wall.
> - Ignoring springback: the finished angle is larger than the die angle.
> - Applying $LDR=2$ to every material (it depends on $R$ and friction).

> [!question]- Predict first: a part is bent to 90° in a tool that makes a perfect 90° die angle. Is the part 90°?
> No: after the punch retracts the part springs back (a few degrees for mild steel, more for stainless or high-strength sheet), so the tool must over-bend by that angle, or the part must be coined (compressed at the bottom of the stroke).

> [!question]- How do you reduce the punch force in blanking without changing the part?
> Bevel the punch face (shear angle) so only part of the perimeter cuts at a time, or stagger multiple punches. The same energy is spent over a longer stroke: lower peak force, a quieter press.

## 4. Connections

- [[Tensile Test, True Stress-Strain and Hardness]] — TS, $n$ and the shear strength used throughout.
- [[Bulk Deformation - Forging, Rolling, Extrusion and Drawing]] — constant-volume plasticity applies as well; deep drawing keeps the surface area, not the volume.
- [[Flexure Formula]] and [[Shear Force and Bending Moment Diagrams]] — the elastic stress distribution that gives the neutral axis; the plastic bend moves it to the inside.
- [[Static Failure Theories - Tresca and von Mises]] — shear at yield: $\tau_y=0.5S_y$ (Tresca) or $0.577S_y$ (von Mises).
