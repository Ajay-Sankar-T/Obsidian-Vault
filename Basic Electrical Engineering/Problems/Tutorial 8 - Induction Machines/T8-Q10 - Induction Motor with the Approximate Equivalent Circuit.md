---
tags: [EE1100, tutorial-solution, machines, induction-machine, equivalent-circuit, efficiency]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q10: A 50 hp Motor from the Approximate Equivalent Circuit

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q9 - Power Flow and Efficiency of a Delta-Connected Motor]] · Next: [[T8-Q11 - Equivalent Circuit and Starting of an Induction Motor]]

> [!question] A three-phase, four-pole, 50 hp, 440 V, 60 Hz, Y-connected induction motor has, per phase, $r_1=0.10$, $x_1=0.35$, $r_2'=0.12$, $x_2'=0.40\ \Omega$. Stator core losses are $1200$ W and rotational losses $950$ W; at no load the motor draws $18$ A at power factor $0.089$ lagging. At a slip of $2.5\ \%$ find (a) the input line current and power factor, (b) the developed torque, (c) the output horsepower, (d) the efficiency. *[Sheet: $58.2$ A, $0.895$ lag; $201$ N·m; $48.25$ hp; $89.6\ \%$]*

**Tests:** the **approximate** equivalent circuit (shunt branch at the input), complex-current addition, power flow.

## Given
Per phase: $V_1=440/\sqrt3=254.0$ V. $n_s=120\times60/4=1800$ rpm, $\omega_s=188.5$ rad/s. $s=0.025$.

## Principle and why it applies
Because the magnetising branch is small compared with the series impedance, it can be moved to the input terminals: the stator current is then the *phasor sum* of the load (rotor) current and the **no-load current** $I_0$ given by the no-load test:
$$\bar I_1=\bar I_2'+\bar I_0,\qquad \bar I_2'=\frac{\bar V_1}{(r_1+r_2'/s)+j(x_1+x_2')}.$$

## Diagram
![[T8-Q10-Q11-equivalent-circuit.png]]

## Solution
**Load branch:** $r_2'/s=0.12/0.025=4.8\ \Omega$, so $Z=(0.10+4.8)+j(0.35+0.40)=4.9+j0.75=4.957\angle8.70^\circ\ \Omega$:
$$\bar I_2'=\frac{254.0}{4.957\angle8.70^\circ}=51.25\angle-8.70^\circ\ \text{A}.$$
**No-load current:** $\bar I_0=18\angle-\cos^{-1}0.089=18\angle-84.9^\circ=1.60-j17.93$ A.

**(a)** $\bar I_1=(50.66-j7.75)+(1.60-j17.93)=52.26-j25.68=\mathbf{58.2\angle-26.2^\circ\ A}$, so the power factor is $\cos26.2^\circ=\mathbf{0.897}$ lagging.

**(b) Developed torque.** Air-gap power per phase is $I_2'^2\,r_2'/s$, so
$$P_g=3\times51.25^2\times4.8=37\,818\ \text{W},\qquad T_{dev}=\frac{P_g}{\omega_s}=\frac{37\,818}{188.5}=\mathbf{200.6\ N\cdot m}.$$

**(c) Output power:**
$$P_{mech}=(1-s)P_g=0.975\times37\,818=36\,872\ \text{W},\qquad P_{out}=P_{mech}-P_{rot}=36\,872-950=35\,922\ \text{W}=\frac{35\,922}{746}=\mathbf{48.15\ hp}.$$

**(d) Efficiency.** Input power from the circuit: $P_{in}=\sqrt3\,V_LI_1\cos\phi=3\times254.0\times58.2\times0.897=39\,830$ W, so
$$\eta=\frac{35\,922}{39\,830}=\mathbf{90.2\ \%}.$$
If instead the losses are summed with the stator copper loss taken on the **full** line current (as the sheet appears to do): $P_{cu1}=3\times58.2^2\times0.10=1017$ W, $P_{cu2}=sP_g=945$ W, core $1200$ W, rotational $950$ W; $\eta=\dfrac{35\,922}{35\,922+4112}=89.7\ \%$.

## Result
$$\boxed{I_1=58.2\ \text{A},\ pf=0.897\ \text{lag};\ \ T_{dev}=200.6\ \text{N·m};\ \ P_{out}=35.9\ \text{kW}=48.15\ \text{hp};\ \ \eta\approx90\ \%\ (90.2\ \text{or}\ 89.7\ \%\ \text{depending on the loss bookkeeping})}$$

## Check
No-load power from the data: $P_0=\sqrt3\times440\times18\times0.089=1221$ W $\approx$ the stated core loss ($1200$ W): the shunt branch represents the core loss, so the rotational loss $950$ W is a *separate* mechanical loss subtracted after $P_{mech}$ ✓. The torque $201$ N·m agrees with the sheet; the output $48.15$ hp differs from the printed $48.25$ by $0.2\ \%$ (the sheet's $746$ W/hp and rounding).

## Trap / alternative
- The **efficiency differs by 0.5 %** according to whether $I_0^2r_1$ is counted; the approximate circuit ignores the magnetising current in $r_1$, so $90.2\ \%$ is the consistent value *within that circuit*, while $89.7\ \%$ (and the sheet's $89.6\ \%$) uses the full $I_1$ in $r_1$.
- $I_1$ is the **phasor** sum, not $51.25+18=69.3$ A.
- Use $\omega_s$ (synchronous), not the rotor speed, for the developed torque.

## Concepts used
- Approximate equivalent circuit, no-load current, power flow ([[Theory - Three-Phase Induction Machines]], [[Induction Motor - Slip, Rotor Circuit and Power Flow]])
