---
id: paper:target-regeneration
type: paper
title: 'Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding'
authors:
- 'Jungseob Lee'
- 'Hogun Seong'
- 'Euijun Choi'
- 'Sugyeong Eo'
year: 2026
month: 10
arxiv_id: '2610.29013'
url: https://arxiv.org/abs/2610.29013
methods:
- method:uno
cites:
- paper:uno
tags:
- speculative-decoding
- gotcha
---

# Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding

## Abstract Summary
Draft-training objectives that look strong on external responses shrink once the target rewrites those responses. Distillation and verification-gated losses add large gains on corpus tokens but much less after greedy regeneration.

## Key Contributions
1. Controls for target regeneration when crediting speculative-draft losses.

## Empirical Highlights
- Code js-lee-AI/TargetRegeneration. Does not retarget Uno.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29013`
- Code: `https://github.com/js-lee-AI/TargetRegeneration` (`code_status: released`).
