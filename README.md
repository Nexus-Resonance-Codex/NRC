# Nexus Resonance Codex: Central Math Vault (NRC)

<p align="center">
  <img src="https://raw.githubusercontent.com/Nexus-Resonance-Codex/.github/main/profile/nrc_logo.png" alt="NRC Central Math Vault" width="380">
</p>

<p align="center">
  <strong>The Algorithmic and Mathematical Foundations of High-Dimensional Lattice Resonance, Modular Arithmetic, and Deterministic Information Stability</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue.svg?style=flat-square" alt="AGPL-3.0 License"></a>
  <a href="LICENSE-DATA"><img src="https://img.shields.io/badge/Data%20License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square" alt="CC BY-NC-SA 4.0"></a>
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python Versions">
  <img src="https://img.shields.io/badge/PyTorch-Supported-EE4C2C.svg?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch Supported">
  <img src="https://img.shields.io/badge/Stability-TTT--7%20Verified-008080.svg?style=flat-square" alt="TTT-7 Verified">
</p>

---

## Executive Overview

The **Nexus Resonance Codex Central Math Vault (`NRC`)** is the foundational mathematical library and algorithmic engine of the Nexus Resonance Codex ecosystem. It provides mathematically verified, type-hardened implementations of core NRC primitives—including **TUPT** (Trageser Universal Pattern Transform), **QRT** (Quantum Resonance Transform), **MST** (Multi-Scale Tensor Recurrence), and **$\phi^\infty$ Shard Folding**—anchored to the **digital root 7 locus** for guaranteed structural and numerical stability.

This repository serves as the single source of mathematical truth across all downstream applications, from cognitive AI attention mechanisms (`Ai-Enhancements`) and structural biophysics (`Protein-Folding`) to post-quantum lattice cryptography (`Phi-Infinity-Lattice-Compression`).

---

## Theoretical Foundations

The Nexus Resonance Codex is founded on the synthesis of ancient geometric invariants and modern high-dimensional computational theory.

```
+-------------------------------------------------------------------------------+
|                       CENTRAL MATH VAULT (NRC) TOPOLOGY                       |
+-------------------------------------------------------------------------------+
|                                                                               |
|   Discrete Modular Domain                         Continuous Manifold Domain  |
|   +------------------------------------+          +-----------------------+   |
|   | TUPT Modular Gate                  |          | QRT Fractal Damping   |   |
|   | Xi(x) = x if x % 9 not in {0,3,6}  | <------> | psi(x) damping curve  |   |
|   +------------------------------------+          +-----------------------+   |
|                     |                                         |               |
|                     v                                         v               |
|   +------------------------------------+          +-----------------------+   |
|   | TTT-7 Stability Locus              |          | MST Hyperbolic Map    |   |
|   | dr(n) in {1, 2, 4, 5, 7, 8}        | <------> | x_{n+1} recurrence    |   |
|   +------------------------------------+          +-----------------------+   |
|                     |                                         |               |
|                     +--------------------+--------------------+               |
|                                          |                                    |
|                                          v                                    |
|                       +-------------------------------------+                 |
|                       |   phi^inf Spectral Shard Folding    |                 |
|                       |   s_k = x * phi^k + roll * phi^-k   |                 |
|                       +-------------------------------------+                 |
|                                                                               |
+-------------------------------------------------------------------------------+
```

### 1. Trageser Universal Pattern Transform (TUPT) & Modular Exclusion
In discrete high-dimensional state spaces, the residue set $\{0, 3, 6\}$ under modulo 9 exhibits chaotic numerical divergence. The TUPT exclusion gate eliminates chaotic attractors while preserving valid state density:

$$\Xi(x) = \begin{cases} 0 & \text{if } x \pmod 9 \in \{0, 3, 6\} \\ x & \text{otherwise} \end{cases}$$

### 2. Trageser Tensor Theorem (TTT-7) Stability Gate
Digital root evaluation ensures that intermediate tensor values, loss terms, and parameters reside strictly within the resonant stability manifold:

$$\text{dr}(n) = (n - 1) \pmod 9 + 1$$

$$\text{Stability Condition: } \text{dr}(n) \in \{1, 2, 4, 5, 7, 8\}$$

### 3. Quantum Resonance Transform (QRT) Fractal Damping
QRT replaces standard stochastic Gaussian noise with deterministic fractal regularization, minimizing entropy without introducing uncontrolled variance:

$$\psi(x) = \sin(\phi\sqrt{2} \cdot \theta_{QRT} \cdot x) \cdot e^{-x^2 / \phi} + \cos\left(\frac{\pi}{\phi} \cdot x\right)$$

where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618033988749895$ and $\theta_{QRT} \approx 51.853^\circ$.

### 4. Multi-Scale Tensor (MST) Recurrence
MST recurrence models and controls dynamic trajectories in non-linear systems (such as protein backbone conformation and deep recurrent activations):

$$x_{n+1} = \lfloor 1000 \cdot \sinh(x_n) \rfloor + \ln(x_n^2 + 1) + \phi^{x_n} \pmod{24389}$$

where the modulus $24389 = 29^3$ corresponds to the discrete 3-state lattice boundary.

### 5. $\phi^\infty$ Shard Folding
Continuous high-dimensional vectors are projected onto self-similar spiral manifolds:

$$s_k = x \cdot \phi^k + \text{roll}(x, k) \cdot \phi^{-k}$$

As $k \to \infty$, information density converges to the golden attractor limit, supporting $O(1)$ coordinate retrieval across $O(\phi^n)$ sequence context.

---

## Package Architecture

```
NRC/
├── src/
│   ├── nrc_math/               # Core mathematical primitives library
│   │   ├── __init__.py         # Exported primitives and constants
│   │   ├── primitives.py       # TUPT, QRT, MST, Binet, and TTT-7 routines
│   │   └── py.typed            # PEP 561 static type marker
│   └── nrc/                    # High-dimensional lattice operations
│       └── core.py             # Manifold projection and tensor transforms
├── proofs/                     # Formal mathematical demonstration scripts
│   ├── proof_01_entropy_collapse.py
│   ├── proof_02_modular_exclusion.py
│   └── proof_03_qrt_resonance.py
├── docs/                       # Institutional documentation & MkDocs sources
│   ├── nrc-math.md             # Formal proofs and derivation notes
│   └── index.md                # Documentation index
├── tests/                      # Automated test suite
│   └── test_primitives.py      # Primitive verification and stability checks
├── pyproject.toml              # Build configuration and dependencies
└── uv.lock                     # Deterministic dependency lockfile
```

---

## Installation & Quickstart

### Environment Setup

This project uses modern Python packaging via [uv](https://github.com/astral-sh/uv) (or standard `pip` / `venv`):

```bash
# Clone the repository
git clone https://github.com/Nexus-Resonance-Codex/NRC.git
cd NRC

# Create and activate virtual environment with uv
uv venv
source .venv/bin/activate

# Install package in editable mode with development dependencies
uv pip install -e ".[dev]"
```

Alternatively, with standard `pip`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

---

## Python Usage Examples

### 1. Continuous and Discrete Fibonacci Projections

```python
from nrc_math.primitives import binet_formula

# Discrete calculation
f_10 = binet_formula(10)
print(f"10th Fibonacci Number: {f_10}")  # Output: 55

# Continuous tensor projection
import numpy as np
coords = np.linspace(0.0, 5.0, 6)
projected = binet_formula(coords)
print(f"Continuous Projection: {projected}")
```

### 2. Modular Exclusion Gate ($\Xi$)

```python
import numpy as np
from nrc_math.primitives import apply_exclusion_gate

# Create sample state array
states = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# Apply TUPT exclusion gate (zeroes out residues 0, 3, 6 modulo 9)
filtered = apply_exclusion_gate(states, modulus=9)
print(f"Filtered States: {filtered}")
# Output: [ 0.  1.  2.  0.  4.  5.  0.  7.  8.  0. 10. 11.]
```

### 3. Verifying Digital Root 7 Stability

```python
from nrc_math.primitives import verify_root_7_stability

test_values = [16, 25, 34, 43, 52, 70]
for val in test_values:
    is_stable = verify_root_7_stability(val)
    print(f"Value: {val:2d} | TTT-7 Stability: {is_stable}")
```

### 4. Stateful TUPT Residue Generation

```python
from nrc_math.primitives import TUPTMixer

mixer = TUPTMixer(seed=42)
sequence = [mixer.next_residue() for _ in range(5)]
print(f"Residue Sequence: {sequence}")
```

---

## Verification & Test Execution

Run the comprehensive unit test suite to verify mathematical invariants and numerical tolerances:

```bash
# Execute unit tests
pytest tests/ -v

# Run formal mathematical proof scripts
python proofs/proof_01_entropy_collapse.py
python proofs/proof_02_modular_exclusion.py
python proofs/proof_03_qrt_resonance.py
```

---

## Licensing & Commercial Governance

The Nexus Resonance Codex is dual-licensed:

- **Open Source / Academic Research:**
  - Codebase: [GNU Affero General Public License v3.0 (AGPL-3.0)](LICENSE)
  - Data & Weights: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)](LICENSE-DATA)
  - Patent Covenant: [Tesla-Style Patent Pledge](PATENT_PLEDGE.md)
  - Trademark: [Trademark & Nomenclature Policy](TRADEMARK_POLICY.md)

- **Enterprise & Commercial Deployment:**
  Commercial organizations requiring proprietary, closed-source integration without AGPL-3.0 copyleft obligations must obtain an Enterprise License. See [COMMERCIAL_USE.md](COMMERCIAL_USE.md) or direct inquiries to:

  **James Paul Trageser**  
  Founder and Chief Architect  
  Email: `NexusResonanceCodex@gmail.com`

---

## Academic Citation

```bibtex
@software{trageser2026nrc_vault,
  author       = {James Paul Trageser},
  title        = {Nexus Resonance Codex (NRC): Central Math Vault and High-Dimensional Lattice Primitives},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub Repository},
  howpublished = {\url{https://github.com/Nexus-Resonance-Codex/NRC}}
}
```

---

*Copyright (c) 2026 Nexus Resonance Codex (NRC). All rights reserved.*
