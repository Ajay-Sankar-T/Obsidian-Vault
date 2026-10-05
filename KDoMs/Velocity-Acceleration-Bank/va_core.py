"""Analytical velocity / acceleration analysis (Ghosh & Mallik, Ch. 2: Secs 2.2, 2.3, 2.9) + finite-difference self-checks."""
import numpy as np
from math import *

# ---------------- four-bar (Fig. 2.4): l1 frame, l2 crank, l3 coupler, l4 follower; angles CCW from the frame -----------------
def fb_theta4(l, th2, mode=+1):
    """(2.3)-(2.4): a sin(th4) + b cos(th4) = c ; mode = +1 / -1 picks the two assembly modes. Returns th4 or None"""
    l1, l2, l3, l4 = l
    a = sin(th2); b = cos(th2)-l1/l2; c = -(l1/l4)*cos(th2)+(l1*l1+l2*l2+l4*l4-l3*l3)/(2*l2*l4)
    disc = a*a+b*b-c*c
    if disc < 0: return None
    return 2*atan2(a+mode*sqrt(disc), b+c)

def fb_state(l, th2, w2=1.0, a2=0.0, mode=+1):
    l1, l2, l3, l4 = l
    th4 = fb_theta4(l, th2, mode)
    if th4 is None: return None
    th3 = atan2(l2*sin(th2)-l4*sin(th4), l2*cos(th2)-l1-l4*cos(th4))          # from (2.2a,b)
    s34 = sin(th3-th4)
    w3 = w2*l2*sin(th2-th4)/(l3*s34)                                           # (2.33) solved
    w4 = w2*l2*sin(th2-th3)/(l4*sin(th4-th3))
    al3 = (l2*a2*sin(th2-th4)+l2*w2**2*cos(th2-th4)-l4*w4**2-l3*w3**2*cos(th3-th4))/(l3*s34)       # (2.34) solved
    al4 = (l2*a2*sin(th2-th3)+l2*w2**2*cos(th2-th3)-l3*w3**2-l4*w4**2*cos(th4-th3))/(l4*sin(th4-th3))
    return dict(th2=th2, th3=th3, th4=th4, w2=w2, w3=w3, w4=w4, a2=a2, a3=al3, a4=al4)

def vec(r, th): return r*np.array([cos(th), sin(th)])
def perp(v): return np.array([-v[1], v[0]])
def point_kin(r, th, w, al):
    """position, velocity, acceleration of the tip of a rotating vector r e^{i th}:  V = w x r, a = al x r - w^2 r  (2.16, 2.17)"""
    p = vec(r, th); return p, w*perp(p), al*perp(p)-w*w*p

# ---------------- offset slider-crank: l2 e^{i th2} + l3 e^{i th3} = s + i e  (derived by the same method as Sec. 2.9) ----------
def sc_state(l2, l3, e, th2, w2=1.0, a2=0.0, mode=+1):
    sin3 = (e-l2*sin(th2))/l3
    if abs(sin3) > 1: return None
    th3 = asin(sin3) if mode > 0 else pi-asin(sin3); c3 = cos(th3)
    s = l2*cos(th2)+l3*c3
    w3 = -l2*w2*cos(th2)/(l3*c3); sd = -l2*w2*sin(th2)-l3*w3*sin(th3)
    al3 = (-l2*a2*cos(th2)+l2*w2**2*sin(th2)+l3*w3**2*sin(th3))/(l3*c3)
    sdd = -l2*a2*sin(th2)-l2*w2**2*cos(th2)-l3*al3*sin(th3)-l3*w3**2*cos(th3)
    return dict(th2=th2, th3=th3, s=s, w3=w3, sd=sd, a3=al3, sdd=sdd)

# ---------------- slotted-lever quick-return (Fig. 2.9, Problem 2.19): (2.10), (2.11), (e), (f) and the second derivatives -------------
def sl_state(l1, l2, th2, w2=1.0, a2=0.0):
    s4 = sqrt(l1*l1+l2*l2+2*l1*l2*sin(th2)); th4 = atan2(l1+l2*sin(th2), l2*cos(th2))          # (2.10), (2.11)
    w4 = l2*w2*cos(th4-th2)/s4; sd = l2*w2*sin(th4-th2)                                       # (e), (f)
    a4 = (l2*a2*cos(th4-th2)+l2*w2**2*sin(th4-th2)-2*sd*w4)/s4                                # second derivative (left as exercise in the book)
    sdd = s4*w4**2+l2*a2*sin(th4-th2)-l2*w2**2*cos(th4-th2)
    return dict(th2=th2, s4=s4, th4=th4, w4=w4, sd=sd, a4=a4, sdd=sdd)

# ---------------- generic finite-difference helper -------------------------------------------------------------------------
def fd(fun, t, h=1e-4):
    f0, fp, fm = fun(t), fun(t+h), fun(t-h); return (fp-fm)/(2*h), (fp-2*f0+fm)/(h*h)

def check():
    # 4R: th2(t) = th0 + w t + a t^2/2 ; compare analytic th3', th4', th3'', th4'' with finite differences of the displacement solution
    l = (5.5, 1.7, 5.5, 4.08); th0, w, al = 0.9, 2.3, -1.4
    th2 = lambda t: th0+w*t+.5*al*t*t
    for mode in (+1, -1):
        for t0 in (0.0, 0.31, 0.77):
            st = fb_state(l, th2(t0), w+al*t0, al, mode)
            if st is None: continue
            for key, ang in (("th3", lambda t: fb_state(l, th2(t), 1, 0, mode)["th3"]), ("th4", lambda t: fb_theta4(l, th2(t), mode))):
                # unwrap through small steps is not needed: the step is tiny
                d1, d2 = fd(ang, t0)
                assert abs(d1-st["w"+key[-1]]) < 1e-5 and abs(d2-st["a"+key[-1]]) < 1e-3, (mode, t0, key, d1, st["w"+key[-1]], d2, st["a"+key[-1]])
    # loop closure holds
    st = fb_state(l, 1.1); chk = l[0]+l[3]*cos(st["th4"])+l[2]*cos(st["th3"])-l[1]*cos(1.1); assert abs(chk) < 1e-12
    # book (2.33)/(2.34)-type linear equations are satisfied
    th3, th4, th2_, w2, a2 = st["th3"], st["th4"], 1.1, 1.0, 0.0
    assert abs(l[3]*sin(th4)*st["w4"]+l[2]*sin(th3)*st["w3"]-l[1]*sin(th2_)*w2) < 1e-12
    assert abs(l[3]*cos(th4)*st["w4"]+l[2]*cos(th3)*st["w3"]-l[1]*cos(th2_)*w2) < 1e-12
    # slider-crank
    for mode in (+1, -1):
        for t0 in (0.1, 0.5):
            st = sc_state(2.0, 6.0, 0.8, th2(t0), w+al*t0, al, mode)
            for key, f in (("s", lambda t: sc_state(2.0, 6.0, 0.8, th2(t), 1, 0, mode)["s"]), ("th3", lambda t: sc_state(2.0, 6.0, 0.8, th2(t), 1, 0, mode)["th3"])):
                d1, d2 = fd(f, t0); v, a = ("sd", "sdd") if key == "s" else ("w3", "a3")
                assert abs(d1-st[v]) < 1e-5 and abs(d2-st[a]) < 1e-3, (key, d1, st[v], d2, st[a])
    # slotted lever + Coriolis relation  a_A(crank pin) = a_P4 + a_rel + a_cor
    l1, l2 = 3.0, 5.0
    for t0 in (0.0, 0.4):
        st = sl_state(l1, l2, th2(t0), w+al*t0, al)
        for key, f, v, a in (("s4", lambda t: sl_state(l1, l2, th2(t), 1, 0)["s4"], "sd", "sdd"), ("th4", lambda t: sl_state(l1, l2, th2(t), 1, 0)["th4"], "w4", "a4")):
            d1, d2 = fd(f, t0); assert abs(d1-st[v]) < 1e-5 and abs(d2-st[a]) < 1e-3, (key, d1, st[v], d2, st[a])
        s, th4_, w4, a4, sd, sdd = st["s4"], st["th4"], st["w4"], st["a4"], st["sd"], st["sdd"]
        _, _, aA = point_kin(l2, th2(t0), w+al*t0, al)                                  # crank pin, absolute
        aP4 = a4*perp(vec(s, th4_))-w4**2*vec(s, th4_)                                  # coincident point on link 4
        arel = sdd*np.array([cos(th4_), sin(th4_)]); acor = 2*w4*sd*perp(np.array([cos(th4_), sin(th4_)]))   # 2 w x V_rel  (2.19)
        assert np.allclose(aA, aP4+arel+acor, atol=1e-9), (aA, aP4+arel+acor)
    print("velocity/acceleration checks passed")

if __name__ == "__main__": check()
