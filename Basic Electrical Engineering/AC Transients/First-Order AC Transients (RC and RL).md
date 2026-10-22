---
tags:
  - EE1100
  - AC-circuits
  - transients
  - first-order
up: "[[AC Transients]]"
---

# First-Order AC Transients (RC and RL)

← up: [[AC Transients|AC Transients]] · builds on: [[Concepts#RC/RL Transients and Time Constant|RC/RL Transients and Time Constant]], [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]

## Universal first-order AC template

$$\boxed{x(t)=x_{ss}(t)+\big[x(0^+)-x_{ss}(0^+)\big]e^{-t/\tau}}$$

The critical difference from the DC version in [[04 Capacitors, Inductors and First Order Circuits|Week 4]]: there, $x_{ss}$ (called $x_\infty$) is a **constant**. Here, $x_{ss}(t)$ is a **time-varying sinusoid**, found from phasor analysis, so the "gap" $x(0^+)-x_{ss}(0^+)$ must be evaluated at $t=0$ using the sinusoid's own value there, not a DC final value.

## RC circuit with an AC source

Series RC driven by $v_s(t)=V_m\sin\omega t$. Impedance $Z=R-j/(\omega C)$, so $|Z|=\sqrt{R^2+1/(\omega C)^2}$, $\theta_Z=-\tan^{-1}\!\big(1/(\omega CR)\big)$ (from [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]). Steady-state current:

$$i_{ss}(t)=I_m\sin(\omega t+\phi),\qquad \phi=-\theta_Z>0\ (\text{current leads})$$

Complete response:

$$i(t)=I_m\sin(\omega t+\phi)+Ae^{-t/RC}$$

**Finding $A$:** at $t=0^+$, $i(0^+)=I_m\sin\phi+A$, so

$$A=i(0^+)-I_m\sin\phi$$

giving

$$i(t)=I_m\sin(\omega t+\phi)+\big[i(0^+)-I_m\sin\phi\big]e^{-t/RC}$$

with $i(0^+)$ fixed by the capacitor-voltage continuity rule $v_C(0^+)=v_C(0^-)$ from [[AC Transients|AC Transients]].

## RL circuit with an AC source

Series RL: $Z=R+j\omega L$, $|Z|=\sqrt{R^2+(\omega L)^2}$, $\phi=\tan^{-1}(\omega L/R)$, current **lags**:

$$i_{ss}(t)=I_m\sin(\omega t-\phi)$$

Time constant $\tau=L/R$ (same formula as [[Concepts#RC/RL Transients and Time Constant|RC/RL Transients and Time Constant]]). Complete response:

$$i(t)=I_m\sin(\omega t-\phi)+Ae^{-Rt/L}$$

At $t=0^+$: $i(0^+)=-I_m\sin\phi+A$, so

$$A=i(0^+)+I_m\sin\phi$$

using $i_L(0^+)=i_L(0^-)$ (inductor current continuity).

## Worked pattern

$v(t)=100\sin(100t)$, $R=10\ \Omega$, $L=0.1\ \text{H}$.

$X_L=\omega L=100(0.1)=10\ \Omega \Rightarrow Z=10+j10,\ |Z|=14.142\ \Omega,\ \phi=45°$

$$I_m=\frac{100}{14.142}=7.071\ \text{A}\qquad\Longrightarrow\qquad i_{ss}(t)=7.071\sin(100t-45°)$$

$\tau=L/R=0.1/10=0.01\ \text{s}$, so the complete response has the form

$$i(t)=7.071\sin(100t-45°)+Ae^{-100t}$$

with $A$ fixed once $i(0^+)$ is known from the pre-switch condition.

## Related
- [[04 Capacitors, Inductors and First Order Circuits|Week 4 — DC first-order transients]] (the $\tau$-finding procedure is identical)
- [[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients (Series and Parallel RLC)]]
