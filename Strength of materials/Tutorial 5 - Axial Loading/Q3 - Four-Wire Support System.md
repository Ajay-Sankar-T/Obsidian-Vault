# AM2200 Tutorial 5 — Q3: Four-Wire Support System

Q3 asks for the vertical displacement of the 800-lb load supported by four identical 304 stainless-steel wires. Each wire has $A=0.05\text{ in}^2, E=28(10^3)\text{ ksi}$.
Upper wires: $4\text{ ft}$. Lower wires: $4.5\text{ ft}$.
Rigid members $AB$ and $DC$ are initially horizontal.
$DC=7\text{ ft}, AB=6\text{ ft}$. Load is $1\text{ ft}$ from $A$.

## 1. Theory
**Axial deformation**: $\boxed{\delta=\frac{TL}{AE}}$.
**Rigid members**: They do not deform; displacement varies linearly along the member.

## 2. Solution
### Forces in lower wires (Rigid member $AB$)
Taking moments about $A$: $\sum M_A=0 \Rightarrow T_B(6)-800(1)=0 \Rightarrow \boxed{T_B=133.33\text{ lb}}$.
Vertical equilibrium: $T_A+T_B=800 \Rightarrow \boxed{T_A=666.67\text{ lb}}$.

### Deformation of lower wires ($L=54\text{ in}, E=28\times 10^6\text{ psi}$)
- $\delta_{A,\text{lower}} = \frac{666.67 \times 54}{0.05 \times 28\times 10^6} = \boxed{0.02571\text{ in}}$
- $\delta_{B,\text{lower}} = \frac{133.33 \times 54}{0.05 \times 28\times 10^6} = \boxed{0.005143\text{ in}}$

### Forces and Deformation of upper wires ($L=48\text{ in}$)
Forces are the same as lower wires: $T_{DE}=666.67\text{ lb}, T_{CF}=133.33\text{ lb}$.
- $\delta_{D,\text{upper}} = \frac{666.67 \times 48}{0.05 \times 28\times 10^6} = \boxed{0.022857\text{ in}}$
- $\delta_{C,\text{upper}} = \frac{133.33 \times 48}{0.05 \times 28\times 10^6} = \boxed{0.004571\text{ in}}$

### Total Displacement of A and B
- $\delta_A = \delta_{D,\text{upper}} + \delta_{A,\text{lower}} = 0.022857 + 0.025714 = \boxed{0.048571\text{ in}}$
- $\delta_B = \delta_{C,\text{upper}} + \delta_{B,\text{lower}} = 0.004571 + 0.005143 = \boxed{0.009714\text{ in}}$

### Displacement of the Load ($H$)
Load is $1/6$ of the way from $A$ to $B$:
$$ \delta_H = \delta_A + \frac{1}{6}(\delta_B - \delta_A) = 0.048571 + \frac{1}{6}(0.009714 - 0.048571) = \boxed{0.0421\text{ in downward}} $$

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[02 Axial Loading]]
- [[Q1 - Axially Loaded Member]]
- [[Q6 - Bolt and Tube Assembly]]
