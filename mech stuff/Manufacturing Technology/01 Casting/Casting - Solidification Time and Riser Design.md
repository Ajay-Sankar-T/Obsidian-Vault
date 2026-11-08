---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Casting, Chvorinov's rule, Riser design, Solidification time, Gating, Sand casting, Die casting, Investment casting]
---

# Casting — Solidification Time and Riser Design

> [!abstract] In one breath
> Casting pours molten metal into a cavity and lets it freeze. Two things decide whether the part is sound: **the metal must fill the cavity** (gating) and **the last metal to freeze must be able to feed the shrinkage** (risers). Both come from simple rules: Bernoulli for filling and **Chvorinov's rule** for freezing.

Part of [[Manufacturing Technology - MOC]]. Next: [[Bulk Deformation - Forging, Rolling, Extrusion and Drawing]].

## 1. Processes

| Process | Mould | Typical use | Tolerance, finish |
| --- | --- | --- | --- |
| **Sand casting** | expendable sand, pattern reusable | engine blocks, large parts, one-offs | ±1 mm, rough |
| **Investment (lost wax)** | expendable ceramic shell on a wax pattern | turbine blades, jewellery, complex thin parts | ±0.1 mm, fine |
| **Die casting** | reusable steel die, pressure injection | zinc, aluminium and magnesium housings | ±0.1 mm, good |
| **Permanent mould** | reusable metal mould, gravity | pistons, wheels | ±0.3 mm |
| **Centrifugal** | spinning mould | pipes, rings | good density |

Steps: pattern (larger than the part by the **shrinkage allowance**, with draft for withdrawal), mould and cores for cavities, melting and pouring, solidification, removal, cleaning and heat treatment.

## 2. Filling: gating

Bernoulli from the pouring basin to the gate: $v=\sqrt{2gh}$. The flow rate is $Q=Av$ with $A$ the smallest (choke) area, and the fill time is $t_f=V/Q$.

**Example.** A casting of volume $2\times10^{-3}$ m³ with a gate area $A=300$ mm² under a head $h=0.3$ m:

$$
v=\sqrt{2(9.81)(0.3)}=2.43\ \text{m/s},\quad Q=3\times10^{-4}(2.43)=7.3\times10^{-4}\ \text{m}^3/\text{s},\quad t_f=\frac{2\times10^{-3}}{7.3\times10^{-4}}=\mathbf{2.7\ s}
$$

A sprue is tapered so the stream stays attached and does not entrain air; a velocity above about 1–2 m/s at the gate causes turbulence and slag.

## 3. Solidification: Chvorinov's rule

Heat leaves through the mould surface; the metal volume holds the heat. Hence

$$
t_s=B\Big(\frac VA\Big)^2
$$

with $V/A$ the **casting modulus** (volume over the *cooling* surface area) and $B$ a mould constant (about 2 s/mm² for sand moulds; the book value varies with metal and mould). The **square** matters: doubling $V/A$ makes the part take four times as long.

For the same volume of $10^6$ mm³ (with $B=2$ s/mm²):

| Shape | $V/A$ | $t_s$ |
| --- | --- | --- |
| sphere | 20.7 mm | 14.3 min |
| cylinder, $D=H$ | 18.1 mm | 10.9 min |
| cube | 16.7 mm | 9.3 min |
| plate 200×200×25 | 10.0 mm | 3.3 min |

The sphere has the smallest surface and freezes last; thin sections freeze first. **Directional solidification** (freeze the far end first, the section next to the riser last) lets the riser feed liquid metal to every part. Use **chills** to speed the far end and **padding** (thickening sections toward the riser).

![[MFG-1-casting.png]]

## 4. Riser design

The riser (feeder) must freeze **after** the casting: $t_{riser}\ge1.25\,t_{casting}$ (a safety margin of about 25 %), and must hold enough liquid to supply the solidification shrinkage.

**Example.** Steel plate $200\times200\times50$ mm: $V=2\times10^6$ mm³, $A=1.2\times10^5$ mm², $V/A=16.7$ mm, $t_s=9.3$ min.

- A cylindrical riser with $H=D$ (top and sides cooling, base attached) has $V/A=D/6$.
- Solidification condition: $(D/6)^2\ge1.25\,(16.7)^2$, so $D\ge6(1.118)(16.7)=\mathbf{112\ mm}$, riser volume $1.10\times10^6$ mm³.
- Volume condition: steel shrinks about 3 % on solidification: $0.03\times2\times10^6=6\times10^4$ mm³; a riser delivers about 14 % of its volume, so it needs $4.3\times10^5$ mm³: satisfied with margin.

The **freezing condition governs**. Place the riser on the thick section, size it by modulus, and check the volume.

## 5. Defects

| Defect | Cause | Remedy |
| --- | --- | --- |
| **Shrinkage cavity** | liquid not fed to the last-freezing region | riser, chills, directional solidification |
| Gas porosity | dissolved gas, trapped air, wet sand | degas, vent, dry moulds |
| Misrun, cold shut | metal freezes before filling, or two streams do not fuse | higher pour temperature, thicker section, faster fill |
| Hot tear | restrained contraction while weak | fillets, collapsible cores |
| Inclusions, slag | oxides or mould erosion | filters, clean gating |

> [!warning] Traps
> - Using the total surface area in $V/A$: only the area through which heat leaves counts (not the surface under the riser).
> - Forgetting the 25 % margin: a riser with the same modulus as the casting freezes at the same time and cannot feed.
> - Thinking a bigger riser is always better: it wastes metal and can create a hot spot.
> - Using the wrong exponent: $t\propto(V/A)^2$ rather than $V/A$.

> [!question]- Predict first: cast a cube of side $a$ and a sphere of diameter $a$. Which solidifies first?
> They freeze at the same time. The cube has $V/A=a^3/6a^2=a/6$ and the sphere of diameter $a$ has $V/A=D/6=a/6$ too, although the sphere holds only 52 % of the cube's volume. The **modulus**, not the volume, sets the time. At equal *volume* the sphere is bigger and freezes later (table above).

> [!question]- A casting has a thick boss far from the riser. What goes wrong?
> The boss is the last to freeze but has no feed path (the thinner neck freezes first and cuts it off): a shrinkage cavity forms in the boss. Add a riser on the boss, or a chill to freeze the neck last.

## 6. Connections

- [[Heat Transfer - MOC]] and [[Steady Conduction and Thermal Resistance Networks]] — freezing is a heat-transfer problem; Chvorinov comes from a thermal resistance of the mould.
- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] — the gating velocity $\sqrt{2gh}$ and the sprue.
- [[Pipe Flow and Losses - Formula Bank]] — runner and gate losses reduce the real velocity (a discharge coefficient of 0.8–0.9).
- [[Phase Diagrams - Lever Rule and the Iron-Carbide Diagram]] — the freezing range and microstructure of the cast alloy.
