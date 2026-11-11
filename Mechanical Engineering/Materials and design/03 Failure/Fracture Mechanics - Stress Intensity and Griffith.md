---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Fracture toughness, Stress intensity factor, Griffith criterion, K_Ic, Linear elastic fracture mechanics, LEFM, Brittle fracture]
---

# Fracture Mechanics — Stress Intensity and Griffith

> [!abstract] In one breath
> Strength calculations assume the material is flawless. **A crack changes the question**: the stress at its tip is huge, and what matters is the **stress intensity factor** $K_I=Y\sigma\sqrt{\pi a}$. The crack runs when $K_I$ reaches the material's **fracture toughness** $K_{Ic}$. Toughness, not strength, decides how large a flaw a part can carry.

Part of [[Materials and Design - MOC]]. Previous: [[Static Failure Theories - Tresca and von Mises]]. Next: [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]], [[Fatigue Crack Growth - Paris Law]].

## 1. Stress concentration at a crack

For an elliptical hole of semi-axes $a$ (across the load) and $b$ the peak stress is $\sigma_{max}=\sigma\big(1+2a/b\big)=\sigma\big(1+2\sqrt{a/\rho}\big)$ with tip radius $\rho=b^2/a$. As the notch becomes a crack, $\rho\to0$ and the elastic stress becomes unbounded. A stress is no longer a useful measure at the tip, so use the **stress intensity factor**:

$$
K_I=Y\,\sigma\sqrt{\pi a}\qquad[\text{MPa}\sqrt{\text{m}}]
$$

$\sigma$ is the remote stress, $a$ the crack length (half length for an internal crack, full length for an edge crack), and $Y$ a dimensionless geometry factor: $Y=1$ for a centre crack in an infinite plate, $Y\approx1.12$ for a small edge crack, $2/\pi=0.64$ for a buried penny-shaped crack; handbooks tabulate $Y$ for other geometries.

**Fracture criterion:** $K_I\ge K_{Ic}$ fails. Then the critical crack length and the fracture stress follow:

$$
a_c=\frac1\pi\Big(\frac{K_{Ic}}{Y\sigma}\Big)^2,\qquad \sigma_f=\frac{K_{Ic}}{Y\sqrt{\pi a}}
$$

Three modes exist (I: opening, II: in-plane shear, III: tearing). Mode I is the dangerous one and the one tabulated.

**Plane strain.** In a thick section the constraint raises the stress triaxiality and lowers toughness to the plane-strain value $K_{Ic}$; a valid $K_{Ic}$ test needs thickness $B\ge2.5\,(K_{Ic}/\sigma_y)^2$, so that the plastic zone at the tip is small enough for linear elasticity.

## 2. Griffith: why a crack runs

An elastic crack of length $2a$ in a plate: extending it releases elastic energy $\pi\sigma^2a^2/E$ per unit thickness and costs surface energy $4a\gamma_s$ (two faces of each length). The crack extends when the release exceeds the cost:

$$
\frac{d}{da}\Big(-\frac{\pi\sigma^2a^2}{E}+4a\gamma_s\Big)=0\ \Rightarrow\ \sigma_f=\sqrt{\frac{2E\gamma_s}{\pi a}}
$$

For a ductile metal the plastic work $\gamma_p\gg\gamma_s$ dominates: replace $\gamma_s$ by $\gamma_s+\gamma_p$. Comparing with $K_I=\sigma\sqrt{\pi a}$ gives the toughness $K_{Ic}=\sqrt{2E(\gamma_s+\gamma_p)}$ (Irwin), linking the energy view and the stress view: $G=K^2/E$ is the **energy release rate**.

**Glass.** $E=70$ GPa, $\gamma_s=1$ J/m², flaw $a=1\ \mu$m: $\sigma_f=\sqrt{2(70\times10^9)(1)/(\pi\times10^{-6})}=\mathbf{211\ MPa}$. Pristine glass fibres reach GPa because their flaws are nanometre-sized; ordinary glass breaks at tens of MPa because of scratches.

## 3. Typical toughness

| Material | $K_{Ic}$ (MPa√m) | Note |
| --- | --- | --- |
| Soda-lime glass | 0.7 | |
| Alumina | 4 | |
| Cast iron | 20–40 | |
| Al 7075-T6 | 24 | high strength, low toughness |
| Structural steel | 100+ | |
| 4340 steel (high-strength) | 50 | |
| Ti-6Al-4V | 55–110 | |

## 4. Worked example

An edge crack of 2 mm in a plate stressed to 300 MPa ($Y=1.12$): $K_I=1.12(300)\sqrt{\pi\times0.002}=\mathbf{26.6\ MPa\sqrt m}$.

| Material | $K_{Ic}$ | Verdict | $a_c$ at 300 MPa | $\sigma_f$ at $a=2$ mm |
| --- | --- | --- | --- | --- |
| Al 7075-T6 | 24 | **fractures** ($26.6>24$) | 1.6 mm | 270 MPa |
| 4340 steel | 50 | safe | 7.0 mm | 563 MPa |

The aluminium alloy has the higher specific strength but the **smaller tolerable flaw**: a 2 mm crack is already critical at 300 MPa. Toughness sets inspection intervals: a part is safe as long as non-destructive testing can find cracks smaller than $a_c$ with margin.

Plane-strain thickness: 4340 ($\sigma_y=1500$ MPa) needs $B\ge2.5(50/1500)^2=2.8$ mm; Al 7075 ($\sigma_y=500$) needs $5.8$ mm.

![[MAT-5-fracture.png]]

## 5. Design with toughness

- **Safe-life:** require $a_c$ much greater than the largest undetected flaw.
- **Fail-safe:** several load paths, so that one cracked member is detected before the next fails.
- Raise toughness by **grain refinement**, higher temperature (above the **ductile–brittle transition** of BCC steels), cleaner material (fewer inclusions) and tough alloys.
- **Fatigue** makes cracks grow below $K_{Ic}$: [[Fatigue Crack Growth - Paris Law]].

> [!warning] Traps
> - Using the full crack length for an internal crack: $a$ is the **half** length.
> - Comparing $K_I$ with the yield strength: $K$ is compared with $K_{Ic}$, units MPa√m.
> - Using $K_{Ic}$ for thin sheet (plane stress toughness is higher and thickness-dependent).
> - Assuming that the stronger alloy tolerates larger flaws: usually the opposite.
> - Ignoring that $Y$ changes with crack depth and geometry.

> [!question]- Predict first: halve the crack length. By what factor can the stress rise?
> $K\propto\sigma\sqrt a$, so at constant $K$ the stress rises by $\sqrt2=1.41$: halving the flaw size buys 41 % more stress.

> [!question]- Why are brittle ceramics so much stronger in compression than tension?
> A crack under compression closes and cannot propagate in mode I, so failure needs very high stresses. Under tension every flaw perpendicular to the load is a Griffith crack, so the weakest flaw decides the strength (and strength scatters with specimen size).

## 6. Connections

- [[Static Failure Theories - Tresca and von Mises]] — the strength-based theories assume no pre-existing crack; this is what they miss.
- [[Euler Buckling of Columns]] — a failure that depends on a geometric imperfection rather than material strength; compare [[Resonance and Buckling - Instability as an Eigenvalue Problem]].
- [[Strain Energy and Castigliano's Theorem]] — the energy release rate $G$ is a strain-energy derivative with respect to crack area.
- [[Energy Methods - A Unified View]] — Griffith is an energy balance: stored elastic energy against the energy to create new surface.
