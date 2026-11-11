---
tags: [fluid-mechanics, control-volume, momentum]
up: "[[Fluid Mechanics - MOC]]"
---

# Linear Momentum Equation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Reynolds Transport Theorem|Reynolds Transport Theorem]]

## From RTT to Newton's second law for a control volume

Momentum $\mathbf P=m\mathbf V$; Newton's second law for a system, $\sum\mathbf F=d\mathbf P/dt$. Setting $B=m\mathbf V,\ b=\mathbf V$ in [[Reynolds Transport Theorem|Reynolds Transport Theorem]], for a fixed inertial control volume:

$$\boxed{\sum\mathbf F=\frac{\partial}{\partial t}\int_{CV}\rho\mathbf V\,dV+\oint_{CS}\rho\mathbf V(\mathbf V\cdot\mathbf n)\,dA}$$

## Steady control-volume momentum

$$\boxed{\sum\mathbf F=\sum_{\rm out}\dot m\mathbf V-\sum_{\rm in}\dot m\mathbf V}$$

One inlet, one outlet: $\boxed{\sum\mathbf F=\dot m(\mathbf V_2-\mathbf V_1)}$.

Component form: $\sum F_x=\sum_{\rm out}\dot mV_x-\sum_{\rm in}\dot mV_x$, and analogously for $F_y,F_z$.

## Universal problem-solving procedure (jet / vane / nozzle / bend / force-on-pipe)

1. Draw the control volume.
2. Draw velocity vectors at every inlet/outlet.
3. Choose $x,y$ axes.
4. Compute $\dot m=\rho AV$ at each port (see [[Conservation of Mass (Continuity Equation)|Conservation of Mass]]).
5. Draw **all** external forces: pressure forces, weight, wall/support reactions, other applied forces.
6. Apply $\sum\mathbf F=\sum\dot m\mathbf V_{\rm out}-\sum\dot m\mathbf V_{\rm in}$.
7. Resolve into $x$ and $y$ components.
8. Solve for the unknown reaction.
9. Watch the wording: **force of fluid on device** is opposite to **force of device on fluid** (Newton's third law) — most exam mistakes are a sign flip here.

See [[Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications]] for the worked cases (flat plate, vane, nozzle, pipe bend).

## Related
- [[Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications — Jets, Vanes, Bends]]
- [[Reynolds Transport Theorem|Reynolds Transport Theorem]]
