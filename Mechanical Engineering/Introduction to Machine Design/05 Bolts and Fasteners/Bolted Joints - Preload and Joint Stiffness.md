---
tags: [concept, machine-design]
course: "Introduction to Machine Design (ME3203)"
aliases: [Bolted joint, Preload, Joint stiffness factor, Bolt stiffness, Member stiffness, Joint separation, Dowel pins]
---

# Bolted Joints — Preload and Joint Stiffness

> [!abstract] In one breath
> A tightened bolt is a **spring stretched against the clamped members, which are a much stiffer spring compressed**. When the joint is loaded, the **bolt takes only the fraction $C=k_b/(k_b+k_m)$ of the external load** and the members give up the rest of their squeeze. Tighten the bolt well, and the bolt barely feels the load until the joint separates.

Part of [[Introduction to Machine Design - MOC]]. Previous: [[Helical Springs]].

## 1. Nomenclature

Nominal (major) diameter $d$, pitch $p$, tensile-stress area $A_t$ (the effective area of the threaded section; M12×1.75: 84.3 mm²), proof strength $S_p$ (about 85–90 % of yield: grade 8.8 has $S_p=600$, $S_y=640$, $S_{ut}=800$ MPa), grip $l$ (total thickness clamped).

## 2. Stiffness

**Bolt** (unthreaded shank $l_d$ in series with the threaded part $l_t$ inside the grip):

$$
k_b=\frac{A_dA_tE}{A_dl_t+A_tl_d}
$$

**Members** (Shigley's frustum method, with a 30° cone from under the head, same material):

$$
k_m=\frac{0.5774\,\pi E d}{2\ln\Big[5\,\dfrac{0.5774\,l+0.5d}{0.5774\,l+2.5d}\Big]}
$$

**Joint stiffness factor** (fraction of the external load carried by the bolt):

$$
C=\frac{k_b}{k_b+k_m}
$$

Typically $C=0.1$–$0.3$ because the members are stiffer than the bolt.

## 3. Load analysis

Let $F_i$ be the preload and $P$ the external tensile load per bolt:

$$
F_b=F_i+CP,\qquad F_m=F_i-(1-C)P\quad(F_m\ \text{is the clamp force})
$$

The joint **separates** when $F_m=0$: $P_0=F_i/(1-C)$. Recommended preload: $F_i=0.75\,S_pA_t$ for reusable joints, $0.90\,S_pA_t$ for permanent ones.

**Safety factors** (static):

$$
n_p=\frac{S_pA_t}{F_b}\ (\text{proof}),\qquad n_L=\frac{S_pA_t-F_i}{CP}\ (\text{load}),\qquad n_0=\frac{F_i}{(1-C)P}\ (\text{separation})
$$

**Fatigue.** The load cycles from 0 to $P$, so the bolt stress alternates by $\sigma_a=CP/2A_t$ about a mean $\sigma_m=\sigma_a+F_i/A_t$. Goodman, with the preload stress $\sigma_i=F_i/A_t$ (a mean stress that is constant):

$$
n_f=\frac{S_e(S_{ut}-\sigma_i)}{S_{ut}\sigma_a+S_e(\sigma_m-\sigma_i)}
$$

($S_e=129$ MPa for rolled-thread M3–M36 grade 8.8, fully corrected).

## 4. Worked example

M12×1.75 grade 8.8 bolt, grip 40 mm (shank 20 mm in the grip, thread 20 mm), steel members, external load $P=15$ kN per bolt, load cycling 0–15 kN:

| Quantity | Value |
| --- | --- |
| $k_b$ | 500 kN/mm |
| $k_m$ | 2235 kN/mm |
| **$C=k_b/(k_b+k_m)$** | **0.183** |
| preload $F_i=0.75S_pA_t$ | **37.9 kN** |
| bolt force $F_i+CP$ | 40.7 kN (+2.7 kN) |
| clamp force $F_i-(1-C)P$ | 25.7 kN (−12.3 kN) |
| separation load $P_0=F_i/(1-C)$ | **46.4 kN** |
| $n_p$, $n_L$, $n_0$ | 1.24, 4.61, 3.09 |
| $\sigma_a$, $\sigma_m$ | 16.3, 466 MPa |
| **fatigue $n_f$** | **2.99** |

The member stiffness is 4.5 times the bolt stiffness, so 82 % of the external load is relieved from the members and **only 18 % goes into the bolt**. Without preload the bolt would see all 15 kN; with preload the stress swing is just 16 MPa, which is why correctly tightened bolts survive vibration.

![[MD-6-bolt.png]]

On the left the bolt and member force–deflection lines meet at the preload; the external load moves both. On the right: bolt force rises slowly with $P$, clamp force falls fast, and the joint separates at 46 kN.

## 5. Design implications

- **Tighten more**: larger $F_i$ reduces the stress swing (it increases the mean, but the fatigue limit tolerates a high mean) and keeps the joint closed.
- **Soft bolt, stiff members**: a long, thin or reduced-shank bolt lowers $k_b$ and $C$.
- **Gaskets** soften the members, raising $C$: the bolt then carries more of the load and the preload is lost with gasket creep.
- **Shear loading**: bolts in a lap joint with friction grip transmit the load as friction $\mu F_i$; precision **dowel pins** carry the shear instead, in shear and bearing on their cross-section, so the bolts only clamp.

> [!warning] Traps
> - Using the nominal area $\pi d^2/4$ instead of $A_t$ for stress in the thread.
> - Treating the external load as going entirely to the bolt: only $CP$ does, while $(1-C)P$ comes off the members.
> - Using a very high $C$ (soft members) without checking fatigue.
> - Taking the preload as a safety factor: it is a *load*, and it can crush soft members or yield the bolt when overtightened.
> - Ignoring the torque–preload relation: $T\approx0.2F_id$ (nut factor $K\approx0.2$).

> [!question]- Predict first: a tight bolt in a stiff joint. Does the bolt's stress change much when the load is applied?
> Hardly. With $C=0.18$ the bolt stress only rises by 18 % of $P/A_t$. For a gasketed joint ($C\to0.5$) it rises by half of $P/A_t$ and fatigue becomes serious.

> [!question]- What torque gives $F_i=37.9$ kN on an M12 bolt?
> With the nut factor 0.2: $T=0.2\times37.9\ \text{kN}\times12\ \text{mm}=91$ N·m. The factor depends on lubrication (dry 0.2, oiled 0.15), so the scatter in preload for a given torque is about ±25 %.

## 6. Connections

- [[Statically Indeterminate Axial Members]] — the bolt and the members are two springs that share an external load by **compatibility**: their extra elongation and relieved compression are equal, $\Delta\delta_b=\Delta\delta_m$.
- [[Thermal Stresses]] — a temperature change alters the preload exactly like an extra load shared with the same stiffness ratio.
- [[Helical Springs]] — the same spring-stiffness language ($k=AE/L$ for the bolt).
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — the Goodman line with a constant preload offset.
- [[Computer Aided Machine Drawing - MOC]] — bolts and threads as drawn.
