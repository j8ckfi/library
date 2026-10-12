---
id: paper:synthself
type: paper
title: Continually Post-training Small Models via Synthetic Self-distillation
authors:
- Woosung Koh
- Hyunsoo Lee
- Kyungjae Lee
- Haeju Park
- Dahyun Lee
- Dasol Hwang
- Moontae Lee
year: 2026
month: 10
arxiv_id: '2610.13113'
url: https://arxiv.org/abs/2610.13113
methods:
- method:synthself
cites:
- paper:aclarena
- paper:opd
tags:
- post-training
- distillation
- continual-learning
- synthself
---

# Continually Post-training Small Models via Synthetic Self-distillation

## Abstract Summary
SDFT needs ICL rewrite that small models cannot do. Acquisition/forgetting correlate with post-train distribution shift. SynthSelf outsources the in-distribution rewrite to a minimally larger same-family aligner, then trains the small student off-policy with rejection sampling so supervision stays in-distribution.

## Key Contributions
1. Linear correlation of small-model CL failure with distribution shift.
2. Same-family slightly-larger aligner + off-policy rejection sampling.
3. Beats six CL/distill baselines at three small scales.

## Empirical Highlights
- See `method:synthself` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13113`
- Code: `none found` (`code_status: none`).
