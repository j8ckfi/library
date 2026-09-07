---
id: paper:pta
type: paper
title: "Persistent Teacher Anchoring for Tool-Using Agents"
authors:
  - "Hyun Bin Park"
  - "Kyungho Song"
  - "Sangmin Lee"
  - "Du-Seong Chang"
year: 2026
month: 9
arxiv_id: "2609.04773"
url: "https://arxiv.org/abs/2609.04773"
methods:
  - method:pta
cites:
  - paper:opd
  - paper:gkd
tags:
  - post-training
  - distillation
  - tool-use
  - opkd
  - pta
---

# Persistent Teacher Anchoring for Tool-Using Agents

## Abstract Summary
On-policy knowledge distillation (OPKD) matches the student to a teacher next-token distribution on student-generated trajectories, then hands the student to downstream RL. In tool use the teacher–student gap is not just text: a student-written call executes before supervision and its observation shapes later prefixes. Existing proposer-verifier methods govern retained text but leave tool execution outside their scope. Persistent Teacher Anchoring (PTA) is a student-induced but teacher-committed rollout: the student proposes chunks, the teacher verifies them (reject if outside teacher top-$K$), and a tool call reaches the environment only after the teacher has verified the whole turn. Verified chunks are atomic units, so persistent lookahead can fill idle rollout capacity and carry unfinished samples across student updates under a fixed verifier. Pre-RL PTA then Search-R1-style retrieval RL and DeepEyes-style perception RL improve macro best@4 by +2.5 / +2.8 vs OPKD under the same downstream RL budget; lookahead raises throughput 24%. Accepted to EMNLP 2026 Main. No official GitHub as of 2026-09-07.

## Key Contributions
1. **Turn-level commitment**: chunk-level teacher verification plus a pending-turn buffer; `Environment.step` runs only after the whole assistant turn is finalized.
2. **Student-induced, teacher-committed**: ~90% of committed assistant tokens stay student-proposed; rare in-call replacements (0.05% retrieval / 0.82% perception) are load-bearing — suppressing them collapses the gain.
3. **Source-aware OPKD**: KL only on committed assistant positions, not observations.
4. **Persistent lookahead**: verified chunk boundaries let the scheduler promote future samples ($T_{\mathrm{sched}}=(B+P)/(t^{\mathrm{gen}}+t^{\mathrm{update}})$); +24% throughput (0.519 → 0.644 samples/s).

## Empirical Highlights
- Retrieval (Qwen3-1.7B ← Qwen3-32B, Search-R1): PTA+RL macro best@4 34.59 vs OPKD+RL 32.07 vs Direct RL 32.66 vs base 30.77.
- Perception (Qwen3-VL-2B ← Qwen3-VL-32B, DeepEyes): PTA+RL macro best@4 70.00 vs OPKD+RL 67.20 vs Direct RL 68.10.
- Pre-RL perception checkpoint: PTA leads OPKD on all six metrics; HRBench8K best@4 65.00 vs 58.00.
- Lookahead: 20.2 promoted samples/step; 24% throughput.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-07. Paper implements PTA in veRL with SGLang by inserting teacher verification into the chunk-level generation loop (`recipe:pta`).
