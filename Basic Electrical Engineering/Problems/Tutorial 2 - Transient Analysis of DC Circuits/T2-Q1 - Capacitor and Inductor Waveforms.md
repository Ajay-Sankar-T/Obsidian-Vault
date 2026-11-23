---
tags: [EE1100, tutorial-solution, DC-circuits, transients, capacitor, inductor]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q1: Voltage, Current and Power Waveforms of C and L

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Next: [[T2-Q2 - DC Steady State with L and C]]

> [!question] (a) Sketch $v(t)$ and $p(t)$ for an 8 µF capacitor whose current (in mA) is a pulse train: $+20$ mA for $0<t<4$ ms, $0$ for $4<t<8$ ms, $-10$ mA for $8<t<16$ ms; $v(0)=0$. (b) Sketch $i(t)$ and $p(t)$ for a 40 mH inductor with the *same-shaped* voltage waveform in mV ($+20,\,0,\,-10$ mV); $i(0)=0$.

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#1. The storage elements|the C and L laws]], integration of a piecewise-constant waveform, instantaneous power and energy.

## Given
Capacitor: $C=8\ \mu$F, $i_C(t)$ as above, $v_C(0)=0$. Inductor: $L=40$ mH, $v_L(t)$ as above, $i_L(0)=0$.

## Principle and why it applies
The element laws are *integral* laws: $v_C(t)=v_C(0)+\dfrac1C\displaystyle\int_0^t i\,dt$ and $i_L(t)=i_L(0)+\dfrac1L\displaystyle\int_0^t v\,dt$. A piecewise-**constant** $i$ (or $v$) integrates to a piecewise-**linear** $v$ (or $i$): ramps with slope $i/C$ (or $v/L$). Because $v_C$ and $i_L$ are continuous they join the ramps without jumps. Instantaneous power is $p=vi$, positive while energy is stored, negative while it is returned.

## Diagram
![[T2-Q1-waveforms.png]]

## Solution
**(a) Capacitor.**
- $0<t<4$ ms: slope $\dfrac{20\ \text{mA}}{8\ \mu\text{F}}=2.5$ V/ms, so $v$ rises to $2.5\times4=10$ V. $p=vi$ grows linearly from $0$ to $10\times20\ \text{mA}=0.2$ W.
- $4<t<8$ ms: $i=0$, so $v$ stays at 10 V and $p=0$.
- $8<t<16$ ms: slope $\dfrac{-10\ \text{mA}}{8\ \mu\text{F}}=-1.25$ V/ms, so $v$ falls by $1.25\times8=10$ V, back to $0$ at 16 ms. $p=vi$ steps to $10\times(-10\ \text{mA})=-0.1$ W and decays linearly to $0$.

**(b) Inductor** (the same shape, with $L$ replacing $1/C$).
- $0<t<4$ ms: slope $\dfrac{20\ \text{mV}}{40\ \text{mH}}=0.5$ A/s $=0.5$ mA/ms, so $i$ reaches $2$ mA. $p$ rises to $20\ \text{mV}\times2\ \text{mA}=40\ \mu$W.
- $4<t<8$ ms: $v=0$, $i=2$ mA constant, $p=0$.
- $8<t<16$ ms: slope $\dfrac{-10\ \text{mV}}{40\ \text{mH}}=-0.25$ mA/ms, so $i$ returns to $0$ at 16 ms; $p$ steps to $2\ \text{mA}\times(-10\ \text{mV})=-20\ \mu$W and decays to $0$.

## Result
| | $v$ or $i$ at 4 ms | at 8 ms | at 16 ms | peak $p$ |
|---|---|---|---|---|
| capacitor $v_C$ | 10 V | 10 V | 0 | $+0.2$ W (at 4 ms⁻), $-0.1$ W (at 8 ms⁺) |
| inductor $i_L$ | 2 mA | 2 mA | 0 | $+40\ \mu$W, $-20\ \mu$W |

## Check
Energy stored at 4 ms: capacitor $\tfrac12Cv^2=\tfrac12(8\ \mu)(10^2)=0.4$ mJ $=$ area of the first triangle of $p$: $\tfrac12\times0.2\ \text{W}\times4\ \text{ms}=0.4$ mJ ✓. Over the whole waveform the net area under $p$ is $0.4-0.4=0$ (the second, negative triangle $\tfrac12\times0.1\times8$ ms $=0.4$ mJ) so **all the stored energy is returned** and $v(16)=0$ ✓. For the inductor, $\tfrac12(40\ \text{mH})(2\ \text{mA})^2=80$ nJ $=\tfrac12\times40\ \mu\text{W}\times4$ ms ✓.

## Trap / alternative
The current through the capacitor **jumps** at 4 ms and 8 ms but its voltage does not; likewise the *voltage* across the inductor jumps while its current does not. Only the integrated quantity is continuous. The power waveform *does* jump (it is the product of a continuous and a jumping quantity). Also label the **sign**: negative power does not mean "wrong", it means the element is releasing stored energy.

## Concepts used
- Capacitor and inductor laws, continuity of $v_C$ and $i_L$, power and energy ([[Theory - Transients in RL, RC and RLC Circuits]])
