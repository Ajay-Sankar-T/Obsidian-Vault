---
title: Pipe Flow and Losses – Formula Bank
tags: [fluid-mechanics, formula-bank, pipe-flow, friction-factor, moody-chart, minor-losses]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
source: "GPS 7 & 8 data sheet (Fox, McDonald and Pritchard, 8th ed., Tables 8.1, 8.2, 8.4, A.8, Fig. 8.15)"
aliases: [Darcy-Weisbach, Moody chart, Colebrook equation, Haaland equation, minor losses, pipe friction]
---

# Pipe Flow and Losses – Formula Bank

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] · worked problems: [[Pipe Flow and Losses - Solved Problems]]

Numbers quoted in the solved problems are recomputed in `Tools/fm_pipe.py`.

## 1. Energy equation with losses

Bernoulli plus a loss term between sections 1 and 2 of a steady incompressible pipe flow:

$$\Big(\frac{p_1}{\rho}+\alpha_1\frac{V_1^2}{2}+gz_1\Big)-\Big(\frac{p_2}{\rho}+\alpha_2\frac{V_2^2}{2}+gz_2\Big)=h_{lT}=h_l+h_{lm}$$

$\alpha\approx1$ (turbulent), $\alpha=2$ (fully developed laminar). $V$ is the mean velocity, $Q=VA$, $Re=VD/\nu$. $h_{lT}$ is energy per unit mass (J/kg); divide by $g$ for head in metres.

If the section velocities are equal (constant-diameter pipe, or the meter and tap in a house) the kinetic terms cancel and the pressure and elevation difference all goes into friction.

## 2. Major loss (Darcy–Weisbach)

$$h_l=f\,\frac{L}{D}\,\frac{V^2}{2}\qquad\Longrightarrow\qquad\Delta p=\rho f\frac{L}{D}\frac{V^2}{2}=\frac{8\rho f L}{\pi^2}\,\frac{Q^2}{D^5}$$

The last form shows why diameter dominates: at fixed $Q$, $\Delta p\propto f\,L\,Q^2/D^5$. A 20 % bigger bore cuts $\Delta p$ to 40 %.

## 3. Friction factor

| Regime | $f$ |
|---|---|
| Laminar, $Re<2300$ | $64/Re$ (independent of roughness) |
| Turbulent, Colebrook (implicit) | $\dfrac1{\sqrt f}=-2.0\log_{10}\!\Big(\dfrac{e/D}{3.7}+\dfrac{2.51}{Re\sqrt f}\Big)$ |
| Turbulent, Haaland (explicit, within 2 %) | $\dfrac1{\sqrt f}=-1.8\log_{10}\!\Big[\Big(\dfrac{e/D}{3.7}\Big)^{1.11}+\dfrac{6.9}{Re}\Big]$ |
| Fully rough (Re large) | $f=\Big[-2.0\log_{10}\dfrac{e/D}{3.7}\Big]^{-2}$ |

The Moody chart is a plot of Colebrook with the laminar line added. On the chart:
- left of $Re=2300$ one line, slope $-1$ on the log–log axes;
- at high $Re$ each $e/D$ curve flattens to its fully rough value, so $f$ stops depending on speed and $\Delta p\propto V^2$ exactly;
- the smooth-pipe curve keeps falling with $Re$.

**Roughness $e$ (mm):** riveted steel 0.9–9, concrete 0.3–3, wood stave 0.2–0.9, cast iron 0.26, galvanized iron 0.15, asphalted cast iron 0.12, commercial steel 0.046, drawn tubing 0.0015, smooth plastic ≈ 0. **Water:** 15 °C: $\rho=999$, $\nu=1.14\times10^{-6}$; 20 °C: $\rho=998$, $\nu=1.01\times10^{-6}$ (SI).

## 4. Minor losses

$$h_{lm}=K\frac{V^2}{2}\qquad\text{or}\qquad h_{lm}=f\frac{L_e}{D}\frac{V^2}{2}$$

$V$ is the mean velocity in the pipe (for an area change, the larger of the two velocities). Add every minor loss to $f\,L/D$ in the same bracket.

| Fitting | $K$ |
|---|---|
| Entrance, re-entrant | 0.78 |
| Entrance, square-edged | 0.50 |
| Entrance, rounded $r/D=0.02$, $0.06$, $\ge0.15$ | 0.28, 0.15, 0.04 |
| Exit into a large reservoir | 1.0 |
| Sudden expansion (on $V_1$) | $(1-A_1/A_2)^2$ |
| Sudden contraction (on $V_2$), $A_2/A_1=0,\,0.2,\,0.4,\,0.6,\,0.8$ | 0.50, 0.42, 0.28, 0.15, 0.04 |

| Fitting (fully open) | $L_e/D$ |
|---|---|
| Gate valve, globe valve, angle valve, ball valve | 8, 340, 150, 3 |
| Standard elbow 90°, 45° | 30, 16 |
| Return bend (close) | 50 |
| Standard tee, through run, through branch | 20, 60 |

## 5. The three pipe problems

| Unknown | Known | Method |
|---|---|---|
| $\Delta p$ (or $h_l$) | $Q$ (or $V$), $D$, $L$, $e$ | $Re\to f\to h_l$. Direct. |
| $Q$ | $\Delta p$, $D$, $L$, $e$ | Guess $f$ (fully rough value), get $V$, then $Re$, then new $f$. Converges in 2–3 passes. |
| $D$ | $\Delta p$, $Q$, $L$, $e$ | Guess $D$, compute $\Delta p$, adjust (or solve with Haaland); then round **up** to a standard size. |

## 6. Laminar tube flow

Fully developed laminar flow in a round tube ($Re<2300$): $f=64/Re$, kinetic-energy coefficient $\alpha=2$, $Q=\dfrac{\pi D^4\Delta p}{128\mu L}$. The largest laminar flow has $V_{max}=2300\,\nu/D$.

## Cross-domain links
- [[Conservation Laws and Flow Networks]] — a pipe is a resistor: $\Delta p$ plays the voltage and $Q$ the current. Laminar flow ($\Delta p\propto Q$, Ohm's law) is a linear resistor; rough turbulent flow ($\Delta p\propto Q^2$) is a nonlinear one, and two pipes in series add their $\Delta p$ at the same $Q$, just as resistors do in [[01 Basic Concepts and Basic Laws|Ohm's and Kirchhoff's laws]].
- [[Dimensional Analysis and Similitude - Formula Bank]] — $f$ is a function of $Re$ and $e/D$ because the pipe-flow problem has exactly those two Π groups besides $\Delta p/\rho V^2$.
