---
title: "Линейная алгебра"
subtitle: "Системы линейных уравнений"
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

## Система линейных уравнений

- Привычный вид:
\begin{equation*}
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
\end{equation*}

## Другие формы СЛУ
- Матричная форма
\begin{equation*}
A = 
\begin{pmatrix}
a_{11} & \dots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \dots & a_{mn}
\end{pmatrix},
\quad
x = 
\begin{pmatrix}
x_1 \\ \vdots \\ x_n
\end{pmatrix},
\quad
b = 
\begin{pmatrix}
b_1 \\ \vdots \\ b_m
\end{pmatrix}
\end{equation*}

\begin{equation*}
A x = b, \text{ на сленге $b$ - right-hand side, правая часть системы.}
\end{equation*}


- Векторная форма. Эта форма даёт нам новый взгляд на СЛУ. С этой точки зрения решение - это набор констант, с которыми нужно взять столбцы матрицы, чтобы получить вектор правой части.
\begin{equation*}
x_1 a_1 + x_2 a_2 + \dots + x_n a_n = b,
\end{equation*}
где $a_i$ — $i$-й столбец матрицы $A$

- Расширенная форма. Используется при решении с использованием элементарных преобразований матрицы.
\begin{equation*}
\left(
\begin{array}{ccc|c}
a_{11} & \dots & a_{1n} & b_1 \\
\vdots &        & \vdots & \vdots \\
a_{m1} & \dots & a_{mn} & b_m
\end{array}
\right)
\end{equation*}

## Элементарные преобразования строк

Существует три типа элементарных преобразований строк:

\begin{enumerate}
\item \textbf{Перестановка строк}: поменять местами две строки матрицы
\item \textbf{Умножение на скаляр}: умножить строку на ненулевой скаляр $a$
\item \textbf{Замена строки}: заменить строку $k$ её суммой с константным множителем строки $j$; все остальные строки остаются неизменными
\end{enumerate}

## Метод Гаусса (приведение к ступенчатому виду)

\begin{enumerate}
\item Найти самый левый ненулевой столбец матрицы
\item Убедиться, применяя преобразования типа 1 (перестановка строк), если необходимо, что первый (верхний) элемент этого столбца ненулевой. Этот элемент называется ведущим элементом
\item Занулить все ненулевые элементы под ведущим, добавляя (вычитая) подходящее кратное первой строки к строкам номер $2, 3, \ldots, m$
\end{enumerate}

## Ступенчатый вид

\begin{enumerate}
\item Все нулевые строки (т.е. строки со всеми элементами равными 0), если они есть, помещаются ниже всех ненулевых строк

Назовём ведущим элементом строки её самый левый ненулевой элемент. Тогда второе свойство ступенчатого вида можно сформулировать следующим образом:

\item Для любой ненулевой строки её ведущий элемент строго правее ведущего элемента в предыдущей строке.
\end{enumerate}

**Примеры:**

\begin{equation*}
\left(\begin{array}{c c c c|c}\boxed{1} & 2 & 0 & 0 & 1 \\ 0 & 0 & \boxed{2} & 2 & 9 \\ 0 & 0 & 0 & \boxed{1} & 3 \\ 0 & 0 & 0 & 0 & 0\end{array}\right), \quad
\left(\begin{array}{c c c c c|c}\boxed{1} & 2 & 0 & 0 & 0 & 1 \\ 0 & 0 & \boxed{1} & 5 & 0 & 2 \\ 0 & 0 & 0 & 0 & \boxed{1} & 3\end{array}\right), \quad
\left(\begin{array}{c c c|c}\boxed{1} & 2 & 3 & 1 \\ 0 & \boxed{2} & 2 & 2 \\ 0 & 0 & \boxed{2} & 6\end{array}\right)
\end{equation*}

Для каждой строки обведен её ведущий элемент. Ведущий элемент каждой строки смещен строго вправо относительно ведущего элемента предыдущей строки.

## Ступенчатый вид

$\left(\begin{array}{c c c c c|c}\boxed{1} & 2 & 0 & 0 & 0 & 1 \\ 0 & 0 & \boxed{1} & 5 & 0 & 2 \\ 0 & 0 & 0 & 0 & \boxed{1} & 3\end{array}\right)$

Некоторые столбцы могут НЕ поймать ведущих элементов. Как, например, в приведенной расширенной матрице системы. Переменные, соответствующие этим столбцам, — **свободные переменные**. В данном случае свободные переменные: $x_2$, $x_4$.
 
- Решение системы

\begin{align*}
1 \cdot x_5 &= 3 \quad \Rightarrow \quad x_5 = 3 \\
1 \cdot x_3 + 5x_4 &= 2 \quad \Rightarrow \quad x_3 = 2 - 5x_4 \\
x_1 + 2x_2 &= 1 \quad \Rightarrow \quad x_1 = 1 - 2x_2
\end{align*}

## Общее решение

- Финально, общее решение СЛУ
\begin{equation*}
x = 
    \begin{cases}
    x_1 = 1 - 2x_2 \\
    x_2 = \text{free} \\
    x_3 = 2 - 5x_4 \\
    x_4 = \text{free} \\
    x_5 = 3
    \end{cases}
    ,\quad x_2, x_4 \in \mathbb{R}
\end{equation*}

- Векторная форма общего решения
\begin{equation*}
X = \begin{pmatrix}1 \\ 0 \\ 2 \\ 0 \\ 3\end{pmatrix} + x_2 \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + x_4 \begin{pmatrix} 0 \\ 0 \\ -5 \\ 1 \\ 0 \end{pmatrix}, \quad x_2, x_4 \in \mathbb{R}
\end{equation*}

## Слайд для записи

## Примеры
