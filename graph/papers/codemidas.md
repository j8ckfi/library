---
id: paper:codemidas
type: paper
title: "CodeMidas: Scaling Agentic Coding RL Environments from Code Itself"
authors:
  - "Bowen Ye"
  - "Lei Li"
  - "Shicheng Li"
  - "Zihao Yue"
  - "Linghao Zhang"
  - "Hanglong Lv"
  - "Yuanxin Liu"
  - "Wenhan Ma"
  - "Hao Tian"
  - "Rang Li"
  - "Jinhao Dong"
  - "Yikai Zhao"
  - "Xiangwei Deng"
  - "Hailin Zhang"
  - "Liang Zhao"
  - "Qi Liu"
  - "Lingpeng Kong"
  - "Tong Yang"
  - "Fuli Luo"
year: 2026
month: 9
arxiv_id: "2609.22068"
url: "https://arxiv.org/abs/2609.22068"
methods:
  - method:codemidas
cites:
  - paper:grpo
  - paper:canopy
  - paper:sao
  - paper:mini-swe-agent
tags:
  - post-training
  - agentic
  - coding-rl
  - environments
  - codemidas
---

# CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

## Abstract Summary
Coding-agent RL needs diverse tasks with reliable verifiers. Most pipelines seed those tasks from issues, PRs, commits, existing tests, or documentation. CodeMidas (Xiaomi MiMo) uses source code as the only task-specific input: agents explore implemented functionality, write behavioral specifications, build tests grounded in execution of the original code, then filter candidates with execution checks and repeated solution rollouts. The resulting set has 5,545 training tasks from 3,185 open-source codebases across 23 languages and 15 technical domains. Training MiMo-V2.5 with GRPO on these tasks lifts issue repair, whole-program construction, code translation, and terminal work.

## Key Contributions
1. **Code-only env construction**: behavioral specs and execution-grounded tests without issues, PRs, commits, existing tests, or written descriptions.
2. **Filter stack**: fail-to-pass execution consistency, adversarial leakage checks, solution-audit of verifier verdicts, and mixed pass/fail rollout filtering.
3. **Transfer across software work**: GRPO on the constructed tasks improves five external coding-agent benches.

## Empirical Highlights
- Dataset: 5,545 tasks / 3,185 repos / 23 languages; median reference patch 142 lines; 65.9% touch at least two files.
- MiMo-V2.5 GRPO: DeepSWE 10.0→21.7, ProgramBench Almost Solved 4.5→21.5, Terminal-Bench v2.1 63.7→72.2 (+8.5 pp), SWE-bench Pro 50.3→54.4, RepoZero C2Rust 40.5→51.8.
- High-quality 5,545 beats a vanilla 8k unfiltered pool on SWE-bench Pro, DeepSWE, and CodeMidas Val.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.22068`
- Project: `https://mimo.xiaomi.com/rl/` (live MiMo RL dashboard as of 2026-09-21; not a public trainer or dataset GitHub).
- No public GitHub found as of 2026-09-21 (`recipe:codemidas` `code_status: none`).
