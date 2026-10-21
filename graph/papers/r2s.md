---
id: paper:r2s
type: paper
title: 'Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation'
authors:
- 'Shu Zhao'
- 'Tan Yu'
year: 2026
month: 10
arxiv_id: '2610.28586'
url: https://arxiv.org/abs/2610.28586
methods:
- method:r2s
cites:
- paper:opd
- paper:spod
tags:
- distillation
- opd
- agentic
- active
---

# Capable Teacher, Myopic Scorer

## Abstract Summary
R2S repairs a myopic teacher scorer before agentic OPD: from student-divergence states the teacher can still finish, but token scores let delaying moves through. Takeover-informed fine-tunes of the teacher become the frozen OPD scorer.

## Key Contributions
1. Reward-free rollout-to-scorer repair for agentic OPD.

## Empirical Highlights
- Wins all 12 teacher-student-environment cells; +12.8 success vs best competing agentic-OPD method per cell.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28586`
- Project: `https://tree-shu-zhao.github.io/r2s/` (`code_status: none`).
