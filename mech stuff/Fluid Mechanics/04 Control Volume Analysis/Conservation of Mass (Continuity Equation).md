---
tags: [fluid-mechanics, control-volume, continuity]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Conservation of Mass (Continuity Equation)

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/04 Control Volume Analysis/Reynolds Transport Theorem|Reynolds Transport Theorem]]

## From RTT to mass conservation

Set $B=m,\ b=1$ in [[Fluid Mechanics/04 Control Volume Analysis/Reynolds Transport Theorem|Reynolds Transport Theorem]]. Since the mass of a system is, by definition, conserved, $dm_{\rm system}/dt=0$, so:

$$\boxed{\frac{\partial}{\partial t}\int_{CV}\rho\,dV+\oint_{CS}\rho(\mathbf V\cdot\mathbf n)\,dA=0}$$

$$\boxed{\text{Accumulation}+\text{Net outflow}=0}\qquad\text{i.e.}\qquad\boxed{\text{Accumulation}=\text{Inflow}-\text{Outflow}}$$

## Mass flow rate

$$\boxed{\dot m=\int_A\rho(\mathbf V\cdot\mathbf n)\,dA}\qquad\text{uniform flow: }\boxed{\dot m=\rho AV}\quad[\text{kg/s}]$$

## Steady flow continuity

For steady flow the accumulation term vanishes:

$$\boxed{\sum\dot m_{\rm in}=\sum\dot m_{\rm out}}$$

One inlet, one outlet: $\rho_1A_1V_1=\rho_2A_2V_2$. For incompressible flow ($\rho_1=\rho_2$):

$$\boxed{A_1V_1=A_2V_2}\qquad\text{Memory: smaller area}\Rightarrow\text{higher velocity}$$

## Differential (pointwise) form

$$\boxed{\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf V)=0}\qquad\text{incompressible: }\boxed{\nabla\cdot\mathbf V=0}$$

Cartesian, 3D: $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}+\dfrac{\partial w}{\partial z}=0$; 2D: $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}=0$.

## Cross-domain: continuity is KCL, is inductor current continuity, is Castigliano compatibility

$\dot m_{\rm in}=\dot m_{\rm out}$ (steady, no accumulation) is the direct fluid-mechanics analogue of $\sum I_{\rm in}=\sum I_{\rm out}$ ([[Nodal and Mesh Analysis (AC)|Nodal Analysis]]'s KCL) — both are the steady-state special case of [[Fluid Mechanics/04 Control Volume Analysis/Reynolds Transport Theorem|Reynolds Transport Theorem]]'s "accumulation = 0." More surprisingly, the **unsteady** accumulation term $\partial(\rho V_{CV})/\partial t\ne0$ (e.g. a tank filling up) is mathematically the same statement as [[AC Transients|capacitor voltage continuity]] $v_C(0^+)=v_C(0^-)$: both say a conserved "stored" quantity (fluid mass in a tank; charge on a capacitor) cannot jump instantaneously — only *changes* at a finite rate set by the net flow through the boundary. (Earlier this paragraph paired the tank with inductor current continuity; the inductor's twin is the fluid's inertia, see [[Cross-Domain Synthesis/Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]].) $A_1V_1=A_2V_2$'s "smaller area, higher velocity" is, in the impedance analogy of [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]], the geometric version of a series circuit forcing the same current through every element regardless of each element's own "resistance" to it.

## Related
- [[Fluid Mechanics/04 Control Volume Analysis/Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]
- [[Nodal and Mesh Analysis (AC)|Cross-domain: Nodal and Mesh Analysis (AC) — KCL]]
