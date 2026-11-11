---
title: Transformer Voltage Regulation and Efficiency
tags: [EE1100, concept, transformer, voltage-regulation, efficiency]
source: "[[Lecture 39 Transformer- Voltage Regulation and Efficiency.pdf]]"
---

Related: [[10 Single Phase Transformers]] (equivalent circuit, [[10 Single Phase Transformers#OC and SC tests|OC and SC tests]]) · [[EE1100 MOC]] · tested in [[Tutorial 7 on Transformer]] (Q8–Q10) · animation: [Parallel flux lines](transformer-current-flux-animation.html)

## What it is
Two numbers characterise the **performance** of a transformer: how much the secondary voltage sags under load (**voltage regulation**) and how much of the input power reaches the load (**efficiency**).

## Voltage regulation
With the primary voltage held constant, regulation is the change in secondary voltage when the full load is thrown off. $E_2$ is the no-load secondary voltage and $V_2$ the full-load terminal voltage:
$$\%VR=\frac{E_2-V_2}{V_{2,\text{rated}}}\times100\quad(\text{regulation up}),\qquad\%VR_{\text{down}}=\frac{E_2-V_2}{E_2}\times100.$$
Referred to the secondary, $E_2=V_2+I_2(r_{e2}+jx_{e2})$ with $r_{e2}=r_2+r_1'$, $x_{e2}=x_2+x_1'$. From the phasor diagram, for load power-factor angle $\phi_2$ ($+$ for lagging),
$$E_2-V_2\approx I_2r_{e2}\cos\phi_2\pm I_2x_{e2}\sin\phi_2\ \ \Longrightarrow\ \ \boxed{VR\approx r_{e2,pu}\cos\phi_2\pm x_{e2,pu}\sin\phi_2}$$
(sign $+$ for lagging, $-$ for leading).

**Zero regulation.** $VR=0$ when $\tan\phi_2=-r_{e2}/x_{e2}$, i.e. $\phi_2=-\tan^{-1}(r_{e2}/x_{e2})$: a **leading** current (capacitive load). A larger capacitive load gives negative regulation (the voltage rises). A normal inductive load gives positive regulation; a good transformer keeps it to a few percent.

*Approximation.* The formula neglects the quadrature part of the drop; it is accurate when the drop is small (it is the form used in the lecture and in the tutorial answers). The exact value comes from $V_1'^2=(V_2+I_2r_{e2}\cos\phi\pm I_2x_{e2}\sin\phi)^2+(I_2x_{e2}\cos\phi\mp I_2r_{e2}\sin\phi)^2$.

## Efficiency
$$\eta=\frac{P_{out}}{P_{in}}=\frac{V_2I_2\cos\phi_2}{V_2I_2\cos\phi_2+I_2^2r_{e2}+P_c}.$$
- **Copper (ohmic) loss** $I_2^2r_{e2}$: **variable**, grows as the square of the load.
- **Core loss** $P_c=P_h+P_e$ (hysteresis + eddy current): **fixed**, depends on the voltage and frequency, not on the load.

## Maximum efficiency
Differentiate $\eta$ with respect to $I_2$ (at fixed $V_2$, $\cos\phi_2$) and set it to zero:
$$\boxed{I_2^2r_{e2}=P_c}\qquad\text{(variable loss = fixed loss)},\qquad I_2=\sqrt{P_c/r_{e2}}$$
and $d^2\eta/dI_2^2<0$ confirms a maximum. Then
$$\eta_{max}=\frac{V_2I_2\cos\phi_2}{V_2I_2\cos\phi_2+2P_c}.$$
In terms of the load fraction $x=I_2/I_{2,rated}$: $x_{opt}=\sqrt{P_c/P_{cu,FL}}$ and the load at maximum efficiency is $x_{opt}\times$ kVA rating. Note $\eta_{max}$ depends on the power factor, but the *load* at which it occurs does not.

## Worked example (Lecture 39)
20 kVA, 2500/500 V, 50 Hz. HV: $r_1=2.5\ \Omega$, $x_1=10\ \Omega$; LV: $r_2=0.1\ \Omega$, $x_2=0.4\ \Omega$; core loss 200 W. Ratio $N_2/N_1=\frac15$.
- Referred to LV: $r_{e2}=0.1+\frac{2.5}{25}=0.2\ \Omega$, $x_{e2}=0.4+\frac{10}{25}=0.8\ \Omega$; $I_2=\frac{20000}{500}=40$ A.
- **(a)** 0.8 lagging: $E_2-V_2=40(0.2\cdot0.8+0.8\cdot0.6)=25.6$ V, $VR=\frac{25.6}{500}=5.12\ \%$. 0.8 leading: $E_2-V_2=40(0.2\cdot0.8-0.8\cdot0.6)=-12.8$ V, $VR=-2.56\ \%$ (the lecture rounds this to $-12$ V and $-2.4\ \%$).
- **(b)** Efficiency at 0.8 lagging: half load ($I_2=20$ A): $\frac{8000}{8000+20^2(0.2)+200}=96.6\ \%$; full load: $\frac{16000}{16000+320+200}=96.9\ \%$.
- **(c)** Maximum efficiency: $I_2=\sqrt{200/0.2}=31.6$ A $=79\ \%$ of full load; $\eta_{max}=\frac{500\cdot31.6\cdot0.8}{500\cdot31.6\cdot0.8+400}=96.9\ \%$.

**Per-unit method (Lecture 39, Tutorial Q10).** When voltages are not given, work with $V_2=1$ pu, $I_2=1$ pu. If $\eta_{max}=98\ \%$ at 0.8 load, 0.8 pf, 100 kVA: $P_{out}=64$ kW, $P_c=P_{cu}(0.8\text{ load})=653.06$ W, full-load copper loss $=653.06/0.64=1020$ W so $r_{e2}=0.0102$ pu. The lecture then takes $x_{e2}=0.05$ pu (the whole 5 % impedance), which gives $VR=3.82\ \%$. Splitting the impedance correctly, $x_{e2}=\sqrt{0.05^2-0.0102^2}=0.0489$ pu and $VR=0.0102(0.8)+0.0489(0.6)=3.75\ \%$, the sheet's answer (see [[T7-Q10 - Maximum Efficiency and Regulation]]).

![[T7-Q8-Q9-plots.png]]
**Figure:** the efficiency curve of Tutorial 7 Q9 (left): rising from light load, peaking where copper loss equals core loss, falling slowly after. Phasor diagram for lagging and leading loads (right).

> [!warning] Traps
> - Using the **wrong sign** for leading loads: $x_{e2}\sin\phi_2$ changes sign with the load angle.
> - Copper loss at **full load** versus at the **test current**: the short-circuit test may be run below rated current. Scale by $(I_{rated}/I_{test})^2$ ([[T7-Q9 - Efficiency and Regulation from Tests]]).
> - The load at maximum efficiency does **not** depend on $\cos\phi$, but the value of $\eta_{max}$ does.
> - Percent regulation can be quoted against $E_2$ or $V_{2,rated}$; the values differ slightly.

## Cross-domain links
- [[Gears, Transformers and Reflected Impedance]] — the same bookkeeping as for a gearbox: a fixed (no-load) loss plus a load-squared loss, so the best efficiency is at the load where they are equal.
- [[Thevenin, Norton and Maximum Power Transfer (AC)]] — "variable = fixed" is the same algebraic optimum as $R_L=R_{Th}$, but here it maximises a *ratio* (efficiency), not power, and sits at about 80 % of full load, not at the matched point.
