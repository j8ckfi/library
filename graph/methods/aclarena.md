---
id: method:aclarena
type: method
title: "ACLArena"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; ACLArena is multi-stage capability stacking, not a math loss"
    use_instead: "method:cispo"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL"
    use_instead: "method:sao"
  - when: "programmatic checker AppWorld coverage / anti-drift"
    reason: "CANOPY remains outcome-only coverage"
    use_instead: "method:canopy"
  - when: "production post-train engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier stack; ACLArena is built on slime as a continual-learning recipe"
    use_instead: "method:miles"
  - when: "GitHub issue to patch / SWE harness"
    reason: "mini-SWE-agent remains the loop"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Multiple post-train stages with heterogeneous environments (paper: Math → Search → E-commerce → IF). Forgetting is the complaint, not a missing Pass@1 kernel."
  - "MLE: offline replay of filtered specialist trajectories (SDFT), then a routed network of LoRA experts each specialized by RL."
  - "Code: WillDreamer/ACLArena. HF collection willhx/aclarena. Built on slime."
last_reviewed: "2026-09-23"
papers:
  - paper:aclarena
recipes:
  - recipe:aclarena
claims:
  - benchmark: "ACLArena in-domain / OOD after Math→Search→E-commerce→IF, Mixture of Low-Rank Experts"
    metric: "AIME26 avg@16 / NQ / τ³-Retail / IF-Eval / single-hop search"
    value: "21.04 / 49.7 / 32.9 / 85.0 / 57.7"
    baseline: "Seq-Final 10.21 / 33.5 / 29.6 / 84.8 / 44.9; per-task oracles peak AIME26 25.83, NQ 49.9, Retail 33.2, IF-Eval 86.2"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.23989"
    notes: "Table 2. MLE also GPQA 42.4, multi-hop 38.6. Not a CISPO / CANOPY / SAO / Miles bake-off."
tags:
  - post-training
  - agentic
  - continual-learning
  - lora
  - aclarena
  - active
---

# ACLArena

## Method Overview
ACLArena studies Agent Continual Learning: stacking capabilities across sequential post-training stages without catastrophic overwrite. Sequential training is the diagnostic. Tasks pull parameters in partially aligned directions; later stages overwrite earlier peaks; token-level prediction change concentrates on high-entropy positions.

Compared consolidators: multi-teacher mixed OPD (MMOPD), self-distilled fine-tuning (SDFT), and weight-space merging. The proposed recipe, Mixture of Low-Rank Experts (MLE), first replays filtered high-quality specialist trajectories, then trains a routed set of LoRA experts with RL so one model serves every stage. This is **not** CISPO, not SAO, not CANOPY, not Miles, and not mini-SWE-agent.

## When to Use
- Multi-stage industrial agent post-training where Math / tool-use / IF stages interfere and you need a controlled ACL recipe plus a testbed.

## When NOT to Use
- Pass@1 math → `method:cispo`. Async stragglers → `method:sao`. AppWorld TGC → `method:canopy`. Production engine → `method:miles`. Issue → patch → `method:mini-swe-agent`.

## Relation to Existing SOTA
- Active first hop on `task:agent-continual-learning` only (method status active; listed in that task's `current_sota`; `sota_for` stays empty). Does **not** retarget `method:cispo`, `method:sao`, `method:canopy`, `method:miles`, `method:opd`, or `method:open-mopd`.

## Gotchas & Failure Modes
- Sequential training is the microscope, not the recipe. Do not report Seq-Final as the method.
- Shared-weight MMOPD / SDFT / merge still trade one capability against another; MLE is the paper's answer to that trade-off, not a new distill default.
- Token-level analysis is under fixed-prefix scoring of a reference sequence. Do not treat it as a Pass@1 result.
