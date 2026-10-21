---
id: paper:native-safety-opd
type: paper
title: 'Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation'
authors:
- 'Bingqi Shang'
- 'Yang Zhang'
- 'Yiwei Chen'
- 'Changsheng Wang'
- 'Shiyu Chang'
- 'Bingquan Shen'
- 'Sijia Liu'
year: 2026
month: 10
arxiv_id: '2610.27555'
url: https://arxiv.org/abs/2610.27555
methods:
- method:opd
cites:
- paper:opd
- paper:opd-safety-backdoor
tags:
- opd
- safety
- gotcha
---

# Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation

## Abstract Summary
Native safety from safety pretraining can transfer small-to-large through OPD, including cross-tokenizer. A 1.7B student ASR rises only 5.00% after subsequent FT vs 11.58% for safety post-training, with utility 48.20 vs the aligned teacher's 27.42. Pair with the OPD-for-safety backdoor warning.

## Key Contributions
1. Native-safety reuse via OPD; selective small-to-large transfer.

## Empirical Highlights
- Does not retarget OPD matching. Complements paper:opd-safety-backdoor rather than replacing it.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27555`
- Code: `none found` (`code_status: none`).
