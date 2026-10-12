---
id: paper:magicbeanstalk
type: paper
title: 'MagicBeanStalk: Escaping the RLVR Zero Advantage Trap with Recursive Data Synthesis'
authors:
- Ximing Lu
- Aviral Kumar
- Jan Kautz
- Yejin Choi
- David Acuna
year: 2026
month: 10
arxiv_id: '2610.12659'
url: https://arxiv.org/abs/2610.12659
methods:
- method:magicbeanstalk
cites:
- paper:verigate
- paper:srd
tags:
- post-training
- rlvr
- data-synthesis
- magicbeanstalk
---

# MagicBeanStalk: Escaping the RLVR Zero Advantage Trap with Recursive Data Synthesis

## Abstract Summary
A large pooled math RLVR corpus is ~88% zero-advantage for a fixed policy and rollout budget. Filtering concentrates signal but throws away hard problems. Prompting a teacher to vary those hard problems does not calibrate difficulty. MagicBeanStalk decomposes hard seeds top-down and recursively synthesizes families that keep the reasoning blueprint but sit in the mixed-success band so some rollouts pass inside the train budget.

## Key Contributions
1. Zero-advantage trap as a function of problems × policy × rollout budget (~88% of a 78K pool).
2. Top-down decompose / bottom-up recursive synthesis that preserves blueprints.
3. +8.6 / +5.4 vs +1.1 full corpus / +5.8 best filter on gpt-oss-120b and DeepSeek v4Flash.

## Empirical Highlights
- See `method:magicbeanstalk` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12659`
- Code: `none found` (`code_status: none`).
