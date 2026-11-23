---
tags: [EE1100, tutorial-solution, machines, induction-machine, torque-slip]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q5: The Speed–Torque (Torque–Slip) Characteristic

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q4 - Slip]] · Next: [[T8-Q6 - Speeds and Rotor Frequency]]

> [!question] Draw and explain the speed–torque characteristic of an induction machine as a function of slip.

**Tests:** the shape and regions of the torque–slip curve, $T_{max}$, $s_m$, starting torque, stability, effect of rotor resistance and voltage.

## Principle and why it applies
The developed torque is $T=P_g/\omega_s=\dfrac{3I_2'^2\,(r_2'/s)}{\omega_s}$, and $I_2'$ depends on slip through the rotor impedance $(r_2'/s)+jx_2'$. Using the Thevenin equivalent of the stator side (theory §5):
$$T(s)=\frac{3}{\omega_s}\frac{V_{th}^2\,r_2'/s}{(R_{th}+r_2'/s)^2+(X_{th}+x_2')^2}.$$
Two competing effects shape the curve: as $s$ **rises** the rotor current rises (more induced emf) but the rotor power factor $\cos\phi_2=\dfrac{r_2'/s}{\sqrt{\cdots}}$ **falls** (rotor frequency, hence reactance, rises). Torque is the product of flux, rotor current and $\cos\phi_2$: it peaks where the two balance.

## Diagram
![[T8-Q5-torque-slip.png]]

**Figure** (a 4-pole, 400 V, 50 Hz motor, the machine of [[T8-Q11 - Equivalent Circuit and Starting of an Induction Motor]]): left, torque against slip for motoring, generating and braking; right, the effect of adding rotor resistance, plotted against speed.

## Solution (the explanation)
**Regions, from the figure:**
1. **$s\to0$ (near synchronous speed):** $r_2'/s$ is large and dominates, so $T\approx\dfrac{3V_{th}^2}{\omega_sr_2'}\,s$: a **straight line through the origin**. The steep slope means the speed barely changes between no load and full load: constant-speed behaviour. **Normal running** is on this part, at $s\approx0.02$–$0.06$.
2. **Pull-out (breakdown) torque** at $s_m=\dfrac{r_2'}{Z_k}$ with $Z_k=\sqrt{R_{th}^2+(X_{th}+x_2')^2}$:
$$T_{max}=\frac{3}{2\omega_s}\frac{V_{th}^2}{R_{th}+Z_k}\quad(\text{typically }2\text{–}3\times\text{rated torque}).$$
It occurs at $s_m\approx0.1$–$0.3$ for cage motors. For the Q11 motor $s_m=0.1325$, $T_{max}=469.7$ N·m.
3. **$s_m<s<1$ (unstable side):** torque falls as slip rises (large $x_2'$, poor power factor); the starting torque at $s=1$ is $T_{st}=\dfrac{3}{\omega_s}\dfrac{V_{th}^2r_2'}{(R_{th}+r_2')^2+(X_{th}+x_2')^2}$ (136 N·m for the Q11 motor), typically $1.5$–$2\times$ rated for a normal cage motor.
4. **$s<0$ (rotor driven above $n_s$):** torque reverses: **generator** operation, returning power to the supply.
5. **$s>1$ (rotor driven backwards, or two supply leads swapped on a running motor):** **braking** (plugging); the torque opposes the rotation and the machine absorbs both electrical and mechanical power.

**Stability:** on the low-slip side ($0<s<s_m$) a load increase slows the rotor, $s$ rises, torque rises: a stable operating point. On the other side a load increase *reduces* torque and the motor stalls: the load torque must stay below $T_{max}$.

**Effect of changing the parameters:**
- **Rotor resistance** (wound-rotor motors, or a high-resistance cage): $s_m\propto r_2'$, so the peak moves to lower speed while $T_{max}$ is **unchanged**; the starting torque rises, reaching $T_{max}$ when $r_2'+R_{ext}'=Z_k$ (Q11(d)); at normal running speed, however, the extra resistance costs efficiency ($P_{cu2}=sP_g$).
- **Supply voltage:** $T\propto V^2$ at every slip (a 10 % sag costs 19 %).
- **Frequency:** lower $f$ at constant $V$ over-fluxes; inverter drives scale $V/f$.

## Result
$$T(s)=\frac{3V_{th}^2\,(r_2'/s)}{\omega_s\big[(R_{th}+r_2'/s)^2+(X_{th}+x_2')^2\big]},\quad s_m=\frac{r_2'}{Z_k},\quad T_{max}=\frac{3V_{th}^2}{2\omega_s(R_{th}+Z_k)}:\ \text{linear near }s=0,\ \text{peak at }s_m,\ \text{falling to }T_{st}\text{ at }s=1.$$

## Check
Limits: $s\to0$: $T\to0$; $s\to\infty$: $T\to0$ (so there must be a maximum between); at $s_m$ the power transfer to $r_2'/s$ is maximal, the same maximum-power condition as [[T1-Q10 - Maximum Power Transfer and Half Power]]. For the figure's motor the computed values are $s_m=0.1325$, $T_{max}=469.7$ N·m, $T_{st}=136.3$ N·m.

## Trap / alternative
- **Torque against *slip* vs against *speed*:** the same curve mirrored ($n_r=(1-s)n_s$): at speed $0$ the slip is $1$.
- Pull-out torque is **independent of the rotor resistance** (only its location moves).
- Starting torque is high with a high-resistance rotor but running efficiency is low; a deep-bar or double-cage rotor gets both.

## Concepts used
- Torque–slip curve, maximum-power-transfer analogy, rotor-resistance control ([[Theory - Three-Phase Induction Machines]], [[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Induction Machines - Types, Construction and Applications]])
