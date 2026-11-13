---
tags: [concept, fluid-mechanics, viscous-flow, constitutive-law]
status: draft
aliases: [Newtonian fluid constitutive law, Stokes relation, viscous stress tensor, bulk viscosity, Stokes hypothesis]
up: "[[Fluid Mechanics - MOC]]"
---

# Newtonian Constitutive Relation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Stress in a Moving Fluid|Stress in a Moving Fluid]], [[Motion of a Fluid Element|Motion of a Fluid Element]], [[Viscosity and Newton's Law of Viscosity|Viscosity]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §4]]

## Core Idea

> **One-sentence definition:** a Newtonian fluid has viscous stress that is a linear, isotropic function of the **rate of strain**: $\tau_{ij}=2\mu\,\dot\varepsilon_{ij}+\lambda\,(\nabla\cdot\mathbf V)\,\delta_{ij}$, with Stokes' choice $\lambda=-\tfrac23\mu$.

**Intuition:** this is the 3-D version of $\tau=\mu\,du/dy$. A solid's stress is proportional to its strain (Hooke's law); a fluid's viscous stress is proportional to how fast it is being strained. "Isotropic" means the fluid has no preferred direction, so only two constants can appear.

## Governing Relations

$$\boxed{\tau_{ij}=2\mu\,\dot\varepsilon_{ij}-\tfrac23\mu\,(\nabla\cdot\mathbf V)\,\delta_{ij}},\qquad\dot\varepsilon_{ij}=\tfrac12\Big(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\Big)$$

The two constants are $\mu$ (shear viscosity) and the bulk viscosity $\kappa=\lambda+\tfrac23\mu$; Stokes' hypothesis sets $\kappa=0$.

**Incompressible flow** ($\nabla\cdot\mathbf V=0$): only $\mu$ remains, and

$$\sigma_{xx}=-p+2\mu\frac{\partial u}{\partial x},\quad\sigma_{yy}=-p+2\mu\frac{\partial v}{\partial y},\quad\sigma_{zz}=-p+2\mu\frac{\partial w}{\partial z}$$
$$\tau_{xy}=\mu\Big(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\Big),\quad\tau_{yz}=\mu\Big(\frac{\partial v}{\partial z}+\frac{\partial w}{\partial y}\Big),\quad\tau_{zx}=\mu\Big(\frac{\partial w}{\partial x}+\frac{\partial u}{\partial z}\Big)$$

Simple shear $u=u(y)$: $\tau_{xy}=\mu\,du/dy$, Newton's law of viscosity.

**Stokes' three assumptions:** (1) $\boldsymbol\tau$ is a linear function of the velocity gradients; (2) the fluid is isotropic; (3) $\boldsymbol\tau=0$ when the fluid is at rest or in rigid-body rotation (so only $\dot{\boldsymbol\varepsilon}$, not the rotation, enters).

**Where:** $\mu$ = dynamic viscosity (Pa·s); $\dot\varepsilon_{ij}$ = rate of strain tensor (1/s).

**Assumptions:** Newtonian (constant $\mu$ at fixed $T$, $p$): water, air, oils, gases. Not for polymers, blood at low shear, paints ([[Newtonian and Non-Newtonian Fluids|non-Newtonian fluids]]).

## Visual

The visual is the decomposition already shown in [[Motion of a Fluid Element|Motion of a Fluid Element]]: of the two parts of the velocity gradient, only the **strain-rate** part (stretching and shearing) produces stress; the rotation part does not. The stress figure in [[Stress in a Moving Fluid|Stress in a Moving Fluid]] shows the components this law fills in.

## When To Use

- Writing the **Navier–Stokes equations** (inserting $\boldsymbol\tau$ in Cauchy's equation).
- Computing **wall shear stress** or the viscous normal stress in a given flow.
- Understanding which fluids it does *not* cover (non-Newtonian).

**Recognition pattern:** "Newtonian fluid", "stress proportional to rate of strain", "viscous normal stress", "stress tensor from a velocity field" → **$\tau_{ij}=2\mu\dot\varepsilon_{ij}$**.

## Method

1. **Identify** the velocity field and check $\nabla\cdot\mathbf V=0$ (incompressible).
2. **Choose** the needed stress component.
3. **Apply** $\tau_{ij}=\mu(\partial_ju_i+\partial_iu_j)$ (incompressible) and add $-p$ on the diagonal for $\sigma_{ij}$.
4. **Check:** shear stress arises from **both** cross derivatives; a rigid rotation gives zero stress; at a no-slip wall in unidirectional flow only $\mu\,\partial u/\partial n$ remains.

## Derivation / Why It Works

Linear and isotropic means the fourth-order tensor connecting $\tau_{ij}$ to $\partial u_k/\partial x_l$ is built from $\delta$'s only, which leaves just two constants ($\lambda,\mu$). Requiring no stress in rigid rotation removes the antisymmetric part of $\nabla\mathbf V$, so $\tau_{ij}=2\mu\dot\varepsilon_{ij}+\lambda\,\delta_{ij}\dot\varepsilon_{kk}$. The trace of this expression gives $\tau_{kk}=(2\mu+3\lambda)\nabla\cdot\mathbf V=3\kappa\nabla\cdot\mathbf V$, so Stokes' $\lambda=-\tfrac23\mu$ sets $\kappa=0$: the mechanical and thermodynamic pressures coincide. For incompressible flow this term vanishes anyway.

## Common Traps

- **Trap:** using only $\mu\,\partial u/\partial y$ for shear stress in a general 2-D flow.
  - **Avoid it by:** including both $\partial u/\partial y$ and $\partial v/\partial x$.
- **Trap:** attributing stress to vorticity: rotation does not stress a Newtonian fluid.
- **Trap:** dropping the viscous normal stresses $2\mu\,\partial u/\partial x$ at a stagnation point; they exist but are small compared with $p$ unless $\mu$ is large.
- **Trap:** applying the law to non-Newtonian fluids.

## Example

### Given
Water ($\mu=10^{-3}$ Pa·s) in the field $u=3y,\ v=2x$ (s⁻¹), and in the stagnation flow $u=Kx,\ v=-Ky$ with $K=10$ s⁻¹.

### Solution
Field 1: $\tau_{xy}=\mu(u_y+v_x)=10^{-3}(3+2)=5\times10^{-3}$ Pa.
Field 2: $\tau_{xx}=2\mu u_x=2(10^{-3})(10)=0.02$ Pa, $\tau_{yy}=-0.02$ Pa, $\tau_{xy}=0$, so
$$\sigma_{xx}=-p+0.02,\qquad\sigma_{yy}=-p-0.02\ \text{Pa}.$$

**Answer:** 0.005 Pa shear in field 1; $\pm0.02$ Pa normal viscous stresses in the stagnation flow.
**Key takeaway:** the viscous stresses in water are tiny compared with the pressure scale (kilopascals), which is why inviscid theory works away from walls.

## Connections

### Prerequisites
- [[Stress in a Moving Fluid|Stress in a Moving Fluid]]
- [[Motion of a Fluid Element|Motion of a Fluid Element]]

### Related Concepts
- [[Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Deborah Number|Deborah Number]] — when a fluid's response is not purely viscous.

### Next
- [[Navier-Stokes Equations|Navier-Stokes Equations]]

### Cross-domain links
- [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]] — a solid obeys $\sigma_{ij}=2G\varepsilon_{ij}+\lambda_L\varepsilon_{kk}\delta_{ij}$ (Lamé constants), the same isotropic linear form with the strain replaced by the strain **rate** and $G\to\mu$.
- [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — $\mu/G$ is the Maxwell relaxation time behind the Deborah number.

## Quick Recall

> **In one line:** Newtonian viscous stress $=2\mu\times$ (strain rate), with no stress from rotation.

**Formula / trigger:** $$\tau_{ij}=\mu\Big(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\Big)\ \ (\text{incompressible})$$

**Remember:** shear stress uses both cross derivatives; $\mu$ replaces $G$, strain rate replaces strain.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]
