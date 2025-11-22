import numpy as np
import matplotlib.pyplot as plt


def leibniz_pi(n):
    partial_sums = np.zeros(n)
    current_sum = 0

    for k in range(n):
        term = 1 / ((4 * k + 1) * (4 * k + 3))
        current_sum += term
        partial_sums[k] = 8 * current_sum

    return partial_sums


def euler_pi(n):
    partial_sums = np.zeros(n)
    current_sum = 0

    for k in range(1, n + 1):
        term = 1 / (k ** 2)
        current_sum += term
        partial_sums[k - 1] = np.sqrt(6 * current_sum)

    return partial_sums


def plot_pi_convergence(N):
    pi_true = np.pi
    leibniz_approx = leibniz_pi(N)
    euler_approx = euler_pi(N)

    leibniz_errors = np.abs(leibniz_approx - pi_true)
    euler_errors = np.abs(euler_approx - pi_true)
    print("\nComputing π:\n")
    print(f"Number of terms: N = {N}")
    print(f"True value of π: {pi_true:.15f}\n")

    print(f"Leibniz formula:")
    print(f"  Approximation: {leibniz_approx[-1]:.15f}")
    print(f"  Final error:   {leibniz_errors[-1]:.2e}\n")

    print(f"Euler formula:")
    print(f"  Approximation: {euler_approx[-1]:.15f}")
    print(f"  Final error:   {euler_errors[-1]:.2e}\n")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    iterations = np.arange(1, N + 1)
    ax1.semilogy(iterations, leibniz_errors, 'b-', linewidth=2,
                 label='Leibniz formula', alpha=0.7)
    ax1.semilogy(iterations, euler_errors, 'r-', linewidth=2,
                 label='Euler formula', alpha=0.7)
    ax1.set_xlabel('Number of terms (N)', fontsize=12)
    ax1.set_ylabel('Absolute error |π_approx - π_true|', fontsize=12)
    ax1.set_title('Convergence of π approximations (log scale)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)

    ax2.plot(iterations, leibniz_approx, 'b-', linewidth=2,
             label='Leibniz formula', alpha=0.7)
    ax2.plot(iterations, euler_approx, 'r-', linewidth=2,
             label='Euler formula', alpha=0.7)
    ax2.axhline(y=pi_true, color='g', linestyle='--', linewidth=2,
                label='True π', alpha=0.7)
    ax2.set_xlabel('Number of terms (N)', fontsize=12)
    ax2.set_ylabel('π approximation', fontsize=12)
    ax2.set_title('Evolution of π approximations', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig('pi_convergence.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nGraph interpretation\n")
    print("1. CONVERGENCE SPEED:")
    print(f"   - Euler's formula converges MUCH faster than Leibniz")
    print(f"   - At N={N}: Euler error ≈ {euler_errors[-1]:.2e}, "
          f"Leibniz error ≈ {leibniz_errors[-1]:.2e}")
    print(f"   - Euler is approximately {leibniz_errors[-1] / euler_errors[-1]:.0f}× more accurate\n")

    print("2. CONVERGENCE RATE:")
    print(f"   - Leibniz: O(1/N) - linear convergence (very slow)")
    print(f"   - Euler: O(1/N²) - quadratic convergence (much faster)\n")

    print("3. PRACTICAL IMPLICATIONS:")
    print(f"   - For same accuracy, Euler needs far fewer terms")
    print(f"   - Leibniz requires ~10,000 terms for 3 decimal places")
    print(f"   - Euler requires only ~100 terms for same precision\n")


plot_pi_convergence(N=100)