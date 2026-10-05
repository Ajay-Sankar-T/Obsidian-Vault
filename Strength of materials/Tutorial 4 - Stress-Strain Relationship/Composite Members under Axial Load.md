---
tags: [strength-of-materials, stress-strain, composite-members]
up: "[[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship]]"
---

# Composite Members under Axial Load

← up: [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Strength of materials/02 Axial Loading/Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]]

## The setup (Q4)

A composite block — e.g. a brass core surrounded by aluminium plates — loaded axially through a **rigid** end plate.

```text
   P (total load)
       │
   ┌───▼───┐
   │ rigid │  ← end plate forces equal displacement
   └─┬───┬─┘
     │   │
  ┌──▼┐ ┌▼──┐
  │Al │ │Br │   both same length L
  └───┘ └───┘
```

## Compatibility

Because the end plate is rigid, both materials are forced to the **same displacement**, and since they share the same length:

$$\boxed{\delta_b=\delta_{Al}}\qquad\Longrightarrow\qquad\boxed{\varepsilon_b=\varepsilon_{Al}=\varepsilon}$$

But their stresses generally differ (different $E$): $\sigma_b=E_b\varepsilon$, $\sigma_{Al}=E_{Al}\varepsilon$.

## Equilibrium

$$\boxed{P=P_b+P_{Al}}=\sigma_bA_b+\sigma_{Al}A_{Al}=\varepsilon(E_bA_b+E_{Al}A_{Al})$$

Solving:

$$\boxed{\varepsilon=\frac{P}{E_bA_b+E_{Al}A_{Al}}}\qquad\Longrightarrow\qquad\sigma_b=E_b\varepsilon,\quad\sigma_{Al}=E_{Al}\varepsilon$$

## Composite-member shortcut

Since both materials share the same strain:

$$\boxed{\sigma_1:\sigma_2=E_1:E_2}$$

— the stiffer material always carries the proportionally larger stress; a direct generalization of [[Strength of materials/02 Axial Loading/Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]]'s "composite/parallel members sharing displacement" case, now with the sum $E_bA_b+E_{Al}A_{Al}$ playing the role of an **equivalent axial stiffness**, exactly as $k_{\rm eq}=k_1+k_2$ for springs in parallel.

## Cross-domain: this is impedance in parallel

Compare with [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]: two circuit elements forced to the **same voltage** (parallel connection) carry currents split by their individual admittances, $I_i=Y_iV$, with total current $I=V\sum Y_i$ — structurally identical to $P=\varepsilon\sum E_iA_i$ here, with strain $\varepsilon$ playing the role of the shared "potential" (voltage) and $E_iA_i$ playing the role of admittance $Y_i$. Both are instances of [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]]'s stiffness ↔ elastance pairing: equal-displacement (parallel spring) sharing is the mechanical mirror of equal-voltage (parallel admittance) sharing.

## Related
- [[Strength of materials/02 Axial Loading/Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]]
- [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Two Dissimilar Plates in a Rigid Opening|Two Dissimilar Plates in a Rigid Opening]] (the equal-*stress*, not equal-strain, counterpart)
- [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|Cross-Domain: The Mechanical-Electrical Analogy]]
