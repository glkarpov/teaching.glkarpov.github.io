---
title: "Теория вероятностей и математическая статистика"
subtitle: "Точечные оценки. Метод моментов. Интервальные оценки I."
institute: "ВШБ Бизнес-информатика"
author: "Глеб Карпов"
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

## Повторение
### Собираем вместе всё, чего успели коснуться

## Точечная оценка: визуализация

### Идеальная ситуация: мы знаем характеристики / параметры

\begin{center}
\begin{tikzpicture}[scale=1.2]
    % Ось
    \draw[->, thick] (0,0) -- (10,0) node[right] {$\mathbb{R}$};
    
    % Деления на оси
    \foreach \x in {1,2,...,9} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\small $\x$};
    }
    
    % Точка E[X]
    \draw[fill=blue] (3,0) circle (2pt) node[above=5pt] {$E[X]$};
    
    % Точка Var[X]
    \draw[fill=red] (6,0) circle (2pt) node[above=5pt] {$Var[X]$};
    
    % Точка theta
    \draw[fill=purple] (8,0) circle (2pt) node[above=5pt] {$\theta$};
\end{tikzpicture}
\end{center}

### Реальная ситуация: параметры неизвестны

\begin{center}
\begin{tikzpicture}[scale=1.2]
    % Ось
    \draw[->, thick] (0,0) -- (10,0) node[right] {$\mathbb{R}$};
    
    % Деления на оси
    \foreach \x in {1,2,...,9} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\small $\x$};
    }
    
    % Серый полупрозрачный фон (туман неопределенности)
    \fill[gray!85, opacity=0.85] (0,-0.5) rectangle (10,0.5);
    
    % Точка E[X] (скрыта в тумане)
    \draw[fill=blue] (3,0) circle (2pt);
    
    % Точка Var[X] (скрыта в тумане)
    \draw[fill=red] (6,0) circle (2pt);
    
    % Точка theta (скрыта в тумане)
    \draw[fill=purple] (8,0) circle (2pt);
    
    
    % Текст о неопределенности
    \node[above=25pt, text width=8cm, align=center] at (5,0) 
        {\small \textcolor{gray!80}{Значения будто скрыты от нас туманом}};
\end{tikzpicture}
\end{center}

## Цель точечной оценки

\begin{itemize}
    \item На основе реализации случайной выборки $x_1, x_2, \ldots, x_n$ получить \textbf{предположения} $\hat{\theta}$ о значениях скрытых в тумане реальности параметров.
    
    \item Идея состоит в том, чтобы посчитать значение оценки на реальных имеющихся данных, и чтобы полученное число было бы как можно ближе к истинному значению параметра.
    
    \item Следуя аналогии, мы хотим найти затерянные в тумане точки, путём их угадывания специальным способом, с помощью функции \textbf{оценки}.
\end{itemize}

\begin{center}
\begin{tikzpicture}[scale=1.2]
    % Ось
    \draw[->, thick] (0,0) -- (10,0) node[right] {$\mathbb{R}$};
    
    % Деления на оси
    \foreach \x in {1,2,...,9} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\small $\x$};
    }
    
    % Серый полупрозрачный фон (туман неопределенности)
    \fill[gray!85, opacity=0.85] (0,-0.5) rectangle (10,0.5);
    
    % Реальные параметры (скрыты в тумане, без подписей)
    \draw[fill=blue] (3,0) circle (2pt);
    \draw[fill=red] (6,0) circle (2pt);
    \draw[fill=purple] (8,0) circle (2pt);
    
    % Оценки (видны, с подписями)
    \draw[fill=green!70!black] (3.2,0) circle (2pt) node[above=5pt] {\textcolor{green!70!black}{$\hat{\mu}$}};
    \draw[fill=orange!70!black] (5.7,0) circle (2pt) node[above=5pt] {\textcolor{orange!70!black}{$\hat{\sigma}^2$}};
    \draw[fill=purple!70!black] (7.8,0) circle (2pt) node[above=5pt] {\textcolor{purple!70!black}{$\hat{\theta}$}};
        
    % Текст о неопределенности
    \node[above=30pt, text width=9cm, align=center] at (5,0) 
        {\small Значения точечных оценок $\hat{\mu}$, $\hat{\sigma}^2$ и $\hat{\theta}$ "попадают" близко к истинным значениям};
\end{tikzpicture}
\end{center}

## Уже известные точечные оценки
Пусть у нас есть случайная выборка $\mathcal{X} = (X_1, X_2, \ldots, X_n)$ (Независимые, одинаково распределенные) с $\mu \equiv E[X_i]$, $\sigma^2 \equiv Var[X_i]$.

### 1. Выборочное среднее $\bar{X}$
\begin{itemize}
    \item Определение: $\bar{X} = \frac{1}{n}\sum\limits_{i=1}^{n} X_i$
    
    \item Характеристики: $E[\bar{X}] = \mu \; \text{(несмещенная оценка)}, \quad \text{Var}(\bar{X}) = \frac{\sigma^2}{n}$
    
    \item Распределение:
    \begin{itemize}
        \item Если $X_i \sim \mathcal{N}(\mu, \sigma^2)$, то $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$
        \item По ЦПТ: при больших $n$ выполняется $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$
    \end{itemize}
\end{itemize}

### 2. Выборочная дисперсия $S^2$

\begin{itemize}
    \item Определение: $S^2 = \frac{1}{n-1}\sum\limits_{i=1}^{n}(X_i - \bar{X})^2$
    
    \item Характеристики: $E[S^2] = \sigma^2 \; \text{(несмещенная оценка)}, \quad \text{Var}(S^2) = \frac{2\sigma^4}{n-1}$
    
    \item Распределение: если $X_i \sim \mathcal{N}(\mu, \sigma^2)$, то:
    $$
    \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)
    $$
\end{itemize}


## Моменты случайной величины

\begin{itemize}
    \item \textbf{Момент $k$-го порядка} случайной величины $X$ — это математическое ожидание $k$-й степени $X$:
    $$
    \mu_k = E[X^k]
    $$
    
    \item \textbf{Первый момент} ($k=1$): $\mu_1 = E[X]$ — математическое ожидание.
    
    \item \textbf{Второй момент} ($k=2$): $\mu_2 = E[X^2]$.
    
    \item \textbf{Центральный момент $k$-го порядка}:
    $$
    \mu_k' = E[(X - E[X])^k]
    $$
    
    \item \textbf{Второй центральный момент}: $\mu_2' = E[(X - E[X])^2] = \text{Var}(X)$ — дисперсия.
\end{itemize}

## Выборочные моменты

\begin{itemize}
    \item Для случайной выборки $X_1, \ldots, X_n$ определяем \textbf{выборочные моменты}:
    
    \item \textbf{Выборочный момент $k$-го порядка}:
    $$
    m_k = \frac{1}{n}\sum_{i=1}^{n} X_i^k
    $$
    
    \item \textbf{Выборочный центральный момент $k$-го порядка}:
    $$
    m_k' = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^k
    $$
    
    \item Выборочные моменты являются оценками соответствующих теоретических моментов.
\end{itemize}


## Метод моментов

\begin{itemize}
    \item \textbf{Идея метода моментов}: приравнять выборочные моменты к теоретическим моментам распределения.
    
    \item Если распределение зависит от $p$ параметров, используем первые $p$ моментов.
\end{itemize}

:::{.callout-definition}
**Метод моментов** для оценки параметров:

\begin{enumerate}
    \item Выразить теоретические моменты через неизвестные параметры.
    
    \item Приравнять выборочные моменты к теоретическим:
    $$
    m_k = \mu_k(\theta_1, \ldots, \theta_p), \quad k = 1, 2, \ldots, p
    $$
    
    \item Решить систему уравнений относительно параметров $\theta_1, \ldots, \theta_p$.
\end{enumerate}
:::

## Пример: Метод моментов для экспоненциального распределения

\begin{itemize}
    \item Пусть $X_1, \ldots, X_n \sim \text{Exp}(\lambda)$ — время до события (например, время до поломки устройства).
    
    \item Нужно оценить параметр $\lambda$ (интенсивность).
    
    \item \textbf{Шаг 1}: Теоретический момент первого порядка:
    $$
    \mu_1 = E[X] = \frac{1}{\lambda}
    $$
    
    \item \textbf{Шаг 2}: Выборочный момент первого порядка:
    $$
    m_1 = \bar{X}
    $$
    
    \item \textbf{Шаг 3}: Приравниваем и выражаем параметр как оценку:
    $$
    \bar{X} = \frac{1}{\lambda} \quad \Rightarrow \quad \hat{\lambda}_{MM} = \frac{1}{\bar{X}}
    $$
\end{itemize}

## Пример: Метод моментов для равномерного распределения

\begin{itemize}
    \item Пусть $X_1, \ldots, X_n \sim \text{Uniform}(0, \theta)$ — равномерное распределение на интервале $[0, \theta]$.
    
    \item Нужно оценить параметр $\theta$ (верхнюю границу интервала).
    
    \item \textbf{Шаг 1}: Теоретический момент первого порядка:
    $$
    \mu_1 = E[X] = \frac{0 + \theta}{2} = \frac{\theta}{2}
    $$
    
    \item \textbf{Шаг 2}: Выборочный момент первого порядка:
    $$
    m_1 = \bar{X}
    $$
    
    \item \textbf{Шаг 3}: Приравниваем и выражаем параметр как оценку:
    $$
    \bar{X} = \frac{\theta}{2} \quad \Rightarrow \quad \hat{\theta}_{MM} = 2\bar{X}
    $$
    
    \item \textbf{Интуиция}: Если среднее значение равно $\frac{\theta}{2}$, то верхняя граница $\theta$ в два раза больше среднего.
\end{itemize}

## Пример: Метод моментов для нормального распределения

\begin{itemize}
    \item Пусть $X_1, \ldots, X_n \sim \mathcal{N}(\mu, \sigma^2)$ — нужно оценить $\mu$ и $\sigma^2$.
    
    \item \textbf{Шаг 1}: Теоретические моменты:
    \begin{align*}
    \mu_1 &= E[X] = \mu \\
    \mu_2 &= E[X^2] = \text{Var}(X) + (E[X])^2 = \sigma^2 + \mu^2
    \end{align*}
    
    \item \textbf{Шаг 2}: Выборочные моменты:
    \begin{align*}
    m_1 &= \frac{1}{n}\sum_{i=1}^{n} X_i = \bar{X} \\
    m_2 &= \frac{1}{n}\sum_{i=1}^{n} X_i^2
    \end{align*}
\end{itemize}

---

## Пример: Метод моментов для нормального распределения

\begin{itemize}
    \item \textbf{Шаг 3}: Приравниваем:
    \begin{align*}
    \bar{X} &= \mu \\
    \frac{1}{n}\sum_{i=1}^{n} X_i^2 &= \sigma^2 + \mu^2
    \end{align*}
    
    \item \textbf{Решение}:
    \begin{align*}
    \hat{\mu}_{MM} &= \bar{X} \\
    \hat{\sigma}^2_{MM} &= \frac{1}{n}\sum_{i=1}^{n} X_i^2 - \bar{X}^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2
    \end{align*}
    
    \item \textbf{Замечание}: Оценка дисперсии методом моментов — это смещенная оценка $S_n^2$!
\end{itemize}

## Доверительные интервалы
\begin{itemize}
    \item Использование только точечной оценки для оценки параметра — это как ловить рыбу в мутном озере гарпуном, а использование доверительного интервала — как ловить сетью. Мы можем бросить гарпун туда, где увидели рыбу, но скорее всего промахнемся. Если мы закинем сеть в эту область, у нас будет больше шансов, что рыбалка будет успешна.
    
    \item Если мы делаем точечную оценку, мы, вероятно, не попадем точно в неизвестный параметр. Если мы используем диапазон правдоподобных значений — доверительный интервал — у нас есть хороший шанс "поймать" параметр.
    
    \item Действительно, если наша точечная оценка $\hat{\theta}$ имеет непрерывное распределение, то $P_{\theta}\{\hat{\theta} = \theta \} = 0$.
\end{itemize}

## Доверительные интервалы

:::{.callout-definition}
**Доверительный интервал**. Пусть
$X_1 , X_2 , \ldots , X_n$ — случайная выборка случайной величины $X$. Пусть задано $0 < \alpha < 1$. Пусть
$L = L(X_1 , X_2 , \ldots , X_n)$ и
$U = U(X_1 , X_2 , \ldots , X_n)$ — две статистики. Мы говорим, что
интервал $(L, U)$ является $(1 - \alpha) \cdot 100\%$ доверительным интервалом для
неизвестного параметра $\theta$, если
$$
    1 -\alpha = P_{\theta}\{ \theta \in (L, U) \}.
$$

Вероятность того, что интервал включает $\theta$, равна $1 - \alpha$,
которая называется **уровнем доверия** интервала.
:::

## Доверительные интервалы
### Иллюстративный пример

Для выборки $X_1, \ldots, X_4$ из $\mathcal{N}(\mu, 1)$ интервальная оценка $\mu$ — это, например, $[\bar{X}-1, \bar{X}+1]$. Найдите вероятность того, что истинный параметр $\mu$ покрывается этим интервалом.

:::{.callout-solution}
## Решение

$P \left( \bar{X}-1 < \mu < \bar{X}+1 \right) = P \left( -1 < \mu - \bar{X} < 1 \right) =
P \left( -1 < \bar{X} - \mu < 1 \right)$

Знаем, что $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \equiv \mathcal{N}\left(\mu, \frac{1}{4}\right)$, приводим к стандартному нормальному распределению:

\begin{gather*}
P \left( -1 < \bar{X} - \mu < 1 \right) = P \left( \frac{-1}{\frac{\sigma}{\sqrt{n}}} < \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} < \frac{1}{\frac{\sigma}{\sqrt{n}}} \right) = \\
P \left( \frac{-1}{\frac{1}{2}} < Z < \frac{1}{\frac{1}{2}} \right) = P \left( -2 < Z < 2 \right) \approx 0.9545
\end{gather*}
:::

## Действие доверительных интервалов

- Некоторые доверительные интервалы включают в себя $\theta$, некоторые нет. Доверительный интервал поймает параметр с вероятностью $1-\alpha$.

\begin{center}
\begin{tikzpicture}[scale=1.2]
    % Ось
    \draw[->, thick] (0,0) -- (10,0) node[right] {$\mathbb{R}$};
    
    % Деления на оси
    \foreach \x in {1,2,...,9} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\small $\x$};
    }
    
    % Серый полупрозрачный фон (туман неопределенности)
    \fill[gray!85, opacity=0.85] (0,-0.5) rectangle (10,0.5);
    
    % Реальный параметр (скрыт в тумане, без подписи)
    \draw[fill=blue] (3,0) circle (2pt);
        
    % Доверительные интервалы (эллипсы)
    % Интервалы, захватывающие параметр (зеленые, центрированы на оценке)
    \draw[green!70!black, very thick] (3.2,0) ellipse (0.5 and 0.15);
    \draw[green!70!black, very thick, dashed] (3.2,0) ellipse (0.8 and 0.12);
    
    % Интервалы, не захватывающие параметр справа (красные)
    \draw[red!70!black, very thick] (4.4,0) ellipse (0.4 and 0.15);
    \draw[red!70!black, very thick, dashed] (5.0,0) ellipse (0.5 and 0.12);
    \draw[red!70!black, very thick] (5.5,0) ellipse (0.35 and 0.13);
    
    % Интервалы, не захватывающие параметр слева (красные)
    \draw[red!70!black, very thick] (1.2,0) ellipse (0.4 and 0.15);
    \draw[red!70!black, very thick, dashed] (0.8,0) ellipse (0.35 and 0.12);
    \draw[red!70!black, very thick] (1.8,0) ellipse (0.3 and 0.13);
    
    % Текст о неопределенности и легенда в одну строку
    \node[above=25pt, text width=9cm, align=center] at (5,0) 
        {\small \textcolor{green!70!black}{$\bullet$} поймал \textcolor{red!70!black}{$\bullet$} не поймал};
\end{tikzpicture}
\end{center}

## Доверительные интервалы для среднего генеральной совокупности
### Если дисперсия генеральной совокупности известна
\begin{itemize}
    \item Нам нужно: случайная выборка размера $n$, дисперсия $\sigma^2 \equiv Var[X_i]$ известна \textit{a priori}.
    
    \item Утверждение состоит в том, что мы хотим, чтобы наш доверительный интервал $(L,U)$ покрывал неизвестное среднее генеральной совокупности $\mu$ с вероятностью $1-\alpha$:
    $$
    1 - \alpha = P(L(X) < \mu < U(X)) = P(-U < -\mu < -L)
    $$
    
    \item Внедряем в центральную часть неравенства известную случайную величину путём одновременного изменения всех частей неравенства:
    \begin{equation*}
    1 - \alpha = P\left( \colorbox{green!20}{$\frac{\bar{X} - U}{\frac{\sigma}{\sqrt{n}}}$} < \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} < \colorbox{red!20}{$\frac{\bar{X} -L}{\frac{\sigma}{\sqrt{n}}}$} \right)
    \end{equation*}
    
    \item Обычно интервалы хотят делать симметричными, поэтому делаем симметричную замену переменных:
    \begin{equation*}
    1 - \alpha = P\left(\colorbox{green!20}{$-z_{\alpha / 2}$} < Z < \colorbox{red!20}{$z_{\alpha / 2}$} \right)
    \end{equation*}
\end{itemize}


## Доверительные интервалы для среднего генеральной совокупности
### Если дисперсия генеральной совокупности известна
\begin{itemize}
    \item После нахождения критической точки $z_{\alpha / 2}$, такой, что $P(Z > z_{\alpha / 2}) = \frac{\alpha}{2}$, выполняем обратную замену и восстанавливаем нужные границы:
    \begin{gather*}
    z_{\alpha / 2} = \frac{\bar{X} - L}{\frac{\sigma}{\sqrt{n}}} \rightarrow L = \bar{X} - z_{\alpha / 2} \frac{\sigma}{\sqrt{n}} \\
    -z_{\alpha / 2} = \frac{\bar{X} - U}{\frac{\sigma}{\sqrt{n}}} \rightarrow U = \bar{X} + z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}
    \end{gather*}
    
    \item В итоге получаем теоретический $(1-\alpha) 100\%$ доверительный интервал для среднего генеральной совокупности $\mu$:
    $$
    \mu \in \left(\bar{X} - z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}, \bar{X} + z_{\alpha / 2} \frac{\sigma}{\sqrt{n}} \right)
    $$
\end{itemize}

## Доверительные интервалы для среднего генеральной совокупности
### Если дисперсия генеральной совокупности известна

\begin{itemize}
    \item Однако на практике $(1-\alpha)100\%$ доверительный интервал для среднего генеральной совокупности $\mu$ записывается как:
    $$
    \mu \in \left(\bar{x} - z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}, \bar{x} + z_{\alpha / 2} \frac{\sigma}{\sqrt{n}} \right)
    $$
    
    \item Отличие лишь в одной букве: $\bar{x}$ вместо $\bar{X}$ — конечно, потому что на практике у нас есть именно \textbf{реализация} выборочного среднего, те данные, что нам удалось собрать. Вокруг них и строим интервал.
\end{itemize}
