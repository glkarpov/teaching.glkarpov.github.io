---
title: "Линейная алгебра"
subtitle: "Векторное пространство. Линейная комбинация и оболочка. Зависимость и независимость векторов."
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

## Векторное пространство (Vector space)
### Основной предмет изучения линейной алгебры

\begin{itemize}
\item Рассмотрим некоторое множество элементов $V$. Помимо того, что в нем просто живут абстрактные элементы, зададим там бинарные операции.

\item Сложение. Любым двум элементам из множества $V$ ставится в соответствие третий:
$$
    \forall x, \, y \in \mathbb{V}: \quad x \oplus y = w, \, w \in \mathbb{V}. 
$$

\item Умножение на скаляр. Любой паре элементов из $\mathbb{V}$ и $\mathbb{R}$ ставится в соответствие элемент из $V$:
$$
    \forall x \in \mathbb{V}, \, \forall \alpha \in \mathbb{R}: \quad \alpha \otimes x = w, \, w \in \mathbb{V}. 
$$
\end{itemize}

## Векторное пространство
### Примеры векторных пространств

Coordinate space. Множество последовательностей длины $n$, частным случаем которых являются геометрические векторы.
$$
    a = \begin{pmatrix}
        a_{1}\\
        a_{2}\\
        \vdots\\
        a_{n}
    \end{pmatrix}
$$

## Векторное пространство
### Примеры векторных пространств

- Множество матриц $n \times m$.
$$
    A = \begin{pmatrix}
        5 & 2\\
        -2 & 7
    \end{pmatrix}, \; 
    B = \begin{pmatrix}
        1 & 4\\
        3 & 0
    \end{pmatrix}
$$

- Множество полиномов (Что? Да!) фиксированной максимальной степени.
\begin{gather*}
    f(x) = a_1 x^2 + b_1 x + c_1, \; g(x) = a_2 x^2 + b_2 x + c_2 \\
    f(x)+g(x) = (a_1 + a_2) x^2 + (b_1 + b_2)x + (c_1 + c_2) \\
    \alpha \in \mathbb{R}: \, \alpha f(x) = (\alpha a_1) x^2 + (\alpha b_1) x + (\alpha c_1)
\end{gather*}

## Линейная комбинация

\begin{itemize}
\item С помощью определенных выше операций мы можем комбинировать элементы векторного пространства.

\item Предположим, мы вытащили набор векторов $v_1, \ldots, v_m$ из $\mathbb{V}$, и набор скаляров $\alpha_1, \ldots, \alpha_m$ из $\mathbb{R}$.

\item \textit{Линейная комбинация} группы векторов - новый вектор, построенный в виде:
$$
    x = \alpha_1 v_1 + \ldots + \alpha_m v_m, \, x \in \mathbb{V}.
$$

\item Из-за замкнутости $\mathbb{V}$ относительно двух введенных операций получившийся элемент $x$ тоже содержится в векторном пространстве $\mathbb{V}$.
\end{itemize}

## Примеры линейных комбинаций

::: {.columns}

::: {.column width="50%"}

Пример: $\mathbb{V} = \mathbb{R}^{2 \times 2}$

\begin{equation*}
\textcolor{red}{A} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix},
\textcolor{blue}{B} = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\end{equation*}

**Линейная комбинация:**
$$
    2\textcolor{red}{A} + 3\textcolor{blue}{B} = 2\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} + 3\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} = \begin{pmatrix}2 & 3 \\ 3 & 2\end{pmatrix}
$$

:::

::: {.column width="50%"}

Пример: $\mathbb{V} = \mathbb{R}[x, 2]$

\begin{equation*}
    \textcolor{red}{p_1}(x) = 1.5x^2 - x, \quad \textcolor{blue}{p_2}(x) = x+1, \quad \textcolor{green}{p_3}(x) = 2
\end{equation*}

**Линейная комбинация:**
\begin{gather*}
    2\textcolor{red}{p_1} + (-2)\textcolor{blue}{p_2} + 5\textcolor{green}{p_3} = \\
    2 (1.5x^2 - x) - 2(x+1) + 5(2) = \\
    3x^2 - 4x + 8
\end{gather*}

:::

:::

## Линейная оболочка

Множество всех-всех возможных линейных комбинаций, полученных из зафиксированного набора векторов $v_1, \ldots, v_m$, назовем _линейной оболочкой_ этого набора и обозначим:
$$
    \text{span} (v_1, \ldots, v_m) = \{ \alpha_1 v_1 + \ldots + \alpha_m v_m : a_1, \ldots, \alpha_m \in \mathbb{R} \}. 
$$

::: {.columns}

::: {.column width="50%"}
\begin{gather*}
\textcolor{red}{a} = \begin{pmatrix}
2 \\
0
\end{pmatrix},
\textcolor{blue}{b} = \begin{pmatrix}
0 \\
1
\end{pmatrix} \\
\text{span}  (\textcolor{red}{a}, \textcolor{blue}{b}) =  \{\alpha_1 \textcolor{red}{a} + \alpha_2 \textcolor{blue}{b} : \forall \alpha_1, \alpha_2 \in \mathbb{R}  \} = \mathbb{R}^2
\end{gather*}
\begin{tikzpicture}[scale=0.8]
% Координатные оси
\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-3) -- (0,3) node[above] {$y$};

% Сетка
\draw[gray, very thin] (-3,-3) grid (3,3);

% Вектор (2,0) - красный
\draw[thick, red, ->] (0,0) -- (2,0) node[midway, below] {$(2,0)$};

% Вектор (0,1) - синий  
\draw[thick, blue, ->] (0,0) -- (0,1) node[midway, left] {$(0,1)$};
\end{tikzpicture}

:::

::: {.column width="50%"}
\begin{gather*}
\textcolor{red}{c} = \begin{pmatrix}
1 \\
1
\end{pmatrix},
\textcolor{blue}{d} = \begin{pmatrix}
4 \\
4
\end{pmatrix} \\
\text{span}  (\textcolor{red}{c}, \textcolor{blue}{d}) =  \{\alpha_1 \textcolor{red}{c} + \alpha_2 \textcolor{blue}{d} : \forall \alpha_1, \alpha_2 \in \mathbb{R}  \} = \text{линия}
\end{gather*}
\begin{tikzpicture}[scale=0.8]
% Координатные оси
\draw[->] (-3,0) -- (3,0) node[right] {$x$};
\draw[->] (0,-3) -- (0,3) node[above] {$y$};

% Сетка
\draw[gray, very thin] (-3,-3) grid (3,3);

% Вектор (1,1) - красный
\draw[thick, red, ->] (0,0) -- (1,1) node[midway, above left] {$(1,1)$};

% Вектор (4,4) - синий
\draw[thick, blue, ->] (0,0) -- (2,2) node[midway, above] {$(4,4)$};

% Линия span - толстая серая линия
\draw[thick, gray, dashed] (-2.5,-2.5) -- (2.5,2.5);
\end{tikzpicture}
:::
:::


## Зависимость и независимость векторов
### Мотивация

- Рассмотрим набор векторов $\{v_1, \ldots, v_m\}$, заранее извлеченных из $\mathbb{V}$, и произвольный набор скаляров $\alpha_1, \ldots, \alpha_m$ из $\mathbb{R}$. В результате построения линейной комбинации получим некий элемент $x \in \mathbb{V}$:
$$
    x = \alpha_1 v_1 + \ldots + \alpha_m v_m
$$

- Уникален ли такой набор $\{\alpha_1, \ldots, \alpha_n\}$ или, может, существует другой
набор $\{\tilde{\alpha}_1, \ldots, \tilde{\alpha}_n\}$ такой, что:
$$
    x = \tilde{\alpha}_1 v_1 + \ldots + \tilde{\alpha}_m v_m.
$$

## Зависимость и независимость векторов
### Мотивация

- Давайте предположим, что набор не уникален, и вычтем два равенства друг из друга:
\begin{multline*}
    (x - x) = \mathbf{0} = (\alpha_1 - \tilde{\alpha}_1) v_1 + (\alpha_2 - \tilde{\alpha}_2) v_2 + \ldots + (\alpha_m - \tilde{\alpha}_m) v_m \\
    = \gamma_1 v_1 + \gamma_2 v_2  + \ldots + \gamma_m v_m
\end{multline*}

- Задача уникальности представления $x$ теперь изменилась к задаче "как получить элемент 0" в результате линейной комбинации.

- Если единственный возможный вариант получить $\mathbf{0}$ это положить все $\gamma_i = 0$:
$$
   \forall i: \, (\alpha_i - \tilde{\alpha}_i) = 0 \rightarrow \alpha_i = \tilde{\alpha}_i.
$$
Что будет означать, что представление $x$ уникально.

- Если есть какой-то другой способ получить $\mathbf{0}$, т.е. хотя бы один $\gamma_k \neq 0$, значит
$(\alpha_k - \tilde{\alpha}_k) \neq 0 \rightarrow \alpha_k \neq \tilde{\alpha}_k$. Что означает, что представление $x$ не уникально - существует другой набор коэффициентов.

## Линейная независимость
### Определение
Мы назовем набор векторов \textit{линейно независимым}, если единственная возможность получить элемент $\mathbf{0}$ как результат линейной комбинации:

$$
    \gamma_1 v_1 + \ldots + \gamma_m v_m = \mathbf{0},
$$

это положить все скаляры равными $0$, $\gamma_1 = \ldots = \gamma_m = 0$. (Также называется \textit{тривиальной комбинацией}).

## Линейная зависимость
### Определение
С другой стороны, мы назовем набор векторов \textit{линейно зависимым}, если **существует** нетривиальная комбинация коэффициентов $\gamma_1, \ldots, \gamma_m$, (не равные $0$ одновременно), такая что:

$$
    \gamma_1 v_1 + \ldots + \gamma_m v_m = \mathbf{0}.
$$
