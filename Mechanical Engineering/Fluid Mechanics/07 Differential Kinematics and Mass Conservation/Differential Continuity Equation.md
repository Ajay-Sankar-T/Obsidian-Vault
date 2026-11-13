---
tags: [concept, fluid-mechanics, kinematics, continuity]
status: draft
aliases: [differential mass conservation, continuity equation, divergence of velocity, incompressible flow condition]
up: "[[Fluid Mechanics - MOC]]"
---

# Differential Continuity Equation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Conservation of Mass (Continuity Equation)|Integral Continuity]], [[Material Derivative and Fluid Acceleration|Material Derivative]] · formulas: [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank §2]]

## Core Idea

> **One-sentence definition:** at every point in a flow, the rate at which density rises equals minus the divergence of the mass flux: $\partial\rho/\partial t+\nabla\cdot(\rho\mathbf V)=0$; for incompressible flow this reduces to $\nabla\cdot\mathbf V=0$.

**Intuition:** mass is neither created nor destroyed. If more fluid flows out of a tiny box than flows in, the density inside must drop. In incompressible flow the density cannot change, so what goes in must come out through the other faces: velocity has zero divergence.

## Governing Relation

$$\boxed{\frac{\partial\rho}{\partial t}+\frac{\partial(\rho u)}{\partial x}+\frac{\partial(\rho v)}{\partial y}+\frac{\partial(\rho w)}{\partial z}=0}\quad\Longleftrightarrow\quad\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf V)=0$$

Following a particle:

$$\frac{D\rho}{Dt}+\rho\,\nabla\cdot\mathbf V=0\qquad\Longrightarrow\qquad\nabla\cdot\mathbf V=-\frac1\rho\frac{D\rho}{Dt}=\frac1{\mathcal V}\frac{D\mathcal V}{Dt}\ \ (\text{dilatation})$$

| Case | Condition |
|---|---|
| steady | $\nabla\cdot(\rho\mathbf V)=0$ |
| **incompressible** (steady or unsteady) | $\boxed{\nabla\cdot\mathbf V=u_x+v_y+w_z=0}$ |
| plane incompressible | $u_x+v_y=0$, so a stream function exists: $u=\psi_y,\ v=-\psi_x$ |
| cylindrical, incompressible | $\dfrac1r\dfrac{\partial(rv_r)}{\partial r}+\dfrac1r\dfrac{\partial v_\theta}{\partial\theta}+\dfrac{\partial v_z}{\partial z}=0$ |

**Where:** $(u,v,w)$ = velocity components; $\rho$ = density.

**Assumptions:** a continuum with no sources or sinks inside the element. It holds for viscous or inviscid, steady or unsteady flow.

## Visual

Draw an element $dx\,dy\,dz$ with mass entering on the left face and leaving on the right face: net outflow in $x$ is $\partial(\rho u)/\partial x\,dx\,dy\,dz$. The sum of the three directional net outflows equals the rate of decrease of the mass inside, $-\partial\rho/\partial t\,dx\,dy\,dz$. (The motion figures in [[Motion of a Fluid Element|Motion of a Fluid Element]] show the same box deforming with constant area when $\nabla\cdot\mathbf V=0$.)

## When To Use

- **Check** that a proposed velocity field is physically possible.
- **Find a missing component**: given $u$ (and $w$), integrate to get $v$.
- Introduce the **stream function** in 2-D incompressible flow.
- Decide the incompressibility condition from $\nabla\cdot\mathbf V\approx0$.

**Recognition pattern:** "is this flow incompressible?", "find $v$ given $u$", "satisfies conservation of mass" → **$\nabla\cdot\mathbf V=0$**.

## Method

1. **Identify** whether the flow is compressible (then keep $\rho$) or incompressible ($Ma<0.3$, liquids).
2. **Choose** the coordinate system (Cartesian or cylindrical) to match the geometry.
3. **Apply** the divergence; to find a missing component, integrate: $\partial v/\partial y=-\partial u/\partial x$ gives $v=-\int(\partial u/\partial x)\,dy+f(x,t)$.
4. **Check:** fix the "constant" $f(x,t)$ by a boundary condition (usually $v=0$ at a wall); confirm $\nabla\cdot\mathbf V=0$ after substitution.

## Derivation / Why It Works

Mass flows through the six faces of a fixed element $dx\,dy\,dz$. Inflow minus outflow in $x$: $-\dfrac{\partial(\rho u)}{\partial x}dx\,dy\,dz$, and similarly for $y,z$. This equals the accumulation $\dfrac{\partial\rho}{\partial t}dx\,dy\,dz$. Equivalently, apply the divergence theorem to the integral form in [[Conservation of Mass (Continuity Equation)|Conservation of Mass]]: $\oint\rho\mathbf V\cdot\mathbf n\,dA=\int\nabla\cdot(\rho\mathbf V)\,dV$; since the control volume is arbitrary, the integrand must vanish.

## Common Traps

- **Trap:** using the incompressible form when the density varies in time or space.
  - **Avoid it by:** checking $Ma$; use the full equation for gases above $Ma\approx0.3$.
- **Trap:** forgetting the **function of integration** $f(x,t)$ when integrating continuity.
- **Trap:** confusing "steady" with "incompressible": a steady compressible flow has $\nabla\cdot(\rho\mathbf V)=0$, not $\nabla\cdot\mathbf V=0$.
- **Trap:** applying the Cartesian divergence to polar components (the factors $1/r$ matter).

## Example

### Given
A 2-D incompressible flow with $u=x^2-y^2$ (check later: is this a possible flow?) and $v=0$ at the wall $y=0$. Find $v$. Also test the radial flow $v_r=Q/(2\pi rh)$, $v_\theta=0$.

### Solution
$$\frac{\partial v}{\partial y}=-\frac{\partial u}{\partial x}=-2x\ \Rightarrow\ v=-2xy+f(x).$$
$v(x,0)=0\Rightarrow f(x)=0$, hence $\boxed{v=-2xy}$. Check: $u_x+v_y=2x-2x=0$ ✓.

Radial flow: $\dfrac1r\dfrac{d(rv_r)}{dr}=\dfrac1r\dfrac{d}{dr}\Big(\dfrac Q{2\pi h}\Big)=0$ ✓ (a line source of strength $Q/h$).

**Answer:** $v=-2xy$; the radial source flow conserves mass for $r>0$.
**Key takeaway:** continuity alone fixes one component once the others are known, up to a boundary-condition function.

## Connections

### Prerequisites
- [[Conservation of Mass (Continuity Equation)|Conservation of Mass (Integral Form)]]
- [[Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]

### Related Concepts
- [[Motion of a Fluid Element|Motion of a Fluid Element]] — $\nabla\cdot\mathbf V$ is the rate of volume change.
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]] — stream function and potential.
- [[Density, Specific Weight and Compressibility|Density and Compressibility]] — when $D\rho/Dt$ can be dropped.

### Next
- [[Motion of a Fluid Element|Motion of a Fluid Element]], [[Euler's Equations of Fluid Motion|Euler's Equations]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — $\nabla\cdot\mathbf V=0$ is Kirchhoff's current law in the continuum: no charge (volume) accumulates at a node.
- [[Fluid Flow, Continuity and Bernoulli|Fluid Flow, Continuity and Bernoulli (Physics)]] — the divergence theorem derivation of the same equation.

## Quick Recall

> **In one line:** $\partial_t\rho+\nabla\cdot(\rho\mathbf V)=0$; incompressible means $\nabla\cdot\mathbf V=0$.

**Formula / trigger:** $$\nabla\cdot\mathbf V=u_x+v_y+w_z=0$$

**Remember:** integrate with a function $f(x,t)$ and fix it with the wall condition.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]
