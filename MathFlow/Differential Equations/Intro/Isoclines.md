Related: [[First Order ODEs]], [[Particular Solution and IVP]]

▶ For a first-order ODE
$$\frac{dy}{dx} = f(x, y),$$
an **isocline** is a curve along which every solution curve has the same constant slope $c$.

▶ It is defined implicitly by
$$f(x, y) = c.$$

▶ Isoclines do not solve the ODE, but they are a graphical tool.

▶ By drawing several isoclines (for different values of $c$) and sketching short line segments of slope $c$ along each one, we build up the **direction field**, which allows us to sketch approximate solution curves without integrating the equation.

▶ This technique is usually introduced before Euler's method or separation of variables, since it builds geometric intuition for the shape of solutions.

## Example 1

For $\frac{dy}{dx} = x$, $f(x,y) = x$ depends only on $x$, so the isoclines are the **vertical lines** $x = c$. Along the line $x = c$, every solution has slope exactly $c$.

The general solution is $y = \frac{x^2}{2} + K$ (a family of parabolas).

## Example 2

For $\frac{dy}{dx} = -\frac{x}{y}$, setting $f(x,y) = -x/y = c$ gives $y = -\frac{x}{c}$, so the isoclines are **straight lines through the origin**.

Solving the ODE by separation of variables ($y\,dy = -x\,dx$) gives a family of concentric circles: $x^2 + y^2 = r^2$.

Notice that the isoclines (radial lines) are *not* the solution curves (circles) — a clear illustration that isoclines only mark constant slope, not the trajectories themselves.

## Example 3

For $\frac{dy}{dx} = x - y$, taking $f(x,y) = x - y = c$ gives $y = x - c$, so the isoclines are **parallel lines of slope 1**.

This is a linear ODE, $y' + y = x$ (see [[Linear Differential Equations]]), with general solution
$$y = x - 1 + Ke^{-x}.$$
As $x \to \infty$, all solution curves approach the line $y = x - 1$.


## Visual

![[DE-E1-isoclines.png]]
**Figure:** Dashed orange lines are isoclines (constant slope $c$); blue curves are the actual solutions. The three examples above: vertical isoclines for $y'=x$, radial isoclines for $y'=-x/y$ (solutions are circles, *not* the isoclines), parallel isoclines for $y'=x-y$ (all solutions approach $y=x-1$).

---
Next: [[Existence and Uniqueness (Picard-Lindelof Theorem)]]
