from typing import Any, List, Optional, Union, cast

import numpy as np

# Type Aliases for Spectral Clarity
LatticeValue = Union[float, np.ndarray, Any]

# Professional Constants
PHI_INT: int = 1618
PHI_FLOAT: float = 1.618033988749895
PHI_INVERSE_FLOAT: float = 0.618033988749895
PHI: float = PHI_FLOAT  # Primary professional alias
SQRT_5: float = 2.23606797749979
SQRT_5_FLOAT: float = SQRT_5
MST_MOD: int = 24389
TUPT_MOD: int = 9
TTT_CYCLE: List[int] = [1, 2, 4, 5, 7, 8]
TUPT_PATTERN = {0, 3, 6, 9}


def binet_formula(n: Any) -> LatticeValue:  # noqa: ANN401
    """Calculates n-th Fibonacci value via continuous Binet projection."""
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2

    # Check if we are doing a discrete or continuous projection
    if isinstance(n, int) and n >= 0:
        return int(round((phi**n - psi**n) / 5**0.5))

    # Continuous manifold for higher dimensions (Tensors/Arrays)
    return (phi**n - (-phi) ** (-n)) / 5**0.5


def apply_exclusion_gate(values: Any, modulus: int = 9) -> Any:  # noqa: ANN401
    """Applies the Trageser Universal Pattern Theorem (TUPT) modular exclusion."""
    type_str = str(type(values))
    is_torch = "torch.Tensor" in type_str
    is_numpy = "numpy.ndarray" in type_str

    if is_torch:
        import torch

        t_values = cast(torch.Tensor, values)
        device = t_values.device
        dtype = t_values.dtype
        mask_val = torch.tensor(0.0, device=device, dtype=dtype)
        mod_val = torch.remainder(t_values, modulus)
        mask = (mod_val == 0) | (mod_val == 3) | (mod_val == 6)
        return torch.where(mask, mask_val, t_values)

    if is_numpy:
        n_values = cast(np.ndarray, values)
        mod_v = n_values % modulus
        mask_n = (mod_v == 0) | (mod_v == 3) | (mod_v == 6)
        out = np.copy(n_values)
        out[mask_n] = 0.0
        return out

    try:
        if float(values) % modulus in [0, 3, 6]:
            return type(values)(0)
    except (ValueError, TypeError):
        pass

    return values


def verify_root_7_stability(value: int) -> bool:
    """Verifies modular stability – checks if the digital root is 7."""
    if value == 0:
        return False
    dr = value % 9
    return (dr if dr != 0 else 9) == 7


def mst_recurrence(x: Any) -> LatticeValue:  # noqa: ANN401
    """Computes the professional MST recurrence value."""
    # Poly-type compatible recurrence logic
    xp = np.abs(x) + 1e-9
    val = np.floor(1000.0 * np.sinh(np.minimum(xp, 20.0))) + np.log(xp**2 + 1.0)
    res = val % MST_MOD
    if isinstance(res, (float, np.float64)):
        return int(res)
    return res


def phi_infinity_shard(x: Any, alpha: float = 1.0) -> LatticeValue:  # noqa: ANN401
    """Calculates a single phi^inf spectral shard with alpha modulation."""
    return x / (PHI * alpha)


def qrt_damping(x: Any) -> LatticeValue:  # noqa: ANN401
    """Calculates the QRT damping factor for scalar or tensor inputs."""
    type_str = str(type(x))
    if "torch" in type_str:
        import torch

        return torch.exp(-(x**2) / PHI)
    return np.exp(-(x**2) / PHI)


class TUPTMixer:
    """Professional stateful mixer for TUPT pattern generation."""

    def __init__(self, seed: Optional[int] = None) -> None:
        """Initialises the stateful TUPT mixer manifold."""
        self.state = float(seed) if seed is not None else PHI
        self._counter = 0

    def next_residue(self) -> float:
        """Generates the next resonant residue in the sequence."""
        self.state = (self.state * PHI + 1.2345) % TUPT_MOD
        self._counter += 1
        return float(self.state)

    @staticmethod
    def mix(a: float, b: float) -> float:
        """Static mix manifold for two residues."""
        return float((a + b * PHI) % TUPT_MOD)
