---
tags: [EE1100, transformer, tutorial-solution, equivalent-circuit, efficiency]
---

# T7-Q6 — Equivalent Circuit Referred to the LT Side

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q5 - Secondary Voltage Under Load]] · Next: [[T7-Q7 - OC and SC Test Parameters]]

> [!question] The equivalent circuit referred to the low-tension side of a 2500/250 V transformer is shown in Fig. 1: shunt branch $R_c=500\ \Omega$ in parallel with $jX_m=j250\ \Omega$ at the input; series $0.2\ \Omega$ and $j0.7\ \Omega$; ideal transformer $N_1/N_2$ at the output. The load impedance referred to the HT terminals is $380+j230\ \Omega$. Find (a) the secondary terminal voltage, (b) the primary current and power factor, (c) the output power and efficiency. *[(a) 222 V (b) 5.1 A, 0.794 lag (c) 9500 W, 93.82 %]*

**Tests:** [[10 Single Phase Transformers|equivalent circuit]], referred load, power balance.

## Given
Input $V_1=2500$ V, i.e. $250$ V on the LT side; $a=10$; shunt $R_c=500\ \Omega\parallel jX_m=j250\ \Omega$; series $Z_s=0.2+j0.7\ \Omega$; load $380+j230$ on the HT side.

## Principle and why it applies
The circuit is drawn on the LT side, so refer the load there: $Z_L'=\dfrac{380+j230}{a^2}=3.8+j2.3\ \Omega$. The shunt branch sits at the input, so it carries a fixed current and does not affect the load voltage.

![[T7-Q6-circuit.png]]

## Solution
**(a)** Series current: $I=\dfrac{250}{Z_s+Z_L'}=\dfrac{250}{4.0+j3.0}=\dfrac{250}{5\angle36.87^\circ}=50\angle-36.87^\circ$ A.
$$V_2'=I\,Z_L'=50\times|3.8+j2.3|=50\times4.442=222.1\ \text{V on the LT side}$$
(so $\boxed{222\ \text{V}}$, the secondary terminal voltage on the 250 V side).

**(b)** Shunt branch current: $I_c=\dfrac{250}{500}=0.5$ A, $I_m=\dfrac{250}{j250}=-j1$ A. Total LT-side input current
$$I_{in}=50\angle-36.87^\circ+0.5-j1=(40+0.5)-j(30+1)=40.5-j31\ \text{A}$$
$|I_{in}|=51.0$ A on the LT side, i.e. **$5.10$ A on the HT side**; power factor $\dfrac{40.5}{51.0}=\boxed{0.794\ \text{lagging}}$.

**(c)** Output power: $P_{out}=I^2\,\mathrm{Re}(Z_L')=50^2\times3.8=\boxed{9500\ \text{W}}$. Input power: $P_{in}=V\,\mathrm{Re}(I_{in})=250\times40.5=10125$ W (series copper $50^2\times0.2=500$ W, core loss $250^2/500=125$ W: $9500+500+125=10125$ ✓).
$$\eta=\frac{9500}{10125}=93.83\ \%.$$

## Result
(a) $V_2=222$ V. (b) $I_1=5.10$ A at pf $0.794$ lagging. (c) $P_{out}=9500$ W, $\eta=93.8\ \%$.

## Check
Power balance holds to the watt (above). The poor efficiency is because this "transformer" has an unusually large series resistance ($0.2\ \Omega$ against a $3.8\ \Omega$ load) and a very low core resistance ($500\ \Omega$).

## Trap / alternative
- Referring the load the wrong way: dividing by $a^2$ is correct for moving an HT impedance to the LT side (multiply to go the other way).
- Putting the shunt branch **after** the series impedance (approximate circuit) would change the input current; here the circuit places it at the input terminals.

## Concepts used
- [[10 Single Phase Transformers]] · [[Gears, Transformers and Reflected Impedance]]
