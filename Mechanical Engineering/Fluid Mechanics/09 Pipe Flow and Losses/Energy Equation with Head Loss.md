---
tags: [concept, fluid-mechanics, pipe-flow, energy-equation, head-loss]
status: draft
aliases: [energy equation for pipe flow, extended Bernoulli, head loss, pump head, turbine head, energy grade line, hydraulic grade line, EGL HGL]
up: "[[Fluid Mechanics - MOC]]"
---

# Energy Equation with Head Loss

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Bernoulli Equation|Bernoulli Equation]], [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §1]] · problems: [[Pipe Flow and Losses - Solved Problems|Solved Problems]]

## Core Idea

> **One-sentence definition:** the steady-flow energy equation for a pipe is Bernoulli plus the energy a pump adds, a turbine removes, and friction turns into heat: $\;H_1+h_{\rm pump}=H_2+h_{\rm turbine}+h_{l}$, with $H=p/\gamma+\alpha V^2/2g+z$.

**Intuition:** Bernoulli's constant is the fluid's mechanical energy per unit weight. In a real pipe, friction continually converts some of it into internal energy (it cannot be recovered), a pump gives more, a turbine takes some out. Head loss $h_l$ is the bookkeeping entry for the energy that went into heat.

## Governing Relation

Between sections 1 and 2 (steady, incompressible, one inlet, one outlet):

$$\boxed{\Big(\frac{p_1}{\gamma}+\alpha_1\frac{V_1^2}{2g}+z_1\Big)+h_p=\Big(\frac{p_2}{\gamma}+\alpha_2\frac{V_2^2}{2g}+z_2\Big)+h_t+h_{lT}}$$

In energy per unit **mass** (J/kg): $\ \dfrac{p_1}{\rho}+\alpha_1\dfrac{V_1^2}2+gz_1+w_p=\dfrac{p_2}{\rho}+\alpha_2\dfrac{V_2^2}2+gz_2+w_t+h_{lT}$.

- $h_{lT}=h_l+h_{lm}$: major (friction) plus minor losses ([[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach]], [[Minor Losses|Minor Losses]]).
- $\alpha$ = kinetic-energy coefficient: $\alpha=2$ for fully developed laminar flow, $\approx1.05$ (use 1) for turbulent.
- The loss is the rise in internal energy minus heat added: $h_{lT}=(u_2-u_1)-q$ per unit mass, always $\ge0$.

**Pump and turbine power:**
$$P_{\rm water}=\rho gQ\,h_p,\qquad P_{\rm shaft}=\frac{\rho gQ\,h_p}{\eta_p},\qquad P_{\rm turbine\ out}=\eta_t\,\rho gQ\,h_t$$

**Grade lines:** $\text{EGL}=p/\gamma+V^2/2g+z$; $\text{HGL}=p/\gamma+z$ (EGL minus $V^2/2g$). EGL falls with friction, rises across a pump, falls across a turbine; for a straight uniform pipe the EGL slope is $h_l/L=(f/D)(V^2/2g)$.

**Where:** $\gamma=\rho g$; $h_p,h_t$ = pump and turbine head (m); $Q$ = flow rate; $\eta$ = efficiency.

**Assumptions:** steady, incompressible, uniform properties at each section (the $\alpha$ factors account for non-uniform velocity), no heat transfer except as part of the loss.

## Visual

![[FM-N4-egl-hgl-pump-losses.png]]

**Figure:** reservoir A to reservoir B through a 0.5 m pipe with $V^2/2g=1$ m. The EGL drops 0.5 m at the entrance, slopes down at 0.04 m/m with friction, **jumps by the pump head 12.9 m**, continues to fall, and loses the whole velocity head (1 m) at the exit. The HGL sits $V^2/2g$ below the EGL and lands on the free surface of B.

## When To Use

- Any pipe-flow problem with **friction, pumps or turbines**: pump sizing, supply lines, siphons, penstocks.
- Finding **pressure at a point** along a pipe (using the HGL).
- Computing **power** requirements.

**Recognition pattern:** "find the pump head/power", "pressure at the end of the pipe", "elevation difference between tanks" → **energy equation with $h_l$**.

## Method

1. **Identify** points 1 and 2 where the most is known (free surfaces, exits to atmosphere); sketch the system.
2. **Choose** $\alpha$ (2 laminar, 1 turbulent) and the datum.
3. **Write** the energy equation with $h_p$, $h_t$, $h_{lT}=f\frac LD\frac{V^2}{2g}+\sum K\frac{V^2}{2g}$.
4. **Solve** for the unknown head, pressure or flow (iteratively if $f$ depends on the unknown $V$: [[Pipe Systems and the Three Problems|Pipe Systems]]).
5. **Check:** a pump must be *added on the supply side*; $h_l\ge0$; pressures in absolute terms against $p_v$.

## Derivation / Why It Works

First law for a control volume with steady flow: $q-w_{\rm shaft}=\Delta\big(h+\tfrac12V^2+gz\big)$ per unit mass, with enthalpy $h=u+p/\rho$. Separate the mechanical terms: $\dfrac{p_2-p_1}\rho+\dfrac{\alpha_2V_2^2-\alpha_1V_1^2}2+g(z_2-z_1)=-w_{\rm shaft}-\big[(u_2-u_1)-q\big]$. The bracket is the unrecoverable loss $h_{lT}$ (positive by the second law), giving the boxed equation. The kinetic-energy coefficient is $\alpha=\dfrac1{A}\int\big(\dfrac uV\big)^3dA$; for the laminar parabola it equals 2.

## Common Traps

- **Trap:** applying plain Bernoulli across a pump or through a long pipe.
  - **Avoid it by:** adding $h_p$ and $h_l$.
- **Trap:** forgetting the exit loss: a free jet carries $V^2/2g$ away; a submerged exit loses all of it.
- **Trap:** mixing J/kg and metres (divide J/kg by $g$ to get head).
- **Trap:** sign of the pump term (it appears on the supply side of the equation).
- **Trap:** using $\alpha=1$ for laminar flow.

## Example

### Given
The system in the figure: reservoir A (surface at 10 m) to reservoir B (surface at 18 m) through a 0.5 m pipe, 85 m long in total; $f=0.02$, entrance $K=0.5$, exit $K=1.0$, both reservoir surfaces at rest and at atmospheric pressure. Find the pump head, the flow rate for $V^2/2g=1$ m, and the power.

### Solution
Velocity: $V=\sqrt{2g(1)}=4.43$ m/s. Friction slope $\dfrac fD\dfrac{V^2}{2g}=\dfrac{0.02}{0.5}(1)=0.04$ m/m, so friction $=0.04\times85=3.4$ m.

Energy between the surfaces ($p$ and $V$ both zero at each end):
$$z_A+h_p=z_B+h_{lT}\ \Rightarrow\ h_p=(18-10)+0.5+3.4+1.0=12.9\ \text{m}.$$
$$Q=VA=4.43\times0.1963=0.870\ \text{m}^3/\text{s},\quad P_{\rm water}=\rho gQh_p=998(9.81)(0.870)(12.9)=110\ \text{kW},\quad P_{\rm shaft}\big|_{\eta=0.8}=137\ \text{kW}.$$

**Answer:** pump head 12.9 m, 0.870 m³/s, 110 kW delivered to the water (137 kW at the shaft).
**Key takeaway:** 8 m of this is static lift; the other 4.9 m (38 %) is pure loss. The velocity head cancels because both ends are at rest.

## Connections

### Prerequisites
- [[Bernoulli Equation|Bernoulli Equation]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]

### Related Concepts
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Minor Losses|Minor Losses]]
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]]
- [[Angular Momentum Principle|Angular Momentum Principle]] — how the pump turns shaft torque into head.

### Next
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — EGL is the "voltage" line: a pump is a battery, a friction loss is a resistor's $IR$ drop, and the energy equation is KVL around the loop.
- [[Exergy and Reversible Work|Exergy and Reversible Work]] — head loss is destroyed exergy: friction turns reversible work into heat, which is why the shaft work always exceeds $\rho gQ\,\Delta H$.
- [[Energy Methods - A Unified View|Energy Methods — A Unified View]]

## Quick Recall

> **In one line:** $H_1+h_p=H_2+h_t+h_l$: Bernoulli's head plus pump, minus turbine, minus friction.

**Formula / trigger:** $$\frac{p_1}{\gamma}+\alpha_1\frac{V_1^2}{2g}+z_1+h_p=\frac{p_2}{\gamma}+\alpha_2\frac{V_2^2}{2g}+z_2+h_t+h_l,\qquad P=\rho gQh$$

**Remember:** EGL drops with friction, jumps up across a pump; $\alpha=2$ laminar, 1 turbulent.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
