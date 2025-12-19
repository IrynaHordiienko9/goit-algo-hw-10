import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import random


A = 0
B = 2
N_POINTS = 100_000
SEED = 42


def f(x):
    return x ** 2


def monte_carlo_numpy(f, a, b, n, seed=None):
    if seed is not None:
        np.random.seed(seed)
    x_rand = np.random.uniform(a, b, n)
    return (b - a) * np.mean(f(x_rand))


def monte_carlo_manual(f, a, b, n, seed=None):
    if seed is not None:
        random.seed(seed)
    sum_fx = 0
    for _ in range(n):
        x_r = random.uniform(a, b)
        sum_fx += f(x_r)
    return (b - a) * sum_fx / n


def analytical_integral(a, b):
    return (b ** 3) / 3 - (a ** 3) / 3


def quad_integral(f, a, b):
    return quad(f, a, b)


def plot_function(f, a, b):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'r', lw=2, label='$f(x)$')
    plt.fill_between(x, y, where=(x >= a) & (x <= b), color='gray', alpha=0.3, label='Площа під кривою')
    plt.axvline(a, color='gray', ls='--')
    plt.axvline(b, color='gray', ls='--')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.title(f'Графік інтегрування $f(x)$ від {a} до {b}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    plot_function(f, A, B)
    mc_numpy = monte_carlo_numpy(f, A, B, N_POINTS, SEED)
    mc_manual = monte_carlo_manual(f, A, B, N_POINTS, SEED)
    analytical = analytical_integral(A, B)
    quad_result, quad_error = quad_integral(f, A, B)

    print("\n--- Порівняння результатів ---")
    print(f"Монте-Карло (NumPy):        {mc_numpy:.6f}")
    print(f"Монте-Карло вручну:         {mc_manual:.6f}")
    print(f"Аналітичний розрахунок:     {analytical:.6f}")
    print(f"SciPy quad:                 {quad_result:.6f} (похибка: {quad_error:.2e})")


if __name__ == "__main__":
    main()
