---
id: method:lesser
type: method
title: "LESSER"
category: "data-attribution"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "LOO / LDS / query-conditioned scoring and you control the trainer"
    reason: "MAGIC remains peak-LDS first hop; LESSER cheapens output-layer-gradient features for SFT/RL selection wrappers"
    use_instead: "method:magic"
  - when: "circuit-engagement RLVR data selection"
    reason: "CircuitLens is CRS-decile selection; LESSER is a cheaper gradient feature"
    use_instead: "method:circuitlens"
  - when: "mix-ratio search or replacing an open pretrain mix"
    reason: "OLMo-3 / Dolma-3 remains the open mix; LESSER is post-train candidate scoring"
    use_instead: "task:open-data-recipe"
assumptions:
  - "You already have a gradient-selection wrapper (LESS / GIST / GradAlign / GRACE). LESSER replaces the full-parameter feature with the LM-head gradient."
  - "Paper: Llama-2-7B; 9.7× SFT / 3.0× RL vs 4-checkpoint LESS."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:lesser
recipes:
  - recipe:lesser
claims:
  - benchmark: "Llama-2-7B feature-extraction FLOP vs 4-checkpoint LESS"
    metric: "FLOP reduction"
    value: "9.7× SFT / 3.0× RL"
    baseline: "4-checkpoint LESS (Xia et al. 2024)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03702"
    notes: "Does not retarget MAGIC LDS. Same final RL accuracy as GradAlign in the paper."
  - benchmark: "selection-set Jaccard vs full-gradient ranking"
    metric: "Jaccard"
    value: "0.53"
    baseline: "random 0.075"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03702"
    notes: "Output-layer features recover much of the full-gradient ranking."
tags:
  - post-training
  - data-attribution
  - lesser
  - active
---

# LESSER

## Method Overview
Influence-style selectors score each candidate with a full-parameter gradient. LESSER stores only the output-layer (LM-head) gradient as the feature and plugs that vector into the same LESS / GIST / GradAlign / GRACE wrapper. Feature extraction is 9.7× cheaper for SFT and 3.0× cheaper for RL vs 4-checkpoint LESS on Llama-2-7B. MAGIC remains the LDS first hop when you own the trainer.

## When to Use
- Post-train SFT or RL data selection where full-gradient features are the bottleneck and you already have a selection wrapper.

## When NOT to Use
- Peak LDS / query-conditioned LOO → `method:magic`. Circuit-engagement RLVR selection → `method:circuitlens`. Open pretrain mix → `task:open-data-recipe`.

## Relation to Existing SOTA
- Active plug-in on `task:training-data-attribution` beside MAGIC (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace MAGIC.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Do not invent a 1.3-point downstream lift. The paper tracks full-gradient / GradAlign accuracy; it does not retarget MAGIC.
