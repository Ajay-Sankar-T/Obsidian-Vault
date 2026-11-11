---
tags: [concept, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
aliases: [Flywheel, Fluctuation of energy, Coefficient of fluctuation of speed]
---

# Flywheel Sizing from the Turning-Moment Diagram

> [!abstract] In one breath
> An engine's torque swings above and below the load torque. The flywheel is an energy tank: it takes the surplus and gives it back, so the speed ripples by only a few per cent. **Find the largest energy swing $\Delta E$ on the torque diagram, then pick the inertia that holds the speed ripple to the allowed $C_s$.**

Part of [[KDoMs - MOC]]. Solved in [[Tutorial-10-solution]].

## 1. The three equations

$$
T_{\text{mean}}=\frac{W_{\text{cycle}}}{\text{angle of one cycle}},\qquad
C_s=\frac{\omega_{\max}-\omega_{\min}}{\omega_{\text{mean}}},\qquad
\Delta E=I\,\omega_{\text{mean}}^{2}\,C_s
$$

- One cycle is $2\pi$ for a two-stroke engine and **$4\pi$ for a four-stroke**.
- With $\omega_{\text{mean}}=\tfrac12(\omega_{\max}+\omega_{\min})$ the last equation is exact: $\tfrac12 I(\omega_{\max}^2-\omega_{\min}^2)=I\omega_{\text{mean}}(\omega_{\max}-\omega_{\min})=I\omega_{\text{mean}}^2C_s$.
- Mass at radius of gyration $k$: $m=I/k^2$.

## 2. Reading the diagram

1. Convert each area to energy with the diagram's scale. Strokes below the zero line are negative work.
2. $W_{\text{cycle}}$ is the algebraic sum. $T_{\text{mean}}$ is its average over the cycle. With a uniform load, the resisting torque is this line.
3. Where engine torque exceeds $T_{\text{mean}}$ the flywheel **gains** energy; below it, it **loses**. The cumulative sum $E(\theta)=\int(T-T_{\text{mean}})\,d\theta$ is the flywheel's energy curve.
4. $\Delta E=E_{\max}-E_{\min}$. It is the area between **consecutive crossings** of the mean line that gives the biggest swing. On a one-peak diagram that is the area *above* the mean line on the power stroke.

For a triangular power stroke of base $\pi$ and peak $T_{\max}=2a/\pi$ (area $a$), the part above $T_{\text{mean}}$ is a similar triangle:

$$
\Delta E=\tfrac12\,\pi\,\frac{T_{\max}-T_{\text{mean}}}{T_{\max}}\,(T_{\max}-T_{\text{mean}})=\frac{\pi\,(T_{\max}-T_{\text{mean}})^{2}}{2\,T_{\max}}
$$

## 3. What the numbers say

- $m\propto 1/C_s$: halve the allowed ripple and you double the flywheel.
- $m\propto1/k^2$: the required $I$ is fixed, so put the mass at the rim. That is why flywheels are rims, not discs.
- More cylinders smooth the torque and shrink $\Delta E$, which is why a single-cylinder engine needs the heaviest flywheel.

> [!warning] Traps
> - Dividing the cycle work by $2\pi$ for a four-stroke engine. It is $4\pi$.
> - Taking the whole power-stroke area as $\Delta E$. Only the part above the mean line counts.
> - Entering rpm in the energy formula. Convert to rad/s.
> - Using $\omega_{\max}/\omega_{\min}$ in the wrong place in $C_s$: it is the *difference* divided by the *mean*.

> [!question]- Predict first: the flywheel mass for a ±1 % speed band against the ±0.5 % band at the same $\Delta E$?
> The band is the total spread: ±1 % gives $C_s=2\%$, ±0.5 % gives $C_s=1\%$. Mass doubles for the narrower band.

> [!question]- Why does the energy curve close after one cycle?
> In steady running the average engine torque equals the load torque, so $\int_0^{4\pi}(T-T_{\text{mean}})\,d\theta=0$. If it did not, the engine would be accelerating or stalling.

## 4. Connections

- [[Mass Moments of Inertia]] — $I=mk^2$ and why the rim carries the mass.
- [[Kinetics of Particles - Work-Energy and Impulse-Momentum]] — $\Delta E$ is just the work-energy theorem for a rotating body.
- [[The Mechanical-Electrical Analogy (Impedance Analogy)]] — with torque ↔ current and speed ↔ voltage, inertia is a capacitor. $\Delta E=\tfrac12C(V_{\max}^2-V_{\min}^2)$ is exactly how the smoothing capacitor of a rectifier is sized for its ripple.
- [[Energy Methods - A Unified View]] — energy bookkeeping again.
