---
tags: [concept, manufacturing]
course: "Manufacturing Technology (ME2302 / ME3305)"
aliases: [Orthogonal cutting, Merchant circle, Shear angle, Chip thickness ratio, Machining mechanics, Specific cutting energy, Cutting forces]
---

# Orthogonal Cutting — Merchant's Shear Plane Model

> [!abstract] In one breath
> In machining the tool shears a thin layer of metal ahead of it along a **shear plane**; the chip then slides up the tool face. Measure the **chip thickness ratio** $r=t_0/t_c$ and the two forces on the tool, and you get the shear angle, shear strain, friction and shear stress. **Merchant's circle** makes all of these components of one resultant force.

Part of [[Manufacturing Technology - MOC]]. Previous: [[Sheet Metal Forming - Blanking, Bending and Deep Drawing]]. Next: [[Tool Life and Machining Economics]].

## 1. Orthogonal model

An edge perpendicular to the cutting speed $V$, an uncut chip thickness $t_0$ (the feed), width $w$, rake angle $\alpha$ (positive when the face leans away from the work). The chip leaves with thickness $t_c>t_0$ (it is compressed and thickened):

$$
r=\frac{t_0}{t_c},\qquad \tan\phi=\frac{r\cos\alpha}{1-r\sin\alpha}
$$

$\phi$ is the **shear angle**. The shear strain in the chip:

$$
\gamma=\cot\phi+\tan(\phi-\alpha)
$$

Small $\phi$ (a thick chip, $r$ small) means more strain, more work, more heat. A larger rake angle increases $\phi$ and reduces the cutting force.

## 2. Forces: Merchant's circle

Measured with a dynamometer: **cutting force** $F_c$ (along $V$) and **thrust force** $F_t$ (perpendicular, into the work). The resultant $R=\sqrt{F_c^2+F_t^2}$ resolves two ways:

On the tool face (friction angle $\beta$, $\mu=\tan\beta$):

$$
F=F_c\sin\alpha+F_t\cos\alpha\ \ (\text{friction}),\quad N=F_c\cos\alpha-F_t\sin\alpha\ \ (\text{normal})
$$

On the shear plane:

$$
F_s=F_c\cos\phi-F_t\sin\phi,\qquad \tau_s=\frac{F_s}{A_s},\ A_s=\frac{t_0w}{\sin\phi}
$$

**Power and specific energy:** $P=F_cV$ and $u=F_c/(t_0w)$ (J/mm³): the energy to remove a unit volume. $u$ is the key machinability number: typically steels 2–6, aluminium alloys 0.4–1, cast iron 1–5 J/mm³.

**Merchant's relation** for the shear angle (minimum energy) and the Lee–Shaffer slip-line version:

$$
\phi=45^\circ+\frac\alpha2-\frac\beta2\ \ (\text{Merchant}),\qquad \phi=45^\circ+\alpha-\beta\ \ (\text{Lee–Shaffer})
$$

Both say: raise the rake angle or lower the friction (lubricant, coating) and the shear angle rises, so the cut becomes easier.

## 3. Worked example

Uncut thickness $t_0=0.25$ mm, chip $t_c=0.50$ mm, width $w=3$ mm, rake $\alpha=10^\circ$, $F_c=1200$ N, $F_t=500$ N, $V=2$ m/s.

| Quantity | Value |
| --- | --- |
| $r=0.25/0.50$ | 0.50 |
| shear angle $\phi$ | **28.3°** |
| shear strain $\gamma$ | **2.19** |
| resultant $R$ | 1300 N |
| friction force $F$ | 701 N |
| normal force $N$ | 1095 N |
| friction coefficient $\mu=F/N$ | **0.64** ($\beta=32.6^\circ$) |
| shear force $F_s$ | 819 N |
| shear area $A_s=t_0w/\sin\phi$ | 1.58 mm² |
| **shear stress $\tau_s$** | **518 MPa** |
| power $F_cV$ | **2.4 kW** |
| specific energy $F_c/(t_0w)$ | **1.6 J/mm³** |

The measured $\phi=28.3^\circ$ is below Merchant's $45+5-16.3=33.7^\circ$ and near Lee–Shaffer's $22.4^\circ$: the models bracket the real chip. The friction coefficient of 0.64 is large; in machining, the high pressure and fresh metal surface make sticking friction, not Coulomb sliding.

![[MFG-4-cutting.png]]

## 4. Other aspects

- **Chip types:** continuous (ductile, high speed, positive rake), built-up edge (low speed: metal welds to the face), discontinuous (brittle materials), serrated.
- **Heat:** most of the energy appears as heat, about 75 % in the shear zone and the rest in the tool-chip friction, carried away mostly by the chip. Tool temperature, not force, limits tool life ([[Tool Life and Machining Economics]]).
- **Real processes** (turning, milling, drilling) are 3-D, but use the orthogonal results as a first model; the forces scale with $t_0$ and $w$.

> [!warning] Traps
> - Using $t_c/t_0$ as $r$: the ratio is $t_0/t_c<1$.
> - Mixing up the friction angle $\beta$ with the rake $\alpha$ in Merchant's formula.
> - Treating the thrust as the cutting force: $F_c$ (along the velocity) does the work.
> - Using total $w\times t_0$ with $F_t$ instead of $F_c$ for the specific energy.
> - Neglecting that the measured forces include the **ploughing** at the edge for very small $t_0$.

> [!question]- Predict first: increase the rake angle from 10° to 20° at the same $r$. What happens to $\phi$ and to the shear strain?
> $\phi$ rises: $\tan\phi=0.5\cos20/(1-0.5\sin20)=0.5671$, so $\phi=29.6^\circ$ (against 28.3°). The shear strain falls: $\gamma=\cot\phi+\tan(\phi-\alpha)=1.76+0.17=1.93$ (against 2.19). A bigger rake gives an easier cut with less strain; the price is a weaker edge.

> [!question]- Why does cutting force depend mostly on $t_0$ and little on speed?
> The shear strength of the metal sets $\tau_s$; speed changes it only a little (thermal softening against strain-rate hardening). The force is the shear stress times the shear area, which is proportional to $t_0w$, so doubling the feed doubles $F_c$ but doubling the speed doubles the **power**.

## 5. Connections

- [[Mohr's Circle for Stress]] — Merchant's circle is a force circle with the same geometry as Mohr's circle: a resultant resolved in two frames.
- [[Static Failure Theories - Tresca and von Mises]] — $\tau_s$ is the shear flow stress; $0.577S_y$ or higher at the large strain of $\gamma\approx2$.
- [[Sheet Metal Forming - Blanking, Bending and Deep Drawing]] — blanking is orthogonal cutting without the chip, with the same shear and friction.
- [[Plane Kinematics of Rigid Bodies]] — the chip velocity triangle ($V$, $V_s$, $V_c$) is a relative-velocity diagram.
