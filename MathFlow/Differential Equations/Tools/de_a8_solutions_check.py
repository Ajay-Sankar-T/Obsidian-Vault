"""Assignment 8, Q5: substitute the general solutions into the original PDEs (arbitrary functions kept symbolic)."""
import sympy as sp
x, y = sp.symbols("x y", positive=True)
f, g = sp.Function("f"), sp.Function("g")


def L(U, A, B, C, D=0, E=0, F=0):
    return sp.simplify(A * sp.diff(U, x, 2) + B * sp.diff(U, x, y) + C * sp.diff(U, y, 2) + D * sp.diff(U, x) + E * sp.diff(U, y) + F * U)


checks = {
    "a": (f(x - y) + x * g(x - y), (1, 2, 1, 0, 0, 0), 0),
    "f": (f(y + sp.log(x)) + g(y * sp.exp(x)), (x * (x * y - 1), -(x**2 * y**2 - 1), y * (x * y - 1), x - 1, y - 1, 0), 0),
    "g": (f(y / x) + sp.log(x) * g(y / x), (x**2, 2 * x * y, y**2, x, y, 0), 0),
    "h": (x**2 * f(x**2 + y**2) + g(x**2 + y**2), (y**2, -2 * x * y, x**2, -y**2 / x, -x**2 / y, 0), 0),
    "i": (y**2 * sp.exp(2 * x) * (x + y) + f(x + y) + g(y * sp.exp(x)), (y - 1, -(y**2 - 1), y * (y - 1), 1, -1, 0), 2 * y * sp.exp(2 * x) * (1 - y)**3),
    "j": (f(y + sp.log(x)) + g(x * y), (x**2 * (y - 1), -x * (y**2 - 1), y * (y - 1), x * y, -1, 0), 0),
    "k": (-sp.Rational(1, 2) * (y + 2 * x)**2 * (4 * y - x)**3 + f(4 * y - x) + g(y + 2 * x), (4, -7, -2, 0, 0, 0), 243 * (2 * x + y) * (x - 4 * y)**2),
    "l": (sp.exp(2 * (2 * x + 3 * y)) * f(y - x) + g(2 * x + 3 * y), (3, 1, -2, -30, 20, 0), 0),
    "m": (8 * x**2 + x * f(y - 4 * x) + g(y - 4 * x), (1, 8, 16, 0, 0, 0), 16),
    "n": (f(3 * x + 4 * y) + sp.exp(-sp.Rational(9, 4) * x) * g(3 * x + 4 * y), (16, -24, 9, 36, -27, 0), 0),
    "o": (f(y - 3 * x) + g(3 * y - x), (3, 10, 3, 0, 0, 0), 0),
    "p": (f(y - 3 * x) + g(y - x), (1, 4, 3, 0, 0, 0), 0),
    "s": (x**4 / 3 - sp.Rational(2, 3) * (x - y) * x**3 + x * f(x - y) + g(x - y), (1, 2, 1, 0, 0, 0), 4 * x * y),
    "t": (f(x + 1 / y) + g(x - 1 / y), (1, 0, -y**4, 0, -2 * y**3, 0), 0),
    "u": (f(y + sp.Rational(2, 3) * x**sp.Rational(3, 2)) + g(y - sp.Rational(2, 3) * x**sp.Rational(3, 2)), (1, 0, -x, -1 / (2 * x), 0, 0), 0),
    "z": (f(y - sp.cos(x) - x) + g(y - sp.cos(x) + x), (1, -2 * sp.sin(x), -sp.cos(x)**2, 0, -sp.cos(x), 0), 0),
}
w = sp.Function("w")
if __name__ == "__main__":
    for k, (U, coeffs, rhs) in checks.items():
        r = sp.simplify(L(U, *coeffs) - rhs)
        print(f"Q5({k}): residual =", r)
    # elliptic (q), (r): harmonic in the new variables
    for name, (A, B, C, re, im) in {"q": (1, 1, 1, y - x / 2, sp.sqrt(3) * x / 2), "r": (1, 2, 17, y - x, 4 * x)}.items():
        F = sp.Function("F")
        # u = Re F(xi + i eta) is harmonic; test with F = exp  and F = z^3
        for FF in (sp.exp, lambda z: z**3):
            U = sp.re(sp.expand(FF(re + sp.I * im)))
            print(f"Q5({name}) test:", sp.simplify(A * sp.diff(U, x, 2) + B * sp.diff(U, x, y) + C * sp.diff(U, y, 2)))
