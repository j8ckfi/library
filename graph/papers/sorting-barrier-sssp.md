---
id: paper:sorting-barrier-sssp
type: paper
title: "Breaking the Sorting Barrier for Directed Single-Source Shortest Paths"
authors:
  - "Ran Duan"
  - "Jiayi Mao"
  - "Xiao Mao"
  - "Xinkai Shu"
  - "Longhui Yin"
year: 2025
month: 4
arxiv_id: "2504.17033"
url: "https://arxiv.org/abs/2504.17033"
methods:
  - method:bmssp
cites: []
tags:
  - algorithms
  - graph-algorithms
  - sssp
  - directed-graphs
  - comparison-addition
  - bmssp
---

# Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

## Abstract Summary
The paper gives a deterministic \(O(m\log^{2/3}n)\)-time algorithm for single-source shortest paths on directed graphs with real non-negative edge weights in the comparison-addition model. This is the first result to break Dijkstra's \(O(m+n\log n)\) bound on sparse graphs, showing Dijkstra is not optimal for SSSP when only distances (not the vertex order) are required. DMSY23 previously broke the bound with a randomized algorithm on undirected graphs; this result is also the first *deterministic* break of \(O(m+n\log n)\) even on undirected graphs.

arXiv comments field: "17 pages". No venue is stated on the abs page.

## Key Contributions
1. **Directed sorting-barrier break**: deterministic \(O(m\log^{2/3}n)\) SSSP on directed real non-negative instances (Theorem 1.1).
2. **BMSSP + FindPivots**: divide-and-conquer bounded multi-source shortest path; \(k\) Bellman-Ford-like relaxations followed by pivot trees of size \(\geq k\); parameters \(k=\lfloor\log^{1/3}n\rfloor\), \(t=\lfloor\log^{2/3}n\rfloor\).
3. **Scope of the lower bound**: Dijkstra remains optimal if the algorithm must output the order of vertices by distances (Haeupler–Hladík–Rozhoň–Tarjan–Tětek, FOCS 2024). This paper computes distances, not that sort.

## Empirical Highlights
- The result is a worst-case comparison-addition *time bound*, not a wall-clock benchmark table.
- Unofficial third-party implementations report that Dijkstra remains faster on typical \(n\) because of large constants, recursion, and auxiliary data structures.

## Open Source Repository
- Official author code: none found.
- Unofficial third-party implementations (not author-maintained): `https://github.com/hparreao/BMSSP-Python`, `https://github.com/NicholasCartaxo/BMSSP-SSSP`.
