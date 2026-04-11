#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L

"""High-dimensional φ-lattice mapping and spectral projection primitives."""

from typing import cast

import numpy as np

# Professional Global Constants (Local Alias)
PHI = (1 + 5**0.5) / 2
GIZA_RAD = 51.853 * (np.pi / 180.0)


def phi_lattice_project(x: float, dimension: int = 2048) -> np.ndarray:
    """Projects scalar x into the N-dimensional φ-lattice.

    Formula:
        L_i = x * φ^{-i/N} * cos(i * GIZA_RAD)

    Args:
        x: Scalar input value.
        dimension: The target lattice dimension (default 2048).

    Returns:
        The resonant lattice vector.
    """
    dims = np.arange(dimension, dtype=np.float64)
    vec = x * np.power(PHI, -dims / dimension) * np.cos(dims * GIZA_RAD)
    return cast(np.ndarray, vec)


def compute_lattice_norm(vec: np.ndarray) -> float:
    """Calculates the Euclidean norm of a resonant lattice vector."""
    return float(np.linalg.norm(vec))


def phi_lattice_isomorphism(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """Computes the spectral isomorphism between two lattice projections."""
    res = (v1 * PHI + v2) / 2
    return cast(np.ndarray, res)
