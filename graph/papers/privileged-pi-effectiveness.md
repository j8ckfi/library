---
id: paper:privileged-pi-effectiveness
type: paper
title: 'Predicting Privileged Information Effectiveness for On-Policy Self-Distillation'
authors:
- 'Kaijian Zou'
- 'Emiliano Penaloza'
- 'MohammadHossein Rezaei'
- 'Anisha Gunjal'
- 'Mohit Raghavendra'
- 'Lu Wang'
- 'Yunzhong He'
- 'Anas Mahmoud'
year: 2026
month: 10
arxiv_id: '2610.22512'
url: https://arxiv.org/abs/2610.22512
methods:
- method:vista
- method:privileged-context-drift
cites:
- paper:vista
- paper:privileged-context-drift
tags:
- opsd
- privileged-information
- gotcha
---

# Predicting Privileged Information Effectiveness for On-Policy Self-Distillation

## Abstract Summary
OPSD with privileged information is not a single design choice: 16 PI configurations across three multi-turn agentic settings show that content and construction dominate. The paper predicts PI effectiveness from KL and error-reduction (Δd_err) rather than introducing a new trainer. Complements Privileged Context as Drift (content vs source) with a selection protocol.

## Key Contributions
1. 16 PI configurations on multi-turn agentic OPSD.
2. KL / Δd_err protocol for choosing PI, not a new update rule.
3. Sibling evidence card to privileged-context-drift.

## Empirical Highlights
- Choose PI by predicted effectiveness; do not treat demo vs feedback vs rephrase as interchangeable.
- Does not retarget VISTA.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22512`
- Code: `none found` (`code_status: none`).
