# j8ckfi/library

> Sprawling, agent-navigable knowledge graph of cutting-edge machine learning research, SOTA methods, primary literature, and executable training recipes (As-of: 2026-08-28).

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

## 2. Agent Routing Cheat-Sheet (2026-08-28 SOTA Index)

```
task: pretrain dense 7B optimizer  -> muon2 (2604.09967) + kl-soap (2607.20548) if memory allows
task: open data recipe             -> olmo-3 / dolma-3 (2512.13961)
task: pretrain MoE architecture    -> deepseek-v4 (2606.19348) + kimi-k3 (2607.24653)
task: train MoE on NVL72        -> mixture-of-kittens (MoK megakernel, 1070 tok/s/GPU on GB300 NVL72)
task: instruct SFT                 -> olmo-3 dolci (2512.13961); industrial alt nemotron-cascade-2 (2603.19220)
task: math/code RL, dense          -> cispo (minimax-m1 2506.13585 + scalerl 2510.13786)
task: math/code RL, MoE/VL         -> sapo (2511.20347); gspo only if Qwen3.5-Omni Talker
task: agentic async RL             -> sao (2607.07508)
task: all-zero verifier groups     -> verigate (2605.30451)
task: LoRA quality 24GB            -> vanilla LoRA + rsLoRA + LR sweep (2602.04998, 2601.22708) NOT DoRA
task: LoRA must 4-bit              -> aqlora-q (2608.23816) or autoqra (2602.22268)
task: full-param mem pretrain      -> scale (2506.16659) not galore
task: native 1.58-bit pretrain     -> sparse-bitnet (2603.05168); keep 2B4T as dense cite
task: ternary an existing SOTA LLM -> scaleq-1.58 (2608.01078)
task: FP4 hardware train           -> quartet-ii nvfp4 (2601.22813) / mxfp4 (2605.09825) / kimi-k3 QAT
task: distill student              -> opd 2604.13016 (single-teacher) / open-mopd 2608.19098 (multi-teacher)
task: SNN sequence/SSM             -> longspike (2606.12895); train with a2sg (2606.11236); silif stays as speech-neuron cite
task: continuous control           -> efficienttdmpc (2605.16692) family; dream-mpc (2605.04568) gradient planner
task: neural video GPU             -> dcvc-uf (2606.04410)
task: neural video deploy          -> mlvc (2606.28027)
task: distill a reasoner (OPD+RLVR)-> opdvr (2608.24696)
task: token-level advantages (1/p) -> bpco (2608.23566)
task: posttrain diffusion          -> diffusion-opsd (2608.24646); no task-specific teacher (flow) -> self-opd (2608.26872)
task: video MLLM RL                -> orarl (2608.20492)
task: label-free TTT / no-GT test-time reasoner -> ttpo (2608.27448)
task: unlabeled math reasoner posttrain (no GT) -> u-opsd (2608.06296)
task: SAE dictionary               -> sasa (2606.06333) KEEP
task: SAE circuits                 -> circuitsteer (2608.05732)
task: SAE effect geometry          -> fega (2607.24645)
```

---

## 3. SOTA Method Map (What You Actually Pick Today)

| Task / Domain | Default SOTA Method | Key Paper / Reference | Code / Repo |
| :--- | :--- | :--- | :--- |
| **Dense 7B Pretrain Optimizer** | **Muon2** (`method:muon2`) + **KL-SOAP** | `arXiv:2604.09967` / `2607.20548` | `none found` / `https://github.com/NVIDIA-NeMo/Emerging-Optimizers` |
| **Open Data Recipe** | **OLMo-3 / Dolma-3** (`method:olmo-3`) | AI2 `arXiv:2512.13961` | `https://github.com/allenai/OLMo-core` / `https://github.com/allenai/dolma3` |
| **Pretrain MoE Architecture** | **DeepSeek-V4** + **Kimi-K3** | `arXiv:2606.19348` / `2607.24653` | `none found` / `https://github.com/MoonshotAI/Kimi-K3` |
| **Train MoE on NVL72** | **Mixture-of-Kittens** (`method:mixture-of-kittens`) | Cursor Research Aug 2026 | `https://github.com/cursor/mixture-of-kittens` |
| **Instruct SFT** | **OLMo-3 Dolci** / **Nemotron-Cascade 2** | `arXiv:2512.13961` / `2603.19220` | `https://github.com/allenai/OLMo-core` / `none found` |
| **Dense Math/Code RL** | **CISPO** (`method:cispo`) | `arXiv:2506.13585` / `2510.13786` | `https://github.com/MiniMax-AI/MiniMax-M1` |
| **MoE/VL Math/Code RL** | **SAPO** (`method:sapo`) | `arXiv:2511.20347` | ms-swift `loss_type=sapo` |
| **Agentic Async RL** | **SAO** (`method:sao`) | `arXiv:2607.07508` | `none found` |
| **All-Zero Verifier Groups** | **VeriGate** (`method:verigate`) | `arXiv:2605.30451` | `none found` |
| **LoRA Quality 24GB** | **Vanilla LoRA + rsLoRA + LR sweep** | `arXiv:2602.04998` / `2601.22708` | `https://github.com/yuang-lee/lr-matters-lora` |
| **LoRA Must 4-Bit** | **AQLoRA-Q** / **AutoQRA** | `arXiv:2608.23816` / `2602.22268` | `https://github.com/Romyull-Islam/AQLoRA` / `none found` |
| **Full-Param Mem Pretrain** | **SCALE** (`method:scale`) | ICML 2026 `arXiv:2506.16659` | `none found` |
| **Native 1.58-Bit Pretrain** | **Sparse-BitNet** (`method:sparse-bitnet`) | `arXiv:2603.05168` | `https://github.com/AAzdi/Sparse-BitNet` |
| **Ternary Existing SOTA LLM**| **ScaleQ-1.58** (`method:scaleq-158`) | `arXiv:2608.01078` | `https://github.com/IntelChina-AI/BitTern` (claimed) |
| **FP4 Hardware Train** | **Quartet-II NVFP4** / **MXFP4** | `arXiv:2601.22813` / `2605.09825` | `https://github.com/IST-DASLab/Quartet-II` / `none found` |
| **Distill Student** | **OPD** (`method:opd`) (single) / **Open-MOPD** (`method:open-mopd`) (multi) | `arXiv:2604.13016` / `2608.19098` | `https://github.com/thunlp/OPD` / `https://github.com/BytedTsinghua-SIA/Open-MOPD` |
| **SNN Sequence / SSM** | **LongSpike** (`method:longspike`) | `arXiv:2606.12895` / `2606.11236` | `https://github.com/xinruihe389-commits/LongSpike` / `https://github.com/KIST-NCL/A2SG.git` |
| **Continuous Control** | **EfficientTDMPC** / **Dream-MPC** | `arXiv:2605.16692` / `2605.04568` | `none found` (BMPC) / `none found` (ICML 2026) |
| **Neural Video GPU** | **DCVC-UF** (`method:dcvc-uf`) | `arXiv:2606.04410` | `https://github.com/microsoft/DCVC` |
| **Neural Video Deploy** | **MLVC** (`method:mlvc`) | `arXiv:2606.28027` | `https://github.com/microsoft/mlvc` |
| **SAE Dictionary** | **SASA** (`method:sasa`) KEEP | `arXiv:2606.06333` | `https://github.com/arshandalili/sasa` |
| **SAE Circuits** | **CircuitSteer** (`method:circuitsteer`) | `arXiv:2608.05732` | `https://github.com/mehrshad-sdtn/CircuitSteer` |
| **SAE Effect Geometry** | **FEGA** (`method:fega`) | `arXiv:2607.24645` | `https://github.com/UKPLab/FEGA` |
| **Distill Reasoner (OPD+RLVR)** | **OPDVR** (`method:opdvr`) | `arXiv:2608.24696` | `https://github.com/LeapLabTHU/OPDVR` |
| **Token-Level Critic (1/prompt)** | **BPCO** (`method:bpco`) | `arXiv:2608.23566` | `https://github.com/QPHutu/golden_critic` |
| **Posttrain Diffusion** | **DiffusionOPSD** (`method:diffusion-opsd`) / **Self-OPD** (`method:self-opd`) | `arXiv:2608.24646` / `2608.26872` | `https://github.com/worldbench/DiffusionOPSD` / `https://github.com/Shiy-Zhang/Self-OPD` |
| **Video MLLM RL** | **OraRL** (`method:orarl`) | `arXiv:2608.20492` | `https://github.com/HVision-NKU/OraRL` |
| **Label-Free Test-Time Reasoning** | **TTPO** (`method:ttpo`) | `arXiv:2608.27448` | `https://github.com/ZJU-REAL/TTPO` |
| **Unlabeled Reasoner Posttrain** | **u-OPSD** (`method:u-opsd`) | `arXiv:2608.06296` | `https://github.com/williamium3000/u-opsd` |

---

## 4. Fast Navigation CLI

```bash
# 1. Look up SOTA method, claims, paper, and recipe for any task
python -m library sota "pretrain dense 7B"

# 2. Search graph nodes
python -m library query "muon2" --type method

# 3. View node metadata and full prose
python -m library show "method:cispo"

# 4. Inspect incoming and outgoing graph edges
python -m library walk "method:muon2"

# 5. Find shortest traversal path between concepts
python -m library path --from "task:pretrain-dense-7b" --to "recipe:muon2-pretraining"

# 6. Validate graph schema and referential integrity
python -m library validate
```

For complete operating instructions for AI agents, see [AGENTS.md](AGENTS.md).
For schema rules and supersession protocol, see [docs/ontology.md](docs/ontology.md).
For adding new research in 5 minutes, see [docs/ingestion-guide.md](docs/ingestion-guide.md).
