---
id: method:ugpc
type: method
title: UGPC (Uncertainty-Guided Progressive Contraction)
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation (OPD)
  reason: UGPC is CoT-SFT data selection, not reverse-KL OPD
  use_instead: method:opd
- when: hard/long-CoT example selection for OPD gains
  reason: OPD-hard-CoT-selection is OPD data selection; UGPC is SFT contraction
  use_instead: method:opd-hard-cot-selection
assumptions:
- 'Teacher CoT corpus plus student SFT. Paper: DAPO-17k, Qwen3.5-4B/9B, plus Gemma/Llama/Mistral
  students.'
- 'Code: Jackbrocp/Learning-More-by-Training-Less (code_status: released).'
last_reviewed: '2026-10-13'
papers:
- paper:ugpc
recipes:
- recipe:ugpc
claims:
- benchmark: Qwen3.5-4B/9B reasoning SFT on DAPO-17k vs full-data SFT
  metric: optimization budget vs full 3-epoch SFT; wall-clock
  value: matches/beats full-data SFT at 0.22–1.91% budget; 8.47/9.23h → 0.01–0.07h
  baseline: full-corpus reasoning SFT
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12933
  notes: Headline 0.22%. Cross-family ~0.45%. Closed-source teachers up to +13.4%.
    Does not retarget OPD.
tags:
- post-training
- distillation
- data-selection
- ugpc
- active
---

# UGPC (Uncertainty-Guided Progressive Contraction)

## Method Overview
Build Monte Carlo reasoning trees around CoT states. Contract the teacher corpus to an uncertainty-rich pool. During student SFT, route remaining steps to the learner-relevant subset from a probe epoch.

## When to Use
- CoT-SFT / reasoning distillation where the corpus is large and you want a tiny optimization budget.

## When NOT to Use
Live teacher OPD → `method:opd`. OPD hard-CoT selection → `method:opd-hard-cot-selection`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). CoT-SFT data selection, not OPD. Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: released** Jackbrocp/Learning-More-by-Training-Less as of 2026-10-13.
- Teacher-side MCRT construction is the expensive step; the student budget is the 0.22% figure.
- Not an OPD keep-mask (IER-OPD / DIAL-OPD).
