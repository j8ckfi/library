---
id: method:sampling-sft
type: method
title: "Sampling SFT"
category: "data-curriculum"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "Vanilla SFT still loses to GRPO; CISPO remains Pass@1. Sampling SFT rewrites expert traces then runs ordinary SFT"
    use_instead: "method:cispo"
  - when: "privileged-teacher OPSD / gold-solution self-distillation"
    reason: "Sampling SFT is SFT on MCMC-projected traces, not a privileged-teacher update. VISTA remains that first hop"
    use_instead: "method:vista"
  - when: "single-teacher student distillation from a frozen larger teacher"
    reason: "Sampling SFT has no teacher logits; OPD remains matching distillation"
    use_instead: "method:opd"
assumptions:
  - "Off-policy expert traces exist and a correctness filter can keep rewrites valid. MCMC / Metropolis–Hastings projection sampling with B=32, T=1856, N_MCMC=10, then ordinary SFT."
  - "Paper: Qwen2.5-3B math; Qwen2.5-7B-Instruct chemistry and medical. Project https://aakaran.github.io/finetuning_with_sampling/. No official training GitHub as of 2026-10-03."
last_reviewed: "2026-10-03"
papers:
  - paper:sampling-sft
recipes:
  - recipe:sampling-sft
claims:
  - benchmark: "Qwen2.5-3B MATH levels 3–5"
    metric: "accuracy (fraction)"
    value: "0.495"
    baseline: "GRPO 0.457 / UFT 0.470 / vanilla SFT 0.243 / base 0.315"
    date: "2026-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02140"
    notes: "Table 1 middle. Vanilla SFT loses to GRPO. Do not headline this as SFT beating GRPO. Sampling SFT then GRPO is 0.545."
  - benchmark: "Qwen2.5-3B MATH500"
    metric: "accuracy (fraction)"
    value: "0.582"
    baseline: "GRPO 0.313 / UFT 0.297 / vanilla SFT 0.168 / base 0.245"
    date: "2026-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02140"
    notes: "Sampling SFT + RL (GRPO on the sampling-SFT checkpoint) 0.652, strongest in the table."
  - benchmark: "Qwen2.5-7B-Instruct chemistry (SciKnowEval)"
    metric: "new-task accuracy (fraction)"
    value: "0.660"
    baseline: "OPSD 0.618 / vanilla SFT 0.618 / base 0.343"
    date: "2026-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02140"
    notes: "Prior-capability avg 0.586 vs OPSD 0.568 vs SFT 0.520 vs base 0.597."
  - benchmark: "Qwen2.5-7B-Instruct medical"
    metric: "new-task accuracy / prior-capability avg"
    value: "0.458 / 0.516"
    baseline: "OPSD 0.466 / 0.501; vanilla SFT 0.448 / 0.353; base 0.353 / 0.597"
    date: "2026-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02140"
    notes: "Roughly tied with OPSD on the new task; forgets less than vanilla SFT (prior avg 0.516 vs 0.353)."
tags:
  - post-training
  - sft
  - mcmc
  - data-curriculum
  - sampling-sft
  - active
---

# Sampling SFT

## Method Overview
Vanilla SFT on off-policy expert traces is off-policy; GRPO is on-policy but cannot learn from traces the base model never samples. Sampling SFT leaves the SFT loss alone and **rewrites the data**. Metropolis–Hastings projection sampling edits expert traces toward the base model while a correctness filter keeps them valid, then ordinary SFT runs on the rewritten set.

Paper hyperparameters: block count B=32, max length T=1856, N_MCMC=10. Vanilla SFT still loses to GRPO on Qwen2.5-3B MATH(3,4,5) (0.243 vs 0.457). Sampling SFT is 0.495; Sampling SFT then GRPO is 0.545 / MATH500 0.652.

Active plug-in. CISPO stays Pass@1. VISTA stays privileged-teacher OPSD.

## When to Use
- You have off-policy expert traces for math/science skill add and want SFT that does not collapse to the vanilla-SFT forgetting regime.

## When NOT to Use
- Pass@1 RLVR default → `method:cispo`. Privileged-teacher OPSD → `method:vista`. Frozen larger-teacher matching → `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` beside `method:cispo` (`sota_for: []`). Mention on `task:privileged-teacher-opsd` next to VISTA / OPSD (chemistry beats OPSD; medical is roughly tied and forgets less). Does **not** enter either `current_sota`. Does **not** replace CISPO, VISTA, or OPD. Do **not** write the card as “SFT beats GRPO.”

## Gotchas & Failure Modes
- Vanilla SFT is not this method. On MATH(3,4,5) vanilla SFT (0.243) is below the base (0.315) and below GRPO (0.457).
- Traces boosted for a different base (Qwen traces used to SFT Olmo) underperform. The MCMC chain is model-native.
- No official training GitHub as of 2026-10-03. Project: https://aakaran.github.io/finetuning_with_sampling/. `aakaran/reasoning-with-sampling` is a different 2025 inference paper.
