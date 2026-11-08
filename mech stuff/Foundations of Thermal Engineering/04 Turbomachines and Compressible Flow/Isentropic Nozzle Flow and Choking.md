---
tags: [concept, thermal-engineering]
course: "Foundations of Thermal Engineering (ME3105)"
aliases: [Compressible flow, Speed of sound, Mach number, Nozzle, Choked flow, Isentropic flow, Stagnation properties, Converging-diverging nozzle, De Laval nozzle]
---

# Isentropic Nozzle Flow and Choking

> [!abstract] In one breath
> At low speed a gas flows like an incompressible fluid. As the velocity approaches the **speed of sound**, density changes become important and the flow behaves in an unexpected way: **in supersonic flow a duct must widen to speed the gas up**. A converging nozzle can never exceed Mach 1, and once its throat reaches Mach 1 it is **choked**: the mass flow is fixed by the upstream state and the throat area and no longer responds to the back pressure.

Part of [[Foundations of Thermal Engineering - MOC]]. Previous: [[Turbomachines - Euler Equation and Velocity Triangles]].

## 1. Speed of sound and Mach number

A small pressure disturbance travels at $a=\sqrt{(\partial p/\partial\rho)_s}$, which for a perfect gas is

$$
a=\sqrt{\gamma RT},\qquad M=\frac Va
$$

Air at 300 K: $a=347$ m/s. Regimes: subsonic $M<1$, transonic $\approx1$, supersonic $M>1$. Compressibility matters above $M\approx0.3$ (density change above 5 %).

## 2. Stagnation properties and isentropic relations

The **stagnation** (total) state $T_0,p_0$ is what you would measure if the flow were brought to rest isentropically. For a perfect gas:

$$
\frac{T_0}{T}=1+\frac{\gamma-1}2M^2,\qquad
\frac{p_0}{p}=\Big(1+\frac{\gamma-1}2M^2\Big)^{\gamma/(\gamma-1)},\qquad
\frac{\rho_0}{\rho}=\Big(1+\frac{\gamma-1}2M^2\Big)^{1/(\gamma-1)}
$$

In adiabatic flow $T_0$ stays constant (energy: $c_pT+V^2/2=c_pT_0$). For $\gamma=1.4$ the incompressible Bernoulli result is the low-$M$ limit: $p_0-p\approx\tfrac12\rho V^2(1+M^2/4)$, as in [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]].

## 3. Area–Mach relation

Combine mass conservation, momentum and the isentropic relations:

$$
\frac{dA}A=(M^2-1)\frac{dV}V\qquad\Longrightarrow\qquad
\frac{A}{A^*}=\frac1M\Bigg[\frac2{\gamma+1}\Big(1+\frac{\gamma-1}2M^2\Big)\Bigg]^{\frac{\gamma+1}{2(\gamma-1)}}
$$

| Flow | Duct that **accelerates** it | Duct that decelerates it (diffuser) |
| --- | --- | --- |
| Subsonic | converging ($dA<0$) | diverging |
| **Supersonic** | **diverging** ($dA>0$) | converging |

At the minimum area (the **throat**) $M=1$ and $A=A^*$; the same $A/A^*$ gives two Mach numbers, one subsonic and one supersonic. A **converging–diverging (de Laval) nozzle** accelerates a gas through $M=1$ at its throat to supersonic speed in the diverging section. (Rocket engines, steam-turbine nozzles, supersonic wind tunnels.)

![[FTE-7-nozzle.png]]

## 4. Choking

For a converging nozzle fed from a reservoir ($p_0,T_0$) discharging to back pressure $p_b$:

- If $p_b/p_0>0.528$ (for $\gamma=1.4$) the flow is subsonic throughout, and the exit pressure equals $p_b$.
- At $p_b/p_0=\left(\frac2{\gamma+1}\right)^{\gamma/(\gamma-1)}=0.528$ the exit is sonic: the **critical pressure ratio**.
- Below that the nozzle is **choked**: the exit stays at $M=1$, the exit pressure stays at $0.528\,p_0$, the extra drop happens outside the nozzle (shock and expansion waves), and the **mass flow is constant**:

$$
\dot m_{max}=A^*p_0\sqrt{\frac{\gamma}{RT_0}}\Big(\frac2{\gamma+1}\Big)^{\frac{\gamma+1}{2(\gamma-1)}}\ \ (\approx0.0404\,A^*p_0/\sqrt{T_0}\ \text{for air, SI units})
$$

## 5. Worked example: air

Reservoir $p_0=500$ kPa, $T_0=300$ K; throat diameter 20 mm ($A^*=314\ \text{mm}^2$):

| Quantity | Value |
| --- | --- |
| $a_0$ at 300 K | 347 m/s |
| back pressure for choking $0.528\,p_0$ | **264 kPa** |
| throat temperature $T^*=T_0\cdot2/(\gamma+1)$ | 250 K |
| **choked mass flow** | **0.367 kg/s** |
| to reach **$M=2$**: $A/A^*$ | **1.69** |
| at $M=2$: $T=300/1.8$, $a$, $V$, $p$ | 166.7 K, 258.8 m/s, **517.6 m/s**, 63.9 kPa |

Beyond choking, **only raising $p_0$ or lowering $T_0$ increases the flow** ($\dot m\propto p_0/\sqrt{T_0}$). The same fact limits a compressor's flow (choke) and a valve's capacity; and it is why a safety valve or a blowdown is sized by upstream pressure alone.

## 6. Beyond the isentropic nozzle

If the back pressure lies between the choking value and the design value of a de Laval nozzle, a **normal shock** forms in the diverging section (the flow jumps from supersonic to subsonic with a pressure rise, a loss in $p_0$ and an entropy increase). **Friction (Fanno)** and **heat addition (Rayleigh)** flows give additional choking limits in constant-area ducts.

> [!warning] Traps
> - Using $a=\sqrt{\gamma RT}$ with $T$ in Celsius.
> - Using $R=8.314$ J/mol·K instead of the specific gas constant 287 J/kg·K for air.
> - Applying the isentropic relations through a shock: $p_0$ drops across a shock.
> - Assuming that lowering the back pressure always increases the flow: not once the nozzle is choked.
> - Using the throat area for the exit when computing $M_e$ (use $A_e/A^*$).

> [!question]- Predict first: a gas flows supersonically in a converging duct. Does it speed up or slow down?
> It **slows down**. In supersonic flow the area relation reverses: $dA<0$ with $M>1$ gives $dV<0$. A converging duct is a *diffuser* for supersonic flow, which is how supersonic inlets decelerate the air.

> [!question]- Why does the choked mass flow depend on the upstream stagnation pressure?
> The throat is sonic, so $\rho^*V^*=\rho^*a^*$ with both fixed by $p_0$ and $T_0$ alone, and information from the back pressure cannot travel upstream through a sonic throat. Doubling $p_0$ doubles $\dot m$.

## 7. Connections

- [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] — Bernoulli is the $M\to0$ limit of the stagnation relations.
- [[Conservation of Mass (Continuity Equation)]] and [[Linear Momentum Equation]] — the area–Mach relation is mass plus momentum for a perfect gas.
- [[Turbomachines - Euler Equation and Velocity Triangles]] — rocket and turbine nozzles produce the jet and blade velocities; compressor choke.
- [[Pipe Flow and Losses - Formula Bank]] — incompressible pipe losses; at high speed friction chokes a duct (Fanno).
- [[Dimensional Analysis and Similitude - Formula Bank]] — $M$ is the compressibility $\Pi$ group.
