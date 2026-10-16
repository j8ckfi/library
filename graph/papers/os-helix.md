---
id: paper:os-helix
type: paper
title: 'OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents'
authors:
- Bowen Yang
- Kaiming Jin
- Zichen Ding
- Zhenyu Wu
- Zehao Li
- Zhoumianze Liu
- Kanzhi Cheng
- Fangzhi Xu
- Yanan Sun
- Qiushi Sun
- Yu Qiao
year: 2026
month: 10
arxiv_id: '2610.22234'
url: https://arxiv.org/abs/2610.22234
methods:
- method:os-helix
cites:
- paper:recreationworld
- paper:opengcua
tags:
- computer-use
- hybrid
---

# OS-Helix

## Abstract Summary
Naively adding a code tool to a GUI agent degrades it. OS-Helix trains GUI and code in one action space: application-artifact composition, decoupled instruction/evaluator generation, SFT on filtered hybrid data, then online RL with Step-balanced GSPO so long code actions do not dominate.

## Key Contributions
1. Native GUI+code action space via training, not prompting.
2. Step-balanced GSPO (importance by action step, not token count).
3. OSWorld-Verified 27B/35B-A3B plus WindowsAgentArena transfer.

## Empirical Highlights
- OS-Helix-27B / 35B-A3B +35.0% / +33.7% relative vs matched Qwen3.5 hybrid baselines.
- OS-Helix-27B-RL 66.44% OSWorld-Verified (not OSWorld 2.0 protocol).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22234`
- Project: `https://os-copilot.github.io/OS-Helix/`
- Code: `https://github.com/os-copilot/OS-Helix` (`code_status: released`).

