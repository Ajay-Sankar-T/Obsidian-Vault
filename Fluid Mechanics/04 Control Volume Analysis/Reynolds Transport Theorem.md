---
tags: [fluid-mechanics, control-volume, reynolds-transport-theorem]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Reynolds Transport Theorem

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/04 Control Volume Analysis/System and Control Volume|System and Control Volume]]

## The theorem

For a fixed control volume, relating the rate of change of any extensive system property $B$ to the equivalent control-volume bookkeeping:

$$\boxed{\frac{dB_{\rm system}}{dt}=\frac{\partial}{\partial t}\int_{CV}\rho b\,dV+\oint_{CS}\rho b(\mathbf V\cdot\mathbf n)\,dA}$$

where $b=B/m$ is the intensive (per-unit-mass) version of $B$.

## Interpretation

$$\boxed{\text{System change}=\text{Accumulation in CV}+\text{Net outflow through CS}}$$

This is the control-volume generalization of the [[Fluid Mechanics/03 Fluid Kinematics/Material Derivative and Fluid Acceleration|material derivative]]: instead of asking "how does a *point property* change following one particle," RTT asks "how does an *extensive property of an entire system* change," expressed using only quantities defined on a fixed region in space. Setting $B=m,b=1$ gives [[Fluid Mechanics/04 Control Volume Analysis/Conservation of Mass (Continuity Equation)|conservation of mass]]; setting $B=m\mathbf V,\ b=\mathbf V$ gives the [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|linear momentum equation]] — every conservation law used in this vault is a specific instance of this one theorem.

## Cross-domain: RTT is the fluid-mechanics KCL

Compare the "Accumulation = Inflow − Outflow" structure with [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Nodal and Mesh Analysis (AC)|Nodal and Mesh Analysis]]'s Kirchhoff's Current Law, $\sum I_{\rm leaving}=0$ at a node — KCL is exactly RTT's mass-conservation special case applied to a control volume shrunk down to a single circuit node, with charge playing the role of the conserved extensive quantity $B$ and current playing the role of the flux term $\oint\rho b(\mathbf V\cdot\mathbf n)\,dA$. Both are, at bottom, the statement that a conserved quantity cannot accumulate or vanish inside a region without a matching flux crossing its boundary.

## Related
- [[Fluid Mechanics/04 Control Volume Analysis/Conservation of Mass (Continuity Equation)|Conservation of Mass (Continuity Equation)]]
- [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]
- [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Nodal and Mesh Analysis (AC)|Cross-domain: Nodal Analysis (AC) — the electrical version of the same bookkeeping]]
