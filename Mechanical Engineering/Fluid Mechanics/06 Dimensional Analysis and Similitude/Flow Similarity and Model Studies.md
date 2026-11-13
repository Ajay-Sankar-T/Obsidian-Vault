---
tags: [concept, fluid-mechanics, dimensional-analysis, similitude, model-testing]
status: draft
aliases: [flow similarity, geometric similarity, kinematic similarity, dynamic similarity, model laws, Froude scaling, Reynolds scaling, incomplete similarity]
up: "[[Fluid Mechanics - MOC]]"
---

# Flow Similarity and Model Studies

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Important Dimensionless Groups|Important Dimensionless Groups]], [[Buckingham Pi Theorem|Buckingham π Theorem]] · formulas: [[Dimensional Analysis and Similitude - Formula Bank|Formula Bank §7]] · problems: [[Dimensional Analysis and Similitude - Solved Problems|Solved Problems]]

## Core Idea

> **One-sentence definition:** a model flow reproduces a prototype flow when it is geometrically, kinematically and dynamically similar, which in practice means every relevant dimensionless group has the same value in both.

**Intuition:** the Π theorem says the result $\Pi_1=G(\Pi_2,\dots,\Pi_k)$ depends only on the groups. If you build a smaller (or cheaper) model and make $\Pi_2,\dots,\Pi_k$ equal, then $\Pi_1$ must be equal too, so you can measure it on the model and scale it up.

## Governing Relations

| Similarity | Meaning | Requirement |
|---|---|---|
| **Geometric** | all lengths in the same ratio $\alpha=L_m/L_p$, same angles, scaled roughness | prerequisite |
| **Kinematic** | same velocity ratio at homologous points, same streamline pattern | follows from dynamic similarity |
| **Dynamic** | same ratio of forces (inertia : viscous : gravity ...) at homologous points | equal $Re$, $Fr$, $We$, $Ma$... as relevant |

**Complete similarity:** $\Pi_{i,m}=\Pi_{i,p}$ for all independent groups $i\ge2$, hence $\Pi_{1,m}=\Pi_{1,p}$.

**Which groups matter** (incompressible flow):
- no free surface: equal $Re$;
- free surface (ships, dams, rivers): equal $Re$ **and** $Fr$ (and $We$, $Ca$ if relevant);
- compressible: equal $Re$ and $Ma$.

**Scaling laws** with $\alpha=L_m/L_p$, same gravity:

$$\textbf{Froude: }\frac{V_m}{V_p}=\alpha^{1/2},\ \frac{Q_m}{Q_p}=\alpha^{5/2},\ \frac{F_m}{F_p}=\frac{\rho_m}{\rho_p}\alpha^3,\ \frac{T_m}{T_p}=\alpha^{1/2}$$

$$\textbf{Reynolds: }\frac{V_m}{V_p}=\frac{\nu_m}{\nu_p}\frac1\alpha,\qquad\frac{F_m}{F_p}=\frac{\rho_m\nu_m^2}{\rho_p\nu_p^2}$$

**Both $Re$ and $Fr$:** $\ \nu_m/\nu_p=\alpha^{3/2}$ (impossible for $\alpha\ll1$ with ordinary fluids, see the figure in [[Important Dimensionless Groups|Important Dimensionless Groups]]).

**Where:** subscripts $m$ = model, $p$ = prototype; $F$ = force of the same type (drag, load).

**Assumptions:** geometric similarity including roughness and fine details; all relevant variables included in the Π analysis.

## Visual

See the scaling figure in [[Important Dimensionless Groups|Important Dimensionless Groups]] (FM-D1) and the force-scale table: Froude scaling gives $V\propto L^{1/2}$ and $F\propto L^3$; Reynolds scaling gives $V\propto1/L$ and $F$ independent of $L$.

## When To Use

- Testing **ship hulls, dams, spillways, harbours** in a laboratory (Froude).
- **Wind tunnel** and **water tunnel** tests of aircraft, cars, buildings (Reynolds and Mach).
- Reading a published coefficient $C_D(Re)$ and applying it at a different size or speed.

**Recognition pattern:** "a 1:25 model is tested at ...; find the corresponding prototype speed/force" → **similarity**.

## Method

1. **Identify** the governing groups (list the variables, form the Π groups, see [[Buckingham Pi Theorem|Buckingham π Theorem]]).
2. **Choose** the dominant group to match (usually $Fr$ for free surfaces, $Re$ otherwise); fix the length ratio.
3. **Apply** the matching condition to get the model speed; use the force or flow scaling to convert measurements.
4. **Check** that the neglected groups are unimportant: compressibility ($Ma<0.3$), surface tension ($We\gg1$), laminar–turbulent state at model $Re$.

## Derivation / Why It Works

Take Froude matching: $V_m/\sqrt{gL_m}=V_p/\sqrt{gL_p}$ gives $V_m/V_p=\alpha^{1/2}$. Forces scale as pressure times area, $F\sim\rho V^2L^2$, so $F_m/F_p=(\rho_m/\rho_p)\alpha\cdot\alpha^2=(\rho_m/\rho_p)\alpha^3$. Flow rate $Q\sim VL^2$ gives $\alpha^{5/2}$. For Reynolds matching, $V_m/V_p=(\nu_m/\nu_p)/\alpha$, and $F\sim\rho V^2L^2$ then gives $F_m/F_p=\rho_m\nu_m^2/(\rho_p\nu_p^2)$, independent of size.

## Incomplete similarity

When two groups conflict (the usual case with $Re$ and $Fr$), match the **dominant** one and correct for the other:

| Situation | Practice |
|---|---|
| ship, dam, harbour | match $Fr$; $Re$ is violated by a factor 10–1000; apply a viscous (friction) correction, use roughened models |
| wind tunnel for a car or aircraft | match $Re$ if $Ma<0.3$; otherwise a pressurised or cryogenic tunnel raises $Re$ |
| sphere, cylinder drag | $C_D$ nearly constant for $10^3\lesssim Re\lesssim2\times10^5$, so only $Re$ in that band is needed |
| rivers and estuaries | distorted models (vertical scale larger than horizontal) with added roughness |

## Common Traps

- **Trap:** equating velocities or forces by the length ratio alone.
  - **Why:** the velocity ratio depends on which group is matched ($\alpha^{1/2}$ against $1/\alpha$).
  - **Avoid it by:** writing the matching equation first, then the scaling.
- **Trap:** a model that "looks right" but has different ratios in different directions, or no roughness scaling.
- **Trap:** matching $Re$ in water for an air prototype and forgetting to check $Ma$ in the original.
- **Trap:** applying the force ratio with the wrong density ratio when the model fluid differs.

## Example

### Given
(a) A 100 m ship at 10 m/s is tested with a 1:25 model in water. (b) A car moving at 30 m/s in air ($\nu=1.5\times10^{-5}$ m²/s, $\rho=1.2$ kg/m³) is tested as a 1:4 model in a water tunnel ($\nu=1.0\times10^{-6}$, $\rho=998$).

### Solution
(a) Froude scaling, $\alpha=1/25$:
$$V_m=10\sqrt{1/25}=2\ \text{m/s},\qquad\frac{F_m}{F_p}=\alpha^3=\frac1{15\,625}.$$

(b) Reynolds scaling, $\alpha=1/4$:
$$V_m=V_p\frac{\nu_m}{\nu_p}\frac1\alpha=30\times\frac{10^{-6}}{1.5\times10^{-5}}\times4=8.0\ \text{m/s},$$
$$\frac{F_m}{F_p}=\frac{\rho_m\nu_m^2}{\rho_p\nu_p^2}=\frac{998\times10^{-12}}{1.2\times2.25\times10^{-10}}=3.70.$$

Check via $F=C_D\tfrac12\rho V^2A$: $\dfrac{998}{1.2}\times\Big(\dfrac8{30}\Big)^2\times\dfrac1{16}=3.70$. ✓.

**Answer:** (a) 2 m/s and a force ratio of 1/15 625; (b) 8.0 m/s and a model force 3.70 times the prototype force.
**Key takeaway:** water is a good wind-tunnel substitute for air because its small $\nu$ lets you reach high $Re$ at modest speed (8 m/s instead of 120 m/s, which would be $Ma=0.35$ in air).

## Connections

### Prerequisites
- [[Buckingham Pi Theorem|Buckingham π Theorem]]
- [[Important Dimensionless Groups|Important Dimensionless Groups]]

### Related Concepts
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]] — the equations behind the groups.
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]] — $f(Re,e/D)$ is a similarity result.
- [[Surface Tension and Capillarity|Surface Tension and Capillarity]] — when $We$ must match.

### Next
- [[Differential Continuity Equation|Differential Continuity Equation]] — moving from scaling to the field equations.

### Cross-domain links
- [[Convection Fundamentals - Boundary Layers and Scale Analysis|Convection Fundamentals]] — heat-transfer correlations $Nu=f(Re,Pr)$ are the same similarity argument for temperature.
- [[Elongation Under Self-Weight and End Load|Elongation Under Self-Weight and End Load]] — the same scaling logic in structures: weight stress $\rho g L$ grows with size, so a small geometrically similar model is *less* stressed than the full-size structure, just as a small model has the wrong $Re$ or $Fr$.

## Quick Recall

> **In one line:** match the dominant dimensionless group, then scale speed and force with the matching law.

**Formula / trigger:** $$\text{Froude: }V\propto\sqrt L,\ F\propto L^3\qquad\text{Reynolds: }V\propto\frac{\nu}{L},\ F\propto\rho\nu^2$$

**Remember:** $Re$ and $Fr$ cannot both be matched in a small model; ships use $Fr$, tunnels use $Re$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
