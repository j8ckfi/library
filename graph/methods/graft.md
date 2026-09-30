---
id: method:graft
type: method
title: "GRAFT"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "GRAFT salvages all-fail groups with peer trajectories; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "gating a trained PRM behind outcome verification on all-zero groups"
    reason: "VeriGate gates process rewards; GRAFT replaces the group with a peer's rollouts"
    use_instead: "method:verigate"
  - when: "choosing the frontier post-train engine"
    reason: "Miles is the stack; GRAFT is a multi-model data exchange on a GRPO-family host"
    use_instead: "method:miles"
  - when: "single-teacher distillation is the goal"
    reason: "GRAFT exchanges verified peer traces, not teacher log-probabilities"
    use_instead: "method:opd"
assumptions:
  - "Two (or more) heterogeneous policies on the same prompt distribution with a binary verifier. Paper: three pairs including SmolLM3-3B-Base × Qwen3-1.7B-Base, n=8, five math benches."
  - "Transfer only receiver all-fail × peer mixed-success groups. Keep source advantages. Sequence compatibility + token IS clip. Peer minibatches after on-policy ones."
  - "No public GitHub as of 2026-09-30. Tokenizers may differ; compatibility is an empirical logp proxy, not an exact cross-tokenizer IS ratio."
last_reviewed: "2026-09-30"
papers:
  - paper:graft
recipes:
  - recipe:graft
claims:
  - benchmark: "Three heterogeneous pairs, five math benches, n=8 vs GRPO n=8"
    metric: "mean score lift"
    value: "+2.1"
    baseline: "Pair 1 SmolLM3-3B 32.60→37.06 (+4.46), Qwen3-1.7B 31.20→33.44 (+2.24); up to +4.5 model-level"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37868"
    notes: "Two of three pairs match or beat GRPO n=32. Beats HACPO / SGT by 4.0 / 1.5. Not a CISPO or VeriGate retarget."
  - benchmark: "Stored peer trajectories from finished independent GRPO runs"
    metric: "mean score lift vs GRPO"
    value: "+1.8"
    baseline: "no simultaneous co-training, no extra peer rollouts"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37868"
    notes: "Offline reuse recovers most of the live co-train gain."
tags:
  - post-training
  - rlvr
  - off-policy
  - graft
  - active
---

# GRAFT

## Method Overview
GRPO all-fail groups have zero advantage. GRAFT gates replacement: if receiver \(B\) has \(k_B(q)=0\) and peer \(A\) has mixed success, swap in \(\mathcal{G}_A(q)\) with source advantages \(\hat{a}^A\), reweight sequences by a bounded compatibility score from receiver log-likelihoods, and clip token IS ratios of \(\pi^B\) vs the stored peer tokens. On-policy minibatches run first; peer-containing minibatches second. Distinct from VeriGate (PRM on all-zero groups, same model) and from HACPO (shares beyond failures) / SGT (NLL on one verified success).

## When to Use
- Multi-model RLVR where heterogeneous peers solve complementary prompts and all-fail groups waste the rollout budget.

## When NOT to Use
- Pass@1 default → `method:cispo`. Same-model PRM gating → `method:verigate`. Production engine → `method:miles`. Teacher distillation → `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` with a mention on `task:all-zero-verifier-groups`. Does **not** enter `current_sota`. Does **not** replace CISPO, VeriGate, Miles, or OPD.

## Gotchas & Failure Modes
- Needs a peer (live co-train or a stored run). One model is not GRAFT.
- Do not pool rewards across models. Source advantages keep within-peer contrast.
- Cross-tokenizer compatibility is a proxy. Tight token IS clips still matter.
- Sharing on prompts that already have on-policy signal is HACPO's setting and lost in this paper.
