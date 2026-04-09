"""Golden Tensor Topology (GTT).
============================
Explicit 5-dimensional geometric framework governing all NRC matrices.
Applies the 5th spatial dimension acting strictly as the Resonance Phase-Space (φ-axis).
"""

import math


def check_gtt_phase(n: int) -> str:
    """[CONJ] Calculates the 5D continuous Binet phase for iteration n.
    If the continuous phase collides with the modulo 9 values {0, 3, 6, 9},
    the structure undergos Void Collapse (Destructive Interference).

    Args:
        n: The discrete time/iteration step.

    Returns:
        String representing topological stability.
    """
    phi = (1 + math.sqrt(5)) / 2
    # The Binet continuous phase topological mapping
    try:
        rho = (phi**n - (-phi) ** (-n)) / math.sqrt(5)
    except OverflowError:
        rho = float("inf")

    if math.isinf(rho):
        return "GTT STABLE (Asymptotic Resonance)"

    # Topological boundary check: does the integer curve collapse into 3-6-9?
    mod_phase = int(round(rho)) % 9

    if mod_phase in [0, 3, 6, 9]:
        return "VOID COLLAPSE (Destructive Interference)"
    return "GTT STABLE (Constructive Resonance)"


if __name__ == "__main__":
    print("Testing First 15 GTT Nodes:")
    for x in range(1, 16):
        print(f"Node {x}: {check_gtt_phase(x)}")
