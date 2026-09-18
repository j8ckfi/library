---
id: method:bias-only-ttrl
type: method
title: "Bias-Only Label-Free TTRL"
category: "rl-alignment"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "label-free test-time reasoning is the library default"
    reason: "TTPO remains the first hop (asymmetric OPSD + Grouped RL); this is a bias-subspace compression of majority-vote TTRL"
    use_instead: "method:ttpo"
  - when: "train-time unlabeled math post-training on a prompt set"
    reason: "u-OPSD remains train-time unlabeled; this is test-time bias steering"
    use_instead: "method:u-opsd"
  - when: "labeled Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "teacher-free train-time self-adaptation without majority vote"
    reason: "OPSA does not use consensus rewards"
    use_instead: "method:opsa"
assumptions:
  - "Test-time adaptation with majority-vote rewards. Frozen backbone; only bias parameters (~100K) move."
  - "MATH-500 headline. Transfer to 4,500 held-out MATH problems in the paper. Also VL/audio benches."
  - "No official GitHub as of 2026-09-18."
last_reviewed: "2026-09-18"
papers:
  - paper:bias-only-ttrl
recipes:
  - recipe:bias-only-ttrl
claims:
  - benchmark: "MATH-500, label-free bias-only TTRL"
    metric: "accuracy"
    value: "76.67%"
    baseline: "authors' labeled bias-steering reproduction (slightly below); full-parameter TTRL uses ~76,000× more trainable params"
    date: "2026-09-16"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.18587"
    notes: "Abstract. Majority-vote rewards. Not a TTPO bake-off. Niche compression of TTRL."
  - benchmark: "Trainable parameters vs full-parameter TTRL"
    metric: "parameter ratio"
    value: "~76,000× fewer (~100K bias-only)"
    baseline: "full-parameter TTRL"
    date: "2026-09-16"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.18587"
    notes: "Backbone frozen. Steering vectors transfer to 4,500 held-out MATH problems."
tags:
  - test-time-training
  - ttrl
  - label-free
  - bias-only
  - niche
---

# Bias-Only Label-Free TTRL

## Method Overview
Keep the pretrained backbone frozen. Train about 100K bias parameters with majority-vote pseudo-labels as the TTRL reward. The claim is that a tiny bias subspace with enough accessible gradient energy can absorb test-time gains that full-parameter TTRL buys with far more weights. Consensus reliability is used as the reason majority-vote rewards do not immediately collapse. This sits beside TTPO on `task:label-free-test-time-reasoner`; it does not replace TTPO's asymmetric OPSD / Grouped RL split.

## When to Use
- Label-free TTT where you can only afford a bias-sized optimizer state and you are willing to trust majority vote.

## When NOT to Use
- Default label-free TTT → `method:ttpo`. Train-time unlabeled → `method:u-opsd`. Labeled Pass@1 → `method:cispo`. No consensus labels → `method:opsa`.

## Relation to Existing SOTA
- Niche sibling on `task:label-free-test-time-reasoner`. Does **not** enter `current_sota`. Does **not** supersede `method:ttpo`.

## Gotchas & Failure Modes
- Majority vote is still a noisy teacher. TTPO exists because naive consensus distillation is brittle; this paper does not retire that argument.
- No public trainer as of 2026-09-18.
- MATH-500 76.67% is not a reason to drop TTPO on AIME-style TTT.
