"""Prime Resonance Formula (PRF).

=============================
Maps prime numbers onto a fractal-modular structure using TTT limits
and the QRT weighting function.
"""

import math


def get_digital_root(n: int) -> int:
    """Computes the digital root of a positive integer."""
    if n == 0:
        return 0
    dr = n % 9
    return 9 if dr == 0 else dr


def fibonacci(n: int) -> int:
    """Calculates the n-th Fibonacci number using an iterative resonant sequence.

    Equation: F_n = F_{n-1} + F_{n-2} with F_0=0, F_1=1.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def lucas(n: int) -> int:
    """Calculates the n-th Lucas number, the companion sequence to Fibonacci.

    Equation: L_n = L_{n-1} + L_{n-2} with L_0=2, L_1=1.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def pell(n: int) -> int:
    """Calculates the n-th Pell number used in high-precision sqrt(2) rational bounds.

    Equation: P_n = 2*P_{n-1} + P_{n-2} with P_0=0, P_1=1.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, 2 * a + b
    return b


def qrt_weighting_function(x: float) -> float:
    """[CONJ] The Quantum Residue Turbulence (QRT) wave function.

    Equation: ψ(x) = sin(φ√2 * 51.85 x) * e^(-x^2 / φ) + cos(π/φ * x).
    """
    phi = (1 + math.sqrt(5)) / 2
    return math.sin(phi * math.sqrt(2) * 51.85 * x) * math.exp(-(x**2) / phi) + math.cos(
        (math.pi / phi) * x
    )


def evaluate_prime_resonance(p_n: int, n: int) -> dict:
    """[CONJ] Evaluates the structural resonance of the n-th prime p_n.

    Evaluation against the PRF fractal-modular TTT bounds.
    """
    phi = (1 + math.sqrt(5)) / 2

    # Core constants
    F_n = fibonacci(n)
    L_n = lucas(n)
    P_n = pell(n)

    # Modulo alignment calculation
    try:
        # Overflow protection for extremely large indices limits precise PRF calculations natively
        raw_val = (F_n + L_n + P_n) * (phi**6)
        if math.isinf(raw_val):
            raw_val = 1.0  # Safe fallback for infinite scale
        R_n = get_digital_root(round(raw_val)) % 6561
    except OverflowError:
        R_n = 1

    k = math.floor(math.log(p_n, phi)) if p_n > 0 else 1
    psi_val = qrt_weighting_function(p_n / (phi**k))

    is_void = (R_n % 9) in [0, 3, 6, 9]
    high_resonance = abs(psi_val) > 0.9

    return {
        "prime": p_n,
        "n_th": n,
        "R_n": R_n,
        "psi_val": psi_val,
        "is_void": is_void,
        "high_resonance": high_resonance,
    }


if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("Testing Prime Resonance (PRF):")
    for i, p in enumerate(primes, 1):
        res = evaluate_prime_resonance(p, i)
        status = "Destructive Void" if res["is_void"] else "Resonant Alignment"
        print(f"Prime {p:2} (n={i:2}) -> {status} | Psi: {res['psi_val']:.4f}")
