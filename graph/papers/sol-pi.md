---
id: paper:sol-pi
type: paper
title: "SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness"
authors:
  - "Haozhe Liu"
  - "Tian Ye"
  - "Sensen Gao"
  - "Qihang Cao"
  - "Yitong Li"
  - "Mingchen Zhuge"
  - "Duomin Wang"
  - "Ruihua Zhang"
  - "Ping Luo"
  - "Jiawang Bian"
  - "Lei Zhu"
  - "Ligeng Zhu"
  - "Enze Xie"
  - "Song Han"
year: 2026
month: 9
arxiv_id: "2609.20519"
url: "https://arxiv.org/abs/2609.20519"
methods:
  - method:sol-pi
cites:
  - paper:harness-playbook
  - paper:neohorse-1
  - paper:mini-swe-agent
tags:
  - agents
  - agent-harness
  - rsi
  - token-efficiency
  - sol-pi
---

# SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

## Abstract Summary
Unattended coding agents spend tokens on long trajectories of reasoning, tools, and feedback. SoL-Pi runs RSI-inspired auto-research at the **harness** layer across many environments and keeps four mechanisms that transfer: Action Fusion (edit/write plus follow-up validation in one call), ObservationPack (large results as stable handles with paged recall), Evidence-Preserving Reducer (long logs → receipts whose quotations match the archive), and Online Context Compact (compact completed plan steps under economic/window checks). On 51-task EdgeBench, SoL-Pi matches Pi across GPT-5.6 Sol and Opus 5 while cutting recorded token traffic 44.7–49.0% and API cost about one third (about $8.75–$13.50/hour vs native Codex/Claude Code harnesses, $4.36–$5.71 vs Pi). Standalone Pi extension, MIT, not an official Pi distribution. Code: `https://github.com/NVlabs/SoL-Pi`.

## Key Contributions
1. **Harness-layer RSI**: scale auto-research loops to discover reusable efficiency mechanisms, not a new SWE start loop.
2. **Four surviving Pi mechanisms**: Action Fusion, ObservationPack, Evidence-Preserving Reducer, Online Context Compact.
3. **EdgeBench parity at much lower token traffic** on GPT-5.6 Sol and Opus 5.

## Empirical Highlights
- EdgeBench (51 tasks): Pi-comparable quality; token traffic −44.7–49.0%; API cost about −1/3.
- Estimated hourly savings: $8.75–$13.50 vs Codex/Claude Code native harnesses; $4.36–$5.71 vs Pi.

## Open Source Repository & Resources
- Code: `https://github.com/NVlabs/SoL-Pi`
- Project page: `https://nvlabs.github.io/SoL-Pi/`
- Install: `pi install git:github.com/NVlabs/SoL-Pi` on `@earendil-works/pi-coding-agent@0.85.1`. Mechanisms default off.
