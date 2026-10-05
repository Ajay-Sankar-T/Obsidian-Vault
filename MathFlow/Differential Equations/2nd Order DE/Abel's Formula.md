Related: [[Linear Independence and the Wronskian]]

From the Wronskian test proof: for solutions $y_1,y_2$ of $y''+P(x)y'+Q(x)y=0$,
$$W' + PW = 0 \quad \text{(Abel's Formula)}$$
a first-order linear DE (see [[Linear Differential Equations]]) whose solution is
$$W(x) = Ce^{-\int P(x)\,dx}.$$

## Consequences

- Since $e^{-\int P(x)dx} \ne 0$ always, $W(x)$ and $W(x_0)$ have the same sign (or both zero) — **it suffices to check $W$ at a single point** $x_0 \in I$.
- If $W(x_0)\ne0$, then $y_1,y_2$ are independent throughout $I$.
- If $W(x_0)=0$, then $y_1,y_2$ are dependent throughout $I$.
- Abel's formula gives an explicit formula for $W$ *without solving the ODE fully*.
- Unlike arbitrary functions, for solutions of a linear ODE: $W\equiv0 \iff y_1,y_2$ are linearly dependent — a much stronger dichotomy than for general functions.

Integrating $W'+PW=0$ from $x_0$ to $x$:
$$W(x) = W(x_0)\,e^{\int_{x_0}^{x} P(t)\,dt}.$$

## Worked Examples

**Verify independence and find GS:** $y_1=e^{2x}, y_2=e^{-3x}$ solve $y''+y'-6y=0$ over $\mathbb{R}$.
- $y_1$: $(4+2-6)e^{2x}=0$ ✓; $y_2$: $(9-3-6)e^{-3x}=0$ ✓
- $W(y_1,y_2) = -3e^{-x}-2e^{-x} = -5e^{-x} \ne 0$ for all $x$ ⇒ independent.
- **GS:** $y = c_1e^{2x}+c_2e^{-3x}$.

**Repeated-root case:** Show $c_1e^{2x}+c_2xe^{2x}$ is the GS of $y''-4y'+4y=0$.
- $y_1=e^{2x}$ satisfies $(4-8+4)e^{2x}=0$. $y_2=xe^{2x}$: $y_2'=e^{2x}+2xe^{2x}$, $y_2''=4e^{2x}+4xe^{2x}$, satisfies the DE.
- $W(y_1,y_2) = e^{2x}(e^{2x}+2xe^{2x}) - xe^{2x}(2e^{2x}) = e^{4x} \ne 0$.
- **GS:** $y=c_1e^{2x}+c_2xe^{2x}$.

**Variable-coefficient case:** Show $c_1x+c_2x\ln x$ is the GS of $x^2y''-xy'+y=0$, $x>0$.
- $y_1=x$: $y_1'=1,y_1''=0 \Rightarrow 0-x+x=0$ ✓. $y_2=x\ln x$: $y_2'=\ln x+1$, $y_2''=1/x$; substituting gives $x-x(\ln x+1)+x\ln x=0$ ✓.
- $W(y_1,y_2) = x(\ln x+1)-x\ln x = x \ne 0$ for $x>0$.
- **GS:** $y=c_1x+c_2x\ln x$.

**Using Abel's formula directly:** If $xy''-(x+1)y'+y=0$ has $W(1)=e$, find $W(x)$.
- Standard form: $y''-\dfrac{x+1}{x}y'+\dfrac1x y=0 \Rightarrow P(x) = -\dfrac{x+1}{x}$.
- $W(x) = W(1)e^{-\int_1^x P(t)dt} = e\cdot e^{\int_1^x \frac{t+1}{t}dt}$.
- $\int_1^x \frac{t+1}{t}dt = (x+\ln x)-1$, so $W(x) = e\cdot e^{x-1+\ln x} = xe^x$.

---
Next: [[Existence, Uniqueness, and Fundamental Sets]]
