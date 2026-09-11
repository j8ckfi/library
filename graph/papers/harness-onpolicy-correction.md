---
id: paper:harness-onpolicy-correction
type: paper
title: "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails"
authors:
  - "Zhou Yu"
  - "Bin Bi"
  - "Shiva Kumar Pentyala"
  - "Shubham Mehrotra"
  - "Sougata Chaudhuri"
  - "Shilpa Bhagavath"
  - "Zeyuan Chen"
  - "Ran Xu"
  - "Phil Mui"
  - "James Zhu"
  - "Sitaram Asur"
year: 2026
month: 9
arxiv_id: "2609.09134"
url: "https://arxiv.org/abs/2609.09134"
methods:
  - method:harness-onpolicy-correction
cites: []
tags:
  - agents
  - agent-harness
  - sft
  - on-policy
  - harness-evolution
---

# Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails

## Abstract Summary
After a harness is evolved around a weaker model, LoRA-SFT on full expert trajectories under that evolved harness regresses on all seven enterprise agent tasks (−4 to −30 points; Qwen3-Coder 30B-A3B and Gemma 4 26B-A4B). The same imitation helps under the unevolved baseline harness. Imitation transfers knowledge and increases scaffold usage but breaks model–harness fit: the student adopts the expert's plan without the competence to run it. The fix is on-policy expert correction: localize the failing turn in the student's own rollout and have the expert rewrite only that turn. A meta-level MLE agent automates the pipeline. No official code.

## Key Contributions
1. **Gotcha**: full-trajectory expert SFT after model-specific harness evolution regresses.
2. **On-policy turn rewrite**: expert edits the failing student turn only, preserving native planning style.
3. **Composition**: harness evolution and lightweight weight updates can stack when the imitation target stays on-policy.

## Empirical Highlights
- Full expert-trajectory LoRA-SFT after harness evolution: −4 to −30 points on all seven tasks, both model families.
- Same procedure helps under the baseline (unevolved) harness.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-11.
