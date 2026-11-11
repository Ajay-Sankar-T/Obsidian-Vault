---
tags: [fluid-mechanics, control-volume]
up: "[[Fluid Mechanics - MOC]]"
---

# System and Control Volume

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]

## System

A fixed, identified quantity of matter — you follow the *same* fluid particles wherever they go. $\boxed{\text{System}=\text{Lagrangian}}$. Physical laws (Newton's second law, conservation of mass, conservation of energy) are stated most fundamentally for a system.

## Control volume (CV)

A chosen region **in space** through which fluid can freely flow in and out; its boundary is the **control surface (CS)**. $\boxed{\text{CV}=\text{Eulerian}}$. Engineering analysis almost always prefers a control volume — fixed in the lab frame, easy to draw around a pump, nozzle, or pipe junction — over tracking a system, whose shape distorts unrecognizably as it flows.

## Why this distinction matters

Every conservation law in this vault ([[Conservation of Mass (Continuity Equation)|Conservation of Mass]], [[Linear Momentum Equation|Linear Momentum Equation]]) is a law about a **system**, but every equation actually solved in this vault is written for a **control volume**. The translation between the two is exactly the [[Reynolds Transport Theorem|Reynolds Transport Theorem]] — the single most important bookkeeping tool in this folder, playing the same "translate between two natural reference frames" role that the [[Material Derivative and Fluid Acceleration|material derivative]] plays one level down (for a single particle instead of an entire region).

## Related
- [[Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]
