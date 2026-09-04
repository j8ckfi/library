---
id: paper:canopy
type: paper
title: "Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents"
authors:
  - "Liming Pu"
  - "Xiaoxia Li"
  - "Yifu Liu"
  - "Teng Cao"
  - "Bin Yang"
year: 2026
month: 9
arxiv_id: "2609.01245"
url: "https://arxiv.org/abs/2609.01245"
methods:
  - method:canopy
cites:
  - paper:grpo
  - paper:dapo
  - paper:sao
  - paper:foldgrpo
tags:
  - post-training
  - agentic
  - outcome-only
  - canopy
---

# Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents

## Abstract Summary
The apparent ceiling of outcome-only RL on small open agent models is an artifact of two failures: signal starvation (group-relative gradients vanish unless a same-task group mixes success and failure) and policy drift (repeated updates on a small task pool collapse the sampling distribution exactly when informative groups become rare). CANOPY (Coverage-ANchored On-PolicY RL) scales same-task exploration until the sparse signal reappears, keeps every update on-policy and KL-anchored over action tokens only, and transfers an enlarged turn/context budget at test time. A Qwen3-14B policy trained by environment interaction alone topped the AppWorld public leaderboard (Feb 2026; Test-Normal TGC 86.9, Test-Challenge 67.6). The same design principles lift Qwen3.5-9B on SWE-bench Verified by 16.6 points mean@4.

## Key Contributions
1. **Signal coverage** $P_{\mathrm{sig}}(p,n)=1-p^n-(1-p)^n$: size $n$ from a pilot $\hat{p}_{\min}$; keep the hardest tier; uncap per-turn generation.
2. **Drift less**: one update per rollout batch (importance ratio identically 1), sparse fully-correct reward, pooled token-mean loss over action tokens, light KL to the base model, fault quarantine of serving-layer failures.
3. **Test-time budget transfer**: train at a moderate turn/context budget, evaluate at a larger one without search.
4. **Position**: denser rewards / SFT priors / skill libraries are compensations for under-exploration, not a property of outcome-only RL.

## Empirical Highlights
- AppWorld Qwen3-14B (Feb 2026 leaderboard, mean@1, 100 turns / 61k): Test-Normal TGC 86.9 / SGC 80.4; Test-Challenge TGC 67.6 / SGC 50.4. Next trained policy ESAT 75.2 / 58.5 on the same backbone.
- Base at the same enlarged budget: Test-Normal mean@4 32.4 vs CANOPY 83.2 (leaderboard m@1 86.9).
- SWE-bench Verified, Qwen3.5-9B, mini-swe-agent: mean@4 31.3 -> 47.9 (+16.6) at matched 80-turn / 36k budget; enlarged budget 50.2.
- Unanchored run: entropy collapses to 0.038 past step ~70, Dev stalls at 81.6; KL-anchored entropy 0.217, Dev 87.3 at step 90.
- Group size n=32 on AppWorld (2,880 rollouts/step); n=16 on SWE because episodes cost more.

## Open Source Repository & Resources
- Planned / listed: `https://github.com/AlibabaResearch/SignalCoverageRL`. Training stack: veRL + SGLang rollouts + Megatron.
