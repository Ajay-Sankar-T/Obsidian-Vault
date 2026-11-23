---
tags: [EE1100, tutorial-solution, machines, induction-machine, power-flow, efficiency, no-load-test]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q9: Losses, Speed, Torque and Efficiency of a 10 kW Delta-Connected Motor

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q8 - Rotor Current, Power Factor and Torque]] · Next: [[T8-Q10 - Induction Motor with the Approximate Equivalent Circuit]]

> [!question] A 10 kW, 400 V, 3-phase, 4-pole, 50 Hz, delta-connected induction motor runs at no load with a line current of 8 A and an input power of 660 W. At full load the line current is 18 A and the input is 11.2 kW. The stator resistance is $1.2\ \Omega$ per phase; friction and windage loss is 420 W. Assuming negligible rotor ohmic loss at no load, calculate (a) the stator core loss, (b) the total rotor losses at full load, (c) the total rotor ohmic losses at full load, (d) the full-load speed, (e) the internal torque, shaft torque and efficiency. *[Sheet: 163.3 W; 648 W; 228 W; 1468.2 rpm; 67.8 N·m, 65 N·m, 89.2 %]*

**Tests:** [[Theory - Three-Phase Induction Machines#4. Power flow and efficiency|power flow]], using the no-load test to split the losses, delta phase currents.

## Given
Delta connection: $I_{ph}=I_L/\sqrt3$. No load: $I_L=8$ A, $P_0=660$ W. Full load: $I_L=18$ A, $P_{in}=11\,200$ W, $P_{out}=10\,000$ W (the rating), $r_1=1.2\ \Omega$/phase, $P_{F\&W}=420$ W, $n_s=1500$ rpm.

## Principle and why it applies
**No-load input** is spent as stator copper loss, core loss and friction/windage; the rotor ohmic loss is negligible ($s\approx0$), so the core loss is what is left. At **full load** the input power flows $P_{in}\to P_g\to P_{mech}\to P_{out}$, losing the stator copper and core loss before the air gap, then the rotor copper ($sP_g$) and friction/windage. Knowing $P_{in}$ and the rated output, the rotor losses follow, and the slip is $s=P_{cu2}/P_g$.

## Diagram
![[T8-Q9-power-flow.png]]

## Solution
**(a) Core loss.** No-load stator copper loss: phase current $8/\sqrt3=4.619$ A, so $P_{cu0}=3\times4.619^2\times1.2=76.8$ W. 
$$P_{core}=660-76.8-420=\mathbf{163.2\ W}\quad(\text{sheet }163.3).$$

**Full-load stator copper loss:** $I_{ph}=18/\sqrt3=10.39$ A, $P_{cu1}=3\times10.39^2\times1.2=388.8$ W. Air-gap power:
$$P_g=P_{in}-P_{cu1}-P_{core}=11\,200-388.8-163.2=10\,648\ \text{W}.$$

**(b) Total rotor losses** (rotor copper plus friction and windage) $=P_g-P_{out}=10\,648-10\,000=\mathbf{648\ W}$.

**(c) Rotor ohmic loss:** $P_{cu2}=648-420=\mathbf{228\ W}$.

**(d) Speed.** $s=\dfrac{P_{cu2}}{P_g}=\dfrac{228}{10\,648}=0.02141$, $\ n_r=(1-s)\,1500=\mathbf{1467.9\ rpm}$ (the sheet's $1468.2$ differs by $0.02\ \%$).

**(e) Torques and efficiency.** $\omega_s=157.08$ rad/s, $\omega_r=2\pi\times1467.9/60=153.7$ rad/s:
$$T_{int}=\frac{P_g}{\omega_s}=\frac{10\,648}{157.08}=\mathbf{67.8\ N\cdot m},\qquad T_{sh}=\frac{P_{out}}{\omega_r}=\frac{10\,000}{153.7}=\mathbf{65.1\ N\cdot m},$$
$$\eta=\frac{P_{out}}{P_{in}}=\frac{10\,000}{11\,200}=\mathbf{89.3\ \%}.$$

## Result
$$\boxed{P_{core}=163.2\ \text{W};\ \ P_{rotor}=648\ \text{W};\ \ P_{cu2}=228\ \text{W};\ \ n_r=1468\ \text{rpm};\ \ T_{int}=67.8,\ T_{sh}=65.1\ \text{N·m};\ \ \eta=89.3\ \%}$$

## Check
Power-flow bookkeeping: $11\,200-388.8-163.2-228-420=10\,000$ W ✓. Internal torque $=P_{mech}/\omega_r$ where $P_{mech}=(1-s)P_g=10\,420$ W: $10\,420/153.7=67.8$ N·m ✓. The difference between internal and shaft torque is the friction/windage torque, $420/153.7=2.7$ N·m ✓.

## Trap / alternative
- **Delta:** the stator phase current is $I_L/\sqrt3$, so stator copper loss is $3I_{ph}^2r_1$, not $3I_L^2r_1$.
- **"Total rotor losses"** here means rotor copper **plus** friction and windage (the whole of $P_g-P_{out}$); "ohmic" isolates the copper.
- Using the full-load slip to find $P_{cu2}$ would be circular: the slip is *obtained from* $P_{cu2}/P_g$.
- The sheet's $1468.2$ rpm and $89.2\ \%$ are rounding differences (by $0.3$ rpm and $0.1\ \%$).

## Concepts used
- Power flow in the induction motor, slip from the loss ratio, no-load test ([[Theory - Three-Phase Induction Machines]], [[Induction Motor - Slip, Rotor Circuit and Power Flow]])
