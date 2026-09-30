---
id: paper:graft
type: paper
title: "Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR"
authors:
  - "Doohyuk Jang"
  - "Yoonsik Park"
  - "Gyouk Chu"
  - "Sihwan Park"
  - "Eunho Yang"
year: 2026
month: 9
arxiv_id: "2609.37868"
url: "https://arxiv.org/abs/2609.37868"
methods:
  - method:graft
cites: []
tags:
  - post-training
  - rlvr
  - off-policy
  - graft
---

# Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR

## Abstract Summary
GRPO all-fail groups contribute no policy-gradient signal. Heterogeneous peers often succeed on complementary prompts (SmolLM3 solves 47.9% of Qwen3-1.7B all-fail prompts; reverse 18.7%). GRAFT (Gated Replacement of Answer-Failed groups with peer Trajectories) replaces a receiver all-fail group with a mixed peer group, keeps source-computed advantages, and controls mismatch with sequence-level compatibility weighting plus token-level IS clip, processing peer minibatches after on-policy ones. +2.1 average over equal-budget GRPO across three heterogeneous pairs; stored peer trajectories from finished independent runs still +1.8 without co-training. Distinct from VeriGate (PRM gating on all-zero groups) and from HACPO / SGT. KAIST / AITRICS. No public GitHub as of 2026-09-30.

## Key Contributions
1. **Where**: transfer only when the receiver is all-fail and the peer has mixed success, with balanced exchange volume.
2. **How**: source advantages (no cross-model reward pooling); compatibility gate + token IS clip; peer-last updates.
3. **Offline reuse**: stored peer groups recover most of the live co-train gain.

## Empirical Highlights
- Three pairs, five math benches, \(n=8\): +2.1 avg over GRPO; Pair 1 SmolLM3-3B 32.60→37.06 (+4.46), Qwen3-1.7B 31.20→33.44 (+2.24). Up to +4.5 model-level.
- Two of three pairs match or beat GRPO \(n=32\) at \(n=8\) GRAFT. Beats HACPO / SGT by 4.0 / 1.5 avg.
- Stored-peer +1.8 over GRPO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.37868`
- Code: none found as of 2026-09-30 (`code_status: none`).
