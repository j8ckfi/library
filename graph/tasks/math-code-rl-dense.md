---
id: task:math-code-rl-dense
type: task
title: "Mathematical and Code RL Reasoning (Dense Policies)"
domain: "post-training"
summary: "Reinforcement learning on verifiable mathematical and coding tasks using dense transformer policies."
scope: "Single-turn (or short-CoT) dense math/code RLVR with a programmatic verifier. Pass@1 default is CISPO."
out_of_scope:
  - "Long-horizon interactive agents judged only at episode end (CANOPY / DRACO)"
  - "Async tool-latency RL (SAO)"
  - "Live-web multi-hop search-agent training (Iris)"
  - "Pass@K / coverage / no-backward (ES-reasoning / DATPO)"
  - "Olympiad NL proofs / IMO TTC (Nemotron IMO Gold)"
redirects:
  - when: "outcome-only long-horizon interactive agent RL"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "train asynchronous RL for a tool-use policy"
    to: "task:agentic-async-rl"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing)"
    to: "task:web-search-agent-rl"
  - when: "Pass@K / coverage / no-backward rather than Pass@1"
    to: "task:passk-reasoning-coverage"
  - when: "olympiad-style natural-language proofs / IMO TTC rather than Pass@1"
    to: "task:olympiad-math-posttrain"
current_sota:
  - method: method:cispo
    as_of: "2026-08-26"
    benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & training stability"
    value: "Default SOTA for Dense RL"
    notes: "CISPO via MiniMax-M1 (2506.13585) + ScaleRL (2510.13786)."
methods:
  - method:cispo
  - method:es-reasoning
  - method:bpco
  - method:dapo
  - method:sspo
  - method:minpro
  - method:dr-grpo
  - method:grpo
  - method:gmts
  - method:diem
  - method:cliff
  - method:self-routing
  - method:opsa
  - method:gapo
  - method:rise
  - method:flowbalance
  - method:tgopd
  - method:sparse-opd-supervision
  - method:opd-then-rlvr
  - method:thinkprior
  - method:datpo
  - method:circuitlens
  - method:dataflex-rl
  - method:verpo
  - method:rlvr-group-correlation
  - method:nemotron-imo-gold
  - method:partial-reasoning-traces
last_reviewed: "2026-09-11"
tags:
  - post-training
  - reasoning
  - math
  - code
  - cispo
---

# Mathematical and Code RL Reasoning (Dense Policies)

## Problem Definition
Training dense language models to generate long chains of thought (CoT) and verifiable solutions for competitive math and coding problems.

## SOTA Recommendation (as of 2026-09-09)
- **Primary Method (Pass@1 labeled RLVR)**: **CISPO** (`method:cispo`, MiniMax-M1 2506.13585 + ScaleRL 2510.13786). Unchanged.
- **Systems Reference**: DAPO stays as systems paper reference. GRPO stays retired.
- **Related alternative (Pass@K / coverage / no-backward)**: `method:es-reasoning` (`arXiv:2608.27351`). Do not swap CISPO for ES or revive GRPO when the goal is Pass@1. Tree-rollout coverage sibling: `method:datpo` (`arXiv:2609.08650`) on `task:passk-reasoning-coverage`.
- **Optional token-filter plug-in**: `method:gmts` (`arXiv:2608.30632`) when using GRPO/DAPO/CISPO-family token truncation. Does not replace CISPO.
- **Optional example-reweight plug-in**: `method:diem` (`arXiv:2608.29252`) gradient-alignment batch reweight. Does not replace CISPO.
- **Optional first-mistake process credit**: `method:cliff` (`arXiv:2609.02817`). Active plug-in, not a PRM, not a CISPO replacement. VeriGate remains the gated-PRM default.
- **Optional sample-level recipe router**: `method:self-routing` (`arXiv:2609.01422`) GRPO / OPSD / REG / skip from rollout correctness+confidence. Does not replace CISPO or OPSA.
- **Optional adaptive IS clip**: `method:gapo` (`arXiv:2609.00444`, EMNLP 2026 Main) widens the GRPO/GSPO clip on scarce-correct hard-problem rollouts. Active plug-in. Does not replace CISPO.
- **Optional cold-start prompt prior**: `method:thinkprior` (`arXiv:2609.09075`) zero-rollout Beta difficulty prior. Cuts silent-group waste; no detected final-accuracy gain. Does not replace CISPO or GAPO.
- **Optional circuit data-selection signal**: `method:circuitlens` (`arXiv:2609.07183`, EMNLP 2026 Findings). Low-engagement decile can win on 7B medium math; regime-dependent.
- **Negative-result data-policy platform**: `method:dataflex-rl` (`arXiv:2609.06107`) — RLVR data policies do not beat uniform GRPO at 95% CI in that study.
- **Related RLVR+self-OPD loop**: `method:rise` (`arXiv:2609.05295`) builds a synthetic teacher from the model's own RLVR trajectory. Does not replace CISPO, OPD, or OPSA.
- **Optional verifier-grounded self-improvement**: `method:flowbalance` (`arXiv:2609.03241`) privileged same-model trajectory balance, sign-gated by group advantage. Does not replace CISPO, OPSA, OPD, VISTA, RISE, or CANOPY.
- **Optional verified-evidence regularizer**: `method:verpo` (`arXiv:2609.06100`) on `task:privileged-teacher-opsd`. Evidence as a proposal, not CISPO.
- **Gotcha**: group-relative magnitude can reward lucky guesses on bounded-answer / search-agent settings (`paper:spurious-advantage-grpo`). Do not promote SignBalance over CISPO.
- **Gotcha (verifier ICC)**: within-group verifier errors are correlated (ρ≈0.53, Kish n_eff≈1.70 at k=8; `method:rlvr-group-correlation`, arXiv:2609.06386). Not an optimizer.
- **Optional OPD teacher-reliability gate**: `method:tgopd` (`arXiv:2609.02998`) on `task:student-distillation`. Prompt-level probes then dense OPD or GRPO. Does not replace CISPO or OPD.
- **Optional sparse OPD token mask**: `method:sparse-opd-supervision` (`arXiv:2609.04565`). Does not replace CISPO or OPD.
- **Optional OPD-then-RL stack**: `method:opd-then-rlvr` (`arXiv:2609.04108`) when both OPD and RLVR will run; sequence them, do not fuse in one step. Stage-2 Pass@1 algorithm stays CISPO. Does not replace CISPO or OPD.
- **No labels / no teacher**: `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. Does not replace CISPO when labels exist.
- **Olympiad NL proofs / IMO TTC (not this Pass@1 task)**: `method:nemotron-imo-gold` on `task:olympiad-math-posttrain`. Does not replace CISPO.
- **Optional partial-trace SFT shaping**: `method:partial-reasoning-traces` (`arXiv:2609.07103`). Does not replace CISPO or OLMo-3.

