---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Metrology, GD&T, Geometric dimensioning and tolerancing, Gauging, Go no-go gauge, Position tolerance, MMC, Flatness, Datum reference frame, CMM]
---

# Metrology and GD&T — Form, Position and Gauging

> [!abstract] In one breath
> **Metrology** is measuring, with known uncertainty. **GD&T** says what to measure: tolerances on **form, orientation, location and runout** relative to **datums**, not just on sizes. A **gauge** checks quickly whether a feature is inside its zone. Everything rests on one chain: *specify, measure, accept*.

Part of [[Manufacturing Technology - MOC]]. Previous: [[Jigs and Fixtures - The 3-2-1 Location Principle]]. Drawing side: [[Limits, Fits and Tolerances]] and [[Surface Finish, Machining Symbols and Production Drawings]] in [[Computer Aided Machine Drawing - MOC]].

## 1. Measurement vocabulary

| Term | Meaning |
| --- | --- |
| **Accuracy** | closeness of the mean to the true value |
| **Precision (repeatability)** | scatter of repeated readings |
| **Resolution** | smallest change the instrument can show |
| **Range** | span measurable |
| **Uncertainty** | stated bound on the error, with confidence |

**Rule of ten:** the instrument's resolution should be about $\frac1{10}$ of the tolerance to be checked (a $\pm0.05$ mm tolerance needs 0.01 mm resolution). **Abbe principle:** the measuring axis should be in line with the scale axis; offset gives a cosine error that grows with the offset.

| Instrument | Typical resolution |
| --- | --- |
| Steel rule | 0.5–1 mm |
| Vernier caliper | 0.02 mm |
| Micrometer | 0.01 mm (0.001 mm digital) |
| Dial indicator | 0.01 mm (0.001 mm) |
| Gauge blocks (reference) | sub-micron (calibrated) |
| CMM (coordinate measuring machine) | 1–5 µm |
| Surface profilometer | tens of nm |

## 2. The geometric tolerances

A tolerance **zone** that the real feature must lie within (a width between two planes, a cylinder, a circle). The 14 symbols fall in five families:

| Family | Characteristics | Datum? |
| --- | --- | --- |
| **Form** | straightness, **flatness**, circularity, cylindricity | no |
| **Orientation** | perpendicularity, parallelism, angularity | yes |
| **Location** | **position**, concentricity, symmetry | yes |
| **Runout** | circular, total | yes (an axis) |
| **Profile** | line, surface | with or without |

A **feature control frame** reads left to right: characteristic · tolerance (with Ø if the zone is a cylinder, and a material-condition modifier) · datum references in order of precedence. The **datum reference frame** is the 3-2-1 set of planes on the datum features, so the same part is measured in the same orientation it will be assembled.

**Example, flatness 0.05:** the surface lies between two parallel planes 0.05 mm apart, wherever they are placed. It limits form only and says nothing about the position of the face.

## 3. Material conditions and bonus tolerance

**MMC** (maximum material condition): the size limit where the part has the most material (smallest hole, biggest shaft); **LMC** the opposite. A tolerance modified by Ⓜ gets a **bonus** equal to the departure of the size from MMC: as a hole gets bigger, a bigger position error still lets the bolt fit.

**Example.** Hole Ø10.0–10.1 mm, position tolerance Ø0.2 at MMC:

| Hole size | Position tolerance zone |
| --- | --- |
| at MMC, Ø10.0 | Ø0.2 |
| Ø10.05 | Ø0.25 |
| at LMC, Ø10.1 | **Ø0.3** |

**Virtual condition** $=$ MMC $-$ tolerance (hole) $=10.0-0.2=9.8$ mm: the pin that always fits has to be at most 9.8 mm. Fixed-size functional gauges are made to the virtual condition.

![[MFG-6-fixture-gdt.png]]

## 4. Gauging

A **fixed gauge** gives a pass/fail answer quickly:

- **GO gauge** checks the MMC limit (the plug that must enter a hole), **NO-GO** (NOT GO) checks the LMC limit and must not enter.
- **Taylor's principle:** the GO gauge should check the **whole** feature at once (full-form: a full plug), the NO-GO checks one dimension at a time (a short pin).
- **Gauge tolerance** is about 10 % of the workpiece tolerance, with a wear allowance on GO gauges.

**Example.** A Ø10 H7 hole has limits 10.000 to 10.015 mm (tolerance 0.015). GO plug 10.000 (+0.0015 gauge tolerance), NO-GO plug 10.015 (−0.0015): a hole accepts GO and rejects NO-GO.

Other checks: **comparators** (a dial indicator against a master), **optical** projectors, **angles** by sine bars, **screw threads** by three-wire method or thread gauges, **surface roughness** with a stylus profilometer (Ra) and **CMM** probes for 3-D position, with software evaluating the feature control frames.

## 5. Why it matters in manufacturing

Tolerance drives process choice and cost: IT12 can come from sawing, IT7 needs turning and reaming, IT5 grinding. Measurement uncertainty must stay a small fraction of the tolerance. A part whose size is in tolerance may still fail on **form** (a bent shaft) or **position** (misaligned holes), which is what GD&T specifies.

> [!warning] Traps
> - Reading a flatness tolerance as a size tolerance: it floats within the size limits.
> - Measuring from the wrong datum: the result depends on the datum order.
> - Forgetting the bonus tolerance when the modifier is MMC.
> - Using a measuring instrument with a resolution equal to the tolerance.
> - Applying the NO-GO as a full-form gauge: it should check one point of size.

> [!question]- Predict first: a hole at Ø10.1 (LMC) is 0.28 mm off its true position. Accept or reject under Ø0.2 at MMC?
> Accept: the allowed zone at LMC is Ø0.3, and a diametral position error of 0.28 mm falls inside. At Ø10.0 (MMC) the same error would be rejected (allowed Ø0.2).

> [!question]- Why is a pass/fail gauge preferred on a production line to a CMM?
> Speed and repeatability: it takes seconds, any operator gets the same answer, and it checks a *functional* envelope (the bolt that has to fit). The CMM gives numbers for process control and for features that cannot be gauged.

## 6. Connections

- [[Limits, Fits and Tolerances]] — the size tolerance (ISO grades and fits) that GD&T extends with form and position.
- [[Surface Finish, Machining Symbols and Production Drawings]] — roughness $R_a$ and the callouts.
- [[Jigs and Fixtures - The 3-2-1 Location Principle]] — datum reference frame = 3-2-1.
- [[Error Analysis - Uncertainty and Propagation]] — measurement uncertainty, repeatability and combination of errors.
- [[Measurements, Instrumentation and Control - MOC]] — sensors and transducers behind digital gauges.
