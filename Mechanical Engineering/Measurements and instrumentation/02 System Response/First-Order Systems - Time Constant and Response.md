---
tags: [concept, instrumentation]
course: "Measurements, Instrumentation and Control (ME2400)"
aliases: [First-order system, Time constant, Step response, Ramp response, Thermocouple response, Dynamic characteristics, RC filter]
---

# First-Order Systems — Time Constant and Response

> [!abstract] In one breath
> Any instrument that stores one kind of energy (a thermocouple bead, an RC circuit, a pressure gauge with a tube) obeys $\tau\,\dot y+y=Kx$. It is characterised by **one number, the time constant $\tau$**: after a step it reaches 63 % in $\tau$ and 95 % in $3\tau$, and it lags a ramp by a constant $\tau$. As a frequency response it is a **low-pass filter** with corner at $1/\tau$.

Part of [[Measurements, Instrumentation and Control - MOC]]. Previous: [[Sensors and Signal Conditioning]]. Next: [[Second-Order Systems - Damping and Overshoot]].

## 1. The model

$$
\tau\frac{dy}{dt}+y=Kx(t)\quad\Longleftrightarrow\quad G(s)=\frac{Y(s)}{X(s)}=\frac{K}{\tau s+1}
$$

$K$ is the static gain (output per unit input), $\tau$ the time constant.

| Input | Response | Key facts |
| --- | --- | --- |
| **Step** of size $A$ | $y=KA(1-e^{-t/\tau})$ | 63.2 % at $t=\tau$; 86.5 % at $2\tau$; 95 % at $3\tau$; 99 % at $4.6\tau$ |
| **Ramp** $x=at$ | $y=Ka[t-\tau(1-e^{-t/\tau})]$ | after a few $\tau$ the output follows with a constant **lag $\tau$ in time** ($=Ka\tau$ in the reading) |
| **Sinusoid** $\sin\omega t$ | amplitude ratio $\dfrac{K}{\sqrt{1+(\omega\tau)^2}}$, phase $-\tan^{-1}(\omega\tau)$ | $-3$ dB and $-45^\circ$ at $\omega=1/\tau$ |

**Bandwidth.** $\omega_b=1/\tau$ (or $f_b=1/2\pi\tau$): signals much slower than this pass; much faster are attenuated by $1/(\omega\tau)$ (−20 dB per decade).

## 2. Worked example: a thermocouple

A thermocouple with $\tau=2$ s:

| Test | Result |
| --- | --- |
| step: 63 % / 95 % / 99 % | 2 s / 6 s / **9.2 s** |
| ramp 10 K/s | steady reading lag $=10\times2=\mathbf{20\ K}$ |
| 0.1 Hz sine ($\omega\tau=1.26$) | amplitude **62 %**, phase **−51°** |
| bandwidth | $1/(2\pi\tau)=0.080$ Hz |

A measurement in a changing temperature is therefore wrong by $\tau\,(dT/dt)$ unless corrected. To measure faster you need a smaller $\tau$.

![[MIC-2-first-order.png]]

## 3. Where $\tau$ comes from

**Thermal sensor** (lumped capacitance, see [[Transient Conduction - Lumped Capacitance and Heisler Charts]]): $\tau=\dfrac{\rho cV}{hA}$. For a spherical bead, $\tau=\rho cd/(6h)$: a 1 mm bead of $\rho=8500$ kg/m³, $c=400$ J/kgK in a gas with $h=100$ W/m²K: $\tau=8500(400)(10^{-3})/(600)=\mathbf{5.7\ s}$. The same bead in a stirred liquid ($h=3000$) has $\tau=0.19$ s. **$\tau$ depends on the surroundings, not only on the sensor.**

**Electrical:** an RC low-pass: $\tau=RC$. **Fluid:** a tank draining through a valve, $\tau=A_{tank}R$. **Mechanical:** a mass with viscous damping, $\tau=m/c$.

## 4. Measuring $\tau$

Apply a step and record: find the time to 63.2 % of the final change, or plot $\ln(1-y/y_\infty)$ against $t$: a straight line of slope $-1/\tau$ for a true first-order system. A line that curves means a higher order.

> [!warning] Traps
> - Using the 63 % rule on a non-first-order system: the step response of a second-order system is not an exponential.
> - Thinking the sensor reads the right value after $\tau$: it has reached only 63 % of the change.
> - Reading the lag of a ramp as vanishing: it stays at $\tau$ **forever**, in a steady ramp.
> - Quoting $\tau$ without the environment ($h$).
> - Sampling and recording at an interval comparable to $\tau$ and losing the dynamics.

> [!question]- Predict first: the thermocouple above sees a temperature rising linearly for a long time at 10 K/s. What does it read, relative to the true value?
> It reads 20 K low, constant, after the first few time constants (about 10 s). The sensor lags by $\tau=2$ s of ramp, so it reports the temperature of 2 seconds ago.

> [!question]- By how much must the bead diameter shrink to halve $\tau$?
> $\tau\propto d$ for a sphere, so halve the diameter (to 0.5 mm). Also the response in a given gas improves with higher $h$ (faster flow).

## 5. Connections

- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — the same exponential and the same meaning of $\tau$.
- [[04 Capacitors, Inductors and First Order Circuits]] — the RC and RL circuit are first-order instruments.
- [[Transient Conduction - Lumped Capacitance and Heisler Charts]] — $\tau=\rho Vc/hA$ is a thermal RC.
- [[Filter Theory]] and [[Frequency Response and Resonance Curves]] — the first-order low-pass.
- [[Frequency Response, Nyquist Plots and Stability Margins]] — its Bode plot is the building block of every loop.
