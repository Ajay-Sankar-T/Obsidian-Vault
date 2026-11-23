---
tags: [EE1100, tutorial-solution, machines, induction-machine, slip]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q4: Slip and Its Typical Value

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]], [[Induction Motor - Slip, Rotor Circuit and Power Flow]] · Previous: [[T8-Q3 - Synchronous Speed]] · Next: [[T8-Q5 - Torque-Slip Characteristic]]

> [!question] Define the slip $s$ of an induction machine. What is its typical value for an induction motor running in steady state?

**Tests:** definition and meaning of slip, its range of values, the rotor frequency $f_2=sf_1$.

## Principle and why it applies
The rotor runs slower than the revolving field. The **slip** measures the *fractional speed lag* of the rotor behind the field:
$$\boxed{s=\frac{n_s-n_r}{n_s}=\frac{\omega_s-\omega_r}{\omega_s}},\qquad n_r=(1-s)\,n_s.$$
It also measures the **relative motion** that induces the rotor emf: the field sweeps past the rotor at $n_s-n_r=s\,n_s$, so the induced emf and its frequency are proportional to $s$:
$$E_{2s}=sE_{20},\qquad f_2=s\,f_1.$$

## Solution
**Values of slip:**

| Condition | $n_r$ | $s$ |
|---|---|---|
| standstill (instant of starting) | $0$ | $1$ |
| **full-load, steady-state motoring** | slightly below $n_s$ | **about 0.02–0.06 (2–6 %)** |
| no load | almost $n_s$ | below $0.01$ |
| synchronous speed (ideal, no torque) | $n_s$ | $0$ |
| above synchronous (generator) | $>n_s$ | $<0$ |
| reverse (braking, "plugging") | opposite to field | $>1$ |

**Typical steady-state value: $s\approx2$–$6\ \%$** (about $1\ \%$ or less in very large machines, up to $5$–$8\ \%$ in small ones). Example: a 4-pole, 50 Hz motor with $s=4\ \%$ runs at $1440$ rpm and the rotor frequency is $2$ Hz.

## Result
$$s=\frac{n_s-n_r}{n_s};\qquad \text{steady-state motoring: }s\approx0.02\text{–}0.06.$$

## Check
A small slip means the motor is nearly a **constant-speed** machine (speed varies by only a few % from no load to full load), and the rotor current frequency $sf_1\approx1$–$3$ Hz is low, so the rotor core loss is negligible. Also, from the power split $P_{cu2}=sP_g$, $s=4\ \%$ means $4\ \%$ of the air-gap power is lost as rotor copper.

## Trap / alternative
- Slip is a fraction of the **synchronous** speed, not of the rotor speed.
- Slip can be quoted as a fraction or in per cent ($0.04=4\ \%$); **don't** put the percentage into $f_2=sf_1$ without converting.
- "Low slip" means high efficiency in the rotor stage; a high-slip motor (large resistance, e.g. a crane motor) wastes more as rotor copper.

## Concepts used
- Slip, rotor frequency, rotor emf at slip ([[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Theory - Three-Phase Induction Machines]])
