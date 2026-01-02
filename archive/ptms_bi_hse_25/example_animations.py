"""
Пример использования обобщенной функции для создания анимаций PDF/CDF
"""

from animation_utils import create_pdf_cdf_animation, create_two_point_animation, uniform_pdf, uniform_cdf, exponential_pdf, exponential_cdf
import numpy as np

def main():
    # Пример 1: Равномерное распределение от 0 до 10
    # print("Создание анимации для равномерного распределения (0, 10)...")
    # create_pdf_cdf_animation(
    #     pdf_func=lambda x: uniform_pdf(x, 0, 10),
    #     cdf_func=lambda x: uniform_cdf(x, 0, 10),
    #     x_range=(-2, 12, 0.01),
    #     title="Равномерное распределение (0, 10)",
    #     filename="uniform_0_10_example.gif",
    #     color='blue'
    # )
    
    # # Пример 2: Равномерное распределение от -5 до 5
    # print("Создание анимации для равномерного распределения (-5, 5)...")
    # create_pdf_cdf_animation(
    #     pdf_func=lambda x: uniform_pdf(x, -5, 5),
    #     cdf_func=lambda x: uniform_cdf(x, -5, 5),
    #     x_range=(-7, 7, 0.01),
    #     title="Равномерное распределение (-5, 5)",
    #     filename="uniform_neg5_5_example.gif",
    #     color='green'
    # )
    
    # # Пример 3: Экспоненциальное распределение
    # print("Создание анимации для экспоненциального распределения...")
    # create_pdf_cdf_animation(
    #     pdf_func=lambda x: exponential_pdf(x, rate=1),
    #     cdf_func=lambda x: exponential_cdf(x, rate=1),
    #     x_range=(-1, 8, 0.01),
    #     title="Экспоненциальное распределение (rate=1)",
    #     filename="exponential_1_example.gif",
    #     color='red'
    # )


    # def triangular_pdf(x, a=0, b=2, c=1):
    #     """PDF для треугольного распределения"""
    #     if x < a or x > b:
    #         return 0
    #     elif x < c:
    #         return 2 * (x - a) / ((b - a) * (c - a))
    #     else:
    #         return 2 * (b - x) / ((b - a) * (b - c))
    
    # def triangular_cdf(x, a=0, b=2, c=1):
    #     """CDF для треугольного распределения"""
    #     if x < a:
    #         return 0
    #     elif x > b:
    #         return 1
    #     elif x < c:
    #         return (x - a) ** 2 / ((b - a) * (c - a))
    #     else:
    #         return 1 - (b - x) ** 2 / ((b - a) * (b - c))
    
    # print("Создание анимации для треугольного распределения...")
    # create_pdf_cdf_animation(
    #     pdf_func=lambda x: triangular_pdf(x, 0, 2, 1),
    #     cdf_func=lambda x: triangular_cdf(x, 0, 2, 1),
    #     x_range=(-0.5, 2.5, 0.01),
    #     title="Треугольное распределение (0, 2, 1)",
    #     filename="triangular_example.gif",
    #     color='purple'
    # )
    
    def parabolic_pdf(x, a=0, b=3, c=1/9):
        """PDF для треугольного распределения"""
        if x < a or x > b:
            return 0
        else:
            return c * (x ** 2)

    def parabolic_cdf(x, a=0, b=3, c=1/27):
        """CDF для треугольного распределения"""
        if x < a:
            return 0
        elif x > b:
            return 1
        else:
            return c * (x ** 3)
    
    print("Создание анимации для треугольного распределения...")
    create_pdf_cdf_animation(
        pdf_func=lambda x: parabolic_pdf(x, 0, 3, 1/9),
        cdf_func=lambda x: parabolic_cdf(x, 0, 3, 1/27),
        x_range=(-0.5, 3.5, 0.01),
        title="Пример из лекции",
        filename="parabolic_example.gif",
        color='purple'
    )
    
    print("Создание двухточечной анимации для параболического распределения...")
    create_two_point_animation(
        pdf_func=lambda x: parabolic_pdf(x, 0, 3, 1/9),
        cdf_func=lambda x: parabolic_cdf(x, 0, 3, 1/27),
        x_range=(-0.5, 3.5, 0.01),
        title="Difference between CDFs as probability",
        filename="two_point_parabolic.gif",
        delay_frames=20
    )

    print("Все анимации успешно созданы!")

if __name__ == "__main__":
    main()
