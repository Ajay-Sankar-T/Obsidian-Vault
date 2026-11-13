---
tags: [concept, fluid-mechanics, pipe-flow, moody-chart, friction-factor]
status: draft
aliases: [Moody diagram, Moody chart, friction factor chart, smooth pipe, fully rough pipe, hydraulically smooth, Nikuradse]
up: "[[Fluid Mechanics - MOC]]"
---

# Moody Chart

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]], [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §3]]

## Core Idea

> **One-sentence definition:** the Moody chart is a log–log plot of the Darcy friction factor $f$ against the Reynolds number for a family of relative roughnesses $e/D$, combining the laminar law and the Colebrook turbulent law in one picture.

**Intuition:** it shows when the pipe wall's roughness matters. At low $Re$ (laminar) the wall is irrelevant. At high $Re$ the viscous sublayer becomes thinner than the roughness bumps, and the pipe behaves as "fully rough": friction depends on roughness only, not on speed.

## Governing Relations

The curves are:

$$f=\frac{64}{Re}\ (Re<2300),\qquad\frac1{\sqrt f}=-2.0\log_{10}\Big(\frac{e/D}{3.7}+\frac{2.51}{Re\sqrt f}\Big)\ (Re>4000),\qquad f_{\rm rough}=\Big[-2.0\log_{10}\frac{e/D}{3.7}\Big]^{-2}$$

**Regions of the chart:**

| Region | $Re$ | Behaviour |
|---|---|---|
| **laminar** | $<2300$ | one straight line, slope $-1$ on log–log axes; independent of $e/D$ |
| **critical (transition) zone** | 2300–4000 | $f$ jumps and is uncertain; avoid designing here |
| **smooth-pipe curve** | any, $e/D\to0$ | lowest turbulent $f$, falls slowly with $Re$ (Blasius $0.3164Re^{-1/4}$ for $Re<10^5$) |
| **transition-rough** | intermediate | $f$ depends on both $Re$ and $e/D$ |
| **fully rough** | large $Re$ | each $e/D$ curve flattens horizontally: $f=f(e/D)$ only, so $\Delta p\propto V^2$ exactly |

**Smooth or rough?** A pipe is hydraulically smooth when $e\lesssim\delta_v\approx5\nu/u_\tau$ (the viscous sublayer thickness) and fully rough when $e\gtrsim60\,\nu/u_\tau$ (roughly), with $u_\tau=V\sqrt{f/8}$.

**Where:** $e$ = equivalent sand-grain roughness (mm); $e/D$ = relative roughness; $\nu$ = kinematic viscosity.

**Assumptions:** fully developed turbulent flow in a circular pipe with uniform roughness (commercial pipes are covered by the Colebrook equation, which interpolates the transition region smoothly).

## Visual

![[FM-P1-moody-operating-points.png]]

**Figure:** the chart with the operating points of the GPS 7 and 8 problems; moving to the right at fixed $e/D$ (higher $Re$) $f$ falls, then levels at the fully rough value.

![[FM-P6-laminar-point.png]]

**Figure:** the laminar branch with the laminar-tube operating point, on the $64/Re$ line.

## When To Use

- Reading **$f$ quickly** from $Re$ and $e/D$.
- Judging **how much roughness matters** (is the pipe near the smooth or the fully rough limit?).
- Deciding whether $\Delta p\propto V^2$ (fully rough) or $\propto V^{1.75}$-ish (smooth) when scaling a flow.

**Recognition pattern:** "from the Moody chart", "relative roughness", "fully rough turbulent flow" → **Moody chart**.

## Method

1. **Identify** $Re=VD/\nu$ and $e/D$ (look up $e$).
2. **Choose** the region: laminar line, smooth curve, or an $e/D$ curve.
3. **Apply:** read $f$ at the point; for accuracy use Haaland (explicit) or iterate Colebrook.
4. **Check:** that $Re>4000$ for the turbulent curves, and compare against the fully rough value as a sanity bound ($f\ge f_{\rm rough}$ and $f\ge f_{\rm smooth}$).

## Derivation / Why It Works

*Smooth limit.* Near the wall the viscous sublayer of thickness $\delta_v\sim\nu/u_\tau$ covers roughness bumps, so only viscous scales matter and $f=f(Re)$. *Rough limit.* If the bumps stick out of the sublayer, the drag is pressure (form) drag on the roughness elements, proportional to $\rho V^2$ and independent of $\nu$, so $f=f(e/D)$. The Colebrook equation is the empirical formula that joins the two limits: it is $1/\sqrt f=-2\log(\text{rough term}+\text{smooth term})$.

## Common Traps

- **Trap:** reading the laminar branch for roughness effects: there are none.
- **Trap:** reading the chart in the critical zone and trusting the value.
- **Trap:** using Fanning-factor charts (values are 1/4 of Darcy).
- **Trap:** using $e$ instead of $e/D$ to select the curve.
- **Trap:** assuming $f$ is constant: it is only constant in the fully rough region.

## Example

### Given
The 100 mm commercial-steel pipe of the [[Darcy-Weisbach Equation and Friction Factor|previous note]]: $e/D=4.6\times10^{-4}$, $Re=1.26\times10^5$ with $f=0.0196$. How does $f$ change when the flow is raised to $Re=2.5\times10^5$ and $10^6$? What is the fully rough limit?

### Solution
Colebrook iteration gives:

| $Re$ | $f$ |
|---|---|
| $1.26\times10^5$ | 0.0196 |
| $2.5\times10^5$ | 0.0182 |
| $10^6$ | 0.0169 |
| $\infty$ (fully rough) | 0.0164 |
| smooth pipe at $1.26\times10^5$ | 0.0172 |

Check of the regime: $\delta_v=5\nu/u_\tau=5(1.01\times10^{-6})/0.063=0.08$ mm against $e=0.046$ mm: the roughness is *inside* the sublayer, so this pipe is nearly smooth at this $Re$; it only becomes fully rough at much higher $Re$.

**Answer:** $f$ falls from 0.0196 to 0.0182 and 0.0169, tending to 0.0164.
**Key takeaway:** at higher speed $f$ falls only 14 % over an 8-fold range of $Re$, so $\Delta p$ rises almost as $V^2$ (roughly $V^{1.93}$).

## Connections

### Prerequisites
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]

### Related Concepts
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]] — chart-based iteration.
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] — the laminar line.
- [[Buckingham Pi Theorem|Buckingham π Theorem]] — why $f=f(Re,e/D)$.

### Next
- [[Minor Losses|Minor Losses]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — the fully rough limit is a **resistor that stops depending on current's regime**: $\Delta p=RQ^2$ with constant $R$.
- [[Forced Convection Correlations|Forced Convection Correlations]] — the heat-transfer coefficient follows the same smooth→rough pattern via the Reynolds analogy.

## Quick Recall

> **In one line:** the Moody chart plots $f(Re,e/D)$: laminar line $64/Re$, a smooth-pipe curve, and horizontal fully rough asymptotes.

**Formula / trigger:** $$f=\frac{64}{Re}\ \text{(lam)},\qquad f_{\rm rough}=\Big[-2\log_{10}\frac{e/D}{3.7}\Big]^{-2}$$

**Remember:** roughness is irrelevant when laminar and decisive at high $Re$; avoid $2300<Re<4000$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
