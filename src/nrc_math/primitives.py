"""NRC Primitives: TUPT, QRT, and MST.

This module provides the core mathematical primitives for the Nexus Resonance Codex,
including Trageser Universal Protein Tensor mixing, Quantum Residue Turbulence damping,
and Multi-Scale Tensor recurrence.
"""

import math
from typing import Final

import numpy as np
from numpy.typing import NDArray

# Core Constants
PHI: Final[float] = (1 + 5**0.5) / 2
PHI_FLOAT: Final[float] = PHI
PHI_INT: Final[int] = 1618
TTT_CYCLE: Final[list[int]] = [3, 6, 9, 7]
MST_MOD: Final[int] = 24389
TUPT_MOD: Final[int] = 12289
TUPT_PATTERN: Final[frozenset[int]] = frozenset({0, 3, 6, 9})


def tupt_mix(x: int, step: int) -> int:
    """TUPT mixing round: x' = (x * φ_int + c_i) mod 12289.

    Args:
        x: Input integer in Z_12289.
        step: Current cycle step index.

    Returns:
        Mixed integer.
    """
    c_i = TTT_CYCLE[step % len(TTT_CYCLE)]
    return (x * PHI_INT + c_i) % TUPT_MOD


def qrt_damping(x: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Quantum Residue Turbulence (QRT) damping function.

    ψ(x) = sin(φ√2 * 51.85 x) * e^(-x^2 / φ) + cos(π/φ * x)

    Args:
        x: Input scalar or array.

    Returns:
        Damped output.
    """
    term1 = np.sin(PHI * np.sqrt(2) * 51.85 * x) * np.exp(-(x**2) / PHI)
    term2 = np.cos(np.pi / PHI * x)
    return float(term1 + term2) if np.isscalar(x) else term1 + term2


def mst_recurrence(x_n: float) -> int:
    """Multi-Scale Tensor (MST) recurrence step.

    x_{n+1} = floor(1000 * sinh(x_n)) + log(x_n^2 + 1) + φ^{x_n} mod 24389

    Args:
        x_n: Current state.

    Returns:
        Next state mod 24389.
    """
    # Use float for intermediate calculation to avoid overflow in sinh if x_n is large
    # In practice, x_n is often bounded or modular
    try:
        val = math.sinh(x_n)
    except OverflowError:
        val = float("inf")

    if val == float("inf"):
        return 0  # Chaotic Void Threshold (Chaos Reset)

    res = math.floor(1000 * val) + math.log(x_n**2 + 1) + PHI**x_n
    return int(res) % MST_MOD


def phi_infinity_shard(x: NDArray[np.float64], k: int) -> NDArray[np.float64]:
    """Generate a φ^∞ shard for data vector x at index k.

    s_k = x * φ^k + roll(x, k) * φ^-k

    Args:
        x: Data vector.
        k: Shard index.

    Returns:
        Shard vector.
    """
    rolled = np.roll(x, k)
    shard = x * (PHI**k) + rolled * (PHI**-k)
    return shard


def apply_exclusion_gate(values: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Apply the TUPT Exclusion gate.

    Values yielding chaotic mod-9 sequence {0, 3, 6, 9} are zeroed out.

    Args:
        values: Input scalar or array.

    Returns:
        Stabilized output.
    """
    if np.isscalar(values):
        mod_val = int(values) % 9
        return 0.0 if mod_val in TUPT_PATTERN else values

    # Vectorized
    mod_vals = np.mod(values.astype(int), 9)
    mask = np.isin(mod_vals, list(TUPT_PATTERN))
    result = np.copy(values)
    result[mask] = 0.0
    return result
