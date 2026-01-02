---
title: "Теория вероятностей и математическая статистика"
subtitle: "Многомерные случайные величины."
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

## Введение
### Возвращение в дискретный мир

\begin{itemize}
    \item Точно так же, как мы можем наблюдать результат одновременного подбрасывания двух монет, мы можем наблюдать результат более чем одной случайной величины одновременно.
    
    \item Для описания этого эксперимента мы используем новое понятие - многомерная случайная величина или случайный вектор:
    $$
    X = (X_1, X_2, \ldots, X_n), \text{ или в двумерном случае } (X, Y).
    $$
    
    \item Сравните это с элементарным исходом вида $\omega = ( \text{состояние}_1, \; \ldots, \; \text{состояние}_n )$, как например для одновременного или последовательного подбрасывания монет
    
    \item Теперь уникальным \textbf{элементарным исходом} будет набор одновременно наблюдаемых значений случайных величин. Например $(x,y) = (10, 2)$, где $X$ - число на кубике с $20$ гранями, $Y$ - число на кубике с 6 гранями, бросили их вместе и наблюдаем вместе как единую целую картину.
\end{itemize}

## Совместная функция вероятности

\begin{itemize}
    \item Нас интересует \textit{взаимное поведение} этих случайных величин.
    \item Связаны ли они? Сопровождается ли некоторое значение одной величины более часто некоторым другим значением второй величины? Можем ли мы извлекать больше информации о происходящих случайных экспериментах, когда мы учитываем взаимодействие случайных величин друг с другом?
    \item Для описания этого взаимодействия, или взаимного поведения, мы используем \textbf{совместную функцию вероятности}, \textit{т.е.}:
    \begin{center}
    \begin{tabular}{c | c c}
            & \(Y=1\) & \(Y=2\) \\
            \hline
            \(X=1\) & $\frac{1}{8}$ & $\frac{1}{4}$ \\
            \(X=2\) & $\frac{1}{8}$ & $\frac{1}{2}$ \\
    \end{tabular}
    \end{center}
\end{itemize}

## Совместная функция вероятности

\begin{itemize}
    \item В общем виде:
    \begin{center}
    \begin{tabular}{c | c c c} 
            & $Y=y_1$ & \ldots & $Y=y_m$ \\
            \hline
            $X=x_1$ & $P(\{ X=x_1, Y=y_1 \})$ & \ldots & $P(\{ X=x_1, Y=y_m \})$ \\
            \ldots & \ldots                   & \ldots & \ldots \\
            $X=x_n$ & $P(\{ X=x_n, Y=y_1 \})$ & \ldots & $P(\{ X=x_n, Y=y_m \})$ \\
    \end{tabular}
    \end{center}

    \item Мы также можем записать $P(\{ X=x_i, Y=y_j \})$ как $P_{X, \, Y} \left(x_i, y_j\right)$
\end{itemize}

### Свойства

\begin{itemize}
    \item $P_{X, \, Y} \left(x_i, y_j\right) \geq 0$, для всех возможных $(x_i, \, y_j)$
    \item Поскольку $P(\Omega) = 1$, здесь мы имеем $\Omega = \{ (x_1, y_1), (x_1, y_2),\ldots, (x_n, y_m) \}$. Из этого следует:
    $$
            \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{m} P(\{ X=x_i, Y=y_j \}) = 1.
    $$
\end{itemize}

## Маргинальная функция вероятности
\begin{itemize}
    \item От англ. marginal. В более старых переводах - частная функция вероятности, частное распределение
    
    \item Предположим, нас интересует получение результата $X=x_i$, независимо от того, чему равно $Y$. Это означает, что все следующие пары являются допустимыми, и они образуют специальное событие:
    $$
            A = \{\text{мы получаем } X = x_i\} = \{ (x_i, \, y_1), (x_i, \, y_2), \ldots, (x_i, \, y_m) \}
    $$
    
    \item Если затем мы хотим найти вероятность этого события, то по свойству аддитивности:
    $$
            P (\{X = x_i\}) = P_{X, \, Y}(x_i, y_1) + P_{X, \, Y}(x_i, y_2) + \ldots + P_{X, \, Y}(x_i,y_m),
    $$
    т.е. мы складываем вероятности всех элементарных исходов, формирующих это событие.
    
    \item Это означает, что используя совместную функцию вероятности, мы можем восстановить собственную функцию вероятности случайной величины, как бы изолируя её отдельно от случайного вектора.
    
    \item Раньше мы называли это просто \textbf{функцией вероятности}, но теперь нам нужно уточнять, потому что добавляется много новых видов функций вероятности.
\end{itemize}

## Маргинальная функция вероятности

\begin{itemize}
    \item В общем виде:
    \begin{gather*}
    P (\{X = x_i\}) = \sum\limits_{j=1}^{m} P(\{ X=x_i, Y=y_j \}) = \sum\limits_{j=1}^{m} P_{X, \, Y}(x_i, y_j) \\
    P (\{Y = y_j\}) = \sum\limits_{i=1}^{n} P(\{ X=x_i, Y=y_j \}) = \sum\limits_{i=1}^{n} P_{X, \, Y}(x_i, y_j)
    \end{gather*}
    
    \item Другими словами, маргинальные вероятномти являются суммами по соответствующей строке или столбцу в таблице совместного распределения:
    \begin{center}
    \begin{tabular}{c | c c c} 
            & $Y=y_1$ & \ldots & $Y=y_m$ \\
            \hline
            $X=x_1$ & $P(\{ X=x_1, Y=y_1 \})$ & \ldots & $P(\{ X=x_1, Y=y_m \})$ \\
            \ldots & \ldots                   & \ldots & \ldots \\
            $X=x_n$ & $P(\{ X=x_n, Y=y_1 \})$ & \ldots & $P(\{ X=x_n, Y=y_m \})$ \\
    \end{tabular}
    \end{center}
\end{itemize}

## Условная функция вероятности

\begin{itemize}
    \item В многомерном мире мы также можем исследовать вопросы следующего вида: $P(X = x_i | Y = y_j)$
    
    \item Мы называем это еще одной функцией вероятности - \textbf{условной функцией вероятности}
    
    \item Напомним: условная вероятность - это своего рода параметризованная функция, где событие-условие служит параметром. Функции $P(X|A)$ и $P(X|B)$, $A \neq B$, являются разными функциями!
    
    \item Применяя определение условной вероятности:
    \begin{gather*}
            P(X = x_i | Y = y_j) = \frac{P(\{X=x_i \} \cap \{ Y=y_j\})}{P(Y=y_j)} = \frac{P(\{ X=x_i, Y=y_j \})}{P(Y=y_j)} \\
            P(Y = y_j| X = x_i) = \frac{P(\{X=x_i \} \cap \{ Y=y_j\})}{P(X=x_i)} = \frac{P(\{ X=x_i, Y=y_j \})}{P(X=x_i)}
    \end{gather*}
\end{itemize}

## Независимость
\begin{itemize}
    \item Наконец, есть важный разговор о независимости случайных величин. В некотором смысле это даже более важно, чем независимость отдельных событий.
    
    \item Напомним. Независимость пары событий:
    \begin{gather*}
    P(A) = P(A|B), \quad P(B) = P(B|A) \\
    P(A) = P(A|B) = \frac{P(A \cap B)}{P(B)} \rightarrow P(A \cap B) = P(A)P(B).
    \end{gather*}
\end{itemize}

## Независимость

- Рассмотрим каждую возможную пару следующих событий:

\begin{columns}
\column{.5\textwidth}
\begin{itemize}
    \item $\{ X=x_1 \}$ \tikzmark{x_1}
    \item $\{ X=x_2 \}$
    \item \ldots
    \item $\{ X=x_n \}$ \tikzmark{x_n}
\end{itemize}

\column{.5\textwidth}
\begin{itemize}
    \item \tikzmark{y_1} $\{ Y=y_1 \}$ 
    \item \tikzmark{y_2} $\{ Y=y_2 \}$
    \item \ldots
    \item \tikzmark{y_m} $\{ Y=y_m \}$
\end{itemize}
\end{columns}

\begin{tikzpicture}[overlay,remember picture]
\draw[red!25, very thick, Stealth-Stealth]         ($({pic cs:x_1})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_1})+(-2ex,1ex)$);
\draw[red!25, very thick, Stealth-Stealth]         ($({pic cs:x_1})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_2})+(-2ex,1ex)$);
\draw[red!25, very thick, Stealth-Stealth]         ($({pic cs:x_1})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_m})+(-2ex,1ex)$);
\draw[green!25, very thick, Stealth-Stealth]         ($({pic cs:x_n})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_1})+(-2ex,1ex)$);
\draw[green!25, very thick, Stealth-Stealth]         ($({pic cs:x_n})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_2})+(-2ex,1ex)$);
\draw[green!25, very thick, Stealth-Stealth]         ($({pic cs:x_n})+(1ex,1ex)$)
    to [left, ""]  ($({pic cs:y_m})+(-2ex,1ex)$);
\end{tikzpicture}

:::{.callout-definition}
Если каждая пара оказывается независимыми событиями, то мы говорим, что случайные величины $X$ и $Y$ независимы.

\begin{equation*}
    \forall x_i, \; \forall y_j: \; P\{ X=x_i \}P\{ Y = y_j \} = P(\{X=x_i \} \cap \{ Y=y_j\}) = P(\{ X=x_i, Y=y_j \}).
\end{equation*}
:::

## Задачи

Совместная функция вероятности $X$ и $Y$ задана следующим образом:

\begin{center}
        \begin{tabular}{c | c c}
    & \(Y=1\) & \(Y=2\) \\
    \hline
    \(X=1\) & $\frac{1}{8}$ & $\frac{1}{4}$ \\
    \(X=2\) & $\frac{1}{8}$ & $\frac{1}{2}$ \\

    \end{tabular}
\end{center}

\begin{enumerate}
    \item Найдите маргинальные функции вероятности для каждой случайной величины.
    \item Вычислите условную функцию вероятности $X$ при условии $Y = i$, $i = 1, 2$.
    \item Независимы ли $X$ и $Y$?
\end{enumerate}

## Решение задачи

### 1. Маргинальные функции вероятности

Для $X$:
\begin{align*}
P(X=1) &= \sum\limits_{j=1}^{2} P(X=1, Y=j) = \frac{1}{8} + \frac{1}{4} = \frac{3}{8} \\
P(X=2) &= \sum\limits_{j=1}^{2} P(X=2, Y=j) = \frac{1}{8} + \frac{1}{2} = \frac{5}{8}
\end{align*}

Для $Y$:
\begin{align*}
P(Y=1) &= \sum\limits_{i=1}^{2} P(X=i, Y=1) = \frac{1}{8} + \frac{1}{8} = \frac{1}{4} \\
P(Y=2) &= \sum\limits_{i=1}^{2} P(X=i, Y=2) = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}
\end{align*}

## Решение задачи (продолжение)
### 2. Условные функции вероятности

$P(X|Y=1)$:
\begin{align*}
P(X=1|Y=1) &= \frac{P(X=1, Y=1)}{P(Y=1)} = \frac{\frac{1}{8}}{\frac{1}{4}} = \frac{1}{2} \\
P(X=2|Y=1) &= \frac{P(X=2, Y=1)}{P(Y=1)} = \frac{\frac{1}{8}}{\frac{1}{4}} = \frac{1}{2}
\end{align*}

$P(X|Y=2)$:
\begin{align*}
P(X=1|Y=2) &= \frac{P(X=1, Y=2)}{P(Y=2)} = \frac{\frac{1}{4}}{\frac{3}{4}} = \frac{1}{3} \\
P(X=2|Y=2) &= \frac{P(X=2, Y=2)}{P(Y=2)} = \frac{\frac{1}{2}}{\frac{3}{4}} = \frac{2}{3}
\end{align*}

## Решение задачи (продолжение)

### 3. Проверка независимости

Проверим условие независимости для пары:
\begin{align*}
P(X=1, Y=1) &= \frac{1}{8} \quad \text{и} \quad P(X=1)P(Y=1) = \frac{3}{8} \cdot \frac{1}{4} = \frac{3}{32} \neq \frac{1}{8}
\end{align*}

**Вывод:** $X$ и $Y$ **не независимы**.

## Функции от случайных векторов

\begin{itemize}
    \item Мы обсуждали идею, что функция от случайной величины сама является случайной величиной, т.е. $W = g(X)$.
    \item Функция может быть от более чем одной переменной, и теперь мы можем получить $W = f(X,Y)$.
    \item Как и в случае с одной переменной, мы можем захотеть предсказать $E[W] = E[f(X,Y)]$. 
    \item Напомним:
    \begin{align*}
    E[X] & = \sum \limits_{i=1}^{n} x_i P(X = x_i) \\
    E[g(X)] & = \sum \limits_{i=1}^{n} g(x_i) P(X = x_i)
    \end{align*}
    \item В новом случае:
    $$
        E[g(X,Y)] = \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} g(x_i, y_j) P(X = x_i, Y = y_j)
    $$
\end{itemize}

## Пример
Совместная функция вероятности $X$ и $Y$ задана следующим образом:

\begin{center}
    \begin{tabular}{c | c c} 
    & \(Y=1\) & \(Y=2\) \\
    \hline
    \(X=1\) & $\frac{1}{8}$ & $\frac{1}{4}$ \\
    \(X=2\) & $\frac{1}{8}$ & $\frac{1}{2}$ \\
    \end{tabular}
\end{center}

Рассмотрим функции $W = XY$,  $G = X-Y$. Найдите их функции вероятности и математические ожидания.

## Пример

Найти математическое ожидание $E[XY]$

**Вариант 1: Через распределение новой случайной величины**

Сначала найдем распределение $W = XY$:
\begin{itemize}
    \item $W = 1$: когда $(X=1, \, Y=1)$, $P(W=1) = P(X=1, \, Y=1) = \frac{1}{8}$
    \item $W = 2$: когда $(X=1, \, Y=2)$ или $(X=2, \, Y=1)$, $P(W=2) = \frac{1}{4} + \frac{1}{8} = \frac{3}{8}$
    \item $W = 4$: когда $(X=2, \, Y=2)$, $P(W=4) = P(X=2, \, Y=2) = \frac{1}{2}$

    \item Теперь вычислим математическое ожидание:
$$
    E[XY] = E[W] = 1 \cdot \frac{1}{8} + 2 \cdot \frac{3}{8} + 4 \cdot \frac{1}{2} = \frac{1}{8} + \frac{6}{8} + \frac{4}{2} = \frac{23}{8}
$$
\end{itemize}

## Пример
**Вариант 2: Используя формулу непосредственного подсчета**

$$E[XY] = \sum\limits_{i=1}^{2} \sum\limits_{j=1}^{2} x_i y_j P(X = x_i, Y = y_j)$$

\begin{align*}
E[XY] &= 1 \cdot 1 \cdot \frac{1}{8} + 1 \cdot 2 \cdot \frac{1}{4} + 2 \cdot 1 \cdot \frac{1}{8} + 2 \cdot 2 \cdot \frac{1}{2} \\
&= \frac{1}{8} + \frac{2}{4} + \frac{2}{8} + \frac{4}{2} \\
&= \frac{23}{8}
\end{align*}

**Ответ:** $E[XY] = \frac{23}{8} = 2.875$

## Пример
Найти математическое ожидание $E[X-Y]$

**Вариант 1: Через распределение новой случайной величины**

Сначала найдем распределение $G = X - Y$:
\begin{itemize}
    \item $G = -1$: когда $(X=1, Y=2)$, $P(G=-1) = P(X=1, Y=2) = \frac{1}{4}$
    \item $G = 0$: когда $(X=1, Y=1)$ и $(X=2, Y=2)$, $P(G=0) = P\left(\{(X=1, Y=1), \, (X=2, Y=2)\}\right) = \frac{1}{8} + \frac{1}{2} = \frac{5}{8}$
    \item $G = 1$: когда $(X=2, Y=1)$, $P(G=1) = P(X=2, Y=1) = \frac{1}{8}$

    \item Теперь вычислим математическое ожидание:
    $$
        E[X-Y] = E[G] = 0 \cdot \frac{5}{8} + (-1) \cdot \frac{1}{4} + 1 \cdot \frac{1}{8} = -\frac{1}{8}
    $$
\end{itemize}

## Пример
**Вариант 2: Используя формулу непосредственного подсчета**

$$E[X-Y] = \sum\limits_{i=1}^{2} \sum\limits_{j=1}^{2} (x_i - y_j) P(X = x_i, Y = y_j)$$

\begin{align*}
E[X-Y] &= (1-1) \cdot \frac{1}{8} + (1-2) \cdot \frac{1}{4} + (2-1) \cdot \frac{1}{8} + (2-2) \cdot \frac{1}{2} \\
&= 0 \cdot \frac{1}{8} + (-1) \cdot \frac{1}{4} + 1 \cdot \frac{1}{8} + 0 \cdot \frac{1}{2} \\
&= 0 - \frac{1}{4} + \frac{1}{8} + 0 \\
&= -\frac{1}{8}
\end{align*}

**Ответ:** $E[X-Y] = -\frac{1}{8} = -0.125$

## Линейная комбинация случайных величин
### Математическое ожидание комбинации

\begin{itemize}
    \item Часто важно анализировать поведение суммы двух или более случайных величин
    \item В основном мы хотим понять, как ведет себя переменная $T = aX \pm bY$, каковы ее характеристики.
    \item Линейное свойство математического ожидания: $E[aX \pm bY] = a E[X] \pm b E[Y]$.
\begin{align*}
    E[T] = & \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} (a x_i \pm b y_j) P(X = x_i, Y = y_j) = \\
    & \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} a x_i P(X = x_i, Y = y_j)  \pm \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} b y_j P(X = x_i, Y = y_j) = \\
    & a \sum \limits_{i=1}^{n} x_i \underset{\text{marginal for } X}{\colorbox{green!20}{$\sum \limits_{j=1}^{m} P(X = x_i, Y = y_j)$}}  \pm b \sum \limits_{j=1}^{m} y_j \underset{\text{marginal for } Y}{\colorbox{red!20}{$\sum \limits_{i=1}^{n} P(X = x_i, Y = y_j)$}} = \\
    & a \sum \limits_{i=1}^{n} x_i \colorbox{green!20}{$P(X=x_i)$} \pm b \sum \limits_{j=1}^{m} y_j \colorbox{red!20}{$P(Y=y_j)$} = a E[X] \pm b E[Y]
\end{align*}
\end{itemize}

## Линейная комбинация случайных величин
### Но дисперсия - это уже совсем другая история...

\begin{itemize}
\item Нас интересует $Var[T] = Var[aX \pm bY]$. 

\item Давайте применим сокращенную формулу для дисперсии:
\begin{align*}
    Var[T] & = E[T^2] - (E[T])^2 = \colorbox{magenta!20}{$E[(aX \pm bY)^2]$} - (aE[X] \pm bE[Y])^2 \\
    & = \colorbox{magenta!20}{$E[a^2 X^2 \pm 2abXY + b^2 Y^2]$} - \left((aE[X])^2 \pm 2abE[X]E[Y] + (bE[Y])^2 \right) \\
    & = \colorbox{green!20}{$a^2 E[X^2]$} \pm 2abE[XY] + \colorbox{red!20}{$b^2 E[Y^2]$} - \colorbox{green!20}{$a^2(E[X])^2$} \mp 2abE[X]E[Y] - \colorbox{red!20}{$b^2(E[Y])^2$} \\
    & = \colorbox{green!20}{$a^2 Var[X]$} + \colorbox{red!20}{$b^2 Var[Y]$} \pm 2ab \biggl(E[XY] - E[X]E[Y] \biggr) 
\end{align*}

\item В процессе использовали свойство линейности математического ожидания.
\item Слагаемое $E[XY] - E[X]E[Y]$ называется \textbf{ковариацией} $X$ и $Y$.
\end{itemize}

## Ковариация и независимость

\textbf{Утверждение:} Если $X$ и $Y$ - независимые случайные величины, то $E[XY] = E[X]E[Y]$

:::{.callout-proof}
Используем определение независимости величин:
\begin{equation*}
    \forall x_i, \; \forall y_j: \; P_X \left( X=x_i \right) P_Y \left( Y = y_j \right) = P(\{X=x_i \} \cap \{ Y=y_j\}) = P \left( X=x_i, Y=y_j \right)
\end{equation*}
\begin{align*}
    E[XY] &= \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} x_i y_j P(X = x_i, Y = y_j) = \sum \limits_{i=1}^{n} \sum \limits_{j=1}^{m} x_i y_j P_X(x_i) P_Y(y_j) \\ &= \sum \limits_{i=1}^{n} x_i P_X(x_i) \sum \limits_{j=1}^{m} y_j P_Y(y_j) = E[X] E[Y].
\end{align*}
:::

Будьте внимательны: обратное утверждение неверно!

## Корреляция

\begin{itemize}
\item Ковариация не является хорошей мерой зависимости, поскольку она зависит от масштабов $X$ и $Y$.
\item Идея: нормализовать ковариацию и избавиться от масштабов.
\item Корреляция:
$$
    Corr(X,Y) = \frac{Cov(X,Y)}{\sqrt{Var[X]Var[Y]}}
$$

\item Она строго ограничена от $-1$ до $1$ и:
\begin{align*}
    Corr(X,Y) = 1 & \leftrightarrow Y = kX + b, \; k > 0 \\
    Corr(X,Y) = -1 & \leftrightarrow Y = -kX + b, \; k > 0
\end{align*}

\item Важно: Если переменные независимы, то их ковариация (и корреляция) равна нулю. Обратное утверждение НЕВЕРНО. Очень может быть, что ковариция равна нулю, но при этом величины являются зависимыми
\end{itemize}

## Пример:


\begin{center}
    \begin{tabular}{c | c c} 
    & \(Y=3\) & \(Y=-3\) \\
    \hline
    \(X=-1\) & $\frac{3}{4}$ & $0$ \\
    \(X=2\) & $0$ & $\frac{1}{4}$ \\
\end{tabular}
\end{center}

\begin{enumerate}
    \item Найдите маргинальные функции вероятности для $X$ и $Y$.
    \item Независимы ли $X$ и $Y$?
    \item Найдите ковариацию (и корреляцию) между $X$ и $Y$.
\end{enumerate}

## Решение задачи

### 1. Маргинальные функции вероятности

Для $X$:
\begin{align*}
P(X=-1) &= \sum\limits_{j} P(X=-1, Y=y_j) = \frac{3}{4} + 0 = \frac{3}{4} \\
P(X=2) &= \sum\limits_{j} P(X=2, Y=y_j) = 0 + \frac{1}{4} = \frac{1}{4}
\end{align*}

Для $Y$:
\begin{align*}
P(Y=3) &= \sum\limits_{i} P(X=x_i, Y=3) = \frac{3}{4} + 0 = \frac{3}{4} \\
P(Y=-3) &= \sum\limits_{i} P(X=x_i, Y=-3) = 0 + \frac{1}{4} = \frac{1}{4}
\end{align*}

## Пример
### Проверка независимости

Проверим условие независимости для пары:
\begin{align*}
P(X=-1, Y=3) &= \frac{3}{4} \quad \text{и} \quad P(X=-1)P(Y=3) = \frac{3}{4} \cdot \frac{3}{4} = \frac{9}{16} \neq \frac{3}{4}
\end{align*}

**Ответ:** $X$ и $Y$ **не независимы**.

## Пример
### Ковариация и корреляция

Сначала найдем математические ожидания:
\begin{align*}
E[X] &= (-1) \cdot \frac{3}{4} + 2 \cdot \frac{1}{4} = -\frac{3}{4} + \frac{1}{2} = -\frac{1}{4} \\
E[Y] &= 3 \cdot \frac{3}{4} + (-3) \cdot \frac{1}{4} = \frac{9}{4} - \frac{3}{4} = \frac{3}{2}
\end{align*}

Теперь найдем $E[XY]$:
\begin{align*}
E[XY] &= (-1) \cdot 3 \cdot \frac{3}{4} + (-1) \cdot (-3) \cdot 0 + 2 \cdot 3 \cdot 0 + 2 \cdot (-3) \cdot \frac{1}{4} \\
&= -\frac{9}{4} + 0 + 0 - \frac{6}{4} = -\frac{15}{4}
\end{align*}

## Пример
Ковариация:
\begin{align*}
Cov(X,Y) &= E[XY] - E[X]E[Y] = -\frac{15}{4} - \left(-\frac{1}{4}\right) \cdot \frac{3}{2} \\
&= -\frac{15}{4} + \frac{3}{8} = -\frac{30}{8} + \frac{3}{8} = -\frac{27}{8}
\end{align*}

Для корреляции найдем дисперсии:
\begin{align*}
E[X^2] &= (-1)^2 \cdot \frac{3}{4} + 2^2 \cdot \frac{1}{4} = \frac{3}{4} + 1 = \frac{7}{4} \\
Var[X] &= E[X^2] - (E[X])^2 = \frac{7}{4} - \left(-\frac{1}{4}\right)^2 = \frac{7}{4} - \frac{1}{16} = \frac{27}{16}
\end{align*}

\begin{align*}
E[Y^2] &= 3^2 \cdot \frac{3}{4} + (-3)^2 \cdot \frac{1}{4} = \frac{27}{4} + \frac{9}{4} = 9 \\
Var[Y] &= E[Y^2] - (E[Y])^2 = 9 - \left(\frac{3}{2}\right)^2 = 9 - \frac{9}{4} = \frac{27}{4}
\end{align*}

## Пример
Корреляция:
\begin{align*}
Corr(X,Y) &= \frac{Cov(X,Y)}{\sqrt{Var[X]Var[Y]}} = \frac{-\frac{27}{8}}{\sqrt{\frac{27}{16} \cdot \frac{27}{4}}} \\
&= \frac{-\frac{27}{8}}{\sqrt{\frac{729}{64}}} = \frac{-\frac{27}{8}}{\frac{27}{8}} = -1
\end{align*}

Корреляция равна $-1$, что означает полную отрицательную линейную зависимость между $X$ и $Y$.
