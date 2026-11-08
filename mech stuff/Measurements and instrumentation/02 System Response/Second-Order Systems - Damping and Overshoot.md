---
tags: [concept, instrumentation]
course: "Measurements, Instrumentation and Control (ME2400)"
aliases: [Second-order system, Natural frequency, Damping ratio, Overshoot, Settling time, Accelerometer, Resonant peak, Underdamped]
---

# Second-Order Systems — Damping and Overshoot

> [!abstract] In one breath
> A system with inertia and a spring (an accelerometer, a pressure gauge with a diaphragm, a U-tube manometer) follows $\ddot y+2\zeta\omega_n\dot y+\omega_n^2y=\omega_n^2Kx$. Two numbers decide everything: the **natural frequency $\omega_n$** (speed) and the **damping ratio $\zeta$** (overshoot). For instruments **$\zeta\approx0.7$** gives the flattest response and the quickest settling.

Part of [[Measurements, Instrumentation and Control - MOC]]. Previous: [[First-Order Systems - Time Constant and Response]]. Next: [[Feedback, Block Diagrams and Transfer Functions]]. This is the same equation as the vault's universal second-order system: [[The Universal Second-Order Linear System]], [[Series RLC Natural Response - Damping Cases]].

## 1. Model

$$
G(s)=\frac{K\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2},\qquad \omega_n=\sqrt{\frac km},\quad \zeta=\frac{c}{2\sqrt{km}}
$$

| $\zeta$ | Response to a step |
| --- | --- |
| $<1$ underdamped | oscillates at $\omega_d=\omega_n\sqrt{1-\zeta^2}$ inside an envelope $e^{-\zeta\omega_nt}$ |
| $=1$ critical | fastest without overshoot |
| $>1$ overdamped | two real poles, sluggish |

## 2. Step-response measures (underdamped)

$$
M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}},\quad t_p=\frac\pi{\omega_d},\quad t_s(2\%)\approx\frac{4}{\zeta\omega_n},\quad \zeta\approx\frac{\ln(1/M_p)}{\sqrt{\pi^2+\ln^2M_p}}
$$

| $\zeta$ | overshoot $M_p$ |
| --- | --- |
| 0.1 | 72.9 % |
| 0.2 | 52.7 % |
| 0.4 | 25.4 % |
| **0.7** | **4.6 %** |

**Example.** $\omega_n=100$ rad/s, $\zeta=0.2$: $\omega_d=98.0$ rad/s, $M_p=\mathbf{52.7\ \%}$, peak at $t_p=32$ ms, settling (2 %) $4/(0.2\times100)=\mathbf{0.20\ s}$. Raising $\zeta$ to 0.7 gives $M_p=4.6$ % and $t_s=57$ ms: **3.5 times faster to settle** and almost no overshoot.

## 3. Frequency response

$$
|G(j\omega)|=\frac{K}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\quad r=\frac\omega{\omega_n},\qquad
M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}\ \text{at}\ \omega_r=\omega_n\sqrt{1-2\zeta^2}
$$

For $\zeta=0.2$ the resonant peak is $M_r=2.55$ (8.1 dB) at 95.9 rad/s: the instrument **amplifies** vibration near its natural frequency. For $\zeta\ge0.707$ there is no peak, and the response is flat ($\pm$ few %) up to about $\omega_n$. Above $\omega_n$ it rolls off at −40 dB per decade.

![[MIC-3-second-order.png]]

## 4. Choosing the design

- **Accelerometer** (seismic mass): the output is flat for frequencies **below** $\omega_n$, so a stiff, light sensor with $\zeta\approx0.7$ gives a wide usable band; piezoelectric types have very high $\omega_n$ and almost no damping and are used well below it.
- **Vibration (seismic) pickup** for displacement: used *above* $\omega_n$, where the mass stays still: needs low $\omega_n$ (soft spring, heavy mass).
- **Manometers, galvanometers, diaphragm gauges:** damp to about 0.7 for a quick, flat response.
- **Measuring $\zeta$ from a step:** overshoot $M_p$ gives $\zeta$; the period $2\pi/\omega_d$ gives $\omega_n$. Alternatively the logarithmic decrement $\delta=\ln(x_k/x_{k+1})=2\pi\zeta/\sqrt{1-\zeta^2}$ from successive peaks.

> [!warning] Traps
> - Using $t_s=4/(\zeta\omega_n)$ for an overdamped system: it applies to the underdamped case.
> - Confusing $\omega_d$ and $\omega_n$ (they differ by a few % for $\zeta<0.3$, but not at higher damping).
> - Believing the resonance is at $\omega_n$: it is at $\omega_n\sqrt{1-2\zeta^2}$, and absent for $\zeta>0.707$.
> - Using a 0.1-damped sensor near its natural frequency: the reading is 5 times too large.
> - Assuming $\zeta$ is a property of the sensor alone: air and oil change the damping.

> [!question]- Predict first: an accelerometer with $\omega_n=1000$ rad/s and $\zeta=0.01$ measures a vibration at 900 rad/s. Is the reading accurate?
> No: $r=0.9$ gives $1/\sqrt{(1-0.81)^2+(0.018)^2}=5.2$: the reading is 5.2 times too high. Use the sensor only for $\omega\ll\omega_n$ (say $<0.2\omega_n$ for 4 % error) or add damping.

> [!question]- Why does $\zeta=0.7$ settle fastest?
> Below it the system rings and takes long to enter the ±2 % band; above it the slow pole dominates. $\zeta\approx0.7$ gives only 4.6 % overshoot and enters the band almost immediately: the best compromise between speed and ringing.

## 5. Connections

- [[The Universal Second-Order Linear System]] — mass–spring–damper, RLC and this instrument are one equation.
- [[Series RLC Natural Response - Damping Cases]] — the same damping cases in circuit form.
- [[Frequency Response and Resonance Curves]] — resonance peak, bandwidth and Q ($Q=1/2\zeta$).
- [[Vibration of Particles and Rigid Bodies]] — $\omega_n$, $\zeta$ and forced response of a mass-spring system.
- [[Damped Oscillations]] and [[Driven Oscillations and Resonance]] — interactive versions of the same response.
