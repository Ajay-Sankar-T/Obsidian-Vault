---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Keys, Sunk key, Key design, Flange coupling, Rigid coupling, Shaft coupling]
---

# Keys and Couplings

> [!abstract] In one breath
> A **key** transmits torque between shaft and hub. It is loaded in **shear** across its length and **crushing** on half its height. The key is deliberately the weak link: designed to fail before the shaft or the hub. A **coupling** joins two shafts; its bolts carry the torque in shear.

Part of [[Introduction to Machine Design - MOC]]. Previous: [[Shaft Design - Static and Fatigue Loading]]. Next: [[Bearings - Rolling Selection and Sliding Lubrication]].

## 1. Key types

| Key | Use |
| --- | --- |
| **Sunk (rectangular or square)** | the standard: width $b$, thickness $t$ in a keyway cut half in the shaft, half in the hub |
| Gib-head | taper key that can be driven in and withdrawn from one side |
| Woodruff | semicircular key in a circular groove; self-aligning, for small torques and tapered shafts |
| Feather | allows the hub to slide along the shaft while transmitting torque |
| Splines | many keys cut in the shaft: high torque, hub can slide |

Standard widths follow the shaft diameter; a common rule is $b\approx d/4$ and $t\approx d/6$ for a rectangular key. For $d=38$–44 mm the preferred key is $12\times8$.

## 2. Loads on the key

The torque $T$ acts at the shaft surface, so the tangential force on the key is $F=T/(d/2)$.

$$
\tau=\frac{F}{bL}\le\frac{S_{sy}}{n}\ \ (\text{shear, } S_{sy}=0.577S_y),\qquad
\sigma_c=\frac{F}{(t/2)L}=\frac{2F}{tL}\le\frac{S_y}{n}\ \ (\text{crushing})
$$

Check both and take the longer length. For a **square** key ($b=t$) with $S_{sy}=0.577S_y$, crushing governs because $2/t$ against $1/b$ with $0.577$ makes crushing about 15 % worse than shear.

**Equal-strength length.** If the key is to be as strong in shear as the shaft in torsion:

$$
\tau\,bL\,\frac d2=\tau\,\frac{\pi d^3}{16}\ \Rightarrow\ L=\frac{\pi d^2}{8b}
$$

which is $L=\pi d/2=1.57\,d$ for $b=d/4$. Hubs are typically $1.25$–$1.5\,d$ long, so keys are usually shorter than equal strength and the key is the weaker part.

## 3. Worked example

$T=143$ N·m on a Ø40 shaft, key $12\times8$ in a steel with $S_y=300$ MPa ($S_{sy}=173$ MPa), $n=2$:

$$
F=\frac{143.2}{0.020}=7160\ \text{N},\quad
L_{shear}=\frac{Fn}{bS_{sy}}=6.9\ \text{mm},\quad
L_{crush}=\frac{2Fn}{tS_y}=\mathbf{11.9\ mm}
$$

Crushing governs (11.9 mm against 6.9 mm). A practical key $12\times8\times40$ has $\tau=14.9$ MPa ($n=11.6$) and $\sigma_c=44.8$ MPa ($n=6.7$): very safe; the equal-strength length would be $\pi d^2/8b=52$ mm. This torque (143 N·m) is small for a Ø40 shaft, hence the generous factors.

![[MD-2-key.png]]

## 4. Flange coupling

Two flanges bolted together, bolts on a pitch circle $D_p$. Bolts in shear carry the torque:

$$
T=n_b\,\frac{\pi d_b^2}{4}\,\tau_b\,\frac{D_p}{2}\ \Rightarrow\
d_b=\sqrt{\frac{8T}{\pi n_b\tau_bD_p}}
$$

Example: 4 bolts on a 100 mm pitch circle, $\tau_b=40$ MPa, $T=143$ N·m: $d_b=4.8$ mm, so M6 bolts (and then check the bolts in bearing against the flange).

Other couplings: **flexible** (rubber bush, jaw, gear) to tolerate misalignment and damp shock; **Oldham** and **universal** joints for offset or angled shafts: [[Kinematic Inversion - Slider-Crank and Double-Slider Families]].

> [!warning] Traps
> - Using the shaft radius for the lever arm of the key: it is at the surface, $d/2$.
> - Checking only shear: crushing usually governs for short deep keys.
> - Using the full thickness $t$ for the bearing area: only half the key sits against each side, $t/2$.
> - Forgetting that the keyway weakens the shaft (stress concentration, see [[Shaft Design - Static and Fatigue Loading]]).
> - Treating the key as a bolt with a preload: a sunk key is loaded purely by contact.

> [!question]- Predict first: halve the key length. How does the shear stress change?
> $\tau=F/(bL)$ so it **doubles**, and the crushing stress doubles too. Doubling the width changes only the shear.

> [!question]- Why is a key made of a *softer* steel than the shaft?
> So the key yields or shears before the shaft or hub are damaged: a cheap, replaceable fuse. Feather and Woodruff keys are the same idea.

## 5. Connections

- [[Power Transmission by Shafts]] — $T=P/\omega$ fixes the key force.
- [[Torsion of Circular Shafts]] — the equal-strength length compares the key's shear with $\tau=16T/\pi d^3$.
- [[Statically Indeterminate Axial Members]] — in a bolted coupling the bolts share the torque by compatibility: the loaded flange rotates slightly and each bolt takes force in proportion to its radius.
- [[Computer Aided Machine Drawing - MOC]] — key and keyway proportions and symbols as drawn.
