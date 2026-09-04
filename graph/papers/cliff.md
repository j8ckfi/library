---
id: paper:cliff
type: paper
title: "Cliff: Learning Process Rewards from the First Mistake"
authors:
  - "Peixuan Han"
  - "Runhui Wang"
  - "Ketan Ramaneti"
  - "Jie Hao"
  - "Gerald Friedland"
  - "Chris Kong"
year: 2026
month: 9
arxiv_id: "2609.02817"
url: "https://arxiv.org/abs/2609.02817"
methods:
  - method:cliff
cites:
  - paper:grpo
  - paper:dapo
  - paper:opd
tags:
  - post-training
  - rlvr
  - process-supervision
  - cliff
---

# Cliff: Learning Process Rewards from the First Mistake

## Abstract Summary
RLVR's outcome reward cannot tell a nearly-correct trace from a fully wrong one. Cliff uses an off-the-shelf teacher to find the first mistake (Pitfall Step), splits the rollout into a correct prefix and an incorrect suffix, and converts that split into token-level advantages for GRPO/DAPO-style trainers. It is not a process reward model: no extra RM is trained, and the teacher is used as a first-error locator. Across 12 math/code scenarios, Cliff reports +15% vs OPD and +7% vs GRPO, including with modest teachers. Default prefix weight is λ=0 to avoid length hacking.

## Key Contributions
1. **Pitfall Step**: only the first error is localized; later tokens already sit on an invalid prefix.
2. **Token-level advantages**: correct rollouts keep A_cor; incorrect prefixes get λ A_cor (paper default λ=0); incorrect suffixes keep A_inc; then zero-mean recenter with offset b.
3. **Teacher filter**: skip teacher guidance (fall back to GRPO) when the teacher's own reference solution fails the verifier.
4. **Not a PRM**: judging first-error location is easier than solving, and postponing a mistake is always better than making it earlier.

## Empirical Highlights
- Qwen3-4B math avg (GSM8k / MATH-500 / DAPO / AIME) with SOTA teacher: Cliff 65.66 vs GRPO 61.68 vs Distill 58.58.
- Qwen3-4B + Qwen3-32B teacher: Cliff math 64.62 vs GRPO 61.20 vs OPD 58.17.
- Qwen3-4B coding avg with SOTA teacher: Cliff 25.96 vs GRPO 24.20.
- Phi-4-mini math with SOTA teacher: Cliff 51.73 vs GRPO 49.78.
- GRPO-with-teacher (same teacher, no Pitfall split) is only a marginal lift; the credit split is the gain.
- Judge vs human Pitfall distance: SOTA avg p-dis 1.23 sentences (82% within 1); Qwen3-32B 3.00 (68% within 1) when the teacher writes its own reference.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-04. Training described as veRL; λ=0. Recipe is Algorithm 3.2 in the paper (`recipe:cliff`).
