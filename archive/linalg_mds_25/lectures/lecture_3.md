---
title: "Линейная алгебра"
subtitle: "Базис векторного пространства."
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
## Базис
### Определение

- Набор векторов $v_1, \ldots, v_n$ из $\mathbb{V}$ называется _базисом_ пространства $\mathbb{V}$ тогда и только тогда, когда _любой_ вектор $x \in \mathbb{V}$ может быть уникально представлен в форме линейной комбинации:
$$
    x = \alpha_1 v_1 + \ldots + \alpha_n v_n.
$$

- Соответствующие уникальные коэффициенты $\alpha_1, \ldots, \alpha_n$ мы называем _координатами_ вектора $x$ в базисе $(v_1, \ldots, v_n)$.

- Немного иначе: набор векторов $v_1, \ldots, v_n$ из $\mathbb{V}$ называется _базисом_ пространства $\mathbb{V}$ тогда и только тогда, когда этот набор векторов линейно независим и $\text{span} (v_1, \ldots, v_n) = \mathbb{V}$, то есть мы можем 'дотянуться' до любого элемента из $\mathbb{V}$.

## Базис. Примеры

### Пример в координатном векторном пространстве

- Координатное пространство $\mathbb{R}^2$. Возьмем вектор, например, $x = \vtwo{5}{2}$:

\begin{align*}
\vtwo{5}{2} & = \textcolor{violet}{5} \vtwo{1}{0} + \textcolor{violet}{2} \vtwo{0}{1}, \quad [x]_S = \vtwo{\textcolor{violet}{5}}{\textcolor{violet}{2}}, \quad S = \left(\vtwo{1}{0}, \, \vtwo{0}{1} \right) \\
\vtwo{5}{2} & = \textcolor{violet}{0.5} \vtwo{2}{4} + \textcolor{violet}{-0.5} \vtwo{-8}{0}, \quad [x]_B = \vtwo{\textcolor{violet}{0.5}}{\textcolor{violet}{-0.5}}, \quad B = \left(\vtwo{2}{4}, \, \vtwo{-8}{0} \right) \\
\vtwo{5}{2} & = \textcolor{violet}{-0.25} \vtwo{-8}{2} + \textcolor{violet}{-5.5} \vtwo{0}{-1}, \quad [x]_C = \vtwo{\textcolor{violet}{-0.25}}{\textcolor{violet}{-5.5}}, \quad C = \left(\vtwo{-8}{2}, \, \vtwo{0}{-1} \right) \\
\end{align*}

## Базис. Примеры
### Пример в векторном пространстве полиномов

- Векторное пространство $\mathbb{R}[x,2]$. Возьмем вектор, например, $f(x) = 2x^2 - 7x + 4$ и посмотрим его представление в разных базисах:

\begin{align*}
f(x) & = \textcolor{violet}{2} \cdot x^2 + \textcolor{violet}{-7} \cdot x + \textcolor{violet}{4} \cdot 1, \quad [x]_S = \vthree{\textcolor{violet}{2}}{\textcolor{violet}{-7}}{\textcolor{violet}{4}}, \quad S = \left(x^2, \, x , \, 1 \right) \\
f(x) & = \textcolor{violet}{0.5} \cdot (4x^2 - 2x) + \textcolor{violet}{-2} \cdot (3x) + \textcolor{violet}{0.5} \cdot 8, \quad [x]_B = \vthree{\textcolor{violet}{0.5}}{\textcolor{violet}{-2}}{\textcolor{violet}{0.5}}, \quad B = \left(4x^2 - 2x, \, 3x , \, 8 \right)
\end{align*}

## Важный промежуточный вывод

::: {.columns}

::: {.column width="50%"}

\begin{tikzpicture}[scale=1.0]
% Центральный вектор
\node[draw, rectangle, minimum width=1.5cm, minimum height=2cm, fill=blue!20] (vector) at (0,0) {
\begin{minipage}{1.2cm}
\centering
$\begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{pmatrix}$
\end{minipage}
};

% Векторные пространства - круги
\node[draw, circle, minimum size=2cm, fill=red!20] (polynomials) at (-3, 2) {
\begin{minipage}{1.8cm}
\centering
\textbf{Полиномы}\\
$p(x) = a_0 + a_1x + \ldots + a_{n-1}x^{n-1}$
\end{minipage}
};

\node[draw, circle, minimum size=2cm, fill=green!20] (matrices) at (3, 2) {
\begin{minipage}{1.8cm}
\centering
\textbf{Матрицы}\\
$A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}$
\end{minipage}
};

\node[draw, circle, minimum size=2cm, fill=yellow!20] (functions) at (0, 3.5) {
\begin{minipage}{1.8cm}
\centering
\textbf{Функции}\\
$f: \mathbb{R} \to \mathbb{R}$
\end{minipage}
};

% Стрелки от пространств к вектору
\draw[thick, ->] (polynomials) -- (vector);
\draw[thick, ->] (matrices) -- (vector);
\draw[thick, ->] (functions) -- (vector);

% Подпись
\node[below] at (0, -1.) {\textbf{Линейная алгебра: единый язык для разных объектов}};

\end{tikzpicture}

:::

::: {.column width="50%"}

\begin{itemize}
    \item Если векторное пространство $\mathbb{V}$ имеет базис $\mathbf{v}_1, \ldots, \mathbf{v}_n$, то любой вектор $\mathbf{v}$ однозначно определяется своими координатами $\alpha_k$ в этом базисе. Если мы упакуем $\alpha_k$ в вектор из $\mathbb{R}^n$, то можем оперировать им вместо оперирования над $\mathbf{v}$.

    \item Если $\mathbf{v}=\sum_{k=1}^n \alpha_k \mathbf{v}_k$ и $\mathbf{w}=\sum_{k=1}^n \beta_k \mathbf{v}_k$, то
$$
\mathbf{v}+\mathbf{w}=\sum_{k=1}^n \alpha_k \mathbf{v}_k+\sum_{k=1}^n \beta_k \mathbf{v}_k=\sum_{k=1}^n\left(\alpha_k+\beta_k\right) \mathbf{v}_k
$$
т.е. вместо сложения двух оригинальных векторов, можно сложить векторы координат. 

\item Аналогично, чтобы получить $\alpha \mathbf{v}$, можно умножить столбец координат $\mathbf{v}$ на $\alpha$ и сразу получить координаты вектора $\alpha \mathbf{v}$.
\end{itemize}

:::

:::




