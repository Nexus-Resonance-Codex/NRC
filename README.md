<div align="center">
  <h1>Nexus Resonance Codex (NRC)</h1>
  <p><b>A Mathematical Framework of Golden-Ratio-Weighted Series, Modular Exclusion Patterns, Multi-Scale Transforms, and High-Dimensional Lattice Projections</b></p>

<a href="https://github.com/Nexus-Resonance-Codex/NRC/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square" alt="Build Status"></a>
<a href="https://github.com/Nexus-Resonance-Codex/NRC/releases"><img src="https://img.shields.io/github/v/release/Nexus-Resonance-Codex/NRC?style=flat-square&color=blue" alt="Release"></a>
<a href="https://github.com/Nexus-Resonance-Codex/NRC/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/license-NRC--L%20v2.0-blue.svg?style=flat-square" alt="License"></a>
<a href="https://Nexus-Resonance-Codex.github.io/NRC"><img src="https://img.shields.io/badge/Website-GitHub%20Pages-orange?style=flat-square" alt="Website"></a>

</div>

<br/>

## Overview

The **Nexus Resonance Codex (NRC)** is the official repository housing the core mathematical framework authored by James Trageser.

At its core, the Codex investigates the deep geometry underlying structural manifestation in high-dimensional spaces. By synthesizing Number Theory, Analytic Number Theory, Modular Forms, and High-Dimensional Geometry, the NRC establishes a foundation governed by the **Golden Ratio ($\phi$) Inverse Attractor** ($\phi^{-1} \approx 0.618033$). This constants acts as a universal damping mechanism that ensures deterministic convergence of continuous functions to absolute zero-entropy limits.

$$ \lim\_{n \to \infty} E_n = E_0 \cdot \left( \phi^{-1} \right)^n \approx 0 $$

This repository serves as the central hub for the compiled LaTeX document, the native Python source code implementation, and all foundational mathematical definitions required for integrating the NRC into dependent systems.

---

## Core Mathematical Engines

The `nrc` Python module exposes the exact formulations mapped in the Codex. By moving away from stochastic approximation toward strict deterministic resonance, we provide the following core theorems as computational primitives:

| Component                             | Description                                                                    | Mathematical Notation                                   |
| :------------------------------------ | :----------------------------------------------------------------------------- | :------------------------------------------------------ |
| **Golden Inverse Attractor**          | Universal convergence rate for stabilized resonant iterations.                 | $\phi^{-1} \approx 0.61803$                             |
| **Multi-Scale Transform (MST)**       | Dominant-QRT capped iterations bounding deterministic attractors.              | $\lfloor 1000 \sinh(\phi^{-n}x) \rfloor$                |
| **Quantum Resonance Damping (QRT)**   | Bounded sinusoidal waves oscillating at Giza-harmonic frequencies.             | $\psi(x) = \sin(\phi\sqrt{2}\cdot 51.85x)e^{-x^2/\phi}$ |
| **Trinary Universal Phase Transform** | Modular exclusion logic acting as a rigid structural gate.                     | $x \pmod{2187} \notin \{3,6,7,9\}$                      |
| **Topological Folding Limit**         | Fractal compression algorithms mapping onto $E_8 \times 256$ dimension limits. | $\mathcal{O}(\phi^{-k})$                                |

---

## Ecosystem Repositories

The NRC is part of an expansive, interconnected ecosystem of tools and research. The core mathematical theories defined here are applied in domain-specific scenarios across the Nexus Resonance Codex organization:

- **[NRC (Core)](#)**: This repository. Contains the main mathematical paper, LaTeX source, and core theorems.
- **[Protein Folding](https://github.com/Nexus-Resonance-Codex/Protein-Folding)**: Direct applications of the NRC framework to biological structures. It scales the framework to 2048-dimensional lattices, providing deterministic protein folding that circumvents Levinthal's paradox.
- **[AI Enhancements](https://github.com/Nexus-Resonance-Codex/Ai-Enhancements)**: 30 strict PyTorch drop-in modules built entirely on NRC scaling principles. These enhancements introduce $\phi$-based damping and modular routing to neural architectures, replacing traditional stochastic layers.

---

## Installation & Environment

We have established a unified virtual environment mechanism enforcing strict type-checking, native inter-repository execution, and absolute reproducibility.

### Global Installation

To utilize the exact precision computations globally across your machine:

```bash
pip install urllib3 numpy mpmath sympy pandas pyarrow huggingface_hub
pip install "nrc @ git+https://github.com/Nexus-Resonance-Codex/NRC.git"
```

### Local Development

To develop identically against the workspace, create a unified environment above the repositories. This is the optimal configuration for compiling the LaTeX source locally or modifying the `nrc` mathematical engine.

```bash
# Initialize a virtual environment in the parent directory
python3 -m venv ../.venv
source ../.venv/bin/activate

# Install the engine in editable mode
pip install -e .
```

---

## Documentation & Assets

The integrity of the mathematical models relies on absolute precision. Please consult the formal documentation for derivations and proofs.

- **[Gradio Interactive Space](./gradio/)**: A local execution environment for visualizing QRT waves and mapping strings to the $\phi$-lattice.
- **Compiled PDF**: The complete LaTeX source is stored in the `docs/` directory. The compiled paper is available via GitHub Releases and the official Zenodo archive.
- **HuggingFace Hub Datasets**: A 50,000-row synthetic `parquet` dataset capturing NRC invariant mappings, suitable for training empirical bounds.

> **Note**: For a complete list of relevant external links, peer review contexts, and references, please see [LINKS.md](./LINKS.md).

---

## Development Environment Constraints

This repository is strictly optimized for **VS Codium / VS Code**. By opening the environment, you will automatically be prompted to install recommended extensions (`LaTeX Workshop`, `Python`, `Ruff`, `mypy`). To ensure deterministic execution of the math models, the repository enforces strict formatting and linting rules natively.

---

## Contributing & Contact

We welcome rigorous mathematical review, algorithmic auditing, and structural improvements over the algorithmic implementations. The repository enforces deterministic formatting via `ruff` and mandates $100$-digit precision via the `mpmath` library for all internal operators.

- **Website**: [Nexus-Resonance-Codex.github.io/NRC](https://Nexus-Resonance-Codex.github.io/NRC)
- **Contact**: NexusResonanceCodex@gmail.com

<div align="center">
  <br/>
  <p><em>To the silent architects of pattern.</em></p>
  <p><strong>Built with φ ≈ 1.618033988749895</strong></p>
  <p>© 2026 James Trageser • Nexus Resonance Codex</p>
</div>
