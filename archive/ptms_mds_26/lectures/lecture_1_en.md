---
title: "Probability Theory and Mathematical Statistics"
subtitle: "Probability Space. Classical Probability."
institute: "HSE FCS"
author: "Gleb Karpov"
format: 
    beamer:
        pdf-engine: xelatex
        aspectratio: 169
        fontsize: 9pt
        theme: Singapore
        fonttheme: serif
        section-titles: true
        incremental: true
        include-in-header: ../files/xeheader.tex  # Custom LaTeX commands and preamble
---
## Andrey Kolmogorov Changes Everything
## Description of a Random Experiment
### Sample Space
\begin{itemize}
\item A set that contains all possible \textit{unique} outcomes of a random experiment:
$$
    \Omega = \{ \omega_1, \, \omega_2, \, \omega_n, \, \ldots  \}
$$
\item May be finite or infinite
\item Critically depends on the setup of the random experiment and what we want to observe and describe
\end{itemize}

## Description of a Random Experiment
### Sample Space: Examples

Let us imagine that we toss:

- Two visually distinguishable coins: $\Omega = \{ Hh, \, Tt, \, Ht, \, Th \}$
- Two identical coins: $\Omega = \{ 2H, \, 2T, \, Diff\}$
- Identical coins with artifically introduced distinction: $\Omega = \{ Hh, \, Tt, \, Ht, \, Th \}$
- A die with letter faces: $\Omega = \{ a, \, b, \, c, \, d, \, e, \, f \}$

## Description of a Random Experiment
### Event

* Often we are interested not in a specific simple outcome, but in a set of several outcomes, e.g., "If 2, 3, or 6 comes up", then we win
* A set constructed from one or more simple outcomes is called an \textit{event}
* An important distinction from a simple outcome: an outcome occurs \textit{one and only one time}, but many events can occur simultaneously!

* ::: {.callout-tip title="Important!"}
 We say that an *event has occurred* if one of the simple outcomes of that event has been realized.
:::

## Description of a Random Experiment
### Event Space

\begin{itemize}
\item A set that contains all possible \textit{events} that can be constructed from the set of outcomes $\Omega$
\item In other words, the set of all possible subsets of $\Omega$:
$$
    \mathcal{F} = \{ A_1, \, A_2, \, A_n, \, \ldots  \}, \; \forall A_i \subset \Omega
$$
\item The sample space itself is also an event: $\Omega \subset \Omega$, therefore $\Omega \in \mathcal{F}$
\end{itemize}

\begin{center}
\begin{tikzpicture}
    % Рисуем круг для множества (справа)
    \draw[thick, fill=blue!10] (3.5,0.5) circle (2.);
    
    % Обозначение множества
    \node[above] at (3.5,2.5) {\small (Example $\mathcal{F}$: all subsets of $\{a,b,c\}$)};
    
    % Все 8 подмножеств
    \node at (3.5,1.5) {$\{a,b,c\}$};
    \node at (2,1.) {$\{a,b\}$};
    \node at (5,1.) {$\{a,c\}$};
    \node at (3.5,1.) {$\{b,c\}$};
    \node at (2,0) {$\{a\}$};
    \node at (5,0) {$\{b\}$};
    \node at (3.5,0) {$\{c\}$};
    \node at (3.5,-1.) {$\{\varnothing \}$};
    
    % Новый круг слева с общими событиями
    \draw[thick, fill=green!10] (-3.5,0.5) circle (2.);
    
    % Обозначение множества
    \node[above] at (-3.5,2.5) {\small ($\mathcal{F}$, in general)};
    
    % Общие события
    \node at (-3.5,1.5) {$\Omega$};
    \node at (-4.7,1.) {$A_1$};
    \node at (-2.3,1.) {$A_2$};
    \node at (-3.5,1.) {$A_3$};
    \node at (-4.7,0) {$A_k$};
    \node at (-2.3,0) {$A_n$};
    \node at (-3.5,0) {$\vdots$};
    \node at (-3.5,-1.) {$\varnothing$};
\end{tikzpicture}
\end{center}

## Description of a Random Experiment
### Event Space

:::{.callout-question}
If the cardinality of the sample space is $|\Omega| = n$, what will be the cardinality of the event space $|\mathcal{F}|$?
:::


## Description of a Random Experiment
### Probability
- Ultimately, we want to attach a "label" to each event with information about how confident we are that the event will occur
- This coefficient of our confidence is measured from $0$ to $1$, and we call it *probability*
- Formally, probability is a function that assigns a number to each event:
$$
    P(X): \, \mathcal{F} \longrightarrow [0,1] \subset \mathbb{R} 
$$

\begin{tikzpicture}
    % Левый круг - область определения (пространство событий)
    \draw[thick, fill=blue!10] (0,0) circle (2);
    \node at (0,0) {$\mathcal{F}$};
    
    % Правый круг - область значений (вещественные числа от 0 до 1)
    \draw[thick, fill=green!10] (10,0) circle (1.0);
    \node at (10,0) {$[0,1]$};
    
    % Стрелка от левого к правому кругу (изогнутая)
    \draw[thick, ->] (2.2,0) .. controls (5, 1) and (5,1) .. (8.8,0) node[midway, above] {$P(X)$};
\end{tikzpicture}

## Properties of the Probability Function
\begin{itemize}
\item $0 \leq P(X) \leq 1, \; \forall X \in \mathcal{F}$
\item $P(\Omega) = 1$, $P(\varnothing) = 0$
\item \textit{Additivity property of probability}:
$$
    \forall X, \, Y \in \mathcal{F}: \, X \cap Y = \varnothing, \, P(X \cup Y) = P(X) + P(Y)
$$

More generally: If a collection of events $A_1, \,  A_2, \, \ldots$ are pairwise disjoint, i.e., $A_i \cap A_j = \varnothing, \, i \neq j$, then:
$$
    P\left(\bigcup_{i=1}^m A_i\right)=\sum_{i=1}^m P\left(A_i\right)
$$
\end{itemize}

## Probability
### Complementary Events and the Inclusion-Exclusion Formula
::: {.columns}
::: {.column width="40%"}
\begin{tikzpicture}[scale=1.2]
  % Прямоугольное пространство выборки Ω
  \draw[thick, black] (0,0) rectangle (5,4);
  \node[above] at (3,4) {\Large $\Omega$};
  
  % Событие A (круг слева)
  \draw[thick, blue, fill=blue!20] (1.5,2) circle (1.3);
  \node[blue] at (0.7,2.8) {\Large $A$};
  
  % Событие B (круг справа)
  \draw[thick, red, fill=red!20] (3.5,2) circle (1.0);
  \node[red] at (4.3,2.8) {\Large $B$};
  
  % Пересечение A ∩ B (закрашено более темным цветом)
  \begin{scope}
    \clip (1.5,2) circle (1.3);
    \fill[purple!40] (3.5,2) circle (1.0);
  \end{scope}
  
  % Подпись пересечения
  \node[purple, font=\large] at (3,2) {$A \cap B$};
  
  % Подписи областей
  \node[blue] at (0.4,1.0) {$\Omega \setminus A$};
  \node[blue] at (0.4,0.6) {$A^c, \, \bar{A}$};
  \node[red] at (4.6,1.0) {$\Omega \setminus B$};
  \node[blue] at (4.6,0.6) {$B^c, \, \bar{B}$};
  \node[black] at (0.7,3.5) {$(A \cup B)^c$};
\end{tikzpicture}
:::

::: {.column width="55%"}
- **Property**: If $A \in \mathcal{F}$, then $P(A) + P(\Omega \backslash A) = 1$.

Events $A$ and $\bar{A} = \Omega \backslash A$ are such that $A \cap \bar{A} = \varnothing$, and $\Omega = A \cup \bar{A}$, from which using the properties of probability we obtain: $P(\Omega) = P(A \cup \bar{A}) = P(A) + P(\Omega \backslash A) = 1$

- **Inclusion-Exclusion Formula**: If $A, B \in \mathcal{F}$, then 
$$
    P(A \cup B) = P(A)  + P(B) - P(A \cap B)
$$
Event $A$ is the union of disjoint sets $A \backslash B$ and $A \cap B$, hence $P(A)=P(A \backslash B) + P(A \cap B)$ and symmetrically $P(B)=P(B \backslash A) + P(A \cap B)$.
\begin{gather*}
P(A)+P(B) =P(A \backslash B)+2 P(A \cap B)+P(B \backslash A) \\
=P((A \backslash B) \cup(A \cap B) \cup(B \backslash A))+P(A \cap B) \\
=P(A \cup B)+P(A \cap B) .
\end{gather*}


- **Property**: If $A, B \in \mathcal{F}$ and $A \subseteq B$, then $P(A) \leq P(B)$.
Easy to show: $P(B) = P(A) + P(B \backslash A) \geq P(A)$.
:::
:::

## Classical Probability
- The first model of a probabilistic experiment, the essence of which is the assumption of equal probability of simple outcomes of a random experiment. This applies to many discrete problems related to random selection of cards, balls, people, rolls of dice and coins, *etc*.
- Let us formalize: $\Omega = \{ \omega_1, \; \ldots, \; \omega_n \}$, $P(\{\omega_1\}) = \ldots = P(\{\omega_n\}) = p$.
- Let us apply the properties of probability to obtain an intuitively clear result about the probability of a simple outcome:
\begin{gather*}
    \Omega = \{ \omega_1 \} \cup \cdots \cup \{ \omega_n \} = \bigcup\limits_{i=1}^{n} \{ \omega_i \} \\
    P(\Omega) = P \left( \bigcup\limits_{i=1}^{n} \{ \omega_i \} \right) = \sum\limits_{i=1}^{n} P(\{ \omega_i \}) = n \cdot p = 1 \rightarrow p = \frac{1}{n}
\end{gather*}

## Classical Probability
### First Important Formula
- Without loss of generality, assume that some event $A$ consists of $k \leq n$ simple outcomes, $A = \{\omega_1, \; \ldots, \; \omega_k \}$. We are interested in $P(A)$.
- Let us derive the formula for the probability of $A$:
\begin{gather*}
    A = \{ \omega_1 \} \cup \cdots \cup \{ \omega_k \} = \bigcup\limits_{i=1}^{k} \{ \omega_i \} \\
    P(A) = P \left( \bigcup\limits_{i=1}^{k} \{ \omega_i \} \right) = \sum\limits_{i=1}^{k} P(\{ \omega_i \}) = k \cdot p = \frac{k}{n} = \frac{|A|}{|\Omega|}
\end{gather*}

## Combinatorial Probability
### Basic Principle of Counting

:::{.callout-definition}
If $r$ experiments are to be performed such that the first can result in any of $n_1$ possible outcomes; and if for each of these $n_1$ possible outcomes there are $n_2$ possible outcomes of the second experiment; and if for each of the possible outcomes of the first two experiments there are $n_3$ possible outcomes of the third experiment; and if ..., then there are a total of $n_1 \cdot n_2 \cdots n_r$ possible outcomes of the $r$ experiments.
:::
\begin{tikzpicture}[scale=0.6]
    % Определяем размеры и позиции (уменьшены)
    \def\sectorwidth{2.5}
    \def\sectorheight{6}
    \def\boxheight{0.8}
    \def\boxwidth{2}
    \def\spacing{1.2}
    
    % Левый сектор A (3 блока)
    \draw[thick, fill=blue!20] (0,0) rectangle (\sectorwidth,\sectorheight);
    \node[above, font=\small] at (\sectorwidth/2,\sectorheight) {Exp A};
    
    % Средний сектор B (4 блока)
    \draw[thick, fill=green!20] (3.5,0) rectangle (3.5+\sectorwidth,\sectorheight);
    \node[above, font=\small] at (3.5+\sectorwidth/2,\sectorheight) {Exp B};
    
    % Правый сектор C (3 блока)
    \draw[thick, fill=orange!20] (7,0) rectangle (7+\sectorwidth,\sectorheight);
    \node[above, font=\small] at (7+\sectorwidth/2,\sectorheight) {Exp C};
    
    % Блоки в левом секторе A (3 штуки)
    \foreach \i in {1,2,3} {
        \def\ypos{\sectorheight - \i*\spacing - \boxheight/2}
        \draw[thick, fill=white] (0.2,\ypos-\boxheight/2) rectangle (0.2+\boxwidth,\ypos+\boxheight/2);
        \node[font=\tiny] at (0.2+\boxwidth/2,\ypos) {A\i};
    }
    
    % Блоки в среднем секторе B (4 штуки)
    \foreach \i in {1,2,3,4} {
        \def\ypos{\sectorheight - \i*\spacing - \boxheight/2}
        \draw[thick, fill=white] (3.7,\ypos-\boxheight/2) rectangle (3.7+\boxwidth,\ypos+\boxheight/2);
        \node[font=\tiny] at (3.7+\boxwidth/2,\ypos) {B\i};
    }
    
    % Блоки в правом секторе C (3 штуки)
    \foreach \i in {1,2,3} {
        \def\ypos{\sectorheight - \i*\spacing - \boxheight/2}
        \draw[thick, fill=white] (7.2,\ypos-\boxheight/2) rectangle (7.2+\boxwidth,\ypos+\boxheight/2);
        \node[font=\tiny] at (7.2+\boxwidth/2,\ypos) {C\i};
    }
    
    % Линии A → B (все блоки A соединяются со всеми блоками B)
    \foreach \i in {1,2,3} {
        \def\yposA{\sectorheight - \i*\spacing - \boxheight/2}
        \foreach \j in {1,2,3,4} {
            \def\yposB{\sectorheight - \j*\spacing - \boxheight/2}
            \draw[thin, gray] (0.2+\boxwidth,\yposA) -- (3.7,\yposB);
        }
    }
    
    % Линии B → C (все блоки B соединяются со всеми блоками C)
    \foreach \i in {1,2,3,4} {
        \def\yposB{\sectorheight - \i*\spacing - \boxheight/2}
        \foreach \j in {1,2,3} {
            \def\yposC{\sectorheight - \j*\spacing - \boxheight/2}
            \draw[thin, gray] (3.7+\boxwidth,\yposB) -- (7.2,\yposC);
        }
    }
\end{tikzpicture}

## Combinatorial Probability
### Permutations

- **Motivation**: How many different ordered sequences can be formed from the set $\{ a, b, c \}$

- $P^r_n = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n - r + 1)$

## Combinatorial Probability
### Permutations: Examples

- :::{.callout-question}
**Random number sampling**. Let the population consist of ten digits 0, 1, ..., 9. Each sequence of five digits represents a sample of size $r = 5$. What is the probability that five consecutive random digits are all different?
:::
- $P = \frac{P_{10}^5}{10^5} = 0.3024$.



## Combinatorial Probability
### Combinations

- **Motivation**: Extract three elements from the set $\{ A, B, C, D, E \}$

- In general, since $n(n − 1)···(n− k + 1)$ represents the number of different ways in which a group of $k$ elements can be chosen from $n$ elements when the order of selection is important, and since each group of $k$ elements will be counted $k!$ times in this count, it follows that the number of different groups of $k$ elements that can be formed from a set of $n$ elements is
$$
\frac{n(n-1) \cdots(n-k+1)}{k!}=\frac{n!}{(n-k)!k!}
$$

- :::{.callout-definition}
We define $C_n^k$, for $k \leq n$, as
$$
C_n^k = \frac{n!}{(n-k)!k!},
$$
and say that $C_n^k$ represents the number of possible combinations (collections) of size $k$ obtained from $n$ objects. The order of elements in this case is not considered important.
:::

## Combinatorial Probability
### Combinations: Example

Problems often fit the model of drawing balls from a bag.

**Example**: A bag contains 15 balls, of which 10 are red and 5 are white. Four balls are selected from the bag.

There is an ambiguity here: for example, if in one draw I select four red balls, and in another draw I select four different red balls, are these samples considered the same or not?

We will assume that these are not the same samples. For example, we can imagine that the balls are numbered, so we can distinguish balls of the same color. This way of thinking is very useful for calculating probabilities in the classical scheme.

## Combinatorial Probability
### Combinations: Example

- 10 red, 5 white, numbered balls

- :::{.callout-question}
How many different samples (of size 4) are possible?
:::
- Order is not important, but numbers are important, so we choose 4 elements from the set of 10 + 5 elements. Therefore, the answer is: $C_{15}^4 = 1365$.

- :::{.callout-question}
How many samples (of size 4) consist entirely of red balls?
:::
- Order is not important, but numbers are important, we choose 4 elements from the set of red balls. Therefore, the answer is: $C_{10}^4 = 210$.

## Combinatorial Probability
### Combinations: Example

- 10 red, 5 white, numbered balls

- :::{.callout-question} 
How many samples contain 2 red and 2 white balls?
:::
- We can choose 2 numbered red balls in $C_{10}^2$ ways and 2 numbered white balls in $C_5^2$ ways. Neither choice affects the other, so the answer is: $C_{10}^2 \cdot C_5^2 = 45 \cdot 10 = 450$.

- :::{.callout-question}
How many samples (of size 4) contain exactly 3 red balls?
:::
- We can choose 3 numbered red balls in $C_{10}^3$ ways and 1 numbered white ball in $C_5^1$ ways. Neither choice affects the other, so the answer is: $C_{10}^3 \cdot C_5^1 = 120 \cdot 5 = 600$.

## Combinatorial Probability
### Combinations: Example

- :::{.callout-question}
How many samples (of size 4) contain at least 3 red balls?
:::

- This is the number of samples with 3 red plus the number of samples with 4 red. We can choose 4 numbered red balls in $C_{10}^4$ ways and 0 numbered white balls in $C_5^0$ ways. Neither choice affects the other, so the answer is: $C_{10}^4 \cdot C_5^0 = 210 \cdot 1 = 210$.
From the previous example, there are 600 ways to choose samples with exactly 3 red balls, so our answer is: $600 + 210 = 810$.

## Combinatorial Probability
### Mixed Counting Problems

- 10 red, 5 white, numbered balls

- :::{.callout-question}
How many samples (of size 4) contain at least one red ball?
:::
- This is $C_{10}^1 \cdot C_5^3 + C_{10}^2 \cdot C_5^2 + C_{10}^3 \cdot C_5^1 + C_{10}^4 \cdot C_5^0$, which equals $10 \cdot 10 + 45 \cdot 10 + 120 \cdot 5 + 210 \cdot 1 = 100 + 450 + 600 + 210 = 1360$.

This is also the total number of samples (1365) minus the number of samples without red balls, which equals $C_{10}^0 \cdot C_5^4 = 5$.


## Geometric Probability

### Definition
Geometric probability applies to experiments where the sample space $\Omega$ is a subset of Euclidean space (line segment, area, volume).

### Basic Formulas

**For the one-dimensional case (line segment):**
$$P(A) = \frac{\text{length of set } A}{\text{length of set } \Omega}$$

**For the two-dimensional case (area):**
$$P(A) = \frac{\text{area of set } A}{\text{area of set } \Omega}$$

**For the three-dimensional case (volume):**
$$P(A) = \frac{\text{volume of set } A}{\text{volume of set } \Omega}$$

<!-- ## Геометрическая вероятность
### Пример: задача о встрече

::: {.columns}
::: {.column width="50%"}


\begin{tikzpicture}[scale=1.2]
  % Квадрат [0,1] × [0,1] - пространство выборки
  \draw[thick, black] (0,0) rectangle (4,4);
  \node[above] at (2,4.2) {\Large $\Omega = [0,1] \times [0,1]$};
  
  % Оси координат
  \draw[thin, gray] (0,0) -- (0,4.3);
  \draw[thin, gray] (0,0) -- (4.3,0);
  \node[right] at (4.3,0) {$x$};
  \node[above] at (0,4.3) {$y$};
  
  % Подписи осей
  \node[below] at (0,0) {$0$};
  \node[below] at (4,0) {$1$};
  \node[left] at (0,4) {$1$};
  
  % Область благоприятных исходов |x - y| ≤ 1/4
  % Заливаем полосу между линиями y = x + 1/4 и y = x - 1/4
  \fill[blue!30] (0,1) -- (3,4) -- (4,4) -- (4,3) -- (1,0) -- (0,0) -- cycle;
  
  % Две параллельные линии (масштаб 4x4)
  \draw[thick, blue] (0,1) -- (3,4);  % y = x + 1/4
  \draw[thick, blue] (1,0) -- (4,3);  % y = x - 1/4
  
  % Диагональ y = x
  \draw[thick, dashed, gray] (0,0) -- (4,4);
  \node[gray] at (3.5,3.5) {$y = x$};
  
  % Подпись области
  \node[blue, font=\large] at (2,2) {$|x - y| \leq \frac{1}{4}$};
  
  % Точка для примера
  \fill[red] (2.5,2.8) circle (0.05);
  \node[right, red] at (2.6,2.8) {$(x, y)$};
\end{tikzpicture}

:::

::: {.column width="45%"}

**Условие задачи:**

Два человека договариваются встретиться в определенном месте между 12:00 и 13:00. Каждый приходит в случайный момент времени и ждет 15 минут. Какова вероятность встречи?

**Решение:**

Пусть $x$ - время прихода первого человека, $y$ - время прихода второго человека.

Встреча произойдет, если $|x - y| \leq \frac{1}{4}$.

**Пространство выборки:** $\Omega = [0,1] \times [0,1]$

**Площадь благоприятной области:**
$$S_{\text{благ}} = 1 - 2 \cdot \frac{1}{2} \cdot \frac{3}{4} \cdot \frac{3}{4} = 1 - \frac{9}{16} = \frac{7}{16}$$

**Ответ:**
$$P(\text{встреча}) = \frac{S_{\text{благ}}}{S_{\Omega}} = \frac{7/16}{1} = \frac{7}{16}$$

:::
::: -->

## Geometric Probability
### Classical Geometric Probability Problems

1. **Meeting Problem**: Two people agree to meet at a certain place between 12:00 and 13:00. Each arrives at a random time and waits 15 minutes. What is the probability of meeting?

2. **Buffon's Needle Problem**: A needle of length $l$ is thrown onto a plane ruled with parallel lines at distance $d$ apart. What is the probability that the needle intersects a line?

3. **Random Point in a Circle Problem**: A point is chosen randomly inside a circle of radius $R$. What is the probability that the distance from the point to the center is less than $r$?



