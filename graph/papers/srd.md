---
id: paper:srd
type: paper
title: "Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight"
authors:
  - "Haoxiang Zhang"
  - "Qinglin Chen"
  - "Hiroaki Hayashi"
  - "Zhuofeng Li"
  - "Siming Zhang"
  - "Jiaxin Zhang"
  - "Jixuan Chen"
  - "Fang Wu"
  - "Pan Lu"
  - "Silvio Savarese"
  - "Julian McAuley"
  - "Chien-Sheng Wu"
year: 2026
month: 10
arxiv_id: "2610.08077"
url: "https://arxiv.org/abs/2610.08077"
methods:
  - method:srd
cites:
  - paper:grpo
  - paper:vista
  - paper:flowbalance
  - paper:verigate
tags:
  - post-training
  - rlvr
  - distillation
  - srd
  - silent-groups
---

# Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

## Abstract Summary
Group-relative RLVR gets a zero advantage when every rollout in the group has the same reward, even if the traces still show what the task needs and how the agent fails. SRD treats completed traces as privileged hindsight and distills that into trajectory-blind foresight of the same policy before the next act. Across 10 tool-integrated and long-horizon tasks, gains up to 24.2 pp. In a 2B setting where 98% of groups are all-failure, RLVR ends at 0.0% success while adding SRD reaches 60.6% under the same rollout budget. Top HF Daily paper 2026-10-08. Code: SalesforceAIResearch/SRD. Beside CISPO / VISTA / VeriGate / FlowBalance.

## Key Contributions
1. All-equal group rewards starve GRPO-family advantages; traces still contain usable structure.
2. Prospective learning: hindsight of a finished trajectory supervises foresight from the pre-interaction view.
3. Same-policy distillation; no extra teacher. Foresight is a train target, not required at inference.

## Empirical Highlights
- 10 tool-integrated reasoning and long-horizon agentic tasks; gains up to 24.2 pp vs RLVR / self-distillation.
- 2B, 98% all-failure groups: RLVR 0.0% vs SRD 60.6% at the same rollout budget.
- Top HF Daily paper 2026-10-08.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08077`
- Code: `https://github.com/SalesforceAIResearch/SRD` (`code_status: released`).
