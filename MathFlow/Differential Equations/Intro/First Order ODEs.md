Related: [[ODE (Ordinary Differential Equations)]]

▶ A first-order ordinary differential equation is an equation in which the highest derivative of the unknown function is the first derivative. It can be expressed in the general form
$$F(x, y, y') = 0,$$
where $x$ is the independent variable, $y = y(x)$ is the dependent variable, and $y' = \frac{dy}{dx}$.

▶ If the equation can be solved explicitly for the derivative, it takes the form
$$\frac{dy}{dx} = f(x, y),$$
which is known as the **explicit form** of a first-order ODE.

▶ When the derivative cannot be isolated explicitly, the equation is said to be in **implicit form**.

▶ The objective in solving a first-order ODE is to determine a function $y(x)$ that satisfies the differential equation on a given interval.

## Forms

- **Explicit form**: $\frac{dy}{dx} = 3x + 2y$.
- **Implicit form**: $x\left(\frac{dy}{dx}\right)^2 + 7y = 4$.
- **Differential form**: $M(x,y)\,dx + N(x,y)\,dy = 0$, where $M$ and $N$ are continuous functions. (See [[Exact Differential Equations]] and [[Integrating Factors]].)

## General solution

> A **general solution** of a first-order differential equation is a family of solutions containing one arbitrary constant.

**Example:** Consider $\frac{dy}{dx} = 2x$. Integrating both sides,
$$y = x^2 + C, \quad C \text{ is an arbitrary constant}$$
is the general solution. Each value of $C$ produces a different solution curve.

---
Next: [[Particular Solution and IVP]]
