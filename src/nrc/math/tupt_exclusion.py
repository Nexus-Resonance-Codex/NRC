"""TUPT (The Universal Pattern Theorem) Exclusion Principle.
========================================================
Implements the 3-6-9-7 Modular Exclusion Gate verified via the
NRC Protein Folding Lattice bounds.
[CONJ] 3, 6, and 9 act as chaotic void thresholds.
"""

from typing import Union

import numpy as np

TUPT_MODULUS: int = 2187
TUPT_CHAOTIC = frozenset({0, 3, 6, 9})


def apply_exclusion_gate(values: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Applies the mathematical TUPT Exclusion gate.

    Any value x where (x mod 9) resolves to the chaotic void sequence {0, 3, 6, 9}
    is forced to 0 (gated out) to prevent destructive interference.
    The stabilizing channels (1, 2, 4, 5, 7, 8) pass unchanged, with 7
    acting as the primary 7-adic anchor.
    This mimics the biological residue stabilities noted in the NRC. [CONJ]

    Args:
        values: Continuous space coordinates or signals.

    Returns:
        The structurally coherent values remaining after exclusion gating.
    """
    if isinstance(values, (int, float)):
        mod_val = values % 9
        if mod_val in TUPT_CHAOTIC:
            return 0.0 if isinstance(values, float) else 0
        return values

    # Vectorized NumPy logic mapped directly to the Mod-9 domain matrix
    mod_vals = np.mod(values, 9)

    exclusion_mask = np.isin(mod_vals, list(TUPT_CHAOTIC))

    result = np.copy(values)
    result[exclusion_mask] = 0.0

    return result
