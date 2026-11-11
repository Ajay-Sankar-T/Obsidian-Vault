---
tags:
  - EE1100
  - RLC
  - graphs
up: "[[EE1100 MOC]]"
---

# RLC Circuits — Responses (Series/Parallel, DC/AC/Step)

← up: [[EE1100 MOC|MOC]]

This folder collects every flavor of RLC response the course touches — **series vs parallel**, **DC vs AC**, **step vs natural vs steady-state** — into one place, with plotted graphs (not just formulas) so the *shapes* of the responses can be compared directly, not just their equations. It draws together material otherwise spread across [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]], [[AC Transients|AC Transients]], and [[08 Resonance and Magnetically Coupled Circuits|Week 8]].

## The four axes of variation

Every RLC response in this course sits somewhere on **two independent axes**:

```text
                    SERIES  ◄──────────────►  PARALLEL
                 (R,L,C share current)    (R,L,C share voltage)

    DC/step  ┌─────────────────────┬─────────────────────┐
    (natural │  Series RLC step    │  Parallel RLC        │
    response)│  response           │  natural response     │
             ├─────────────────────┼─────────────────────┤
    AC       │  Series RLC AC      │  Parallel RLC AC      │
    (forced +│  transient + steady │  transient + steady   │
    natural) │  state              │  state                 │
             └─────────────────────┴─────────────────────┘
```

Once you know **which cell of this grid** a problem is in, the solution method is fixed — see [[Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]] for how to tell them apart, and [[DC Step Response of RLC Circuits|DC Step Response]] / [[AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response]] for the two "rows."

## Notes in this folder

- [[Series RLC Natural Response - Damping Cases|Series RLC Natural Response — Damping Cases]] (with graphs)
- [[Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response — Damping Cases]] (with graphs)
- [[Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]] (side-by-side graph)
- [[DC Step Response of RLC Circuits|DC Step Response of RLC Circuits]]
- [[AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response of RLC Circuits]] (with graph)
- [[Frequency Response and Resonance Curves|Frequency Response and Resonance Curves]] (Bode-style magnitude/phase graphs)

## Related
- [[Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2 — DC transients]]
- [[AC Transients|AC Transients]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]]
- [[The Universal Second-Order Linear System|Cross-Domain: The Universal Second-Order Linear System]]
