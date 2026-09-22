---
id: paper:harness-zero
type: paper
title: "Harness-Zero: Harness Distillation via Agent-as-Harness"
authors:
  - "Haoran Ye"
  - "Yuxing Lu"
  - "Haonan Dong"
  - "Zhaochen Su"
  - "Guojie Song"
year: 2026
month: 9
arxiv_id: "2609.24974"
url: "https://arxiv.org/abs/2609.24974"
methods:
  - method:harness-zero
cites:
  - paper:mini-swe-agent
  - paper:opd
  - paper:open-mopd
  - paper:neohorse-1
  - paper:harness-playbook
  - paper:harness-onpolicy-correction
  - paper:sao
tags:
  - agents
  - agent-harness
  - distillation
  - harness-zero
---

# Harness-Zero: Harness Distillation via Agent-as-Harness

## Abstract Summary
Optimized agent harnesses raise task success, but the gains stay attached to that harness at deployment. Because the best harness varies by domain, instance, and model, a general-purpose agent either accepts a shared suboptimal harness or routes among many specialized ones. Harness distillation uses a domain- or instance-optimized harness as training-time guidance and transfers the behaviors it induces into weights, so the gains survive under a single fixed target harness. Source and target harnesses differ in action space and available information, so source trajectories are not valid imitation targets. Harness-Zero wraps the student with a harnessing agent (agent-as-harness): guided by an adapted private reference harness, it PASS/REPLACE-corrects each student reply into the target action space before execution. SFT on the reviewed trajectories internalizes the behavior; the specialized harness is removed at deploy.

## Key Contributions
1. **Harness distillation as a task**: move optimized-harness behaviors into weights under a fixed target harness (mini-SWE-agent-style bash).
2. **Agent-as-harness**: a harnessing agent re-expresses optimized-harness guidance as executable corrections in the student's action space.
3. **Deploy without the specialized harness**: distilled student under the target harness alone can beat the base model that still has the evolved harness attached.

## Empirical Highlights
- Frontier, no training: agent-as-harness 81.1% vs code-as-harness / meta-harness 78.1% vs mini-SWE-agent 68.6% (six benchmark–model settings).
- Qwen3.5-9B distillation, specialized harness removed: macro success 23.3% → 44.3% (SpreadsheetBench 44.0 / AppWorld 58.9 / USPTO 30.0) vs 41.7% with the evolved harness still attached.
- Recovers 82.3% of 28 harness-exclusive patterns (memory, skill, tool, middleware).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.24974`
- Code: `https://github.com/metaevo-ai/harness-zero` (`code_status: released`; Harbor rollouts, Tinker SFT).
- Models: Hugging Face `metaevo-ai`.
