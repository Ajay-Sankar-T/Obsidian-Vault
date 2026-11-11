---
tags: [EE1100, transformer, tutorial-solution, flux, saturation]
---

# T7-Q3 — Transformer on a Supply Other Than Rated

Hub: [[Tutorial 7 on Transformer]] · Previous: [[T7-Q2 - Exciting Current and Primary Current]] · Next: [[T7-Q4 - Referred Impedances and Short-Circuit Voltage]]

> [!question] A single-phase transformer is designed for 240/120 V, 50 Hz. Find the no-load secondary voltage and frequency when the HV side is connected to (a) 240 V, 40 Hz; (b) 120 V, 25 Hz; (c) 120 V, 50 Hz; (d) 480 V, 50 Hz; (e) 240 V dc. *[(a) 120 V, 40 Hz (b) 60 V, 25 Hz (c) 60 V, 50 Hz (d) overrated, 240 V, 50 Hz (e) may burn]*

**Tests:** $E=4.44fN\Phi_m$, flux $\propto V/f$, turns ratio, saturation.

## Given
Rated 240/120 V at 50 Hz: ratio 2:1, rated flux $\Phi_{rated}\propto240/50=4.8$.

## Principle and why it applies
The secondary voltage is the turns ratio times the primary voltage and has the supply **frequency**: $V_2=V_1/2$, $f_2=f_1$. But the core flux is $\Phi_m=\dfrac{V_1}{4.44fN_1}\propto\dfrac{V_1}{f}$: it must not exceed the rated flux or the core saturates (magnetising current rises sharply, the iron overheats, the waveform distorts).

## Solution

| Case | $V_1$, $f$ | $V_2$ (ideal) | $f_2$ | $V/f$ vs 4.8 | Verdict |
|---|---|---|---|---|---|
| (a) | 240 V, 40 Hz | 120 V | 40 Hz | 6.0 (**125 %**) | over-fluxed by 25 %: likely saturation, high exciting current |
| (b) | 120 V, 25 Hz | 60 V | 25 Hz | 4.8 (100 %) | normal flux, **safe**; lower voltage and frequency |
| (c) | 120 V, 50 Hz | 60 V | 50 Hz | 2.4 (50 %) | under-excited, safe, half voltage |
| (d) | 480 V, 50 Hz | (240 V) | 50 Hz | 9.6 (**200 %**) | **overrated**: deep saturation, winding insulation over-stressed |
| (e) | 240 V dc | 0 | none | | no changing flux, no induced emf: only $V/R$ limits the current, so the winding **burns** |

## Result
(a) 120 V, 40 Hz (but overflux). (b) 60 V, 25 Hz. (c) 60 V, 50 Hz. (d) nominally 240 V, 50 Hz but the transformer is overrated and saturates. (e) 0 V; transformer may burn.

## Check
Frequency never changes across an ideal transformer. In (e), a DC source gives $d\Phi/dt=0$, so $v_2=0$ and the primary current is $240/R_1$, tens or hundreds of times rated.

## Trap / alternative
Concluding that (a) is fine because the output is 120 V. The **flux** is what matters: lowering frequency at the same voltage raises $\Phi_m$ in proportion. This is why a transformer for 60 Hz can usually run at 50 Hz only at 5/6 of its voltage (the same $V/f$).

## Concepts used
- [[10 Single Phase Transformers]]
