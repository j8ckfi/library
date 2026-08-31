---
id: paper:laguna-m1-xs2
type: paper
title: "Laguna M.1/XS.2 Technical Report"
authors:
  - "Poolside team"
  - "research@poolside.ai"
year: 2026
month: 5
arxiv_id: "2605.27605"
url: "https://arxiv.org/abs/2605.27605"
methods:
  - method:poolside-model-factory
  - method:automixer
  - method:blender-streaming
  - method:hive-synth
cites:
  - paper:minimax-m1
  - paper:muon-scalable
tags:
  - systems
  - training-systems
  - model-factory
  - moe
  - coding
  - laguna
---

# Laguna M.1/XS.2 Technical Report

## Abstract Summary
Poolside presents Laguna M.1 and Laguna XS.2, two Mixture-of-Experts foundation models built for long-horizon agentic coding, together with the Model Factory process that produced them. M.1 has 225.8B total parameters (23.4B activated per token); XS.2 has 33.4B total (3B activated). Both were trained from scratch end-to-end inside one internal stack of versioned data, training, evaluation, and inference. XS.2 was started just after M.1 pretraining finished; start-of-training to Apache-2.0 release spanned five weeks. Both models trained on more than 30T pretraining tokens. M.1 used 6144 NVIDIA H200s; XS.2 used 2048. The factory used Muon (Moonlight variant) across stages and CISPO for online RL with verifiable rewards. Laguna is a **coding MoE**; it is not the library's MoE architecture default (`method:deepseek-v4` / `method:kimi-k3` stay).

XS.2 weights: Apache-2.0 at https://huggingface.co/collections/poolside/laguna-xs2. PDF: https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf. Hub: https://poolside.ai/research.

## Key Contributions
1. **Model Factory principles (§2)**: (1) experiments as code with a Dagster DAG control plane and two-way lineage; (2) composable decoupled components, one research+production codebase; (3) reserve human attention for novel decisions (custom scheduler, auto-recovery, cross-replica hash checks).
2. **Named factory machines**: Spark/Iceberg ingest (~20T tok/day at Poolside), Blender streaming mixes, Titan (PyTorch trainer seeded from TorchTitan, 2200+ patches), Atlas (vLLM-based infer on NVIDIA/AMD/Trainium), Hive declarative synth, AutoMixer proxy-swarm mix search, ~1M-repo OCI code-exec, Podium dataset/model viewer, GPU↔GPU NCCL P2P weight sync for online RL.
3. **Train kernels unchanged**: Laguna ran Muon (Moonlight) and CISPO on the factory stack. Those remain the library's train defaults; the paper is evidence they compose with a factory process, not a retarget.
4. **Coding MoE artifacts**: architecture, >30T-token mix, post-training, and quantization for a coding MoE family. Do not treat Laguna as the frontier MoE template.

## Empirical Highlights
- M.1: 225.8B / 23.4B active; 6144 H200. XS.2: 33.4B / 3B active; 2048 H200. Cluster on the order of 10k H200s.
- XS.2 from-scratch factory cycle after M.1: five weeks to Apache-2.0.
- Pretrain corpus sampled from ~27T unique tokens; both models trained on >30T tokens.
- AutoMixer (component, not the open-data default): ~60 proxy 0.5B MoEs on ~60B tokens; reported HumanEval+ +43% vs a hand mix, with small commonsense regressions. XS.2 mix: raw code 30.6%, web 25.2%, synth/code-text 25.4%, math 9.0%, knowledge 6.6%, rest small.
- Distributed Muon in Titan: optimizer overhead <1% of M.1 step time.
- Agent-coding SWE-bench numbers are in the report figures; this library does not restate them here.

## Accompanying factory blogs (2025; no arXiv IDs)
Schema requires `arxiv_id`, so these are cited from method cards rather than as paper nodes:
1. https://poolside.ai/blog/introducing-the-model-factory (2025-07-17)
2. https://poolside.ai/blog/gathering-and-processing-raw-materials-for-the-model-factory (2025-07-29)
3. https://poolside.ai/blog/titan-the-model-factory-s-furnace (2025-08-07)
4. https://poolside.ai/blog/designing-a-world-class-code-execution-environment (2025-08-12)
5. https://poolside.ai/blog/the-carrier-and-the-beacon (2025-08-14)
6. https://poolside.ai/blog/post-training-in-the-model-factory (2025-08-25)
