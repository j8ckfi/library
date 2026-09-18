---
id: method:opd-eos
type: method
title: "OPD EOS Termination Fix"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher student-distillation default"
    reason: "This is an EOS-mismatch gotcha and a semantic-class stop patch on OPD, not a new distill kernel"
    use_instead: "method:opd"
  - when: "teacher-free unlabeled self-adaptation"
    reason: "OPSA has no teacher EOS to mismatch"
    use_instead: "method:opsa"
  - when: "privileged-teacher math OPSD with gold solutions"
    reason: "VISTA remains that first hop; this paper is base-student vs post-trained-teacher stop ids"
    use_instead: "method:vista"
assumptions:
  - "OPD with a base (or earlier-stage) student and a post-trained teacher whose stop ids may differ. Paper: Qwen3, Llama-3.2, Gemma-3, K2-Horizon; verl + sampled-token OPD; DAPO-Math-17k TTRL prompts."
  - "Decoding-stop alignment alone is the insufficient control. Semantic-class scoring is the fix."
last_reviewed: "2026-09-18"
papers:
  - paper:opd-eos
recipes:
  - recipe:opd-eos
claims:
  - benchmark: "Qwen3-1.7B-Base student / Qwen3-4B teacher, sampled-token OPD, 200 updates"
    metric: "stop-mass at the student's actual stop / clip rate"
    value: "without fix, stop-mass → ~0 by step 150 and clip rate → ~100%"
    baseline: "native student EOS (condition A) vs two-stop decoding (B)"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20511"
    notes: "Gotcha on method:opd. Semantic-class stop (condition D) restores termination. Not an OPD replacement."
  - benchmark: "Gemma-3-4B-pt → 4B-it, 7168 response budget"
    metric: "mean response length / clip rate"
    value: "budget-saturating ~100% clip → mean ~2000 tokens, clipping near zero"
    baseline: "unaligned / decoding-only stop alignment"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20511"
    notes: "Llama lands ~3500–4000 tokens and about half the clip rate. K2-Horizon still shows a late inflation mode after alignment."
tags:
  - post-training
  - distillation
  - opd
  - eos
  - gotcha
  - niche
---

# OPD EOS Termination Fix

## Method Overview
Not a new distill default. OPD scores the student's own tokens with the teacher. If the two models put EOS mass on different ids, terminating is an action the student can sample that the teacher will not support, and the teacher's stop id never appears in rollouts. Length then inflates into the budget. The fix treats equivalent EOS tokens as one semantic stop and scores that class with the teacher's summed terminal mass (`EOS_MODE=semantic_class` in `UNCSciML/opd-eos`). Aligning decode stop ids without changing the loss is not enough. A later K2-Horizon inflation mode can remain after alignment.

## When to Use
- OPD runs that grow to the max length with correct answers, especially base student + instruct/post-trained teacher.

## When NOT to Use
- Choosing a distill kernel → `method:opd`. No teacher → `method:opsa`. Privileged math OPSD → `method:vista`.

## Relation to Existing SOTA
- Niche gotcha on `task:student-distillation`. Wired onto `method:opd` / `recipe:opd` the same way `paper:spurious-advantage-grpo` is wired onto CISPO/GRPO. Does **not** enter `current_sota`. Does **not** supersede `method:opd`.

## Gotchas & Failure Modes
- Declared stop sets can match while sampled stop ids do not.
- Termination preference can flip across training stages (K2-Horizon). Re-check ids after SFT/RL, not only at init.
- Semantic-class stop is not a complete theory of OPD length; late inflation can persist.
