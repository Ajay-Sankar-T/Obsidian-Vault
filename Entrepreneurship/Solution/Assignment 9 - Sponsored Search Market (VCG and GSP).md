---
title: Assignment 9 – Sponsored Search Market (VCG and GSP)
course: Innovation & Entrepreneurship for Engineers (IIT Madras)
source: "[[Pricing-1.pdf]] (slides 54–57)"
tags: [entrepreneurship, assignment, auctions, gsp, vcg, pricing]
aliases: [Assignment 9]
---

# Assignment 9: Sponsored Search Market (VCG and GSP)

**Batch B · Group 14**

Ajay Sankar (ME25B012) · Aadit Pankaj (EP25B001) · Aarav Prakash (CH25B002) · Yuvraj Dighe (ME25B146) · Gudditi Himesh Raghava Chandra (CS25B028)

**Market (Pricing-1, slide 57).** Slots a, b, c have click-through rates 10, 4, 0. Advertisers x, y, z earn 7, 6, 1 per click. Find the efficient allocation and the VCG prices, then analyse the GSP auction (slide 54): truthful bidding, equilibria, revenue.

## 1. Efficient allocation

Value of a slot to an advertiser = CTR × value per click.

| | x | y | z |
|---|---|---|---|
| a (10) | 70 | 60 | 10 |
| b (4) | 28 | 24 | 4 |
| c (0) | 0 | 0 | 0 |

The best assignment is x→a, y→b, z→c, worth 70 + 24 + 0 = **94**. The next best is y→a, x→b, worth 88.

## 2. VCG

Each winner pays the harm it causes the others: their best total value without it, minus their total value with it (slide 56).

| | Others' value without it | Others' value with it | Price | Per click | Payoff |
|---|---|---|---|---|---|
| x | y→a 60 + z→b 4 = 64 | y→b 24 + z→c 0 = 24 | **40** | 4 | 30 |
| y | x→a 70 + z→b 4 = 74 | x→a 70 + z→c 0 = 70 | **4** | 1 | 20 |
| z | 70 + 24 = 94 | 70 + 24 = 94 | **0** | 0 | 0 |

VCG revenue is **44**. A winner's price depends only on the others' reports, so reporting the true value is optimal. (The same method on the slide 55 market gives 13 and 3, as on slide 56.)

## 3. GSP

**Truthful bids (7, 6, 1).** x takes a and pays y's bid: 6 × 10 = 60, payoff 10. y takes b and pays 1 × 4 = 4, payoff 20. z takes c and pays 0. Revenue is 64.

**Truthful bidding is not an equilibrium.** If x bids 5, it drops to slot b and pays z's bid: 1 × 4 = 4. Its payoff rises from 10 to 28 − 4 = **24** (figure below).

**Equilibria.** Both profiles below survive every unilateral deviation.

| Bids (x, y, z) | Allocation | Payoffs (x, y, z) | Revenue | Welfare | Best deviations |
|---|---|---|---|---|---|
| (5, 4, 2) | x, y, z | 30, 16, 0 | 48 | 94 | x bids 3: 28 − 8 = 20. y bids above 5: 60 − 50 = 10. z takes b: 4 − 16 = −12. |
| (3, 5, 1) | y, x, z | 24, 30, 0 | 34 | 88 | y bids 2: 24 − 4 = 20. x bids above 5: 70 − 50 = 20. z takes b: 4 − 12 = −8. |

In the second equilibrium y (value 6) holds slot a while x (value 7) holds b, so 6 units of welfare are lost. z bids freely because slot c has zero clicks.

![[A9-fig2-payoff-vs-bid.png]]

*Figure. Payoff to x as its bid varies, with y bidding 6 and z bidding 1.*

## 4. Comparison

| Mechanism | Revenue | Welfare |
|---|---|---|
| VCG | 44 | 94 |
| GSP, truthful (not an equilibrium) | 64 | 94 |
| GSP equilibrium (5, 4, 2) | 48 | 94 |
| GSP equilibrium (3, 5, 1) | 34 | 88 |

- VCG is truthful and efficient, with revenue 44.
- GSP is not truthful and has several equilibria, some inefficient.
- GSP revenue can be above (48) or below (34) VCG, depending on the equilibrium.
