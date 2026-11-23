---
tags: [EE1100, tutorial-solution, machines, induction-machine, slip, synchronous-speed]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q6: Synchronous Speed, Rotor Speed and Rotor Frequency

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q5 - Torque-Slip Characteristic]] · Next: [[T8-Q7 - Relative Speeds of the Fields]]

> [!question] A 3-phase induction motor has 4 poles and is supplied by a 50 Hz balanced 3-phase voltage; it runs at a slip of 6 %. Determine (a) the synchronous speed in rpm, (b) the rotor speed in rpm, (c) the frequency of voltage and current in the rotor circuit. *[Sheet: 1500 rpm, 1410 rpm, 3 Hz]*

**Tests:** [[T8-Q3 - Synchronous Speed|$n_s=120f/P$]], [[T8-Q4 - Slip|slip]], $f_2=sf_1$.

## Given
$P=4$, $f_1=50$ Hz, $s=0.06$.

## Principle and why it applies
The stator field turns at $n_s=120f/P$ irrespective of load; the rotor lags by the slip, $n_r=(1-s)n_s$; the rotor conductors see the field sweep past at the *difference* speed $sn_s$, so the rotor emf and current have frequency $f_2=sf_1$.

## Solution
**(a)** $n_s=\dfrac{120\times50}{4}=\mathbf{1500\ rpm}$.

**(b)** $n_r=(1-s)n_s=(1-0.06)\times1500=\mathbf{1410\ rpm}$.

**(c)** $f_2=sf_1=0.06\times50=\mathbf{3\ Hz}$.

## Result
$$\boxed{n_s=1500\ \text{rpm},\quad n_r=1410\ \text{rpm},\quad f_2=3\ \text{Hz}}$$

## Check
Relative speed $n_s-n_r=90$ rpm $=1.5$ rev/s; with 2 pole pairs the rotor sees $2\times1.5=3$ cycles per second ✓ $=f_2$.

## Trap / alternative
The rotor frequency is not $50$ Hz (that is the **standstill** value, $s=1$) but $3$ Hz. Always use the number of poles, $P=4$, in $n_s$; and write the slip as a fraction ($0.06$) in the products.

## Concepts used
- Synchronous speed, slip, rotor frequency ([[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Revolving Magnetic Field and Synchronous Speed]])
