---
id: paper:traceforge
type: paper
title: 'TraceForge: Distilling with Your Own Thinking'
authors:
- 'Yan Wang'
year: 2026
month: 10
arxiv_id: '2610.29680'
url: https://arxiv.org/abs/2610.29680
methods:
- method:traceforge
cites:
- paper:opd
- paper:bridged-self-distill
tags:
- distillation
- traces
- active
---

# TraceForge

## Abstract Summary
TraceForge trains a generator to write student-family reasoning traces from context plus a teacher answer, then a critic picks authentic-looking traces. Training is SFT then adversarial; it does not replay encrypted teacher blocks.

## Key Contributions
1. TraceForge as an active plug-in on `task:student-distillation`.

## Empirical Highlights
- generated family-native traces beat Fable 5's own thinking on coding; authenticity 0.68 vs real traces 0.66 (critic-selected 0.82). Does not retarget `method:opd`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29680`
- Code: `none found` (`code_status: none`).
