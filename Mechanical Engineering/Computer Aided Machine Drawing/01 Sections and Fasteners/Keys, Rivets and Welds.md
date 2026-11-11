---
tags: [concept, machine-drawing]
course: "Computer Aided Machine Drawing (ME3283)"
aliases: [Keys, Keyways, Rivets, Riveted joints, Welding symbols, Weld symbols, Fillet weld, Lap joint, Butt joint, Cotter, Pins]
---

# Keys, Rivets and Welds

> [!abstract] In one breath
> Three ways to connect parts, each with its own drawing rules. A **key** locks a hub to a shaft and is proportioned from the shaft diameter. A **rivet** is a permanent headed pin set by hammering a second head, proportioned from the rivet diameter. A **weld** is shown not as a drawing of the bead but as a **symbol** on a reference line that says what, where, how big.

Part of [[Computer Aided Machine Drawing - MOC]]. Previous: [[Screw Threads and Threaded Fasteners]]. Next: [[Limits, Fits and Tolerances]]. Strength design: [[Keys and Couplings]], [[Joining Processes - Welding, Brazing and Adhesives]].

## 1. Keys

| Key | Proportions (shaft diameter $d$) | Use |
| --- | --- | --- |
| **Rectangular sunk** | width $b=d/4$, thickness $t=d/6$, length $\approx1.5d$ | general |
| **Square sunk** | $b=t=d/4$ | small shafts |
| **Taper (gib-head)** | taper 1 in 100 on the top | driven in, withdrawn from one side |
| **Woodruff** | segment of a disc in a circular keyway | tapered shafts, small torques |
| **Feather** | sliding, fixed to the shaft | hub that moves along the shaft |
| **Spline** | many keys in one | high torque, sliding |

In the drawing the **keyway** is cut half in the shaft (depth $t/2$) and half in the hub. In an end view of a Ø40 shaft: key 10 × 6.7 mm (nearest standard: 12 × 8 for 38–44 mm shafts), hub length $1.5d=60$ mm. A key cut by a lengthwise section is **not hatched**. The designation reads like "Key 12 × 8 × 40 IS 2048".

![[CAMD-3-keys-rivets.png]]

## 2. Rivets and riveted joints

A rivet has a head, a shank of diameter $d$, and a tail that is hammered into a second head. **Snap head** (the standard for boilers and structures) proportions: head diameter $1.6d$, height $0.7d$. A rivet **hole** is $d+1.5$ mm (for $d\ge12$ mm).

**Joints:** **lap** (plates overlap) or **butt** (plates meet, with one or two cover plates); **single-, double-, triple-riveted**; rows **chain** (rivets in line) or **zig-zag**. Unwin's rule for the rivet diameter from the plate thickness $t$: $d=6\sqrt t$ (mm). Rules of thumb: **pitch** $p\ge3d$ (minimum, to avoid tearing the plate), **margin** (hole centre to plate edge) $=1.5\,d_{hole}$, **back pitch** (between rows) $\approx0.7p$.

**Failure modes** of a single-riveted lap joint (per pitch): tearing of the plate between holes $(p-d_h)t\sigma_t$; shearing of the rivet $\frac\pi4d_h^2\tau$ (double shear for a butt joint with two cover plates doubles this); crushing of the plate or rivet $d_ht\sigma_c$; also shearing of the plate edge and rivet-head failure, avoided by the margin. The **efficiency** is the weakest of these over the strength of the plate $pt\sigma_t$.

**Example.** $t=10$ mm: $d=6\sqrt{10}=19$ mm, hole 20.5 mm, $p=60$ mm; $\sigma_t=100$, $\tau=60$, $\sigma_c=150$ MPa.

| Failure | Strength (N) |
| --- | --- |
| tearing $(60-20.5)(10)(100)$ | 39 500 |
| **shearing** $\frac\pi4(20.5)^2(60)$ | **19 800** |
| crushing $(20.5)(10)(150)$ | 30 750 |
| plate $60\times10\times100$ | 60 000 |

Efficiency $=19\,800/60\,000=\mathbf{33\ \%}$ (shear governs). Double-riveting or a butt joint with double shear raises it; a pitch change moves the balance between tearing and shearing.

**Drawing:** rivets are shown with their heads; in a section they are **not hatched**; a symbol in a plan view (a cross or a filled circle) marks the position, with the pitch dimensioned.

## 3. Welds and welding symbols

A **weld symbol** sits on a **reference line** attached to an **arrow** that points to the joint, with an optional **tail** for process notes.

| Element | Meaning |
| --- | --- |
| Symbol **below** the reference line | weld on the **arrow side** of the joint |
| Symbol **above** the line | weld on the **other side** |
| Fillet (right triangle ◿) | the standard weld in a T or lap joint; leg size written to the **left** of the symbol |
| Groove symbols: square, V, bevel, U, J | butt joints prepared to different edges; thicker plates use V or U |
| Circle at the arrow bend | weld **all around** |
| Flag | **field weld** (made on site) |
| Number after the symbol | length (and pitch for intermittent welds: 50 − 150) |
| Spot, seam | resistance welds |

**Fillet weld size.** The **leg** $s$ is drawn and written; the **throat** (the load-bearing section) is $0.707\,s$. Strength per unit length $=0.707\,s\,\tau_{all}$: for $s=6$ mm and $\tau_{all}=80$ MPa that is **339 N/mm**, so 100 mm of weld carries 33.9 kN. Other joint types: butt (square-edged for thin plate), lap, T, corner and edge.

> [!warning] Traps
> - Using the **leg** instead of the **throat** for fillet-weld strength.
> - Putting the symbol on the wrong side of the reference line.
> - Hatching a rivet or a key in a lengthwise section.
> - Taking the rivet diameter from the *hole* diameter in the strength formulas (use the hole, which is what the metal fills).
> - Ignoring the margin: a rivet too near the edge can shear out of the plate.

> [!question]- Predict first: a rivet joint in which shearing governs. Does a wider pitch increase the joint efficiency?
> No, it falls. Widening the pitch from 60 to 90 mm leaves the shear strength per pitch at 19.8 kN but raises the plate strength $pt\sigma_t$ to 90 kN, so the efficiency drops from 33 % to 22 %. It rises only if the shear strength per pitch rises (more rivets, double shear).

> [!question]- Why is the throat, not the leg, the design dimension of a fillet weld?
> The weld fails along its shortest section, which is the throat: the perpendicular from the root to the hypotenuse, $0.707\,s$ for an equal-leg fillet.

## 4. Connections

- [[Keys and Couplings]] — the shear and crushing checks on the key.
- [[Joining Processes - Welding, Brazing and Adhesives]] — the processes, heat input and HAZ behind a weld symbol.
- [[Bolted Joints - Preload and Joint Stiffness]] — the alternative detachable joint.
- [[Sectional Views and Hatching Conventions]] — keys, rivets and bolts are not hatched when cut lengthwise.
