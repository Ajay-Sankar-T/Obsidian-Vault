---
tags: [EE1100, diodes, tutorial-solution]
---

# A-Q1 — Formation of the p-n Junction

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Next: [[A-Q2 - Poisson Equation, Field and Potential]]

> [!question] Describe briefly how a p-n junction is formed.

## 1. Theory

**Doping.** Pure (intrinsic) silicon has equal electron and hole concentrations, $n=p=n_i\approx1.5\times10^{10}\ \text{cm}^{-3}$ at 300 K.
- **n-type:** doped with donors (P, As; concentration $N_d$): electrons are the majority carriers, $n\approx N_d$, $p\approx n_i^2/N_d$.
- **p-type:** doped with acceptors (B; concentration $N_a$): holes are the majority carriers, $p\approx N_a$, $n\approx n_i^2/N_a$.
Both materials are electrically neutral overall.

## 2. How the junction forms

1. A p-type and an n-type region are brought into contact (in practice, a single crystal doped differently on the two sides).
2. **Diffusion.** Holes are plentiful on the p side and scarce on the n side, so holes diffuse $p\to n$; electrons diffuse $n\to p$. This is a *diffusion current* (driven by the concentration gradient, not by a field).
3. **Uncovered ions.** Each carrier that leaves its side exposes a fixed, charged dopant ion: negative acceptor ions $N_a^-$ on the p side and positive donor ions $N_d^+$ on the n side. A **space-charge (depletion) region** forms, almost free of mobile carriers.
4. **Built-in field.** The two charge layers create an electric field $E$ pointing from n to p. It opposes further diffusion and causes a *drift current* in the opposite direction.
5. **Equilibrium.** Diffusion current $=$ drift current for each carrier type, so the net current is zero. The field corresponds to a potential step across the junction, the **built-in (contact) potential**

$$V_0=V_T\ln\frac{N_aN_d}{n_i^2}$$

and the depletion width is

$$W=x_p+x_n=\sqrt{\frac{2\varepsilon V_0}{q}\Big(\frac1{N_a}+\frac1{N_d}\Big)},\qquad N_ax_p=N_dx_n$$

(the depletion region extends further into the lightly doped side).

![[A1-junction-formation.png]]

## 3. Numbers (Si, 300 K, $N_a=10^{17}$, $N_d=10^{16}$ cm⁻³)

| Quantity | Value |
|---|---|
| $V_0=0.02586\ln\dfrac{10^{33}}{(1.5\times10^{10})^2}$ | 0.753 V |
| $W$ | 0.327 µm |
| $x_n$ (lightly doped n side) | 0.298 µm |
| $x_p$ | 0.030 µm |

> [!note] Key points to state
> - Diffusion creates the space-charge region; the space charge creates the field; the field causes drift opposing diffusion.
> - At equilibrium there is no net current and the Fermi level is constant across the junction.
> - The built-in potential **cannot** be measured with a voltmeter (it is cancelled by contact potentials at the metal terminals).
