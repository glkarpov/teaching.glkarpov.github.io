import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.patches as patches

# Настройка для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

def plot_normal_problem(problem_num, x_range, prob_range, title, mu=6, sigma=5):
    """
    Создает график для задачи с нормальным распределением
    
    Parameters:
    - problem_num: номер задачи
    - x_range: диапазон x для исходного распределения (a, b)
    - prob_range: диапазон для стандартного нормального (z_a, z_b)
    - title: заголовок задачи
    - mu: среднее исходного распределения
    - sigma: стандартное отклонение исходного распределения
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=False)
    
    # Верхний график: исходное нормальное распределение
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = norm.pdf(x, mu, sigma)
    
    ax1.plot(x, y, 'b-', linewidth=2, label=f'$X \\sim \\mathcal{{N}}({mu}, {sigma}^2)$')
    ax1.fill_between(x, 0, y, where=((x >= x_range[0]) & (x <= x_range[1])), 
                     color='red', alpha=0.5, label='Запрашиваемая вероятность')
    
    ax1.set_ylabel('Плотность вероятности')
    ax1.set_title(f'Задача {problem_num}: {title}')
    ax1.legend()
    ax1.grid(True, alpha=0.6)
    ax1.set_xlim(mu - 4*sigma, mu + 4*sigma)
    
    # Нижний график: стандартное нормальное распределение
    # Используем тот же диапазон X, но показываем стандартное нормальное
    z = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    z_y = norm.pdf(z, 0, 1)  # Стандартное нормальное с центром в 0
    
    ax2.plot(z, z_y, 'g-', linewidth=2, label='$Z \\sim \\mathcal{N}(0, 1)$')
    ax2.fill_between(z, 0, z_y, where=((z >= prob_range[0]) & (z <= prob_range[1])), 
                     color='orange', alpha=0.5, label='Преобразованная область')
    
    ax2.set_xlabel('Значение')
    ax2.set_ylabel('Плотность вероятности')
    ax2.set_title('Стандартное нормальное распределение')
    ax2.legend()
    ax2.grid(True, alpha=0.6)
    ax2.set_xlim(mu - 4*sigma, mu + 4*sigma)
    
    # Добавляем вертикальные линии для границ
    if x_range[0] != x_range[1]:  # Если это не точка
        ax1.axvline(x_range[0], color='red', linestyle='--', alpha=0.7)
        ax1.axvline(x_range[1], color='red', linestyle='--', alpha=0.7)
    
    if prob_range[0] != prob_range[1]:  # Если это не точка
        ax2.axvline(prob_range[0], color='orange', linestyle='--', alpha=0.7)
        # Добавляем вторую линию только если второй конец не бесконечность
        if prob_range[1] != float('inf') and prob_range[1] != 4:  # 4 используется как "бесконечность" в задаче 4
            ax2.axvline(prob_range[1], color='orange', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    return fig

# Задача 1: P(6 ≤ X ≤ 12)
fig1 = plot_normal_problem(1, (6, 12), (0, 1.2), 
                          '$P(6 \\leq X \\leq 12)$')
plt.savefig('problem_1.png', dpi=300, bbox_inches='tight')
plt.show()

# Задача 2: P(0 ≤ X ≤ 8)
fig2 = plot_normal_problem(2, (0, 8), (-1.2, 0.4), 
                          '$P(0 \\leq X \\leq 8)$')
plt.savefig('problem_2.png', dpi=300, bbox_inches='tight')
plt.show()

# Задача 3: P(-2 < X ≤ 0)
fig3 = plot_normal_problem(3, (-2, 0), (-1.6, -1.2), 
                          '$P(-2 < X \\leq 0)$')
plt.savefig('problem_3.png', dpi=300, bbox_inches='tight')
plt.show()

# Задача 4: P(X > 21)
fig4 = plot_normal_problem(4, (21, 30), (3, 4), 
                          '$P(X > 21)$')
plt.savefig('problem_4.png', dpi=300, bbox_inches='tight')
plt.show()

# Задача 5: P(|X - 6| < 5) = P(1 < X < 11)
fig5 = plot_normal_problem(5, (1, 11), (-1, 1), 
                          '$P(|X - 6| < 5) = P(1 < X < 11)$')
plt.savefig('problem_5.png', dpi=300, bbox_inches='tight')
plt.show()

print("Все графики созданы и сохранены!")
print("Отдельные задачи: problem_1.png - problem_5.png")
