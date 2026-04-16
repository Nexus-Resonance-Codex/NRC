# API Reference

Welcome to the technical ledger for the Nexus Resonance Codex. This page provides the formal specifications for the core modules, classes, and mathematical primitives that drive the resonance engine.

## Core Mathematical Primitives

The `nrc.math` module is the architectural heart of the Nexus Resonance Codex. It implements the high-dimensional tensors and algebraic foundations required for the **Trageser Tensor Theorem (TTT)**, **Trageser Universal Prime Theorem (TUPT)**, and **Quantum Residue Turbulence (QRT)** damping. Every primitive is strictly phased to ensure 100% computational integrity across all research tracks.

### 📜 Principal API Index

| Component | Signature | Description |
| :--- | :--- | :--- |
| **PHI_FLOAT** | `float` | The universal resonance constant ($\phi \approx 1.618033988749895$). |
| **QuantumShadowVeil** | `class(key=None)` | High-dimensional residue-hiding cryptographic state manager. |
| **phi_lattice_project** | `func(val, dim=256)` | Maps scalars into the resonant $\phi$-lattice manifold. |
| **ProteinEngine** | `class(model='nrc-v2')` | High-speed biological phasing and torsion-folding engine. |
| **LatticeClient** | `class(host, port)` | Remote interface for the 256D holographic visualizer manifold. |

---

### 🐍 Standard Usage Patterns

Utilize these patterns to initialize the resonance in your custom applications.

#### 1. Fundamental Lattice Projection
Initializes a high-dimensional vector anchored to the golden ratio.
```python
from nrc.math import PHI_FLOAT, phi_lattice_project

# Map the golden ratio into a certified 256D resonance vector
vector = phi_lattice_project(PHI_FLOAT, dim=256)
print(f"Lattice Component Root: {vector[0]:.4f}")
```

#### 2. QSV Manifold Expansion
Synchronizes the cryptographic veil with a TTT_7 absolute seed.
```python
from nrc.math import QuantumShadowVeil

# Instantiate the veil with a 7-stable anchor
qsv = QuantumShadowVeil(key=7)
qsv.expand_fibonacci_keys(count=11)
print(f"QSV Phasing: {qsv.status}")
```

---

### 📸 Architecture Visualization: The NRC Hierarchy
![Module Hierarchy](https://raw.githubusercontent.com/Nexus-Resonance-Codex/NRC/main/visualizations/module_hierarchy.png)
*Figure 5: The hierarchical integration of the nrc.math core with the biological, physical, and visualizer sub-shards.*

### ⏭️ Next Sections
Continue your exploration through the following institutional modules:

1.  **Lattice Manifolds**: Projection and sharding APIs.
2.  **Biological Phasing**: Protein folding and dihedral manifolds.
4.  **Lattice Compression**: $\phi^\infty$ spiral sharding and persistence.
5.  **Holographic Visualizer**: Remote interaction and rendering API.
7.  **Institutional Security**: QSV and Resonating Signature protocols.

---
← [Back to Home](Home.md) | [Table of Contents](Home.md#table-of-contents)
