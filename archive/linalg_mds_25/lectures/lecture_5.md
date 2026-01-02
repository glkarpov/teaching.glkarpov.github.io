---
title: "Линейная алгебра"
subtitle: "Замена базиса как линейное отображение. Построение матрицы линейного отображения."
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
## Линейные отображения и векторные пространства
### Минимальная визуализация

\begin{center}
\begin{tikzpicture}
    % Top notation
    \node[above] at (2.5,2.5) {$\varphi: \mathbb{V} \longrightarrow \mathbb{W}$};
    
    % V set with three elements
    \draw[thick, fill=blue!10] (0,0) circle (1.2);
    \node[above] at (0,1.4) {$\mathbb{V}$};
    \node[below] at (0,-1.5) {Basis $B = \{v_1, \,v_2\}$};
    
    % Elements in V
    \fill[red] (-0.2,0.5) circle (2pt);
    \node[left] at (-0.3,0.5) {$x$};
    
    \fill[green] (-0.2,-0.4) circle (2pt);
    \node[below] at (-0.2,-0.5) {$v_1$};
    
    \fill[blue] (0.4,0.2) circle (2pt);
    \node[below] at (0.4,0.1) {$v_2$};

    % W set with five elements (larger circle)
    \draw[thick, fill=green!10] (5,0) circle (1.8);
    \node[above] at (5,2.0) {$\mathbb{W}$};
    \node[below] at (5,-2.2) {Basis $C = \{\omega_1, \,\omega_2\}$};
    
    % Elements in W
    \fill[red] (4.5,1.0) circle (2pt);
    \node[right] at (4.5,1.0) {$\varphi(x)$};
    
    \fill[green] (4.8,-1.3) circle (2pt);
    \node[right] at (4.9,-1.3) {$\varphi(v_1)$};
    
    \fill[blue] (4.3,0.2) circle (2pt);
    \node[right] at (4.4,0.2) {$\varphi(v_2)$};
    
    \fill[brown] (4.2,-0.8) circle (2pt);
    \node[left] at (4.1,-0.8) {$\omega_1$};
    
    \fill[orange] (5.8,-0.8) circle (2pt);
    \node[right] at (5.9,-0.8) {$\omega_2$};
  
    % Arrows connecting elements
    \draw[thick, ->] (-0.1,0.5) .. controls (2.5, 1.0) .. (4.3,1.0);
    \draw[thick, ->] (-0.1,-0.4) .. controls (1.5, -0.8) and (3.0,-1.0) .. (4.6,-1.3);
    \draw[thick, ->] (0.5,0.2) .. controls (2.8, 0.1) .. (4.1,0.2);
\end{tikzpicture}
\end{center}

## Замена базиса сквозь призму линейного отображения

Давайте рассмотрим самое глупенькое отображение, которое не делает ничего, кроме как находит копию элемента (identity transformation, тождественное преобразование):


\begin{center}
\begin{minipage}{0.6\textwidth}
\begin{align*}
    \varphi: \mathbb{V} \longrightarrow \mathbb{W}, \; \mathbb{W} = \mathbb{V}, \\
    \text{such that } \forall x \in \mathbb{V} \, \varphi(x) = x \in \mathbb{W}
\end{align*}
\begin{tikzpicture}
    \draw[thick, fill=blue!10] (0,0) circle (1.0);
    \node[above] at (0,1.2) {$\mathbb{V}$};
    \node at (0,-0.3) {$[x]_B$};
    \fill[red] (0,0) circle (2pt);

    \draw[thick, fill=green!10] (4,0) circle (1.0);
    \node[above] at (4,1.2) {$\mathbb{W}$};
    \node at (4,-0.3) {$[x]_C$};
    \fill[red] (4,0) circle (2pt);
  
    \draw[thick, ->] (1.1,0.4) .. controls (2, 0.7) and (2,0.7) .. (2.9,0.4) node[midway, above] {$\varphi$};

    \node at (2,0) {$\mathbb{V} = \mathbb{W}$};
\end{tikzpicture}
\end{minipage}
\hfill
\begin{minipage}{0.35\textwidth}
\begin{center}
\includegraphics[width=0.8\textwidth]{actions_meme.jpeg}
\end{center}
\end{minipage}
\end{center}

Пусть в пространстве $\mathbb{V}$ у нас действует базис $B = \{v_1, v_2\}$, а в пространстве $\mathbb{W}$ действует базис $C = \{ \omega_1, \omega_2 \}$.

## Замена базиса сквозь призму линейного отображения

$$
    x = x_1 v_1 + x_2 v_2,
$$
$$
   \varphi(x) = \varphi(x_1 v_1 + x_2 v_2) = x_1 \varphi(v_1) + x_2 \varphi(v_2).
$$

Помните, что $\varphi(v_1)$, $\varphi(v_2)$ — это \textit{векторы}, \textit{т.е.} абстрактные элементы векторного пространства $W$.

## Замена базиса сквозь призму линейного отображения
Давайте посмотрим на элементы $\varphi(v_1)$, $\varphi(v_2)$ в базисе $C$:

\begin{gather*}
\varphi(v_{\textcolor{red}{1}}) = v_{\textcolor{red}{1}} = a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \omega_{\textcolor{violet}{2}}, \; [v_{\textcolor{red}{1}}]_C = \vtwo{a_{\textcolor{violet}{1}\textcolor{red}{1}}}{a_{\textcolor{violet}{2}\textcolor{red}{1}}} \\
\varphi(v_{\textcolor{red}{2}}) = v_{\textcolor{red}{2}} = a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \omega_{\textcolor{violet}{2}}, \; [v_{\textcolor{red}{2}}]_C = \vtwo{a_{\textcolor{violet}{1}\textcolor{red}{2}}}{a_{\textcolor{violet}{2}\textcolor{red}{2}}}\\
\end{gather*}

\vspace{-5mm}

Теперь вернемся к $\varphi(x) = x_{\textcolor{red}{1}} \varphi(v_{\textcolor{red}{1}}) + x_{\textcolor{red}{2}} \varphi(v_{\textcolor{red}{2}}) \Longleftrightarrow x = x_{\textcolor{red}{1}} v_{\textcolor{red}{1}} + x_{\textcolor{red}{2}} v_{\textcolor{red}{2}}$.

\begin{align*}
\varphi(x) = x = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \omega_{\textcolor{violet}{2}} \right) & + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \omega_{\textcolor{violet}{2}} \right) =\\
\left(a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} \right) \omega_{\textcolor{violet}{1}} & + \left( a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}} \right) \omega_{\textcolor{violet}{2}} = \gamma_1 \omega_{\textcolor{violet}{1}} + \gamma_2 \omega_{\textcolor{violet}{2}} 
\end{align*}

- Мы получили разложение элемента $\varphi(x) = x$ по базису пространства $\mathbb{W}$. Можем записать координаты как:

\begin{equation*}
    \left[ \varphi(x) \right]_C = \left[ x \right]_C = \vtwo{\gamma_1}{\gamma_2} = \vtwo{a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}}}{a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}}}
\end{equation*}

## Умножение матрицы на вектор... снова...
Наконец:
$$
    \left[ x \right]_{C} = 
    \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}} & a_{\textcolor{violet}{1} \textcolor{red}{2}} \\
        a_{\textcolor{violet}{2}\textcolor{red}{1}} & a_{\textcolor{violet}{2} \textcolor{red}{2}} \\
    \end{pmatrix}
    \begin{pmatrix}
        x_{\textcolor{red}{1}}\\
        x_{\textcolor{red}{2}}
    \end{pmatrix} = A_{B \rightarrow C} \left[x \right]_{B}.
$$


::: {.callout-tip}
## Матрица замены координат
Матрица для identity transformation помогает нам связать координаты одного и того же элемента $x$ в двух разных базисах. Эту формулу также называют формулой замены координат.


Если у нас есть два базиса $B = \{v_1, v_2, \ldots, v_n\}$ и $C = \{\omega_1, \omega_2, \ldots, \omega_n\}$, то матрица замены координат $A_{B \rightarrow C}$ строится как:

$$
    A_{B \rightarrow C} = \begin{pmatrix} | & | & \cdots & | \\ [v_1]_C & [v_2]_C & \cdots & [v_n]_C \\ | & | & \cdots & | \end{pmatrix},
$$

где $[v_i]_C$ — это координаты вектора $v_i$ в базисе $C$.
:::

## Примеры

