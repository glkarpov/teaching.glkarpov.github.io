#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Анимация дискретной кумулятивной функции распределения (CDF)
Показывает пошаговое построение CDF с движущейся точкой
для произвольной дискретной случайной величины
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Настройка шрифтов для корректного отображения русского текста
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['legend.fontsize'] = 12

def create_cdf_animation(states, probabilities, filename='discrete_cdf_animation.gif'):
    """
    Создает GIF анимацию дискретной CDF для произвольной случайной величины
    
    Parameters:
    states (list): значения случайной величины
    probabilities (list): соответствующие вероятности
    filename (str): имя файла для сохранения GIF
    """
    
    # Сортируем состояния по возрастанию для правильного построения CDF
    sorted_indices = np.argsort(states)
    sorted_states = np.array(states)[sorted_indices]
    sorted_probabilities = np.array(probabilities)[sorted_indices]
    
    # Вычисляем CDF
    cdf_values = np.cumsum(sorted_probabilities)
    
    # Создаем фигуру с двумя подграфиками
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'X = {states}, P = {probabilities}', 
                 fontsize=16, y=0.95)
    
    # Настройка первого графика (PMF)
    start_x = sorted_states[0] - 1  # Начальная позиция анимации
    end_x = sorted_states[-1] + 1   # Конечная позиция анимации
    ax1.set_xlim(start_x, end_x)
    ax1.set_ylim(0, max(sorted_probabilities) * 1.2)
    ax1.set_ylabel(r'Вероятность $P_X(X = x)$')
    ax1.set_title('Функция вероятности')
    ax1.grid(True, alpha=0.3)
    
    # Настройка второго графика (CDF)
    ax2.set_xlim(start_x, end_x)
    ax2.set_ylim(0, 1.1)
    ax2.set_title(r'Функция распределения $F_X(x) = P(X \leq x)$')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Инициализация элементов анимации
    bars = ax1.bar(sorted_states, [0] * len(sorted_states), alpha=0.7, color='skyblue', 
                   edgecolor='navy', linewidth=1, width=0.1)
    
    # Линии для CDF - используем step для правильной ступенчатой функции
    cdf_line, = ax2.step([], [], where='post', linewidth=3, 
                        color='darkred', alpha=0.8, label='CDF')
    
    # Движущаяся точка
    moving_point, = ax2.plot([], [], 'o', markersize=12, color='gold', 
                            markeredgecolor='black', markeredgewidth=2, 
                            zorder=10, label='Текущая позиция')
    
    # Текст с текущим значением CDF
    cdf_text = ax2.text(0.02, 0.95, '', transform=ax2.transAxes, 
                       fontsize=12, bbox=dict(boxstyle='round', 
                       facecolor='lightyellow', alpha=0.8))
    
    def animate(frame):
        """Функция анимации для каждого кадра"""
        # Плавное движение точки по горизонтали от (первое значение - 1) до последнего состояния + 1
        start_x = sorted_states[0] - 1  # Динамическая начальная позиция
        end_x = sorted_states[-1] + 1
        total_frames = len(sorted_states) * 20  # 20 кадров на каждое состояние для плавности
        progress = min(frame / total_frames, 1.0)
        
        # Определяем текущую позицию точки
        current_x = start_x + progress * (end_x - start_x)
        
        # Определяем текущий индекс состояния
        current_idx = -1  # Начинаем с -1, чтобы показать CDF = 0
        for i, state in enumerate(sorted_states):
            if current_x >= state:
                current_idx = i
            else:
                break
        
        # Обновляем PMF (показываем только до текущего индекса)
        for i, bar in enumerate(bars):
            if i <= current_idx:
                bar.set_height(sorted_probabilities[i])
                bar.set_color('lightcoral' if i == current_idx else 'skyblue')
            else:
                bar.set_height(0)
                bar.set_color('lightgray')
        
        # Обновляем CDF (ступенчатая функция, строящаяся синхронно с точкой)
        # Создаем данные для step функции
        x_cdf = []
        y_cdf = []
        
        # Начинаем с левой стороны (динамическая начальная позиция)
        x_cdf.append(start_x)
        y_cdf.append(0)
        
        # Добавляем все состояния до текущего индекса
        for i in range(current_idx + 1):
            x_cdf.append(sorted_states[i])
            y_cdf.append(cdf_values[i])
        
        # Добавляем текущую позицию точки
        if current_idx >= 0:
            x_cdf.append(current_x)
            y_cdf.append(cdf_values[current_idx])
        else:
            # Если точка еще не дошла до первого состояния, CDF остается на уровне 0
            x_cdf.append(current_x)
            y_cdf.append(0)
        
        # Обновляем step функцию
        cdf_line.set_data(x_cdf, y_cdf)
            
        # Обновляем движущуюся точку (плавно по горизонтали)
        # Вычисляем Y-координату для текущей X
        if current_idx < 0:
            current_y = 0
        else:
            current_y = cdf_values[current_idx]
        
        moving_point.set_data([current_x], [current_y])
        
        # Обновляем текст
        cdf_text.set_text(f'x = {current_x:.1f}\nF({current_x:.1f}) = {current_y:.3f}')
        
        return bars, cdf_line, moving_point, cdf_text
    
    # Создаем анимацию
    total_frames = len(sorted_states) * 20 + 5  # 20 кадров на каждое состояние + 5 дополнительных
    anim = animation.FuncAnimation(fig, animate, frames=total_frames, 
                                 interval=30, blit=False, repeat=True)
    
    # Сохраняем как GIF
    print(f"Создание GIF анимации...")
    anim.save(filename, writer='pillow', fps=5, dpi=100)
    print(f"GIF анимация сохранена в файл: {filename}")
    
    plt.close()
    return anim


def create_step_by_step_animation(states, probabilities, filename='step_by_step_cdf.gif'):
    """
    Создает пошаговую анимацию с подробными объяснениями
    """
    
    # Сортируем состояния по возрастанию
    sorted_indices = np.argsort(states)
    sorted_states = np.array(states)[sorted_indices]
    sorted_probabilities = np.array(probabilities)[sorted_indices]
    cdf_values = np.cumsum(sorted_probabilities)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    fig.suptitle(f'Пошаговое построение CDF: X = {states}, P = {probabilities}', fontsize=16)
    
    # Настройка PMF графика
    x_min, x_max = min(sorted_states) - 1, max(sorted_states) + 1
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(0, max(sorted_probabilities) * 1.2)
    ax1.set_xlabel('x (значения случайной величины)')
    ax1.set_ylabel('P(X = x)')
    ax1.set_title('Функция массы вероятности')
    ax1.grid(True, alpha=0.3)
    
    # Настройка CDF графика
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(0, 1.1)
    ax2.set_xlabel('x (значения случайной величины)')
    ax2.set_ylabel('F(x) = P(X ≤ x)')
    ax2.set_title('Кумулятивная функция распределения')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7)
    
    # Инициализация
    bars = ax1.bar(sorted_states, [0] * len(sorted_states), alpha=0.6, color='lightblue',
                   edgecolor='navy', linewidth=1, width=0.8)
    
    cdf_line, = ax2.plot([], [], 'ro-', linewidth=3, markersize=8, 
                        color='darkred', alpha=0.8)
    
    moving_point, = ax2.plot([], [], 'o', markersize=15, color='gold',
                            markeredgecolor='black', markeredgewidth=3, zorder=10)
    
    # Текстовые аннотации
    step_text = ax2.text(0.02, 0.85, '', transform=ax2.transAxes, fontsize=11,
                        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    cdf_text = ax2.text(0.02, 0.65, '', transform=ax2.transAxes, fontsize=11,
                       bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    def animate(frame):
        current_idx = frame
        
        # Обновляем PMF
        for i, bar in enumerate(bars):
            if i <= current_idx:
                bar.set_height(sorted_probabilities[i])
                bar.set_color('coral' if i == current_idx else 'lightblue')
            else:
                bar.set_height(0)
                bar.set_color('lightgray')
        
        # Обновляем CDF (ступенчатая функция)
        if current_idx >= 0 and current_idx < len(sorted_states):
            # Создаем ступенчатую функцию CDF без вертикальных линий
            x_cdf = []
            y_cdf = []
            
            for i in range(current_idx + 1):
                if i == 0:
                    x_cdf.extend([sorted_states[i] - 2, sorted_states[i]])
                    y_cdf.extend([0, 0])
                else:
                    x_cdf.extend([sorted_states[i-1], sorted_states[i]])
                    y_cdf.extend([cdf_values[i-1], cdf_values[i-1]])
            
            if current_idx < len(sorted_states):
                x_cdf.extend([sorted_states[current_idx], sorted_states[current_idx] + 2])
                y_cdf.extend([cdf_values[current_idx], cdf_values[current_idx]])
            
            cdf_line.set_data(x_cdf, y_cdf)
            moving_point.set_data([sorted_states[current_idx]], [cdf_values[current_idx]])
            
            # Обновляем тексты
            if current_idx == 0:
                step_text.set_text(f'Шаг {current_idx + 1}: F({sorted_states[0]}) = P(X ≤ {sorted_states[0]}) = P(X = {sorted_states[0]})')
                cdf_text.set_text(f'F({sorted_states[0]}) = {cdf_values[0]:.4f}')
            else:
                prob_sum = ' + '.join([f'P(X = {sorted_states[i]})' for i in range(current_idx + 1)])
                step_text.set_text(f'Шаг {current_idx + 1}: F({sorted_states[current_idx]}) = P(X ≤ {sorted_states[current_idx]})\n' +
                                 f'= {prob_sum}')
                cdf_text.set_text(f'F({sorted_states[current_idx]}) = {cdf_values[current_idx]:.4f}\n' +
                                f'Сумма вероятностей: {cdf_values[current_idx]:.4f}')
        
        return bars, cdf_line, moving_point, step_text, cdf_text
    
    # Создаем анимацию
    anim = animation.FuncAnimation(fig, animate, frames=len(sorted_states) + 2, 
                                 interval=1000, blit=False, repeat=True)
    
    # Сохраняем как GIF
    print(f"Создание пошаговой GIF анимации...")
    anim.save(filename, writer='pillow', fps=1, dpi=100)
    print(f"Пошаговая GIF анимация сохранена в файл: {filename}")
    
    plt.close()
    return anim

def main():
    """
    Основная функция для создания всех анимаций
    """
    print("Создание GIF анимаций для дискретной CDF...")
    print("=" * 60)
    
    # Создаем папку для анимаций, если её нет
    if not os.path.exists('animations'):
        os.makedirs('animations')
    
    # Определяем случайную величину: X = {-1, 0, 1, 2} с вероятностями {0.1, 0.5, 0.3, 0.1}
    states = [-2, 0, 1, 4]
    probabilities = [0.1, 0.5, 0.3, 0.1]
    
    print(f"Случайная величина: X = {states}")
    print(f"Вероятности: P = {probabilities}")
    print(f"Проверка: сумма вероятностей = {sum(probabilities)}")
    print("-" * 60)
    
    # 1. Основная анимация CDF
    print("1. Создание основной анимации CDF...")
    create_cdf_animation(states, probabilities, filename='animations/discrete_cdf_animation.gif')

    # 3. Пошаговая анимация с объяснениями
    print("\n3. Создание пошаговой анимации...")
    create_step_by_step_animation(states, probabilities, filename='animations/step_by_step_cdf.gif')
    
    print("\n" + "=" * 60)
    print("Все GIF анимации успешно созданы!")

if __name__ == "__main__":
    main()
