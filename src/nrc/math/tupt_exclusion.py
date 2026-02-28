"""
TUPT (The Universal Pattern Theorem) Exclusion Principle.
========================================================
Implements the 3-6-9-7 Modular Exclusion Gate verified via the
NRC Protein Folding Lattice bounds.
"""
from typing import Union

import numpy as np

TUPT_MODULUS: int = 2187
TUPT_PATTERN = frozenset({3, 6, 7, 9})

def apply_exclusion_gate(values: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    """
    Applies the mathematical TUPT Exclusion gate.

    Any value x where (x mod 2187) is perfectly divisible by 3, 6, 7, or 9
    is forced to 0 (gated out). All other values pass unchanged.
    This mimics the biological residue stabilities noted in the NRC.

    Args:
        values: Continuous space coordinates or signals.

    Returns:
        The structurally coherent values remaining after exclusion gating.
    """
    if isinstance(values, (int, float)):
        mod_val = values % TUPT_MODULUS
        if any(mod_val % p == 0 for p in TUPT_PATTERN if p != 0):
            return 0.0 if isinstance(values, float) else 0
        return values

    # Vectorized NumPy logic
    mod_vals = np.mod(values, TUPT_MODULUS)

    mask_3 = (mod_vals % 3 == 0)
    mask_6 = (mod_vals % 6 == 0)
    mask_7 = (mod_vals % 7 == 0)
    mask_9 = (mod_vals % 9 == 0)

    exclusion_mask = mask_3 | mask_6 | mask_7 | mask_9

    result = np.copy(values)
    result[exclusion_mask] = 0.0

    return result
