---
tags: [concept, machine-drawing]
course: "Computer Aided Machine Drawing (ME3283)"
aliases: [Surface finish, Surface roughness, Ra, Rz, Machining symbols, Roughness symbols, Production drawing, Detail drawing, Title block, Machining allowance, Lay]
---

# Surface Finish, Machining Symbols and Production Drawings

> [!abstract] In one breath
> A machined surface is never smooth: it carries a texture left by the tool. **Surface roughness** measures that texture (most often as **$R_a$**, the mean height of the profile about its centre line), and a **symbol** on the drawing tells the machinist what texture to leave. A **production (detail) drawing** is the complete instruction to make one part: views, sizes, tolerances, finishes, material and notes.

Part of [[Computer Aided Machine Drawing - MOC]]. Previous: [[Limits, Fits and Tolerances]]. Next: [[Assembly Drawings, 3D Modelling and Bills of Materials]].

## 1. Measures of roughness

For a profile $y(x)$ measured from the mean line over a sampling length $L$:

$$
R_a=\frac1L\int_0^L|y|\,dx,\qquad R_q=\sqrt{\frac1L\int_0^Ly^2dx},\qquad R_z=\text{mean peak-to-valley height over five sampling lengths}
$$

$R_a$ is the average and hides single scratches; $R_z$ (and $R_{max}$) catches peaks and valleys. For a sine wave of amplitude $A$: $R_a=2A/\pi=0.637A$ and $R_z=2A$, so $R_z\approx3R_a$ for a smooth profile (about 4–7 for real machined surfaces).

![[CAMD-5-roughness.png]]

The profile above has $R_a=1.31\ \mu$m, $R_q=1.50\ \mu$m, $R_z\approx6.0\ \mu$m. The right panel shows what each process can reach.

**ISO roughness grades** (the old N numbers): N6 = 0.8 µm, N7 = 1.6, N8 = 3.2, N9 = 6.3, N10 = 12.5, N11 = 25, N12 = 50 µm $R_a$.

| Process | Typical $R_a$ (µm) | Where used |
| --- | --- | --- |
| Sand casting, flame cutting | 12.5–50 | non-functional surfaces |
| Drilling, rough milling | 3.2–12.5 | clearance holes |
| Turning, milling | 0.8–6.3 | general machined faces |
| Reaming | 0.8–3.2 | accurate holes |
| Grinding | 0.1–1.6 | bearing seats, sliding surfaces |
| Honing, lapping, polishing | 0.025–0.8 | cylinder bores, gauges, seals |

## 2. What decides the finish

For turning with a feed $f$ and a tool nose radius $r$ the ideal (geometrical) finish is the scallop left between two passes:

$$
R_{max}=\frac{f^2}{8r},\qquad R_a\approx\frac{f^2}{18\sqrt3\,r}
$$

**Example.** $f=0.2$ mm/rev, $r=0.8$ mm: $R_{max}=6.25\ \mu$m and $R_a=\mathbf{1.6\ \mu m}$. Halving the feed gives a quarter of the roughness. In practice the real finish is worse (tool wear, built-up edge, vibration), so the feed for a given finish is chosen from this relation and then confirmed ([[Tool Life and Machining Economics]]).

**Function:** bearing journals and seal surfaces need about $0.4$–$0.8\ \mu$m; running fits IT6–IT7 need $\approx0.8$ µm; cosmetic faces 3.2; castings as cast. Finer finishes cost much more (more operations): specify the **coarsest finish that works**. Roughness must also be a fraction of the tolerance: a rule of thumb is $R_z\le0.25\times$ the tolerance.

## 3. Surface texture symbols

The basic symbol is a check-mark ✓ (a 60° "V") touching the surface or its extension line, with:

| Variant | Meaning |
| --- | --- |
| ✓ with a bar | material **removal by machining** is required |
| ✓ with a circle | material removal is **prohibited** (as cast, as forged) |
| ✓ with a number | **maximum $R_a$** in µm (e.g. 1.6), or the N grade |
| Letters beside the symbol | **lay**: = parallel, ⊥ perpendicular, X crossed, M multi-directional, C circular, R radial |
| Value to the left, above | machining allowance (mm), sampling length |
| Symbol with a circle on the outline | the same finish on **all surfaces** of the part |

A drawing lists the general finish once (at the top right, "✓ 6.3 (✓ )") with exceptions marked on the individual surfaces. Old-style triangles ▽ (rough), ▽▽ (fine) ▽▽▽ (very fine) also appear on older drawings.

## 4. The production drawing

A **detail (production) drawing** gives everything the machinist needs for one part:

1. **Views:** the minimum number that defines the shape (usually front, top, a section), in first-angle projection with the symbol.
2. **Dimensions:** size, position and **datum** dimensions; each dimension once; chain, baseline or coordinate dimensioning chosen to avoid tolerance accumulation.
3. **Tolerances:** fits (H7, g6), limits, geometric tolerances ([[Metrology and GD&T - Form, Position and Gauging]]), general tolerance class.
4. **Surface texture** symbols and finishing notes (heat treatment, plating, coating, deburr).
5. **Title block:** part name, number, material (with specification), scale, projection symbol, units, drawn/checked/approved, date, revision, sheet size.
6. **Notes:** break all sharp edges 0.5 mm, unspecified radii R3, material and heat-treatment specifications, general tolerance ISO 2768-m.

**Machining allowances** are added to the casting or forging drawing (3–6 mm on rough sand castings) to be removed by machining; the **machine-shop** drawing then gives the finished size. **Manufacturing drawings** for the casting (pattern), the forging die and the machined part are separate sheets of the same component.

> [!warning] Traps
> - Quoting $R_a$ when a surface function depends on peaks ($R_z$, bearing area).
> - Specifying a finer finish than the tolerance can use: costs go up with no benefit.
> - Putting the surface symbol on the dimension line instead of the surface.
> - Forgetting that a *cast* surface needs a "no machining" symbol or an allowance.
> - Mixing up µm and µin (1 µm = 39.4 µin).

> [!question]- Predict first: a shaft seat needs Ra 0.8 µm. Can it be turned?
> Only with a fine feed and a good tool: $R_a=f^2/(18\sqrt3\,r)$ with $r=0.8$ mm gives 0.8 µm at $f=0.14$ mm/rev, but real finishes are poorer. Normally it is ground. Turning is the borderline of the range (0.8–6.3 µm).

> [!question]- Why is the finish symbol not placed on a centre line?
> Roughness belongs to a **surface**, not to a feature axis. The symbol touches the outline of the surface (or an extension line from it) pointing at the material side.

## 5. Connections

- [[Limits, Fits and Tolerances]] — the finish a tolerance grade needs and the fit it implies.
- [[Tool Life and Machining Economics]] and [[Orthogonal Cutting - Merchant's Shear Plane Model]] — the feed and tool geometry that produce $R_a$.
- [[Metrology and GD&T - Form, Position and Gauging]] — measuring roughness with a profilometer.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — the surface factor $k_a$ is a function of finish: a rougher surface has a lower endurance limit.
