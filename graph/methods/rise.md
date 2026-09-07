---
id: method:rise
type: method
title: "RISE (Recursive Improvement via Self-Extrapolating Policy Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "a strong external / white-box teacher is available and the goal is intentional distillation"
    reason: "RISE synthesizes a teacher from the student's RLVR trajectory; OPD remains the single-teacher default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR alone"
    reason: "RISE is an RLVR+OPD loop, not the labeled dense RLVR default"
    use_instead: "method:cispo"
  - when: "no teacher, no reward, no RLVR grounding"
    reason: "OPSA is train-time supervision-free self-adaptation; RISE needs outcome-verified RLVR steps"
    use_instead: "method:opsa"
  - when: "a same-size teacher is privileged with a gold reference solution"
    reason: "That is VISTA / privileged OPSD, not self-extrapolation"
    use_instead: "method:vista"
  - when: "long-horizon outcome-only agent RL with a programmatic checker"
    reason: "Coverage / anti-drift is CANOPY, not a synthetic OPD teacher"
    use_instead: "method:canopy"
assumptions:
  - "Host run already does group-relative RLVR with a verifier. Paper: VeRL, 8 GPUs, one epoch, AdamW constant LR, GRPO advantages without std normalization, token-IS clip 2.0."
  - "Default β0=1.2 linear decay to 1, top-K=100 (K=20 for code), Qwen EMA η=0.1, OLMo previous-ckpt η=1. Distillation loss in the paper is Jensen–Shannon."
  - "Weight-space teacher is a task-arithmetic checkpoint; logit-space teacher needs current and post-RLVR logps on the same prefixes (top-K plus tail)."
last_reviewed: "2026-09-07"
papers:
  - paper:rise
recipes:
  - recipe:rise
claims:
  - benchmark: "Qwen3-8B DAPOMath in-domain Math Avg (MATH500 / AIME24 / AIME25 / AMC23 / Minerva / OlyBench)"
    metric: "average accuracy"
    value: 62.7
    baseline: "GRPO 60.0 / GRPO+SDPO 55.9 / SDAR 59.7 / RLSD 59.8"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05295"
    notes: "Table 1 RISE (weight). Multi-seed 62.4±0.2 vs GRPO 60.1±0.2. RISE (logit) 62.5."
  - benchmark: "OLMo3-7B-Instruct-SFT OpenR1 in-domain Math Avg"
    metric: "average accuracy"
    value: 56.4
    baseline: "GRPO 47.6 / SDAR 49.6"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05295"
    notes: "Table 1 RISE (logit). AIME24 46.9 vs GRPO 30.2."
  - benchmark: "Qwen3-4B-Base mixed math+STEM Math Avg / STEM Avg"
    metric: "average accuracy"
    value: "44.8 / 47.5"
    baseline: "GRPO 40.2 / 45.5; GRPO+SDPO 42.1 / 47.0"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05295"
    notes: "Table 2 RISE (weight). No privileged gold context, unlike GRPO+SDPO."
  - benchmark: "ALFWorld success / WebShop Score / WebShop Acc"
    metric: "success rate and score"
    value: "84.4 / 86.3 / 74.2"
    baseline: "GRPO 75.0 / 79.8 / 63.3; RISE (logit) 78.1 / 78.8 / 68.0"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05295"
    notes: "Table 3 RISE (weight). Multi-turn agentic; still not CANOPY's long-horizon coverage setting."
tags:
  - post-training
  - distillation
  - rlvr
  - self-extrapolation
  - rise
  - active
---

# RISE (Recursive Improvement via Self-Extrapolating Policy Distillation)

## Method Overview
RISE turns the model's own RLVR step into a dense OPD teacher. After an outcome-verified update $\theta_n\to\theta_{n+1}'$, extrapolate past the current checkpoint with $\beta>1$:

\[
\varphi(\pi_{\mathrm{future}})=\varphi(\pi_{\theta_n})+\beta\cdot\big(\varphi(\pi_{\theta_{n+1}'})-\varphi(\pi_{\theta_n})\big).
\]

Weight space: $\theta_{\mathrm{future}}=\theta_n+\beta(\theta_{n+1}'-\theta_n)$ (task arithmetic). Logit space: the same displacement on $\log\pi(\cdot\mid s_t)$, restricted to top-$K$ tokens plus a tail. The student is distilled toward $\mathrm{sg}[\pi_{\mathrm{future}}]$ (paper uses Jensen–Shannon). $\beta$ decays linearly from $\beta_0=1.2$ to $1$ over the run. A trailing anchor (Qwen EMA $\eta=0.1$, OLMo previous checkpoint $\eta=1$) tracks the displacement source. The teacher is rebuilt every iteration, so there is no static-teacher ceiling.

No external teacher. No privileged gold conditioning. RLVR is required: the displacement is the outcome-grounded update.

## When to Use
- Already running RLVR and want denser token-level targets without renting a larger teacher.
- When OPD is blocked by no white-box teacher, and VISTA/OPSD is blocked because there is no gold solution to condition on.

## When NOT to Use
- External teacher available -> `method:opd`.
- Labels exist and you only need Pass@1 RLVR -> `method:cispo`.
- No verifier / no RLVR -> `method:opsa`.
- Privileged same-size teacher with gold -> `method:vista`.
- Long-horizon episode-end coverage -> `method:canopy`.

## Relation to Existing SOTA
- Active sibling on `task:student-distillation` and a related mention on `task:math-code-rl-dense` / `task:teacher-free-on-policy-self-adaptation`. Does **not** supersede `method:opd`, `method:cispo`, `method:opsa`, `method:vista`, or `method:canopy`.
- Distinct from `method:opd-one-example` / `method:opd-hard-cot-selection` (data selection on teacher OPD) and from `method:self-routing` (labeled GRPO/OPSD router).

## Gotchas & Failure Modes
- Weight-space needs a second forward of $\theta_{\mathrm{future}}$ (or a fused logit mix). Logit-space needs both checkpoints' logps on the same prefixes; store top-$K$ plus tail, not the full vocab.
- Paper wall-time overhead is 1.3–1.6× vs GRPO-only; sampling cost is unchanged.
- Neither extrapolation space always wins. Default to $\beta_0=1.2$ linear decay; Table 4 shows 1.5 and a fixed $\beta$ are worse.
- GRPO inside the loop is the paper's inner optimizer, not a revival of GRPO as the library Pass@1 default.
