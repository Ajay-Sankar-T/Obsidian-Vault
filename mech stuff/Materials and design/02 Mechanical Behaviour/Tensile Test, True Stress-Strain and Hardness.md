---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Tensile test, True stress, True strain, Considere criterion, Necking, Toughness, Resilience, Brinell hardness, Vickers hardness, Rockwell]
---

# Tensile Test, True Stress–Strain and Hardness

> [!abstract] In one breath
> A tensile test gives the **engineering stress–strain curve** ($\sigma=F/A_0$, $e=\Delta L/L_0$), from which the elastic modulus, yield strength, ultimate strength and ductility are read. Engineering stress **falls** after the peak only because the area shrinks in the neck: the **true stress keeps rising**. Necking starts where hardening can no longer keep up with the area loss (**Considère criterion**).

Part of [[Materials and Design - MOC]]. Previous: [[Dislocations, Slip and Strengthening]]. Next: [[Static Failure Theories - Tresca and von Mises]].

## 1. Reading the engineering curve

| Property | Definition |
| --- | --- |
| Young's modulus $E$ | initial slope $\sigma=Ee$ (a bond property: nearly the same for every steel) |
| Yield strength $S_y$ | start of plastic flow; 0.2 % offset if the curve has no sharp knee |
| Ultimate tensile strength $S_{ut}$ | maximum engineering stress |
| Ductility | % elongation $=\Delta L_f/L_0$; % reduction in area $=(A_0-A_f)/A_0$ |
| **Resilience** | elastic energy per volume $U_r=S_y^2/2E$ |
| **Toughness** | area under the whole curve (energy per volume to fracture) |

A **generalised Hooke's law** for the 3-D elastic range: $\varepsilon_x=\frac1E[\sigma_x-\nu(\sigma_y+\sigma_z)]$ and cyclic. Poisson's ratio $\nu\approx0.3$ for metals. For a bar in tension, the volume change $\Delta V/V=(1-2\nu)\sigma/E$ vanishes at $\nu=0.5$ (incompressible plastic flow).

## 2. True stress and true strain

With the instantaneous area $A$ and length $L$:

$$
\sigma_T=\frac FA,\qquad \varepsilon_T=\ln\frac L{L_0}
$$

Up to necking the volume is constant, $AL=A_0L_0$, so

$$
\sigma_T=\sigma_E(1+e),\qquad \varepsilon_T=\ln(1+e)
$$

Beyond necking these relations fail (the strain is concentrated in the neck): use the measured neck area. In the plastic range most metals follow the **power law**

$$
\sigma_T=K\varepsilon_T^{\,n}
$$

$n$ is the strain-hardening exponent (0.1–0.5: annealed copper 0.5, annealed low-carbon steel about 0.25, cold-worked steel 0.1).

## 3. Necking: Considère

The force is $F=\sigma_TA$. The neck starts when $F$ is a maximum, $dF=0$:

$$
d\sigma_T\,A+\sigma_T\,dA=0,\qquad \frac{dA}{A}=-d\varepsilon_T\ \Rightarrow\ \boxed{\frac{d\sigma_T}{d\varepsilon_T}=\sigma_T}
$$

Necking begins when the slope of the true curve equals the true stress itself. For the power law this means

$$
nK\varepsilon^{n-1}=K\varepsilon^n\ \Rightarrow\ \varepsilon_{neck}=n
$$

**Example.** $K=900$ MPa, $n=0.2$: necking at $\varepsilon_T=0.20$ (engineering strain $e=e^{0.2}-1=0.221$), true stress $900(0.2)^{0.2}=\mathbf{652\ MPa}$, so

$$
S_{ut}=\frac{\sigma_T}{1+e}=\frac{652}{1.221}=\mathbf{534\ MPa}
$$

![[MAT-3-tensile.png]]

On the left the dashed true curve keeps rising after the engineering curve peaks; on the right the Considère construction picks out the neck at $\varepsilon=n$.

## 4. Hardness

Hardness is resistance to indentation: quick, nearly non-destructive, and correlated with strength.

| Test | Indenter | Definition |
| --- | --- | --- |
| **Brinell** HB | 10 mm steel or carbide ball, 500–3000 kgf | $HB=\dfrac{2F}{\pi D\big(D-\sqrt{D^2-d^2}\big)}$ (load over curved area) |
| **Vickers** HV | 136° diamond pyramid | $HV=1.854\,F/d_{av}^2$ ($F$ in kgf, $d$ in mm) |
| **Rockwell** HR | cone or ball, depth under a major load | scale letter (HRC for hard steels) |

**Example.** Brinell with $F=3000$ kgf, $D=10$ mm and an indent of $d=4$ mm: $HB=2(3000)/[\pi(10)(10-9.165)]=\mathbf{229}$. For steels the tensile strength follows $S_{ut}\approx3.45\,HB$ MPa, here **790 MPa**. A Vickers test with 30 kgf and $d=0.45$ mm gives $HV=275$.

Hardness is one number for yield, work hardening and, in steel, microstructure: [[Heat Treatment of Steel - TTT and CCT Diagrams]].

> [!warning] Traps
> - Using $\sigma_T=\sigma_E(1+e)$ after necking.
> - Reading the UTS as the failure stress: fracture happens at a *lower* engineering stress (the neck).
> - Mixing percentage elongation with true strain: $e=0.22$ is 22 %; $\varepsilon_T=0.20$.
> - Using $HB\to S_{ut}$ for non-steels (the factor differs: roughly 3.4 for steels but 4 for some brass).
> - Taking toughness as the same thing as strength: a brittle high-strength steel has little toughness.

> [!question]- Predict first: a metal with $n=0.5$ (annealed copper) against one with $n=0.1$. Which necks later?
> $\varepsilon_{neck}=n$: the copper necks at a true strain of 0.5, the cold-worked steel at 0.1. A high $n$ means the metal can be stretched far in sheet forming without localising.

> [!question]- Why is the 0.2 % offset method used for yield?
> Many alloys have no sharp yield point. The offset line (parallel to the elastic slope, displaced 0.002 in strain) defines a repeatable stress where plastic strain is just measurable.

## 5. Connections

- [[Stress-Strain Diagram and Hooke's Law]] and [[Generalized Hooke's Law and Poisson's Ratio]] — the same curve in the elastic range and the 3-D law.
- [[Strain Energy and Castigliano's Theorem]] — resilience $S_y^2/2E$ is the elastic strain energy density.
- [[Dislocations, Slip and Strengthening]] — $n$ reflects dislocation multiplication.
- [[Lab - Tensile Test on the ES6 Tester]] — a tensile test in practice, the curve described here.
