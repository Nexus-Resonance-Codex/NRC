#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L
#  "This work is part of the Nexus Resonance Codex (NRC) incorporating TTT 
#  modular exclusion, phi^inf compression, 256D->729D lattice, QRT, and MST."

"""NRC Primitives: TUPT, QRT, and MST.

This module provides the core mathematical primitives for the Nexus Resonance Codex,
including Trageser Universal Protein Tensor mixing, Quantum Residue Turbulence damping,
and Multi-Scale Tensor recurrence.
"""

import math
from typing import Final, Union

import numpy as np
from numpy.typing import NDArray

# --- Fundamental Stability Constants ---
PHI: Final[float] = (1 + 5**0.5) / 2
PHI_FLOAT: Final[float] = PHI
PHI_INT: Final[int] = 1618

# TTT Stabilization Cycle: digital root {3, 6, 9, 7} resonance.
TTT_CYCLE: Final[list[int]] = [3, 6, 9, 7]

# Numerical Moduli
MST_MOD: Final[int] = 24389  # (29^3)
TUPT_MOD: Final[int] = 12289 # Prime field
TUPT_PATTERN: Final[frozenset[int]] = frozenset({0, 3, 6, 9})


class TUPTMixer:
    """Stateful modular mixer for Nexus Resonance projections."""

    def __init__(self, seed: int = 7) -> None:
        """Initialize the mixer with a Root-7 stabilized seed."""
        self.state: int = seed % TUPT_MOD
        self.step_count: int = 0

    def next_residue(self) -> int:
        """Generate the next TUPT resonant residue.
        
        Formula: x_{n+1} = (x_n * φ_int + cycle[step % 4]) mod TUPT_MOD
        """
        c_i = TTT_CYCLE[self.step_count % 4]
        self.state = (self.state * PHI_INT + c_i) % TUPT_MOD
        self.step_count += 1
        return self.state


def qrt_damping(x: Any) -> Any:
    """Quantum Residue Turbulence (QRT) damping function with high-fidelity poly-type support.

    ψ(x) = sin(φ√2 * 51.85 x) * e^(-x^2 / φ) + cos(π/φ * x)
    """
    freq_scale = PHI_FLOAT * math.sqrt(2) * 51.85
    
    # 1. Handle Scalar Types
    if np.isscalar(x):
        term1 = math.sin(freq_scale * x) * math.exp(-(x**2) / PHI_FLOAT)
        term2 = math.cos(math.pi / PHI_FLOAT * x)
        return float(term1 + term2)

    # 2. Handle PyTorch Tensors natively
    v_type = str(type(x))
    if "torch" in v_type:
        import torch
        term1 = torch.sin(freq_scale * x) * torch.exp(-(x**2) / PHI_FLOAT)
        term2 = torch.cos(math.pi / PHI_FLOAT * x)
        return term1 + term2

    # 3. Handle NumPy/Iterable fallback
    x_arr = np.asanyarray(x, dtype=np.float64)
    term1 = np.sin(freq_scale * x_arr) * np.exp(-(x_arr**2) / PHI_FLOAT)
    term2 = np.cos(np.pi / PHI_FLOAT * x_arr)
    return term1 + term2


def mst_recurrence(x_n: float) -> int:
    """Multi-Scale Tensor (MST) recurrence step.

    x_{n+1} = floor(1000 * sinh(x_n)) + log(x_n^2 + 1) + φ^{x_n} mod 24389
    """
    try:
        # Combined check for exponential and power overflows
        exp_term = math.sinh(float(x_n))
        pow_term = PHI**float(x_n)
        
        if math.isinf(exp_term) or math.isinf(pow_term):
            return 0
            
        res = math.floor(1000 * exp_term) + math.log(x_n**2 + 1) + pow_term
        return int(res) % MST_MOD
    except (OverflowError, ValueError):
        return 0  # Chaotic Void Reset


def phi_infinity_shard(x: NDArray[np.float64], k: int) -> NDArray[np.float64]:
    """Generate a φ^∞ shard for data vector x at index k."""
    x_arr = np.asanyarray(x, dtype=np.float64)
    rolled = np.roll(x_arr, k)
    return x_arr * (PHI**k) + rolled * (PHI**-k)


def apply_exclusion_gate(values: Any) -> Any:
    """Apply the TUPT Exclusion gate with high-fidelity poly-type support.
    
    Supports: float, int, list, numpy.ndarray, torch.Tensor.
    """
    # 1. Handle Scalar Types
    if np.isscalar(values):
        mod_val = int(values) % 9
        return 0.0 if mod_val in TUPT_PATTERN else float(values)

    # 2. Handle PyTorch Tensors natively (to prevent type-fracturing)
    # We use high-precision string reflection to ensure detection even in
    # complex shadowed environments.
    v_type_str = str(type(values))
    if "torch" in v_type_str and ("Tensor" in v_type_str or "Parameter" in v_type_str):
        import torch
        # Modulo arithmetic on integers
        v_int = values.to(torch.int32) if values.is_floating_point() else values
        mod_vals = torch.remainder(v_int, 9)
        
        # Build the exclusion mask ([0, 3, 6, 9] mapped to True)
        # Note: 9 mod 9 is 0, so we check {0, 3, 6}
        mask = (mod_vals == 0) | (mod_vals == 3) | (mod_vals == 6)
        
        # We use .masked_fill (non-inplace) to maintain graph stability
        return values.masked_fill(mask, 0.0)

    # 3. Handle NumPy/Iterable fallback
    v_arr = np.asanyarray(values, dtype=np.float64)
    mod_vals = np.mod(v_arr.astype(int), 9)
    mask = np.isin(mod_vals, list(TUPT_PATTERN))
    
    result = np.copy(v_arr)
    result[mask] = 0.0
    return result


def verify_root_7_stability(value: int) -> bool:
    """Verify if a result resides in the stabilized Root-7 anchor space."""
    d_root = value % 9
    if d_root == 0:
        d_root = 9
    return d_root == 7
