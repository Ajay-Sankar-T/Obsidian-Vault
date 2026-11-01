"""Assignment 8, second-order part (Q4-Q6): classification and canonical forms, derived and checked with sympy.
   For  A u_xx + B u_xy + C u_yy + D u_x + E u_y + F u = G  and new variables (xi, eta):
       A' = A xi_x^2 + B xi_x xi_y + C xi_y^2,  B' = 2A xi_x eta_x + B(xi_x eta_y + xi_y eta_x) + 2C xi_y eta_y,  C' = ... (eta)
       D' = A xi_xx + B xi_xy + C xi_yy + D xi_x + E xi_y, E' likewise with eta.
   The new equation is  A' u_xixi + B' u_xieta + C' u_etaeta + D' u_xi + E' u_eta + F u = G, then everything is
   written in (xi, eta) with the inverse map and divided by the leading coefficient.
   Run: python de_a8_second_order.py"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
X, Y = sp.symbols("xi eta", real=True)


def transform(A, B, C, D, E, F, G, xi, eta):
    xx, xy_, yy = sp.diff(xi, x), sp.diff(xi, y), None
    A1 = A * sp.diff(xi, x)**2 + B * sp.diff(xi, x) * sp.diff(xi, y) + C * sp.diff(xi, y)**2
    B1 = 2 * A * sp.diff(xi, x) * sp.diff(eta, x) + B * (sp.diff(xi, x) * sp.diff(eta, y) + sp.diff(xi, y) * sp.diff(eta, x)) + 2 * C * sp.diff(xi, y) * sp.diff(eta, y)
    C1 = A * sp.diff(eta, x)**2 + B * sp.diff(eta, x) * sp.diff(eta, y) + C * sp.diff(eta, y)**2
    D1 = A * sp.diff(xi, x, 2) + B * sp.diff(xi, x, y) + C * sp.diff(xi, y, 2) + D * sp.diff(xi, x) + E * sp.diff(xi, y)
    E1 = A * sp.diff(eta, x, 2) + B * sp.diff(eta, x, y) + C * sp.diff(eta, y, 2) + D * sp.diff(eta, x) + E * sp.diff(eta, y)
    return A1, B1, C1, D1, E1, F, G


def canonical(name, coeffs, xi, eta, inv, lead):
    """inv = (x(xi,eta), y(xi,eta)) or None; lead = which coefficient to normalise by: 'B' (hyperbolic), 'C' (parabolic u_etaeta), 'AC' (elliptic)"""
    A, B, C, D, E, F, G = coeffs
    t = transform(A, B, C, D, E, F, G, xi, eta)
    if inv is not None:
        sub = {x: inv[0], y: inv[1]}
        t = tuple(sp.simplify(sp.simplify(c).subs(sub)) for c in t)
    else:
        t = tuple(sp.simplify(c) for c in t)
    A1, B1, C1, D1, E1, F1, G1 = t
    div = {"B": B1, "C": C1, "A": A1}[lead]
    out = [sp.simplify(c / div) for c in (A1, B1, C1, D1, E1, F1, G1)]
    names = ["u_xixi", "u_xieta", "u_etaeta", "u_xi", "u_eta", "u", "RHS"]
    terms = [f"({o}) {n}" for o, n in zip(out[:6], names[:6]) if o != 0]
    print(f"({name}):  " + " + ".join(terms) + " = " + str(out[6]))
    return out


def disc(A, B, C):
    return sp.simplify(B**2 - 4 * A * C)


def main():
    xp, yp = sp.symbols("xp yp", positive=True)         # positive branches
    # ------------------------------------------------ Q4  discriminants
    print("== Q4  B^2 - 4AC")
    Q4 = {
        "a": (1, x - 1, 1), "b": (y, -x, y), "c": (x + 2, 2 * (x + y), 2 * (y - 1)), "d": (y**2, 0, -x**2), "e": (x**2, 2 * x * y, y**2),
        "f": (1, 0, x**2), "g": (1, 2, 5), "h": (1, 2 * x, 1 - y**2), "i": (y, 0, 1), "j": (1 + x**2, 0, 1 + y**2),
        "k": (sp.sin(x)**2, sp.sin(2 * x), sp.cos(x)**2), "l": (x, 0, y), "m": (1, y, x), "n": (y, 2, 1),
    }
    for k, (a, b, c) in Q4.items():
        print(f"Q4({k}): disc =", sp.factor(sp.simplify(disc(a, b, c))))
    # ------------------------------------------------ Q5
    print("== Q5 canonical forms")
    R = sp.Rational
    # (a)
    canonical("a", (1, 2, 1, 0, 0, 0, 0), x - y, x, (Y, Y - X), "C")
    # (b) y<0, s=sqrt(-y)
    s = sp.symbols("s", positive=True)
    canonical("b", (1, 0, y, 0, 0, 0, 0), x + 2 * sp.sqrt(-y), x - 2 * sp.sqrt(-y), ((X + Y) / 2, -((X - Y) / 4)**2), "B")
    # (c)
    canonical("c", (1, 0, -x**2, 0, 0, 0, 0), y + x**2 / 2, y - x**2 / 2, (sp.sqrt(X - Y), (X + Y) / 2), "B")
    # (d) x<0
    canonical("d", (1, 0, x, 0, 0, 0, 0), y + R(2, 3) * (-x)**R(3, 2), y - R(2, 3) * (-x)**R(3, 2), (-(3 * (X - Y) / 4)**R(2, 3), (X + Y) / 2), "B")
    # (e)
    canonical("e", (1, -2 * x * y, x**2 * y**2, 0, 0, 0, 0), y * sp.exp(x**2 / 2), x, (Y, X * sp.exp(-Y**2 / 2)), "C")
    # (f) xi = y + ln x (x>0), eta = y e^x: print coefficients in x, y
    A = x * (x * y - 1); B = -(x**2 * y**2 - 1); C = y * (x * y - 1)
    canonical("f", (A, B, C, x - 1, y - 1, 0, 0), y + sp.log(x), y * sp.exp(x), None, "B")
    # (g) Euler operator
    canonical("g", (x**2, 2 * x * y, y**2, x, y, 0, 0), y / x, sp.log(x), (sp.exp(Y), X * sp.exp(Y)), "C")
    # (h)
    canonical("h", (y**2, -2 * x * y, x**2, -y**2 / x, -x**2 / y, 0, 0), x**2 + y**2, x, (Y, sp.sqrt(X - Y**2)), "C")
    # (i) xi = x + y, eta = y e^x
    canonical("i", (y - 1, -(y**2 - 1), y * (y - 1), 1, -1, 0, 2 * y * sp.exp(2 * x) * (1 - y)**3), x + y, y * sp.exp(x), None, "B")
    # (j) xi = y + ln|x|, eta = xy
    canonical("j", (x**2 * (y - 1), -x * (y**2 - 1), y * (y - 1), x * y, -1, 0, 0), y + sp.log(x), x * y, None, "B")
    # (k)
    canonical("k", (4, -7, -2, 0, 0, 0, 243 * (2 * x + y) * (x - 4 * y)**2), 4 * y - x, y + 2 * x, ((4 * Y - X) / 9, (Y + 2 * X) / 9), "B")
    # (l)
    canonical("l", (3, 1, -2, -30, 20, 0, 0), y - x, 2 * x + 3 * y, ((Y - 3 * X) / 5, (Y + 2 * X) / 5), "B")
    # (m)
    canonical("m", (1, 8, 16, 0, 0, 0, 16), y - 4 * x, x, (Y, X + 4 * Y), "C")
    # (n)
    canonical("n", (16, -24, 9, 36, -27, 0, 0), 3 * x + 4 * y, x, (Y, (X - 3 * Y) / 4), "C")
    # (o)
    canonical("o", (3, 10, 3, 0, 0, 0, 0), y - 3 * x, 3 * y - x, ((Y - 3 * X) / 8, (3 * Y - X) / 8), "B")
    # (p)
    canonical("p", (1, 4, 3, 0, 0, 0, 0), y - 3 * x, y - x, ((Y - X) / 2, (3 * Y - X) / 2), "B")
    # (q)
    canonical("q", (1, 1, 1, 0, 0, 0, 0), y - x / 2, sp.sqrt(3) / 2 * x, (2 * Y / sp.sqrt(3), X + Y / sp.sqrt(3)), "A")
    # (r)
    canonical("r", (1, 2, 17, 0, 0, 0, 0), y - x, 4 * x, (Y / 4, X + Y / 4), "A")
    # (s)
    canonical("s", (1, 2, 1, 0, 0, 0, 4 * x * y), x - y, x, (Y, Y - X), "C")
    # (t) y != 0
    canonical("t", (1, 0, -y**4, 0, -2 * y**3, 0, 0), x + 1 / y, x - 1 / y, ((X + Y) / 2, 2 / (X - Y)), "B")
    # (u) x > 0
    canonical("u", (1, 0, -x, -1 / (2 * x), 0, 0, 0), y + R(2, 3) * x**R(3, 2), y - R(2, 3) * x**R(3, 2), ((3 * (X - Y) / 4)**R(2, 3), (X + Y) / 2), "B")
    # (v)
    canonical("v", (y**2, 0, 1, 0, 0, 0, 0), x, y**2 / 2, (X, sp.sqrt(2 * Y)), "A")
    # (w)
    canonical("w", (x**2, 0, y**2, 0, 0, 0, 0), sp.log(y), sp.log(x), (sp.exp(Y), sp.exp(X)), "A")
    # (x)
    canonical("x", (4 * y**2, 0, -sp.exp(2 * x), 0, 0, 0, 0), y**2 + sp.exp(x), y**2 - sp.exp(x), (sp.log((X - Y) / 2), sp.sqrt((X + Y) / 2)), "B")
    # (y)
    canonical("y", (y**2, 0, -x**2, 0, 0, 0, 0), y**2 + x**2, y**2 - x**2, (sp.sqrt((X - Y) / 2), sp.sqrt((X + Y) / 2)), "B")
    # (z)
    canonical("z", (1, -2 * sp.sin(x), -sp.cos(x)**2, 0, -sp.cos(x), 0, 0), y - sp.cos(x) - x, y - sp.cos(x) + x, ((Y - X) / 2, (X + Y) / 2 + sp.cos((Y - X) / 2)), "B")
    # ------------------------------------------------ Q6
    print("== Q6")
    # (h) Tricomi y>0: xi = x, eta = (2/3) y^{3/2};  y<0: xi = x + (2/3)(-y)^{3/2}, eta = x - (2/3)(-y)^{3/2}
    canonical("6h y>0", (y, 0, 1, 0, 0, 0, 0), x, R(2, 3) * y**R(3, 2), (X, (3 * Y / 2)**R(2, 3)), "A")
    canonical("6h y<0", (y, 0, 1, 0, 0, 0, 0), x + R(2, 3) * (-y)**R(3, 2), x - R(2, 3) * (-y)**R(3, 2), ((X + Y) / 2, -(3 * (X - Y) / 4)**R(2, 3)), "B")
    # (e) discriminant invariance, symbolic
    a, b, c = sp.symbols("a b c")
    xi_x, xi_y, et_x, et_y = sp.symbols("xi_x xi_y eta_x eta_y")
    A1 = a * xi_x**2 + b * xi_x * xi_y + c * xi_y**2
    B1 = 2 * a * xi_x * et_x + b * (xi_x * et_y + xi_y * et_x) + 2 * c * xi_y * et_y
    C1 = a * et_x**2 + b * et_x * et_y + c * et_y**2
    J = xi_x * et_y - xi_y * et_x
    print("6(e): B'^2-4A'C' - J^2 (b^2-4ac) =", sp.simplify(sp.expand(B1**2 - 4 * A1 * C1 - J**2 * (b**2 - 4 * a * c))))
    # (f) general solution check
    phi, psi = sp.Function("phi"), sp.Function("psi")
    U = phi(x + y) + x * psi(x + y)
    print("6(f): u_xx - 2u_xy + u_yy for u = phi(x+y) + x psi(x+y) :", sp.simplify(sp.diff(U, x, 2) - 2 * sp.diff(U, x, y) + sp.diff(U, y, 2)))
    # (g) u_xieta - 4u_xi + u_eta + 3u with u = v e^{lam xi + mu eta}
    xi_, eta_, lam, mu = sp.symbols("xi eta lambda mu")
    v = sp.Function("v")(xi_, eta_)
    U = v * sp.exp(lam * xi_ + mu * eta_)
    expr = sp.simplify((sp.diff(U, xi_, eta_) - 4 * sp.diff(U, xi_) + sp.diff(U, eta_) + 3 * U) * sp.exp(-lam * xi_ - mu * eta_))
    expr = sp.expand(expr)
    print("6(g): coeff of v_xi:", expr.coeff(sp.Derivative(v, xi_)), " v_eta:", expr.coeff(sp.Derivative(v, eta_)),
          " v:", sp.simplify(expr.subs({sp.Derivative(v, xi_): 0, sp.Derivative(v, eta_): 0, sp.Derivative(v, xi_, eta_): 0}) / v))
    print("   with lam=-1, mu=4: constant =", (lam * mu - 4 * lam + mu + 3).subs({lam: -1, mu: 4}))
    # (i)
    al, be = sp.symbols("alpha beta")
    v2 = sp.Function("v")(x, y)
    U = v2 * sp.exp(al * x + be * y)
    expr = sp.expand(sp.simplify((sp.diff(U, x, 2) + sp.diff(U, y, 2) + 2 * sp.diff(U, x) - 4 * sp.diff(U, y) + U) * sp.exp(-al * x - be * y)))
    print("6(i): v_x coeff:", expr.coeff(sp.Derivative(v2, x)), " v_y coeff:", expr.coeff(sp.Derivative(v2, y)))
    cc = (al**2 + be**2 + 2 * al - 4 * be + 1).subs({al: -1, be: 2})
    print("   alpha=-1, beta=2 -> c =", cc)


if __name__ == "__main__":
    main()
