---
id: paper:eapo
type: paper
title: "Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning"
authors:
  - "Woongyeong Yeo"
  - "Minki Kang"
  - "Chanuk Lee"
  - "Sangwoo Park"
  - "Jinheon Baek"
  - "Sung Ju Hwang"
year: 2026
month: 9
arxiv_id: "2609.33781"
url: "https://arxiv.org/abs/2609.33781"
methods:
  - method:eapo
cites: []
tags:
  - post-training
  - rlvr
  - exploration
  - credit-assignment
  - eapo
---

# Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning

## Abstract Summary
Outcome RLVR shares one group-normalized advantage across every token. Entropy-guided methods that treat uncertainty the same way under success and failure put the strongest penalties on high-entropy positions in failed traces, where alternatives for recovery still exist. Entropic Advantage Policy Optimization (EAPO) redistributes the response advantage with a sign–entropy coupling: reinforce high-entropy tokens on success, penalize low-entropy tokens on failure, and attenuate penalties at uncertain positions in fails. Batch-percentile entropy normalization; no auxiliary model, extra sampling, or privileged information. Best overall vs GRPO / EntropyAdv / HAPO / 80-20 / RLRT on math and Reasoning Gym. KAIST / DeepAuto.ai. Code: `https://github.com/wgcyeo/EAPO`. Project: `https://eapo-explore.github.io`.

## Key Contributions
1. **Asymmetry**: high-entropy success is less repeatable; low-entropy failure recurs; failed high-entropy windows still recover.
2. **Signed-entropy weights**: \(w_{i,t}\propto\exp(\kappa\,\mathrm{sign}(\hat{A}^i)h_{i,t})\) mean-normalized within the response; \(\hat{A}_t^{i,\mathrm{E}}=\hat{A}^i w_{i,t}\).
3. **Drop-in GRPO surrogate**: replace the shared response advantage; host Pass@1 algorithm stays CISPO.

## Empirical Highlights
- Qwen3-4B-Base six-bench mean Avg@32 31.0 (+5.6 vs EntropyAdv). Qwen3-8B-Base 34.0 (+4.3 vs 80/20).
- Qwen3-4B reasoning backbone 72.4; Olmo-3-7B-Think-DPO 74.3.
- Reasoning Gym 34.89 / 43.02. Broader problem coverage under test-time sampling budgets.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.33781`
- Code: `https://github.com/wgcyeo/EAPO` (`code_status: released`).
- Project: `https://eapo-explore.github.io`
