---
id: paper:dpo-hp-landscape
type: paper
title: 'The Shape of the DPO Hyperparameter Landscape: What to Measure, How It Moves with Scale, and When Not to Transfer It'
authors:
- 'Hannan Mahadik'
- 'David Salinas'
- 'Jacek Golebiowski'
- 'Aaron Klein'
year: 2026
month: 10
arxiv_id: '2610.27895'
url: https://arxiv.org/abs/2610.27895
methods:
- method:olmo-3
cites:
- paper:olmo-3
tags:
- dpo
- gotcha
---

# The Shape of the DPO Hyperparameter Landscape

## Abstract Summary
DPO LR and beta are not transferable across scale or datasets. Validation loss is a weak proxy for downstream-best hyperparameters. Short candidate runs cut selection cost.

## Key Contributions
1. Dense DPO HP grid across same-family scales; transfer and proxy-metric gotchas.

## Empirical Highlights
- Does not retarget OLMo-3 Dolci. Tune DPO HPs per model, dataset, and eval.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27895`
- Code: `none found` (`code_status: none`).
