---
id: paper:mac-meta-agent
type: paper
title: "The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?"
authors:
  - "Xinyu Lu"
  - "Tianshu Wang"
  - "Pengbo Wang"
  - "Zujie Wen"
  - "Zhiqiang Zhang"
  - "Jun Zhou"
  - "Boxi Cao"
  - "Yaojie Lu"
year: 2026
month: 6
arxiv_id: "2606.04455"
url: "https://arxiv.org/abs/2606.04455"
methods:
  - method:single-agent-plus-tools
  - method:mini-swe-agent
cites:
  - paper:openhands
  - paper:mini-swe-agent
tags:
  - agents
  - meta-agent
  - mac
---

# The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?

## Abstract Summary
MAC gives code agents 12–24 hours to write an agent. Only **5/39** configs beat a human baseline. Successful artifacts converge on **simple ReAct loops**. They fail to beat Terminus-2 / OpenHands. This is why the library's first hop for "build an agent" is mini-SWE-agent, not meta-agent search.

## Key Contributions
1. Meta-agent challenge protocol (12–24h autonomous agent development).
2. Empirical failure of agent-designed agents: 5/39 beat human baseline.
3. Successful artifacts collapse to simple ReAct; they do not beat Terminus-2 / OpenHands.

## Empirical Highlights
- 5/39 configs beat the human baseline.
- Winning designs are simple ReAct loops, not planner-coder-tester graphs.
