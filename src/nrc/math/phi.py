import math
from typing import Literal, Union, overload

import mpmath  # type: ignore[import-untyped]
import numpy as np

# Professional Global Constants
PHI_FLOAT: float = (1 + math.sqrt(5)) / 2
PHI_INVERSE_FLOAT: float = 1 / PHI_FLOAT
SQRT_5_FLOAT: float = math.sqrt(5)
THETA_QRT: float = 51.853
RAD_QRT: float = THETA_QRT * (math.pi / 180.0)


@overload
def binet_formula(n: int, as_mpmath: Literal[False] = ...) -> float: ...


@overload
def binet_formula(n: int, as_mpmath: Literal[True]) -> mpmath.mpf: ...


def binet_formula(n: int, as_mpmath: bool = False) -> Union[float, mpmath.mpf]:
    """Calculates n-th Fibonacci value via continuous Binet projection."""
    if as_mpmath:
        phi = (mpmath.mpf(1) + mpmath.sqrt(5)) / 2
        sqrt5 = mpmath.sqrt(5)
        return (phi**n - (-phi) ** (-n)) / sqrt5

    return float((PHI_FLOAT**n - (-PHI_FLOAT) ** (-n)) / SQRT_5_FLOAT)


@overload
def phi_projection(x: float) -> float: ...


@overload
def phi_projection(x: np.ndarray) -> np.ndarray: ...


def phi_projection(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Projects scalar or vector into the Phi-resonant frequency manifold."""
    if isinstance(x, np.ndarray):
        return x * PHI_FLOAT
    return float(x * PHI_FLOAT)


def phi_infinity_fold(x: Union[float, np.ndarray], iterations: int = 5) -> Union[float, np.ndarray]:
    """Computes the φ^∞ topological folding mechanic."""
    for n in range(1, iterations + 1):
        x = (PHI_FLOAT**n) * x + (1.0 / SQRT_5_FLOAT)
    return x
