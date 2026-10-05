---
id: paper:metarubric
type: paper
title: "MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning"
authors:
  - "Yuxuan Fan"
  - "Jaehong Yoon"
year: 2026
month: 10
arxiv_id: "2610.02824"
url: "https://arxiv.org/abs/2610.02824"
methods:
  - method:metarubric
cites:
  - paper:draco
  - paper:canopy
tags:
  - post-training
  - rl-alignment
  - rubric
  - metarubric
---

# MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning

## Abstract Summary
Rubric judges can award a criterion even when the required information or action is absent (Vacuous Credit), which can flip a GRPO advantage sign. MetaRubric alternates evidence-aware policy optimization with response-guided rubric adaptation: credit is the min of satisfaction, requirement coverage, and evidential support; an outer loop revises criteria and weights from current-policy errors while preserving the initial rubric's meaning. Active plug-in beside DRACO on outcome-only agent RL. Code: `https://github.com/metarubric/metarubric` and `https://metarubric.github.io`.

## Key Contributions
1. **Vacuous Credit** as the failure mode of static rubric judges.
2. **Inner evidence-aware GRPO + outer rubric revision / weight adaptation**.
3. **Qwen3-4B PubMedQA 78.40 vs static-judge GRPO 72.40 (+6.00)**; Gemma-e2b 72.00 vs 51.60 (+20.40).

## Empirical Highlights
- HealthBench-Hard Qwen3-4B 13.02 vs 10.56 (+2.46); 8B 10.34 vs 7.15 (+3.19).
- MMOral-OPG 8B 30.44 vs 27.35 (+3.09); Gemma 35.10 vs 31.28 (+3.82).
- DRACO remains outcome-blind rubric credit with no learned judge; CANOPY remains checker TGC.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02824`
- Project: `https://metarubric.github.io`
- Code: `https://github.com/metarubric/metarubric` (`code_status: released`; HTTP 200 as of 2026-10-05).
