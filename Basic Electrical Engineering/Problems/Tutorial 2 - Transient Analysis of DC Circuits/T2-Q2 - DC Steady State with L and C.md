---
tags: [EE1100, tutorial-solution, DC-circuits, transients, steady-state, energy]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q2: DC Steady State with an Inductor and a Capacitor

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q1 - Capacitor and Inductor Waveforms]] · Next: [[T2-Q3 - DC Steady State with a Current Source]]

> [!question] Find $I_{in}$, $V_1$ and $V_2$ under DC steady state with $V_{in}=15$ V. If $L=16$ mH and the total energy stored in the circuit is 5 mJ in the steady state, find $C$. *[Sheet: $I_{in}=0.5$ A, $V_1=10$ V, $V_2=5$ V, $C=60\ \mu$F]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#2. DC steady state (Q2, Q3)|DC steady state]], stored energy.

## Given
15 V source; $20\ \Omega$ in parallel with the capacitor $C$ (voltage $V_1$); then the inductor $L=16$ mH in series with a $10\ \Omega$ resistor (voltage $V_2$ across the resistor).

## Principle and why it applies
"DC steady state" means all currents and voltages are constant, so $dv_C/dt=0$ and $di_L/dt=0$: the capacitor carries **no current** (open circuit) and the inductor has **no voltage** (short circuit). The circuit collapses to resistors, and the stored energies follow from the values of $v_C$ and $i_L$.

## Diagram
![[T2-Q2-circuit.png]]

## Solution
With $C$ open and $L$ shorted, the $20\ \Omega$ and $10\ \Omega$ are in series:
$$I_{in}=\frac{15}{20+10}=\mathbf{0.5\ A}.$$
The capacitor sits in parallel with the $20\ \Omega$: $V_1=0.5\times20=\mathbf{10\ V}$. The inductor is a short, so $V_2$ is the whole drop in the $10\ \Omega$: $V_2=0.5\times10=\mathbf{5\ V}$.

Energy: the inductor carries $I_L=I_{in}=0.5$ A, so
$$E_L=\tfrac12LI_L^2=\tfrac12(16\ \text{mH})(0.5)^2=2\ \text{mJ}.$$
The capacitor must hold the remainder: $E_C=5-2=3$ mJ $=\tfrac12CV_1^2$, so
$$C=\frac{2E_C}{V_1^2}=\frac{2\times3\times10^{-3}}{100}=\mathbf{60\ \mu F}.$$

## Result
$$\boxed{I_{in}=0.5\ \text{A},\quad V_1=10\ \text{V},\quad V_2=5\ \text{V},\quad C=60\ \mu\text{F}}$$

## Check
KVL: $V_1+V_2=10+5=15$ V $=V_{in}$ ✓ (the inductor drops no DC voltage).

## Trap / alternative
The capacitor value is **not needed** to find the three steady-state quantities. It enters only in the energy part, which is why the question gives the energy last. A common slip is to use the source voltage (15 V) for the capacitor energy; the capacitor sees only $V_1$.

## Concepts used
- Open/short equivalents at DC, energy in $L$ and $C$ ([[Theory - Transients in RL, RC and RLC Circuits]])
