import numpy as np
from scipy import stats

print('=== ВАРИАНТ 1 ===')
# X̄ ~ N(1, 4/12), Ȳ ~ N(-2, 9/6), Z̄ ~ N(0, 1/4)
# W = X̄ + Ȳ + Z̄
E_W = 1 + (-2) + 0
Var_W = 4/12 + 9/6 + 1/4
print(f'E[W] = {E_W}')
print(f'Var[W] = {Var_W}')
print(f'σ_W = {np.sqrt(Var_W):.4f}')
z_score = (0.42 - E_W) / np.sqrt(Var_W)
prob = stats.norm.cdf(z_score)
print(f'z-score = {z_score:.4f}')
print(f'P(W < 0.42) = {prob:.4f}')

print('\n=== ВАРИАНТ 2 ===')
# X̄ ~ N(2, 5/8), Ȳ ~ N(-1, 6/10), Z̄ ~ N(1, 2/5)
# W = X̄ - Ȳ + Z̄
E_W = 2 - (-1) + 1
Var_W = 5/8 + 6/10 + 2/5
print(f'E[W] = {E_W}')
print(f'Var[W] = {Var_W}')
print(f'σ_W = {np.sqrt(Var_W):.4f}')
z_score = (3.5 - E_W) / np.sqrt(Var_W)
prob = stats.norm.cdf(z_score)
print(f'z-score = {z_score:.4f}')
print(f'P(W < 3.5) = {prob:.4f}')

print('\n=== ВАРИАНТ 3 ===')
# X̄ ~ N(0, 3/6), Ȳ ~ N(2, 4/9), Z̄ ~ N(-1, 5/7)
# W = X̄ + Ȳ + Z̄
E_W = 0 + 2 + (-1)
Var_W = 3/6 + 4/9 + 5/7
print(f'E[W] = {E_W}')
print(f'Var[W] = {Var_W}')
print(f'σ_W = {np.sqrt(Var_W):.4f}')
# P(W > k) = 0.75 означает P(W < k) = 0.25
z_025 = stats.norm.ppf(0.25)
k = E_W + z_025 * np.sqrt(Var_W)
print(f'z_0.25 = {z_025:.4f}')
print(f'k = {k:.4f}')
print(f'Проверка: P(W > {k:.4f}) = {1 - stats.norm.cdf((k - E_W)/np.sqrt(Var_W)):.4f}')

print('\n=== ВАРИАНТ 4 ===')
# X̄ ~ N(3, 7/10), Ȳ ~ N(-2, 8/4), Z̄ ~ N(1, 3/8)
# W = X̄ + 2Ȳ - Z̄
E_W = 3 + 2*(-2) - 1
Var_W = 7/10 + 4*(8/4) + 3/8  # Var[2Ȳ] = 4*Var[Ȳ]
print(f'E[W] = {E_W}')
print(f'Var[W] = {Var_W}')
print(f'σ_W = {np.sqrt(Var_W):.4f}')
z_score = (2.3 - E_W) / np.sqrt(Var_W)
prob = stats.norm.cdf(z_score)
print(f'z-score = {z_score:.4f}')
print(f'P(W < 2.3) = {prob:.4f}')
