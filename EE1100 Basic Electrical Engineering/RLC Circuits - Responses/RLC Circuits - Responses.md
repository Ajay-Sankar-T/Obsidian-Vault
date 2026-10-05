---
tags: [EE1100, RLC, graphs]
up: "[[EE1100 Basic Electrical Engineering/EE1100 MOC]]"
---

# RLC Circuits — Responses (Series/Parallel, DC/AC/Step)

← up: [[EE1100 Basic Electrical Engineering/EE1100 MOC|MOC]]

This folder collects every flavor of RLC response the course touches — **series vs parallel**, **DC vs AC**, **step vs natural vs steady-state** — into one place, with plotted graphs (not just formulas) so the *shapes* of the responses can be compared directly, not just their equations. It draws together material otherwise spread across [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2]], [[EE1100 Basic Electrical Engineering/AC Transients/AC Transients|AC Transients]], and [[EE1100 Basic Electrical Engineering/08 Resonance and Magnetically Coupled Circuits|Week 8]].

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

Once you know **which cell of this grid** a problem is in, the solution method is fixed — see [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]] for how to tell them apart, and [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/DC Step Response of RLC Circuits|DC Step Response]] / [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response]] for the two "rows."

## Notes in this folder

- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/Series RLC Natural Response - Damping Cases|Series RLC Natural Response — Damping Cases]] (with graphs)
- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/Parallel RLC Natural Response - Damping Cases|Parallel RLC Natural Response — Damping Cases]] (with graphs)
- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/Series vs Parallel RLC - Key Distinctions|Series vs Parallel RLC — Key Distinctions]] (side-by-side graph)
- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/DC Step Response of RLC Circuits|DC Step Response of RLC Circuits]]
- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/AC Transient and Steady-State Response of RLC Circuits|AC Transient and Steady-State Response of RLC Circuits]] (with graph)
- [[EE1100 Basic Electrical Engineering/RLC Circuits - Responses/Frequency Response and Resonance Curves|Frequency Response and Resonance Curves]] (Bode-style magnitude/phase graphs)

## Related
- [[EE1100 Basic Electrical Engineering/Tutorial 2 - Transient Analysis of DC Circuits|Tutorial 2 — DC transients]]
- [[EE1100 Basic Electrical Engineering/AC Transients/AC Transients|AC Transients]]
- [[EE1100 Basic Electrical Engineering/08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]]
- [[Cross-Domain Synthesis/The Universal Second-Order Linear System|Cross-Domain: The Universal Second-Order Linear System]]
