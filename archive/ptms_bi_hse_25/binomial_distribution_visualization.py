#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Визуализация функции массы вероятности биномиального распределения
для различных значений параметра p
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import matplotlib.backends.backend_pdf as backend_pdf

# Настройка шрифтов для корректного отображения русского текста
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['legend.fontsize'] = 12

def plot_binomial_pmf(n, p_values, titles, filename):
    """
    Создает график PMF биномиального распределения для заданных параметров
    
    Parameters:
    n (int): количество испытаний
    p_values (list): список значений вероятности успеха
    titles (list): список заголовков для каждого графика
    filename (str): имя файла для сохранения
    """
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Функция вероятности биномиального распределения\n' + 
                 f'n = {n} испытаний', fontsize=18, y=1.02)
    
    # Значения k для построения графика
    k_values = np.arange(0, n + 1)
    
    colors = ['#d62728', '#2ca02c', '#1f77b4']  # красный, зеленый, синий
    
    for i, (p, title, color) in enumerate(zip(p_values, titles, colors)):
        # Вычисление PMF
        pmf_values = binom.pmf(k_values, n, p)
        
        # Создание столбчатой диаграммы
        axes[i].bar(k_values, pmf_values, alpha=0.7, color=color, 
                   edgecolor='black', linewidth=0.5)
        
        # Добавление линий для лучшей визуализации
        axes[i].plot(k_values, pmf_values, 'o-', color='darkred', 
                    markersize=4, linewidth=1.5, alpha=0.8)
        
        # Настройка осей и заголовков
        axes[i].set_xlabel('Количество успехов (k)')
        axes[i].set_ylabel('Вероятность P(X = k)')
        axes[i].set_title(f'{title}\np = {p}')
        axes[i].grid(True, alpha=0.3)
        axes[i].set_ylim(0, max(pmf_values) * 1.1)
        
        # Добавление статистических показателей
        mean = n * p
        variance = n * p * (1 - p)
        std = np.sqrt(variance)
        
        # Текстовая аннотация с статистикой
        stats_text = f'μ = {mean:.2f}\nσ² = {variance:.2f}\nσ = {std:.2f}'
        axes[i].text(0.02, 0.98, stats_text, transform=axes[i].transAxes,
                    verticalalignment='top', bbox=dict(boxstyle='round', 
                    facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    
    # Сохранение в PDF
    with backend_pdf.PdfPages(filename) as pdf:
        pdf.savefig(fig, bbox_inches='tight', dpi=300)
    
    plt.close()
    print(f"График сохранен в файл: {filename}")

def create_individual_plots(n, p_values, titles):
    """
    Создает отдельные графики для каждого значения p
    """
    k_values = np.arange(0, n + 1)
    colors = ['#d62728', '#2ca02c', '#1f77b4']
    
    for i, (p, title, color) in enumerate(zip(p_values, titles, colors)):
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        
        # Вычисление PMF
        pmf_values = binom.pmf(k_values, n, p)
        
        # Создание столбчатой диаграммы
        ax.bar(k_values, pmf_values, alpha=0.7, color=color, 
               edgecolor='black', linewidth=0.8)
        
        # Добавление линий
        ax.plot(k_values, pmf_values, 'o-', color='darkred', 
                markersize=6, linewidth=2, alpha=0.9)
        
        # Настройка графика
        ax.set_xlabel('Количество успехов (k)', fontsize=14)
        ax.set_ylabel('Вероятность P(X = k)', fontsize=14)
        ax.set_title(f'Биномиальное распределение: {title}\n' + 
                    f'n = {n}, p = {p}', fontsize=16)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, max(pmf_values) * 1.1)
        
        # Статистические показатели
        mean = n * p
        variance = n * p * (1 - p)
        std = np.sqrt(variance)
        
        stats_text = f'Среднее значение (μ) = {mean:.2f}\n' + \
                    f'Дисперсия (σ²) = {variance:.2f}\n' + \
                    f'Стандартное отклонение (σ) = {std:.2f}'
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
                verticalalignment='top', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        plt.tight_layout()
        
        # Сохранение отдельного файла
        filename = f'binomial_pmf_p_{p:.1f}.pdf'
        with backend_pdf.PdfPages(filename) as pdf:
            pdf.savefig(fig, bbox_inches='tight', dpi=300)
        
        plt.close()
        print(f"Отдельный график сохранен в файл: {filename}")

def main():
    """
    Основная функция для создания всех визуализаций
    """
    # Параметры
    n = 20  # количество испытаний
    p_values = [0.7, 0.5, 0.3]  # p > 0.5, p = 0.5, p < 0.5
    titles = ['p > 0.5 (смещение вправо)', 
              'p = 0.5 (симметричное)', 
              'p < 0.5 (смещение влево)']
    
    print("Создание визуализаций биномиального распределения...")
    print(f"Параметры: n = {n}, p = {p_values}")
    print("-" * 60)
    
    # Создание общего графика с тремя подграфиками
    plot_binomial_pmf(n, p_values, titles, 'binomial_pmf_comparison.pdf')
    
    # Создание отдельных графиков
    create_individual_plots(n, p_values, titles)
    
    print("-" * 60)
    print("Все графики успешно созданы и сохранены в PDF файлы!")
    print("\nСозданные файлы:")
    print("1. binomial_pmf_comparison.pdf - сравнительный график")
    print("2. binomial_pmf_p_0.7.pdf - график для p > 0.5")
    print("3. binomial_pmf_p_0.5.pdf - график для p = 0.5") 
    print("4. binomial_pmf_p_0.3.pdf - график для p < 0.5")

if __name__ == "__main__":
    main()
