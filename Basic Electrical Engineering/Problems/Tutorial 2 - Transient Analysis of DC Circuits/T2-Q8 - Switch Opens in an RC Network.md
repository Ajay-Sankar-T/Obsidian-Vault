---
tags: [EE1100, tutorial-solution, DC-circuits, transients, RC-circuit, switching]
tutorial: 2
up: "[[Tutorial 2 - Transient Analysis of DC Circuits]]"
---

# T2-Q8: Switch Opens in an RC Network (and Q9: Closes)

Hub: [[Tutorial 2 - Transient Analysis of DC Circuits]] · Theory: [[Theory - Transients in RL, RC and RLC Circuits]] · Previous: [[T2-Q7 - Discharging a Capacitor through a Coil]] · Next: [[T2-Q9 - Switch Closes in an RC Network]]

> [!question] The switch is opened at $t=0$ after having been closed for a long time. Determine the capacitor voltage $v_C$ and the output voltage $v_o$ at (a) $t=0^-$, (b) $t=0^+$, (c) $t=1.3$ ms. *[Sheet: $100,\ 38.4$ V; $100,\ 25.6$ V; $59.45$ V, $25.6$ V. The last $v_o$ is revised below.]*

**Tests:** [[Theory - Transients in RL, RC and RLC Circuits#3. First-order circuits (one storage element)|first-order switching recipe]]: $v_C$ continuous, $v_o$ *not*; $\tau$ from the equivalent resistance seen by $C$.

## Given
The 120 V source is in series with the switch in the **vertical branch** at the node between the $250\ \Omega$ and the $600\ \Omega$. Left of that node: $4\ \mu$F ($v_C$) in parallel with $1250\ \Omega$, then $250\ \Omega$. Right of the node: $600\ \Omega$, then $2\ \text{k}\Omega$ to ground, then $100\ \Omega$ and the $400\ \Omega$ across which $v_o$ is measured.

## Principle and why it applies
Three time instants test three ideas. At $0^-$ the circuit is in DC steady state (capacitor open). At $0^+$ the **capacitor voltage is unchanged** but everything else re-settles instantly to the new circuit. For $t>0$ the capacitor discharges through the resistance the *new* network presents to it, with time constant $\tau=R_{eq}C$.

## Diagram
![[T2-Q8-circuit.png]]

## Solution
**(a) $t=0^-$** (switch closed, $C$ open). The 120 V source holds the middle node at 120 V.
- Left: $v_C=120\cdot\dfrac{1250}{250+1250}=\mathbf{100\ V}$.
- Right: the $2\ \text{k}\Omega$ in parallel with ($100+400=500\ \Omega$) is $400\ \Omega$; $V_{R}=120\cdot\dfrac{400}{600+400}=48$ V; $v_o=48\cdot\dfrac{400}{500}=\mathbf{38.4\ V}$.

**(b) $t=0^+$.** $v_C(0^+)=100$ V. The switch has isolated the source, so the whole circuit is now one closed network: $C$ discharges through two parallel paths, the $1250\ \Omega$ and the chain $250+600+(2\ \text{k}\Omega\parallel500\ \Omega)=250+600+400=1250\ \Omega$. Current through the chain: $100/1250=0.08$ A. The $400\ \Omega$ (2 k∥500 Ω) node therefore sits at $0.08\times400=32$ V and
$$v_o(0^+)=32\times\frac{400}{500}=\mathbf{25.6\ V}.$$
(The output has jumped from 38.4 V to 25.6 V; it is *not* a storage variable.)

**(c) $t=1.3$ ms.** Both paths from the capacitor are $1250\ \Omega$ in parallel:
$$R_{eq}=1250\parallel1250=625\ \Omega,\qquad \tau=625\times4\times10^{-6}=2.5\ \text{ms}.$$
$$v_C(t)=100e^{-t/2.5\,\text{ms}}\ \Rightarrow\ v_C(1.3\ \text{ms})=100e^{-0.52}=\mathbf{59.45\ V}.$$
$v_o$ is a fixed fraction of $v_C$ here ($25.6/100$), so it decays with the **same** time constant:
$$v_o(1.3\ \text{ms})=25.6\,e^{-0.52}=\mathbf{15.2\ V}.$$

## Result
| | $v_C$ | $v_o$ |
|---|---|---|
| $0^-$ | 100 V | 38.4 V |
| $0^+$ | 100 V | 25.6 V |
| 1.3 ms | 59.45 V | **15.2 V** |

![[T2-Q8-Q9-response.png]]

> [!warning] The sheet's last entry
> The sheet lists $v_o(1.3\ \text{ms})=25.6$ V, the same as at $0^+$. That cannot be right: once the source is disconnected nothing holds $v_o$ constant, and it must decay with the circuit's single time constant. It looks like the Q9 pattern (where $v_o$ really is constant at 38.4 V) was copied across. The computed value is $15.2$ V (verified numerically in `Tools/ee_t1_t4_t8.py`).

## Check
Energy view: $v_C$ falls to 59.45 V when 35 % of the initial energy $\tfrac12(4\ \mu)(100)^2=20$ mJ remains ($\propto e^{-2\cdot0.52}=0.353$) ✓. KVL at $0^+$: the loop current through the chain (0.08 A) and through the $1250\ \Omega$ (0.08 A) both come from the capacitor, total $0.16$ A $=i_C(0^+)$ (the capacitor *current* jumps from $0$ to $0.16$ A).

## Trap / alternative
- Using $v_o(0^-)$ for $0^+$: only $v_C$ is continuous.
- Taking $R_{eq}$ as $1250\ \Omega$ only, or including the $250\ \Omega$ twice.
- Solving by Thevenin: seen by $C$ the network is two $1250\ \Omega$ in parallel, $625\ \Omega$ (no source), which is the same result in one line.

## Concepts used
- Continuity of $v_C$, time constant from the equivalent resistance, voltage dividers ([[Theory - Transients in RL, RC and RLC Circuits]], [[Voltage Divider Rule]])
