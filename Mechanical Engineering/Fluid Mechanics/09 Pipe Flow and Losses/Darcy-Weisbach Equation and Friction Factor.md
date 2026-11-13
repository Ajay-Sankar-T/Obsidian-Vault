---
tags: [concept, fluid-mechanics, pipe-flow, friction-factor, major-losses]
status: draft
aliases: [Darcy-Weisbach, Darcy–Weisbach equation, friction factor, major loss, Colebrook equation, Haaland equation, relative roughness, hydraulic diameter]
up: "[[Fluid Mechanics - MOC]]"
---

# Darcy-Weisbach Equation and Friction Factor

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Energy Equation with Head Loss|Energy Equation with Head Loss]], [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §2–§3]]

## Core Idea

> **One-sentence definition:** the Darcy–Weisbach equation $h_l=f\,\dfrac LD\dfrac{V^2}{2g}$ gives the head lost to friction in a straight pipe, with the dimensionless friction factor $f$ depending on the Reynolds number and the relative roughness $e/D$.

**Intuition:** the loss is proportional to the length of pipe (more wall, more shear), to the dynamic pressure of the flow, and inversely to the diameter (less wall per unit flow area). All the complicated physics of laminar versus turbulent flow and wall roughness is packed into the one number $f$.

## Governing Relations

$$\boxed{h_l=f\,\frac LD\,\frac{V^2}{2g}}\qquad\Delta p=\rho g\,h_l=f\,\frac LD\,\frac{\rho V^2}{2}=\frac{8\rho fL}{\pi^2}\frac{Q^2}{D^5}$$

(In J/kg: $h_l=f\dfrac LD\dfrac{V^2}2$.) At fixed $Q$, $\Delta p\propto f\,L\,Q^2/D^5$: diameter dominates; a 20 % larger bore cuts $\Delta p$ to about 40 %.

**Friction factor**

| Regime | $f$ |
|---|---|
| laminar, $Re<2300$ | $\dfrac{64}{Re}$ (no roughness dependence) |
| turbulent, **Colebrook** (implicit) | $\dfrac1{\sqrt f}=-2.0\log_{10}\!\Big(\dfrac{e/D}{3.7}+\dfrac{2.51}{Re\sqrt f}\Big)$ |
| turbulent, **Haaland** (explicit, within 2 %) | $\dfrac1{\sqrt f}=-1.8\log_{10}\!\Big[\Big(\dfrac{e/D}{3.7}\Big)^{1.11}+\dfrac{6.9}{Re}\Big]$ |
| smooth pipe, $Re\lesssim10^5$ (Blasius) | $f=0.3164\,Re^{-1/4}$ |
| fully rough | $f=\Big[-2.0\log_{10}\dfrac{e/D}{3.7}\Big]^{-2}$ |

**Wall shear:** $\tau_w=\dfrac f8\rho V^2$.

**Non-circular ducts:** use the hydraulic diameter $D_h=\dfrac{4A}{P_w}$ ($A$ = flow area, $P_w$ = wetted perimeter) in $Re$, $e/D_h$ and the Darcy equation (approximate for turbulent flow; poor for laminar flow in sharp-cornered ducts).

**Roughness $e$ (mm):** riveted steel 0.9–9, concrete 0.3–3, cast iron 0.26, galvanised iron 0.15, commercial steel 0.046, drawn tubing 0.0015, smooth plastic $\approx0$.

**Where:** $L,D$ = pipe length and diameter; $V$ = mean velocity; $e$ = equivalent sand-grain roughness; $f$ = **Darcy** friction factor (the Fanning factor is $f/4$: check which a table uses).

**Assumptions:** steady, fully developed, incompressible, uniform pipe, no fittings (add them via [[Minor Losses|minor losses]]).

## Visual

![[FM-P1-moody-operating-points.png]]

**Figure:** the Moody chart with the operating points of the worked problems: $f$ against $Re$ for several $e/D$ ([[Moody Chart|how to read it]]).

## When To Use

- Pressure drop or head loss in **any long straight pipe or duct**.
- Sizing a pipe for a given flow and allowable $\Delta p$.
- Estimating pumping power for pipelines, water mains and ducts.

**Recognition pattern:** "pressure drop over a length of pipe", "friction factor", "commercial steel pipe" → **Darcy–Weisbach**.

## Method

1. **Identify** $Q$ (or $V$), $D$, $L$, material (for $e$), and the fluid ($\rho$, $\nu$ at the temperature).
2. **Compute** $V=Q/A$, $Re=VD/\nu$, $e/D$.
3. **Choose** $f$: $64/Re$ if laminar; Haaland (direct) or Colebrook (iterate) if turbulent.
4. **Apply** $h_l=f(L/D)V^2/2g$ and $\Delta p=\rho gh_l$.
5. **Check:** $Re$ regime, which friction factor convention (Darcy vs Fanning), and that minor losses are added when fittings exist.

## Derivation / Why It Works

**Force balance** on a pipe length $L$ in steady fully developed flow: $\Delta p\,\dfrac{\pi D^2}4=\tau_w\,\pi DL\ \Rightarrow\ \Delta p=\dfrac{4L}{D}\tau_w$. Dimensional analysis ([[Buckingham Pi Theorem|Π theorem]]) for $\tau_w$ as a function of $\rho,\bar u,D,\mu,e$ (6 variables, 3 dimensions, 3 groups) gives $\dfrac{\tau_w}{\rho\bar u^2}=\phi\big(Re,\ e/D\big)$; define $f=8\tau_w/\rho\bar u^2$ so that
$$\Delta p=\frac{4L}D\cdot\frac f8\rho\bar u^2=f\,\frac LD\,\frac{\rho\bar u^2}2.$$
For laminar flow the exact solution ([[Hagen-Poiseuille Flow|Hagen–Poiseuille]]) gives $f=64/Re$; for turbulent flow, the function $\phi$ comes from experiment (Nikuradse, Colebrook).

## Common Traps

- **Trap:** using the Fanning factor from one table in the Darcy equation (factor 4 error).
  - **Avoid it by:** checking whether $f\to64/Re$ (Darcy) or $16/Re$ (Fanning) in laminar flow.
- **Trap:** forgetting that roughness does not matter in laminar flow.
- **Trap:** using absolute roughness $e$ where $e/D$ is needed.
- **Trap:** a non-circular duct without hydraulic diameter.
- **Trap:** Colebrook iterated starting from a wild $f$ (start from the fully rough value; it converges in 2–3 passes).
- **Trap:** using $\nu$ at the wrong temperature.

## Example

### Given
Water at 20 °C ($\rho=998$ kg/m³, $\nu=1.01\times10^{-6}$ m²/s) flows at $Q=0.01$ m³/s through a 100 m length of commercial-steel pipe, $D=100$ mm, $e=0.046$ mm. Find the head loss and pressure drop.

### Solution
$$V=\frac{Q}{\pi D^2/4}=1.273\ \text{m/s},\quad Re=\frac{VD}{\nu}=1.26\times10^5,\quad\frac eD=4.6\times10^{-4}.$$
Colebrook (iterated) gives $f=0.0196$ (Haaland: 0.0193, within 1.2 %).
$$h_l=0.0196\times\frac{100}{0.1}\times\frac{1.273^2}{2(9.81)}=1.62\ \text{m},\qquad\Delta p=\rho gh_l=15.8\ \text{kPa}.$$

**Answer:** $f=0.0196$, head loss 1.62 m, $\Delta p=15.8$ kPa.
**Key takeaway:** a smooth pipe ($e=0$) would give $f=0.0172$; roughness of only 0.046 mm already raises the loss by 14 %. Doubling the flow to $0.02$ m³/s multiplies $\Delta p$ by about $3.7$ (not 4: $f$ falls slightly with $Re$).

## Connections

### Prerequisites
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]
- [[Buckingham Pi Theorem|Buckingham π Theorem]]

### Related Concepts
- [[Moody Chart|Moody Chart]]
- [[Minor Losses|Minor Losses]]
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]]
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] — origin of $64/Re$.

### Next
- [[Moody Chart|Moody Chart]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — $\Delta p=R\,Q^2$ with $R=8\rho fL/\pi^2D^5$: a nonlinear (quadratic) resistor; laminar flow is Ohm's law ($\Delta p\propto Q$).
- [[Forced Convection Correlations|Forced Convection Correlations]] — the Reynolds (and Colburn) analogy ties $f$ to the Nusselt number: $St\,Pr^{2/3}=f/8$.

## Quick Recall

> **In one line:** $h_l=f\,(L/D)\,V^2/2g$, with $f=64/Re$ laminar and Colebrook/Haaland for turbulent flow.

**Formula / trigger:** $$\Delta p=f\frac LD\frac{\rho V^2}{2},\qquad f=\frac{64}{Re},\ \ \frac1{\sqrt f}=-1.8\log_{10}\Big[\Big(\frac{e/D}{3.7}\Big)^{1.11}+\frac{6.9}{Re}\Big]$$

**Remember:** $\Delta p\propto Q^2/D^5$; Darcy $f$ is 4 × Fanning.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
