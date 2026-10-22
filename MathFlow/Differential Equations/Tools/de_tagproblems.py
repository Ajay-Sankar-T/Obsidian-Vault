"""Tag the problem-set notes with the new concept notes (idempotent): extra frontmatter tags + a 'concept map' callout."""
import io, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Problems")

A4_MAP = """> [!info] Concept notes for this sheet
> Q1–Q2 (ordinary points): [[Power Series Method]] · [[Radius of Convergence of Series Solutions]] · [[Series Solutions About x0 not equal to 0]]. Q1(b) is [[Legendre's Equation]] → [[Legendre Polynomials and Rodrigues' Formula]].
> Q3 (Frobenius): [[Regular and Irregular Singular Points]] → [[Frobenius Method - Indicial Equation and Three Cases]] → [[Frobenius Method - Worked Examples]] (the same Bessel-type problems, solved in lecture).
>
> | Q3 part | Indicial roots | Case (see [[Frobenius Method - Indicial Equation and Three Cases]]) | Logarithm? |
> |---|---|---|---|
> | (a) $x=0$ / $x=1$ | $0,\\frac73$ / $0,-\\frac13$ | I | no |
> | (b) | $0,1$ | III (difference 1) | **yes** |
> | (c) | $\\frac14,\\frac34$ | I (Bessel of order $\\frac14$, [[Bessel's Equation and Bessel Functions of the First Kind]]) | no |
> | (d) | $-2,-3$ | III (difference 1) | no ($\\cosh x/x^3,\\ \\sinh x/x^3$; compare Bessel order $\\frac12$) |
> | (e) at $x=2$ | $\\frac{1\\pm i\\sqrt{11}}4$ | I (complex) | no |
> | (f) | $1,-\\frac12$ | I | no |
> | (g) at $x=0$ | $\\pm1$ | III (difference 2) | **yes** (like Bessel order 1, $Y_1$) |
> | (h) | $0,0$ | II | **yes** ($e^x\\ln x$) |
> | (i) | $0,-1$ | III (difference 1) | no |
"""

A5_MAP = """> [!info] Concept notes for this sheet
> | Questions | Concept note |
> |---|---|
> | toolkit §0.1–0.2, Q1, Q2 | [[Legendre Polynomials and Rodrigues' Formula]] (series solution, $P_n(1)=1$, Rodrigues, roots by Rolle) |
> | toolkit §0.3–0.4, Q1, Q8, Q9, Q10 | [[Generating Function of Legendre Polynomials]] |
> | toolkit §0.5, Q7 (orthogonality integrals) | [[Orthogonality and Norm of Legendre Polynomials]] · [[Inner Product Spaces and Orthogonal Functions]] |
> | toolkit §0.6, Q3, Q5, Q6 | [[Legendre Series and Fourier-Legendre Expansions]] |
> | Q4, Q7 (recurrence-based integrals), toolkit R1–R5 | [[Legendre Recurrence Relations and Integrals]] |
> | Q7(e), Q7(h) (Gamma / Beta functions) | [[Gamma Function]] |
> | Q11 (associated Legendre) | [[Legendre Polynomials and Rodrigues' Formula]] + [[Special Functions - MOC]] |
"""

def tag(fname, new_tags, concepts, block, before):
    p = os.path.join(ROOT, fname)
    s = io.open(p, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in s else "\n"
    if "Concept notes for this sheet" in s: return "skip " + fname
    # frontmatter tags
    i = s.index("tags:" + nl) + len("tags:" + nl); j = s.index("source:", i)
    existing = s[i:j]
    add = "".join("  - %s%s" % (t, nl) for t in new_tags if ("- " + t) not in existing)
    s = s[:j] + add + s[j:]
    # concepts property (before 'aliases:' or at end of frontmatter)
    prop = "concepts:" + nl + "".join('  - "[[%s]]"%s' % (c, nl) for c in concepts)
    k = s.index("aliases:")
    s = s[:k] + prop + s[k:]
    # callout
    m = s.index(before)
    s = s[:m] + block.replace("\n", nl) + nl + s[m:]
    io.open(p, "w", encoding="utf-8", newline="").write(s); return "tagged " + fname

if __name__ == "__main__":
    print(tag("Assignment 4 - Series Solutions - Solutions.md", ["frobenius-indicial-cases", "bessel-type-equations"],
              ["Frobenius Method - Indicial Equation and Three Cases", "Frobenius Method - Worked Examples", "Legendre Polynomials and Rodrigues' Formula"], A4_MAP, "> [!warning] Corrections and notes"))
    print(tag("Assignment 5 - Legendre Polynomials and Functions - Solutions.md", ["rodrigues", "generating-function", "orthogonality", "fourier-legendre", "recurrence-relations", "gamma-function"],
              ["Legendre Polynomials and Rodrigues' Formula", "Generating Function of Legendre Polynomials", "Orthogonality and Norm of Legendre Polynomials", "Legendre Series and Fourier-Legendre Expansions", "Legendre Recurrence Relations and Integrals", "Gamma Function"], A5_MAP, "> [!warning] Two statements in the sheet need correction"))
