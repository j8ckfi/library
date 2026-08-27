---
id: method:olmo-3
type: method
title: "OLMo-3 / Dolma-3 Open Recipe & Dolci Stack"
category: "data-curriculum"
status: sota
sota_for:
  - task:open-data-recipe
  - task:instruct-sft-alignment
  - task:direct-preference-alignment
supersedes:
  - method:olmo-2-curriculum
  - method:tulu3-rlvr
papers:
  - paper:olmo-3
recipes:
  - recipe:olmo-3
claims:
  - benchmark: "Dolma-3 Open Token Mix / MMLU / GSM8k / Dolci Instruct"
    metric: "open foundation & instruct SOTA"
    value: "Leading open data recipe and open instruct SFT baseline"
    baseline: "OLMo-2 Curriculum / Tülu-3 Stack"
    date: "2026-08-26"
    verified: true
    notes: "Dolma-3 multi-trillion token open mix + Dolci curated SFT and verifiable reward alignment."
tags:
  - pretraining
  - open-data
  - data-curriculum
  - instruct
  - dolci
  - sota
---

# OLMo-3 / Dolma-3 Open Recipe & Dolci Stack

## Method Overview
OLMo-3 provides the comprehensive open foundation model pretraining and alignment stack:
1. **Dolma-3 Open Data Recipe**: Multi-trillion token open pretraining dataset with transparent mixture proportions and filtering pipelines.
2. **Curriculum Annealing**: Staged pretraining transitioning from broad web data to high-signal synthetic reasoning tokens.
3. **Dolci Instruct Stack**: Curated SFT and verifiable reward post-training pipeline establishing the open instruct standard.

## When to Use
- Default SOTA open data pretraining recipe.
- Default SOTA open instruct SFT and alignment pipeline.

## Supersession
- Supersedes `method:olmo-2-curriculum` for open data recipes.
- Supersedes `method:tulu3-rlvr` for open instruct SFT and alignment.
