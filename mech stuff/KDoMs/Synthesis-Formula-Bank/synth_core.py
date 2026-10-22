"""Dimensional-synthesis helpers (Ghosh & Mallik, Ch. 3: motion generation, path generation) + self-checks."""
import numpy as np
from math import *

def R(a): return np.array([[cos(a), -sin(a)], [sin(a), cos(a)]])
def circumcenter(p1, p2, p3):
    ax, ay = p1; bx, by = p2; cx, cy = p3
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
    uy = ((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
    return np.array([ux, uy])

# ---- motion generation: coupler poses (x, y, phi) ---------------------------------------------
def to_world(pose, q): x, y, ph = pose; return R(ph)@np.asarray(q, float)+np.array([x, y])
def to_body(pose, w): x, y, ph = pose; return R(-ph)@(np.asarray(w, float)-np.array([x, y]))
def motion_free(poses, a_body, b_body):
    """Two coupler points A, B (body coords) -> ground pivots O2, O4 = circumcentres of their 3 positions."""
    A = [to_world(p, a_body) for p in poses]; B = [to_world(p, b_body) for p in poses]
    return circumcenter(*A), circumcenter(*B)
def inverted_positions(poses, O):
    """Kinematic inversion: pivot O seen from the coupler held fixed in position 1."""
    return [to_world(poses[0], to_body(p, O)) for p in poses]
def motion_pivots(poses, O2, O4):
    """Given pivots: hinge positions A1, B1 (world, pose 1) = circle centres of the inverted pivot positions."""
    return circumcenter(*inverted_positions(poses, O2)), circumcenter(*inverted_positions(poses, O4))

# ---- path generation by inversion (3 positions of coupler point C) -----------------------------
def circle_circle(c0, r0, c1, r1, near):
    d = np.linalg.norm(c1-c0); a = (r0*r0-r1*r1+d*d)/(2*d); h = sqrt(max(r0*r0-a*a, 0))
    m = c0+a*(c1-c0)/d; n = np.array([-(c1-c0)[1], (c1-c0)[0]])/d
    P = [m+h*n, m-h*n]; return min(P, key=lambda p: np.linalg.norm(p-near))
def path_gen3(C, O2, O4, B1):
    """C = [C1,C2,C3]; O2, O4, B1 chosen.  Returns A1, coupler poses (mapping pose 1 -> pose k), and B_k."""
    C = [np.asarray(c, float) for c in C]; O2 = np.asarray(O2, float); O4 = np.asarray(O4, float); B1 = np.asarray(B1, float)
    rB = np.linalg.norm(B1-O4); bc = np.linalg.norm(C[0]-B1)
    Bk = [B1]
    for k in (1, 2): Bk.append(circle_circle(O4, rB, C[k], bc, Bk[-1]))
    ang0 = atan2(*(C[0]-Bk[0])[::-1]); poses = []
    for k in range(3):
        ph = atan2(*(C[k]-Bk[k])[::-1])-ang0
        t = C[k]-R(ph)@C[0]; poses.append((t[0], t[1], ph))
    inv_pts = [to_body(p, O2) for p in poses]               # O2 seen from the coupler fixed in position 1
    return circumcenter(*inv_pts), poses, Bk
def move(pose, w): x, y, ph = pose; return R(ph)@np.asarray(w, float)+np.array([x, y])

# ---- poles ---------------------------------------------------------------------------------------
def pole(A1, A2, B1, B2):
    """pole P12 = intersection of the perpendicular bisectors of A1A2 and B1B2"""
    def bis(P, Q): m = (P+Q)/2; d = Q-P; return m, np.array([-d[1], d[0]])
    (m1, n1), (m2, n2) = bis(A1, A2), bis(B1, B2)
    t = np.linalg.solve(np.c_[n1, -n2], m2-m1); return m1+t[0]*n1
def ang(P, Q, S):
    """signed angle Q-P-S, CCW from PQ to PS, in (-pi, pi]"""
    a = atan2(*(S-P)[::-1])-atan2(*(Q-P)[::-1]); return (a+pi) % (2*pi)-pi

# ---- four-bar kinematics (verification and coupler curves) -----------------------------------------
def fourbar(O2, O4, l2, l3, l4, th2, branch=1):
    A = O2+l2*np.array([cos(th2), sin(th2)]); d = np.linalg.norm(O4-A)
    if d > l3+l4 or d < abs(l3-l4): return None
    a = (l3*l3-l4*l4+d*d)/(2*d); h = sqrt(max(l3*l3-a*a, 0)); m = A+a*(O4-A)/d; n = np.array([-(O4-A)[1], (O4-A)[0]])/d
    return A, m+branch*h*n
def coupler_point(A, B, u, v):
    """coupler point at u along AB and v perpendicular (CCW) from A"""
    e = (B-A)/np.linalg.norm(B-A); return A+u*e+v*np.array([-e[1], e[0]])
def coupler_curve(O2, O4, l2, l3, l4, u, v, branch=1, n=1440):
    pts = []
    for t in np.linspace(0, 2*pi, n):
        r = fourbar(O2, O4, l2, l3, l4, t, branch)
        pts.append(coupler_point(*r, u, v) if r else (np.nan, np.nan))
    return np.array(pts)

# ---- dyads (3.18) --------------------------------------------------------------------------------
def dyad_solve(delta, th2, th3):
    """L(e^{i th2_j}-1) + L*(e^{i th3_j}-1) = delta_j,  j = 2,3  (3.20a,b)  ->  L, L*"""
    M = np.array([[np.exp(1j*th2[j])-1, np.exp(1j*th3[j])-1] for j in range(2)]); return np.linalg.solve(M, np.asarray(delta, complex))

# ---- analytic function generators ----------------------------------------------------------------
def chebyshev(xi, xf, k): a, h = (xi+xf)/2, (xf-xi)/2; return [a+h*cos((2*l-1)*pi/(2*k)) for l in range(1, k+1)]
def freudenstein_K(pairs):
    """pairs [(th2, th4)] in rad -> K1,K2,K3 from cos(th2-th4) = K1 cos th4 - K2 cos th2 + K3   (3.6)"""
    M = np.array([[cos(t4), -cos(t2), 1] for t2, t4 in pairs]); b = np.array([cos(t2-t4) for t2, t4 in pairs]); return np.linalg.solve(M, b)
def slider_K(pairs):
    """pairs [(th2, s)] -> K1,K2,K3 from K1 s cos th2 + K2 sin th2 - K3 = s^2   (3.8)"""
    M = np.array([[s*cos(t), sin(t), -1] for t, s in pairs]); b = np.array([s*s for t, s in pairs]); return np.linalg.solve(M, b)

def slider4(th, spp):
    """4 accuracy points (3.9)-(3.15).  th = [theta_l] (rad), spp = [s''_l] (known part of the slider displacement, s_l = s^i + s''_l).
    Returns the (up to two) solutions [(l2, l3, l4, s^i)]."""
    th = np.asarray(th, float); spp = np.asarray(spp, float)
    M = np.c_[np.cos(th), spp*np.cos(th), np.sin(th), -np.ones(4)]
    Pv = np.linalg.solve(M, spp); Qv = np.linalg.solve(M, spp**2)           # (3.13a), (3.13b)
    a, b, c = Pv[1], Qv[1]-2*Pv[0], -2*Qv[0]                                  # (3.15)  A^2 P2 + (Q2 - 2 P1) A - 2 Q1 = 0
    disc = b*b-4*a*c; out = []
    if disc < 0: return out
    for A in sorted({(-b+e*sqrt(disc))/(2*a) for e in (1, -1)}):
        R1, R2, R3, R4 = Qv+A*Pv; R5 = A                                       # (3.14)
        l2 = R2/2; si = R5/2; l4 = R3/R2; l3 = sqrt(l2*l2+l4*l4+si*si-R4); out.append((l2, l3, l4, si))
    return out

def check():
    # Problem 3.5   y = log10 x on 1..10, th2 = 45 + (60/9)(x-1), th4 = 135 + 90 y
    xs = chebyshev(1, 10, 3); assert np.allclose(xs, [9.4, 5.5, 1.6], atol=.06), xs
    th2 = [45+60/9*(x-1) for x in xs]; th4 = [135+90*log10(x) for x in xs]
    K = freudenstein_K([(radians(a), radians(b)) for a, b in zip(th2, th4)]); assert np.allclose(K, [2, -0.703, 1.078], atol=.03), K
    l2 = 5; l1 = K[0]*l2; l4 = l1/K[1]; l3 = sqrt(l1*l1+l2*l2+l4*l4-2*l2*l4*K[2])
    assert abs(l1-10) < .1 and abs(l4+14.2) < .2 and abs(l3-21.85) < .2, (l1, l3, l4)
    # Problem 3.6 (book's accuracy points 128.7, 90, 51.3 deg)
    K = slider_K([(radians(128.7), 3.95), (radians(90), 8.26), (radians(51.3), 9.97)]); assert np.allclose(K, [9.61, 130.75, 62.75], rtol=.01), K
    l2 = K[0]/2; l4 = K[1]/(2*l2); l3 = sqrt(l2*l2+l4*l4-K[2]); assert abs(l2-4.805) < .02 and abs(l4-13.6) < .1 and abs(l3-12.05) < .05, (l2, l4, l3)
    # Problem 3.7: instantaneous conditions
    th2, th4, w2, w4, a2, a4 = radians(60), radians(90), 3, 2, -1, 0
    M = np.array([[cos(th4), -cos(th2), 1], [w4*sin(th4), -w2*sin(th2), 0], [a4*sin(th4)+w4**2*cos(th4), -(a2*sin(th2)+w2**2*cos(th2)), 0]])
    b = np.array([cos(th2-th4), (w2-w4)*sin(th2-th4), (a2-a4)*sin(th2-th4)+(w2-w4)**2*cos(th2-th4)])
    K = np.linalg.solve(M, b); assert np.allclose(K, [-.738, -.376, .678], atol=.002), K
    # motion generation, 3 poses: circumcentres, then inversion with those pivots must return the same hinges
    poses = [(0, 0, 0), (3, 2, .5), (5, 1, 1.1)]; a_b, b_b = (0, 0), (4, 0)
    O2, O4 = motion_free(poses, a_b, b_b)
    A = [to_world(p, a_b) for p in poses]; B = [to_world(p, b_b) for p in poses]
    assert all(abs(np.linalg.norm(a-O2)-np.linalg.norm(A[0]-O2)) < 1e-9 for a in A)
    assert all(abs(np.linalg.norm(b-O4)-np.linalg.norm(B[0]-O4)) < 1e-9 for b in B)
    A1, B1 = motion_pivots(poses, O2, O4); assert np.allclose(A1, A[0], atol=1e-8) and np.allclose(B1, B[0], atol=1e-8)
    # path generation by inversion: A_k stays on a circle about O2, B_k on a circle about O4
    Cp = [(0, 0), (3, 1), (6, 0)]; O2 = np.array([-3., -4.]); O4 = np.array([4., -4.]); B1 = np.array([0., -3.])
    A1, poses, Bk = path_gen3(Cp, O2, O4, B1); Ak = [move(p, A1) for p in poses]
    assert all(abs(np.linalg.norm(a-O2)-np.linalg.norm(Ak[0]-O2)) < 1e-9 for a in Ak)
    assert all(abs(np.linalg.norm(b-O4)-np.linalg.norm(Bk[0]-O4)) < 1e-9 for b in Bk)
    # poles: P12 sees A1A2 and B1B2 under the coupler rotation theta12
    th = .6; Pc = np.array([1., 3.]); mv = lambda p: Pc+R(th)@(p-Pc)
    A1, B1 = np.array([0., 0]), np.array([4., 0]); P12 = pole(A1, mv(A1), B1, mv(B1)); assert np.allclose(P12, Pc, atol=1e-9)
    assert abs(ang(P12, A1, mv(A1))-th) < 1e-9 and abs(ang(P12, B1, mv(B1))-th) < 1e-9
    # dyad standard form (3.18) recovers a known pair
    L, Ls = 1.3+.4j, .7-1.1j; t2 = [.5, 1.0]; t3 = [.8, -.3]
    d = [L*(np.exp(1j*a)-1)+Ls*(np.exp(1j*b)-1) for a, b in zip(t2, t3)]; assert np.allclose(dyad_solve(d, t2, t3), [L, Ls])
    # Peaucellier: P on a circle through O, OP*OQ = OA^2 - AP^2  =>  Q lies on the line x = k/(2 r)
    OA, AP, r = 5., 2., 2.5; k = OA**2-AP**2
    for t in np.linspace(-1.2, 1.2, 5):
        Pp = r*np.array([1+cos(2*t), sin(2*t)]); Q = Pp/np.dot(Pp, Pp)*k; assert abs(Q[0]-k/(2*r)) < 1e-9
    # four-accuracy-point slider-crank (3.9)-(3.15): recover a known mechanism
    l2t, l3t, l4t, sit = 2.0, 5.0, 1.2, 7.0; ths = np.radians([20, 55, 100, 140])
    st = l2t*np.cos(ths)+np.sqrt(l3t**2-(l2t*np.sin(ths)-l4t)**2); sols = slider4(ths, st-sit)
    assert any(np.allclose(x, (l2t, l3t, l4t, sit), atol=1e-6) for x in sols), sols
    print("synthesis checks passed")

if __name__ == "__main__": check()
