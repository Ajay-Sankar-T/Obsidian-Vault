---
tags: [concept, fluid-mechanics, pipe-flow, minor-losses, fittings]
status: draft
aliases: [minor losses, loss coefficient, K factor, equivalent length, fittings, valves, sudden expansion, Borda-Carnot, entrance loss, exit loss]
up: "[[Fluid Mechanics - MOC]]"
---

# Minor Losses

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]], [[Energy Equation with Head Loss|Energy Equation with Head Loss]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §4]]

## Core Idea

> **One-sentence definition:** minor losses are the head losses caused by entrances, exits, bends, valves and changes of area, written as $h_{lm}=K\,V^2/2g$ with a loss coefficient $K$ (or as an equivalent length $L_e/D$ of straight pipe).

**Intuition:** whenever the flow has to separate, turn, accelerate or decelerate abruptly, it creates swirling, recirculating regions that dissipate mechanical energy into heat. The loss scales with the dynamic pressure $V^2/2g$, and the coefficient $K$ records how violent the disturbance is. They are "minor" only in long pipes; in a short system with many fittings they can dominate.

## Governing Relations

$$\boxed{h_{lm}=K\frac{V^2}{2g}}\qquad\text{or}\qquad h_{lm}=f\frac{L_e}{D}\frac{V^2}{2g}$$

$V$ is the mean velocity in the pipe at the fitting (for an area change, the velocity named in the table: usually the larger-velocity section, or $V_1$ for an expansion). Add every minor loss to $fL/D$ in one bracket:

$$h_{lT}=\Big(f\frac LD+\sum K\Big)\frac{V^2}{2g}$$

| Fitting | $K$ |
|---|---|
| entrance, re-entrant | 0.78 |
| entrance, square-edged | 0.50 |
| entrance, rounded $r/D=0.02,\ 0.06,\ \ge0.15$ | 0.28, 0.15, 0.04 |
| exit into a large reservoir | 1.0 |
| sudden expansion $A_1\to A_2$ (on $V_1$) | $(1-A_1/A_2)^2$ |
| sudden contraction $A_2/A_1=0,\,0.2,\,0.4,\,0.6,\,0.8$ (on $V_2$) | 0.50, 0.42, 0.28, 0.15, 0.04 |

| Fitting (fully open) | $L_e/D$ |
|---|---|
| gate valve, globe valve, angle valve, ball valve | 8, 340, 150, 3 |
| standard elbow 90°, 45° | 30, 16 |
| return bend (close) | 50 |
| standard tee, through run, through branch | 20, 60 |

**Where:** $K$ = loss coefficient; $L_e$ = equivalent length; both are determined experimentally (except the sudden expansion).

**Assumptions:** fully turbulent flow beyond the fitting; fittings spaced far enough apart that their disturbances do not interact (usually more than about 10 diameters).

## Visual

![[FM-N9-area-change-K.png]]

**Figure:** the expansion loss $K=(1-A_1/A_2)^2$ is derived exactly and is large for a big area jump (an exit into a reservoir, $A_1/A_2\to0$, is $K=1$); contraction losses are smaller because the converging flow stays attached except at the vena contracta.

## When To Use

- Short pipe runs with **valves, elbows, tees, entrances and exits**.
- Computing the total **pressure loss** of a piping system.
- Estimating pump **head** or driving head in fixture-heavy systems (plumbing, hydraulics).

**Recognition pattern:** "fittings", "elbows and valve", "sudden enlargement", "square-edged entrance" → **minor losses**.

## Method

1. **Identify** every fitting and the velocity each $K$ refers to.
2. **Choose** $K$ (or $L_e/D$) from tables; for expansions compute $(1-A_1/A_2)^2$.
3. **Apply:** sum $\sum K\,V^2/2g$, converting $L_e/D$ to $K=f\,L_e/D$; for fittings at different diameters, refer each to its own $V$ or convert via continuity ($V_1=V_2A_2/A_1$).
4. **Add** to the friction term in the energy equation.
5. **Check:** the entrance and exit losses are included once each; the exit loss $K=1$ applies to a submerged exit, while a free jet carries away $V^2/2g$ as kinetic energy.

## Derivation / Why It Works

**Sudden expansion (Borda–Carnot).** Control volume from just upstream of the step to a section downstream where the flow is uniform again; the pressure on the step face equals $p_1$ (the jet has not yet spread). Momentum: $(p_1-p_2)A_2=\rho A_2V_2(V_2-V_1)$ so $(p_1-p_2)/\rho=V_2^2-V_1V_2$. Energy: $h_l=\dfrac{p_1-p_2}\rho+\dfrac{V_1^2-V_2^2}2=\dfrac{(V_1-V_2)^2}{2}$. With continuity $V_2=V_1A_1/A_2$:
$$h_l=\Big(1-\frac{A_1}{A_2}\Big)^2\frac{V_1^2}{2}.$$
Other fittings are too complicated for theory and are measured; dimensional analysis shows $K=K(\text{geometry},Re)$, and $K$ is nearly independent of $Re$ for turbulent flow.

## Common Traps

- **Trap:** using the wrong velocity for $K$ at an area change.
  - **Avoid it by:** checking the table: expansion on $V_1$ (smaller section), contraction on $V_2$ (smaller section).
- **Trap:** forgetting the exit loss $K=1$ (or treating the free-jet exit as a loss).
- **Trap:** double counting: the $L_e/D$ and $K$ forms are alternatives for the same fitting.
- **Trap:** ignoring minor losses in a short system (they can be most of the loss).

## Example

### Given
Water ($\rho=998$ kg/m³) at $V=2$ m/s in a pipe of diameter 50 mm, length 20 m, $f=0.025$, containing: a square-edged entrance ($K=0.5$), two standard 90° elbows ($L_e/D=30$ each), one open gate valve ($L_e/D=8$) and an exit into a reservoir ($K=1$).

### Solution
$$f\frac LD=0.025\times\frac{20}{0.05}=10,\qquad\sum K=0.5+2(0.025\times30)+0.025\times8+1.0=3.2,$$
$$h_{lT}=(10+3.2)\frac{V^2}{2g}=13.2\times\frac{4}{2(9.81)}=2.69\ \text{m},\qquad\Delta p=\rho gh_{lT}=26.3\ \text{kPa}.$$

Minor share: $3.2/13.2=24\%$.

**Answer:** head loss 2.69 m, $\Delta p=26.3$ kPa, with minor losses a quarter of the total.
**Key takeaway:** at 400 diameters of pipe the fittings still add 24 %; in a pipe only 100 diameters long ($fL/D=2.5$) they would be 56 % of the total.

**Second example (sudden expansion).** $A_1/A_2=0.25$, $V_1=3$ m/s: $K=(1-0.25)^2=0.5625$, loss $=0.5625\times9/2=2.53$ J/kg (0.26 m of head).

## Connections

### Prerequisites
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]]
- [[Linear Momentum Equation|Linear Momentum Equation]] — the Borda–Carnot derivation.

### Related Concepts
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]]
- [[Moody Chart|Moody Chart]]
- [[Bernoulli Equation|Bernoulli Equation]] — the loss is the energy Bernoulli cannot account for.

### Next
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — each fitting is a small nonlinear resistor in series ($\Delta p=\tfrac12\rho K\,V^2$); series elements simply add their $K$'s, as resistances add.
- [[Fracture Mechanics - Stress Intensity and Griffith|Fracture Mechanics — Stress Intensity and Griffith]] — an abrupt geometric change causes a local penalty (energy loss here, stress amplification at a notch or crack there) quantified by a dimensionless factor times the nominal quantity.

## Quick Recall

> **In one line:** $h_{lm}=K\,V^2/2g$, added to $fL/D$; sudden expansion $K=(1-A_1/A_2)^2$.

**Formula / trigger:** $$h_{lT}=\Big(f\frac LD+\sum K\Big)\frac{V^2}{2g},\qquad K_{\rm exp}=\Big(1-\frac{A_1}{A_2}\Big)^2$$

**Remember:** entrance 0.5 (square), exit 1.0, convert $L_e/D$ via $K=fL_e/D$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
