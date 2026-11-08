---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Fourier's law, Thermal resistance, Composite wall, Critical radius of insulation, Overall heat transfer coefficient]
---

# Steady Conduction and Thermal Resistance Networks

> [!abstract] In one breath
> **Fourier's law** says heat flows down a temperature gradient, $q''=-k\,dT/dx$. In steady 1-D flow the same heat rate passes every layer, so each layer acts as a **resistance** $R=\Delta T/Q$ and layers in series simply add, exactly like resistors. Almost every wall, pipe and insulation problem is that one picture.

Part of [[Heat Transfer - MOC]]. Next: [[Extended Surfaces - Fins]].

## 1. Fourier's law and the heat equation

$$
q''_x=-k\frac{dT}{dx}\quad(\text{W/m}^2),\qquad
\rho c\frac{\partial T}{\partial t}=\nabla\!\cdot(k\nabla T)+\dot q
$$

Steady, no generation, constant $k$: $\nabla^2T=0$. In 1-D the temperature profile is linear in a plane wall, logarithmic in a cylinder, and $1/r$ in a sphere.

## 2. Resistances

| Element | Resistance $R$ (K/W) | Heat rate |
| --- | --- | --- |
| Plane wall, thickness $L$, area $A$ | $\dfrac{L}{kA}$ | $Q=\dfrac{\Delta T}{R}$ |
| Convection film | $\dfrac{1}{hA}$ | |
| Cylinder shell $r_1\to r_2$, length $\ell$ | $\dfrac{\ln(r_2/r_1)}{2\pi k\ell}$ | |
| Sphere shell | $\dfrac{1}{4\pi k}\Big(\dfrac1{r_1}-\dfrac1{r_2}\Big)$ | |
| Radiation to surroundings | $\dfrac{1}{h_rA}$, $h_r=\varepsilon\sigma(T_s+T_{sur})(T_s^2+T_{sur}^2)$ | |

Series: $R_{tot}=\sum R_i$. Parallel: $1/R_{tot}=\sum 1/R_i$. Overall coefficient: $UA=1/R_{tot}$, so $Q=UA\,\Delta T$. Temperature at each interface follows from $T_{i+1}=T_i-QR_i$.

## 3. Worked example: an insulated wall

Brick 0.20 m ($k=0.7$), insulation 0.05 m ($k=0.04$), plaster 0.02 m ($k=0.8$); $A=10$ m²; room at 22 °C ($h_i=8$), outside $-5$ °C ($h_o=25$ W/m²K).

| Resistance | K/W | share |
| --- | --- | --- |
| inside film | 0.0125 | 7 % |
| brick | 0.0286 | 17 % |
| **insulation** | **0.1250** | **72 %** |
| plaster | 0.0025 | 1 % |
| outside film | 0.0040 | 2 % |
| total | 0.1726 | |

$$
Q=\frac{22-(-5)}{0.1726}=\mathbf{156\ W},\qquad U=\frac{1}{AR_{tot}}=0.58\ \text{W/m}^2\text{K}
$$

Interface temperatures: 22.0 → 20.0 (inner surface) → 15.6 (brick/insulation) → −4.0 (insulation/plaster) → −4.4 (outer surface) → −5.0 °C. The insulation holds 72 % of the resistance and so 72 % of the temperature drop.

![[HT-1-conduction.png]]

## 4. Critical radius of insulation

For a pipe of outer radius $r_1$ with insulation to radius $r_2$ and outside film $h$:

$$
q'=\frac{2\pi(T_i-T_\infty)}{\dfrac{\ln(r_2/r_1)}{k}+\dfrac{1}{h\,r_2}}
\quad\Rightarrow\quad
\frac{dq'}{dr_2}=0\ \text{at}\ r_{cr}=\frac{k}{h}
$$

Below $r_{cr}$, more insulation grows the outside area faster than it adds conduction resistance, so **the loss rises** to a maximum at $r_{cr}$ and then falls.

Example: $r_1=10$ mm, $k=0.15$, $h=10$: $r_{cr}=15$ mm. The bare pipe loses 50.3 W/m; at $r_2=15$ mm the loss is **53.6 W/m** (up 7 %); only beyond $r_2=24$ mm does insulation beat the bare pipe, and at 50 mm it cuts the loss to 39.5 W/m. This matters for thin wires and small tubes; for large pipes $r_1>r_{cr}$ and any insulation helps.

> [!warning] Traps
> - Using $L/kA$ for a cylinder: the area changes with $r$, so use the logarithmic form.
> - Forgetting the film resistances $1/hA$ at the surfaces: often they are the main resistance when $k$ is high (a metal wall).
> - Adding resistances for layers in *parallel* (studs bridging insulation). They combine as conductances.
> - Reading $T_\infty$ as the surface temperature. The surface temperature is found *after* the film resistance.

> [!question]- Predict first: a 2 mm copper wire, $h=10$, plastic coating $k=0.2$. Does a thin coating cool the wire or heat it?
> $r_{cr}=k/h=20$ mm, far above the wire's 1 mm radius. Any coating up to an outer radius of 20 mm *raises* the heat loss, so the wire runs **cooler** (the extra outer area outweighs the added conduction resistance). Insulation only starts to hold heat in once the outer radius is well past 20 mm. This is why a thin plastic coat on a current-carrying wire is no thermal problem.

> [!question]- Why does the wall's heat rate not depend on where you put the insulation?
> In series the resistances simply add, so the order of layers changes the interface temperatures (important for condensation, freezing and thermal stress) but not $Q$.

## 5. Connections

- [[Series-Parallel Resistance Reduction]] — same algebra, with $\Delta T\leftrightarrow\Delta V$, $Q\leftrightarrow I$, $R_{th}\leftrightarrow R$. [[Conservation Laws and Flow Networks]] shows the same bookkeeping for flow networks.
- [[Fluids and Solids - Pressure, Stress and Constitutive Laws]] — Fourier's law is a third linear constitutive law, next to Hooke's and Newton's.
- [[Thermal Stresses]] — the temperature profile found here is the input to restrained-expansion stress.
- [[Viscous Flow and Exact Solutions - Formula Bank]] — the 1-D diffusion equation $\nabla^2T=0$ is the temperature twin of the velocity profile $u''=\text{const}$.
