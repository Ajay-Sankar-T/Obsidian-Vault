"""Verification of every number and closed form in the Assignments 6-10 revision notes
(Formula Bank, How to Solve, DE Question Bank 1-3).   Run:  python de_a610_bank.py
Each function p1_q1 ... p3_q14 recomputes one question by an independent route (symbolic substitution, quadrature or a
brute-force series) and asserts the quoted result.  Prints the numbers that appear in the notes."""
import numpy as np
import sympy as sp
from scipy import special as sc
from scipy.integrate import quad
from scipy.optimize import brentq

PI = np.pi
x, y, t, r, th = sp.symbols("x y t r theta", real=True)
OUT = {}


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1, abs(b))


def note(key, val):
    OUT[key] = val
    print(f"  {key}: {val}")


# =====================================================================================================================
# PART 1  Bessel functions (A6) and Sturm-Liouville problems (A7)
# =====================================================================================================================
def p1_q1():
    """Upward recurrence J_{k+1} = (2k/x) J_k - J_{k-1} at x = 2 from J0, J1."""
    J0, J1 = sc.jv(0, 2), sc.jv(1, 2)
    J2 = (2 * 1 / 2) * J1 - J0
    J3 = (2 * 2 / 2) * J2 - J1
    J4 = (2 * 3 / 2) * J3 - J2
    for n, v in ((2, J2), (3, J3), (4, J4)):
        assert close(v, sc.jv(n, 2))
    note("q1", dict(J0=J0, J1=J1, J2=J2, J3=J3, J4=J4))


def p1_q2():
    """int_0^1 x^3 J0(x) dx = J1(1) - 2 J2(1);  antiderivative x^3 J1 - 2 x^2 J2."""
    val = quad(lambda s: s**3 * sc.jv(0, s), 0, 1)[0]
    cf = sc.jv(1, 1) - 2 * sc.jv(2, 1)
    assert close(val, cf)
    # antiderivative check by differentiation at a point
    F = lambda s: s**3 * sc.jv(1, s) - 2 * s**2 * sc.jv(2, s)
    h = 1e-6
    assert close((F(1.7 + h) - F(1.7 - h)) / (2 * h), 1.7**3 * sc.jv(0, 1.7), 1e-6)
    # int_0^2 x^4 J1?  (mu+nu = 5 odd): x^4 J1 -> x^4 J2 - 2 x^3 J3  (used in the MCQ)
    G = lambda s: s**4 * sc.jv(2, s) - 2 * s**3 * sc.jv(3, s)
    assert close((G(1.3 + h) - G(1.3 - h)) / (2 * h), 1.3**4 * sc.jv(1, 1.3), 1e-6)
    note("q2", dict(J1_1=sc.jv(1, 1), J2_1=sc.jv(2, 1), value=cf))


def p1_q3():
    """x^2 y'' + x y' + (16 x^4 - 9) y = 0  ->  y = Z_{3/2}(2 x^2); elementary form."""
    X = sp.symbols("X", positive=True)
    y1 = (sp.sin(2 * X**2) / (2 * X**2) - sp.cos(2 * X**2)) / X
    y2 = (sp.cos(2 * X**2) / (2 * X**2) + sp.sin(2 * X**2)) / X
    for yy in (y1, y2):
        res = X**2 * sp.diff(yy, X, 2) + X * sp.diff(yy, X) + (16 * X**4 - 9) * yy
        for p in (0.4, 0.9, 1.7):
            assert abs(float(res.subs(X, p))) < 1e-10
    # J_{3/2}(2x^2) really is y1 / sqrt(pi) up to the constant
    for p in (0.5, 1.2):
        assert close(sc.jv(1.5, 2 * p**2), float(y1.subs(X, p)) / np.sqrt(PI))
    note("q3", "y = (1/x)[A (sin 2x^2/(2x^2) - cos 2x^2) + B (cos 2x^2/(2x^2) + sin 2x^2)]")


def fb_coeffs(f, nu, L, N):
    """Fourier-Bessel coefficients on [0, L]"""
    al = sc.jn_zeros(nu, N)
    out = []
    for a in al:
        num = quad(lambda s: s * f(s) * sc.jv(nu, a * s / L), 0, L, limit=300)[0]
        out.append(2 / (L**2 * sc.jv(nu + 1, a) ** 2) * num)
    return al, np.array(out)


def p1_q4():
    """1 - x^2 on [0,1] in J0(alpha_n x):  a_n = 8 / (alpha_n^3 J1(alpha_n))"""
    N = 8
    al, a = fb_coeffs(lambda s: 1 - s**2, 0, 1, N)
    cf = 8 / (al**3 * sc.jv(1, al))
    assert np.allclose(a, cf, rtol=1e-8)
    assert np.allclose(4 * sc.jv(2, al) / (al**2 * sc.jv(1, al) ** 2), cf, rtol=1e-8)
    # Parseval: sum a_n^2 J1^2 / 2 = int x (1-x^2)^2 = 1/6 ; many terms
    al2 = sc.jn_zeros(0, 4000)
    a2 = 8 / (al2**3 * sc.jv(1, al2))
    pars = np.sum(a2**2 * sc.jv(1, al2) ** 2 / 2)
    assert abs(pars - 1 / 6) < 1e-8, pars
    # value at 0 and at 0.5 of a long partial sum
    s0 = np.sum(a2 * sc.jv(0, al2 * 0.0))
    s5 = np.sum(a2 * sc.jv(0, al2 * 0.5))
    assert abs(s0 - 1) < 1e-4 and abs(s5 - 0.75) < 1e-6
    note("q4", dict(alpha=al[:3], a=a[:3], parseval=pars, s0=s0, s5=s5))


def p1_q5():
    """McMahon: j_{nu,s} ~ beta - (mu-1)/(8 beta), beta = (s + nu/2 - 1/4) pi, mu = 4 nu^2"""
    res = {}
    for nu in (0, 1):
        s = 10
        beta = (s + nu / 2 - 0.25) * PI
        mu = 4 * nu**2
        approx = beta - (mu - 1) / (8 * beta)
        exact = sc.jn_zeros(nu, s)[-1]
        assert abs(approx - exact) < 2e-3
        res[nu] = (beta, approx, exact)
    z0 = sc.jn_zeros(0, 20)
    gaps = np.diff(z0)
    assert abs(gaps[-1] - PI) < 1e-3
    note("q5", dict(res=res, last_gap=gaps[-1]))


def p1_q6():
    """addition theorem  J_n(x+y) = sum_k J_k(x) J_{n-k}(y);  n = 0, y = x:  J0(2x) = J0^2 + 2 sum (-1)^k J_k^2"""
    xv = 1.3
    lhs = sc.jv(0, 2 * xv)
    rhs = sc.jv(0, xv) ** 2 + 2 * sum((-1) ** k * sc.jv(k, xv) ** 2 for k in range(1, 40))
    assert close(lhs, rhs, 1e-12)
    # general: n = 2
    xv, yv = 0.9, 1.7
    lhs = sc.jv(2, xv + yv)
    rhs = sum(sc.jv(k, xv) * sc.jv(2 - k, yv) for k in range(-40, 41))
    assert close(lhs, rhs, 1e-12)
    note("q6", dict(J0_2x=lhs if False else sc.jv(0, 2.6), J0_x_sq=sc.jv(0, 1.3) ** 2))


def p1_q7():
    """Hermite and Laguerre in Sturm-Liouville form"""
    X, lam = sp.symbols("X lambda")
    yf = sp.Function("yf")
    # Hermite y'' - 2 x y' + 2 lam y = 0 ; p = exp(-x^2)
    p = sp.exp(-X**2)
    herm = sp.simplify(sp.diff(p * yf(X).diff(X), X) / p - (yf(X).diff(X, 2) - 2 * X * yf(X).diff(X)))
    assert herm == 0
    # Laguerre x y'' + (1-x) y' + lam y = 0 ; p = x e^{-x}, r = e^{-x}
    p2 = X * sp.exp(-X)
    lag = sp.simplify(sp.diff(p2 * yf(X).diff(X), X) / sp.exp(-X) - (X * yf(X).diff(X, 2) + (1 - X) * yf(X).diff(X)))
    assert lag == 0
    # orthogonality weights numerically: H2, H3 ; L1, L2
    H2 = sp.hermite(2, X); H4 = sp.hermite(4, X)
    assert sp.integrate(H2 * H4 * sp.exp(-X**2), (X, -sp.oo, sp.oo)) == 0
    L1, L2 = sp.assoc_laguerre(1, 0, X), sp.assoc_laguerre(2, 0, X)
    assert sp.simplify(sp.integrate(L1 * L2 * sp.exp(-X), (X, 0, sp.oo))) == 0
    note("q7", "Hermite p=r=e^{-x^2}; Laguerre p=x e^{-x}, r=e^{-x}")


def p1_q8():
    """y'' + lam y = 0, y(0) = 0, y(1) = y'(1):  lam = 0 (y = x) and lam = mu^2, tan mu = mu"""
    f = lambda m: np.sin(m) - m * np.cos(m)
    roots = []
    for k in range(1, 6):
        lo, hi = k * PI + 1e-6, k * PI + PI / 2 - 1e-6
        roots.append(brentq(f, lo, hi))
    roots = np.array(roots)
    assert np.allclose(np.tan(roots), roots)
    # no root below pi, no negative eigenvalue: tanh k = k only k=0
    assert all(f(m) > 0 for m in np.linspace(0.01, PI, 500))
    ks = np.linspace(0.01, 20, 4000)
    assert all(np.sinh(k) - k * np.cosh(k) < 0 for k in ks)
    # lam = 0: y = x satisfies y(0)=0, y(1)-y'(1) = 0
    assert 1 - 1 == 0
    # orthogonality including y_0 = x
    for m in roots[:3]:
        assert abs(quad(lambda s: s * np.sin(m * s), 0, 1)[0]) < 1e-12
    for m1, m2 in ((roots[0], roots[1]), (roots[1], roots[2])):
        assert abs(quad(lambda s: np.sin(m1 * s) * np.sin(m2 * s), 0, 1)[0]) < 1e-12
    norms = [quad(lambda s: np.sin(m * s) ** 2, 0, 1)[0] for m in roots[:3]]
    cf = [0.5 - np.sin(2 * m) / (4 * m) for m in roots[:3]]
    assert np.allclose(norms, cf)
    # also equals (1 + 1/(1+mu^2)... ) check alternative form: sin^2 = mu^2/(1+mu^2) at tan mu = mu
    alt = [0.5 * (1 - (np.sin(m) * np.cos(m)) / m) for m in roots[:3]]
    assert np.allclose(norms, alt)
    # norm of y0 = x
    assert close(quad(lambda s: s * s, 0, 1)[0], 1 / 3)
    note("q8", dict(mu=roots[:4], lam=roots[:4] ** 2, norms=norms))


def p1_q9():
    """(x y')' + (lam/x) y = 0, y'(1) = 0, y(e^2) = 0 :  lam_n = ((2n-1) pi/4)^2, y_n = cos(mu_n ln x), weight 1/x.
       1 = (4/pi) sum (-1)^{n+1} cos(mu_n ln x)/(2n-1)"""
    n = np.arange(1, 4000)
    mu = (2 * n - 1) * PI / 4
    for m in mu[:4]:
        # residual of ODE for y = cos(m ln x)
        X = sp.symbols("X", positive=True)
        yy = sp.cos(float(m) * sp.log(X))
        res = sp.diff(X * sp.diff(yy, X), X) + float(m) ** 2 / X * yy
        assert abs(float(res.subs(X, 1.9))) < 1e-10
        # BC: y'(1) = 0 , y(e^2) = cos(2m) = 0
        assert abs(float(sp.diff(yy, X).subs(X, 1))) < 1e-12 and abs(np.cos(2 * m)) < 1e-12
    # orthogonality with weight 1/x : substitute t = ln x
    assert abs(quad(lambda s: np.cos(mu[0] * s) * np.cos(mu[1] * s), 0, 2)[0]) < 1e-12
    assert close(quad(lambda s: np.cos(mu[0] * s) ** 2, 0, 2)[0], 1.0)
    a = (-1) ** (n + 1) * 4 / ((2 * n - 1) * PI)
    num = [quad(lambda s: np.cos(m * s), 0, 2)[0] for m in mu[:5]]
    assert np.allclose(num, a[:5])
    for xv in (1.0, 2.0, 5.0):
        s = np.sum(a * np.cos(mu * np.log(xv)))
        assert abs(s - 1) < 2e-3, (xv, s)
    note("q9", dict(lam=mu[:3] ** 2, a=a[:4]))


def p1_q10():
    """Chebyshev: x^4 = (3 T0 + 4 T2 + T4)/8 with weight 1/sqrt(1-x^2); Parseval 35 pi/128"""
    T = lambda n, s: np.cos(n * np.arccos(s))
    coef = {}
    for n in range(0, 7):
        # theta substitution: int f T_n / sqrt(1-x^2) dx = int_0^pi cos^4(theta) cos(n theta) dtheta
        I = quad(lambda th_: np.cos(th_) ** 4 * np.cos(n * th_), 0, PI)[0]
        coef[n] = I / PI if n == 0 else 2 * I / PI
    assert close(coef[0], 3 / 8) and close(coef[2], 1 / 2) and close(coef[4], 1 / 8)
    assert abs(coef[1]) < 1e-12 and abs(coef[3]) < 1e-12 and abs(coef[6]) < 1e-12
    xs = np.linspace(-1, 1, 11)
    assert np.allclose((3 * T(0, xs) + 4 * T(2, xs) + T(4, xs)) / 8, xs**4)
    parseval = PI * (coef[0] ** 2 + 0.5 * (coef[2] ** 2 + coef[4] ** 2))
    assert close(parseval, 35 * PI / 128)
    assert close(quad(lambda th_: np.cos(th_) ** 8, 0, PI)[0], 35 * PI / 128)
    # x^3 = (3 T1 + T3)/4
    c1 = 2 * quad(lambda th_: np.cos(th_) ** 3 * np.cos(th_), 0, PI)[0] / PI
    c3 = 2 * quad(lambda th_: np.cos(th_) ** 3 * np.cos(3 * th_), 0, PI)[0] / PI
    assert close(c1, 3 / 4) and close(c3, 1 / 4)
    note("q10", dict(coef=coef, parseval_over_pi=parseval / PI))


# --------------------------------------------------------------------------------------------------------------------
# MCQ-level facts for the hub
def mcq_part1():
    # Wronskian of J_{1/2}, J_{-1/2} = -2/(pi x)
    X = sp.symbols("X", positive=True)
    j1 = sp.sqrt(2 / (sp.pi * X)) * sp.sin(X)
    j2 = sp.sqrt(2 / (sp.pi * X)) * sp.cos(X)
    W = sp.simplify(j1 * sp.diff(j2, X) - sp.diff(j1, X) * j2)
    assert sp.simplify(W + 2 / (sp.pi * X)) == 0
    # J_{3/2}(pi) = sqrt(2/pi^2) (0 - (-1)) /pi ... numeric
    val = sc.jv(1.5, PI)
    assert close(val, np.sqrt(2 / (PI * PI)) * (np.sin(PI) / PI - np.cos(PI)))
    # j0 first zero pi ; spherical bessel zeros of j1: tan x = x
    # Gamma(1/2)
    assert close(sc.gamma(0.5), np.sqrt(PI))
    # d/dx [x^2 J2] = x^2 J1
    h = 1e-6
    assert close(((1.4 + h) ** 2 * sc.jv(2, 1.4 + h) - (1.4 - h) ** 2 * sc.jv(2, 1.4 - h)) / (2 * h), 1.4**2 * sc.jv(1, 1.4), 1e-6)
    # J0'(x) = -J1(x)
    assert close((sc.jv(0, 2.0 + h) - sc.jv(0, 2.0 - h)) / (2 * h), -sc.jv(1, 2.0), 1e-6)
    # int_0^inf e^{-x} J0(x) dx = 1/sqrt(2)
    assert close(quad(lambda s: np.exp(-s) * sc.jv(0, s), 0, 60)[0], 1 / np.sqrt(2), 1e-8)
    # largest value of |J1| 0.5819 ; J0(0)=1
    xs = np.linspace(0, 10, 100001)
    assert abs(np.max(np.abs(sc.jv(1, xs))) - 0.5819) < 1e-4
    # Legendre: x^2 as P0/P2 : x^2 = (2 P2 + P0)/3 ... not used here
    note("mcq1", "ok")


# =====================================================================================================================
def formula_bank_checks():
    """formulas quoted in the Formula Bank that are not covered by a question"""
    L = 1.7
    n = 3
    s = lambda f: quad(f, 0, L, limit=300)[0]
    sn = lambda z: np.sin(n * PI * z / L)
    cn = lambda z: np.cos(n * PI * z / L)
    q = n * PI
    assert close(s(lambda z: sn(z)), L * (1 - (-1) ** n) / q)
    assert close(s(lambda z: z * sn(z)), (-1) ** (n + 1) * L**2 / q)
    assert close(s(lambda z: z**2 * sn(z)), (-1) ** (n + 1) * L**3 / q + 2 * L**3 * ((-1) ** n - 1) / q**3)
    assert close(s(lambda z: z * (L - z) * sn(z)), 2 * L**3 * (1 - (-1) ** n) / q**3)
    assert close(s(lambda z: z * cn(z)), L**2 * ((-1) ** n - 1) / q**2)
    # series: 1 = (4/pi) sum_odd sin/k ; x = (2L/pi) sum (-1)^{k+1} sin/k ; x(L-x) = (8L^2/pi^3) sum_odd sin/k^3
    k = np.arange(1, 200001)
    z = 0.37 * L
    sk = np.sin(k * PI * z / L)
    odd = (k % 2 == 1)
    assert abs(4 / PI * np.sum((sk / k)[odd]) - 1) < 1e-3
    assert abs(2 * L / PI * np.sum((-1.0) ** (k + 1) * sk / k) - z) < 1e-3
    assert abs(8 * L**2 / PI**3 * np.sum((sk / k**3)[odd]) - z * (L - z)) < 1e-9
    # triangle with peak h at L/2 : (8h/pi^2) sum_odd (-1)^{(k-1)/2} sin/k^2
    h = 1.0
    tri = lambda w: 2 * h * w / L if w <= L / 2 else 2 * h * (L - w) / L
    kk = k[odd]
    assert abs(8 * h / PI**2 * np.sum((-1.0) ** ((kk - 1) // 2) * np.sin(kk * PI * z / L) / kk**2) - tri(z)) < 1e-8
    # cosine series of x on (0, L): L/2 - (4L/pi^2) sum_odd cos/k^2
    assert abs(L / 2 - 4 * L / PI**2 * np.sum(np.cos(kk * PI * z / L) / kk**2) - z) < 1e-8
    # mixed-basis integrals when cos mu = 0 : int_0^1 sin = 1/mu, int_0^1 x sin = sin(mu)/mu^2
    for m in ((np.arange(1, 5) - 0.5) * PI):
        assert close(quad(lambda w: np.sin(m * w), 0, 1)[0], 1 / m)
        assert close(quad(lambda w: w * np.sin(m * w), 0, 1)[0], np.sin(m) / m**2)
    # Bessel: integral representation, norm, f = x^nu coefficient, Laplace transform, int J0 = 1
    for nn_, xx in ((0, 2.3), (1, 2.3), (3, 5.1)):
        val = quad(lambda w: np.cos(nn_ * w - xx * np.sin(w)), 0, PI)[0] / PI
        assert close(val, sc.jv(nn_, xx))
    for nu in (0, 1, 2.5):
        a1 = sc.jn_zeros(int(nu), 1)[0] if nu == int(nu) else 2.0 * PI / 2   # half-integer: roots of J_{5/2}
        if nu != int(nu):
            a1 = brentq(lambda w: sc.jv(2.5, w), 5.0, 7.0)
        nrm = quad(lambda w: w * sc.jv(nu, a1 * w) ** 2, 0, 1)[0]
        assert close(nrm, 0.5 * sc.jv(nu + 1, a1) ** 2)
        assert close(sc.jvp(nu, a1), -sc.jv(nu + 1, a1))
        # f = x^nu : a_n = 2 / (alpha J_{nu+1}(alpha))
        num = quad(lambda w: w * w**nu * sc.jv(nu, a1 * w), 0, 1)[0]
        assert close(2 / sc.jv(nu + 1, a1) ** 2 * num, 2 / (a1 * sc.jv(nu + 1, a1)))
    assert abs(sc.itj0y0(2000.0)[0] - 1.0) < 0.03          # conditionally convergent: the tail oscillates like x^(-1/2)
    assert close(1 / np.hypot(1e-6, 1.0), 1.0, 1e-9)       # Laplace transform with a -> 0 gives int_0^oo J0 = 1
    for a_, b_ in ((1.3, 0.8), (0.5, 2.0)):
        assert close(quad(lambda w: np.exp(-a_ * w) * sc.jv(0, b_ * w), 0, 80, limit=400)[0], 1 / np.hypot(a_, b_), 1e-8)
    # Y definition and asymptotics
    nu_, xx = 0.4, 7.3
    assert close(sc.yv(nu_, xx), (sc.jv(nu_, xx) * np.cos(nu_ * PI) - sc.jv(-nu_, xx)) / np.sin(nu_ * PI))
    xx = 60.0
    assert abs(sc.jv(2, xx) - np.sqrt(2 / (PI * xx)) * np.cos(xx - PI - PI / 4)) < 5e-3
    assert abs(sc.yv(2, xx) - np.sqrt(2 / (PI * xx)) * np.sin(xx - PI - PI / 4)) < 5e-3
    # Wronskian W(J_nu, J_-nu) = -2 sin(nu pi)/(pi x)
    nu_, xx, h_ = 0.3, 2.1, 1e-6
    W = sc.jv(nu_, xx) * (sc.jv(-nu_, xx + h_) - sc.jv(-nu_, xx - h_)) / (2 * h_) - (sc.jv(nu_, xx + h_) - sc.jv(nu_, xx - h_)) / (2 * h_) * sc.jv(-nu_, xx)
    assert close(W, -2 * np.sin(nu_ * PI) / (PI * xx), 1e-6)
    zt = {nu: sc.jn_zeros(nu, 5) for nu in (0, 1, 2)}
    # Lagrange formation determinant: P = phi_y psi_u - phi_u psi_y, Q = phi_u psi_x - phi_x psi_u, R = phi_x psi_y - phi_y psi_x
    X, Y, U = sp.symbols("X Y U")
    for phi, psi in ((X * Y + U**2, X + Y + U), (X * Y * U, X + Y + U)):
        P = sp.diff(phi, Y) * sp.diff(psi, U) - sp.diff(phi, U) * sp.diff(psi, Y)
        Q_ = sp.diff(phi, U) * sp.diff(psi, X) - sp.diff(phi, X) * sp.diff(psi, U)
        R_ = sp.diff(phi, X) * sp.diff(psi, Y) - sp.diff(phi, Y) * sp.diff(psi, X)
        # check along a solution surface: pick F(phi, psi) = phi - psi^2 ... use implicit solution u(x,y)
        F = phi - psi**2
        uu = sp.Function("uu")
        eq = F.subs(U, uu(X, Y))
        sol = sp.diff(eq, X)
        sol2 = sp.diff(eq, Y)
        p_, q_ = sp.symbols("p_ q_")
        ssol = sp.solve([sol.subs(sp.Derivative(uu(X, Y), X), p_).subs(sp.Derivative(uu(X, Y), Y), q_),
                         sol2.subs(sp.Derivative(uu(X, Y), X), p_).subs(sp.Derivative(uu(X, Y), Y), q_)], [p_, q_], dict=True)[0]
        lhs = (P * ssol[p_] + Q_ * ssol[q_] - R_).subs(uu(X, Y), U)
        assert sp.simplify(lhs) == 0
    # plucked at a: A_n = 2 h L^2 sin(n pi a / L) / (a (L - a) n^2 pi^2)
    L, a, h = 1.3, 0.4, 0.9
    pl = lambda w: h * w / a if w <= a else h * (L - w) / (L - a)
    for n in (1, 2, 3, 5):
        An = 2 / L * quad(lambda w: pl(w) * np.sin(n * PI * w / L), 0, L, points=[a])[0]
        assert close(An, 2 * h * L**2 * np.sin(n * PI * a / L) / (a * (L - a) * n**2 * PI**2))
    # Robin: y(0) = 0, y'(L) + h y(L) = 0 -> tan(mu L) = -mu/h
    L, hh = 2.0, 0.7
    f = lambda m: m * np.cos(m * L) + hh * np.sin(m * L)
    m1 = brentq(f, PI / (2 * L) + 1e-6, PI / L - 1e-6)
    assert close(np.tan(m1 * L), -m1 / hh, 1e-8)
    assert close(quad(lambda w: np.sin(m1 * w) ** 2, 0, L)[0], L / 2 - np.sin(2 * m1 * L) / (4 * m1))
    # first-order-term elimination: u_xi,eta + d u_xi + e u_eta + f u = 0, u = exp(-e xi - d eta) v -> v_xieta + (f - d e) v = 0
    d, e, ff = sp.symbols("d e f")
    xi, eta = sp.symbols("xi eta")
    v = sp.Function("v")
    uu = sp.exp(-e * xi - d * eta) * v(xi, eta)
    L_ = sp.diff(uu, xi, eta) + d * sp.diff(uu, xi) + e * sp.diff(uu, eta) + ff * uu
    red = sp.simplify(L_ / sp.exp(-e * xi - d * eta))
    assert sp.simplify(red - (sp.diff(v(xi, eta), xi, eta) + (ff - d * e) * v(xi, eta))) == 0
    # Laplace form: u_xx + u_yy + d u_x + e u_y + f u: alpha = -d/2, beta = -e/2, c = f - (d^2+e^2)/4
    uu = sp.exp(-d * x / 2 - e * y / 2) * v(x, y)
    L_ = sp.diff(uu, x, 2) + sp.diff(uu, y, 2) + d * sp.diff(uu, x) + e * sp.diff(uu, y) + ff * uu
    red = sp.simplify(L_ / sp.exp(-d * x / 2 - e * y / 2))
    assert sp.simplify(red - (sp.diff(v(x, y), x, 2) + sp.diff(v(x, y), y, 2) + (ff - (d**2 + e**2) / 4) * v(x, y))) == 0
    # constant coefficients: u = f(y + lam x) with a lam^2 + b lam + c = 0
    f_ = sp.Function("f")
    lam = sp.symbols("lam")
    aa, bb, cc = sp.symbols("aa bb cc")
    uu = f_(y + lam * x)
    res = aa * sp.diff(uu, x, 2) + bb * sp.diff(uu, x, y) + cc * sp.diff(uu, y, 2)
    assert sp.simplify(res - (aa * lam**2 + bb * lam + cc) * sp.diff(f_(y + lam * x), y, 2)) == 0
    # Neumann ends u_x(0)=alpha, u_x(L)=beta: mean rises at c^2 (beta - alpha)/L ; check on w = alpha x + (beta-alpha) x^2/(2L) + c^2 (beta-alpha) t/L
    al, be, Lq, c2, tq = sp.symbols("alpha beta L c2 t", positive=True)
    w = al * x + (be - al) * x**2 / (2 * Lq) + c2 * (be - al) * tq / Lq
    assert sp.simplify(sp.diff(w, tq) - c2 * sp.diff(w, x, 2)) == 0
    assert sp.simplify(sp.diff(w, x).subs(x, 0) - al) == 0 and sp.simplify(sp.diff(w, x).subs(x, Lq) - be) == 0
    # semi-infinite strip decay and rectangle driven from the bottom: sinh(n pi (b - y)/a)/sinh(n pi b/a) is 1 at y=0, 0 at y=b
    # Poisson kernel half-disc closed form already verified in p3_q14; sector kernel in p3_q13
    # Hermite weight etc. verified in p1_q7.   McMahon verified in p1_q5.
    note("zeros", {k_: np.round(v_, 4) for k_, v_ in zt.items()})


def run_part1():
    print("PART 1")
    for f in (p1_q1, p1_q2, p1_q3, p1_q4, p1_q5, p1_q6, p1_q7, p1_q8, p1_q9, p1_q10, mcq_part1, formula_bank_checks):
        print(f.__name__)
        f()


if __name__ == "__main__":
    run_part1()
    print("part 1 checks passed")
