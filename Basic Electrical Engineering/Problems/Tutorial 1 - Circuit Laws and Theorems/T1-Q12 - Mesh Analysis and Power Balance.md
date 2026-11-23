---
tags: [EE1100, tutorial-solution, DC-circuits, mesh-analysis, supermesh, power-balance]
tutorial: 1
up: "[[Tutorial 1 - Circuit Laws and Theorems]]"
---

# T1-Q12: Mesh Analysis with a Supermesh, and Power Balance

Hub: [[Tutorial 1 - Circuit Laws and Theorems]] · Theory: [[Theory - Circuit Laws and Network Theorems]] · Previous: [[T1-Q11 - Supernodes]] · Next: [[T1-Q13 - Star-Delta Reduction]]

> [!question] Use mesh analysis to find all branch currents, compute the power delivered by each source and prove that total power supplied equals total power consumed. *[Sheet: $I_{ad}=4.5$ A, $I_{ba}=2.839$, $I_{be}=0.329$, $I_{de}=3.332$, $I_{cd}=1.168$, $I_{cb}=3.168$, $I_{ea}=1.661$, $I_{ec}=2$ A; powers $+185.363,+46.978,+14.193,-3.655,-3.503$ W; total 239.376 W]*

**Tests:** [[Theory - Circuit Laws and Network Theorems#6. Mesh analysis|mesh analysis with a supermesh]], [[Theory - Circuit Laws and Network Theorems#1. Variables and sign conventions|power balance]].

## Given
Nodes $a,b,c,d,e$ and corners $p,q,r,s$. Top row: $p$–$2\ \Omega$–$a$–$3\ \Omega$–$q$. Left: 4.5 A source from $p$ down to $d$. Right: 5 V battery between $q$ and $b$ ($+$ at $q$). Centre: 2.2 V battery between $a$ and $e$ ($+$ at $e$). Middle row: $d$–$9\ \Omega$–$e$–$4\ \Omega$–$b$. Lower: $d$–$3\ \Omega$–$r$ with the 3 V battery from $r$ to $c$ ($+$ at $r$); 2 A source from $e$ down to $c$; $b$–$6\ \Omega$–$s$–$1\ \Omega$–$c$. (Polarities are those that reproduce the printed branch currents.)

## Principle and why it applies
Four meshes, two current sources. The 4.5 A source lies on the **outer edge of mesh 1 only**, so it fixes that mesh current. The 2 A source is shared by meshes 3 and 4: its voltage is unknown, so merge them into a **supermesh** and use the constraint $I_3-I_4=2$.

## Diagram
![[T1-Q12-circuit.png]]

## Solution
Clockwise mesh currents: mesh 1 (top-left), 2 (top-right), 3 (bottom-left), 4 (bottom-right).

- Mesh 1: current source on its edge, the clockwise current runs *up* through it while the source drives *down*: $I_1=-4.5$ A.
- Constraint from the 2 A source (downwards through it): $I_3-I_4=2\ \Rightarrow\ I_4=I_3-2.$
- **Mesh 2** (shared $4\ \Omega$ with mesh 4): $\ -3I_2-5-4(I_2-I_4)-2.2=0\ \Rightarrow\ 7I_2-4I_4=-7.2.$
- **Supermesh 3+4** (outer loop, skipping the 2 A source): shared $9\ \Omega$ with mesh 1 and $4\ \Omega$ with mesh 2:
$$-9(I_3-I_1)-4(I_4-I_2)-6I_4-1\,I_4+3-3I_3=0\ \Rightarrow\ -12I_3-11I_4+4I_2=37.5.$$
Substituting $I_4=I_3-2$: $\ 7I_2-4I_3=-15.2$ and $-23I_3+4I_2=15.5$. Hence
$$I_2=-2.839\ \text{A},\quad I_3=-1.168\ \text{A},\quad I_4=-3.168\ \text{A}.$$

**Branch currents** (differences of mesh currents):
$I_{ba}=-I_2=2.839$; $\ I_{be}=I_2-I_4=0.329$; $\ I_{de}=I_3-I_1=3.332$; $\ I_{ea}=I_2-I_1=1.661$ (through the 2.2 V battery); $\ I_{dc}=-I_3=1.168$; $\ I_{cb}=-I_4=3.168$ (through the $6\ \Omega$ and $1\ \Omega$ in series); $\ I_{ad}=4.5$ and $I_{ec}=2$ A (given).

**Power balance** (delivered = voltage rise in the direction of the current × current):

| Source | Delivered |
|---|---|
| 4.5 A | $+185.363$ W |
| 2 A | $+46.978$ W |
| 5 V | $+14.193$ W |
| 2.2 V | $-3.655$ W (absorbs) |
| 3 V | $-3.503$ W (absorbs) |
| **total delivered** | **239.376 W** |

| Resistor | Absorbed |
|---|---|
| $2\ \Omega$ ($4.5^2\cdot2$) | 40.500 W |
| $3\ \Omega$ top ($2.839^2\cdot3$) | 24.180 W |
| $9\ \Omega$ ($3.332^2\cdot9$) | 99.920 W |
| $4\ \Omega$ ($0.329^2\cdot4$) | 0.433 W |
| $3\ \Omega$ left ($1.168^2\cdot3$) | 4.090 W |
| $6+1\ \Omega$ ($3.168^2\cdot7$) | 70.250 W |
| **total absorbed** | **239.37 W** |

## Result
$$\boxed{I_{ba}=2.839,\ I_{be}=0.329,\ I_{de}=3.332,\ I_{ea}=1.661,\ I_{dc}=1.168,\ I_{cb}=3.168\ \text{A};\quad P_{\text{supplied}}=P_{\text{consumed}}=239.38\ \text{W}}$$

## Check
KCL at $b$: $I_{cb}=3.168=I_{ba}+I_{be}=2.839+0.329$ ✓. At $a$: $I_{ba}+I_{ea}=4.5=I_{ad}$ ✓. The power balance closes to the third decimal (`Tools/ee_t1_t4_t8.py`).

## Trap / alternative
- The clockwise convention makes $I_1$ **negative** (the source points the other way round the loop); the printed $4.5$ A is the branch current.
- The two batteries 2.2 V and 3 V *absorb* power; that is physically a charging current, and the balance only works if you keep the signs.
- Nodal analysis would use four unknowns after merging $a$–$e$; mesh with a supermesh needs three. Both work; this question asks for mesh.

## Concepts used
- Mesh analysis, supermesh, Tellegen's theorem ([[Theory - Circuit Laws and Network Theorems]])
