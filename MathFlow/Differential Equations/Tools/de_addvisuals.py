"""Append a '## Visual' section to existing concept notes that had no figure (idempotent)."""
import os, io
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
NOTES = {
 "Intro/Isoclines.md": ("DE-E1-isoclines.png", "Dashed orange lines are isoclines (constant slope $c$); blue curves are the actual solutions. The three examples above: vertical isoclines for $y'=x$, radial isoclines for $y'=-x/y$ (solutions are circles, *not* the isoclines), parallel isoclines for $y'=x-y$ (all solutions approach $y=x-1$)."),
 "Intro/Exact Differential Equations.md": ("DE-E2-exact-level-curves.png", "The solution of an exact equation is a level curve $F(x,y)=C$ of the potential. The gradient $\\nabla F=(M,N)$ is perpendicular to every level curve, which is why $M\\,dx+N\\,dy=dF=0$ along a solution."),
 "Intro/Existence and Uniqueness (Picard-Lindelof Theorem).md": ("DE-E3-uniqueness.png", "Left: $y'=y$ satisfies the Lipschitz condition, one solution through each point. Right: $y'=y^{1/3}$ is only continuous at $y=0$; a solution can sit at $y=0$ for any time $c$ and then leave along $(2(x-c)/3)^{3/2}$, giving infinitely many solutions."),
 "Intro/Applications of First Order ODEs.md": ("DE-E4-applications.png", "Exponential growth, radioactive decay (with its half-life $\\ln2/\\lambda$), and Newton's cooling, where every temperature curve relaxes to the ambient $T_s$ with the same time constant $1/k$."),
 "Intro/Linear Differential Equations.md": ("DE-E5-linear-bernoulli.png", "Left panel: the solution family of $y'+2y=e^{-2x}$; the integrating factor $e^{2x}$ turns the equation into $(e^{2x}y)'=1$, so every solution decays. The other two panels show the Bernoulli examples from the next note."),
 "Intro/Bernoulli Differential Equations.md": ("DE-E5-linear-bernoulli.png", "Middle: $3y^2y'+y^3=e^{-x}$ ($v=y^3$ makes it linear). Right: $y'=y(xy^3-1)$ with $y=[x+\\frac{1}{3}+Ce^{3x}]^{-1/3}$; the nonlinear term lets solutions blow up at finite $x$, which a linear equation never does."),
 "2nd Order DE/Linear Independence and the Wronskian.md": ("DE-E6-wronskian.png", "Independent solutions have $W\\ne0$ everywhere; dependent ones have $W\\equiv0$. The right panel is the warning in the note: $x^3$ and $|x|^3$ have $W\\equiv0$ yet are independent, because they do not solve a common linear ODE with continuous coefficients."),
 "2nd Order DE/2nd Order Linear ODE with Constant Coefficients.md": ("DE-E7-constant-coefficients.png", "Roots of $r^2+ar+b=0$ in the complex plane and the resulting behaviour: distinct real roots (overdamped), a repeated root (critically damped), complex roots (underdamped oscillation inside an $e^{\\alpha x}$ envelope)."),
 "2nd Order DE/Undetermined Coefficients.md": ("DE-E8-resonance.png", "Left: when the forcing $\\cos x$ already solves the homogeneous equation, the trial form must be multiplied by $x$, and the particular solution $\\frac{1}{2}x\\sin x$ grows linearly (resonance). Right: for a nearby frequency no extra factor is needed and the response is bounded (beats)."),
 "2nd Order DE/Cauchy-Euler Equations.md": ("DE-E9-cauchy-euler.png", "The three root cases of $am(m-1)+bm+c=0$. Compare with the constant-coefficient case: powers of $x$ replace exponentials, and $\\ln x$ replaces $x$ (so complex roots oscillate in $\\ln x$)."),
 "Series Solutions of DE/Power Series Method.md": ("DE-S1-power-series.png", "For $y''-y=0$ the recurrence $a_{n+2}=a_n/((n+1)(n+2))$ splits into an even chain ($\\cosh x$) and an odd chain ($\\sinh x$). Partial sums approximate the exact solution on a window that grows with the number of terms; here $R=\\infty$."),
 "Series Solutions of DE/Radius of Convergence of Series Solutions.md": ("DE-S2-radius-of-convergence.png", "Left: the radius is the distance (in the complex plane) to the nearest singular point. Middle: a Legendre series ($p=\\frac{1}{2}$) is trustworthy only inside $|x|<1$. Right: Airy's equation has no singular point, and its series is good everywhere (more terms extend the window)."),
 "Series Solutions of DE/Ordinary and Singular Points.md": ("DE-S2-radius-of-convergence.png", "Singular points of Legendre's equation ($x=\\pm1$, red crosses) limit the series about an ordinary point to the disc reaching the nearest one: $R=1$ about $x_0=0$, $R=\\frac{1}{2}$ about $x_0=\\frac{1}{2}$."),
 "Series Solutions of DE/Airy's Equation.md": ("DE-S3-airy.png", "The Airy functions $\\mathrm{Ai},\\mathrm{Bi}$ oscillate for $x<0$ and grow/decay exponentially for $x>0$. Right: $\\mathrm{Ai}$ is the specific combination $\\mathrm{Ai}(0)y_1+\\mathrm{Ai}'(0)y_2$ of the two power series."),
 "Series Solutions of DE/Hermite's Equation.md": ("DE-S4-hermite.png", "When $n$ is a non-negative integer the series terminates and gives the Hermite polynomials $H_n$ (left). Multiplied by $e^{-x^2/2}$ they become the quantum-oscillator wave functions (right)."),
 "Series Solutions of DE/Legendre's Equation.md": ("DE-S5-legendre-equation.png", "Integer $p=n$: a polynomial solution $P_n$ (left) plus a second solution $Q_n$ that is log-singular at $\\pm1$ (middle). Non-integer $p$: neither series terminates (right). Continued in [[Legendre Polynomials and Rodrigues' Formula]]."),
 "Series Solutions of DE/Frobenius Theorem.md": ("DE-N1-frobenius-cases.png", "The three cases for the indicial roots and the shape of the corresponding solutions. Full derivation: [[Frobenius Method - Indicial Equation and Three Cases]]; examples: [[Frobenius Method - Worked Examples]]."),
}

def add(rel, img, cap):
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    s = io.open(p, encoding="utf-8", newline="").read()
    if img in s: return "skip (already has it): " + rel
    block = "\n## Visual\n\n![[%s]]\n**Figure:** %s\n" % (img, cap)
    nl = "\r\n" if "\r\n" in s else "\n"; block = block.replace("\n", nl)
    marker = nl + "---" + nl
    i = s.rfind(marker)
    if i != -1 and len(s) - i < 500: s = s[:i] + nl + block.rstrip(nl) + nl + s[i:]
    else: s = s.rstrip() + nl + block
    io.open(p, "w", encoding="utf-8", newline="").write(s); return "added: " + rel

if __name__ == "__main__":
    for rel, (img, cap) in NOTES.items(): print(add(rel, img, cap))
