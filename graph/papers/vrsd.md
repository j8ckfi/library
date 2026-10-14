---
id: paper:vrsd
type: paper
title: Self-Distillation with Verbal Regularization
authors:
- Jiazheng Li
- Yawei Li
- Junru Lu
- Zhenyi Shen
- Di Yin
- Lin Gui
- Xing Sun
- David Rügamer
- Xinpeng Wang
- Yulan He
year: 2026
month: 10
arxiv_id: '2610.16354'
url: https://arxiv.org/abs/2610.16354
methods:
- method:vrsd
cites:
- paper:vista
- paper:nsd
tags:
- distillation
- privileged-opsd
- verbal-regularization
---

# VRSD

## Abstract Summary
System prompts attenuate privileged-info influence on the teacher to counter entropy collapse and shortcutting in privileged self-distillation. 11/12 settings improve. Does not replace VISTA / NSD.

## Key Contributions
1. Verbal regularization of the privileged teacher (prompt-side, not a new loss).
2. Pass@1 lifts on Qwen3-4B / OLMo-3-7B / Qwen3-8B.
3. Released github.com/lijiazheng99/VRSD.

## Empirical Highlights
- Avg +3.9pp Pass@1 (7.2 / 2.8 / 1.6 on Qwen3-4B / OLMo-3-7B / Qwen3-8B) (single-paper).
- 11/12 settings win.
- Qwen3-4B SQL OPSD 69.8 vs VRSD 81.0.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.16354`
- Code: `https://github.com/lijiazheng99/VRSD` (`code_status: released`).
