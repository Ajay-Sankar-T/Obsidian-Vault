---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Lumped capacitance, Biot number, Fourier number, Heisler charts, Transient conduction, One-term solution]
---

# Transient Conduction — Lumped Capacitance and Heisler Charts

> [!abstract] In one breath
> Two numbers decide how a hot body cools. The **Biot number** $Bi=hL_c/k$ compares the resistance inside the body with the resistance of the surface film. If $Bi<0.1$ the body stays at one temperature and cools like an RC circuit (**lumped capacitance**). If not, temperature varies inside and you need the series solution in the **Fourier number** $Fo=\alpha t/L^2$ (the Heisler charts).

Part of [[Heat Transfer - MOC]]. Previous: [[Extended Surfaces - Fins]]. Next: [[Convection Fundamentals - Boundary Layers and Scale Analysis]].

## 1. Lumped capacitance

Energy balance on a body at uniform temperature $T(t)$ in a fluid at $T_\infty$:

$$
\rho Vc\frac{dT}{dt}=-hA(T-T_\infty)\ \Rightarrow\
\frac{T-T_\infty}{T_0-T_\infty}=e^{-t/\tau},\qquad
\tau=\underbrace{\rho Vc}_{C_{th}}\ \underbrace{\frac{1}{hA}}_{R_{th}}
$$

Valid when $Bi=\dfrac{hL_c}{k}<0.1$ with $L_c=V/A$ (a slab of half-thickness $L$ heated on both faces: $L_c=L$; a sphere: $d/6$; a long cylinder: $d/4$).

**Example.** Steel ball, $d=25$ mm, $\rho=7800$, $c=480$, $k=45$, $h=100$, from 500 °C into 25 °C air.

$$
L_c=4.17\ \text{mm},\ Bi=0.0093<0.1,\quad
\tau=\frac{\rho cL_c}{h}=156\ \text{s},\quad
t_{100^\circ C}=-\tau\ln\frac{100-25}{500-25}=\mathbf{288\ s}
$$

## 2. When $Bi$ is not small: the slab series solution

For a slab of thickness $2L$ at uniform $T_0$ whose faces are suddenly exposed to a fluid, the centre temperature is a sum of decaying cosines:

$$
\theta^*_0=\frac{T_0^{\text{centre}}-T_\infty}{T_i-T_\infty}=\sum_{n}C_n e^{-\zeta_n^2Fo},\quad
\zeta_n\tan\zeta_n=Bi,\quad
C_n=\frac{4\sin\zeta_n}{2\zeta_n+\sin2\zeta_n}
$$

For $Fo\gtrsim0.2$ the first term alone is accurate to a few per cent: $\theta_0^*\approx C_1e^{-\zeta_1^2Fo}$. The Heisler charts are plots of exactly this series; **the table below replaces the chart**.

| $Bi$ | $\zeta_1$ | $C_1$ | $Fo$ for $\theta_0^*=0.1$ |
| --- | --- | --- | --- |
| 0.1 | 0.311 | 1.016 | 24.0 |
| 1 | 0.860 | 1.119 | 3.26 |
| 10 | 1.429 | 1.262 | 1.24 |

$Bi\to0$ gives $\zeta_1^2\approx Bi$, $C_1\to1$, so $\theta^*_0=e^{-Bi\,Fo}$: the lumped result, since $Bi\cdot Fo=ht/(\rho cL)$. $Bi\to\infty$ gives $\zeta_1\to\pi/2$: the surface is held at $T_\infty$ and the body cools at the diffusion rate $e^{-(\pi/2)^2Fo}$.

![[HT-3-transient.png]]

## 3. Method

1. Compute $Bi$ with the geometry's $L_c=V/A$.
2. $Bi<0.1$: use $e^{-t/\tau}$.
3. Otherwise compute $Fo$, read $\zeta_1$ and $C_1$ (table or solve $\zeta\tan\zeta=Bi$), and use the one-term form for $Fo>0.2$.
4. Off-centre or surface temperatures multiply by $\cos(\zeta_1x/L)$ (plane wall).

> [!warning] Traps
> - Using $L_c=V/A$ in the **series** solution: Heisler charts use the half-thickness (or radius) $L$ and $Bi=hL/k$.
> - Applying one term at $Fo<0.2$.
> - Using the diameter instead of $V/A$ in the Biot number: $d/6$ for a sphere is a factor 6 smaller.
> - Applying the semi-infinite-solid shortcut to a thin body: valid only while $\delta\approx\sqrt{\alpha t}\ll L$.

> [!question]- Predict first: a thick brick wall, $Bi=10$. Does doubling $h$ change the cooling time much?
> No. $Bi\gg1$ means the surface is already close to $T_\infty$ and the time is set by diffusion, $t\approx Fo\,L^2/\alpha$ with $Fo$ nearly constant. Doubling $h$ from $Bi=10$ to $20$ lowers $Fo$ for $\theta_0^*=0.1$ only from 1.24 to 1.14 (about 8 %); even $h\to\infty$ gives 1.03.

> [!question]- The ball is 10 times larger ($d=250$ mm) with the same $h$. Is lumped analysis still valid?
> $L_c=41.7$ mm, $Bi=100(0.0417)/45=0.093$: borderline ($<0.1$). The time constant is 10 times longer (1560 s) and the centre lags the surface by a few per cent.

## 4. Connections

- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — $\tau=R_{th}C_{th}$ is the same time constant as an RC circuit.
- [[04 Capacitors, Inductors and First Order Circuits]] — thermal resistance $1/hA$ and capacitance $\rho Vc$ play the roles of $R$ and $C$.
- [[Measurements, Instrumentation and Control - MOC]] — a thermocouple's lag is a first-order response with this $\tau$; $h$ and the junction size set the measurement delay.
- [[Sturm-Liouville Problems]] — $\zeta_n\tan\zeta_n=Bi$ is a Robin-condition eigenvalue problem, and $C_n$ are Fourier coefficients on the eigenfunctions $\cos\zeta_nx$.
