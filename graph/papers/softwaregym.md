---
id: paper:softwaregym
type: paper
title: 'SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments'
authors:
- Tian Jin
- Wenhao Wang
- Jing Kang
- Haoting Shi
- Rui Ye
- Yijun Lu
- Siheng Chen
year: 2026
month: 10
arxiv_id: '2610.12611'
url: https://arxiv.org/abs/2610.12611
methods:
- method:softwaregym
cites:
  - paper:recreationworld
  - paper:osworld-2
tags:
- agents
- computer-use
- environments
- softwaregym
---

# SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments

## Abstract Summary
Native app envs are expensive to build; browser-hosted envs are shallow. SoftwareGym synthesizes structurally diverse GUI apps, realizes them as runnable software, and repairs them with GUI evaluation until they pass. 182 apps / 12 categories. Trajectories from those envs train a CUA that transfers Pass@3 41.39→56.97 on strictly OOD OSWorld.

## Key Contributions
1. Automated synthesize → realize → GUI-eval repair loop for CUA envs.
2. 182 apps, 91.5% mean GUI task pass; 120-task SoftwareGym-Bench.
3. OOD OSWorld Pass@3 +15.58pp after training on synthesized trajectories.

## Empirical Highlights
- See `method:softwaregym` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12611`
- Code: `none found` (`code_status: none`).
