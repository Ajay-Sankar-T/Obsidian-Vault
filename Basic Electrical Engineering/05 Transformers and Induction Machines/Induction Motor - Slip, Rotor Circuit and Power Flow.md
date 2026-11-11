---
title: Induction Motor – Slip, Rotor Circuit and Power Flow
tags: [EE1100, concept, induction-machine, slip, power-flow, equivalent-circuit]
source: "[[Lecture 41 Induction Machine-Circuit Representation.pdf]]"
---

Related: [[11 Three Phase Induction Machines]] · [[Revolving Magnetic Field and Synchronous Speed]] · [[Induction Machines - Types, Construction and Applications]] · [[10 Single Phase Transformers]] · [[Transformer Voltage Regulation and Efficiency]]

## What it is
An induction motor is a **transformer with a rotating secondary**. The stator is the primary; the rotor windings (or bars) are a short-circuited secondary. With the same flux linking both,
$$E_1=4.44f_1N_1'\Phi_m,\quad E_2=4.44f_2N_2'\Phi_m\ \Rightarrow\ \frac{E_1}{E_2}=\frac{N_1'}{N_2'}\quad(N'=k_wN),$$
but the air gap between rotor and stator adds reluctance and leakage, so the no-load (magnetising) current is **30–50 %** of rated current, against 2–6 % for a transformer.

## Slip
The rotor cannot reach synchronous speed: at $n_r=n_s$ there would be no relative motion, no induced rotor emf and no torque.
$$\boxed{s=\frac{n_s-n_r}{n_s}},\qquad n_r=(1-s)n_s,\qquad\omega_r=(1-s)\omega_s,\qquad s\approx2\text{–}6\%\ \text{at full load}.$$
$s=1$ at standstill, $s\to0$ near synchronous speed.

**Rotor frequency.** The field moves at $s\,n_s$ relative to the rotor, so
$$f_2=s\,f_1.$$
The rotor current sets up its own rotating field, which turns at $f_2/(P/2)=sn_s$ relative to the rotor; add the rotor's own speed $n_r=(1-s)n_s$ and the rotor field turns at $n_s$ relative to the **stator**. Stator and rotor fields are therefore stationary with respect to each other at every slip, which is the condition for steady torque.

## Rotor circuit at slip $s$
At standstill the rotor emf is $E_2$ and reactance $x_2$. At slip $s$: $E_{2s}=sE_2$, $x_{2s}=2\pi f_2L_2=sx_2$. The rotor current
$$I_2=\frac{sE_2}{r_2+jsx_2}=\frac{E_2}{\dfrac{r_2}s+jx_2},\qquad\cos\phi_2=\frac{r_2/s}{\sqrt{(r_2/s)^2+x_2^2}}.$$
So the rotor looks like a **standstill** rotor of reactance $x_2$ in series with the resistance $r_2/s$, and the power factor is poor at standstill (small $r_2/s$) and improves as the rotor speeds up.

## Power flow
Power crossing the air gap into the rotor, $P_g=I_2^2\,\dfrac{r_2}{s}$. Split the resistance:
$$\frac{r_2}s=r_2+\frac{r_2(1-s)}s\quad\Longrightarrow\quad P_g=\underbrace{I_2^2r_2}_{sP_g\ (\text{rotor copper loss})}+\underbrace{I_2^2\frac{r_2(1-s)}s}_{(1-s)P_g=P_{em}}$$
$$P_g:\ P_{cu2}:\ P_{em}=1:s:(1-s).$$
- **Developed (electromechanical) power** $P_{em}=P_g-P_{cu2}=(1-s)P_g$.
- **Shaft power** $P_{sh}=P_{em}-(\text{core loss}+\text{friction and windage})$.
- **Torque:** $T_{em}=\dfrac{P_{em}}{\omega_r}=\dfrac{(1-s)P_g}{(1-s)\omega_s}=\boxed{\dfrac{P_g}{\omega_s}=\dfrac{I_2^2r_2/s}{\omega_s}}$, and $T_{sh}=\dfrac{P_{sh}}{\omega_r}=\dfrac{P_{sh}}{\omega_s(1-s)}$.
- **Efficiency** is at best $\approx(1-s)$ of the rotor stage: a motor running at 5 % slip loses at least 5 % of the air-gap power as rotor copper, so speed regulation and efficiency are the same trade-off.

**Worked illustration** (4-pole, 50 Hz, $s=4\%$, $P_g=10$ kW): $n_s=1500$ rpm, $n_r=1440$ rpm, $f_2=2$ Hz, $\omega_s=157.1$ rad/s. Rotor copper loss $sP_g=400$ W, $P_{em}=9.6$ kW, $T=P_g/\omega_s=63.7$ N·m (and $P_{em}/\omega_r=9600/150.8=63.7$ N·m ✓).

> [!warning] Traps
> - Slip is relative to the **synchronous** speed ($n_s$), not to the rotor speed.
> - $r_2/s$ is *not* the same as $r_2$: the extra $r_2(1-s)/s$ is the **load**, representing mechanical output.
> - Torque is $P_g/\omega_s$ (synchronous angular speed), not $P_g/\omega_r$.
> - A rotor at slip $s$ sees frequency $sf_1$, so its iron loss is negligible at normal slip (the core loss is mostly in the stator).

## Cross-domain links
- [[Gears, Transformers and Reflected Impedance]] — the resistance $r_2/s$ is a **reflected impedance**: the mechanical load seen from the electrical side. It is the transformer picture with the load resistor $r_2(1-s)/s$ standing for shaft power.
- [[Thevenin, Norton and Maximum Power Transfer (AC)]] — torque is proportional to the power delivered to $r_2/s$, so the **maximum (pull-out) torque** occurs where $r_2/s$ equals the magnitude of the source-side impedance, $r_2/s=\sqrt{r_{th}^2+(x_{th}+x_2)^2}$, with $Z_{th}=r_{th}+jx_{th}$ the Thevenin impedance of the stator side. Beyond that slip the motor stalls.
