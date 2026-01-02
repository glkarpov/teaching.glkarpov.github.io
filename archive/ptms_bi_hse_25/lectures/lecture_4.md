---
title: "Теория вероятностей и математическая статистика"
subtitle: "Дискретные случайные величины и их свойства."
institute: "ВШБ Бизнес-информатика"
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

## Функции от случайных величин

- Случайная величина, будучи неизвестным, но все-таки числом, может быть аргументом для какой-либо другой функции,
- Например, если $X$ - это количество проданных тортов, то $Y = cX$ - это доход, где $c$ - цена. Далее, $T = Y - aX - b = kX - b$ может быть чистой прибылью, доход за вычетом издержек на производство. Все это - случайные величины!

- \begin{tikzpicture}
    \draw[thick, fill=blue!10] (0,0) circle (1.0);
    \node at (0,0) {$\Omega_X$};

    \draw[thick, fill=green!10] (4,0) circle (1.0);
    \node at (4,0) {$\Omega_Y$};

    \draw[thick, fill=red!10] (8,0) circle (1.0);
    \node at (8,0) {$\Omega_T$};
  
    \draw[thick, ->] (1.1,0.4) .. controls (2, 0.7) and (2,0.7) .. (2.9,0.4) node[midway, above] {$Y = f(X)$};

    \draw[thick, ->] (5.1,0.4) .. controls (6, 0.7) and (6,0.7) .. (6.9,0.4) node[midway, above] {$T = g(Y)$};
\end{tikzpicture}

## Функции от случайных величин
### Пример

Пусть распределение случайной величины задано таблицей

\begin{center}
    \begin{tabular}{c | c c c c c c} 
        \hline
        $x$ & 0 & -1 & -2 & 1 & 2 & 3\\ [0.5ex] 
        \hline
        $p_X(x)$ & $0.1$ & $0.1$ & $0.1$ & $0.2$ & $0.2$ & $0.3$ \\ 
        \hline
    \end{tabular}
\end{center}

Постройте распределение случайной величины $Y = X^2 + 10$.

Наша задача: восстановить новое пространство элементарных исходов $\Omega_Y$ для величины $Y$ и выразить новую функцию вероятности $P_Y(y)$ через старую известную $P_X(x)$.

- $P_Y(Y=10) = P_X(\{X=0\}) = 0.1$
- $P_Y(Y=11) = P_X(\{X=1\} \cup \{X=-1\}) = P_X(\{X=1\}) + P_X(\{X=-1\}) = 0.3$

- $P_Y(Y=14) = P_X(\{X=2\} \cup \{X=-2\}) = P_X(\{X=2\}) + P_X(\{X=-2\}) = 0.3$

- $P_Y(Y=19) = P_X(\{X=3\}) = 0.3$

- \begin{tabular}{c | c c c c} 
         \hline
         $y$ & 10 & 11 & 14 & 19\\ [0.5ex] 
         \hline
         $p_Y(y)$ & $0.1$ & $0.3$ & $0.3$ & $0.3$ \\ 
         \hline
   \end{tabular}

## Функции от случайных величин

- Если $Y=g(X)$, то $Y$ это новая случайная величина, со своими характеристиками, со своими возможными значениями $\Omega_Y$, и со своей функцией вероятности $P_Y(y)$.

- :::{.callout-tip title="Построение новой функции вероятности"}
Если $Y=g(X)$, функцию вероятности для $Y$ можно выразить через функцию вероятности для $X$:
$$
p_Y(y) = P(Y=y) = P(g(X) = y) = P(\{ X \in g^{-1}(y) \}) = \sum \limits_{x \in g^{-1}(y)} P(X = x)
$$

- Можно расширить предыдыщую картинку и в каком-то смысле говорить, что функция от случайной величины порождает абсолютно новый случайный эксперимент с новым вероятностным пространством (тройкой Колмогорова):
\begin{tikzpicture}
    \draw[thick, fill=blue!10] (0,0) circle (1.0);
    \node at (0,0) {$\Omega_X, \mathcal{F}_X, P_X$};

    \draw[thick, fill=green!10] (4,0) circle (1.0);
    \node at (4,0) {$\Omega_Y, \mathcal{F}_Y, P_Y$};

    \draw[thick, fill=red!10] (8,0) circle (1.0);
    \node at (8,0) {$\Omega_T, \mathcal{F}_T, P_T$};
  
    \draw[thick, ->] (1.1,0.4) .. controls (2, 0.7) and (2,0.7) .. (2.9,0.4) node[midway, above] {$Y = f(X)$};

    \draw[thick, ->] (5.1,0.4) .. controls (6, 0.7) and (6,0.7) .. (6.9,0.4) node[midway, above] {$T = g(Y)$};
\end{tikzpicture}

## Физическое \cancel{Лирическое} отступление

-
\begin{tikzpicture}[scale=1.4]
    % Ось X
    \draw[thick, ->] (-0.5, -0.5) -- (3, -0.5) node[right] {$X$};
    
    % Деления на оси
    \foreach \x in {0, 1, 2} {
        \draw (\x, -0.4) -- (\x, -0.6) node[below] {\x};
    }
    
    % Стержень
    \draw[very thick, gray] (0, 0) -- (2, 0);
    
    % Левая масса в координате 0
    \draw[thick, fill=blue!20] (0, 0) circle (0.3);
    \node at (0, 0) {0.5 кг};
    
    % Правая масса в coordinate 2
    \draw[thick, fill=blue!20] (2, 0) circle (0.3);
    \node at (2, 0) {0.5 кг};
\end{tikzpicture}

-
\begin{tikzpicture}[scale=1.4]
    % Ось X
    \draw[thick, ->] (-0.5, -0.5) -- (3, -0.5) node[right] {$X$};
    
    % Деления на оси
    \foreach \x in {0, 1, 2} {
        \draw (\x, -0.4) -- (\x, -0.6) node[below] {\x};
    }
    
    % Стержень
    \draw[very thick, gray] (0, 0) -- (2, 0);
    
    % Левая масса в координате 0
    \draw[thick, fill=blue!20] (0, 0) circle (0.25);
    \node at (0, 0.35) {0.4 кг};
    
    % Правая масса в coordinate 2
    \draw[thick, fill=blue!20] (2, 0) circle (0.35);
    \node at (2, 0) {0.6 кг};
\end{tikzpicture}

## Физическое \cancel{Лирическое} отступление

\begin{tikzpicture}[scale=1.4]
\draw[thick, ->] (-0.5, -0.5) -- (3, -0.5) node[right] {$X$};

\foreach \x in {0, 1, 2} {
    \draw (\x, -0.4) -- (\x, -0.6) node[below] {\x};
}

\draw[very thick, gray] (0, 0) -- (2, 0);

\draw[thick, fill=blue!20] (0, 0) circle (0.25);
\node at (0, 0.35) {0.4 кг};

\draw[thick, fill=blue!20] (2, 0) circle (0.35);
\node at (2, 0) {0.6 кг};

\draw[thick, fill=red!30] (1.2, -0.1) -- (1.1, -0.3) -- (1.3, -0.3) -- cycle;
\node[below] at (1.2, -0.5) {ЦТ};
\end{tikzpicture}

- $x_{gc} = \sum\limits_{i} x_i m_i$, при $\sum\limits_{i} m_i = 1$.

- В данном примере $x_{gc} = 0 \cdot 0.4 + 2 \cdot 0.6 = 1.2$ 

- Предположим С.В., которую мы реализуем $10^5$ раз с $P_X(0) = 0.4$, $P_X(2) = 0.6$. Посчитаем среднее суммы за все испытания:
$$
    avg = \frac{\approx 60000 \cdot 2 + \approx 40000 \cdot 0}{10^5} \approx 1.2
$$

## Характеристики С.В.: Математическое ожидание

- Математическое ожидание - это число, **константа**, которое помогает нам понять тренд значений, куда в среднем стремятся значения случайной величины на большой дистанции.
- Можно рассматривать это как средний результат множества реализаций данного случайного эксперимента.
- Ожидаемое значение может не входить в набор возможных значений $\Omega_X$.

- :::{.callout-definition}
Если $X$ - дискретная случайная величина, то ожидание $X$ обозначается как $E[X]$ и определяется как:
$$
    E[X] = \sum \limits_{x \in \Omega_X} x P(X = x) = \sum \limits_{x \in \Omega_X} x P_X(x).
$$
:::



## Характеристики С.В.: Математическое ожидание

::: {.columns}

::: {.column width="50%"}
**В физическом мире**:

\begin{tikzpicture}[scale=1.4]
\draw[thick, ->] (-0.5, -0.5) -- (4, -0.5) node[right] {$X$};

\foreach \x in {0, 1, 2, 3} {
    \draw (\x, -0.4) -- (\x, -0.6) node[below] {\x};
}

\draw[very thick, gray] (0, 0) -- (3, 0);

\draw[thick, fill=blue!20] (0, 0) circle (0.2);
\node at (0, 0.35) {0.2 кг};

\draw[thick, fill=blue!20] (1, 0) circle (0.3);
\node at (1, 0.45) {0.5 кг};

\draw[thick, fill=blue!20] (3, 0) circle (0.25);
\node at (3, 0.4) {0.3 кг};

\draw[thick, fill=red!30] (1.4, -0.1) -- (1.3, -0.3) -- (1.5, -0.3) -- cycle;
\node[below] at (1.4, -0.5) {ЦТ};
\end{tikzpicture}

- $x_{gc} = \sum x_i m_i = 0 \cdot 0.2 + 1 \cdot 0.5 + 3 \cdot 0.3 = 1.4$
:::

::: {.column width="50%"}
**В вероятностном мире**:
\begin{tabular}{c | c c c} 
        \hline
        $x$ & 0 & 1 & 3\\ [0.5ex] 
        \hline
        $p_X(x)$ & $0.2$ & $0.5$ & $0.3$ \\ 
        \hline
\end{tabular}

\vspace{4.2em}
- $E[X] = \sum x_i \cdot P_X(X=x_i) = 0 \cdot 0.2 + 1 \cdot 0.5 + 3 \cdot 0.3 = 1.4$
:::
:::

::: {.callout-tip title="Fun facts"}
В международной литературе функция вероятности дискретной случайной величины $P_X(x)$ называется Probability **Mass** Function, своим названием явно подчеркивая аналогию, что вероятность может выступать в роли "массы" элементарного исхода. Тогда математическое ожидание можно интерпретировать как взвешенную сумму всех исходов, где в качестве веса используется вероятность.
:::



## Свойства математического ожидания

\begin{enumerate}
\item \textbf{Линейность}: Для любых констант $a$ и $b$:
   $$E[aX + b] = aE[X] + b$$

\item \textbf{Константа}: Если $c$ - константа, то:
   $$E[c] = c$$

\item \textbf{Ожидание функции}: Для функции $Y = g(X)$:
   $$E[g(X)] = \sum_{x \in \Omega_X} g(x) P(X = x)$$

   \textbf{Доказательство}:
   \begin{gather*}
    E(Y) =\sum_{y \in \Omega_Y} y \, \textcolor{magenta}{P(Y=y)} =  \\
    =\sum_{y \in \Omega_Y} y \left( \textcolor{magenta}{\sum_{x \in g^{-1}(y)} P(X=x)} \right) = \sum_{x \in \Omega_X} g(x)P(X=x)
   \end{gather*}

\end{enumerate}

## Математическое ожидание: пример

Посмотрим на примеры вычисления математического ожидания на основе уже посчитанной задачи:

::: {.columns}
::: {.column width="50%"}

\begin{tabular}{c | c c c c c c} 
        \hline
        $x$ & 0 & -1 & -2 & 1 & 2 & 3\\ [0.5ex] 
        \hline
        $p_X(x)$ & $0.1$ & $0.1$ & $0.1$ & $0.2$ & $0.2$ & $0.3$ \\ 
        \hline
\end{tabular}

:::
::: {.column width="50%"}
\begin{tabular}{c | c c c c} 
         \hline
         $y$ & 10 & 11 & 14 & 19\\ [0.5ex] 
         \hline
         $p_Y(y)$ & $0.1$ & $0.3$ & $0.3$ & $0.3$ \\ 
         \hline
\end{tabular}
:::
:::

\begin{itemize}

\item $E[X] = \sum \limits_{i=1}^{6} x_i P_X(X = x_i) = -0.1 - 0.2 + 0.2 + 0.4 + 0.9 = 1.2$

\item Первый подход к вычислению $E[Y]$ - по определению, зная таблицу функции вероятности для $Y$:
    \begin{gather*}
        E[Y] = \sum \limits_{i=1}^{4} y_i P_Y(Y = y_i) = 10 \cdot 0.1 + 11 \cdot 0.3 + 14 \cdot 0.3 + 19 \cdot 0.3 = 14.2
    \end{gather*}

\item Второй подход к вычислению $E[Y]$ - по свойству \textbf{3} с предыдущего слайда. Главная идея: мы можем миновать шаг построения таблицы вероятности для $Y$ и сразу предсказать, каким будет $E[Y]$, по таблице вероятностей для $X$ и зная вид функции $Y = g(X)$, в нашем примере $Y = X^2 + 10$:
    \begin{gather*}
        E[Y] = \sum \limits_{i=1}^{6} g(x_i) P_X(X = x_i) = \sum \limits_{i=1}^{6} (x^2_i + 10) P_X(X = x_i) = \\
        = 10 \cdot 0.1 + 11 \cdot 0.1 + 14 \cdot 0.1 + 11 \cdot 0.2 + 14 \cdot 0.2 + 19 \cdot 0.3 = 14.2
    \end{gather*}
\end{itemize}

## Физическое \cancel{Лирическое} отступление 2

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Ось X
    \draw[thick, ->] (-5., -1.5) -- (5, -1.5) node[right] {$X$};
    
    % Деления на оси
    \foreach \x in {-1, 0, 1} {
        \draw (\x, -1.4) -- (\x, -1.6) node[below] {\x};
    }

    \draw (-4, -1.4) -- (-4, -1.6) node[below] {-1000};
    \draw (0, -1.4) -- (0, -1.6) node[below] {0};
    \draw (4, -1.4) -- (4, -1.6) node[below] {1000};
    
    % Стержень
    \draw[very thick, gray] (-1, 0) -- (1, 0);

    % Стержень
    \draw[very thick, gray] (-4, -1) -- (4, -1);
    
    % Левая масса в координате -1
    \draw[thick, fill=blue!20] (-1, 0) circle (0.2);
    \node at (-1, 0.35) {0.5 кг};
    
    % Правая масса в coordinate 1
    \draw[thick, fill=blue!20] (1, 0) circle (0.2);
    \node at (1, 0.35) {0.5 кг};
    
    % Центр тяжести в coordinate 0
    \draw[thick, fill=red!30] (0, -0.1) -- (-0.08, -0.25) -- (0.08, -0.25) -- cycle;

    % Левая масса в координате -100 (визуально в -1)
    \draw[thick, fill=blue!20] (-4, -1) circle (0.2);
    \node at (-4, -0.65) {0.5 кг};
    
    % Правая масса в coordinate 100 (визуально в 1)
    \draw[thick, fill=blue!20] (4, -1) circle (0.2);
    \node at (4, -0.65) {0.5 кг};
    
    % Центр тяжести в координате 0
    \draw[thick, fill=red!30] (0, -1.1) -- (-0.08, -1.25) -- (0.08, -1.25) -- cycle;
\end{tikzpicture}
\end{center}

- В вероятностном мире интерпретация картинки такая, что может быть две случайные величины с одинаковым математическим ожиданием, но с кардинально разными значениями.
- Представьте, что в одном случае вы кидаете монетку с привязанными численными значениями $+1$ и $-1$ (например, выигрыш - проигрыш), а в другом ту же монетку, но с привязанными значениями уже $+1000$ и $-1000$. Математическое ожидание в обоих случаях будет $0$, но сравните магнитуды возможных значений!
- Это помогает нам понять мотивацию введения новой характеристики для случайной величины - **дисперсии** - которая сможет охарактеризовать степень разброса значений случайной величины.


## Характеристики С.В.: Дисперсия

- Дисперсия случайной величины - это число, **константа**, которое помогает нам понять степень разброса потенциальных значений случайной величины относительно среднего.

- :::{.callout-definition}
Для случайной величины $X$ её дисперсия обозначается $Var[X]$ (Variance) и определяется как:
$$
    Var[X] =  E\left[ \left( X - E[X] \right)^2 \right]
$$
:::

- Формально говоря, это математическое ожидание новой случайной величины:
$$
    Y = g(X) = \left( X - E[X]\right)^2,
$$
описывающей квадрат расстояния между значением случайной величины $X$ и её математическим ожиданием.

## Характеристики С.В.: Дисперсия

::: {.callout-tip title="Вычисление дисперсии"}
Существует упрощенная формула:
\begin{gather*}
    E\left[ \left( X - E[X] \right)^2 \right] = E\left[  X^2 - 2XE[X] + (E[X])^2  \right] = \\
    = E[X^2] - E\left[2 E[X] X \right] + E \left[ (E[X])^2 \right] = E[X^2] - 2 E[X] E[X] + (E[X])^2 = \\  \boxed{E[X^2] - (E[X])^2}
\end{gather*}

В процессе мы используем свойство линейности математического ожидания, а также знание того, что $E[X]$ - это константа, при этом $E[c] = c$, то есть $E \left[  E[X] \right] = E[X]$.
:::

## Свойства дисперсии
\begin{enumerate}
    \item \textbf{Неотрицательность}: Для любой случайной величины $X$:
    $$Var[X] \geq 0$$

    \item \textbf{Дисперсия константы}: Если $c$ - константа, то:
    $$Var[c] = 0$$

    \item \textbf{Масштабирование}: Для любой константы $c$:
    $$Var[cX] = c^2 Var[X]$$
\end{enumerate}

## Дисперсия: пример
Посчитаем дисперсию на примере нашей задачи. Считаем уже известным, что $E[X] = 1.2$.

\begin{center}
    \begin{tabular}{c | c c c c c c} 
        \hline
        $x$ & 0 & -1 & -2 & 1 & 2 & 3\\ [0.5ex] 
        \hline
        $p_X(x)$ & $0.1$ & $0.1$ & $0.1$ & $0.2$ & $0.2$ & $0.3$ \\ 
        \hline
    \end{tabular}
\end{center}

\begin{itemize}
\item Нам нужно вычислить $E[Y]$, где $Y = \left( X - E[X] \right)^2$. Сразу воспользуемся подходом, позволяющим миновать шаг построения таблицы вероятности для $Y$:
\begin{gather*}
    E[Y] = \sum \limits_{i=1}^{6} g(x_i) P_X(X = x_i) = \sum \limits_{i=1}^{6} (x_i - 1.2)^2 P_X(X = x_i) = \\
    = 1.44 \cdot 0.1 + 4.84 \cdot 0.1 + 10.24 \cdot 0.1 + 0.04 \cdot 0.2 + 0.64 \cdot 0.2 + 3.24 \cdot 0.3 = 2.76
\end{gather*}

\item Но для дисперсии у нас есть ещё более умный подход, описанный на одном из слайдов выше:
\begin{gather*}
    Var[X] = E \left[X^2 \right] - \left( E \left[ X \right] \right)^2 = 4.2 - \left( 1.2 \right)^2 = 2.76 \\
    E \left[ X^2 \right] = \sum \limits_{i=1}^{6} (x_i)^2 P_X(X = x_i) = 0.1 + 4 \cdot 0.1 + 1 \cdot 0.2 + 4 \cdot 0.2 + 9 \cdot 0.3 = 4.2
\end{gather*}

\item \textit{Voilà!}

\end{itemize}
