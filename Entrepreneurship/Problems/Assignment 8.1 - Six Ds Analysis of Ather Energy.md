---
title: Assignment 8.1 – Six Ds Analysis of Ather Energy
course: Innovation & Entrepreneurship for Engineers (IIT Madras)
session: M4S8B2 – Exponential & Systems Thinking
tags: [entrepreneurship, assignment, exponential-thinking, six-ds, EXPAND, ather]
source: "[[Lecture 8 - Innovation  Entrepreneurship for Engineers - M4S8B2 - 16 Oct 2026.pdf]]"
aliases: [Assignment 8.1, Ather six Ds]
---

# Assignment 8.1 – Six Ds Analysis of a Company: Ather Energy

**Batch B · Group 14**

Ajay Sankar (ME25B012) · Aadit Pankaj (EP25B001) · Aarav Prakash (CH25B002) · Yuvraj Dighe (ME25B146) · Gudditi Himesh Raghava Chandra (CS25B028)

Framework: Peter Diamandis' **6 Ds**, the **EXPAND checklist** and the **Exponential Project Canvas** from the Session 8 deck.

Related: [[Assignment 8.2 - Exponential Thinking for Our Project]] · [[Team Contribution]] · [[Case Study 1- Ather Energy.pdf]]

> [!abstract] Answer in one paragraph
> Ather has **fully leveraged Digitized** (a connected, over-the-air-updatable scooter with a paid software layer) and has **already come through the Deceptive phase** (revenue ₹79.8 Cr in FY20 → ₹3,672 Cr in FY26, ~46×). It has **partly leveraged Disruptive, Demonetized and Democratized**: it leads inside electric two-wheelers (17.4 % share in Q2 FY26) and rides a battery-price curve that fell 93 % since 2010, but petrol scooters still dominate overall volume and its vehicles are not yet mass-market priced. **Dematerialized is the D it has hardly used**: the vehicle stays a physical object, and only some functions (key, navigation, diagnostics) fold into software. The binding limits are non-exponential: capital, cell and component supply, factory capacity, service reach and safety.

---

## 1. Why Ather, and the company in brief

I chose **Ather Energy** because it is the clearest case in the deck where a *physical* product gains exponential leverage from software, charging infrastructure and a product platform (deck, Case 2), and because the course's own [[Case Study 1- Ather Energy.pdf|case study]] gives the origin and decisions to build on.

- **Founded 2013** by Tarun Mehta and Swapnil Jain, IIT Madras graduates; premium, software-defined electric scooter instead of a "petrol scooter with a battery".
- **Product:** electric scooters with a connected touchscreen dashboard, a battery management system (BMS), mobile app, OTA updates; **Ather Grid** fast chargers; **AtherStack** software; the **Rizta** family scooter and the **EL platform** for lower-cost models.
- **Manufacturing:** two plants at Hosur (about 4.2 lakh scooters/year combined) and a new plant at Bidkin, Maharashtra (about ₹2,000 Cr, planned ~10 lakh/year) taking planned capacity to about 14.2 lakh/year.
- **Listed on BSE/NSE on 6 May 2025** (issue price ₹328; ₹2,981 Cr IPO).

## 2. The evidence: what the curve looks like

![[E8-fig1-evidence.png]]
*Figure 1. Four pieces of evidence (sources in §9). Revenue is operating revenue; the FY20 and FY26 endpoints are the deck's own endpoints.*

| Metric | Value | Source type |
|---|---|---|
| Revenue from operations | ₹79.8 Cr (FY20) → ₹1,754 Cr (FY24) → ₹2,255 Cr (FY25) → ₹3,672 Cr (FY26); ~46× over FY20–FY26, ≈ 89 % a year compounded | deck slide 41; press reports of results |
| Net loss | ₹1,060 Cr (FY24) → ₹812 Cr (FY25) → ₹517 Cr (FY26) | press reports of results |
| EBITDA margin | −36 % (Q4 FY24) → −23 % (Q4 FY25) → −6.7 % (FY26) | press reports of results |
| Quarterly deliveries | 39,305 (Q2 FY25) → 65,595 (Q2 FY26), +67 % | Q2 FY26 results coverage |
| E-2W market share | 9 % (Q1 FY25) → 17.4 % (Q2 FY26); 25 % in South India | results coverage |
| Non-vehicle revenue (software, charging, spares, accessories) | ≈ 12 % of total income in Q2 FY26 | results coverage |
| Fast-charging points (Ather Grid) | 580 (Oct 2022) → 3,300+ (Jul 2025) → 5,900+ (company blog, undated) | press / company |
| Li-ion pack price (global) | $108/kWh in 2025, −93 % vs 2010 (BEV packs $99; LFP packs $81) | BloombergNEF survey |

> [!warning] Reality check (deck slide 25: "a curve needs evidence and a time horizon")
> The 46× is *company* growth from a very small base, not a law of nature. Only the end-points are used (the deck says the same: "endpoint comparison; measures and periods differ"). Operating revenue (₹3,672 Cr) and total income (₹3,823 Cr) are different numbers in different reports. The Grid count comes from an undated company blog.

## 3. The six technology laws behind Ather (deck slides 12–22)

The deck's "connected EV" example maps almost one-to-one onto Ather. The six laws are the *enabling curves*; the 6 Ds describe what happens when they converge.

| Law | Capability | Where it appears in Ather |
|---|---|---|
| Moore | compute per chip | on-board compute for the dashboard, ride modes, traction control, connected features |
| Kryder | cheaper data storage | ride logs, maps, battery and diagnostics data in the cloud |
| Koomey | compute per joule | energy-efficient edge processing, important on a battery-limited scooter |
| Nielsen | bandwidth | OTA updates, app connectivity, cloud analytics |
| Metcalfe | network value ∝ users² | charging network, community, fleet and service ecosystem |
| Wright | cost falls with cumulative output | cell and pack cost, manufacturing yield and learning at Hosur/Bidkin |

## 4. Six Ds analysis

![[E8-fig2-six-ds-scorecard.png]]
*Figure 2. Scoring is my judgement from the evidence in the table below.*

| D | Status | What Ather has done (evidence) | What it is yet to leverage |
|---|---|---|---|
| **1. Digitized** | **Leveraged** | The scooter is a connected software product: touchscreen dashboard, mobile app, BMS, cloud analytics, **OTA updates** that improve the vehicle after sale (case study). Software is monetised: AtherStack Pro attach is reported at ~89 % of owners, with software ≈ 6 % of revenue at 53–56 % EBITDA margin (press analysis). | Use the fleet data more deeply: predictive maintenance, battery-health-based warranty/financing, route and charger-aware range, personalisation. |
| **2. Deceptive** | **Leveraged** (phase passed) | 2013 founding → first deliveries years later; small volumes looked unimpressive. Now deliveries are +67 % a year and revenue ~46× since FY20. | Nothing to "leverage"; the lesson is *patience with evidence*: the next small-base curves (EL-platform models, new regions, non-vehicle revenue at ≈12 %) are the new deceptive stage. |
| **3. Disruptive** | **Partly** | Inside e-2W, Ather has crossed the threshold of performance + design + software: 17.4 % national and 25 % South India share; overtook a rival, Ola Electric, in quarterly revenue (press). | Petrol two-wheelers still dominate overall; the disruptive threshold (price, range, charging and trust together) is crossed for urban/premium riders, not yet for the mass market. |
| **4. Dematerialized** | **Not yet / limited** | Some separate physical items fold into the dashboard and app: key, navigation, trip computer, theft alert, service diagnostics. | The vehicle, battery and charger remain physical. **It would be misleading to call Ather dematerialized**; the realistic next step is converging more functions into software and the phone (digital key, voice assistant, service-at-home diagnostics). |
| **5. Demonetized** | **Partly** | The battery-price curve ($108/kWh, −93 % since 2010) lowers cost per unit; running cost per km is about an order of magnitude below petrol (illustrative estimate in §6); OTA features and software have near-zero marginal cost. | Vehicle price is far above zero. The EL platform is the demonetization move (lower cost per model through shared architecture); battery-swapping or battery-as-a-service could lower the upfront price but is not yet part of the model. |
| **6. Democratized** | **Partly / early** | Rizta (family scooter) already ≈ 57 % of FY25 volumes; expansion beyond South India (Middle India is the fastest-growing region); Grid and LECCS-standard charging open to other EVs. | Tier-3/4 towns and price-sensitive buyers; financing, resale value and service reach; apartment-dwellers without home charging. |

**Which D best explains Ather's scale mechanism?** **Digitized**, followed by **Demonetized**. Software turns a one-time sale into an improving, subscription-bearing product, and falling battery costs plus platform reuse (Rizta → EL) widen the market.

**Which D is not yet relevant or would be misleading?** **Dematerialized.** A scooter does not dematerialize; claiming it would hide the real constraints (cells, factories, service).

## 5. EXPAND checklist applied to Ather

| Letter | Question (deck) | Evidence | Verdict |
|---|---|---|---|
| **E** Enabling curve | What capability is improving, with what evidence? | Pack price $108/kWh (−93 % vs 2010; LFP $81/kWh); cheaper on-board compute and connectivity (Moore, Nielsen); learning from manufacturing (Wright). | **Strong** |
| **X** 10× outcome | Which measurable outcome could improve 10×? | Energy cost per km ≈ 9× lower than petrol (illustrative, §6); Grid points ≈ 10× in three years; revenue ≈ 46× in six. Purchase price has *not* improved 10×. | **Partly**: strong on running cost and reach, weak on upfront price |
| **P** Platform | Can one core capability serve many users and products? | Ather 450 → Rizta → **EL platform** ("family, commuter, performance"), shared battery/BMS/software stack; AtherStack across models; charging network open to LECCS-compatible vehicles. | **Strong** and widening |
| **A** Access | Can cost, skills, infrastructure barriers fall? | Family scooter, new regions, 5,900+ chargers, EL platform for lower prices. | **Partly**: price, charging at home and service reach remain barriers |
| **N** Network / learning | Does use create data, learning, trust, partners? | Fleet telemetry improves BMS and features via OTA; ~89 % AtherStack Pro attach (reported); Grid and community strengthen with use. | **Medium–strong**; value depends on interoperability and trust |
| **D** Dependencies | What bottleneck could stop scale? | Cash burn (net loss ₹517 Cr in FY26), cell and component supply (largely imported; a widely reported industry risk, to verify for Ather's current sourcing), factory capacity (4.2 lakh/year at Hosur until Bidkin ramps), service reach, battery safety, competition from large incumbents and EV start-ups, policy/incentives. | **The weak spot**: none of these scale exponentially |

## 6. Exponential Project Canvas for Ather (deck slide 51)

| Canvas box | Ather Energy |
|---|---|
| **Project / user** | *Target user:* urban and semi-urban daily-commute rider in India (individual and family). *Painful problem:* fuel and maintenance cost, range and charging anxiety, doubts about EV reliability, high upfront price. |
| **Current baseline** | 65,595 deliveries in Q2 FY26; 17.4 % e-2W share; adjusted gross margin ≈ 22 %; non-vehicle ≈ 12 % of income; 5,900+ Grid chargers; EBITDA margin −6.7 % (FY26). |
| **10× aspiration** | *Realised (partly):* energy cost per km ≈ **9× lower** than petrol. Illustrative assumptions (mine, not from sources): petrol ₹100/L at 40 km/L = ₹2.5/km; scooter 3.5 kWh/100 km at ₹8/kWh = ₹0.28/km. *Next (hypothesis):* **10× quarterly deliveries** from the Q2 FY26 base within about a decade. This needs ≈ 26 lakh scooters a year (about 13 % of India's ≈ 19–20 million annual two-wheeler sales, approximate), which is almost **twice the 14.2 lakh/year** planned capacity: capacity, not demand, is the first limit. |
| **Enabling technology** | Li-ion pack price curve ($108/kWh in 2025, −93 % since 2010, BNEF); cheaper compute and connectivity; learning-curve effects in cells and assembly. |
| **6 Ds** | *Relevant:* Digitized (mechanism), Demonetized (battery cost, platform reuse), Democratized (Rizta, EL, regions); Deceptive (passed). *Not-yet-relevant / limited:* Dematerialized (misleading for the vehicle), Disruptive (only partly achieved). |
| **System redesign** | *Digitize:* ownership (OTA, diagnostics, app). *Share:* one platform across many models, one charging standard. *Automate:* Industry 4.0 plant at Bidkin. *Remove:* fuel stops, oil changes, many drivetrain moving parts. *Redesign:* from "selling a scooter" to selling an ownership experience with charging, software and service (case study). |
| **Bottleneck / risk** | *Non-exponential:* capital intensity and cash burn; cell, magnet and component supply; factory capacity; service coverage. *Unintended risk:* battery fires and recycling at end of life; a grid that is still largely fossil-fuelled (so the carbon benefit depends on the power mix); exclusion of buyers who cannot charge at home or afford the upfront price. |
| **2-week experiment** | *Test:* "A tier-2-city daily commuter would switch from petrol to an Ather-class scooter if 3-year cost of ownership is at least 25 % lower and a charger is within their routine." *With:* 30 commuters (interviews plus a 3-year TCO calculator and a price/charging-access choice card). *Success:* ≥ 40 % choose the EV in the stated scenario. *Failure:* < 15 % choose it, or "no home/nearby charging" is the top objection (then the bottleneck is infrastructure, not price). |

**One-sentence hypothesis (deck slide 23):** *Because battery cost and on-board compute are improving, Ather can now offer a connected, software-updatable scooter to everyday commuters, and make the model work by spreading platform cost over the EL family and earning recurring software and charging revenue.*

## 7. The system view (user → product → infrastructure → value)

![[E8-fig3-system-map.png]]
*Figure 3. The loops (learning, data, network) are the exponential parts; the boxes in the middle (plants, chargers, suppliers, service) are the parts that scale linearly with money and time.*

## 8. Conclusion: leveraged vs. yet to leverage

| Already leveraged | Yet to leverage |
|---|---|
| **Digitized**: OTA, app, BMS, paid software layer | **Dematerialized**: more functions folded into software/phone; not applicable to the vehicle itself |
| **Deceptive**: survived the slow start, now on the steep part of the curve | **Disruptive** (fully): cross the price/charging/trust threshold for the mass market |
| **Demonetized (partly)**: battery curve, platform reuse | **Demonetized**: price and ownership cost far lower via EL platform and new ownership models |
| **Democratized (partly)**: Rizta, new regions, wider Grid | **Democratized**: tier-3/4 towns, financing, resale, shared charging, home-charging gaps |

The pattern the deck asks us to notice: **the exponential parts of Ather are the software, data, platform and network loops; the parts that do not scale automatically are batteries, factories, service and capital.** Ather's next phase depends on managing those constraints, not on any further technology curve alone.

## 9. Sources

Course materials: Session 8 deck (M4S8B2, 16 Oct 2026), slides 12–27, 29–35, 37–51; [[Case Study 1- Ather Energy.pdf]].

External (accessed 27 Oct 2026; figures differ across outlets, so each is attributed in §2):

- [Entrackr: Ather Q4 FY25 revenue and loss](https://entrackr.com/fintrackr/ather-energy-posts-rs-676-cr-revenue-in-q4-fy25-narrows-losses-by-17-9060538) · [Inc42: Ather Q4 FY25](https://inc42.com/buzz/ather-q4-fy25-ev-major-trims-loss-by-17-yoy-to-inr-234-cr) · [The Machine Maker: FY25 loss ₹812.3 Cr](https://themachinemaker.com/?p=74505)
- [Business Standard: Ather Q2 FY26 results](https://www.business-standard.com/amp/industry/auto/e-scooter-maker-ather-energy-narrows-losses-in-q2-as-revenue-rises-57-125111001815_1.html) · [Business Standard: market share 17.4 %](https://www.business-standard.com/amp/markets/capital-market-news/ather-energy-surges-after-record-q2-revenue-trims-losses-expands-market-share-125111101217_1.html)
- [The Machine Maker: Ather FY26 performance](https://themachinemaker.com/news/ather-energy-reports-record-fy26-performance-with-strong-volume-growth/) · [Inc42: Ather outruns Ola Electric](https://inc42.com/features/ather-outruns-ola-electric-can-it-keep-its-throttle-steady/) · [Autocar Pro: EL platform](https://www.autocarpro.in/news/ather-unveils-affordable-el-platform-to-spawn-scooters-across-family-commuter-performance-models-128307)
- [Ather blog: fast charging](https://www.atherenergy.com/blog/how-fast-charging-technology-works-for-ather-electric-scooters) · [The Week: Grid points, Maharashtra](https://www.theweek.in/wire-updates/business/2025/07/24/dcm25-biz-ather-energy.html) · [Autocar Pro: 580th charging point](https://www.autocarpro.in/news-national/ather-energy-installs-580th-fast-charging-point--targets-1-400-by-endfy2023-103052)
- [Deccan Herald: Bidkin plant](https://deccanherald.com/business/ather-energy-to-set-up-third-manufacturing-plant-in-maharashtra-3082215) · [I Am a Biker: Bidkin plant capacity](https://iamabiker.com/avin/2024/ather-energy-gears-up-for-massive-expansion-with-third-manufacturing-plant-in-maharashtra/)
- [BNEF: Li-ion pack price survey 2025](https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour) · [ESS News on the same survey (−93 % vs 2010)](https://www.ess-news.com/?p=7552)

*Limits of this analysis:* software-revenue share, AtherStack Pro attach and some capacity figures come from press analysis and may not match company filings; the running-cost comparison and the 10× delivery target are my own illustrative calculations with stated assumptions. Reproduce the figures with `Solution/Tools/ather_figs.py`.

## Cross-domain links
- [[Applications of First Order ODEs]] — constant-rate growth $dy/dt=ky$ behind the exponential-growth framing.
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — the decay counterpart and the idea of a characteristic time.
- [[Systems thinking and Systems Engineering_v2.pdf]] — the system map (user, product, infrastructure, value) with feedback loops.
- [[Measurements, Instrumentation and Control - MOC]] — feedback loops (learning, data, network) are closed loops in the control sense.
