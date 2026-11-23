---
tags: [EE1100, tutorial-theory, DC-circuits, transients, RLC]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# Theory: Transients in RC, RL and RLC Circuits

← up: [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]] · lectures: [[Lecture 8 Transient Analysis of DC circuits.pdf]], [[Lecture 9 Transient Analysis of R-L Series Circuit.pdf]], [[Lecture 10 R-C and RLC Series Circuit.pdf]], [[Lecture 11 Step Response to RLC Series Circuit.pdf]], [[Lecture 12 An Example on Step Response to RLC Series Circuit.pdf]], [[Lecture 13 Transient Response_Some Examples.pdf]] · week: [[04 Capacitors, Inductors and First Order Circuits]] · deeper treatment of the second-order cases: [[RLC Circuits - Responses]], [[Series RLC Natural Response - Damping Cases]], [[Parallel RLC Natural Response - Damping Cases]], [[DC Step Response of RLC Circuits]]

> [!abstract] The idea in one paragraph
> Resistors respond instantly; **capacitors and inductors store energy and so remember**. A capacitor remembers its voltage ($\tfrac12Cv^2$), an inductor its current ($\tfrac12Li^2$), and neither can change instantly while the other quantities can jump. A **transient** is the circuit's passage from one stored-energy state to another after a switch operates. For one storage element the passage is an exponential with time constant $\tau$; for two it is an exponential, a critical form or a damped sinusoid depending on how much resistance there is.

## 1. The storage elements

| | Capacitor | Inductor |
|---|---|---|
| defining law | $i=C\dfrac{dv}{dt}$ | $v=L\dfrac{di}{dt}$ |
| integral form | $v(t)=v(0)+\dfrac1C\displaystyle\int_0^t i\,dt$ | $i(t)=i(0)+\dfrac1L\displaystyle\int_0^t v\,dt$ |
| stored energy | $\tfrac12Cv^2$ | $\tfrac12Li^2$ |
| **cannot jump** | voltage $v_C$ | current $i_L$ |
| DC steady state ($d/dt=0$) | open circuit ($i=0$) | short circuit ($v=0$) |
| a step of current/voltage | infinite $i$ would be needed for a jump in $v$ | infinite $v$ would be needed for a jump in $i$ |

*Why the continuity rules.* A jump in $v_C$ would need an infinite current ($i=C\,dv/dt$) and an infinite power; a jump in $i_L$ would need an infinite voltage. So for a finite source, $v_C(0^+)=v_C(0^-)$ and $i_L(0^+)=i_L(0^-)$. Every other current or voltage in the circuit (the capacitor current, the inductor voltage, a resistor voltage) **may jump** at the switching instant and is found afterwards from the circuit equations.

**Power and energy.** $p=vi$. When $p>0$ the element absorbs energy (stores it); when $p<0$ it returns it. The energy in the element is the area under $p(t)$ ($E=\int p\,dt=\tfrac12Cv^2$ or $\tfrac12Li^2$). This is the content of Q1: plot $v$, $i$ and $p$ for a given waveform and see that the area under $p$ is the stored energy.

## 2. DC steady state (Q2, Q3)

Long after any switching, all derivatives are zero: **replace each capacitor by an open circuit and each inductor by a short circuit**, solve the resistive circuit, then compute the stored energy $\tfrac12Cv_C^2+\tfrac12Li_L^2$. The capacitor voltage is whatever the resistive circuit puts across the open gap, the inductor current whatever flows through the short.

## 3. First-order circuits (one storage element)

Any circuit with one $L$ or $C$ and resistors is, as seen from the storage element, a **Thevenin source $V_{th}$ with resistance $R_{th}$** driving it (theory of [[Theory - Circuit Laws and Network Theorems]]). Then:

$$RC:\ \ R_{th}C\frac{dv_C}{dt}+v_C=V_{th},\qquad RL:\ \ \frac{L}{R_{th}}\frac{di_L}{dt}+i_L=\frac{V_{th}}{R_{th}}.$$

The solution of both is the **universal first-order formula**

$$\boxed{x(t)=x_\infty+\big[x(0^+)-x_\infty\big]\,e^{-t/\tau},\qquad \tau_{RC}=R_{th}C,\quad \tau_{RL}=\frac{L}{R_{th}}}$$

where $x$ is *any* voltage or current in the circuit (not only the storage variable), $x(0^+)$ its value just after switching and $x_\infty$ its final value. Five steps solve every switching problem:

1. **Before the switch ($t=0^-$):** DC steady state of the old circuit gives $v_C(0^-)$ or $i_L(0^-)$.
2. **Continuity:** $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$.
3. **After the switch, $t\to\infty$:** DC steady state of the new circuit gives $x_\infty$.
4. **Time constant:** $R_{th}$ seen by the storage element in the *new* circuit (independent sources off).
5. **Assemble** the formula; for another variable $x$, evaluate $x(0^+)$ from the new circuit with the storage element replaced by a source ($v_C(0^+)$ as a voltage source, $i_L(0^+)$ as a current source).

*Facts worth knowing.* After one $\tau$ the response has covered $63.2\ \%$ of the way to its final value; after $5\tau$ it is within $0.7\ \%$. For a source-free decay the energy is $\propto e^{-2t/\tau}$, so half of it is gone after $t_{1/2}=\tfrac{\tau}{2}\ln2=0.347\,\tau$ (Q4). The slope at $t=0$ is $-(x(0^+)-x_\infty)/\tau$, so the tangent at $0$ hits the final value at $t=\tau$.

## 4. Second-order circuits (L and C together)

**Series RLC** driven by a DC step $V$ (zero initial energy):
$$L\frac{d^2i}{dt^2}+R\frac{di}{dt}+\frac iC=0\quad(t>0),\qquad i(0)=0,\ \ \frac{di}{dt}(0)=\frac VL.$$
Characteristic roots $s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$ with
$$\alpha=\frac{R}{2L},\qquad \omega_0=\frac1{\sqrt{LC}},\qquad \zeta=\frac{\alpha}{\omega_0}=\frac R2\sqrt{\frac CL},\qquad R_c=2\sqrt{\frac LC},\qquad \omega_d=\sqrt{\omega_0^2-\alpha^2}.$$

| Case | Condition | Current response (zero initial state, step $V$) |
|---|---|---|
| **overdamped** | $R>R_c$, $\zeta>1$ | $i=\dfrac{V}{L(s_1-s_2)}\big(e^{s_1t}-e^{s_2t}\big)$, two real negative roots |
| **critically damped** | $R=R_c$, $\zeta=1$ | $i=\dfrac VL\,t\,e^{-\alpha t}$, fastest non-oscillatory settling |
| **underdamped** | $R<R_c$, $\zeta<1$ | $i=\dfrac{V}{\omega_dL}e^{-\alpha t}\sin\omega_dt$, a damped sinusoid |
| **undamped** | $R=0$ | $i=\dfrac{V}{\omega_0L}\sin\omega_0t$, undamped oscillation at $\omega_0$ |

The capacitor voltage in the underdamped case, from $v_C=V-L\,di/dt-Ri$ or by integrating,
$$v_C=V\Big[1-e^{-\alpha t}\Big(\cos\omega_dt+\frac{\alpha}{\omega_d}\sin\omega_dt\Big)\Big].$$
Its peak overshoot is $e^{-\pi\alpha/\omega_d}\times100\ \%$. The energy picture: the capacitor and inductor trade energy back and forth, the resistor drains a fraction each cycle ($Q=\omega_0L/R=1/2\zeta$ is the number of radians of oscillation per $e$-fold of energy loss).

**Parallel RLC** driven by a DC current step $I$ has the same mathematics with
$$\alpha=\frac{1}{2RC},\qquad \omega_0=\frac1{\sqrt{LC}},\qquad v=\frac{I}{C\omega_d}e^{-\alpha t}\sin\omega_dt\ \ (\text{underdamped, zero initial energy}),$$
and the *dual* role of $R$: damping *increases* as $R$ **decreases**.

**With non-zero initial conditions** (Q11) write the general solution of the *homogeneous* equation $e^{-\alpha t}(A\cos\omega_dt+B\sin\omega_dt)$ plus the particular (steady-state) solution, and fix $A$, $B$ from $i(0)$ and $\dfrac{di}{dt}(0)$, the latter from the circuit equation at $t=0^+$ using $v_C(0^+)$ and $i(0^+)$.

## 5. Reading a differential equation as a circuit (Q11)

The integro-differential equation $\;a\,\dfrac{di}{dt}+b\,i+c\displaystyle\int i\,dt=e\;$ is KVL for a **series** loop with $L=a$, $R=b$, $1/C=c$ and source $e$. The initial value of the integral term is the **initial capacitor voltage** $v_C(0)=c\int_{-\infty}^{0}i\,dt$. A non-zero steady state exists only if the source is *not* blocked by the capacitor, i.e. for a DC source, the series current $i_\infty$ is zero because the capacitor eventually charges to $e$.

## 6. Common traps
- Using the initial value of a **resistor** voltage or **capacitor** current from *before* the switch: those jump; only $v_C$ and $i_L$ are continuous.
- Computing $\tau$ with the *old* circuit's resistance, or leaving independent sources on when finding $R_{th}$.
- Forgetting that $R_{th}$ for an inductor is in the **denominator**: $\tau=L/R$ (a bigger resistance makes an RL circuit *faster*).
- Mixing up series vs parallel damping (series: $\alpha=R/2L$; parallel: $\alpha=1/2RC$).
- Missing the amplitude factor $1/(\omega_dL)$ (series, current) or $1/(\omega_dC)$ (parallel, voltage) in the underdamped step response.

## 7. Cross-domain links
- [[Conservation Laws and Flow Networks]]: the RC time constant is the same as a tank draining through a pipe, $\tau=R_{hyd}\,C_{tank}$.
- [[First-Order Systems - Time Constant and Response]]: the first-order formula of §3 is exactly the first-order system response.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] and [[2nd Order ODEs - MOC]]: the damping cases of §4 are the damping cases of a mass–spring–damper ($m\ddot x+c\dot x+kx=0$ with $L\leftrightarrow m$, $R\leftrightarrow c$, $1/C\leftrightarrow k$).
