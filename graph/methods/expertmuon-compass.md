---
id: method:expertmuon-compass
type: method
title: "ExpertMuon-Compass"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Compass is a per-expert Muon step-size plug-in, not a dense Muon2 replacement"
    use_instead: "method:muon2"
  - when: "Kimi-K2 / QK-clip Muon stability"
    reason: "MuonClip remains the QK-clip recipe; Compass scales expert step size from alignment"
    use_instead: "method:muonclip-kimi-k2"
  - when: "temporary soft-orthogonality then remove"
    reason: "ORCA is spectral annealing, not expert step multipliers"
    use_instead: "method:orca"
assumptions:
  - "MoE pretrain with a Muon-family expert update. Paper: FineWeb-Edu; Nesterov on all matrices in the headline run."
  - Keeps Muon direction and momentum. Only multiplies the expert step.
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:expertmuon-compass
recipes:
  - recipe:expertmuon-compass
claims:
  - benchmark: "FineWeb-Edu MoE pretrain vs Muon / NorMuon"
    metric: "pretrain loss / expert-load balance"
    value: "matches or beats Muon and NorMuon; strongest on blocked multilingual"
    baseline: "Muon / NorMuon (WD matched to NorMuon on longer runs)"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04140"
    notes: "Does not retarget Muon2 or MuonClip."
tags:
  - pretraining
  - optimizer
  - moe
  - expertmuon-compass
  - active
---

# ExpertMuon-Compass

## Method Overview
Compass multiplies each MoE expert's Muon step by (1) a family factor from the cosine of the orthogonalized update vs the gradient, compared with other experts in the layer, and (2) a scalar radius from row-wise update–gradient alignment. Direction and the Muon momentum buffer stay Muon's.

## When to Use
- MoE pretrain on a Muon-family trainer where experts see shifting data (blocked multilingual is the paper's sharpest case).

## When NOT to Use
- Dense ~7B optimizer → `method:muon2`. QK-clip Muon → `method:muonclip-kimi-k2`. Spectral annealing → `method:orca`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` beside `method:muon2` / `method:muonclip-kimi-k2` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2 or DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Do not change Muon direction; Compass is a step-length multiplier.
- Dense (non-MoE) pretrain is not this card.
