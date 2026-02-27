import numpy as np

def fib_mod9(n):
    """Generate first n Fibonacci numbers mod 9."""
    fibs = np.zeros(n, dtype=int)
    fibs[0], fibs[1] = 0, 1
    for i in range(2, n):
        fibs[i] = (fibs[i-1] + fibs[i-2]) % 9
    return fibs

def modular_projector(seq):
    """
    Applies the M(r) Modular Exclusion Projector to the sequence.
    M(r) = 0 if r(mod 9) in {0, 3, 6}, else 1
    """
    excluded = {0, 3, 6}
    return np.array([0 if x in excluded else 1 for x in seq])

def demonstrate_variance_reduction():
    print("Nexus Resonance Codex - Variance Reduction Demo")
    
    n_terms = 500
    fibs = fib_mod9(n_terms)
    
    # Original partial sums
    S_n = np.cumsum(fibs)
    var_original = np.var(S_n)
    
    # Filtered partial sums
    filtered_fibs = fibs * modular_projector(fibs)
    S_tilde_n = np.cumsum(filtered_fibs)
    var_filtered = np.var(S_tilde_n)
    
    print(f"Variance of original partial sums: {var_original:.2f}")
    print(f"Variance of filtered partial sums: {var_filtered:.2f}")
    print(f"Reduction ratio: {var_filtered / var_original:.3f}")

if __name__ == "__main__":
    demonstrate_variance_reduction()
