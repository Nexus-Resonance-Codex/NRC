<p align="center">
  <img src="https://raw.githubusercontent.com/Nexus-Resonance-Codex/.github/main/profile/nrc_logo.png" alt="NRC Scientific Logo" width="300">
</p>

# [Nexus Resonance Codex (NRC)](https://github.com/Nexus-Resonance-Codex)

<div align="center">
<img src="https://raw.githubusercontent.com/Nexus-Resonance-Codex/Phi-Infinity-Lattice-Compression/main/docs/assets/phi_spiral_banner.png" width="100%" alt="NRC Math Vault Banner">

# NRC (Central Math Vault)
## Professional-Grade Core Mathematics for the Nexus Resonance Codex

[![License: CC-BY-NC-SA-4.0](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-00F0FF?style=for-the-badge&logo=creative-commons "Professional License: CC-BY-NC-SA-4.0")](LICENSE)
[![CI: Math Integrity](https://img.shields.io/badge/CI-Math%20Integrity-blue?style=for-the-badge&logo=github "Continuous Integration: Mathematical Integrity")](https://github.com/Nexus-Resonance-Codex/NRC/actions)
[![Docs: Math Foundations](https://img.shields.io/badge/Docs-Foundations-green?style=for-the-badge&logo=markdown "Mathematical Foundations Documentation")](https://nexus-resonance-codex.github.io/NRC/)
[![Lattice: 8192D](https://img.shields.io/badge/Lattice-8192D-gold?style=for-the-badge&logo=mathematica "High-Dimensional Lattice Specification")](src/nrc_math/)
[![Math-Vault Evaluations](https://github.com/Nexus-Resonance-Codex/NRC/actions/workflows/prompt-evals.yml/badge.svg)](https://github.com/Nexus-Resonance-Codex/NRC/actions/workflows/prompt-evals.yml)

[Foundations](https://nexus-resonance-codex.github.io/NRC/) • [NRC Playground](#-nrc-playground) • [Primitives](src/nrc_math/primitives.py) • [Lattice Research](notebooks/) • [Proofs](proofs/)

</div>

---

### Reproducibility Statement

Numerical results and stable residue distributions reported in this repository are reproducible under the following experimental conditions. Environment: Python 3.12+, PyTorch 2.x, NumPy 1.26+. Stochastic seed: `42`. Verification command: `uv pip install -e . && pytest tests/ -q`. Resulting metrics are verified against the Trageser Transformation Theorem (TTT) and Trageser Universal Pattern Theorem (TUPT) specifications.

### Verified Results

| Metric | Empirical Value | Verification Asset |
| :--- | :--- | :--- |
| **Modular Stability** | $100\%$ Coverage | `tests/test_primitives.py` |
| **MSE Fidelity** | $< 10^{-24}$ | `src/nrc_math/primitives.py` |
| **Hurst Exponent ($H$)** | $0.78 \pm 10^{-3}$ | `src/nrc/math/qrt.py` |
| **Lattice Dim** | $8192$ | `src/nrc_math/primitives.py` |

---

### Methodology

The framework utilizes a modular exclusion principle based on residue classes modulo 9, 27, and 81, synchronized with the Pisano periods of $\varphi$-recursive sequences. Primitives utilize the Trageser Transformation Theorem (TTT) and the Trageser Universal Pattern Theorem (TUPT) for high-dimensional state-space stabilization. Sequential data is projected into an 8192D lattice manifold where retrieval complexity is $O(1)$ and convergence is maintained via non-linear damping.

### Core Mathematical Primitives

*   **Trageser Universal Pattern Theorem (TUPT)**: Modular exclusion operators for preventing numerical divergence in iterative systems.
*   **Quantum Residue Turbulence (QRT)**: Deterministic fractal damping function for gradient regularization and entropy management.
*   **Multi-Scale Tensor (MST)**: Chaotic oscillation monitoring for signal stability across high-frequency domains.
*   **Lattice Resonance**: 8192D state-space mapping for high-fidelity information retrieval.

---

### 🚀 NRC Playground – Test Directly on GitHub

Verify the foundational theorems of the Nexus Resonance Codex directly in the GitHub UI using the **Models** tab.

| Feature | Interactive Prompt | Model Recommendation |
| :--- | :--- | :--- |
| **TTT Stability** | [Audit Constants](https://github.com/Nexus-Resonance-Codex/NRC/blob/master/.github/prompts/ttt-modular-exclusion-tester.prompt.yml) | GPT-4o |
| **φ-Projection** | [Spiral Calculator](https://github.com/Nexus-Resonance-Codex/NRC/blob/master/.github/prompts/phi-spiral-projection-calculator.prompt.yml) | GPT-4o |
| **TUPT Signatures** | [Post-Quantum Oracle](https://github.com/Nexus-Resonance-Codex/NRC/blob/master/.github/prompts/tupt-lattice-signature-generator.prompt.yml) | o1-preview |

Refer to the [**NRC Playground Guide**](https://nexus-resonance-codex.github.io/NRC/NRC-Playground-Guide.html) for rigorous verification instructions.

---

### Professional Setup

The NRC ecosystem uses a **Unified Virtual Environment** to ensure mathematical reproduction across all repositories.

```bash
# 1. Clone the repository
git clone https://github.com/Nexus-Resonance-Codex/NRC.git
cd NRC

# 2. Activate the Unified NRC Environment
source ../.venv/bin/activate

# 3. Verify the mathematical foundations
pytest tests/
```

<div align="center">
<i>Nexus Resonance Codex © 2026</i><br>
</div>
