---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME3105)"
aliases: [Turbomachines, Euler turbomachine equation, Velocity triangles, Degree of reaction, Pump, Turbine, Compressor, Affinity laws, Specific speed]
---

# Turbomachines — Euler Equation and Velocity Triangles

> [!abstract] In one breath
> A turbomachine passes fluid through a **rotor** that exchanges energy with it by changing the fluid's **angular momentum**. Take the angular-momentum balance over a control volume and you get the **Euler equation**, $w=u_2c_{\theta2}-u_1c_{\theta1}$, whatever the machine. **Velocity triangles** at the inlet and the outlet supply the three velocities that go into it.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Combustion - Stoichiometry, Heating Value and Flame Temperature]]. Next: [[Isentropic Nozzle Flow and Choking]].

## 1. Classes

| Class | Examples | Energy flow |
| --- | --- | --- |
| **Turbomachines** (continuous flow, rotor with blades) | pumps, fans, compressors (absorb work), turbines (produce work) | fluid ↔ rotor |
| Positive displacement | piston pumps, gear pumps, Roots blowers | trapped volume pushed |
| By flow direction | **axial**, radial (centrifugal), mixed | |
| By fluid | hydraulic (incompressible: water turbines, pumps) or thermal (compressible: gas and steam) | |

## 2. Velocity triangles

At any station the fluid's **absolute velocity** $\vec c$ is the vector sum of the **blade speed** $\vec u=\omega r$ and the **relative velocity** $\vec w$ (the velocity seen by the blade):

$$
\vec c=\vec u+\vec w
$$

Components: axial $c_x$ (or meridional $c_m$ in a radial machine) and tangential $c_\theta$. The relative flow follows the blade, so the blade angle fixes the direction of $\vec w$: the exit angle $\beta_2$ sets $w_{\theta2}$.

## 3. The Euler equation

The torque on the fluid equals the rate of change of its angular momentum, so $T=\dot m(r_2c_{\theta2}-r_1c_{\theta1})$ and the power is $\omega T$:

$$
\boxed{\;w=u_2c_{\theta2}-u_1c_{\theta1}\;}\ \ \text{(specific work, J/kg, positive when the fluid receives work)}
$$

It is the [[Linear Momentum Equation]] taken about the axis. Sign convention: $w>0$ for pumps and compressors, $w<0$ for turbines (many texts write $w=u_1c_{\theta1}-u_2c_{\theta2}$ for a turbine so that it is positive).

**Degree of reaction** $R$: the fraction of the stage's energy transfer that appears as a static-pressure (enthalpy) change in the rotor. $R=0$: **impulse** stage (all drop in the nozzle; rotor only deflects the jet); $R=0.5$: **symmetric** blading.

**Machine head:** for a pump, $H=w/g$ (ideal); real $H=\eta_h\,w/g$ (slip, friction).

## 4. Worked examples

**Centrifugal pump.** Impeller outer radius 0.15 m at 1450 rpm: $u_2=22.8$ m/s. Backward-curved blades, $\beta_2=25^\circ$ to the tangent, radial flow velocity $c_{m2}=2.5$ m/s, no prewhirl ($c_{\theta1}=0$):

$$
c_{\theta2}=u_2-\frac{c_{m2}}{\tan\beta_2}=22.8-\frac{2.5}{0.466}=17.4\ \text{m/s},\quad
w=u_2c_{\theta2}=397\ \text{J/kg},\quad H=\frac wg=\mathbf{40.4\ m}
$$

(ideal head; slip and friction lower it by 20–40 %). Since $H\propto u_2^2$, the head comes mostly from the tip speed.

**Axial turbine stage.** Mean blade speed $U=300$ m/s, constant axial velocity $c_x=150$ m/s, nozzle exit angle $\alpha_2=60^\circ$ from the axial direction, axial exit ($c_{\theta3}=0$):

| Quantity | Value |
| --- | --- |
| $c_{\theta2}=c_x\tan60^\circ$ | 260 m/s |
| **work** $w=U\,c_{\theta2}$ | **77.9 kJ/kg** |
| $w_{\theta2}=c_{\theta2}-U$, $\beta_2$ | −40 m/s, −15.0° |
| $w_{\theta3}=-U$, $\beta_3$ | −300 m/s, −63.4° |
| rotor enthalpy drop $(w_3^2-w_2^2)/2$ | **44.2 kJ/kg** |
| **degree of reaction** $R=\Delta h_{rotor}/w$ | **0.57** |

The relative flow is accelerated through the rotor ($w_3=335>w_2=155$ m/s): the rotor does part of the expansion.

![[FTE-6-velocity-triangles.png]]

## 5. Similarity and the affinity laws

The groups from [[Buckingham Pi Theorem]]: **flow coefficient** $\varphi=Q/(ND^3)$, **head coefficient** $\psi=gH/(N^2D^2)$, **power coefficient** $\pi_P=P/(\rho N^3D^5)$. Geometrically similar machines at similar operating points share the coefficients, so for the same pump at a different speed:

$$
Q\propto N,\qquad H\propto N^2,\qquad P\propto N^3
$$

Doubling the speed doubles the flow, quadruples the head and multiplies the power by 8. **Specific speed** $N_s=N\sqrt Q/(gH)^{3/4}$ classifies the machine: low (radial, high head) to high (axial, low head, high flow).

## 6. Efficiencies and performance

Pump: $\eta=\rho gQH/P_{shaft}$; compressor (adiabatic) $\eta_c=(h_{2s}-h_1)/(h_2-h_1)$; turbine $\eta_t=(h_1-h_2)/(h_1-h_{2s})$. A **performance map** plots head (or pressure ratio) against flow with efficiency contours; the operating point is the intersection with the system curve. A compressor map has a **surge** limit on the low-flow side (flow reversal) and **choke** on the high side ([[Isentropic Nozzle Flow and Choking]]).

> [!warning] Traps
> - Measuring the blade angle $\beta$ from the axial direction in one place and from the tangent in another: state the convention.
> - Using the absolute velocity components in the relative triangle.
> - Taking $w=u(c_{\theta2}-c_{\theta1})$ for a radial machine: $u_1\ne u_2$.
> - Forgetting that real pump head is much less than Euler's (slip and losses).
> - Applying affinity laws to different-sized machines without the diameter factors.

> [!question]- Predict first: double the pump speed. By what factor does the head rise, and the power?
> Head $\times4$ ($H\propto N^2$) and power $\times8$ ($P\propto N^3$) at the same flow coefficient, with the flow doubling. This is why throttling a pump by a valve wastes power compared with slowing the motor.

> [!question]- Why do backward-curved blades give a stable pump?
> $c_{\theta2}=u_2-c_{m2}/\tan\beta_2$ falls as the flow rises, so the head falls with flow: a drooping characteristic that is stable. Forward-curved blades give a rising characteristic and risk surging.

## 7. Connections

- [[Linear Momentum Equation]] and [[Momentum Equation Applications - Jets, Vanes, Bends]] — the Euler equation is angular momentum; a vane deflecting a jet is a turbine blade.
- [[Reynolds Transport Theorem]] and [[System and Control Volume]] — control volume around the rotor.
- [[Buckingham Pi Theorem]] and [[Dimensional Analysis and Similitude - Formula Bank]] — the non-dimensional groups and the affinity laws.
- [[Rankine Cycle - Superheat, Reheat and Regeneration]] and [[Brayton Cycle - Intercooling, Reheat and Regeneration]] — turbines and compressors in cycles.
- [[Plane Kinematics of Rigid Bodies]] — $\vec c=\vec u+\vec w$ is the relative-velocity (rotating frame) relation.
