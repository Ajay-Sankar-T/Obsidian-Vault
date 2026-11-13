---
tags: [concept, fluid-mechanics, pipe-flow, pipe-systems, pump-curve]
status: draft
aliases: [pipe systems, series and parallel pipes, three pipe problems, system curve, pump curve, operating point, pipe network]
up: "[[Fluid Mechanics - MOC]]"
---

# Pipe Systems and the Three Problems

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach]], [[Minor Losses|Minor Losses]], [[Moody Chart|Moody Chart]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §5]] · problems: [[Pipe Flow and Losses - Solved Problems|Solved Problems]]

## Core Idea

> **One-sentence definition:** a pipe system is solved with three rules: the energy equation between two known points, **continuity at every junction** (flow in = flow out), and **the same head difference across parallel branches**.

**Intuition:** this is circuit analysis. Head plays the role of voltage and flow rate the role of current; a pipe is a nonlinear resistor $\Delta h=R\,Q^2$. Series elements carry the same current ($Q$) and add voltage drops; parallel elements share the same voltage drop and add currents.

## Governing Relations

**Single pipe as a resistor** (turbulent, fixed $f$): $\ h_l=R\,Q^2$, with $R=\dfrac{8}{\pi^2g}\Big(\dfrac{fL}{D^5}+\dfrac{\sum K}{D^4}\Big)$.

| Arrangement | Same | Adds | Rule |
|---|---|---|---|
| **series** | $Q$ | head losses | $h_{lT}=\sum_i R_iQ^2$ |
| **parallel** | head loss $\Delta h$ | flows | $Q=\sum_iQ_i,\ \ Q_i=\sqrt{\Delta h/R_i}$ |
| **junction** | — | — | $\sum Q_{\rm in}=\sum Q_{\rm out}$ |
| **loop** | — | — | $\sum h_l=0$ around a closed loop (with sign) |

**Operating point of a pump and a system:** the system curve $H_{\rm sys}(Q)=\Delta z+\Delta p/\gamma+RQ^2$ meets the pump curve $H_p(Q)$:

$$H_p(Q)=H_{\rm sys}(Q)\quad\text{at the operating point}$$

**The three pipe problems**

| Unknown | Known | Method |
|---|---|---|
| $\Delta p$ (or $h_l$) | $Q$ (or $V$), $D$, $L$, $e$ | $Re\to f\to h_l$. Direct. |
| $Q$ | $\Delta p$, $D$, $L$, $e$ | guess $f$ (fully rough), get $V$, then $Re$, new $f$; 2–3 passes. |
| $D$ | $\Delta p$, $Q$, $L$, $e$ | guess $D$, compute $\Delta p$, adjust (or solve with Haaland), then round **up** to a standard size. |

**Where:** $R$ = hydraulic resistance (s²/m⁵); $H_p$ = pump head; $\Delta z$ = static lift.

**Assumptions:** steady incompressible flow, fully turbulent (constant $f$ per pipe, adjusted iteratively), junction losses folded into $K$.

## Visual

![[FM-P1-moody-operating-points.png]]

**Figure:** the operating points on the Moody chart: the solution of the "find $Q$" problem walks along a line of constant $e/D$ until $f$ and $V$ converge. The graded-line picture of a system with a pump is in [[Energy Equation with Head Loss|Energy Equation with Head Loss]].

## When To Use

- **Water supply, siphons, drainage, hydraulic circuits, pump selection.**
- Several pipes in series (changes of diameter) or in parallel (looped mains).
- Any problem where the unknown is the **flow rate** or the **diameter**, not the pressure drop.

**Recognition pattern:** "how much flows", "what diameter is needed", "two pipes in parallel", "pump operating point" → **pipe system**.

## Method

1. **Identify** the unknown (head loss, $Q$, or $D$) and the two reference points for the energy equation.
2. **Choose** series, parallel or network structure; label flows and heads.
3. **Apply** the energy equation (with $h_p$ and all losses) plus continuity and the parallel head rule.
4. **Iterate** when $f$ depends on the unknown $V$: guess fully rough $f$, solve for $V$, update $Re$ and $f$ (converges in 2–3 passes).
5. **Check:** $Re$ regime, positive pressure (above $p_v$, see [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]]), junction continuity, and round pipe diameters up to standard sizes.

## Derivation / Why It Works

Express each pipe's loss as $h_l=\big(fL/D+\sum K\big)V^2/2g$ and substitute $V=4Q/\pi D^2$: $h_l=RQ^2$. Series pipes carry the same $Q$, so their losses add. For parallel pipes, the pressure at the two junctions is common, so each branch has the same $h_l$: $R_1Q_1^2=R_2Q_2^2$. At fixed $f$, $R\propto L/D^5$, so for equal lengths $Q_1/Q_2=(D_1/D_2)^{5/2}$. The pump–system intersection follows from requiring the head the pump delivers equal the head the system needs at the same flow.

## Common Traps

- **Trap:** adding flows in series or head losses in parallel.
  - **Avoid it by:** series = same $Q$, parallel = same $\Delta h$.
- **Trap:** assuming a constant $f$ across different pipes or after the flow changes.
- **Trap:** choosing the next smaller standard diameter in the design problem (the loss then exceeds the budget).
- **Trap:** treating a pump curve as a constant head.
- **Trap:** forgetting the exit kinetic energy: a free jet carries $V^2/2g$ out.

## Example

### Given
**(a) Find $Q$:** water at 20 °C ($\nu=1.01\times10^{-6}$ m²/s) drains from a tank through a 50 mm commercial-steel pipe ($e=0.046$ mm), $L=50$ m, with a square-edged entrance ($K=0.5$), discharging as a free jet 10 m below the tank surface.

**(b) Parallel pipes:** two pipes of equal length with $D_A=100$ mm and $D_B=50$ mm and the same $f$.

**(c) Pump operating point (illustrative curves):** $H_{\rm sys}=10+2000\,Q^2$ and $H_p=30-5000\,Q^2$ ($Q$ in m³/s, heads in m).

### Solution
**(a)** Energy from the surface to the jet: $gH=\dfrac{V^2}2\Big(1+K+f\dfrac LD\Big)$, so $V=\sqrt{\dfrac{2gH}{1.5+fL/D}}$.

| Pass | $f$ | $V$ (m/s) | $Re$ |
|---|---|---|---|
| 1 (fully rough guess) | 0.0192 | 3.08 | $1.5\times10^5$ |
| converged | 0.0212 | 2.94 | $1.46\times10^5$ |

$Q=VA=2.94\times1.963\times10^{-3}=5.8$ L/s.

**(b)** Same $f$ and $L$: $R\propto D^{-5}$, so $Q_A/Q_B=2^{5/2}=5.66$ and pipe A carries $5.66/6.66=85\%$ of the flow.

**(c)** $10+2000Q^2=30-5000Q^2\ \Rightarrow\ Q^2=2.857\times10^{-3}$, $Q=0.0535$ m³/s, $H=15.7$ m.

**Answer:** (a) 5.8 L/s; (b) the 100 mm pipe takes 85 %; (c) 53.5 L/s at 15.7 m.
**Key takeaway:** twice the diameter carries 5.7 times the flow at the same head, so a modest oversize of the pipe pays off enormously; and the first iteration in (a) was already within 5 % of the converged velocity.

## Connections

### Prerequisites
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]]
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Minor Losses|Minor Losses]]
- [[Moody Chart|Moody Chart]]

### Related Concepts
- [[Differential Continuity Equation|Differential Continuity Equation]] — continuity at junctions.
- [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]] — the siphon limit and pump NPSH.
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] — the laminar case is linear and exact.

### Next
- [[Pipe Flow and Losses - Solved Problems|Pipe Flow and Losses — Solved Problems]] and [[Viscous Flow and Exact Solutions - Solved Problems|Viscous Flow Solved Problems]].

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — pipe networks are circuits: continuity at junctions is KCL, head loss around a loop is KVL, $\Delta h=RQ^2$ is a nonlinear resistor; the Hardy Cross method is nodal analysis solved iteratively.
- [[Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]] — the same series/parallel rule: shared flow adds drops; shared drop adds flows.

## Quick Recall

> **In one line:** series: same $Q$, add losses; parallel: same $\Delta h$, add flows; unknown $Q$ or $D$: iterate on $f$.

**Formula / trigger:** $$h_l=RQ^2,\quad R\propto\frac{L}{D^5},\quad Q=\sum Q_i\ (\text{parallel}),\quad H_p(Q)=H_{\rm sys}(Q)$$

**Remember:** round the diameter up; 2–3 passes fix $f$; twice the diameter carries 5.7 × the flow.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
