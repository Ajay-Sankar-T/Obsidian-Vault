---
tags: [EE1100, tutorial-solution, machines, induction-machine, equivalent-circuit, torque-slip, starting]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q11: Running, Maximum and Starting Performance of a 400 V Motor

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q10 - Induction Motor with the Approximate Equivalent Circuit]] · Back to [[Tutorial 8 - Induction Machines]] · [[Problems - MOC]]

> [!question] A three-phase, star-connected, 400 V, 50 Hz, 4-pole induction motor has per-phase constants referred to the stator $r_1=0.15$, $x_1=0.45$, $r_2'=0.12$, $x_2'=0.45$, $x_\varphi=28.5\ \Omega$; fixed losses (core, friction and windage) $400$ W; stator-to-rotor effective turns ratio $1.2$. Compute (a) the stator current, output torque and efficiency at slip $0.04$; (b) the slip at maximum torque, the maximum torque and the corresponding power output; (c) the rotor current and torque at starting; (d) the external rotor resistance for maximum torque at starting. *[Sheet: (a) $71.06$ A, $274.12$ N·m, $90.36\ \%$; (b) $0.1326$, $469.1$ N·m, $63\,515$ W; (c) $243.94$ A, $136.4$ N·m; (d) $0.5452\ \Omega$]*

**Tests:** the **exact** equivalent circuit, the Thevenin form for torque, $s_m$ and $T_{max}$, rotor resistance referred through the turns ratio.

## Given
$V_1=400/\sqrt3=230.9$ V per phase; $n_s=1500$ rpm, $\omega_s=157.08$ rad/s; $a=N_1/N_2=1.2$ (so a rotor-side resistance $R$ appears as $a^2R=1.44R$ at the stator); only the magnetising reactance $x_\varphi$ is given (no core-loss resistance), so the fixed losses are subtracted from the mechanical power.

## Principle and why it applies
With $x_\varphi$ given and $x_\varphi\gg$ the series impedance, but with accuracy expected to a few digits, use the **exact circuit** ($r_1+jx_1$, then $jx_\varphi$ in parallel with the rotor branch $r_2'/s+jx_2'$). For torque as a function of slip use the **Thevenin equivalent** of the stator side (theory §5), which gives $s_m$ and $T_{max}$ in closed form.

## Diagram
![[T8-Q10-Q11-equivalent-circuit.png]]

![[T8-Q5-torque-slip.png]]

## Solution
**Thevenin equivalent** (per phase, seen from the rotor branch):
$$Z_{th}=\frac{jx_\varphi(r_1+jx_1)}{r_1+j(x_1+x_\varphi)}=0.1454+j0.4438\ \Omega,\qquad V_{th}=V_1\frac{jx_\varphi}{r_1+j(x_1+x_\varphi)}=227.3\ \text{V}.$$

**(a) $s=0.04$.** Rotor branch $r_2'/s+jx_2'=3+j0.45\ \Omega$; in parallel with $jx_\varphi$ then in series with $r_1+jx_1$:
$$\bar I_1=71.0\angle-21.5^\circ\ \text{A},\qquad \bar I_2'=69.5\ \text{A}.$$
$$P_g=3I_2'^2\frac{r_2'}{s}=3\times69.5^2\times3=43.5\ \text{kW},\quad T_{dev}=\frac{P_g}{\omega_s}=277.0\ \text{N·m},\quad P_{mech}=0.96P_g=41.77\ \text{kW}.$$
$$P_{out}=P_{mech}-400=41.37\ \text{kW},\quad T_{out}=\frac{P_{out}}{\omega_r}=\frac{41\,367}{150.8}=\mathbf{274.3\ N\cdot m},\quad\eta=\frac{P_{out}}{3V_1I_1\cos\phi}=\frac{41.37}{45.78}=\mathbf{90.4\ \%}.$$

**(b) Maximum torque.** $Z_k=\sqrt{R_{th}^2+(X_{th}+x_2')^2}=\sqrt{0.1454^2+0.8938^2}=0.9055\ \Omega$:
$$s_m=\frac{r_2'}{Z_k}=\frac{0.12}{0.9055}=\mathbf{0.1325},\qquad T_{max}=\frac{3V_{th}^2}{2\omega_s(R_{th}+Z_k)}=\frac{3\times227.3^2}{2\times157.08\times1.0509}=\mathbf{469.7\ N\cdot m}.$$
Power at that point: $P_{mech}=T_{max}\,\omega_s(1-s_m)=469.7\times157.08\times0.8675=64.0$ kW, so the output is $64.0-0.4=\mathbf{63.6\ kW}$.

**(c) Starting ($s=1$).** Rotor branch $0.12+j0.45$; the exact circuit gives
$$I_2'=\mathbf{243.9\ A},\quad I_1=247.7\ \text{A},\quad T_{st}=\frac{3I_2'^2r_2'}{\omega_s}=\mathbf{136.3\ N\cdot m}.$$

**(d) External resistance for maximum starting torque.** At $s=1$ we need $r_2'+R_{ext}'=Z_k$ (so that the peak sits at $s=1$):
$$R_{ext}'=0.9055-0.12=0.7855\ \Omega\ \ (\text{referred to the stator});\qquad R_{ext}=\frac{R_{ext}'}{a^2}=\frac{0.7855}{1.44}=\mathbf{0.5455\ \Omega}\ \ (\text{actual, in the rotor}).$$
The starting torque then equals $T_{max}=469.7$ N·m.

## Result
$$\boxed{\begin{array}{l}\text{(a) }I_1=71.0\ \text{A},\ T_{out}=274.3\ \text{N·m},\ \eta=90.4\ \%\\ \text{(b) }s_m=0.1325,\ T_{max}=469.7\ \text{N·m},\ P_{out}=63.6\ \text{kW}\\ \text{(c) }I_2'=243.9\ \text{A},\ T_{st}=136.3\ \text{N·m}\\ \text{(d) }R_{ext}=0.5455\ \Omega\end{array}}$$
(The printed answers agree to better than $0.3\ \%$ except the output power at $T_{max}$, $63\,515$ W against $63\,600$ W, $0.13\ \%$; the differences come from rounding the Thevenin constants.)

## Check
Starting torque with $R_{ext}$: $\dfrac{3V_{th}^2\,(r_2'+R_{ext}')}{\omega_s[(R_{th}+0.9055)^2+(X_{th}+0.45)^2]}=\dfrac{3\times227.3^2\times0.9055}{157.08\times(1.0509^2+0.8938^2)}=469.7$ N·m $=T_{max}$ ✓. Slip at maximum torque is much higher than the running slip (0.04), as expected: the motor has about $1.7\times$ its full-load torque in reserve. The starting current ($248$ A in the stator) is about $3.5\times$ the full-load current.

## Trap / alternative
- **Referring $R_{ext}$:** $R_{ext}'=a^2R_{ext}$ (impedances scale with the **square** of the turns ratio): using $R_{ext}'=0.7855$ directly as the rotor resistance gives $0.7855\ \Omega$, wrong; dividing by $a=1.2$ instead of $a^2=1.44$ gives $0.65\ \Omega$, also wrong.
- Using the *approximate* circuit changes the numbers slightly ($s_m=0.1315$, $R_{ext}=0.550\ \Omega$, $I_1=73.1$ A at $s=0.04$) because $x_\varphi$ is not infinite; the printed answers need the exact (Thevenin) treatment.
- $P_{out}=P_{mech}-$ fixed losses, and $T_{out}=P_{out}/\omega_r$ differs from $T_{dev}=P_g/\omega_s$ ($274.3$ against $277.0$ N·m).

## Concepts used
- Exact equivalent circuit, Thevenin equivalent, pull-out torque, starting with rotor resistance ([[Theory - Three-Phase Induction Machines]], [[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Thevenin, Norton and Maximum Power Transfer (AC)]])
