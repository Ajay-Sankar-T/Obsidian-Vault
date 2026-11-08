---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Phase diagram, Lever rule, Eutectic, Eutectoid, Iron-carbon diagram, Fe-Fe3C, Pearlite, Ferrite, Austenite, Cementite, Ledeburite]
---

# Phase Diagrams — Lever Rule and the Iron–Carbide Diagram

> [!abstract] In one breath
> A binary **phase diagram** is a map of which phases are stable at a temperature and composition, in equilibrium. Two tools read it: the **tie line** (the compositions of the two phases that coexist) and the **lever rule** (how much of each). The most important diagram in engineering is **Fe–Fe₃C**: it explains steel.

Part of [[Materials and Design - MOC]]. Previous: [[Fatigue Crack Growth - Paris Law]]. Next: [[Heat Treatment of Steel - TTT and CCT Diagrams]].

## 1. Reading a diagram

- **Phase**: a region of uniform structure and composition.
- In a **single-phase** region, the phase has the **alloy** composition.
- In a **two-phase** region, draw the horizontal **tie line** at the temperature; its ends on the phase boundaries give the compositions $C_\alpha$ and $C_\beta$ of the two phases.
- **Lever rule:** for an alloy of composition $C_0$ the mass fractions are the opposite lever arms over the tie-line length:

$$
W_\alpha=\frac{C_\beta-C_0}{C_\beta-C_\alpha},\qquad W_\beta=\frac{C_0-C_\alpha}{C_\beta-C_\alpha}
$$

- **Gibbs phase rule** at constant pressure: $F=C-P+1$ (components, phases): in a two-phase region of a binary alloy $F=1$ (temperature fixes both compositions); at the eutectic three phases coexist, $F=0$ (invariant).

## 2. Invariant reactions

| Reaction | Form | Example |
| --- | --- | --- |
| **Eutectic** | liquid → α + β | Pb–Sn 61.9 wt% Sn, 183 °C; Fe–C 4.30 wt% C, 1147 °C |
| **Eutectoid** | γ → α + Fe₃C | Fe–C 0.76 wt% C, 727 °C (pearlite) |
| Peritectic | liquid + α → β | Fe–C near 1495 °C (δ) |
| Monotectic | L₁ → L₂ + α | Cu–Pb |
| Peritectoid | α + β → γ | |

## 3. A eutectic system: Pb–Sn

![[MAT-8-phases.png]]

Worked example: an alloy with 40 wt% Sn at 150 °C is in the α + β field. Tie-line ends: $C_\alpha=11$, $C_\beta=99$ wt% Sn.

$$
W_\alpha=\frac{99-40}{99-11}=\mathbf{0.67},\qquad W_\beta=0.33
$$

A hypoeutectic alloy (30 wt% Sn) cooled just below 183 °C: **primary α** $=\dfrac{61.9-30}{61.9-19.2}=0.747$ and the remaining $0.253$ is **eutectic** (a fine mixture of α and β lamellae; inside it the α share is $\frac{97.5-61.9}{97.5-19.2}=0.455$). The microstructure is coarse primary α grains in a fine eutectic matrix.

## 4. The iron–iron-carbide diagram

Key points (wt% C, °C):

| Point | Composition | Temperature |
| --- | --- | --- |
| eutectic | 4.30 | 1147 |
| max solubility in austenite | 2.14 | 1147 |
| eutectoid | **0.76** | **727** |
| max solubility in ferrite | 0.022 | 727 |
| cementite Fe₃C | 6.70 | |

**Phases.** Ferrite α (BCC, soft, ductile, dissolves very little carbon); austenite γ (FCC, nonmagnetic, dissolves up to 2.14 %); cementite Fe₃C (hard, brittle intermetallic, 6.70 wt% C); delta ferrite δ (BCC at high temperature).

**Microconstituents.** **Pearlite** = alternating lamellae of ferrite and cementite formed by the eutectoid reaction (fraction of cementite in pearlite $=\frac{0.76-0.022}{6.70-0.022}=0.11$). **Ledeburite** = eutectic of austenite and cementite (4.30 % C). **Proeutectoid** ferrite or cementite is whatever forms before the eutectoid reaction.

**Classification by carbon:**

| Material | wt% C | Slow-cooled structure |
| --- | --- | --- |
| Hypoeutectoid steel | < 0.76 | proeutectoid ferrite + pearlite |
| Eutectoid steel | 0.76 | 100 % pearlite |
| Hypereutectoid steel | 0.76–2.14 | proeutectoid cementite + pearlite |
| Cast iron | 2.14–6.7 | contains ledeburite (white iron) or graphite (grey iron) |

**Worked example, 0.40 wt% C just below 727 °C:**

$$
W_{\alpha,pro}=\frac{0.76-0.40}{0.76-0.022}=\mathbf{0.488},\quad W_{pearlite}=\frac{0.40-0.022}{0.76-0.022}=\mathbf{0.512}
$$

Total cementite (including inside the pearlite): $\dfrac{0.40-0.022}{6.70-0.022}=0.057$.

**1.0 wt% C (hypereutectoid):** proeutectoid cementite $=\dfrac{1.0-0.76}{6.70-0.76}=0.040$, pearlite $=0.960$.

**Strength follows the structure:** more carbon, more pearlite, more cementite: higher strength and hardness, lower ductility. A 0.2 % C steel is mostly ferrite (soft, formable, welds well); 0.8 % is all pearlite (strong, wear-resistant); above 2 % the cementite network makes it brittle.

## 5. Method

1. Locate $(C_0,T)$ on the diagram; name the phase field.
2. Single phase: the composition is $C_0$. Two phase: tie line, read $C_\alpha$, $C_\beta$.
3. Lever rule for the fractions.
4. Microstructure: follow the cooling path line down; note any crossing of invariant lines and which constituents form at each stage.

> [!warning] Traps
> - Reading the lever rule with the near arm: the **fraction of a phase is proportional to the far arm** (the segment on the *other* side of $C_0$).
> - Applying the diagram to fast cooling: it is **equilibrium**; use TTT/CCT diagrams for real cooling ([[Heat Treatment of Steel - TTT and CCT Diagrams]]).
> - Mixing wt% with atom %.
> - Calling pearlite a phase: it is a **microconstituent** made of two phases.
> - Using the Fe–Fe₃C diagram for graphitic cast irons (it describes the metastable carbide system).

> [!question]- Predict first: a 0.2 wt% C and a 0.6 wt% C steel are slowly cooled. Which has more pearlite?
> The 0.6 % steel: $W_{pearlite}=(0.6-0.022)/0.738=0.78$ against $(0.2-0.022)/0.738=0.24$. More carbon means more pearlite and so higher strength.

> [!question]- Why does the lever rule use composition differences, not temperature?
> It is a mass balance on the solute at fixed temperature: $C_0=W_\alpha C_\alpha+W_\beta C_\beta$ with $W_\alpha+W_\beta=1$. Solving gives the lever form: it is conservation of the component, the same bookkeeping as [[Conservation of Mass (Continuity Equation)]].

## 6. Connections

- [[Crystal Structures and Packing]] — ferrite is BCC and austenite FCC; the diagram's solubility limits follow from the interstitial sites in each cell.
- [[Heat Treatment of Steel - TTT and CCT Diagrams]] — what happens when equilibrium is not reached.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — diffusion-controlled transformation rates have an exponential temperature dependence (Arrhenius), the origin of the C-shaped curves.
- [[Conservation Laws and Flow Networks]] — the lever rule is a mass balance.
