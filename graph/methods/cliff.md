---
id: method:cliff
type: method
title: "Cliff (First-Mistake Process Credit)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR optimizer"
    reason: "Cliff is a process-credit plug-in on GRPO/DAPO-style trainers; CISPO remains the Pass@1 default"
    use_instead: "method:cispo"
  - when: "single-teacher distillation is the goal"
    reason: "Cliff locates a first mistake; it does not match teacher token distributions"
    use_instead: "method:opd"
  - when: "gating a trained PRM behind outcome verification on all-zero groups"
    reason: "Cliff is not a PRM; VeriGate remains the process-supervision default"
    use_instead: "method:verigate"
  - when: "you need a learned step-level reward model"
    reason: "Cliff uses an off-the-shelf teacher as a first-error locator, not a trained PRM"
    use_instead: "method:verigate"
assumptions:
  - "Host RLVR already samples a group and has a binary (or thresholded) outcome verifier."
  - "An off-the-shelf teacher can produce a reference solution and point at the first student mistake. If the teacher's own solution fails the verifier, fall back to vanilla GRPO for that group."
  - "Paper trains Qwen3-4B-Base (SFT on OpenThoughts then RL) and Phi-4-mini-Instruct on DAPO-math / Deepcoder in veRL. Default λ=0."
last_reviewed: "2026-09-04"
papers:
  - paper:cliff
recipes:
  - recipe:cliff
claims:
  - benchmark: "Qwen3-4B math avg (GSM8k / MATH-500 / DAPO / AIME), SOTA teacher"
    metric: "average accuracy"
    value: 65.66
    baseline: "GRPO 61.68 / Distill 58.58 / GRPO-with-teacher 62.37"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02817"
    notes: "Table 2. Abstract also reports +15% vs OPD and +7% vs GRPO across 12 scenarios."
  - benchmark: "Qwen3-4B math avg, Qwen3-32B teacher"
    metric: "average accuracy"
    value: 64.62
    baseline: "GRPO 61.20 / OPD 58.17"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02817"
    notes: "Table 2. Cross-family Gemma3-27B teacher: Cliff 63.70 vs GRPO 62.02 vs OPD 55.24."
tags:
  - post-training
  - rlvr
  - process-supervision
  - cliff
  - active
---

# Cliff (First-Mistake Process Credit)

## Method Overview
Cliff is a process-credit plug-in for GRPO/DAPO-style RLVR. An off-the-shelf teacher writes a reference solution; if that solution fails the verifier, the group falls back to vanilla GRPO. Otherwise the teacher marks the Pitfall Step $p(a)$ — the first incorrect reasoning step — on each failed student rollout. Token advantages are then

\[
A_{i,j}=\begin{cases}
A_{\mathrm{cor}}-b & R=1,\\
\lambda A_{\mathrm{cor}}-b & R=0 \land j<p(a_i),\\
A_{\mathrm{inc}}-b & R=0 \land j\geq p(a_i),
\end{cases}
\]

with $A_{\mathrm{cor}}=(1-\mu)/\sigma$, $A_{\mathrm{inc}}=-\mu/\sigma$ the usual group-relative values and $b$ a zero-mean offset. Paper default $\lambda=0$: the correct prefix of a failed rollout is not positively reinforced (avoids length hacking); the incorrect suffix still gets $A_{\mathrm{inc}}$. Overlength rollouts set $p(a)=0$.

This is not a process reward model. No PRM is trained. The teacher is a first-error locator.

## When to Use
- Optional add-on when already running GRPO/DAPO/CISPO-family RLVR and a modest teacher can judge first mistakes (judging is easier than solving in the paper).
- When OPD is blocked by tokenizer / family mismatch but you still want denser-than-outcome credit.

## When NOT to Use
- Do not pick Cliff instead of `method:cispo` as the dense RLVR algorithm.
- Do not replace `method:verigate` as the gated-PRM / all-zero-group default.
- Do not replace `method:opd` when the goal is teacher-distribution matching.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense`, `task:reasoning-rl-alignment`, and `task:all-zero-verifier-groups`. Does **not** supersede `method:cispo`, `method:opd`, `method:verigate`, or PRMs.
- Distinct from CRISP (deferred; name collision only).

## Gotchas & Failure Modes
- Use $\lambda=0$. Positive prefix reward on failed rollouts invites length hacking.
- If the teacher fails the verifier, that group is vanilla GRPO. Weak teachers need the ground-truth reference filter.
- False negatives (teacher says wrong when the verifier says right) are the main judge error; false positives are rare.
- Coding in the paper uses a binary all-tests-pass reward, then the same Pitfall split.
