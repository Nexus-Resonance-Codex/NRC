#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L

"""Foundational prime number resonance and Trageser digital root manifold."""

from typing import Dict, List


def get_digital_root(n: int) -> int:
    """Calculates the digital root of an integer (mod 9 resonance)."""
    if n == 0:
        return 0
    res = n % 9
    return res if res != 0 else 9


def prime_manifold_density(primes: List[int]) -> Dict[int, float]:
    """Calculates the resonant density of prime indices in the NRC manifold."""
    res: Dict[int, float] = {}
    for p in primes:
        dr = get_digital_root(p)
        res[dr] = res.get(dr, 0.0) + 1.0
    return res
