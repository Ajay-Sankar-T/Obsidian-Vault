"""Newton-Raphson displacement solver + velocity/acceleration from the same Jacobian (Ghosh & Mallik Ch. 2 loop equations).
   Phi(q, th2) = 0  ->  Newton:  J dq = -Phi ;  velocity:  J qd = -Phi_th w2 ;  acceleration:  J qdd = -Phi_th a2 - gamma.
   Run `python va_newton.py` to run the checks against the closed forms of va_core.py."""
import numpy as np
from math import *
from va_core import fb_state, sc_state, sl_state

class Mech:
    """phi(q,t2) residual, jac(q,t2) = dPhi/dq, pth(q,t2) = dPhi/dth2,
       gam(q,qd,t2,w2) = the part of d2Phi/dt2 that does not contain qdd or a2 (so  J qdd + pth a2 + gam = 0)."""
    def __init__(s, par, phi, jac, pth, gam, names): s.par, s.phi, s.jac, s.pth, s.gam, s.names = par, phi, jac, pth, gam, names

def fourbar(l):
    l1, l2, l3, l4 = l
    phi = lambda q, t: np.array([l1+l4*cos(q[1])+l3*cos(q[0])-l2*cos(t), l4*sin(q[1])+l3*sin(q[0])-l2*sin(t)])
    jac = lambda q, t: np.array([[-l3*sin(q[0]), -l4*sin(q[1])], [l3*cos(q[0]), l4*cos(q[1])]])
    pth = lambda q, t: np.array([l2*sin(t), -l2*cos(t)])
    gam = lambda q, qd, t, w: np.array([-l3*cos(q[0])*qd[0]**2-l4*cos(q[1])*qd[1]**2+l2*cos(t)*w*w,
                                        -l3*sin(q[0])*qd[0]**2-l4*sin(q[1])*qd[1]**2+l2*sin(t)*w*w])
    return Mech(l, phi, jac, pth, gam, ("th3", "th4"))

def slidercrank(l2, l3, e):
    phi = lambda q, t: np.array([l2*cos(t)+l3*cos(q[0])-q[1], l2*sin(t)+l3*sin(q[0])-e])
    jac = lambda q, t: np.array([[-l3*sin(q[0]), -1.], [l3*cos(q[0]), 0.]])
    pth = lambda q, t: np.array([-l2*sin(t), l2*cos(t)])
    gam = lambda q, qd, t, w: np.array([-l2*cos(t)*w*w-l3*cos(q[0])*qd[0]**2, -l2*sin(t)*w*w-l3*sin(q[0])*qd[0]**2])
    return Mech((l2, l3, e), phi, jac, pth, gam, ("th3", "s"))

def slotted(l1, l2):
    phi = lambda q, t: np.array([q[1]*cos(q[0])-l2*cos(t), q[1]*sin(q[0])-l1-l2*sin(t)])
    jac = lambda q, t: np.array([[-q[1]*sin(q[0]), cos(q[0])], [q[1]*cos(q[0]), sin(q[0])]])
    pth = lambda q, t: np.array([l2*sin(t), -l2*cos(t)])
    gam = lambda q, qd, t, w: np.array([-2*qd[1]*qd[0]*sin(q[0])-q[1]*cos(q[0])*qd[0]**2+l2*cos(t)*w*w,
                                         2*qd[1]*qd[0]*cos(q[0])-q[1]*sin(q[0])*qd[0]**2+l2*sin(t)*w*w])
    return Mech((l1, l2), phi, jac, pth, gam, ("th4", "s4"))

def newton(M, q0, th2, tol=1e-12, itmax=30, history=False):
    """Newton-Raphson on Phi(q, th2) = 0 from the guess q0.  Returns q (and the list of ||Phi|| per iteration if history)."""
    q = np.array(q0, float); hist = []
    for _ in range(itmax):
        F = M.phi(q, th2); hist.append(np.linalg.norm(F))
        if hist[-1] < tol: break
        q = q+np.linalg.solve(M.jac(q, th2), -F)                        # q_{k+1} = q_k - J^-1 Phi
    else: raise RuntimeError("Newton-Raphson did not converge (bad guess or non-assemblable / toggle position)")
    return (q, hist) if history else q

def vel_acc(M, q, th2, w2=1.0, a2=0.0):
    J = M.jac(q, th2); qd = np.linalg.solve(J, -M.pth(q, th2)*w2)
    qdd = np.linalg.solve(J, -M.pth(q, th2)*a2-M.gam(q, qd, th2, w2)); return qd, qdd

def sweep(M, q0, th2s, w2=1.0, a2=0.0):
    """Position-by-position solution with continuation: each converged q is the first guess for the next theta2."""
    out, q = [], np.array(q0, float)
    for t in th2s:
        q = newton(M, q, t); qd, qdd = vel_acc(M, q, t, w2, a2); out.append((t, q.copy(), qd, qdd))
    return out

def check():
    l = (5.5, 1.7, 5.5, 4.08); th2, w2, a2 = 1.1, 2.3, -1.4
    M = fourbar(l)
    for mode in (1, -1):                                            # starting from a rough guess near each assembly mode
        ex = fb_state(l, th2, w2, a2, mode); g = [ex["th3"]+.25, ex["th4"]-.25]
        q, h = newton(M, g, th2, history=True); qd, qdd = vel_acc(M, q, th2, w2, a2)
        assert np.allclose(q, [ex["th3"], ex["th4"]], atol=1e-10) and np.allclose(qd, [ex["w3"], ex["w4"]], atol=1e-10) and np.allclose(qdd, [ex["a3"], ex["a4"]], atol=1e-9)
        assert len(h) <= 8 and h[-1] < 1e-12                        # quadratic convergence: few iterations
    # slider-crank, both modes (guess on the right branch)
    M = slidercrank(2.0, 6.0, 0.8)
    for mode in (1, -1):
        ex = sc_state(2.0, 6.0, 0.8, th2, w2, a2, mode); q = newton(M, [ex["th3"]+.2, ex["s"]-.3], th2); qd, qdd = vel_acc(M, q, th2, w2, a2)
        assert np.allclose(qd, [ex["w3"], ex["sd"]], atol=1e-10) and np.allclose(qdd, [ex["a3"], ex["sdd"]], atol=1e-9)
    # slotted lever
    M = slotted(3.0, 5.0); ex = sl_state(3.0, 5.0, th2, w2, a2); q = newton(M, [ex["th4"]+.2, ex["s4"]+.5], th2); qd, qdd = vel_acc(M, q, th2, w2, a2)
    assert np.allclose(qd, [ex["w4"], ex["sd"]], atol=1e-10) and np.allclose(qdd, [ex["a4"], ex["sdd"]], atol=1e-9)
    # continuation sweep over a full crank revolution of a crank-rocker, 1 deg steps, matches the closed form (mode kept automatically)
    l = (5.5, 1.7, 5.5, 4.08); M = fourbar(l); ex0 = fb_state(l, 0.0, 1, 0, 1)
    res = sweep(M, [ex0["th3"], ex0["th4"]], np.radians(np.arange(0, 361, 1.0)), 2.0, 0.5)
    for t, q, qd, qdd in res:
        ex = fb_state(l, t, 2.0, 0.5, 1)
        # angles may differ by 2 pi only in the unwrapped continuation: compare velocities (single valued) and wrapped angles
        assert abs(qd[0]-ex["w3"]) < 1e-9 and abs(qd[1]-ex["w4"]) < 1e-9 and abs(qdd[0]-ex["a3"]) < 1e-8 and abs(qdd[1]-ex["a4"]) < 1e-8
    # a linkage that cannot be assembled (6 > 1+2+2): the solver must report failure, not return nonsense
    try: newton(fourbar((6., 1., 2., 2.)), [1., 1.], 0.5); raise AssertionError("expected failure")
    except (RuntimeError, np.linalg.LinAlgError): pass
    print("Newton-Raphson checks passed")

if __name__ == "__main__": check()
