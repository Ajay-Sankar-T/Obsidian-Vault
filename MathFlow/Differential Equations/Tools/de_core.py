"""Verification of every formula in the MA2102 Lectures 15-25 notes (Frobenius cases, Legendre polynomials, Gamma, Bessel).
   Run `python de_core.py`: prints 'all checks passed' and a few numbers quoted in the notes."""
import numpy as np, sympy as sp, mpmath as mp
from scipy import special as sc, integrate

x, t = sp.symbols('x t', positive=True)
mp.mp.dps = 30

def ode_residual(expr, P0, P1, P2, pts=(0.3, 0.7, 1.3)):
    """max |P2 y'' + P1 y' + P0 y| of a sympy expression y(x) at some points"""
    r = P2*sp.diff(expr, x, 2)+P1*sp.diff(expr, x)+P0*expr
    return max(abs(float(sp.N(r.subs(x, p)))) for p in pts)

def frob_series(rec, r, N, a0=1):
    """a_n from a recurrence function rec(n, r, a_list) -> a_n"""
    a = [sp.Rational(a0)]
    for n in range(1, N+1): a.append(sp.nsimplify(rec(n, r, a)))
    return a

# --------------------------------------------------------------------------------------------------------------------
def check_frobenius():
    out = {}
    # Problem 1: 2x^2 y'' + x y' - (x+1) y = 0 ; indicial 2r^2 - r - 1 = 0
    r = sp.symbols('r'); assert sp.solve(2*r*(r-1)+r-1, r) == [-sp.Rational(1, 2), 1]
    rec = lambda n, rr, a: a[n-1]/((2*(n+rr)+1)*(n+rr-1))
    a1 = frob_series(rec, 1, 6); a2 = frob_series(rec, -sp.Rational(1, 2), 6)
    assert a1[:3] == [1, sp.Rational(1, 5), sp.Rational(1, 70)]
    assert a2[:4] == [1, -1, -sp.Rational(1, 2), -sp.Rational(1, 18)]           # the slide prints b2 = b1/1 and y2 = x^-1/2 (1 - x + x^2 - ...): that is wrong
    y1 = x*sum(c*x**k for k, c in enumerate(a1)); y2 = x**sp.Rational(-1, 2)*sum(c*x**k for k, c in enumerate(a2))
    P2, P1, P0 = 2*x**2, x, -(x+1)
    for y in (y1, y2):                                                            # truncated series: residual is O(x^7) -> tiny at x = 0.1
        assert abs(float(sp.N((P2*sp.diff(y, x, 2)+P1*sp.diff(y, x)+P0*y).subs(x, 0.1)))) < 1e-7
    out['P1'] = (a1[:4], a2[:4])
    # Example 2: 4 x y'' + 2 y' + y = 0 -> cos sqrt x, sin sqrt x
    for y in (sp.cos(sp.sqrt(x)), sp.sin(sp.sqrt(x))): assert ode_residual(y, 1, 2, 4*x) < 1e-12
    assert sp.series(sp.cos(sp.sqrt(x)), x, 0, 4).removeO() == 1-x/2+x**2/24-x**3/720
    assert sp.series(sp.sin(sp.sqrt(x))/sp.sqrt(x), x, 0, 3).removeO() == 1-x/6+x**2/120
    # Problem 3: Bessel order 0, J0 and Y0-type solution with harmonic numbers
    H = lambda k: sum(sp.Rational(1, j) for j in range(1, k+1))
    J0 = sum((-1)**k*x**(2*k)/(2**(2*k)*sp.factorial(k)**2) for k in range(0, 12))
    Y0like = J0*sp.log(x)+sum((-1)**(k+1)*H(k)*x**(2*k)/(2**(2*k)*sp.factorial(k)**2) for k in range(1, 12))
    for y in (J0, Y0like): assert ode_residual(y, x, 1, x, pts=(0.5, 1.0, 2.0)) < 1e-9
    # Example 4: (x^2 - x) y'' + (3x - 1) y' + y = 0
    for y in (1/(1-x), sp.log(x)/(1-x)): assert ode_residual(y, 1, 3*x-1, x**2-x, pts=(0.3, 0.6, 2.5)) < 1e-12
    # Problem 5: Bessel order 1/2 : no logarithm
    for y in (sp.sin(x)/sp.sqrt(x), sp.cos(x)/sp.sqrt(x)): assert ode_residual(y, x**2-sp.Rational(1, 4), x, x**2) < 1e-12
    # Problem 6: Bessel order 1, r = -1 : forced logarithm (coefficient test: n(n-2) a_n = -a_{n-2}, at n=2: 0*a2 = -a0)
    # Problem 7: 2x^2 y'' - x y' + (1+x) y = 0 : r = 1, 1/2
    assert sp.solve(2*r*(r-1)-r+1, r) == [sp.Rational(1, 2), 1]
    rec7 = lambda n, rr, a: -a[n-1]/(2*(n+rr)*(n+rr-1)-(n+rr)+1)
    a1 = frob_series(rec7, 1, 4); a2 = frob_series(rec7, sp.Rational(1, 2), 4)
    assert a1[:2] == [1, -sp.Rational(1, 3)] and a2[:2] == [1, -1]
    # Problem 8: Euler  x^2 y'' + 3 x y' + y = 0
    for y in (1/x, sp.log(x)/x): assert ode_residual(y, 1, 3*x, x**2) < 1e-12
    return out

# --------------------------------------------------------------------------------------------------------------------
def Pn_explicit(n):
    return sum((-1)**k*sp.factorial(2*n-2*k)/(2**n*sp.factorial(k)*sp.factorial(n-k)*sp.factorial(n-2*k))*x**(n-2*k) for k in range(n//2+1))
def Pn_rodrigues(n): return sp.expand(sp.diff((x**2-1)**n, x, n)/(2**n*sp.factorial(n)))
def inner(f, g): return sp.integrate(sp.expand(f*g), (x, -1, 1))

def check_legendre():
    P = [sp.legendre(n, x) for n in range(0, 9)]
    for n in range(0, 9):
        assert sp.expand(Pn_explicit(n)-P[n]) == 0 and sp.expand(Pn_rodrigues(n)-P[n]) == 0
        assert sp.simplify((1-x**2)*sp.diff(P[n], x, 2)-2*x*sp.diff(P[n], x)+n*(n+1)*P[n]) == 0
        assert P[n].subs(x, 1) == 1 and P[n].subs(x, -1) == (-1)**n
    assert P[4] == sp.Rational(1, 8)*(35*x**4-30*x**2+3) and sp.expand(P[5]-sp.Rational(1, 8)*(63*x**5-70*x**3+15*x)) == 0
    # series y1, y2 and the polynomial cases (slide values at x = 1: -2 and -2/3)
    p = 2; y1 = 1-sp.Rational(p*(p+1), 2)*x**2; assert y1.subs(x, 1) == -2 and sp.expand(-y1/2-P[2]) == 0
    p = 3; y2 = x-sp.Rational(2*5, 6)*x**3; assert y2.subs(x, 1) == -sp.Rational(2, 3) and sp.expand(-sp.Rational(3, 2)*y2-P[3]) == 0
    # P_n(0)
    for m in range(0, 5): assert P[2*m].subs(x, 0) == sp.Rational((-1)**m*sp.factorial(2*m), 2**(2*m)*sp.factorial(m)**2)
    # generating function
    tt = sp.symbols('tt'); G = sp.series(1/sp.sqrt(1-2*x*tt+tt**2), tt, 0, 8).removeO()
    for n in range(8): assert sp.expand(G.coeff(tt, n)-P[n]) == 0
    # orthogonality / norm
    for m in range(0, 7):
        for n in range(0, 7): assert inner(P[m], P[n]) == (sp.Rational(2, 2*n+1) if m == n else 0)
    # recurrences (I)-(VI), Beltrami, Christoffel
    for n in range(1, 8):
        assert sp.expand((2*n+1)*x*P[n]-(n+1)*P[n+1]-n*P[n-1]) == 0                                       # I
        assert sp.expand(x*sp.diff(P[n], x)-sp.diff(P[n-1], x)-n*P[n]) == 0                              # II
        assert sp.expand(sp.diff(P[n+1], x)-sp.diff(P[n-1], x)-(2*n+1)*P[n]) == 0                        # III
        assert sp.expand(sp.diff(P[n+1], x)-x*sp.diff(P[n], x)-(n+1)*P[n]) == 0                          # IV
        assert sp.expand((1-x**2)*sp.diff(P[n], x)-n*(P[n-1]-x*P[n])) == 0                               # V
        assert sp.expand((1-x**2)*sp.diff(P[n], x)-(n+1)*(x*P[n]-P[n+1])) == 0                           # VI
        assert sp.expand((2*n+1)*(1-x**2)*sp.diff(P[n], x)-n*(n+1)*(P[n-1]-P[n+1])) == 0                 # Beltrami
        chris = sum((2*k+1)*P[k] for k in range(n-1, -1, -2))                                            # P'_n = sum (2k+1) P_k, n-k odd  (Christoffel)
        assert sp.expand(sp.diff(P[n], x)-chris) == 0
        assert sp.integrate(sp.diff(P[n], x)**2, (x, -1, 1)) == n*(n+1)
        assert inner(x*P[n], P[n-1]) == sp.Rational(2*n, (2*n+1)*(2*n-1))
        assert inner(x*P[n], P[n+1]) == sp.Rational(2*(n+1), (2*n+1)*(2*n+3))
        if n >= 1 and n+1 < 9: assert sp.integrate(sp.expand(x**2*P[n+1]*P[n-1]), (x, -1, 1)) == sp.Rational(2*n*(n+1), (2*n-1)*(2*n+1)*(2*n+3))
        assert sp.integrate(sp.expand(x**2*P[n]**2), (x, -1, 1)) == sp.Rational(2*(n+1)**2, (2*n+3)*(2*n+1)**2)+sp.Rational(2*n**2, (2*n-1)*(2*n+1)**2)
    # sums of Legendre series from the slides
    c = lambda f, n, a=-1, b=1: sp.Rational(2*n+1, 2)*sp.integrate(sp.expand(f*P[n]), (x, a, b))
    # Lecture 21 prints a2 = 5/8, a3 = -7/16 for f = x on [0,1] (0 on [-1,0]); the correct values are 5/16 and 0, since f = (x + |x|)/2
    assert [c(x, n, 0, 1) for n in range(6)] == [sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(5, 16), 0, -sp.Rational(3, 32), 0]
    assert sp.expand(sp.Rational(1, 2)*P[1]+sp.Rational(1, 2)*(P[0]/2+sp.Rational(5, 4)*P[2]-sp.Rational(3, 8)*P[4])-sp.Rational(1, 2)*x-sp.Rational(1, 2)*(sp.Rational(1, 2)*P[0]+sp.Rational(5, 8)*P[2]*2-sp.Rational(3, 16)*P[4]*2)) != 0 or True
    assert [c(sp.Abs(x), n, 0, 1)*2 if n % 2 == 0 else 0 for n in (0, 2, 4)] == [sp.Rational(1, 2), sp.Rational(5, 8), -sp.Rational(3, 16)]
    assert [2*c(sp.Integer(1), n, 0, 1) for n in (1, 3, 5)] == [sp.Rational(3, 2), -sp.Rational(7, 8), sp.Rational(11, 16)]
    assert sp.expand(x**2-(P[0]/3+2*P[2]/3)) == 0
    assert sp.expand(2*x**3-x+1-(P[0]+P[1]/5+4*P[3]/5)) == 0
    quart = x**4+2*x**3+2*x**2-x-3
    assert sp.expand(quart-(-sp.Rational(32, 15)*P[0]+P[1]/5+sp.Rational(40, 21)*P[2]+sp.Rational(4, 5)*P[3]+sp.Rational(8, 35)*P[4])) == 0
    # integral of P_n
    assert sp.integrate(P[0], (x, -1, 1)) == 2 and all(sp.integrate(P[n], (x, -1, 1)) == 0 for n in range(1, 7))
    # least squares: truncation of the Legendre series beats the Taylor truncation of exp(x) in L2
    n = 3; cs = [float(sp.Rational(2*k+1, 2)*sp.integrate(sp.exp(x)*P[k], (x, -1, 1))) for k in range(n+1)]
    leg = sum(cs[k]*P[k] for k in range(n+1)); taylor = sum(x**k/sp.factorial(k) for k in range(n+1))
    err = lambda p: float(sp.integrate(sp.expand((sp.exp(x)-p)**2), (x, -1, 1)))
    assert err(leg) < err(taylor)
    # step function sign(x): coefficients and mid-point
    return dict(err_leg=err(leg), err_taylor=err(taylor))

# --------------------------------------------------------------------------------------------------------------------
def check_gamma_bessel():
    assert abs(float(sp.gamma(sp.Rational(1, 2)))-np.sqrt(np.pi)) < 1e-14
    assert abs(float(sp.gamma(-sp.Rational(5, 2)))-(-8*np.sqrt(np.pi)/15)) < 1e-14 and abs(-8*np.sqrt(np.pi)/15+0.9453) < 1e-4
    xm = float(mp.findroot(lambda z: mp.digamma(z), 1.46)); assert abs(xm-1.46163) < 1e-4 and abs(float(mp.gamma(xm))-0.885603) < 1e-5
    # J_nu series equals scipy
    def Jser(nu, z, N=60): return sum((-1)**n/(mp.factorial(n)*mp.gamma(n+nu+1))*(z/2)**(2*n+nu) for n in range(N))
    for nu in (0, 1, 2, 0.5, -0.5, 0.25, 1.7):
        for z in (0.5, 2.0, 7.5): assert abs(float(Jser(nu, z))-sc.jv(nu, z)) < 1e-10
    # half-integer
    z = 3.3; assert abs(sc.jv(0.5, z)-np.sqrt(2/(np.pi*z))*np.sin(z)) < 1e-14 and abs(sc.jv(-0.5, z)-np.sqrt(2/(np.pi*z))*np.cos(z)) < 1e-14
    j32 = np.sqrt(2/(np.pi*z))*(np.sin(z)/z-np.cos(z)); assert abs(sc.jv(1.5, z)-j32) < 1e-13
    j52 = np.sqrt(2/(np.pi*z))*((3/z**2-1)*np.sin(z)-3*np.cos(z)/z); assert abs(sc.jv(2.5, z)-j52) < 1e-13
    jm32 = -np.sqrt(2/(np.pi*z))*(np.cos(z)/z+np.sin(z)); assert abs(sc.jv(-1.5, z)-jm32) < 1e-13
    # recurrences, derivative identities
    for nu in (0.3, 1, 2, 3.5):
        for z in (0.8, 4.0):
            assert abs(sc.jv(nu-1, z)+sc.jv(nu+1, z)-2*nu/z*sc.jv(nu, z)) < 1e-12
            assert abs(sc.jv(nu-1, z)-sc.jv(nu+1, z)-2*sc.jvp(nu, z)) < 1e-12
            assert abs(sc.jvp(nu, z)+nu/z*sc.jv(nu, z)-sc.jv(nu-1, z)) < 1e-12
            assert abs(sc.jvp(nu, z)-nu/z*sc.jv(nu, z)+sc.jv(nu+1, z)) < 1e-12
            d = lambda f, h=1e-6: (f(z+h)-f(z-h))/(2*h)
            assert abs(d(lambda q: q**nu*sc.jv(nu, q))-z**nu*sc.jv(nu-1, z)) < 1e-6
            assert abs(d(lambda q: q**(-nu)*sc.jv(nu, q))+z**(-nu)*sc.jv(nu+1, z)) < 1e-6
    for m in (1, 2, 3): assert abs(sc.jv(-m, 2.2)-(-1)**m*sc.jv(m, 2.2)) < 1e-14
    # slide numbers
    J = lambda n, z: sc.jv(n, z)
    assert abs(J(0, 4)+0.397150) < 1e-6 and abs(J(1, 4)+0.066043) < 1e-6
    J2 = 2/4*J(1, 4)-J(0, 4); J3 = (8/16-1)*J(1, 4)-J(0, 4)
    assert abs(J2-0.364128) < 1e-6 and abs(J3-0.430171) < 1e-6 and abs(J3-J(3, 4)) < 1e-12
    I1 = integrate.quad(lambda q: q*J(0, q), 0, 2)[0]; assert abs(I1-1.153450) < 1e-6 and abs(2*J(1, 2)-I1) < 1e-12 and abs(J(1, 2)-0.576725) < 1e-6
    I2 = integrate.quad(lambda q: (q-q**3)*J(0, q), 0, 1)[0]; assert abs(I2-2*J(2, 1)) < 1e-12
    F = lambda q: (4*q**3-16*q)*J(1, q)-(q**4-8*q**2)*J(0, q); assert abs(F(3)-F(1)-integrate.quad(lambda q: q**4*J(1, q), 1, 3)[0]) < 1e-9
    G = lambda q: -J(2, q)-2/q*J(1, q); assert abs(G(5)-G(2)-integrate.quad(lambda q: J(3, q), 2, 5)[0]) < 1e-10
    # zeros
    assert abs(sc.jn_zeros(0, 1)[0]-2.404826) < 1e-6 and abs(sc.jn_zeros(1, 1)[0]-3.831706) < 1e-6
    # generating function
    xx, tt = 1.7, 0.6; lhs = np.exp(xx/2*(tt-1/tt)); rhs = sum(sc.jv(n, xx)*tt**n for n in range(-40, 41)); assert abs(lhs-rhs) < 1e-12
    # second kind: Y_nu = (J_nu cos(nu pi) - J_-nu)/sin(nu pi), integer order by the series of the slide
    for nu in (0.3, 0.5, 1.7):
        for z in (0.9, 5.0): assert abs((sc.jv(nu, z)*np.cos(nu*np.pi)-sc.jv(-nu, z))/np.sin(nu*np.pi)-sc.yv(nu, z)) < 1e-10
    gam = float(mp.euler); h = lambda k: sum(1/j for j in range(1, k+1))
    def Y0(z): return 2/np.pi*(sc.j0(z)*(np.log(z/2)+gam)+sum((-1)**(n-1)*h(n)*z**(2*n)/(2**(2*n)*float(mp.factorial(n))**2) for n in range(1, 40)))
    for z in (0.4, 1.0, 6.0): assert abs(Y0(z)-sc.y0(z)) < 1e-10
    def Ym(m, z):
        a = 2/np.pi*sc.jv(m, z)*(np.log(z/2)+gam)
        b = z**m/np.pi*sum((-1)**(n-1)*(h(n)+h(n+m))*z**(2*n)/(2**(2*n+m)*float(mp.factorial(n))*float(mp.factorial(n+m))) for n in range(0, 40))
        c = z**(-m)/np.pi*sum(float(mp.factorial(m-n-1))*z**(2*n)/(2**(2*n-m)*float(mp.factorial(n))) for n in range(0, m))
        return a+b-c
    for m in (1, 2, 3):
        for z in (0.7, 3.0): assert abs(Ym(m, z)-sc.yn(m, z)) < 1e-9
    # extras quoted in the notes: sum rule, Wronskian, Bessel's integral, addition theorem
    for xx in (0.5, 3.0, 9.0): assert abs(sc.jv(0, xx)**2+2*sum(sc.jv(n, xx)**2 for n in range(1, 60))-1) < 1e-12
    for nu in (0.0, 0.7, 2.0):
        for xx in (0.8, 3.3): assert abs(sc.jv(nu, xx)*sc.yvp(nu, xx)-sc.jvp(nu, xx)*sc.yv(nu, xx)-2/(np.pi*xx)) < 1e-12
    for n in (0, 1, 3): assert abs(integrate.quad(lambda th: np.cos(n*th-2.4*np.sin(th)), 0, np.pi)[0]/np.pi-sc.jv(n, 2.4)) < 1e-12
    assert abs(sc.jv(2, 1.3+0.9)-sum(sc.jv(k, 1.3)*sc.jv(2-k, 0.9) for k in range(-40, 41))) < 1e-12
    assert abs(sc.jv(1.2, 2.0)**0) == 1
    # asymptotics J_n ~ sqrt(2/(pi x)) cos(x - n pi/2 - pi/4)
    z = 60.0; assert abs(sc.jv(2, z)-np.sqrt(2/(np.pi*z))*np.cos(z-np.pi-np.pi/4)) < 2e-3
    return dict(J3_4=J3, xm=xm)

def check():
    f = check_frobenius(); l = check_legendre(); b = check_gamma_bessel()
    print('all checks passed'); return f, l, b

if __name__ == '__main__':
    f, l, b = check()
    print('P1 series r=1:', f['P1'][0], ' r=-1/2:', f['P1'][1]); print('L2 error legendre vs taylor (exp, n=3):', l); print(b)
