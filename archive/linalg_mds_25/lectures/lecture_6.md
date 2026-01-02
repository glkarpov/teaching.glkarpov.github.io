---
title: "Линейная алгебра"
subtitle: "Построение матрицы линейного отображения."
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
## Слайд для записи

## Обратные элементы 

## Обратная матрица

::: {.callout-definition}
## Обратная матрица
Для квадратной матрицы $A$ размера $n \times n$ **обратной матрицей** называется матрица $A^{-1}$ такая, что:

$$A \cdot A^{-1} = A^{-1} \cdot A = I_n$$

где $I_n$ — единичная матрица размера $n \times n$.
:::

Обратная матрица существует **только** для невырожденных (обратимых) матриц. Матрица $A$ невырождена тогда и только тогда, когда:

\begin{itemize}
\item $\det(A) \neq 0$
\item Столбцы матрицы $A$ линейно независимы
\item Строки матрицы $A$ линейно независимы
\item Система $Ax = 0$ имеет только тривиальное решение $x = 0$
\item Для любого вектора $b$ система $Ax = b$ имеет единственное решение
\end{itemize}

Если иначе, то матрица $A$ называется **вырожденной** или **сингулярной** и обратной не имеет.


## Формула для матрицы 2x2

### Общая формула
Для матрицы $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:

$$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

где $\det(A) = ad - bc$

## Примеры
