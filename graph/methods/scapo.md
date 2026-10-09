---
id: method:scapo
type: method
title: "SCAPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "SCAPO is semifactual token credit on a GRPO host; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "first-mistake process credit (Pitfall Step prefix/suffix)"
    reason: "Cliff is first-mistake; SCAPO is semifactual stability"
    use_instead: "method:cliff"
  - when: "outcome-blind rubrics without a checker"
    reason: "DRACO remains that sibling"
    use_instead: "method:draco"
assumptions:
  - "You can construct semifactual prompts that preserve the gold answer."
  - "Code: DtYXs/SCAPO (`code_status: released`). HF Daily 2026-10-08." 
last_reviewed: "2026-10-09"
papers:
  - paper:scapo
recipes:
  - recipe:scapo
claims:
  - benchmark: "Qwen3-4B-Base and Qwen3-1.7B-Base AIME 2024-2026 vs GRPO"
    metric: "AIME 2024-2026 accuracy lift vs GRPO"
    value: "+5.63 (4B) / +4.17 (1.7B)"
    baseline: "GRPO uniform sequence advantage"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.40360"
    notes: "HF Daily 2026-10-08. Does not retarget CISPO." 
tags:
  - post-training
  - rlvr
  - credit-assignment
  - scapo
  - active
---

# SCAPO

## Method Overview
For a completed response, rewrite task-irrelevant prompt features while keeping the answer. Tokens whose distribution jumps are unstable. Downweight them in the GRPO-family advantage so outcome credit does not reinforce spurious prompt features. Stability alone gets no extra credit.

## When to Use
- RLVR policy that flips under irrelevant prompt paraphrases, and you can build answer-preserving semifactuals.

## When NOT to Use
- Pass@1 kernel -> `method:cispo`. First-mistake prefix/suffix -> `method:cliff`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO or Cliff.

## Gotchas & Failure Modes
- **code: released** DtYXs/SCAPO as of 2026-10-09.
- Semifactual construction is problem-family specific. Decode-time filter is not a trainer.
