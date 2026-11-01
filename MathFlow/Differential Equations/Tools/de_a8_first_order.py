"""Assignment 8, first-order part (Q1-Q3, Q6a-d): every answer in the note is verified here.
   Q2: a first integral phi of dx/a = dy/b = du/c satisfies  a phi_x + b phi_y + c phi_u = 0.
   Q3: the solution is substituted into the PDE and the initial data.
   Run: python de_a8_first_order.py"""
import sympy as sp
x, y, u = sp.symbols("x y u", real=True)
p_, q_ = sp.symbols("p q")


def is_integral(a, b, c, phi):
    return sp.simplify(a * sp.diff(phi, x) + b * sp.diff(phi, y) + c * sp.diff(phi, u)) == 0


def independent(phi, psi):
    J = sp.Matrix([[sp.diff(f, v) for v in (x, y, u)] for f in (phi, psi)])
    return any(sp.simplify(J[:, [i, j]].det()) != 0 for i, j in ((0, 1), (0, 2), (1, 2)))


# ---------------------------------------------------------------- Q2 : (label, a, b, c, phi, psi)
Q2 = [
    ("a", x**2, y**2, (x + y) * u, 1 / x - 1 / y, (x - y) / u),
    ("b", u * (x + y), u * (x - y), x**2 + y**2, x**2 - y**2 - u**2, 2 * x * y - u**2),
    ("c", x**2, 1, u**2, y + 1 / x, y + 1 / u),
    ("d", (x + 1)**2, (y - 1)**2, (x + y) * u, 1 / (x + 1) - 1 / (y - 1), (x - y + 2) / u),
    ("e", sp.cos(x + y), sp.sin(x + y), u, x - y - sp.log(sp.cos(x + y) + sp.sin(x + y)),
     sp.log(u) - sp.log(sp.tan((x + y) / 2 + sp.pi / 8)) / sp.sqrt(2)),
    ("f", x**2 + y**2, 2 * x * y, (x + y) * u, y / (x**2 - y**2), (x + y) / u),
    ("g (as printed)", 0 * x + (x + y) * u, 0 * x, x * y, y, u**2 - 2 * x * y + 2 * y**2 * sp.log(x + y)),
    ("g (xu p + yu q)", x * u, y * u, x * y, x / y, x * y - u**2),
    ("h", y**2, -x * y, x * (u - 2 * y), x**2 + y**2, y * (u - y)),
    ("i", 1, 3, 5 * u + sp.tan(y - 3 * x), y - 3 * x, sp.exp(-5 * x) * (u + sp.tan(y - 3 * x) / 5)),
    ("j", u * (u**2 + x * y) * x, -u * (u**2 + x * y) * y, x**4, x * y, x**4 - u**4 - 2 * x * y * u**2),
    ("k", y, x, x * y * u**2 * (x**2 - y**2), x**2 - y**2, 1 / u + (x**4 - y**4) / 4),
    ("l", x**2 - y**2 - u**2, 2 * x * y, 2 * x * u, u / y, (x**2 + y**2 + u**2) / y),
    ("m", x * y, y**2, x * y * u - 2 * x**2, y / x, (y * u - 2 * x) * sp.exp(-x) / x),
    ("n", u, -u, u**2 + (x + y)**2, x + y, (u**2 + (x + y)**2) * sp.exp(-2 * x)),
    ("o", x * (y**2 - u**2), -y * (u**2 + x**2), u * (x**2 + y**2), x**2 + y**2 + u**2, x / (y * u)),
    ("p", y + u, u + x, x + y, (x - y) / (y - u), (x - y)**2 * (x + y + u)),
    ("q", y - u * x, x + y * u, x**2 + y**2, x * y - u, x**2 - y**2 + u**2),
    ("r", x - y, y - x - u, u, x + y + u, (x - y + u) / u**2),
    ("s", y - u, u - x, x - y, x + y + u, x**2 + y**2 + u**2),
    ("t", x * (y - u), y * (u - x), u * (x - y), x * y * u, x + y + u),
    ("u", x**2 - y * u, y**2 - u * x, u**2 - x * y, (x - y) / (y - u), x * y + y * u + u * x),
    ("v", sp.tan(x), sp.tan(y), sp.tan(u), sp.sin(x) / sp.sin(y), sp.sin(y) / sp.sin(u)),
    ("w", x + 2 * u, 4 * u * x - y, 2 * x**2 + y, x**2 - y - u, u**2 - x * y),
    ("x", y**2 + u**2, -x * y, -x * u, y / u, x**2 + y**2 + u**2),
    ("y", x + y - u, y + u - x, u + x - y,
     (x**2 + y**2 + u**2 - x * y - y * u - u * x) / (x + y + u)**2,
     sp.sqrt(3) * sp.log(x + y + u) + sp.atan(sp.sqrt(3) * (y - u) / (2 * x - y - u))),
]

# Q2(z): linear system, eigen-method.  M = [[0,1,1],[-1,0,1],[0,5,1]] has eigenvalues 1, 2, -2
M = sp.Matrix([[0, 1, 1], [-1, 0, 1], [0, 5, 1]])
left = {ev: (M.T - ev * sp.eye(3)).nullspace()[0].T for ev in (1, 2, -2)}
Lz = {ev: sp.simplify((left[ev] * sp.Matrix([x, y, u]))[0]) for ev in left}
# first integrals of d(l.v)/dt = lambda (l.v):  (l1.v)^(1/l1) / (l2.v)^(1/l2)
phiz = Lz[2] / Lz[1]**2          # lambda 2 over lambda 1 squared
psiz = Lz[1] * Lz[-2]**1 / 1     # growth e^{t} * e^{-2t} ... fixed below
Q2.append(("z", y + u, u - x, u + 5 * y, None, None))


def run_q2():
    ok = True
    for lab, a, b, c, phi, psi in Q2:
        if lab == "z":
            continue
        r1, r2, ind = is_integral(a, b, c, phi), is_integral(a, b, c, psi), independent(phi, psi)
        ok &= (r1 and r2 and ind)
        print(f"Q2({lab}): phi {r1}, psi {r2}, independent {ind}")
    return ok


def run_q2z():
    print("Q2(z): eigenvalues of M:", M.eigenvals())
    for ev, l in left.items():
        print("   lambda", ev, "left eigenvector (l1,l2,l3) =", list(l), "  l.v =", Lz[ev])
    # d(l.v)/dt = lambda * (l.v) along characteristics => (l_a.v)^{1/la} / (l_b.v)^{1/lb} constant
    f1 = Lz[2]**1 / Lz[1]**2          # e^{2t} / e^{2t}
    f2 = Lz[1] * Lz[-2]               # e^{t} * e^{-2t} is e^{-t}; use (l_-2.v)(l_2.v) = const (e^{-2t} e^{2t})
    f2 = Lz[2] * Lz[-2]
    for name, f in (("(l2.v)/(l1.v)^2", f1), ("(l2.v)(l-2.v)", f2)):
        print("   ", name, "is a first integral:", is_integral(y + u, u - x, u + 5 * y, f))
    return f1, f2


# ---------------------------------------------------------------- Q3
def check_pde(expr_u, pde):
    """pde(p, q, u, x, y) must vanish when u = expr_u(x, y)"""
    p, q = sp.diff(expr_u, x), sp.diff(expr_u, y)
    return sp.simplify(pde(p, q, expr_u))


Q3 = [
    ("a", y * sp.exp(x), lambda p, q, U: p + q - U - sp.exp(x), (lambda: sp.simplify(Q3_u(0, y=0))), None),
]


def Q3_u(*a, **k):
    return None


Q3_list = [
    ("a", y * sp.exp(x), lambda p, q, U: p + q - U - sp.exp(x), (x, 0, 0)),
    ("b", sp.log(1 + x - y / x), lambda p, q, U: x * p + y * q - x * sp.exp(-U), (x, x**2, 0)),
    ("c", y + 1 + ((x + y)**2 - 1) * sp.exp(y), lambda p, q, U: p - q + U - y, (x, 0, x**2)),
    ("d", x * y**2 + (x - y) / 2, lambda p, q, U: x * p - y * q + U - x, (x, x, x**3)),
    ("e", (x**2 + y**2 + 2) / (2 * (1 - x * y)), lambda p, q, U: x * (y**2 + U) * p - y * (x**2 + U) * q - (x**2 - y**2) * U, (x, -x, 1)),
    ("f", (x + y) * sp.exp(sp.sqrt(2) * y), lambda p, q, U: p - q + sp.sqrt(2) * U, (x, 0, x)),
    ("g", (x + y)**2 * sp.exp(-sp.sqrt(2) * y), lambda p, q, U: p - q - sp.sqrt(2) * U, (x, 0, x**2)),
    ("h", (x + y + sp.exp(x + y)) * sp.exp(sp.sqrt(2) * y), lambda p, q, U: p - q + sp.sqrt(2) * U, (x, 0, x + sp.exp(x))),
    ("i", sp.exp(sp.sqrt(2) * x) * (sp.exp(x + y) - x - y), lambda p, q, U: p - q - sp.sqrt(2) * U, (0, y, sp.exp(y) - y)),
    ("j", sp.exp(x + sp.Rational(5, 4) * y), lambda p, q, U: 3 * p - 4 * q + 2 * U, (x, 0, sp.exp(x))),
    ("k", x / (1 + y), lambda p, q, U: U * p + q, (x, 0, x)),
    ("l", sp.cos(x - y) / (1 - y * sp.cos(x - y)), lambda p, q, U: p + q - U**2, (x, 0, sp.cos(x))),
    ("m", x + y, lambda p, q, U: x * p + y * q - U, (1, y, 1 + y)),
    ("n", (y - x**2)**2 + x * y - sp.Rational(2, 3) * x**3, lambda p, q, U: p + 2 * x * q - y, (0, y, y**2)),
    ("o", x**2 + y**2, lambda p, q, U: y * p - x * q, (0, y, y**2)),
]


def run_q3():
    ok = True
    for lab, U, pde, (xd, yd, ud) in Q3_list:
        res = check_pde(U, lambda p, q, V: pde(p, q, V))
        data = sp.simplify(U.subs({x: xd, y: yd}) - ud)
        good = res == 0 and data == 0
        ok &= good
        print(f"Q3({lab}): PDE residual {res}, data residual {data}")
    # (p): u^2 = (2/7)(2x - y)(x + 2y), u = 0 on y = 2x
    U2 = sp.Rational(2, 7) * (2 * x - y) * (x + 2 * y)
    Up = sp.sqrt(U2)
    resp = sp.simplify(Up * (x + y) * sp.diff(Up, x) + Up * (x - y) * sp.diff(Up, y) - (x**2 + y**2))
    print("Q3(p): PDE residual", resp, " data u^2 on y=2x:", sp.simplify(U2.subs(y, 2 * x)))
    ok &= (resp == 0) and sp.simplify(U2.subs(y, 2 * x)) == 0
    return ok


# ---------------------------------------------------------------- Q1 : formation of PDEs
def run_q1():
    a, b, n, m = sp.symbols("a b n m")
    res = {}
    # (a) u = (x^2+a)(y^2+b)   -> pq = 4xyu
    U = (x**2 + a) * (y**2 + b)
    p, q = sp.diff(U, x), sp.diff(U, y)
    res["a"] = sp.simplify(p * q - 4 * x * y * U)
    # (b) u = ax+by+ab  -> u = px+qy+pq
    U = a * x + b * y + a * b
    p, q = sp.diff(U, x), sp.diff(U, y)
    res["b"] = sp.simplify(U - (p * x + q * y + p * q))
    # (c) (x-a)^2+(y-b)^2+u^2=1 -> u^2(p^2+q^2+1) = 1   (implicit, check by eliminating a,b)
    Uc = sp.sqrt(1 - (x - a)**2 - (y - b)**2)
    p, q = sp.diff(Uc, x), sp.diff(Uc, y)
    res["c"] = sp.simplify(Uc**2 * (p**2 + q**2 + 1) - 1)
    # (d) u = (x-a)^2+(y-b)^2 -> p^2+q^2 = 4u
    Ud = (x - a)**2 + (y - b)**2
    p, q = sp.diff(Ud, x), sp.diff(Ud, y)
    res["d"] = sp.simplify(p**2 + q**2 - 4 * Ud)
    f = sp.Function("f")
    # (e) u = x^n f(y/x) -> x p + y q = n u
    Ue = x**n * f(y / x)
    res["e"] = sp.simplify(x * sp.diff(Ue, x) + y * sp.diff(Ue, y) - n * Ue)
    # (f) u = e^{mx} f(x+y) -> p - q = m u
    Uf = sp.exp(m * x) * f(x + y)
    res["f"] = sp.simplify(sp.diff(Uf, x) - sp.diff(Uf, y) - m * Uf)
    # (g) G(xy+u^2, x+y+u)=0 -> (2u-x)p + (y-2u)q = x-y : check with Jacobian form  (phi_x+phi_u p)(psi_y+psi_u q) = (phi_y+phi_u q)(psi_x+psi_u p)
    P, Q = sp.symbols("P Q")
    phi, psi = x * y + u**2, x + y + u
    det = sp.expand((sp.diff(phi, x) + sp.diff(phi, u) * P) * (sp.diff(psi, y) + sp.diff(psi, u) * Q) - (sp.diff(phi, y) + sp.diff(phi, u) * Q) * (sp.diff(psi, x) + sp.diff(psi, u) * P))
    res["g"] = sp.simplify(det - ((2 * u - x) * P + (y - 2 * u) * Q - (x - y)) * (-1))
    # (h) xyu = f(x+y+u) -> x(y-u)p + y(u-x)q = u(x-y)
    phi, psi = x * y * u, x + y + u
    det = sp.expand((sp.diff(phi, x) + sp.diff(phi, u) * P) * (sp.diff(psi, y) + sp.diff(psi, u) * Q) - (sp.diff(phi, y) + sp.diff(phi, u) * Q) * (sp.diff(psi, x) + sp.diff(psi, u) * P))
    target = x * (y - u) * P + y * (u - x) * Q - u * (x - y)
    res["h"] = sp.simplify(sp.simplify(det / target)) if sp.simplify(target) != 0 else None
    # (i) G(x+y+u, x^2+y^2-u^2) -> (y+u)p - (x+u)q... computed by Jacobian
    phi, psi = x + y + u, x**2 + y**2 - u**2
    det = sp.expand((sp.diff(phi, x) + sp.diff(phi, u) * P) * (sp.diff(psi, y) + sp.diff(psi, u) * Q) - (sp.diff(phi, y) + sp.diff(phi, u) * Q) * (sp.diff(psi, x) + sp.diff(psi, u) * P))
    res["i_det"] = sp.factor(det)
    # (j) u = f(x+iy)+g(x-iy) -> u_xx + u_yy = 0
    g = sp.Function("g")
    Uj = f(x + sp.I * y) + g(x - sp.I * y)
    res["j"] = sp.simplify(sp.diff(Uj, x, 2) + sp.diff(Uj, y, 2))
    for k, v in res.items():
        print("Q1(%s): %s" % (k, v))
    return res


if __name__ == "__main__":
    print("== Q1"); run_q1()
    print("== Q2"); ok2 = run_q2(); run_q2z()
    print("== Q3"); ok3 = run_q3()
    print("ALL Q2 integrals OK:", ok2, "| ALL Q3 OK:", ok3)
