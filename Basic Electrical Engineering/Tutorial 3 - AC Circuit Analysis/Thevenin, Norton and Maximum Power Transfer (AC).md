---
tags:
  - EE1100
  - AC-circuits
  - network-theorems
  - thevenin
  - maximum-power-transfer
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# Thevenin, Norton and Maximum Power Transfer (AC)

← up: [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[03 DC Network Theorems|Week 3]], [[Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]], [[07 AC Circuit Analysis and Network Theorems|Week 7]]

## Thevenin's theorem

Any linear two-terminal network reduces to a source $V_{\rm Th}$ in series with $Z_{\rm Th}$. For a load $Z_L$ attached to the terminals:

$$I_L=\frac{V_{\rm Th}}{Z_{\rm Th}+Z_L}$$

**Finding $V_{\rm Th}$:** remove the load; $V_{\rm Th}=V_{\rm OC}$, the open-circuit terminal voltage.

**Finding $Z_{\rm Th}$:** deactivate all independent sources (voltage source → short, current source → open — same as DC), then find the impedance looking into the terminals via series/parallel Z reduction ([[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]).

## Norton's theorem

Equivalent representation: current source $I_N$ in parallel with $Z_N$, where

$$I_N=I_{\rm SC}\ (\text{short-circuit current}),\qquad Z_N=Z_{\rm Th},\qquad V_{\rm Th}=I_NZ_N$$

Source transformation between the two forms works exactly as in DC.

## Maximum power transfer — DC baseline

For a purely resistive load: $R_L=R_{\rm Th}$ gives $P_{\max}=V_{\rm Th}^2/(4R_{\rm Th})$ — see [[Concepts#Network Theorems|Concepts — Network Theorems]] and [[Tutorial 1 - Circuit Laws and Theorems|Tutorial 1]].

## Maximum power transfer — AC (Q12, the critical formula)

If $Z_{\rm Th}=R_{\rm Th}+jX_{\rm Th}$ and the load impedance $Z_L$ can be **any** complex value, maximum average power occurs at the **complex-conjugate match**:

$$\boxed{Z_L=Z_{\rm Th}^{*}=R_{\rm Th}-jX_{\rm Th}}$$

i.e. $R_L=R_{\rm Th}$ and $X_L=-X_{\rm Th}$ — the load's reactance is chosen to exactly cancel the source's reactance, so the net loop reactance is zero and only the two resistances (equal) remain, which is precisely the DC-style matched-resistance condition applied to what's left after cancellation.

**Memory:** maximum AC power → load = conjugate of Thevenin impedance.

With the conjugate match in place, the reactive parts cancel and

$$P_{\max}=\frac{|V_{\rm Th}|^2}{4R_{\rm Th}}$$

— the same form as the DC result, now with $R_{\rm Th}$ specifically (not $|Z_{\rm Th}|$).

**Constrained case:** if the load is restricted to be purely resistive (no reactance available), the optimum instead becomes $R_L=|Z_{\rm Th}|$ — a weaker match than the full conjugate condition, noted already in [[07 AC Circuit Analysis and Network Theorems|Week 7]].

## Related
- [[Nodal and Mesh Analysis (AC)|Nodal and Mesh Analysis (AC)]] — the alternative full-circuit-equation route to the same answers
- [[Power Factor Correction|Power Factor Correction]] — a different (grid-side, not load-optimizing) use of choosing a reactance to cancel another
