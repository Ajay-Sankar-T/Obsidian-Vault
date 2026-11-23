---
tags: [EE1100, tutorial-theory, machines, induction-machine]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# Theory: The Three-Phase Induction Machine

← up: [[Tutorial 8 - Induction Machines|Tutorial 8]] · lectures: [[Lecture 40 Electric Machines.pdf]], [[Lecture 41 Induction Machine-Circuit Representation.pdf]] · week: [[11 Three Phase Induction Machines]] · focused notes: [[Revolving Magnetic Field and Synchronous Speed]] (full derivation), [[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Induction Machines - Types, Construction and Applications]] · transformer analogue: [[10 Single Phase Transformers]], [[Transformer Voltage Regulation and Efficiency]]

> [!abstract] The idea in one paragraph
> A three-phase stator winding produces a magnetic field of constant strength that **rotates** at the synchronous speed $n_s=120f/P$. The field sweeps across the rotor conductors, **inducing** currents in the short-circuited rotor (transformer action); those currents, in the same field, feel a force (the Lorentz force) that drags the rotor in the direction of the field (Lenz's law: the rotor chases the change that induces its current). The rotor can never quite catch the field, because at synchronous speed there would be no relative motion, no induced emf, no current and no torque. The difference is the **slip**.

## 1. The rotating field

Three coils $120^\circ$ apart in space carrying currents $120^\circ$ apart in time produce the resultant MMF
$$F_R(\alpha,t)=\tfrac32F_m\sin(\omega t-\alpha),$$
a wave of **constant amplitude** that travels round the air gap. The proof (Q2) adds the three space-distributed pulsating MMFs; the "backward" terms cancel because they are three phasors $120^\circ$ apart.

For a machine with $P$ poles supplied at $f$ Hz,
$$n_s=\frac{120f}{P}\ \text{rpm},\qquad\omega_s=\frac{4\pi f}{P}\ \text{rad/s}.$$
Swapping any two supply leads reverses the sequence and the direction of rotation.

## 2. Slip and rotor quantities

$$s=\frac{n_s-n_r}{n_s},\qquad n_r=(1-s)n_s,\qquad f_2=sf_1\ \text{(rotor frequency)},\qquad E_{2s}=sE_{20},\qquad X_{2s}=sX_{20}.$$

| Operating condition | slip | note |
|---|---|---|
| standstill (starting) | $s=1$ | rotor frequency $=f_1$, rotor emf largest |
| full-load motoring | $s\approx0.02$–$0.06$ | rotor frequency $1$–$3$ Hz at 50 Hz |
| synchronous speed | $s=0$ | no emf, no torque |
| above synchronous (generator) | $s<0$ | driven by a prime mover, supplies power |
| reverse rotation (plugging, braking) | $s>1$ | the rotor is driven against the field |

The **rotor current** for a rotor with resistance $R_2$ and standstill reactance $X_{20}$ is
$$I_2=\frac{sE_{20}}{\sqrt{R_2^2+(sX_{20})^2}},\qquad\cos\phi_2=\frac{R_2}{\sqrt{R_2^2+(sX_{20})^2}},$$
so the rotor is strongly inductive at standstill (low pf, large current) and nearly resistive at small slip (pf $\approx1$).

## 3. Equivalent circuit (per phase)

The machine is a transformer with a rotating secondary. Refer the rotor to the stator side with the effective turns ratio $a=N_1/N_2$: $E_2'=aE_{2}$, $r_2'=a^2r_2$, $x_2'=a^2x_2$, $I_2'=I_2/a$. At slip $s$ the rotor branch is the standstill reactance $x_2'$ in series with the **resistance $r_2'/s$**:
$$\frac{r_2'}{s}=r_2'+\underbrace{r_2'\frac{1-s}{s}}_{\text{represents the shaft power}}.$$

![[T8-Q10-Q11-equivalent-circuit.png]]

The **exact circuit** has $r_1+jx_1$, the shunt magnetising branch $jx_\varphi$ (in parallel with a core-loss resistance $R_c$ when specified), then $x_2'$ and $r_2'/s$. The **approximate circuit** moves the shunt branch to the input terminals (valid because $x_\varphi\gg r_1+jx_1$), so $I_1=I_2'+I_0$ with $I_0=V_1/(R_c\parallel jx_\varphi)$. The parameters come from a **no-load test** ($I_0$, core loss; slip $\approx0$) and a **blocked-rotor test** ($s=1$, series $r_1+r_2'$, $x_1+x_2'$), exactly as for the transformer OC/SC tests.

## 4. Power flow and efficiency

$$P_{in}=\sqrt3V_LI_L\cos\phi,\qquad P_g=P_{in}-P_{cu1}-P_{core},\qquad P_{cu2}=sP_g,\qquad P_{mech}=(1-s)P_g,\qquad P_{out}=P_{mech}-P_{F\&W}.$$
$$P_g:P_{cu2}:P_{mech}=1:s:(1-s).$$
Torque: $\;T_{dev}=\dfrac{P_g}{\omega_s}=\dfrac{P_{mech}}{\omega_r}$ (the same number, since $\omega_r=(1-s)\omega_s$); shaft torque $T_{sh}=P_{out}/\omega_r$; $\ \eta=P_{out}/P_{in}$. Because $P_{cu2}=sP_g$, a motor at slip $s$ can never be more than $(1-s)$ efficient *in the rotor stage*: speed regulation and efficiency trade off.

## 5. The torque–slip characteristic

Replace the stator side by its **Thevenin equivalent** seen from the rotor branch:
$$V_{th}=V_1\frac{jx_\varphi}{r_1+j(x_1+x_\varphi)},\qquad Z_{th}=\frac{jx_\varphi(r_1+jx_1)}{r_1+j(x_1+x_\varphi)}=R_{th}+jX_{th}.$$
Then $I_2'=V_{th}\big/\big[(R_{th}+r_2'/s)+j(X_{th}+x_2')\big]$ and
$$\boxed{T(s)=\frac{3}{\omega_s}\,\frac{V_{th}^2\,r_2'/s}{\big(R_{th}+r_2'/s\big)^2+\big(X_{th}+x_2'\big)^2}}$$
(approximately, with $r_1+jx_1$ in series and $x_\varphi$ at the input: $Z_{th}\to r_1+jx_1$, $V_{th}\to V_1$). Maximising $T$ over $r_2'/s$ is the maximum-power-transfer condition of [[Theory - Circuit Laws and Network Theorems]] §9:
$$\frac{r_2'}{s_m}=Z_k\equiv\sqrt{R_{th}^2+(X_{th}+x_2')^2},\qquad s_m=\frac{r_2'}{Z_k},\qquad T_{max}=\frac{3}{2\omega_s}\frac{V_{th}^2}{R_{th}+Z_k}.$$

Consequences:
- $T_{max}$ does **not depend on the rotor resistance**; $s_m\propto r_2'$. Adding external rotor resistance (wound rotor) slides the peak towards low speed and raises the starting torque, up to $T_{start}=T_{max}$ when $r_2'+R_{ext}'=Z_k$.
- $T\propto V^2$: a 10 % voltage drop costs 19 % of the torque.
- **Stable region:** for $0<s<s_m$ torque rises with slip, so a load increase slows the rotor and the motor produces more torque. Beyond $s_m$ torque falls with slip, so a load above $T_{max}$ stalls the motor.
- At small slip $r_2'/s\gg$ everything else, so $T\approx\dfrac{3V^2}{\omega_sr_2'}\,s$: a straight line, the "constant speed" region.

![[T8-Q5-torque-slip.png]]

## 6. Starting
At standstill $s=1$, the rotor looks like a short circuit: the starting current is $5$–$7$ times the rated current with a poor power factor, and the starting torque is moderate. Remedies: reduced-voltage or star-delta starters for cage motors, external rotor resistance for wound-rotor motors ([[Induction Machines - Types, Construction and Applications]]).

## 7. Common traps
- $n_s=120f/P$ uses **poles**, not pole pairs.
- Slip is relative to the **synchronous** speed; $f_2=sf_1$.
- Torque is $P_g/\omega_s$ (or $P_{mech}/\omega_r$), never $P_g/\omega_r$.
- $r_2'/s$ is not $r_2'$: the extra $r_2'(1-s)/s$ is the mechanical load.
- **Referred** quantities carry $a^2$ for impedances but $a$ for voltages and $1/a$ for currents.
- Output torque (shaft) differs from developed torque by the friction and windage loss.

## 8. Cross-domain links
- [[Gears, Transformers and Reflected Impedance]]: the equivalent circuit is a transformer plus a gear: $r_2'(1-s)/s$ is the reflected mechanical load; a high-slip (low-speed) load looks like a smaller resistance.
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] and [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]: the rotating field is three phasors $120^\circ$ apart made physical.
- [[Thevenin, Norton and Maximum Power Transfer (AC)]]: pull-out torque is the maximum-power-transfer point of the rotor resistance.
