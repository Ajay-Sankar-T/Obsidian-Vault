---
tags: [EE1100, tutorial-solution, machines, induction-machine, slip, rotating-field]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q7: Poles, Slip and Relative Speeds of Stator and Rotor Fields

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q6 - Speeds and Rotor Frequency]] · Next: [[T8-Q8 - Rotor Current, Power Factor and Torque]]

> [!question] A three-phase 50 Hz induction motor has a full-load speed of 1440 rpm. Calculate (a) the number of poles; (b) the full-load slip and rotor frequency; (c) the speed of the stator field with respect to (i) the stator structure and (ii) the rotor structure; (d) the speed of the rotor field with respect to (i) the rotor structure, (ii) the stator structure, (iii) the stator field. *[Sheet: 4; $s=0.04$, $f_2=2$ Hz; (c) 1500, 60 rpm; (d) 60, 1500, 0 rpm]*

**Tests:** choosing the synchronous speed just above the rated speed, and tracking *relative* speeds, the condition for steady torque.

## Given
$f_1=50$ Hz, $n_r=1440$ rpm (full load, slightly below the synchronous speed).

## Principle and why it applies
The rated speed must be just below $n_s=120f/P$ with $P$ an even integer. The candidates are $3000,1500,1000,\dots$ rpm, so $n_s=1500$ rpm. The rotor field is produced by the **rotor currents**, which have frequency $sf_1$, so relative to the rotor structure it rotates at $sn_s$.

## Diagram
![[T8-Q7-speeds.png]]

## Solution
**(a)** $n_s$ must be the smallest synchronous speed above 1440 rpm: $n_s=1500$ rpm, so $P=\dfrac{120f}{n_s}=\dfrac{120\times50}{1500}=\mathbf{4\ poles}$.

**(b)** $s=\dfrac{1500-1440}{1500}=\mathbf{0.04}$ ($4\ \%$), $f_2=sf_1=\mathbf{2\ Hz}$.

**(c) Stator field.**
- (i) with respect to the **stator structure**: $n_s=\mathbf{1500\ rpm}$.
- (ii) with respect to the **rotor structure**: $n_s-n_r=1500-1440=\mathbf{60\ rpm}$ (this is $sn_s$).

**(d) Rotor field.** The rotor currents (frequency $sf_1=2$ Hz) set up a field that turns, relative to the rotor, at $\dfrac{120f_2}{P}=\dfrac{120\times2}{4}=sn_s$:
- (i) with respect to the **rotor structure**: $\mathbf{60\ rpm}$ (in the same direction as the stator field).
- (ii) with respect to the **stator structure**: $60+n_r=60+1440=\mathbf{1500\ rpm}$.
- (iii) with respect to the **stator field**: $1500-1500=\mathbf{0\ rpm}$.

## Result
$$\boxed{P=4;\ \ s=0.04,\ f_2=2\ \text{Hz};\ \ \text{stator field: }1500,\ 60\ \text{rpm};\ \ \text{rotor field: }60,\ 1500,\ 0\ \text{rpm}}$$

## Check
(d)(iii) $=0$ is the essential result: stator and rotor fields are **stationary relative to each other** at every slip, which is the condition for a steady, non-pulsating torque. The rotor field is always locked to the stator field even though the rotor itself turns slower than both.

## Trap / alternative
- Don't choose $n_s=3000$ rpm ($P=2$): the slip would be $52\ \%$, far outside the working range.
- Distinguish "w.r.t. the **structure**" (the physical rotor or stator) from "w.r.t. the **field**": the rotor field's speed w.r.t. the rotor is only $60$ rpm but w.r.t. the stator it is $1500$ rpm.

## Concepts used
- Synchronous speed, slip, relative speed of the fields ([[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Revolving Magnetic Field and Synchronous Speed]])
