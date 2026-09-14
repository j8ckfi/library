---
id: method:plc-dpo
type: method
title: "PLC-DPO (Posterior Label Correction DPO)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the open instruct / preference stack default"
    reason: "OLMo-3 Dolci remains the open stack; PLC-DPO is a noisy-label DPO plug-in"
    use_instead: "method:olmo-3"
  - when: "clean pairwise prefs and a reference-free length-normalized loss is enough"
    reason: "SimPO remains the simple offline preference baseline; PLC-DPO needs policy and reference logps"
    use_instead: "method:simpo"
  - when: "labeled Pass@1 math/code RLVR"
    reason: "PLC-DPO is offline preference routing, not CISPO"
    use_instead: "method:cispo"
assumptions:
  - "Paired preferences that may be flipped or weakly directional. Paper: UltraFeedback Binarized and 57 dataset-model-benchmark cells. EMNLP 2026 Findings."
  - "Reuses DPO policy and reference log-probabilities. LoRA rank 16, LR 1e-5, one epoch, effective batch 64 in the official repo."
last_reviewed: "2026-09-14"
papers:
  - paper:plc-dpo
recipes:
  - recipe:plc-dpo
claims:
  - benchmark: "57 dataset-model-benchmark cells, mean win rate vs one-epoch DPO"
    metric: "mean win rate"
    value: 60.5
    baseline: "next-best method 55.5"
    date: "2026-09-14"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2608.30597"
    notes: "EMNLP 2026 Findings. Routing clean/flip/tie from calibrated policy-reference margin. Not a Dolci or SimPO supersession."
tags:
  - post-training
  - preference-alignment
  - dpo
  - plc-dpo
  - noisy-labels
  - active
---

# PLC-DPO (Posterior Label Correction DPO)

## Method Overview
Each preference pair is a latent clean / flip / tie. PLC-DPO uses the standardized policy-reference margin as evidence and mixes forward DPO, reversed DPO, and a tie regularizer. EMA calibration, a warm-up fraction, and confidence-gated mixing delay aggressive corrections until the margin is trustworthy.

## When to Use
- Offline DPO on preferences that are noisy, flipped, or weakly directional.
- When you already run DPO (policy + reference logps) and can swap the loss.

## When NOT to Use
- Open instruct default → `method:olmo-3`. Clean reference-free prefs → `method:simpo`. Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active on `task:direct-preference-alignment`. Does **not** enter `current_sota`. OLMo-3 Dolci stays the stack. SimPO stays the simple offline baseline.

## Gotchas & Failure Modes
- Three official schedules: aggressive / balanced / conservative (\(\alpha\), \(\tau_{\mathrm{dir}}\), \(\tau_{\mathrm{tie}}\), warm-up, \(\gamma_{\max}\), \(\kappa\)). Start from balanced.
- Repo release (2026-09-14) covers clean UFB plus three PLC settings; not every paper cell is in the first drop.
