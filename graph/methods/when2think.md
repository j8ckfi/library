---
id: method:when2think
type: method
title: "When2Think (IDAC Hybrid Think/NoThink)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "When2Think is a Think/NoThink length-control plug-in; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR loss"
    reason: "SAPO remains the MoE/VL algorithm; IDAC does not change the surrogate"
    use_instead: "method:sapo"
  - when: "Pass@K / coverage / no-backward as the primary goal"
    reason: "ES-reasoning remains that first hop; When2Think reports Pass@3 as an efficiency trade-off"
    use_instead: "method:es-reasoning"
  - when: "outcome-only long-horizon agent RL"
    reason: "CANOPY remains coverage/anti-drift; this is single-turn hybrid reasoning length"
    use_instead: "method:canopy"
assumptions:
  - "Hybrid Think/NoThink reasoner with a verifier. Paper uses pre-computed reference accuracy and token-usage statistics; no learned RM and no online reference-model queries."
  - "Math-only evidence in the abstract (AIME24/AIME25). Host Pass@1 algorithm stays CISPO."
  - "GitHub JJunShim/When2Think is a stub README as of 2026-09-18."
last_reviewed: "2026-09-18"
papers:
  - paper:when2think
recipes:
  - recipe:when2think
claims:
  - benchmark: "AIME24 vs base hybrid reasoner"
    metric: "Pass@3 / token usage"
    value: "Pass@3 +10.0% with tokens −27.9%"
    baseline: "base model (uniform overthinking / no IDAC)"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.19671"
    notes: "Abstract. Efficiency plug-in, not a CISPO bake-off. Pass@3 is the paper's reported metric."
  - benchmark: "AIME25 Pass@3"
    metric: "Pass@3"
    value: "40.0%"
    baseline: "compression and routing-only length-control baselines"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.19671"
    notes: "Abstract. Outperforms compression and routing-only. Not Pass@1 SOTA."
tags:
  - post-training
  - rlvr
  - hybrid-reasoning
  - length-control
  - when2think
  - active
---

# When2Think (IDAC Hybrid Think/NoThink)

## Method Overview
When2Think is a post-training length-control plug-in for hybrid reasoners. Easy items should skip CoT (NoThink); hard items should keep it (Think). IDAC shapes the verifier reward with offline reference statistics — accuracy and token usage — so the advantage tells the policy when System 1 is enough. Batch-wise standardized advantages keep the update critic-free. The host RLVR loss does not change.

## When to Use
- Hybrid Think/NoThink math reasoners that waste tokens on easy items and you can precompute reference accuracy/length stats.

## When NOT to Use
- Pass@1 kernel → `method:cispo`. MoE/VL loss → `method:sapo`. Pass@K / no-backward → `method:es-reasoning`. Agents → `method:canopy`.

## Relation to Existing SOTA
- Active efficiency plug-in on `task:math-code-rl-dense`. Does **not** enter `current_sota`. Does **not** supersede `method:cispo`.

## Gotchas & Failure Modes
- GitHub is a stub README as of 2026-09-18 (`code_status: partial`).
- IDAC needs reference stats before training. No online teacher queries in the paper recipe.
- Headline is Pass@3 + tokens, not Pass@1. Do not read this as a CISPO replacement.
