---
tags: [EE1100, tutorial-solution, AC-circuits, complex-power, maximum-power, thevenin]
tutorial: 3
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# T3-Q12: Source Powers and AC Maximum Power Transfer

Hub: [[Tutorial 3 - AC Circuit Analysis]] · Theory: [[AC Power and Power Factor]], [[Thevenin, Norton and Maximum Power Transfer (AC)]] · Previous: [[T3-Q11 - Mesh, Nodal and Thevenin for Two Sources]] · Next tutorial: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]

> [!question] For the circuit of Fig. 5 (Q11): (a) real, reactive and apparent powers and power factors of source 1 and source 2; (b) the $Z_3=R_3+jX_3$ for maximum power in $Z_3$, the maximum power, and what each source contributes at that point. *[Sheet: $P_1=7.92$ W, $P_2=54.57$ W, $pf_1=0.5$ leading, $pf_2=0.9013$ lagging; $Z_3=1\ \Omega$, $P_{max}=46.65$ W, $P_1=P_2=23.32$ W. The sheet's $Q$ and $S$ entries are swapped between the sources; see below.]*

**Tests:** [[AC Power and Power Factor|complex power]] of a source, [[Thevenin, Norton and Maximum Power Transfer (AC)|conjugate matching]] $Z_L=Z_{th}^*$.

## Given
As in Q11: $\bar V_1=10\angle0^\circ$, $\bar V_2=10\angle-60^\circ$ V (rms), $Z_1=1+j1$, $Z_2=1-j1$, $Z_3=1+j2\ \Omega$. From Q11: $\bar V_a=10.80\angle-11.57^\circ$ V; $\bar I_1=1.585\angle60^\circ$ A is the current leaving source 1; the current leaving source 2 is $\bar I_{s2}=\dfrac{\bar V_2-\bar V_a}{Z_2}=6.055\angle-85.7^\circ$ A.

## Principle and why it applies
**(a)** The complex power *delivered by* a source is $\bar S=\bar V\bar I^*$ with $\bar I$ the current **leaving its $+$ terminal**. The sign of $Q$ then says what the source sees as a load: $Q<0$ means it is feeding a capacitive load (leading current).

**(b)** For a load $Z_L$ fed from a Thevenin source $\bar V_{th}$, $Z_{th}$, power is maximised when the load impedance is the **complex conjugate** of the source impedance, $Z_L=Z_{th}^*$: the reactances cancel and the resistances match. Then $P_{max}=\dfrac{|\bar V_{th}|^2}{4R_{th}}$.

## Diagram
![[T3-Q11-circuit.png]]

## Solution
**(a)**
$$\bar S_1=\bar V_1\bar I_1^*=10\angle0^\circ\times1.585\angle-60^\circ=15.85\angle-60^\circ=\mathbf{7.92-j13.73\ VA},$$
$$P_1=7.92\ \text{W},\quad Q_1=-13.73\ \text{VAr},\quad S_1=15.85\ \text{VA},\quad pf_1=\frac{7.92}{15.85}=0.5\ \text{leading}.$$
$$\bar S_2=\bar V_2\bar I_{s2}^*=10\angle-60^\circ\times6.055\angle+85.7^\circ=60.55\angle25.7^\circ=\mathbf{54.57+j26.23\ VA},$$
$$P_2=54.57\ \text{W},\quad Q_2=+26.23\ \text{VAr},\quad S_2=60.55\ \text{VA},\quad pf_2=\frac{54.57}{60.55}=0.901\ \text{lagging}.$$
The sheet pairs $Q_1=26$, $S_1=60.5$ with source 1 and $Q_2=-13.73$, $S_2=15.85$ with source 2: swapped (its $P$ and $pf$ entries are right: $pf_1=0.5=P_1/15.85$, impossible with $S_1=60.5$).

*Balance:* total supplied $P=7.92+54.57=62.50$ W $=I_1^2R_1+I_{s2}^2R_2+I_{Z_3}^2R_3=2.51+36.66+23.33$ ✓; $Q=-13.73+26.23=12.50$ VAr $=2.51-36.66+46.66$ ✓.

**(b)** From the Thevenin equivalent of Q11: $Z_{th}=1\ \Omega$, $|\bar V_{th}|=13.66$ V. So
$$Z_3=Z_{th}^*=\mathbf{1\ \Omega\ (\text{pure resistance, }R_3=1\ \Omega,\ X_3=0)},\qquad P_{max}=\frac{13.66^2}{4\times1}=\mathbf{46.65\ W}.$$
With $Z_3=1\ \Omega$ the node voltage becomes $\bar V_a=(\bar V_1Y_1+\bar V_2Y_2)/(Y_1+Y_2+1)$ and the source powers are
$$\bar S_1=37.5+j3.35\ \text{VA},\qquad \bar S_2=37.5-j3.35\ \text{VA}\ \ \Rightarrow\ \ P_1=P_2=\mathbf{37.5\ W}.$$
Total supplied $75$ W: $46.65$ W reaches $Z_3$ and $28.35$ W is lost in $R_1=R_2=1\ \Omega$ ($I_1^2+I_{s2}^2$).

## Result
$$\boxed{\text{(a) }\bar S_1=7.92-j13.73\ (0.5\ \text{lead}),\ \bar S_2=54.57+j26.23\ (0.901\ \text{lag});\quad\text{(b) }Z_3=1\ \Omega,\ P_{max}=46.65\ \text{W},\ P_1=P_2=37.5\ \text{W}}$$

![[T3-Q12-power-curve.png]]

**Figure:** the power in $Z_3$ for $X_3=0$ peaks at $R_3=|Z_{th}|=1\ \Omega$; this is the AC form of the DC rule $R_L=R_{th}$ (see [[T1-Q10 - Maximum Power Transfer and Half Power]]).

> [!warning] "23.32 W from each source"
> The sheet's $23.32$ W is exactly $P_{max}/2$: it is each source's *equal share of the power that reaches $Z_3$* by symmetry. The power each source actually **delivers** at the matched point is $37.5$ W, because the sources must also supply the $28.35$ W lost in $Z_1$ and $Z_2$.

## Check
$P_1+P_2-P_{loss}=75-28.35=46.65$ W $=P_{max}$ ✓. For $Z_3\neq Z_{th}^*$ (e.g. the original $1+j2$) the load receives $23.33$ W, half of the maximum, and $|I|^2R$ for the matched load is $|13.66/2|^2\times1=46.65$ ✓.

## Trap / alternative
- Matching in AC requires the **conjugate**, not equal impedance: choosing $Z_3=Z_{th}$ leaves the reactance uncancelled. Here $Z_{th}$ is real so the two coincide, but they will not in general.
- Superposition does **not** apply to power: you cannot find $P_2$ by treating the sources separately.
- The maximum is only 50 % efficient (28.35 W lost in the source impedances, 46.65 W delivered).

## Concepts used
- Complex power of a source, conjugate matching, Thevenin equivalent ([[AC Power and Power Factor]], [[Thevenin, Norton and Maximum Power Transfer (AC)]])
