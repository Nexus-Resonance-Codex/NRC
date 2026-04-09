#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L

"""Modular Synchronisation Theory (MST) — Foundational Mathematics."""

import math
from typing import Union, cast, overload

import numpy as np

# MST Constants
MST_MODULUS: int = 24389
MST_LAMBDA: float = 0.381966  # 1/φ^2


@overload
def mst_step(x: float) -> float: ...


@overload
def mst_step(x: np.ndarray) -> np.ndarray: ...


def mst_step(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Calculates a single resonant step of the MST map.

    Formula:
        x_{n+1} = (floor(1000 * sinh(x)) + log(x^2 + 1) + φ^x) % MST_MOD

    Args:
        x: Scalar or vector input coordinate.

    Returns:
        The synchronised MST coordinate.
    """
    phi = (1 + 5**0.5) / 2
    if isinstance(x, np.ndarray):
        xp = np.abs(x) + 1e-9
        val = (
            np.floor(1000.0 * np.sinh(np.minimum(xp, 20.0))) + np.log(xp**2 + 1.0) + (phi**xp)
        ) % MST_MODULUS
        return cast(np.ndarray, val)

    xp = abs(x) + 1e-9
    val = (
        math.floor(1000.0 * math.sinh(min(xp, 20.0))) + math.log(xp**2 + 1.0) + (phi**xp)
    ) % MST_MODULUS
    return float(val)
