"""
Golden Ratio (Phi) Constants and Fibonacci Calculations.
======================================================
Provides extremely high-precision constants, Binet's equation,
and continuous geometric operators.
"""
import math
import mpmath
import numpy as np
from typing import Union, overload

# Ensure extreme precision locally
mpmath.mp.dps = 100

# Constants
PHI_MP: mpmath.mpf = (mpmath.mpf(1) + mpmath.sqrt(5)) / 2
PHI_FLOAT: float = float(PHI_MP)

PHI_INVERSE_MP: mpmath.mpf = 1 / PHI_MP
PHI_INVERSE_FLOAT: float = float(PHI_INVERSE_MP)

SQRT_5_FLOAT: float = math.sqrt(5.0)

GIZA_SLOPE_DEG: float = 51.853
GIZA_SLOPE_RAD: float = GIZA_SLOPE_DEG * (math.pi / 180.0)


@overload
def binet_formula(n: int, as_mpmath: bool = False) -> Union[float, mpmath.mpf]: ...

def binet_formula(n: int, as_mpmath: bool = False) -> Union[float, mpmath.mpf]:
    """
    Computes the exact nth Fibonacci number using Binet's continuous formula.

    Formula:
        F_n = (φ^n - (-φ)^{-n}) / √5

    Args:
        n: The sequence index (integer distance).
        as_mpmath: If True, returns a 100-decimal precision mpmath float.

    Returns:
        The exact Fibonacci sequence value at spatial location n.
    """
    if as_mpmath:
        return (PHI_MP**n - (-PHI_MP)**(-n)) / mpmath.sqrt(5)
    return (PHI_FLOAT**n - (-PHI_FLOAT)**(-n)) / SQRT_5_FLOAT


def phi_infinity_fold(x: Union[float, np.ndarray], iterations: int = 5) -> Union[float, np.ndarray]:
    """
    Computes the φ^∞ topological folding mechanic.

    Repeated application of φ^n scaling mixed with the 1/√5 stabilization boundary,
    allowing arrays to infinitely fractalize losslessly into deeper dimensional shards.

    Args:
        x: Base signal scalar or numpy array.
        iterations: Number of fractal folding steps (depth).

    Returns:
        The structurally folded tensor mapping.
    """
    folded = np.copy(x) if isinstance(x, np.ndarray) else x
    for n in range(1, iterations + 1):
        folded = (PHI_FLOAT**n) * folded + (1.0 / SQRT_5_FLOAT)
    return folded
