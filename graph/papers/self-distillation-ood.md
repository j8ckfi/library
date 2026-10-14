---
id: paper:self-distillation-ood
type: paper
title: Does self-distillation improve reasoning?
authors:
- Jason Ken Adhinarta
- Raina Wu
- Ashutosh Sharma
- Avinash Balakrishnan
- Rameswar Panda
- Polina Golland
- Yoon Kim
- Zhang-Wei Hong
year: 2026
month: 10
arxiv_id: '2610.18613'
url: https://arxiv.org/abs/2610.18613
methods:
- method:vista
cites:
- paper:vista
- paper:nsd
tags:
- distillation
- privileged-opsd
- ood
- gotcha
---

# Does self-distillation improve reasoning?

## Abstract Summary
Negative-result caveat on privileged self-distillation. SDPO/OPSD gains largely do not generalize OOD; the paper attributes this to overfitting / transfer of existing behavior rather than new reasoning. Does not retarget VISTA.

## Key Contributions
1. SDPO LCB test_unseen Qwen3-8B −2.5 vs GRPO +3.7.
2. Science OOD −7.1 to −16.6 vs GRPO +0.9 to +1.6.
3. Treat ID OPSD lifts as in-distribution unless an OOD split is reported.

## Empirical Highlights
- OOD drops while GRPO stays flat or slightly up (single-paper).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.18613`
- Code: `https://github.com/sleepypandu/does-sd-improve-reasoning` (`code_status: released`).
