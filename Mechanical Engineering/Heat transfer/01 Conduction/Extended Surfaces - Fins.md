---
tags: [concept, heat-transfer]
course: "Heat Transfer (ME3101)"
aliases: [Fins, Fin efficiency, Fin effectiveness, Extended surfaces]
---

# Extended Surfaces — Fins

> [!abstract] In one breath
> A fin adds surface where the convection coefficient is low. Heat enters at the base and leaks out along the length, so the fin gets cooler towards the tip: a **1-D conduction problem with a convective sink**, $\theta''=m^2\theta$. The answer is controlled by one number, $mL$.

Part of [[Heat Transfer - MOC]]. Previous: [[Steady Conduction and Thermal Resistance Networks]]. Next: [[Transient Conduction - Lumped Capacitance and Heisler Charts]].

## 1. The fin equation

Take a thin fin of constant cross-section $A_c$, perimeter $P$, conductivity $k$, in a fluid at $T_\infty$ with coefficient $h$. Energy balance on a slice $dx$ (conduction in minus conduction out equals convection from the surface):

$$
\frac{d^2\theta}{dx^2}-m^2\theta=0,\qquad \theta=T-T_\infty,\qquad m=\sqrt{\frac{hP}{kA_c}}
$$

General solution $\theta=C_1\cosh mx+C_2\sinh mx$. Boundary conditions: $\theta(0)=\theta_b$ at the base, and one of four tip conditions:

| Tip | $\theta/\theta_b$ | Heat rate $Q$ |
| --- | --- | --- |
| Infinitely long | $e^{-mx}$ | $M$ |
| **Insulated** | $\dfrac{\cosh m(L-x)}{\cosh mL}$ | $M\tanh mL$ |
| Convecting ($h$ at the tip) | $\dfrac{\cosh m(L-x)+\frac{h}{mk}\sinh m(L-x)}{\cosh mL+\frac{h}{mk}\sinh mL}$ | $M\,\dfrac{\sinh mL+\frac{h}{mk}\cosh mL}{\cosh mL+\frac{h}{mk}\sinh mL}$ |
| Fixed tip temperature | | from $\theta(L)=\theta_L$ |

with $M=\sqrt{hPkA_c}\;\theta_b$. A convecting tip is well approximated by an insulated tip of corrected length $L_c=L+A_c/P$ ($=L+D/4$ for a pin, $L+t/2$ for a thin strip).

## 2. Efficiency and effectiveness

$$
\eta_f=\frac{Q}{hA_f\theta_b}=\frac{\tanh mL}{mL}\quad(\text{insulated tip}),\qquad
\varepsilon_f=\frac{Q}{hA_c\theta_b}
$$

$\eta_f$ compares the real heat rate with an ideal fin at the base temperature everywhere. $\varepsilon_f$ compares the fin with the bare base. A fin only pays if $\varepsilon_f\gtrsim2$ (rule of thumb), i.e. when $k$ is high and $h$ is low.

## 3. Worked example

Aluminium pin fin, $D=5$ mm, $L=50$ mm, $k=200$ W/mK, $h=25$ W/m²K, base 100 °C, air 25 °C.

$$
P=\pi D=15.7\ \text{mm},\ A_c=19.6\ \text{mm}^2,\quad
m=\sqrt{\frac{4h}{kD}}=\sqrt{\frac{4(25)}{200(0.005)}}=10\ \text{m}^{-1},\quad mL=0.5
$$

$$
M=\sqrt{hPkA_c}\,\theta_b=0.0393\times75=2.945\ \text{W},\qquad
Q=M\tanh0.5=\mathbf{1.36\ W}\ (\text{insulated tip})
$$

Convecting tip: $1.390$ W; the corrected-length shortcut gives $1.390$ W, matching. Efficiency $\eta_f=\tanh0.5/0.5=\mathbf{0.924}$; effectiveness $\varepsilon_f=37$. The infinite-fin formula ($M=2.945$ W) would overestimate the heat by a factor of 2 because the tip is still warm: it needs $mL\gtrsim3$.

![[HT-2-fins.png]]

> [!warning] Traps
> - Using the infinite-fin result for a short fin ($mL<3$).
> - Taking $P$ and $A_c$ for the wrong shape: a pin has $P/A_c=4/D$, a rectangular strip $\approx2/t$.
> - Treating the fin as isothermal at $T_b$ for the area: use $\eta_f$.
> - Forgetting that $h$ at the surface is itself uncertain by 20–30 %; a more elaborate tip formula rarely helps.

> [!question]- Predict first: doubling the fin length. Does the heat double?
> No. At $mL=0.5$ doubling $L$ gives $mL=1$: $\tanh1/\tanh0.5=1.65$, so +65 %, and the efficiency falls from 0.92 to 0.76. Beyond $mL\approx2$ extra length buys almost nothing.

> [!question]- Same shape in steel ($k=45$) instead of aluminium?
> $m=10\sqrt{200/45}=21.1$ m⁻¹, so $mL=1.05$ and $\eta_f=0.74$. $M\propto\sqrt k$ falls by $\sqrt{45/200}=0.47$ to 1.40 W, and $Q=1.40\tanh1.05=\mathbf{1.09\ W}$. Steel gives about 20 % less heat than aluminium, even though $k$ is 4.4 times smaller: the heat rate scales only like $\sqrt k$ once the fin is short.

## 4. Connections

- [[2nd Order Linear ODE with Constant Coefficients]] — $\theta''-m^2\theta=0$ is the real-roots case, so cosh/sinh solutions.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — $e^{-mx}$ is spatial relaxation with decay length $1/m$ (here 0.1 m); the infinite fin is the long-distance limit.
- [[Euler Buckling of Columns]] — the same ODE with $+m^2$ gives sines and cosines (buckling), with $-m^2$ gives cosh and sinh (fin). Sign of the term decides oscillation or decay.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — the other sign of the same operator.
