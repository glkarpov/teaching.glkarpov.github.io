---
title: "Теория вероятностей и математическая статистика"
subtitle: "Точечные оценки."
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

## Напоминание: задачи статистики

\begin{itemize}
    \item Случайные процессы вокруг нас — чёрные ящики — случайные генераторы. Мы хотим "расшифровать" один такой ящик и выяснить его параметры и/или свойства, например, математическое ожидание и дисперсию. Для этого мы наблюдаем случайную величину некоторое количество раз и затем делаем выводы на основе накопленной информации.
    
    \item Параметры случайной величины — числа, \textbf{точки} на числовой оси. Процесс угадывания этих значений обычно называется \textbf{точечной оценкой}, то есть мы хотим эти точки на числовой оси как можно ближе угадать.
\end{itemize}

## Точечные оценки

\begin{itemize}
    \item \textbf{Оценка} — это специальная статистика, функция от случайной выборки. Её реализация может быть использована в качестве кандидата-значения, \textbf{предположения} о значении какого-либо параметра неизвестной случайной величины.
    
    \item Пусть $\theta$ — неизвестный параметр случайной величины (например, $\mu$ или $\sigma^2$). Тогда оценка: $
    \hat{\theta} = \hat{\theta}(X_1, \ldots, X_n)$, функция от случайной выборки, тоже является случайной величиной. 
    
    \item \textbf{Реализация оценки} — конкретное числовое значение, полученное из конкретного наблюдения выборки.
\end{itemize}

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
    
    % Подпись оси
    \node[below=15pt] at (5,0) {Характеристики / параметры случайной величины $X$};
\end{tikzpicture}
\end{center}

### Реальная ситуация: характеристики и параметры неизвестны

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
    \item На основе реализации случайной выборки $x_1, x_2, \ldots, x_n$ получить \textbf{предположения} $\hat{\theta}$ для скрытых в тумане реальности параметров
    
    \item Идея состоит в том, чтобы посчитать значение оценки на реальных имеющихся данных, и чтобы полученное число было бы как можно ближе к истинным значениям параметров
    
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

## Смещенность и несмещенность

:::{.callout-definition}
Оценка $\hat{\theta}$ называется **несмещенной**, если:
$$
E[\hat{\theta}] = \theta
$$

Оценка $\hat{\theta}$ называется **смещенной**, если:
$$
E[\hat{\theta}] \neq \theta
$$

**Смещение** (bias) определяется как:
$$
\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta
$$
:::

## Среднеквадратичная ошибка (MSE)

:::{.callout-definition}
**Среднеквадратичная ошибка** (Mean Squared Error, MSE) оценки $\hat{\theta}$ определяется как:
$$
\text{MSE}(\hat{\theta}) = E[(\hat{\theta} - \theta)^2]
$$
:::

\begin{itemize}
    \item MSE измеряет средний квадрат отклонения оценки от истинного значения параметра.
    
    \item \textbf{Разложение MSE}:
    $$
    \text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + [\text{Bias}(\hat{\theta})]^2
    $$
    
    \item MSE учитывает как дисперсию оценки, так и её смещение, и является неким "мерилом" качества точечной оценки. Чем меньше MSE, тем лучше работает точечная оценка.
\end{itemize}

## Разложение MSE

\begin{itemize}
    \item Докажем формулу разложения:
    \begin{align*}
    \text{MSE}(\hat{\theta}) &= E[(\hat{\theta} - \theta)^2] \\
    &= E[(\hat{\theta} - E[\hat{\theta}] + E[\hat{\theta}] - \theta)^2] \\
    &= E[(\hat{\theta} - E[\hat{\theta}])^2] + 2E[(\hat{\theta} - E[\hat{\theta}])(E[\hat{\theta}] - \theta)] + E[(E[\hat{\theta}] - \theta)^2]
    \end{align*}
    
    \item Второе слагаемое равно нулю, так как $E[\hat{\theta}] - \theta$ — константа.
    
    \item Получаем:
    $$
    \text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + (E[\hat{\theta}] - \theta)^2 = \text{Var}(\hat{\theta}) + [\text{Bias}(\hat{\theta})]^2
    $$
\end{itemize}

## Состоятельность оценки

:::{.callout-definition}
Оценка $\hat{\theta}$ называется **состоятельной**, если при увеличении размера выборки $n \to \infty$ оценка "сходится" к истинному значению параметра $\theta$.
:::

\begin{itemize}
    \item \textbf{Интуиция}: Чем больше данных мы собираем, тем точнее становится наша оценка, тем ближе "в тумане" мы находим значения параметров.
    
    \item При $n \to \infty$ оценка должна становиться сколь угодно близкой к истинному значению параметра.
    
    \item \textbf{Важно}: Состоятельность — это асимптотическое свойство (при больших выборках).

    \item \textbf{Связь с несмещённостью}: Несмещённая оценка с дисперсией, стремящейся к нулю при $n \to \infty$, является состоятельной.
    
    \item Заметим, что состоятельная оценка может быть смещённой для малых выборок, но смещение должно исчезать при росте $n$.
\end{itemize}

---

## Свойства основных оценок

Для всех последующих примеров предположим, что у нас есть случайная выборка $\mathcal{X} = (X_1, X_2, \ldots, X_n)$ (Независимые, одинаково распределенные) с $\mu \equiv E[X_i]$, $\sigma^2 \equiv Var[X_i]$.

### Выборочное среднее $\bar{X}$

\begin{itemize}
    \item Выборочное среднее $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$ является оценкой неизвестного математического ожидания $\mu$ для исследуемой случайной величины.

    \item Проверим несмещенность:
    $$
    E[\bar{X}] = E\left[\frac{1}{n}\sum_{i=1}^{n} X_i\right] = \frac{1}{n}\sum_{i=1}^{n} E[X_i] = \frac{1}{n} \cdot n \cdot \mu = \mu
    $$
    
    \item \textbf{Вывод}: $\bar{X}$ — \textbf{несмещенная} оценка $\mu$.
    
    \item Проверим состоятельность. Дисперсия выборочного среднего:
    $$
    \text{Var}(\bar{X}) = \text{Var}\left(\frac{1}{n}\sum_{i=1}^{n} X_i\right) = \frac{1}{n^2}\sum_{i=1}^{n} \text{Var}(X_i) = \frac{1}{n^2} \cdot n \cdot \sigma^2 = \frac{\sigma^2}{n}
    $$
    
    \item При $n \to \infty$ имеем $\text{Var}(\bar{X}) = \frac{\sigma^2}{n} \to 0$.
    
    \item \textbf{Вывод}: $\bar{X}$ — \textbf{состоятельная} оценка $\mu$ (несмещённая с дисперсией, стремящейся к нулю).
\end{itemize}

## Свойства основных оценок
### Выборочная дисперсия c делением на $n-1$
Выборочная дисперсия $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$ является оценкой дисперсии для исследуемой случайной величины.
\begin{itemize}    
    \item Используем факт: $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ (хи-квадрат с $n-1$ степенями свободы). Для такой хи-квадрат случайной величины:
    $$
        E[\chi^2_{n-1}] = n-1, \quad \text{Var}(\chi^2_{n-1}) = 2(n-1)
    $$
    
    \item Проверим несмещённость:
    $$
    E\left[\frac{(n-1)S^2}{\sigma^2}\right] = n-1 \Rightarrow E[S^2] = \sigma^2
    $$
    
    \item \textbf{Вывод}: $S^2$ — \textbf{несмещенная} оценка для $\sigma^2$.
    
    \item Проверим состоятельность. Дисперсия $S^2$:
    $$
    \text{Var}\left(\frac{(n-1)S^2}{\sigma^2}\right) = 2(n-1) \Rightarrow \text{Var}(S^2) = \frac{2\sigma^4}{n-1} \xrightarrow{n \to \infty} 0
    $$
    
    \item \textbf{Вывод}: $S^2$ — \textbf{состоятельная} оценка для $\sigma^2$ (несмещённая с дисперсией, стремящейся к нулю).
\end{itemize}

## Свойства основных оценок
### Выборочная дисперсия c делением на $n$
Рассмотрим другой вариант оценки дисперсии: $S_n^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2$.
\begin{itemize}    
    \item Связь с несмещенной $S^2$:
    $$
        S_n^2 = \frac{n-1}{n} S^2 = \frac{n-1}{n}\frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2 = S_n^2
    $$
    
    \item Используя $E[S^2] = \sigma^2$, получаем:
    $$
    E[S_n^2] = E\left[\frac{n-1}{n} S^2\right] = \frac{n-1}{n} E[S^2] = \frac{n-1}{n}\sigma^2 \neq \sigma^2
    $$
    
    \item \textbf{Вывод}: $S_n^2$ — \textbf{смещенная} оценка $\sigma^2$.
    
    \item Вычислим смещение:
    $$
    \text{Bias}(S_n^2) = E[S_n^2] - \sigma^2 = \frac{n-1}{n}\sigma^2 - \sigma^2 = \frac{n-1-n}{n}\sigma^2 = -\frac{\sigma^2}{n}
    $$
\end{itemize}

## Свойства основных оценок
### Выборочная дисперсия c делением на $n$

\begin{itemize}
\item Проверим состоятельность. Дисперсия $S_n^2$:
    $$
    \text{Var}(S_n^2) = \text{Var}\left(\frac{n-1}{n} S^2\right) = \left(\frac{n-1}{n}\right)^2 \text{Var}(S^2) = \left(\frac{n-1}{n}\right)^2 \cdot \frac{2\sigma^4}{n-1} = \frac{2(n-1)\sigma^4}{n^2}
    $$
    
    \item При $n \to \infty$ смещение стремится к нулю:
    $$
    \lim_{n \to \infty} \text{Bias}(S_n^2) = \lim_{n \to \infty} \left(-\frac{\sigma^2}{n}\right) = 0
    $$
    
    \item И дисперсия стремится к нулю:
    $$
    \lim_{n \to \infty} \text{Var}(S_n^2) = \lim_{n \to \infty} \frac{2(n-1)\sigma^4}{n^2} = 0
    $$
    
    \item \textbf{Вывод}: $S_n^2$ — \textbf{состоятельная} оценка $\sigma^2$ (смещение стремится к нулю при росте выборки).
\end{itemize}
