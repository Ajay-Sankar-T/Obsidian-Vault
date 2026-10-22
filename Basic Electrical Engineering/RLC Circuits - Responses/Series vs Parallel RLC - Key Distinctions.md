---
tags:
  - EE1100
  - RLC
  - series
  - parallel
  - duality
  - graphs
up: "[[RLC Circuits - Responses]]"
---

# Series vs Parallel RLC — Key Distinctions

← up: [[RLC Circuits - Responses|RLC Circuits — Responses]] · builds on: [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]

## The duality table

| Quantity | Series RLC | Parallel RLC |
|---|---:|---:|
| Shared variable | current $i$ (same through all three) | voltage $v$ (same across all three) |
| Impedance combination | $Z=R+j(X_L-X_C)$ | $Y=\dfrac1R+j\!\left(\omega C-\dfrac1{\omega L}\right)$ |
| $\omega_n$ | $1/\sqrt{LC}$ | $1/\sqrt{LC}$ (same!) |
| Damping coefficient $\alpha$ | $R/(2L)$ | $1/(2RC)$ |
| Effect of large $R$ | **more** damping (overdamped) | **less** damping (underdamped) |
| $|Z|$ at resonance | **minimum** ($=R$) | **maximum** ($=R$) |
| Current at resonance | **maximum** | **minimum** |
| Bandwidth ∝ | $R$ (larger $R$ → wider bandwidth) | $1/R$ (larger $R$ → narrower bandwidth) |

Every row follows from one fact: series and parallel RLC are **dual circuits** — swap $R\leftrightarrow1/R$, $L\leftrightarrow C$, voltage$\leftrightarrow$current throughout, and every series-RLC formula becomes the corresponding parallel-RLC formula. This is why $\omega_n=1/\sqrt{LC}$ is *identical* in both (it's built from $L$ and $C$ only, which swap into each other under duality and so the formula is self-dual), while every formula involving $R$ flips.

## The graph

![Series vs Parallel RLC side by side](series_vs_parallel_side_by_side.png)

Same qualitative shapes (underdamped rings, critical is fastest clean settle, overdamped crawls) — but notice the legend: for series RLC, underdamped is the **small**-$R$ case; for parallel RLC, underdamped is the **large**-$R$ case. The *shape* of damping is universal (see [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]]); which physical $R$ produces which shape is exactly reversed.

## Impedance vs frequency: opposite resonance behavior

![Series RLC impedance vs frequency](series_rlc_impedance_vs_frequency.png)

![Parallel RLC impedance vs frequency](parallel_rlc_impedance_vs_frequency.png)

**Series RLC** presents **minimum** impedance at resonance (reactances cancel, leaving only $R$) — so current is *maximum* at $\omega_0$: a series RLC circuit is naturally a **band-pass** filter for current / **acceptor** circuit, used when you want to *pass* a narrow band of frequencies through to a load.

**Parallel RLC** presents **maximum** impedance at resonance (the inductive and capacitive branch currents cancel in the *tank*, leaving minimal current drawn from the source even though internal circulating current between $L$ and $C$ is large) — a parallel RLC circuit is naturally a **band-stop/tank** circuit, the basis of the tank circuits used in oscillators and radio-frequency tuning to *reject* all but a narrow band.

## Practical identification rule

$$\boxed{\text{Elements share the same current}\Rightarrow\text{series}}\qquad\boxed{\text{Elements share the same voltage}\Rightarrow\text{parallel}}$$

Matches exactly the "do these elements share force or displacement?" rule already established for mechanical springs in [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Two Dissimilar Plates in a Rigid Opening|Two Dissimilar Plates in a Rigid Opening]] — series circuit elements are the electrical analogue of springs sharing the same force (stress), parallel circuit elements are the analogue of springs sharing the same displacement (strain).

## Related
- [[Series RLC Natural Response - Damping Cases|Series RLC Natural Response — Damping Cases]]
- [[Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response — Damping Cases]]
- [[Frequency Response and Resonance Curves|Frequency Response and Resonance Curves]]
- [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Two Dissimilar Plates in a Rigid Opening|Cross-Domain: series/parallel springs, the mechanical dual]]
