---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RLC, underdamped, critical-damping]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q7: Discharging a Charged Capacitor through an RL Coil

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q6 - RC Circuit with a Two-Position Switch]] · Next: [[T2-Q8 - Switch Opens in an RC Network]]

> [!question] A 5 µF capacitor, initially charged to 10 V, is discharged suddenly through a coil of inductance 2 H and resistance 200 Ω. (a) Find the current $i(t)$. (b) The additional resistance needed for critical damping. *[Sheet: $i(t)=0.01601\,e^{-50t}\sin312.25t$ A, $R_{ext}=1064.9\ \Omega$]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#4. Second-order circuits (L and C together)|series RLC natural response]], damping classification, critical resistance.

## Given
$C=5\ \mu$F with $v_C(0)=10$ V, $L=2$ H, $R=200\ \Omega$, switch closes at $t=0$, $i(0)=0$. (The figure on the sheet shows 10 µF, 100 Ω and 1 H, but the **printed answers correspond to the text values**; see the last section.)

## Principle and why it applies
Source-free series RLC: $\;L\dfrac{d^2i}{dt^2}+R\dfrac{di}{dt}+\dfrac iC=0$. The type of response depends on $\alpha=R/2L$ against $\omega_0=1/\sqrt{LC}$. The initial conditions are $i(0)=0$ (inductor) and $L\,\dfrac{di}{dt}(0)=v_C(0)-Ri(0)=10$ V (KVL at $t=0^+$: the whole capacitor voltage appears across $L$).

## Solution
$$\alpha=\frac R{2L}=\frac{200}{4}=50\ \text{s}^{-1},\qquad \omega_0=\frac1{\sqrt{LC}}=\frac1{\sqrt{2\times5\times10^{-6}}}=316.2\ \text{rad/s},$$
$$R_c=2\sqrt{\frac LC}=2\sqrt{\frac{2}{5\times10^{-6}}}=1264.9\ \Omega\ \ >R=200\ \Omega\ \Rightarrow\ \text{underdamped}.$$
$$\omega_d=\sqrt{\omega_0^2-\alpha^2}=\sqrt{100\,000-2500}=312.25\ \text{rad/s}.$$
With $i=e^{-\alpha t}(A\cos\omega_dt+B\sin\omega_dt)$: $i(0)=0\Rightarrow A=0$; $\dfrac{di}{dt}(0)=B\omega_d=\dfrac{V_0}{L}=5\Rightarrow B=\dfrac{5}{312.25}=0.01601$:
$$\mathbf{i(t)=0.01601\,e^{-50t}\sin(312.25\,t)\ \text{A}}\qquad\Big(=\frac{V_0}{\omega_dL}e^{-\alpha t}\sin\omega_dt\Big).$$

**(b) Critical damping.** The total resistance must be $R_c=1264.9\ \Omega$, so the additional series resistance is
$$R_{ext}=R_c-R=1264.9-200=\mathbf{1064.9\ \Omega}.$$

## Result
$$\boxed{i(t)=0.01601\,e^{-50t}\sin312.25t\ \text{A},\qquad R_{ext}=1064.9\ \Omega}$$

![[T2-Q7-damping.png]]

**Figure:** left, the underdamped current inside its $\pm0.016e^{-50t}$ envelope (peak about 12.6 mA at about 4.5 ms); right, the same circuit with three resistances: critical damping (green) is the fastest return to zero without crossing it; larger $R$ is slower; smaller $R$ rings.

## Check
$\zeta=R/R_c=0.158<1$ ✓ underdamped. The first peak is where $\tan\omega_dt=\omega_d/\alpha$, $t_p=\dfrac1{\omega_d}\arctan\dfrac{\omega_d}{\alpha}=4.5$ ms and $i_p=0.01601\,e^{-0.226}\sin(1.412)\approx12.6$ mA. Energy: $\tfrac12CV_0^2=250\ \mu$J all ends up as heat in $R$.

## Trap / alternative
- *Text versus figure.* With the figure's values ($C=10\ \mu$F, $R=100\ \Omega$, $L=1$ H) the decay and ringing frequencies are **identical** ($\alpha=50$, $\omega_d=312.25$) but the amplitude doubles, $V_0/(\omega_dL)=0.03203$ A, and $R_c=632.5\ \Omega$ so $R_{ext}=532.5\ \Omega$. The sheet's printed answer is the **text** version, which is what is solved above.
- "Additional" resistance means $R_c-R$, not $R_c$.
- Don't forget the $1/\omega_d$ factor; writing $V_0/L$ as the amplitude is the critical-damping form, not the underdamped one.

## Concepts used
- Series RLC natural response, damping cases ([[Theory - Transients in RL, RC and RLC Circuits]], [[Series RLC Natural Response - Damping Cases]])
