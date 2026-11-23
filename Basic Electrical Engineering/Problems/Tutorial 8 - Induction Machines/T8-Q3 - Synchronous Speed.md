---
tags: [EE1100, tutorial-solution, machines, induction-machine, synchronous-speed]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q3: The Synchronous Speed $n_s=120f/P$

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]], [[Revolving Magnetic Field and Synchronous Speed]] · Previous: [[T8-Q2 - The Revolving Field]] · Next: [[T8-Q4 - Slip]]

> [!question] The speed at which the revolving field rotates in the air gap is the synchronous speed. Write the expression for the synchronous speed of an induction machine of $P$ poles supplied at frequency $f$ (Hz).

**Tests:** electrical versus mechanical angle, poles versus pole pairs.

## Principle and why it applies
The field pattern rotates at the supply (electrical) angular frequency $\omega=2\pi f$ *in electrical degrees*. A machine with $P$ poles has $P/2$ **pole pairs**; one pole pair spans $360^\circ$ electrical but only $360^\circ/(P/2)$ **mechanical**. So the *mechanical* angle swept per electrical cycle is $\dfrac{2}{P}$ of a turn:
$$\theta_{elec}=\frac P2\,\theta_{mech}\ \Rightarrow\ \omega_s=\frac{\omega}{P/2}=\frac{4\pi f}{P}\ \text{rad/s}.$$

## Solution
Convert to revolutions per minute ($1$ rad/s $=60/2\pi$ rpm):
$$\boxed{n_s=\frac{120\,f}{P}\ \text{rpm}}\qquad\Big(n_s=\frac{2f}{P}\ \text{rev/s}=\frac{f}{p}\ \text{rev/s},\ p=\frac P2\ \text{pole pairs}\Big).$$

| Poles $P$ | 2 | 4 | 6 | 8 | 12 |
|---|---|---|---|---|---|
| $n_s$ at 50 Hz (rpm) | 3000 | 1500 | 1000 | 750 | 500 |
| $n_s$ at 60 Hz (rpm) | 3600 | 1800 | 1200 | 900 | 600 |

(The motor of Q6 is a 4-pole, 50 Hz machine: $n_s=120\times50/4=1500$ rpm.)

## Result
$$n_s=\frac{120f}{P}\ \text{rpm}.$$
The synchronous speed is fixed **only** by the supply frequency and the number of poles; the load changes the rotor speed, not $n_s$.

## Check
$P=2$, $f=50$: one electrical cycle $=$ one mechanical revolution, so $n_s=50$ rev/s $=3000$ rpm ✓. Doubling the poles halves the speed ✓.

## Trap / alternative
- $P$ is the **number of poles**, not pole pairs: using the pole-pair count gives $n_s=60f/p$ and the formula "$120f/P$" with $P=p$ is off by a factor of 2.
- To change the speed of a given motor: change $f$ (inverter drive), change the number of poles (pole-changing windings), or accept more slip (rotor resistance, voltage control).
- Speeds quoted on nameplates (e.g. 1440 rpm) are the **rotor** speed at full load, just below $n_s$.

## Concepts used
- Revolving field, pole pairs, electrical and mechanical angles ([[Revolving Magnetic Field and Synchronous Speed]], [[Theory - Three-Phase Induction Machines]])
