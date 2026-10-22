---
id: paper:echo-vocab-collapse
type: paper
title: 'ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization'
authors:
- 'Yun Li'
- 'Ehsan Javanmardi'
- 'Simon Thompson'
- 'Jiachen Gong'
- 'Qunli Zhang'
- 'Zifan Zeng'
- 'Shiming Liu'
- 'Peng Wang'
year: 2026
month: 10
arxiv_id: '2610.29410'
url: https://arxiv.org/abs/2610.29410
methods:
- method:olmo-3
cites:
- paper:olmo-3
tags:
- preference
- gotcha
- dpo
---

# ECHO

## Abstract Summary
Preference optimization can raise every ranking metric while a shared hidden-state offset (the common-mode) grows unseen by the relative loss, until one vocabulary row dominates decoding.

## Key Contributions
1. Common-mode offset diagnostic for DPO-family collapse. Slug avoids collision with method:echo-mtp.

## Empirical Highlights
- Does not retarget OLMo-3 Dolci. Distinct from method:echo-mtp.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29410`
- Code: `none found` (`code_status: none`).
