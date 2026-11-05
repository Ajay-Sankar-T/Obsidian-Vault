---
tags: [concept, physics-lab, PH1030, thermal-radiation, stefan-boltzmann, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [Stefan's law, Stefan-Boltzmann law, radiation from a hot filament, thermopile, tungsten filament temperature]
---

# Lab - Stefan's Law (Hot Filament)

> [!abstract] The experiment in one line
> Heat a lamp filament with different currents, find its temperature from its *resistance*, measure the radiation with a thermopile, and show on a log–log plot that the radiated power rises as $T^4$ (slope 4).

## Aim and theory
**Aim:** verify Stefan's law. A black body radiates energy flux $L(T)=\sigma T^4$ with $\sigma=5.67\times10^{-8}$ W m⁻² K⁻⁴; a "grey" body (constant absorptivity below 1) obeys the same $T^4$ law, and a tungsten filament is a fair grey body.

The thermopile at fixed distance receives flux $\propto L(T)$ and its emf is proportional to that, but it also radiates at room temperature $T_R$:
$$V_{TC}\propto T^4-T_R^4\approx T^4\ \ \Longrightarrow\ \ \log V_{TC}=4\log T+\text{const}.$$

**Temperature from resistance.** Tungsten's resistance rises with temperature:
$$R(t)=R_0\big(1+\alpha t+\beta t^2\big),\quad\alpha=4.82\times10^{-3}\,\text{K}^{-1},\ \beta=6.67\times10^{-7}\,\text{K}^{-2},\quad T=t+273.$$
Find $R_0$ from a cold measurement, $R_0=\dfrac{R(t_R)}{1+\alpha t_R+\beta t_R^2}$, then invert for $t$ at each current: $t=\dfrac{-\alpha+\sqrt{\alpha^2-4\beta(1-R/R_0)}}{2\beta}$.

![[PL-stefan.png]]

**Figure:** Left, converting filament resistance to temperature (illustrative filament with $R_0=0.73\ \Omega$). Right, simulated thermopile readings on log–log axes: the straight line has slope $4.08\approx4$, confirming $V_{TC}\propto T^4$.

> [!question]- 🎯 Predict first: you raise the filament temperature from 1000 K to 1325 K. By what factor does the radiated flux grow?
> $(1325/1000)^4=3.08$: **three times** from a 33% temperature rise. Doubling $T$ would give $16\times$. That sensitivity is why the log–log slope (not the absolute values) is the clean test.

## Procedure (condensed)
1. **Cold resistance:** at about $0.1$ V steps measure $V$ and $I$ with the filament cold; $R(t_{\rm room})=V/I$ and so $R_0$. Keep currents tiny: heating would change $R_0$.
2. **Hot runs:** for filament voltages from $1$ V to about $15$ V in $0.2$ V steps record $V$, $I$ and the thermopile millivolts (set the multimeter on its 100 or 200 mV range).
3. Compute $R=V/I$, $T$ from the formula above, and $\log V_{TC}$, $\log T$.
4. Plot $\log V_{TC}$ against $\log T$; the slope should be $4$.

**Precautions:** handle the thermopile only with the rod, never by hand; never exceed $2.0$ A through the filament.

## Worked example
> [!example]- 🔬 One hot point (illustrative lamp)
> Cold: $R(27^\circ\text{C})=0.83\ \Omega$ gives $R_0=0.83/(1+0.130+0.0005)=0.734\ \Omega$.
> Hot: $V=6$ V and $I=1.2$ A, so $R=5.0\ \Omega$, $R/R_0=6.81$. Solving $\beta t^2+\alpha t-5.81=0$ gives $t=1052^\circ$C, $T=1325$ K.
> **Check:** $T$ in the range $1000$–$2200$ K for $1$–$15$ V is typical for a tungsten lamp (melting point $3695$ K).

> [!warning]- ⚠️ Using Celsius in the fit
> $\log V$ vs $\log T$ needs **kelvin**. In Celsius the slope is meaningless.

> [!danger]- 💥 Neglecting $T_R^4$ at low temperatures
> At the lowest filament temperatures ($\sim500$ K) $T_R^4=(300)^4$ is already $13\%$ of $T^4$, so the low-$T$ points bend away from slope 4. Fit only the higher-temperature region, or subtract $T_R^4$.

## Questions
> [!question]- Why does the log–log slope of 4 test the law better than a single value?
> It does not require knowing the geometry, the thermopile sensitivity or the emissivity: any constant factor only shifts the line, not its slope.

> [!question]- Why a grey body, not a black body?
> The filament absorbs less than 100%, but if the absorptivity is independent of wavelength the emitted spectrum keeps the $T^4$ total, so the law's *form* survives.

## Connections
- **Cross-domain:** [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] (cooling approaches ambient exponentially, radiation $\propto T^4$ makes it nonlinear), [[Heat Transfer - MOC]] (radiation is one of the three modes), [[Foundations of Thermal Engineering - MOC]].
- **Errors:** [[Error Analysis - Uncertainty and Propagation]] (a $1\%$ error in $T$ is a $4\%$ error in flux).

## Self-check
- [ ] I can convert $R$ to $T$ for tungsten and say why $R_0$ is measured cold.
- [ ] I can explain the log–log slope of 4 and the role of $T_R$.
- [ ] I can state the precautions for the thermopile and filament.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]
