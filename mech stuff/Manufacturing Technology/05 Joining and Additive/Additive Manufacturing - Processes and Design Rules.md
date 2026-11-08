---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Additive manufacturing, 3D printing, FDM, SLA, SLS, SLM, Powder bed fusion, Binder jetting, Directed energy deposition, Layer by layer]
---

# Additive Manufacturing — Processes and Design Rules

> [!abstract] In one breath
> Additive manufacturing (AM) **builds a part layer by layer from a 3-D model**, adding material instead of removing it. It trades speed and surface finish for **geometric freedom**: internal channels, lattices and consolidated assemblies come at no extra tooling cost. Knowing the seven process families and a handful of design rules is most of the subject.

Part of [[Manufacturing Technology - MOC]]. Previous: [[Joining Processes - Welding, Brazing and Adhesives]].

## 1. The workflow

CAD solid → **STL** (triangulated surface) → orient and add supports → **slice** into layers of thickness $t$ → toolpath → build → remove supports → post-process (heat treatment, machining, polishing).

## 2. Process families

| Family | Example | How a layer is made | Materials | Notes |
| --- | --- | --- | --- | --- |
| **Material extrusion** | FDM/FFF | heated nozzle lays down a filament | thermoplastics | cheap, visible layers, anisotropic |
| **Vat photopolymerisation** | SLA, DLP | UV light cures a resin layer | photopolymers | fine detail, smooth, brittle |
| **Powder bed fusion** | SLS (polymers), **SLM/DMLS/EBM** (metals) | laser or beam fuses a thin powder layer | nylon; steel, Ti, Al, Ni alloys | dense functional parts, residual stress |
| **Binder jetting** | | print binder on powder | sand, metal, ceramic | fast, sintering shrinks the part |
| **Material jetting** | | droplets of photopolymer | polymers | multi-material, colour |
| **Directed energy deposition** | LENS, WAAM | melts powder or wire as it is fed | metals | repair, large parts, rough |
| **Sheet lamination** | LOM | bond and cut sheets | paper, metal foil | low cost, limited accuracy |

## 3. Build time and layers

Number of layers $=H/t$ with $H$ the build height in the build direction. Metal powder-bed time is roughly the **recoating time per layer** times the layers plus the **melt time** (volume over a volumetric rate).

**Illustration.** A 60 mm tall part of 50 cm³, layer $t=0.04$ mm, recoat 10 s per layer, melt rate 10 cm³/h:

$$
\text{layers}=\frac{60}{0.04}=1500,\quad t_{recoat}=1500\times10\ \text{s}=4.2\ \text{h},\quad t_{melt}=\frac{50}{10}=5\ \text{h}\ \Rightarrow\ \approx9\ \text{h}
$$

Halving the layer thickness doubles the layer count and the recoat time. **Orientation** matters: lay a tall part down and the layer count falls, but the area per layer and the support volume rise.

## 4. Surface quality: the staircase effect

A surface inclined at angle $\theta$ to the horizontal is approximated by steps one layer high. The maximum **cusp height** (normal to the surface) is

$$
c=t\cos\theta
$$

a vertical wall ($\theta=90^\circ$) has no stair-step; a nearly horizontal surface ($\theta\to0$) has the full layer height. With $t=0.2$ mm and $\theta=30^\circ$: $c=0.17$ mm: visible, and removed by machining or polishing. Thinner layers and smaller inclination improve the finish; metal powder-bed parts typically have $R_a$ of 5–15 µm as built.

## 5. Design rules

- **Overhangs:** surfaces steeper than about 45° from the vertical (i.e. flatter than about 45° from horizontal) need **supports**; avoid them or reshape (teardrop holes instead of circles; chamfers instead of flat undersides).
- **Minimum features:** wall 0.4–1 mm (metals), hole 0.5 mm; leave **clearance** for powder removal from internal channels.
- **Anisotropy:** strength differs along and across layers (poor between layers for FDM; good for fused metal after HIP).
- **Residual stress and warping** in metal AM: rapid heating and cooling; control with support structures, preheating and stress-relief heat treatment before removing the part from the plate.
- **Porosity** and rough surface reduce **fatigue life** a lot: finish critical surfaces and use hot isostatic pressing (HIP) for aerospace parts.
- **Consolidate:** one printed part can replace an assembly, saving fasteners and joints.

**When to choose AM:** low volume, high complexity, customisation, lightweight lattice structure, prototypes. **When not:** large volume of simple shapes (casting, forging, machining win on cost per part), tight tolerance without post-machining.

> [!warning] Traps
> - Comparing AM and machining on a single part: AM has no tooling cost, but a **high cost per part** that does not drop with volume.
> - Ignoring orientation: it affects time, support, finish and strength simultaneously.
> - Taking as-built properties for wrought: porosity, anisotropy and residual stress differ.
> - Forgetting that sintering and binder-jet parts shrink 15–20 %: the model is scaled up.

> [!question]- Predict first: a 45° downward-facing surface and a horizontal downward-facing surface. Which needs supports?
> The horizontal one for sure (no material beneath the first layers). A 45° surface is at the limit; shallower than that needs support. This is why AM designs prefer self-supporting angles.

> [!question]- Why is the surface of a printed part rough on slanted faces but smooth on vertical walls?
> The stair-step cusp height is $t\cos\theta$: zero on a vertical wall and equal to the layer height on a near-horizontal face.

## 6. Connections

- [[Phase Diagrams - Lever Rule and the Iron-Carbide Diagram]] and [[Heat Treatment of Steel - TTT and CCT Diagrams]] — rapid solidification and reheating cycles give fine, non-equilibrium microstructures in metal AM.
- [[Thermal Stresses]] — layer-by-layer heating creates residual stress and warping.
- [[Heat Transfer - MOC]] — a moving melt pool: conduction into the substrate sets the cooling rate and the microstructure.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — surface roughness and defects govern fatigue of printed metal.
