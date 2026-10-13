---
id: paper:specialists-learn-faster
type: paper
title: 'Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge
  Update Efficiency'
authors:
- Sheng Zhao
- Yuhao Zhu
year: 2026
month: 10
arxiv_id: '2610.13835'
url: https://arxiv.org/abs/2610.13835
methods:
- method:specialists-learn-faster
cites:
- paper:olmo-3
tags:
- pretraining
- data-ordering
- specialists-learn-faster
---

# Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency

## Abstract Summary
Chronologically ordered pretraining knowledge yields specialists that need fewer update steps than shuffled generalists (about half in the paper). The authors give an update-cost law plus a data-organization strategy. Plug-in on `task:open-data-recipe` (data-ordering gotcha); link `task:agent-continual-learning`.

## Key Contributions
1. Chronological specialists vs shuffled generalists on update-step cost.
2. Update-cost law relating organization to later adaptation.
3. Data-organization strategy for pretraining mixes.

## Empirical Highlights
- Specialists need ~half as many update steps as shuffled generalists.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13835`
- Project: `https://horizon-lab.org/specialist/`
- Code: `none found` (`code_status: none`).
