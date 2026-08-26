# j8ckfi/library

> Sprawling, agent-navigable knowledge graph of cutting-edge machine learning research, SOTA methods, primary literature, and executable training recipes (As-of: 2026-08-26).

---

## 1. Overview

`j8ckfi/library` is a machine-readable knowledge graph and zero-dependency CLI engine designed for autonomous training agents and ML engineers. When tasked with *"train model X to do Y"*, agents query this graph to identify current, date-stamped SOTA methods, read empirical validation claims, trace arXiv papers, and pull runnable PyTorch/JAX recipes in a few hops.

```
+---------------+        has_sota_method       +-----------------+
|     Task      | ───────────────────────────> │     Method      |
| (task:<slug>) │ <─────────────────────────── │ (method:<slug>) │
+---------------+           sota_for           +-----------------+
        │                                               │
        │ recipe_for_task                 described_in  │ implements
        ▼                                               ▼
+---------------+                              +-----------------+
|    Recipe     | ───────────────────────────> │      Paper      |
|(recipe:<slug>)|          implements          | (paper:<slug>)  |
+---------------+                              +-----------------+
```

---

## 2. Agent Routing Cheat-Sheet (2026-08-26 SOTA Index)

```
task: pretrain dense 7B     -> muon-scalable  (+ soap-muon-scale if big batch / extra mem)
task: pretrain MoE          -> deepseek-v3 arch, muonclip-kimi-k2 opt; read kimi-k3 if 2026-frontier
task: open data recipe      -> olmo-2-curriculum
task: instruct SFT          -> tulu3-rlvr (SFT stage)
task: general alignment     -> tulu3-rlvr (SFT->DPO->RLVR)
task: math/code RL, dense   -> dapo + dr-grpo
task: math/code RL, MoE     -> gspo + dr-grpo
task: process supervision   -> verigate (not un-gated PRM)
task: LoRA 24GB             -> qlora; quality: dora or delora
task: full-param, 24GB      -> galore
task: tiny on-device LLM    -> bitnet-b158 (from-scratch) else qlora+GGUF
task: distill student       -> on-policy-distillation
task: SNN audio/event       -> silif
task: SAE / circuits        -> sasa
task: neural video train    -> dcvcrt
task: continuous control    -> td-mpc2, then dream-mpc planner
```

---

## 3. SOTA Method Map (What You Actually Pick Today)

| Task / Domain | Default SOTA Method | Key Paper / Reference | Code / Repo |
| :--- | :--- | :--- | :--- |
| **Dense 7B Pretraining** | **Scalable Muon** (`method:muon-scalable`) | Moonshot AI `arXiv:2502.16982` | `https://github.com/MoonshotAI/Moonlight` |
| **Large-Batch Pretraining**| **KL-SOAP** (`method:soap-muon-scale`) | NVIDIA `arXiv:2607.20548` | `https://github.com/NVIDIA-NeMo/Emerging-Optimizers` |
| **Frontier MoE Pretrain** | **Kimi-K3** / **DeepSeek-V3** | `arXiv:2607.24653` / `2412.19437` | `https://github.com/MoonshotAI/Kimi-K3` |
| **Open Data Recipe** | **OLMo 2 Curriculum** | AI2 `arXiv:2501.00656` | `https://github.com/allenai/OLMo` |
| **Instruct / Chat SFT** | **Tülu-3 Stack** (`method:tulu3-rlvr`) | AI2 `arXiv:2411.15124` | `https://github.com/allenai/open-instruct` |
| **Dense Math/Code RL** | **DAPO** + **Dr. GRPO** | `arXiv:2503.14476` / `2503.20783` | `https://github.com/BytedTsinghua-SIA/DAPO` |
| **MoE Reasoning RL** | **GSPO** + **Dr. GRPO** | `arXiv:2507.18071` / `2503.20783` | Hugging Face TRL & Qwen Stacks |
| **Process Supervision** | **VeriGate** (Gated PRM) | `arXiv:2605.30451` | Gated verification protocol |
| **1-GPU 24GB Fine-Tuning** | **QLoRA** / **DoRA** / **DeLoRA** | `arXiv:2305.14314` / `2402.09353` / `2503.18225` | `https://github.com/NVlabs/DoRA` |
| **Full-Param 24GB Train** | **GaLore** (`method:galore`) | `arXiv:2403.03507` | `https://github.com/jiaweizzhao/GaLore` |
| **Student Distillation** | **On-Policy Distillation** (GKD) | `arXiv:2306.13649` / Thinking Machines | `https://github.com/huggingface/trl` |
| **Extreme 1-Bit LLM** | **BitNet b1.58** | `arXiv:2504.12285` (arch `2402.17764`) | `https://github.com/microsoft/BitNet` |
| **Spiking Neural Net** | **SiLIF / C-SiLIF** (`method:silif`) | `arXiv:2506.06374` | `https://github.com/Maxtimer97/SSM-inspired-LIF` |
| **Circuits & SAEs** | **SASA** (`method:sasa`) | `arXiv:2606.06333` | `https://github.com/arshandalili/sasa` |
| **Neural Video Codec** | **DCVC-RT** (`method:dcvcrt`) | `arXiv:2502.20762` | `https://github.com/microsoft/DCVC` |
| **Continuous Control RL** | **TD-MPC2** / **Dream-MPC** | `arXiv:2310.16828` / `2605.04568` | `https://github.com/nicklashansen/tdmpc2` |

---

## 4. Fast Navigation CLI

```bash
# 1. Look up SOTA method, claims, paper, and recipe for any task
python -m library sota "pretrain dense 7B"

# 2. Search graph nodes
python -m library query "muon scalable" --type method

# 3. View node metadata and full prose
python -m library show "method:dapo"

# 4. Inspect incoming and outgoing graph edges
python -m library walk "method:muon-scalable"

# 5. Find shortest traversal path between concepts
python -m library path --from "task:pretrain-dense-7b" --to "recipe:muon-pretraining"

# 6. Validate graph schema and referential integrity
python -m library validate
```

For complete operating instructions for AI agents, see [AGENTS.md](AGENTS.md).
For schema rules and supersession protocol, see [docs/ontology.md](docs/ontology.md).
For adding new research in 5 minutes, see [docs/ingestion-guide.md](docs/ingestion-guide.md).
