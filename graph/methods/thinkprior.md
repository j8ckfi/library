---
id: method:thinkprior
type: method
title: "ThinkPrior"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR default"
    reason: "ThinkPrior is a prompt-selection data policy; CISPO remains the Pass@1 loss"
    use_instead: "method:cispo"
  - when: "adaptive IS clip on scarce-correct groups is the issue"
    reason: "GAPO changes clip width, not which prompts are sampled"
    use_instead: "method:gapo"
  - when: "gating process rewards on all-zero groups"
    reason: "Silent-group prompt selection is not VeriGate's PRM gate"
    use_instead: "method:verigate"
  - when: "Pass@K / coverage / no-backward is the goal"
    reason: "Coverage default stays ES-reasoning; DATPO is the tree-rollout sibling"
    use_instead: "method:es-reasoning"
assumptions:
  - "Host RLVR is GRPO/DAPO-family with a KL-free group-relative advantage. Silent groups exist only for that estimator."
  - "Paper: Qwen2.5-Math-7B, 16 seeds, 250-prompt pool (plus a 1200-prompt directional check). Anchor is a cheap external model scored by the training verifier."
  - "Does not claim a final-accuracy gain. DataFlex-RL is the negative-result cousin on data-policy accuracy."
last_reviewed: "2026-09-09"
papers:
  - paper:thinkprior
recipes:
  - recipe:thinkprior
claims:
  - benchmark: "Qwen2.5-Math-7B GRPO, 16 seeds, early silent-group rate"
    metric: "silent prompt-group rate"
    value: "10.6%"
    baseline: "uniform 23.8% (55% relative reduction; 95% [-16.4, -9.9] pp, d=-2.95)"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.09075"
    notes: "Uniform spends 39% of whole-run rollouts on silent groups; 37.9% of early groups are silent."
  - benchmark: "Same 16-seed run, final accuracy"
    metric: "accuracy delta vs uniform"
    value: "+0.7 points"
    baseline: "interval [-2.2, 3.5]; no detected difference"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.09075"
    notes: "Waste cut, not a Pass@1 bake-off. 250-prompt pool full-run discards 968 vs 885 (reallocation)."
  - benchmark: "ThinkPrior+DAPO vs DAPO, generated rollouts at 3840 update budget"
    metric: "generated rollouts"
    value: 7381
    baseline: "DAPO 8256 (−10.6%); early waste −65.4%"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.09075"
    notes: "Same 3840-rollout update budget in both arms."
tags:
  - post-training
  - rlvr
  - data-policy
  - thinkprior
  - active
---

# ThinkPrior

## Method Overview
ThinkPrior is a **cold-start prompt-selection** plug-in for GRPO-family RLVR. Silent groups (all-correct or all-wrong) have zero group-relative advantage under the KL-free surrogate. One offline verifier-scored pass of an external anchor initializes a Beta posterior per prompt. Selection uses expected learnability with a dispersion penalty (at equal posterior mean, prefer the prompt whose difficulty is better known). After training starts, the posterior updates from target-policy outcomes. Loss and optimizer do not change.

Sits beside CISPO (loss) and GAPO (clip). Does not replace VeriGate. DataFlex-RL is the accuracy-null cousin: data policies need not beat uniform GRPO at 95% CI.

## When to Use
- Short-horizon GRPO/DAPO runs where early silent-group waste is a large share of generation.
- You can afford one cheap offline anchor pass over the prompt pool.

## When NOT to Use
- Pass@1 kernel → `method:cispo`. Clip width → `method:gapo`. PRM gating → `method:verigate`.
- Do not pick ThinkPrior to raise final accuracy on a 250-prompt pool; the paper's accuracy result is a null.

## Relation to Existing SOTA
- Active data-policy plug-in on `task:math-code-rl-dense`. Optional mention on `task:all-zero-verifier-groups`. Does **not** supersede `method:cispo`, `method:gapo`, or `method:verigate`.
- Distinct from DataFlex-RL (evaluation platform / negative accuracy result) and from DATPO (tree rollouts for Pass@K).

## Gotchas & Failure Modes
- No official GitHub as of 2026-09-09. Project page only.
- Silence is defined for the KL-free group-relative term. Objectives with a KL term can still update on a silent group.
- Full-run accounting on the 250-prompt pool discards slightly *more* than uniform (968 vs 885). The 1200-prompt late result is directional (three seeds, overlapping ranges at step 200).
- Eleven selection rules split by whether they carry a verifier-scored zero-rollout prior (12.5–16.7% early waste) vs not (20.4–42.5%; uniform 37.9%).
