---
tags: [EE1100, tutorial-solution, DC-circuits, thevenin, maximum-power]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q10: Maximum Power Transfer and the Half-Power Loads

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q9 - Norton Equivalent]] · Next: [[T1-Q11 - Supernodes]]

> [!question] (a) Power delivered to $R_L=3\ \Omega$. (b) The $R_L$ that receives maximum power, and that power. (c) The $R_L$ for which the power is $P_{max}/2$. The network: 20 V, $R_1=R_2=2\ \Omega$, 30 V, 40 V. *[Sheet: 42.18 W; $R_L=1\ \Omega$; $R_L=5.8\ \Omega$ and $0.172\ \Omega$]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#9. Maximum power transfer|maximum power transfer]], Thevenin reduction, solving a quadratic.

## Given
20 V source → $R_1=2\ \Omega$ → node M; from M a branch $R_2=2\ \Omega$ in series with a 30 V source to ground (positive at top); between M and terminal $a$ a 40 V source ($+$ at M); $R_L$ between $a$ and $b$ (the ground wire).

## Principle and why it applies
$R_L$ is the only variable element, so Thevenin-reduce everything else once and use $P_L=\dfrac{V_{th}^2R_L}{(R_L+R_{th})^2}$ for all three parts.

## Diagram
![[T1-Q10-circuit.png]]

## Solution
**Thevenin equivalent.** Node M is fed by two branches (20 V behind $2\ \Omega$, and 30 V behind $2\ \Omega$) with nothing else attached when $R_L$ is removed, so by Millman:
$$V_M=\frac{20/2+30/2}{1/2+1/2}=25\ \text{V}.$$
The 40 V battery opposes it, $V_{ab}=25-40=-15$ V: take $V_{th}=15$ V (polarity only reverses the current direction). With the sources off, $R_{th}=R_1\parallel R_2=1\ \Omega$.

**(a)** $R_L=3\ \Omega$: $\ I=\dfrac{15}{1+3}=3.75$ A, $\ P=I^2R_L=3.75^2\times3=\mathbf{42.19\ W}.$

**(b)** Maximum power at $R_L=R_{th}=\mathbf{1\ \Omega}$:
$$P_{\max}=\frac{V_{th}^2}{4R_{th}}=\frac{225}{4}=\mathbf{56.25\ W}.$$

**(c)** Require $\dfrac{V_{th}^2R_L}{(R_L+R_{th})^2}=\dfrac{V_{th}^2}{8R_{th}}$, i.e. $8R_LR_{th}=(R_L+R_{th})^2$:
$$R_L^2-6R_{th}R_L+R_{th}^2=0\ \Rightarrow\ R_L=(3\pm2\sqrt2)R_{th}=\mathbf{5.83\ \Omega}\ \text{or}\ \mathbf{0.172\ \Omega}.$$

## Result
$$\boxed{P(3\ \Omega)=42.19\ \text{W};\quad R_L=1\ \Omega,\ P_{max}=56.25\ \text{W};\quad R_L=5.83\ \Omega\ \text{or}\ 0.172\ \Omega}$$

![[T1-Q10-power-curve.png]]

**Figure:** the power curve is flat near its peak and falls off asymmetrically; the two half-power loads are *reciprocal* ($5.83\times0.172=1=R_{th}^2$), so on a log axis they sit symmetrically about $R_{th}$.

## Check
Both half-power loads give $P=28.1$ W: for $5.83\ \Omega$: $I=15/6.83=2.196$ A, $P=2.196^2\times5.83=28.1$ W ✓; for $0.172\ \Omega$: $I=12.8$ A, $P=28.1$ W ✓. Efficiency at matching is $R_L/(R_L+R_{th})=50\ \%$.

## Trap / alternative
- Part (c) has **two** answers; giving only one loses marks. The sheet's "$0.172$" is the second.
- Do not use $P_{\max}=V^2/(4R)$ with the *unreduced* source voltage: first reduce to $V_{th}$ (15 V, not 20 V, 30 V or 40 V).
- At maximum power the load takes the **same** power as is lost inside the source, so matching suits signals, not power transmission.

## Concepts used
- Thevenin reduction, maximum power transfer, Millman's theorem ([[Theory - Circuit Laws and Network Theorems]])
