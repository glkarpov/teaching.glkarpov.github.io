---
title: "Линейная алгебра"
subtitle: "Проекции. Ортогонализация базиса."
institute: "МНаД ФКН ВШЭ"
author: "Глеб Карпов"
format: 
    beamer:
        pdf-engine: xelatex
        aspectratio: 169
        fontsize: 9pt
        theme: Singapore
        fonmttheme: serif
        section-titles: true
        incremental: true
        include-in-header: ../files/xeheader.tex  # Custom LaTeX commands and preamble
---
## Ортогональные базисы.

::: {.callout-def}
#### Определение

Система векторов $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ называется ортогональной, если любые два вектора взаимно ортогональны, то есть $\left(\mathbf{v}_j, \mathbf{v}_k\right)=0$ при $j \neq k$.

Если дополнительно $\left\|\mathbf{v}_k\right\|=1$ для всех $k$, то система называется ортонормированной.
:::

## Зачем это нужно?

$$
\mathbf{x}=\alpha_1 \mathbf{v}_1+\alpha_2 \mathbf{v}_2+\ldots+\alpha_n \mathbf{v}_n=\sum_{j=1}^n \alpha_j \mathbf{v}_j
$$

Взяв скалярное произведение обеих частей равенства с $\mathbf{v}_1$, получаем
$$
\left(\mathbf{x}, \mathbf{v}_1\right)=\sum_{j=1}^n \alpha_j\left(\mathbf{v}_j, \mathbf{v}_1\right)=\alpha_1\left(\mathbf{v}_1, \mathbf{v}_1\right)=\alpha_1\left\|\mathbf{v}_1\right\|^2
$$


Аналогично, беря скалярное произведение обеих частей с $\mathbf{v}_k$, получаем
$$
\left(\mathbf{x}, \mathbf{v}_k\right)=\sum_{j=1}^n \alpha_j\left(\mathbf{v}_j, \mathbf{v}_k\right)=\alpha_k\left(\mathbf{v}_k, \mathbf{v}_k\right)=\alpha_k\left\|\mathbf{v}_k\right\|^2
$$

Итак
$$
\alpha_k=\frac{\left(\mathbf{x}, \mathbf{v}_k\right)}{\left\|\mathbf{v}_k\right\|^2}
$$

## Проекции

**Ортогональная проекция на вектор**.

:::: {.callout-def}
#### Определение (ортогональная проекция)

Пусть $\mathbf{x} \neq \mathbf{0}$. Обозначим единичный вектор в направлении $\mathbf{x}$ как
$$
\mathbf{u} = \frac{\mathbf{x}}{\|\mathbf{x}\|}.
$$
Ортогональная проекция вектора $\mathbf{y}$ на направление $\mathbf{x}$ (обозначение: $\Pr_{\mathbf{x}}(\mathbf{y})$) равна
$$
\Pr_{\mathbf{x}}(\mathbf{y}) = (\mathbf{y},\mathbf{u})\,\mathbf{u} = \frac{(\mathbf{y},\mathbf{x})}{\|\mathbf{x}\|^2}\,\mathbf{x}.
$$
::::

Сопряжённый (ортогональный) остаток:
$$
\mathbf{r} = \mathbf{y} - \Pr_{\mathbf{x}}(\mathbf{y}), \qquad (\mathbf{r},\mathbf{x})=0.
$$

## Пример: ортогональная проекция


\begin{tikzpicture}[scale=1.5]
% Координатные оси
\draw[->] (-0.5,0) -- (4,0) node[right] {$x_1$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$x_2$};

% Вектор x (синий)
\draw[thick, blue, ->] (0,0) -- (3,1);
\node[blue] at (3.2,1.2) {$\mathbf{x}$};

% Единичный вектор u (светло-синий)
\draw[thick, blue!60, ->] (0,0) -- (0.949,0.316) node[midway, below] {$\mathbf{u} = \frac{\mathbf{x}}{\|\mathbf{x}\|}$};

% Вектор y (красный)
\draw[thick, red, ->] (0,0) -- (2,2.5) node[pos=0.7, above] {$\mathbf{y}$};

% Ортогональная проекция y на x (зеленый)
\draw[thick, green, ->] (0,0) -- (2.55,0.85) node[pos=0.7, below] {$\Pr_{\mathbf{x}}(\mathbf{y})$};

% Темно-фиолетовая параллельная линия
\draw[very thick, violet!80!black] (0,0.1) -- (2.55,0.95);

% Ортогональный остаток (оранжевый) - теперь действительно ортогонален к x
\draw[thick, orange, ->] (2.55,0.85) -- (2,2.5) node[midway, right] {$\mathbf{r} = \mathbf{y} - \Pr_{\mathbf{x}}(\mathbf{y})$};

% Пунктирная линия для показа ортогональности
\draw[dashed, gray] (2,2.5) -- (2.55,0.85);

% Точка пересечения
\fill[black] (2.55,0.85) circle (1.5pt);

% Угол альфа между векторами x и y
\draw (0.3,0.1) arc (18.43:51.34:0.3);
\node at (0.4,0.25) {$\alpha$};

% Подписи формул
\node at (1.5,-0.4) {$\Pr_{\mathbf{x}}(\mathbf{y}) = \frac{(\mathbf{y},\mathbf{x})}{\|\mathbf{x}\|^2}\mathbf{x}$};
\node at (0.5,1.5) {$(\mathbf{r},\mathbf{x}) = 0$};
\end{tikzpicture}

$$
    \textcolor{green}{Pr_{x}(\mathbf{y})} = \textcolor{green}{\frac{(\mathbf{y},\mathbf{x})}{\|\mathbf{x}\|^2}\mathbf{x}} = \frac{(\mathbf{y},\mathbf{x})}{\|\mathbf{x}\|_2} \cdot \frac{\mathbf{x}}{\|\mathbf{x}\|_2} = \frac{\|\mathbf{y}\|_2 \|\mathbf{x}\|_2 \cos(\alpha)}{\|\mathbf{x}\|_2} \cdot \frac{\mathbf{x}}{\|\mathbf{x}\|_2} = \textcolor{violet!80!black}{\|\mathbf{y}\|_2 \cos(\alpha)} \cdot \textcolor{blue!60}{\frac{\mathbf{x}}{\|\mathbf{x}\|_2}}
$$


## Алгоритм Грама-Шмидта

Вход: линейно независимые векторы $\mathbf{x}_1,\ldots,\mathbf{x}_k$.

Шаги ортогонализации:
$$
\begin{aligned}
\mathbf{v}_1 &= \mathbf{x}_1, \\
\mathbf{v}_m &= \mathbf{x}_m - \sum_{j=1}^{m-1} \frac{(\mathbf{x}_m,\mathbf{v}_j)}{\|\mathbf{v}_j\|^2}\,\mathbf{v}_j, \quad m=2,\ldots,k.
\end{aligned}
$$
Получаем ортогональную систему $\{\mathbf{v}_j\}$ с теми же линейными оболочками: $\operatorname{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_m\}=\operatorname{span}\{\mathbf{x}_1,\ldots,\mathbf{x}_m\}$.

Нормировка (получение ортонормированного базиса):
$$
\mathbf{e}_m = \frac{\mathbf{v}_m}{\|\mathbf{v}_m\|}, \quad m=1,\ldots,k.
$$

## Шаг 1: Исходные векторы

\begin{tikzpicture}[scale=1.5]
% Координатные оси
\draw[->] (-0.5,0) -- (4,0) node[right] {$x_1$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$x_2$};

% Исходные векторы
\draw[thick, blue, ->] (0,0) -- (3,1) node[midway, below] {$\mathbf{x}_1$};

\draw[thick, red, ->] (0,0) -- (2,2.5) node[midway, above left] {$\mathbf{x}_2$};

% Подпись
\node at (1.5,-0.4) {\textbf{Шаг 1:} $\mathbf{v}_1 = \mathbf{x}_1$};
\end{tikzpicture}

## Шаг 2: Вычисление проекции

\begin{tikzpicture}[scale=1.5]
% Координатные оси
\draw[->] (-0.5,0) -- (4,0) node[right] {$x_1$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$x_2$};

% Вектор v_1 (синий)
\draw[thick, blue, ->] (0,0) -- (3,1);
\node[blue] at (3.2,1.2) {$\mathbf{v}_1$};

% Вектор x_2 (красный)
\draw[thick, red, ->] (0,0) -- (2,2.5) node[midway, above left] {$\mathbf{x}_2$};
\node[red] at (2.2,2.8) {$\mathbf{x}_2$};

% Проекция x_2 на v_1 (зеленый)
\draw[thick, green, ->] (0,0) -- (2.55,0.85) node[midway, below] {$\Pr_{\mathbf{v}_1}(\mathbf{x}_2)$};

% Пунктирная линия для показа проекции
\draw[dashed, gray] (2,2.5) -- (2.55,0.85);

% Точка пересечения
\fill[black] (2.55,0.85) circle (1.5pt);

% Подпись формулы проекции
\node at (1.5,-0.4) {$\Pr_{\mathbf{v}_1}(\mathbf{x}_2) = \frac{(\mathbf{x}_2,\mathbf{v}_1)}{\|\mathbf{v}_1\|^2}\mathbf{v}_1$};
\end{tikzpicture}

## Шаг 3: Получение ортогонального вектора

\begin{tikzpicture}[scale=1.5]
% Координатные оси (сдвинуты к центру)
\draw[->] (-1,0) -- (5,0) node[right] {$x_1$};
\draw[->] (0,-1) -- (0,4) node[above] {$x_2$};

% Вектор v_1 (синий)
\draw[thick, blue, ->] (0,0) -- (3,1);
\node[blue] at (3.2,1.2) {$\mathbf{v}_1$};

% Вектор x_2 (красный, пунктирный)
\draw[thick, red, dashed, ->] (0,0) -- (2,2.5) node[midway, above left] {$\mathbf{x}_2$};

% Проекция x_2 на v_1 (зеленый, пунктирный)
\draw[thick, green, dashed, ->] (0,0) -- (2.55,0.85) node[midway, below] {$\Pr_{\mathbf{v}_1}(\mathbf{x}_2)$};

% Показать вычитание: зеленый вектор от конца красного к концу оранжевого
\draw[thick, green, dashed, ->] (2,2.5) -- (-0.55,1.65) node[pos=0.2, left] {$- \Pr_{\mathbf{v}_1}(\mathbf{x}_2)$};

% Результирующий ортогональный вектор v_2 (оранжевый) из начала координат
\draw[thick, orange, ->] (0,0) -- (-0.55,1.65) node[midway, left] {$\mathbf{v}_2$};
\node[orange] at (-0.8,2.4) {$\mathbf{v}_2 = \mathbf{x}_2 - \Pr_{\mathbf{v}_1}(\mathbf{x}_2)$};

% Пунктирная линия для показа ортогональности
\draw[dashed, gray] (2,2.5) -- (2.55,0.85);

% Точка пересечения
\fill[black] (2.55,0.85) circle (1.5pt);

% Подпись результата
\node at (2,-0.4) {\textbf{Результат:} $\mathbf{v}_1 \perp \mathbf{v}_2$, $(\mathbf{v}_1, \mathbf{v}_2) = 0$};
\end{tikzpicture}

## Пример
\vspace{-12.0mm}
Ортогонализовать набор векторов $G = \left\{\vthree{1}{1}{1}, \vthree{0}{1}{2}, \vthree{1}{0}{2} \right\}$ 

## Слайд для записей


## Обращение матриц через СЛУ: Идея


\begin{tikzpicture}[scale=1.2]
% Матрица A
\draw[thick, blue] (0,0) rectangle (3,3);
\node[blue] at (1.5,1.5) {\Large $\mathbf{A}$};
\node at (1.5,-0.3) {\textbf{Матрица A}};

% Знак умножения
\node at (3.5,1.5) {\Large $\times$};

% Матрица B с цветными столбцами
\draw[thick] (3,0) rectangle (6,3);

% Столбец 1 матрицы B
\draw[thick, fill=blue!20] (3,0) rectangle (4,3);
\node[blue!80] at (3.5,1.5) {\Large $\mathbf{b}_1$};

% Столбец 2 матрицы B
\draw[thick, fill=purple!20] (4,0) rectangle (5,3);
\node[purple!80] at (4.5,1.5) {\Large $\mathbf{b}_2$};

% Столбец 3 матрицы B
\draw[thick, fill=teal!20] (5,0) rectangle (6,3);
\node[teal!80] at (5.5,1.5) {\Large $\mathbf{b}_3$};

\node at (4.5,-0.3) {\textbf{Матрица B}};

% Знак равенства
\node at (6.5,1.5) {\Large $=$};

% Результирующая матрица C с цветными столбцами
\draw[thick] (7,0) rectangle (10,3);

% Столбец 1 результата
\draw[thick, fill=blue!20] (7,0) rectangle (8,3);
\node[blue!80] at (7.5,1.5) {\Large $\mathbf{c}_1$};

% Столбец 2 результата
\draw[thick, fill=purple!20] (8,0) rectangle (9,3);
\node[purple!80] at (8.5,1.5) {\Large $\mathbf{c}_2$};

% Столбец 3 результата
\draw[thick, fill=teal!20] (9,0) rectangle (10,3);
\node[teal!80] at (9.5,1.5) {\Large $\mathbf{c}_3$};

\node at (8.5,-0.3) {\textbf{Результат C}};

% Стрелки показывающие соответствие (лестница)
\draw[thick, blue!80, ->] (3.5,3.2) -- (3.5,3.8);
\node[blue!80] at (3.5,4.1) {\textbf{$\mathbf{A}\mathbf{b}_1 = \mathbf{c}_1$}};

\draw[thick, purple!80, ->] (4.5,3.2) -- (4.5,4.0);
\node[purple!80] at (4.5,4.3) {\textbf{$\mathbf{A}\mathbf{b}_2 = \mathbf{c}_2$}};

\draw[thick, teal!80, ->] (5.5,3.2) -- (5.5,4.2);
\node[teal!80] at (5.5,4.5) {\textbf{$\mathbf{A}\mathbf{b}_3 = \mathbf{c}_3$}};
\end{tikzpicture}

## Три системы линейных уравнений

\begin{tikzpicture}[scale=1.2]
% Система 1
\draw[thick, blue] (0,0) rectangle (2,1.5);
\node[blue] at (1,0.75) {\Large $\mathbf{A}\mathbf{x}_1 = \mathbf{e}_1$};
\node at (1,-0.3) {\textbf{Система 1}};

% Система 2
\draw[thick, blue] (2.5,0) rectangle (4.5,1.5);
\node[blue] at (3.5,0.75) {\Large $\mathbf{A}\mathbf{x}_2 = \mathbf{e}_2$};
\node at (3.5,-0.3) {\textbf{Система 2}};

% Система 3
\draw[thick, blue] (5,0) rectangle (7,1.5);
\node[blue] at (6,0.75) {\Large $\mathbf{A}\mathbf{x}_3 = \mathbf{e}_3$};
\node at (6,-0.3) {\textbf{Система 3}};

% Стрелка объединения
\draw[thick, red, ->] (3.5,1.8) -- (3.5,2.2);
\node[red] at (3.5,2.5) {\textbf{Объединяем}};

% Результат
\draw[thick, orange] (1.5,2.8) rectangle (5.5,4.3);
\node[orange] at (3.5,3.55) {\Large $\mathbf{A}[\mathbf{x}_1|\mathbf{x}_2|\mathbf{x}_3] = [\mathbf{e}_1|\mathbf{e}_2|\mathbf{e}_3] = \mathbf{I}$};
\node at (3.5,2.9) {\textbf{Результат}};
\end{tikzpicture}

## Визуализация расширенной матрицы

\begin{tikzpicture}[scale=0.9]
% Расширенная матрица [A|I] с цветными столбцами
\draw[thick] (0,0) rectangle (6,3);

% Матрица A
\draw[thick, blue] (0,0) rectangle (3,3);
\node[blue] at (1.5,1.5) {\Large $\mathbf{A}$};

% Столбцы единичной матрицы I
\draw[thick, fill=red!20] (3,0) rectangle (4,3);
\node[red] at (3.5,1.5) {\Large $\mathbf{e}_1$};

\draw[thick, fill=green!20] (4,0) rectangle (5,3);
\node[green] at (4.5,1.5) {\Large $\mathbf{e}_2$};

\draw[thick, fill=orange!20] (5,0) rectangle (6,3);
\node[orange] at (5.5,1.5) {\Large $\mathbf{e}_3$};

% Подписи
\node at (1.5,-0.3) {\textbf{Матрица A}};
\node[red] at (3.5,-0.3) {\textbf{1}};
\node[green] at (4.5,-0.3) {\textbf{2}};
\node[orange] at (5.5,-0.3) {\textbf{3}};

% Стрелка преобразования
\draw[thick, purple, ->] (6.2,1.5) -- (7.8,1.5);
\node[purple] at (7,1.8) {\textbf{Гаусс}};

% Результирующая матрица [I|A⁻¹]
\draw[thick] (8,0) rectangle (14,3);

% Столбцы единичной матрицы I
\draw[thick, fill=red!20] (8,0) rectangle (9,3);
\node[red] at (8.5,1.5) {\Large $\mathbf{e}_1$};

\draw[thick, fill=green!20] (9,0) rectangle (10,3);
\node[green] at (9.5,1.5) {\Large $\mathbf{e}_2$};

\draw[thick, fill=orange!20] (10,0) rectangle (11,3);
\node[orange] at (10.5,1.5) {\Large $\mathbf{e}_3$};

% Столбцы обратной матрицы A⁻¹
\draw[thick, fill=red!20] (11,0) rectangle (12,3);
\node[red] at (11.5,1.5) {\Large $\mathbf{x}_1$};

\draw[thick, fill=green!20] (12,0) rectangle (13,3);
\node[green] at (12.5,1.5) {\Large $\mathbf{x}_2$};

\draw[thick, fill=orange!20] (13,0) rectangle (14,3);
\node[orange] at (13.5,1.5) {\Large $\mathbf{x}_3$};

% Подписи результата
\node[red] at (8.5,-0.3) {\textbf{1}};
\node[green] at (9.5,-0.3) {\textbf{2}};
\node[orange] at (10.5,-0.3) {\textbf{3}};
\end{tikzpicture}

$$
\textcolor{blue}{\mathbf{A}}[\textcolor{red}{\mathbf{x}_1}|\textcolor{green}{\mathbf{x}_2}|\textcolor{orange}{\mathbf{x}_3}] = [\textcolor{red}{\mathbf{e}_1}|\textcolor{green}{\mathbf{e}_2}|\textcolor{orange}{\mathbf{e}_3}] = \textcolor{green}{\mathbf{I}}
$$

$$
\Rightarrow \quad [\textcolor{red}{\mathbf{x}_1}|\textcolor{green}{\mathbf{x}_2}|\textcolor{orange}{\mathbf{x}_3}] = \textcolor{orange}{\mathbf{A}^{-1}}
$$


## Пример: Обращение матрицы 3x3

$$
\mathbf{A} = \begin{pmatrix}
2 & 0 & 0 \\
1 & 3 & 0 \\
0 & 1 & 2
\end{pmatrix}, \quad
\left[\begin{array}{ccc|ccc}
2 & 0 & 0 & 1 & 0 & 0 \\
1 & 3 & 0 & 0 & 1 & 0 \\
0 & 1 & 2 & 0 & 0 & 1
\end{array}\right]
$$

## Слайд для записей
