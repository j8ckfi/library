---
id: paper:mintrl
type: paper
title: "MInTRL: Off-policy Intervention can boost On-policy RL"
authors:
  - "Mingyu Chen"
  - "Yefan Tao"
  - "Gerald Friedland"
  - "Xuezhou Zhang"
  - "Chris Kong"
year: 2026
month: 9
arxiv_id: "2609.12419"
url: "https://arxiv.org/abs/2609.12419"
methods:
  - method:mintrl
cites:
  - paper:grpo
  - paper:opd
  - paper:minimax-m1
tags:
  - post-training
  - rl-alignment
  - rlvr
  - mintrl
  - exploration
---

# MInTRL: Off-policy Intervention can boost On-policy RL

## Abstract Summary
RLVR is typically on-policy, which keeps training data close to the current policy but limits learning to trajectories the policy can discover. Off-policy methods can inject external knowledge at the cost of large distribution shift. Minimal Intervention Reinforcement Learning (MInTRL) expands the exploration frontier with sparse, local interventions inside otherwise on-policy rollouts. A judge-intervention policy periodically reviews the current policy's output, replaces erroneous suffixes with short corrections, and immediately returns control. Training uses a sequence-level advantage-regression objective that avoids importance sampling. Performance peaks at moderate intervention intensity.

## Key Contributions
1. **Semi-on-policy rollouts**: Keep / Revise loop; Revise rewrites a short suffix then resumes the student.
2. **Advantage regression**: no IS ratios on mixed-policy trajectories; MInTRL-Const vs MInTRL-Proxy anchors on intervention tokens.
3. **Minimal intensity**: non-monotonic Pass@1 vs off-policy token fraction; self-intervention also works.

## Empirical Highlights
- Qwen3-1.7B (non-thinking): MInTRL-Const math avg 35.45 / code avg 61.95. Gains of +13.61 / +14.12 vs the stronger of GRPO and OPD.
- Qwen3-4B: MInTRL-Const math 55.73 / code 72.63 (+3.02 / +6.80 vs those two baselines).
- Judge is Qwen3-4B-Instruct-2507. Math data: AceReason-Nemotron subset. Code: DeepCoder-Preview. Eval: AIME25/AIME26/HMMT25 and LiveCodeBench/HumanEval+/MBPP+; 32 samples as Pass@1.
- Paper contribution line also states up to +9.44 pp over the strongest competitor. Long-horizon agentic evaluation is listed as future work.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-14.
