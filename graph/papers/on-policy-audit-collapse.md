---
id: paper:on-policy-audit-collapse
type: paper
title: 'Better Policies, Worse Verifier Audits'
authors:
- 'Daniel Cieslak'
- 'Jacek Lubinski'
year: 2026
month: 10
arxiv_id: '2610.29029'
url: https://arxiv.org/abs/2610.29029
methods:
- method:cispo
cites:
- paper:verigate
- paper:minimax-m1
tags:
- rlvr
- verifier
- gotcha
---

# Better Policies, Worse Verifier Audits

## Abstract Summary
As a policy masters one conjunct of a verifier, on-policy AUC of that component verifier can collapse and even prefer a worse verifier, because the audit mix loses F-failures. Call this on-policy audit collapse.

## Key Contributions
1. Identified-set / erasure-threshold analysis for component-verifier refresh loops.

## Empirical Highlights
- Does not retarget CISPO or VeriGate. GSM8K is a negative control in the paper.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29029`
- Code: `none found` (`code_status: none`).
