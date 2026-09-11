---
id: method:nemotron-imo-gold
type: method
title: "Nemotron IMO Gold Recipe"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-turn dense math/code Pass@1 RLVR"
    reason: "This is an olympiad-proof specialist + NL TTC pipeline; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "choosing the Nemotron 3 Ultra pretrain architecture"
    reason: "Specialist post-train on top of Ultra; architecture default stays the Ultra node / DeepSeek-V4 / Kimi-K3 shelf"
    use_instead: "method:nemotron-3-ultra"
  - when: "general chat / instruct SFT"
    reason: "OLMo-3 Dolci / Nemotron-Cascade 2 remain instruct defaults"
    use_instead: "method:olmo-3"
assumptions:
  - "Start from Nemotron 3 Ultra GA (nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16). SFT max seq 425,984. Then RL specialist. TTC is generate–verify–refine over three checkpoints."
  - "Released: nvidia/Nemotron-3-Labs-Ultra-Math-SFT and -RL; data nvidia/Nemotron-Math-Proofs-v3-SFT and -RL; NeMo-Skills recipes/nemotron-imo-tts; NeMo-RL imo-26-ultra-v3 guide."
last_reviewed: "2026-09-11"
papers:
  - paper:nemotron-imo-gold
recipes:
  - recipe:nemotron-imo-gold
claims:
  - benchmark: "IMO 2026 official contest"
    metric: "points / 42"
    value: 30
    baseline: "gold-medal threshold (30/42)"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10712"
    notes: "NL generate–verify–refine; no formal prover, tools, or internet. Three Ultra checkpoints plus a high-compute selection stage."
  - benchmark: "Nemotron-IMO-Bench"
    metric: "released problem count"
    value: 200
    baseline: "held-out novel olympiad-level items (not IMO 2026 papers)"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10712"
    notes: "Eval set released with the recipe. Do not mix with AIME Pass@1 CISPO numbers."
tags:
  - post-training
  - math
  - olympiad
  - nemotron
  - test-time-compute
  - active
---

# Nemotron IMO Gold Recipe

## Method Overview
Post-train two Nemotron 3 Ultra specialists (SFT proof corpus, then RL) and run a natural-language generate–verify–refine loop at test time. The search uses the GA Ultra checkpoint plus both specialists; a later high-compute stage picks the submission. No Lean, no tools, no web.

This is an olympiad-proof / hard-math **recipe**, not the dense Pass@1 kernel. CISPO stays Pass@1. Ultra stays the base MoE architecture node.

## When to Use
- Olympiad-style natural-language proofs from a Nemotron 3 Ultra stack, with the released SFT/RL checkpoints or the NeMo-Skills / NeMo-RL recipes.

## When NOT to Use
- Pass@1 AIME/MATH RLVR → `method:cispo`. Instruct SFT → `method:olmo-3`. Frontier MoE architecture pick → `method:deepseek-v4` / `method:nemotron-3-ultra`.

## Relation to Existing SOTA
- Active on `task:olympiad-math-posttrain` (that task's first hop) and a mention on `task:math-code-rl-dense`. Does **not** retarget CISPO. Does **not** supersede `method:nemotron-3-ultra`.

## Gotchas & Failure Modes
- 30/42 is a contest TTC system, not a Pass@1 training metric.
- Sequence length 425k SFT is load-bearing for proofs; do not drop to short-CoT CISPO settings and expect the same.
- Branch `imo-26-ultra-v3` on NeMo-RL is the documented RL guide; Skills `recipes/nemotron-imo-tts` is the TTC entry.
