---
tags: [EE1100, tutorial-solution, machines, induction-machine, rotor-circuit, torque]
tutorial: 8
up: "[[Tutorial 8 - Induction Machines]]"
---

# T8-Q8: Rotor Current, Power Factor and Torque at Start and at Full Load

Hub: [[Tutorial 8 - Induction Machines]] · Theory: [[Theory - Three-Phase Induction Machines]] · Previous: [[T8-Q7 - Relative Speeds of the Fields]] · Next: [[T8-Q9 - Power Flow and Efficiency of a Delta-Connected Motor]]

> [!question] A 3-phase, 4-pole, 1440 rpm, 50 Hz induction motor has a star-connected rotor winding with $0.2\ \Omega$ resistance and $1\ \Omega$ standstill leakage reactance per phase. At rated voltage and frequency the rotor induced emf at standstill is $120$ V per phase. (a) Find the rotor current, power factor and torque at starting and at full load, and compare. (b) With $1\ \Omega$ external resistance per phase inserted in the rotor circuit, find the rotor current, power factor and torque at starting. *[Sheet: (a) $117.67$ A, $0.196$ lag, $52.9$ N·m; $23.53$ A, $0.98$ lag, $52.87$ N·m; (b) $76.82$ A, $0.768$ lag, $135.25$ N·m]*

**Tests:** [[Theory - Three-Phase Induction Machines#2. Slip and rotor quantities|rotor quantities at slip $s$]], torque from rotor copper loss, effect of rotor resistance.

## Given
$R_2=0.2\ \Omega$, $X_{20}=1\ \Omega$ per phase, $E_{20}=120$ V per phase (star rotor), $n_s=1500$ rpm so $\omega_s=157.08$ rad/s, full-load slip $s=\dfrac{1500-1440}{1500}=0.04$.

## Principle and why it applies
At slip $s$ the rotor sees a voltage $sE_{20}$ at frequency $sf_1$, with reactance $sX_{20}$:
$$I_2=\frac{sE_{20}}{\sqrt{R_2^2+(sX_{20})^2}},\qquad\cos\phi_2=\frac{R_2}{\sqrt{R_2^2+(sX_{20})^2}}.$$
The torque follows from the power crossing the air gap, $P_g=3I_2^2R_2/s$: $\ T=P_g/\omega_s$.

## Diagram
![[T8-Q8-rotor-vs-slip.png]]

## Solution
**(a) Starting, $s=1$.** $Z_2=0.2+j1$, $|Z_2|=1.0198\ \Omega$:
$$I_2=\frac{120}{1.0198}=\mathbf{117.67\ A},\quad\cos\phi_2=\frac{0.2}{1.0198}=\mathbf{0.196\ lag},\quad T=\frac{3I_2^2R_2/1}{\omega_s}=\frac{3\times13\,846\times0.2}{157.08}=\mathbf{52.9\ N\cdot m}.$$
**Full load, $s=0.04$.** Rotor emf $sE_{20}=4.8$ V, reactance $sX_{20}=0.04\ \Omega$, $|Z|=\sqrt{0.2^2+0.04^2}=0.2040\ \Omega$:
$$I_2=\frac{4.8}{0.2040}=\mathbf{23.53\ A},\quad\cos\phi_2=\frac{0.2}{0.2040}=\mathbf{0.980\ lag},\quad T=\frac{3I_2^2R_2/s}{\omega_s}=\frac{3\times553.8\times0.2/0.04}{157.08}=\mathbf{52.87\ N\cdot m}.$$
**Comparison.** At starting the rotor current is $5\times$ the full-load value but its power factor is only $0.196$, so the **torque is the same** ($52.9$ N·m) as at full load: a large current at a very poor power factor gives no more torque than a small current at near-unity power factor. (This equality is a property of these numbers, not a general law; the figure shows torque rising to a maximum between the two.)

**(b) Starting with $1\ \Omega$ external resistance per phase.** Total rotor resistance $R=0.2+1=1.2\ \Omega$:
$$|Z_2|=\sqrt{1.2^2+1^2}=1.562\ \Omega,\quad I_2=\frac{120}{1.562}=\mathbf{76.82\ A},\quad\cos\phi_2=\frac{1.2}{1.562}=\mathbf{0.768\ lag},$$
$$T=\frac{3\times76.82^2\times1.2}{157.08}=\mathbf{135.25\ N\cdot m}.$$

## Result
| | $I_2$ (A) | $\cos\phi_2$ | $T$ (N·m) |
|---|---|---|---|
| start, no external resistance | 117.67 | 0.196 | 52.9 |
| full load ($s=0.04$) | 23.53 | 0.980 | 52.87 |
| start, $R_{ext}=1\ \Omega$ | 76.82 | 0.768 | **135.25** |

Adding rotor resistance **reduces the starting current by 35 % and raises the starting torque 2.6-fold**.

## Check
Torque as $\dfrac{3E\,I_2\cos\phi_2}{\omega_s}$ at start: $\dfrac{3\times120\times117.67\times0.196}{157.08}=52.9$ ✓. For (b): $\dfrac{3\times120\times76.82\times0.768}{157.08}=135.2$ ✓. At standstill the torque of this rotor circuit alone is greatest when the total rotor resistance equals the standstill reactance ($R=X_{20}=1\ \Omega$, i.e. $R_{ext}=0.8\ \Omega$), so the $1.2\ \Omega$ total of part (b) is close to the optimum.

## Trap / alternative
- The rotor **reactance** at slip $s$ is $sX_{20}$ (not $X_{20}$) and the **emf** is $sE_{20}$; forgetting the factor $s$ in either gives a wrong full-load current.
- External resistance is the *wound-rotor* method of getting torque at low starting current; a cage motor cannot do this.
- Torque uses $3I_2^2R_2/s$ (power at the air gap, including the load part $R_2(1-s)/s$), divided by $\omega_s$: don't divide by the rotor speed.

## Concepts used
- Rotor circuit at slip $s$, starting torque, rotor-resistance control ([[Induction Motor - Slip, Rotor Circuit and Power Flow]], [[Theory - Three-Phase Induction Machines]])
