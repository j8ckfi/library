---
id: method:zip-sr
type: method
title: "ZIP-SR"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "ZIP-SR is 4-bit AdamW state quantization; Muon2 remains the 7B default"
    use_instead: "method:muon2"
  - when: "full-param memory-efficient pretrain via subspace projections"
    reason: "SCALE remains that first hop; ZIP-SR quantizes AdamW states"
    use_instead: "method:scale"
  - when: "ternary column-wise one-sparse FT optimizer state"
    reason: "TACO is FT-axis sparse state; ZIP-SR is 4-bit AdamW moments"
    use_instead: "method:taco"
assumptions:
  - "Host is AdamW. Paper: 130M-2.7B GPT/Llama-style pretrain and full-param SFT."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:zip-sr
recipes:
  - recipe:zip-sr
claims:
  - benchmark: "GPT/Llama-style pretrain 130M-2.7B, 4-bit AdamW states vs TorchAO"
    metric: "mean validation-loss gap to 32-bit AdamW"
    value: "gap reduced at every size; largest reported reduction 70%"
    baseline: "TorchAO 4-bit AdamW; 32-bit AdamW"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.12444"
    notes: "AdamW-only. Does not retarget Muon2 or SCALE." 
tags:
  - optimizer
  - quantization
  - adamw
  - 4bit
  - zip-sr
  - active
---

# ZIP-SR

## Method Overview
Quantize AdamW's second moment with a codebook that includes zero. Choose the stochastic-rounding coin-flip in preconditioner coordinates, not raw-state coordinates, so the next adaptive step sees less distortion near zero. First moment stays NF4.

## When to Use
- You must keep AdamW and want 4-bit optimizer states without TorchAO's val-loss gap.

## When NOT to Use
- Hidden-layer 7B default -> `method:muon2`. Subspace full-param memory -> `method:scale`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`) with a mention on `task:full-param-memory-efficient-pretrain`. Does **not** replace Muon2 or SCALE.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Not a Muon method. Targeted LM-head first-moment SR in the last 10% of training is part of the paper recipe.
