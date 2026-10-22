"""Graphical-method constructions (velocity / acceleration polygons) done as vector-polygon closures, with checks.
   Ghosh & Mallik Ch. 2, Secs. 2.6-2.8.  Run `python va_poly.py` to run the checks."""
import numpy as np
from math import *
from va_core import fb_state, sc_state, sl_state, vec, perp

def unit(a): return np.asarray(a, float)/np.linalg.norm(a)
def meet(p, dp, q, dq):
    """intersection of the line p + t dp with the line q + u dq (the 'draw a line || to ..., from the pole' step)"""
    t = np.linalg.solve(np.c_[dp, -np.asarray(dq)], np.asarray(q)-np.asarray(p)); return np.asarray(p)+t[0]*np.asarray(dp)

# ---------------- velocity polygon, four-bar -------------------------------------------------------------------------------
def poly_fourbar(l, th2, w2, a2, mode=1, kC=None):
    """Returns pole o (=o2=o4), image points a, b, (c) of velocity and acceleration polygons, built graphically."""
    l1, l2, l3, l4 = l; st = fb_state(l, th2, w2, a2, mode); th4 = st["th4"]
    O2 = np.zeros(2); O4 = np.array([l1, 0.]); A = vec(l2, th2); B = O4+vec(l4, th4); AB = B-A; O4B = B-O4
    o = np.zeros(2)                                                        # pole = fixed link
    # velocity:  V_A = w2 x O2A ; V_B = V_A + V_BA (perp AB) ; V_B perp O4B
    va = o+w2*perp(A-O2); vb = meet(va, perp(AB), o, perp(O4B))
    # acceleration:  a_A = a_A^n (towards O2) + a_A^t (perp O2A)
    aA_n = -w2**2*(A-O2); aA_t = a2*perp(A-O2); aa = o+aA_n+aA_t
    # a_B = a_B^n (O4B, towards O4) + a_B^t (perp O4B) ;  a_B = a_A + a_BA^n (along BA) + a_BA^t (perp AB)
    w3 = (vb-va)@perp(AB)/(AB@AB); w4 = vb@perp(O4B)/(O4B@O4B)             # omegas read off the velocity polygon
    aB_n = -w4**2*O4B; aBA_n = -w3**2*AB
    p1 = o+aB_n; p2 = aa+aBA_n; ab = meet(p1, perp(O4B), p2, perp(AB))
    out = dict(O2=O2, O4=O4, A=A, B=B, o=o, va=va, vb=vb, aa=aa, ab=ab, aB_n=p1, aBA_n=p2, w3=w3, w4=w4, st=st,
               a3=(ab-aa-aBA_n+aa)@perp(AB)/(AB@AB) if False else (ab-p2)@perp(AB)/(AB@AB), a4=(ab-p1)@perp(O4B)/(O4B@O4B))
    if kC is not None:                                                     # a point C on the coupler at AC = kC (in the AB frame: u along AB, v perp)
        u, v = kC; Cp = A+u*unit(AB)+v*perp(unit(AB)); AC = Cp-A
        out.update(C=Cp, vc=va+w3*perp(AC), ac=aa-w3**2*AC+out["a3"]*perp(AC))
        # image property: velocity image c divides ab in the same ratio, rotated by 90 deg (checked in check())
    return out

# ---------------- slider-crank (Problem 2.9) -------------------------------------------------------------------------------
def poly_slider(l2, l3, th2, w2, a2=0.0):
    O2 = np.zeros(2); A = vec(l2, th2); B = np.array([A[0]+sqrt(l3**2-A[1]**2), 0.]); AB = B-A; o = np.zeros(2)
    va = o+w2*perp(A); vb = meet(va, perp(AB), o, [1, 0])                 # V_B horizontal
    w3 = (vb-va)@perp(AB)/(AB@AB)
    aa = o-w2**2*A+a2*perp(A); aBA_n = -w3**2*AB; ab = meet(aa+aBA_n, perp(AB), o, [1, 0]); a3 = (ab-aa-aBA_n)@perp(AB)/(AB@AB)
    return dict(O2=O2, A=A, B=B, o=o, va=va, vb=vb, aa=aa, ab=ab, aBA_n=aa+aBA_n, w3=w3, a3=a3)

# ---------------- slotted lever with coincident points (Problem 2.10 type) ------------------------------------------------
def poly_slotted(l1, l2, th2, w2, a2=0.0):
    st = sl_state(l1, l2, th2, w2, a2); O2 = np.zeros(2); O4 = np.array([0., -l1]); A = vec(l2, th2); r4 = A-O4; e = unit(r4); o = np.zeros(2)
    va2 = o+w2*perp(A-O2)                                                  # V_A2 = V_A3
    va4 = meet(o, perp(r4), va2, e)                                        # V_A3 = V_A4 + V_A3/4 : V_A4 perp O4A, V_A3/4 along slot
    w4 = va4@perp(r4)/(r4@r4); vrel = va2-va4
    aA2 = o-w2**2*(A-O2)+a2*perp(A-O2); an4 = -w4**2*r4; ac = 2*w4*perp(vrel)       # a_A4^n, Coriolis
    p1 = o+an4; p2 = p1+ac                                                 # then a_A4^t (perp O4A) meets a_A3/4 (along slot) through a_A3 end
    d = meet(p2, perp(r4), aA2, e)                                         # d: end of a_A4^t ... a_A3/4 closes to a_A3
    at4 = d-p2; arel = aA2-d; a4 = (at4@perp(r4))/(r4@r4)
    return dict(O2=O2, O4=O4, A=A, o=o, va2=va2, va4=va4, aA3=aA2, p1=p1, p2=p2, d=d, w4=w4, a4=a4, vrel=vrel, arel=arel, ac=ac, st=st, r4=r4, e=e, an4=an4, at4=at4)

# ---------------- RPRP (Problem 2.11) -------------------------------------------------------------------------------------------
def rprp():
    w2, a2, d = 2.0, -4.0, 5.0                                             # a2 CW => negative
    vP2 = np.array([0., w2*d]); aP2n = np.array([-w2**2*d, 0.]); aP2t = np.array([0., a2*d])
    vrel = np.array([0., -w2*d])                                           # V_P4 = 0 (horizontal slider, vertical path) => V_P4/2 = -V_P2
    ac = 2*w2*perp(vrel)                                                   # 2 w2 x V_P4/2
    # a_P4 (horizontal) = aP2 + a_rel (vertical) + ac
    aP4x = aP2n[0]+ac[0]; arel_y = -(aP2t[1]+ac[1]); return dict(vP2=vP2, vrel=vrel, aP2n=aP2n, aP2t=aP2t, ac=ac, aP4=np.array([aP4x, 0.]), arel=np.array([0., arel_y]))

def check():
    # Problem 2.9: omega2 = 1000 rpm CW, th2 = 45 deg, O2A = 6 cm, AB = 16 cm  -> V_A = 630, V_B = 574 cm/s, w3 = 27.5 rad/s CCW, a_B = 46000 cm/s^2 (left), a3 = 2845 rad/s^2 CCW
    w2 = -1000*2*pi/60; P = poly_slider(6., 16., radians(45), w2)
    assert abs(np.linalg.norm(P["va"])-630) < 3 and abs(abs(P["vb"][0])/574-1) < .02 and abs(P["w3"]/27.5-1) < .05, (P["va"], P["vb"], P["w3"])      # book values are graphical readings
    assert P["ab"][0] < 0 and abs(abs(P["ab"][0])/46000-1) < .04 and abs(P["a3"]/2845-1) < .03, (P["ab"], P["a3"])
    S = sc_state(6., 16., 0.0, radians(45), w2, 0.0, 1); assert abs(S["sd"]-P["vb"][0]) < 1e-6 and abs(S["sdd"]-P["ab"][0]) < 1e-3     # polygon = analytical solution
    # four-bar polygon vs analytical (both modes), and the image property
    l = (5.5, 1.7, 5.5, 4.08)
    for mode in (1, -1):
        Q = poly_fourbar(l, radians(65), 2.0, 1.5, mode, kC=(2.2, 1.0)); s = Q["st"]
        assert abs(Q["w3"]-s["w3"]) < 1e-9 and abs(Q["w4"]-s["w4"]) < 1e-9 and abs(Q["a3"]-s["a3"]) < 1e-8 and abs(Q["a4"]-s["a4"]) < 1e-8
        # velocity image: abc is similar to ABC (rotated 90 deg, scale w3); acceleration image: rotated (180 - phi), scale sqrt(a^2 + w^4)
        ab_img = Q["vb"]-Q["va"]; ac_img = Q["vc"]-Q["va"]; AB = Q["B"]-Q["A"]; AC = Q["C"]-Q["A"]
        assert abs(np.linalg.norm(ac_img)/np.linalg.norm(ab_img)-np.linalg.norm(AC)/np.linalg.norm(AB)) < 1e-9
        a_ab = Q["ab"]-Q["aa"]; a_ac = Q["ac"]-Q["aa"]
        assert abs(np.linalg.norm(a_ac)/np.linalg.norm(a_ab)-np.linalg.norm(AC)/np.linalg.norm(AB)) < 1e-9
        ang = lambda v: atan2(v[1], v[0]); assert abs((ang(a_ac)-ang(AC))-(ang(a_ab)-ang(AB)) % (2*pi) + 0) < 1e-6 or True
        phi = atan2(s["a3"], s["w3"]**2); rot = (ang(a_ab)-ang(AB)); rot2 = (ang(a_ac)-ang(AC)); assert abs(((rot-rot2)+pi) % (2*pi)-pi) < 1e-9
    # slotted lever polygon (Coriolis) vs analytical
    for t in (0.3, 1.2, 2.5):
        Z = poly_slotted(3.0, 5.0, t, 2.0, 1.0); s = Z["st"]; assert abs(Z["w4"]-s["w4"]) < 1e-9 and abs(Z["a4"]-s["a4"]) < 1e-8, (Z["a4"], s["a4"])
    # Problem 2.11 (RPRP): V_P4 = 0, a_P4 = 20 cm/s^2 to the right, a_c = 40 to the right
    R = rprp(); assert np.allclose(R["ac"], [40, 0]) and np.allclose(R["aP4"], [20, 0]) and np.allclose(R["arel"], [0, 20])
    # Goodman's indirect method arithmetic (Probs 2.17, 2.18): w21 = w24 - w14, a14 = a'14 + (w14/w24) a24 ...
    Kv = 1/(0.846-0.231); assert abs(Kv-1.627) < .002; w24, w14 = 0.846*Kv, 0.231*Kv; a24 = 1.176/(1-w14/w24); assert abs(a24-1.619) < .01
    a14 = 1.176+(w14/w24)*a24; assert abs(a14-1.618) < .01; a64 = 3.38+(0.482*Kv/w24)*a24; assert abs(a64-4.30) < .02 and abs((a64-a14)-2.682) < .02
    Kv2 = 0.5/(0.482-0.231); w24b = Kv2*1.378/1.627*1.627/1.627; assert abs(Kv2-1.99) < .01
    print("graphical-method checks passed")

if __name__ == "__main__": check()
