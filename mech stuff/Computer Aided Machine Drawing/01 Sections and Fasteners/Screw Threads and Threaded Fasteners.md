---
tags: [concept, machine-drawing]
course: "Computer Aided Machine Drawing (ME3283)"
aliases: [Screw threads, ISO metric thread, Thread terminology, Bolts nuts and screws, Thread representation, Washers, Locking devices, Pitch, Lead]
---

# Screw Threads and Threaded Fasteners

> [!abstract] In one breath
> A screw thread is a helical ridge. Drawing it exactly is pointless, so drawings use a **conventional representation**: the major diameter as a thick line, the minor diameter as a thin line. The thread is **specified by its designation** (e.g. M12 × 1.75) and every other dimension is read from standard tables or computed from $d$ and the pitch.

Part of [[Computer Aided Machine Drawing - MOC]]. Previous: [[Sectional Views and Hatching Conventions]]. Next: [[Keys, Rivets and Welds]]. Strength side: [[Bolted Joints - Preload and Joint Stiffness]].

## 1. Terminology

| Term | Meaning |
| --- | --- |
| **Major (nominal) diameter** $d$ | largest diameter of an external thread (crest) |
| **Minor (core) diameter** $d_1$ | smallest diameter (root of an external thread) |
| **Pitch diameter** $d_2$ | the diameter where the thread width equals the space width |
| **Pitch** $P$ | axial distance between adjacent crests |
| **Lead** $L$ | axial advance in one turn: $L=n\,P$ ($n$ starts) |
| **Crest, root, flank** | the top, the bottom and the sloping sides |
| **Thread angle** | 60° for ISO metric and unified threads, 55° for Whitworth |
| **Right-hand** | tightens when turned clockwise (standard) |

## 2. The ISO metric thread

Fundamental triangle height $H=0.866\,P$; the crest is truncated by $H/8$ and the root by $H/4$ so the working depth is $5H/8=0.541P$.

$$
d_2=d-0.6495P,\qquad d_1=d-1.0825P\ (\text{nut minor }D_1),\qquad A_t=\frac\pi4(d-0.9382P)^2\ (\text{tensile stress area})
$$

![[CAMD-2-threads.png]]

**M12 × 1.75:** $H=1.52$ mm, $d_2=10.86$ mm, $d_1=10.11$ mm (root diameter of the bolt $=d-1.2269P=9.85$ mm), $A_t=84.3$ mm².

| Designation | Coarse pitch $P$ (mm) | $A_t$ (mm²) |
| --- | --- | --- |
| M6 | 1.0 | 20.1 |
| M8 | 1.25 | 36.6 |
| M10 | 1.5 | 58.0 |
| M12 | 1.75 | 84.3 |
| M16 | 2.0 | 156.7 |
| M20 | 2.5 | 244.8 |
| M24 | 3.0 | 352.5 |

Written **M12** for the coarse thread and **M12 × 1.25** for a fine thread. Fine threads have a larger $A_t$ (M12 × 1.25: 92.1 mm², +9 %), a smaller helix angle (they loosen less under vibration) and a finer adjustment, but strip more easily and cross-thread. Other forms: **square** and **ACME** (power screws, jacks, lead screws), **buttress** (one-directional heavy load), BSW, BSP (pipes), NPT.

## 3. How to draw a thread (convention)

- **External thread (bolt, stud):** the crest line (major diameter) is a thick continuous line; the root line (minor diameter) is a thin continuous line, drawn at about $0.8d$ from the axis. In the end view the root circle is a thin **three-quarter circle**; the thread end (limit of full thread) is a thick line across.
- **Internal thread (tapped hole):** in a section the minor diameter is thick and the major diameter thin; in the end view the major circle is the three-quarter thin one.
- **Threaded length:** to a thick line. **Undercut or runout** at the end of the thread is shown by a short thin taper.
- A tapped hole is drilled deeper than the threaded length (the drill depth is about the thread length plus 0.5 d).

## 4. Fasteners and their proportions

Hexagonal **bolt**: head across flats $s\approx1.5d+3$ mm (across corners $\approx1.155\,s$), head height $k=0.7d$, chamfer 30° on the corners. **Nut**: thickness $m=0.8d$, same across-flats as the head. For M12: $s=21$ mm, $k=8.4$ mm, $m=9.6$ mm (the exact standards give 18–19 mm across flats for M12; drawing proportions are approximations: follow the course book or the ISO table).

| Item | Role |
| --- | --- |
| **Bolt and nut** | passes through the parts and is clamped by the nut |
| **Stud** | threaded both ends, one end screwed into a tapped hole (cylinder heads, for parts that are frequently removed) |
| **Cap screw, machine screw** | screws into a tapped hole; head types: hexagon socket, cheese, pan, countersunk |
| **Set screw** | locks a hub on a shaft |
| **Washer** | spreads the load, protects the surface, can lock (spring washer) |
| **Locking devices** | lock nut (jam nut), castle nut with split pin, spring or tab washer, Nyloc nut, wire locking: stop loosening from vibration |

**Selection from the hole:** clearance hole $\approx d+1$ (medium fit: M12 → 13.5 mm); tapping drill $=d-P$ (M12: 10.25 mm).

> [!warning] Traps
> - Showing the thread as a plain cylinder: the thin root line is what says "thread".
> - Drawing the root circle as a full circle instead of three-quarters.
> - Reversing the thick/thin pairs for an internal thread.
> - Using the nominal diameter for strength: stress is computed on $A_t$.
> - Forgetting that the designation, not the drawing, fixes the pitch: M12 means 1.75 unless stated.

> [!question]- Predict first: an M12 and an M12 × 1.25 bolt carry the same tension. Which has the lower thread stress, and why?
> The fine thread: its tensile stress area is larger (92 against 84 mm²), so the stress is 8 % lower. The coarse thread is stronger against **stripping** of the nut because its thread is deeper.

> [!question]- Why are bolts and screws in a sectioned assembly not hatched?
> They are standard solid items cut along their axis. Hatching would suggest solid mass, the same as the plates around them: by convention bolts, nuts, screws and washers are shown as plain views.

## 5. Connections

- [[Bolted Joints - Preload and Joint Stiffness]] — the load analysis using $A_t$, preload and stiffness.
- [[Sectional Views and Hatching Conventions]] — a bolt in section is not hatched.
- [[Kinematic Pairs, Links and Chains]] — a screw is a helical pair, 1 DOF, where rotation and translation are tied by the lead.
- [[Keys, Rivets and Welds]] and [[Assembly Drawings, 3D Modelling and Bills of Materials]] — the other joints and how they are listed.
