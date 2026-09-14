---
id: method:esrl
type: method
title: "ESRL (Expert-Space Exploration Reinforcement Learning)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the MoE/VL RLVR loss"
    reason: "ESRL perturbs rollout routing; SAPO remains the MoE/VL algorithm default"
    use_instead: "method:sapo"
  - when: "dense Pass@1 math/code RLVR"
    reason: "No expert router; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE post-train router soft-anchor"
    reason: "RPB anchors the live router to the base prior; ESRL explores routing at rollout"
    use_instead: "method:rpb"
  - when: "choosing the frontier MoE architecture"
    reason: "ESRL does not retarget DeepSeek-V4 / Kimi-K3"
    use_instead: "method:deepseek-v4"
assumptions:
  - "MoE host RL (paper uses GRPO on slime). Qwen3-30B-A3B top-k, Sigma-20B-A0.5B top-1, Moonlight-16B-A3B shared-expert."
  - "Rollout-side noisy routing in the public repo is Qwen3-MoE on SGLang's non-DeePEP path."
  - "Replay expert IDs (R3), not routing weights. Enable one routing variant at a time."
last_reviewed: "2026-09-14"
papers:
  - paper:esrl
recipes:
  - recipe:esrl
claims:
  - benchmark: "Qwen3-30B-A3B MATH post-train, avg of OlympiadBench / AIME / AMC / MinervaMath"
    metric: "Pass@1 / Pass@8"
    value: "42.1 / 64.2"
    baseline: "GRPO 38.9 / 59.7; GSPO 41.6 / 63.3"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13058"
    notes: "+3.2 Pass@1 and +4.5 Pass@8 vs GRPO. No extra sampling. SAPO is not the paper host; do not read this as a SAPO bake-off."
tags:
  - post-training
  - moe
  - rl-alignment
  - esrl
  - routing
  - active
---

# ESRL (Expert-Space Exploration Reinforcement Learning)

## Method Overview
Expert routing is a second temperature. ESRL perturbs router logits at rollout, keeps high-confidence experts as anchors, samples the remaining slots from a bounded candidate pool, scales noise with router entropy, and replays rollout expert IDs during the training-side logp pass (R3). The reward and the policy-optimization objective stay whatever the host already uses.

## When to Use
- MoE RLVR where token-level sampling is not producing diverse expert paths.
- Complementary to SAPO / GRPO / GSPO: routing exploration, not a new loss.

## When NOT to Use
- MoE/VL loss choice → `method:sapo`. Dense Pass@1 → `method:cispo`. Soft-anchor the pretrained router → `method:rpb`. Architecture → `method:deepseek-v4`.

## Relation to Existing SOTA
- Active on `task:math-code-rl-moe`. Does **not** enter `current_sota`. SAPO stays the MoE/VL default. RPB stays the router-anchor candidate.

## Gotchas & Failure Modes
- Unrestricted routing noise activates bad experts. Keep anchors + candidate pool.
- Public patches: Qwen3-MoE, SGLang normal path, `--use-slime-router`. DeePEP / FuseEP not validated.
- Do not enable two routing variants at once.
