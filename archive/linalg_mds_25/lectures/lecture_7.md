---
title: "Линейная алгебра"
subtitle: "Построение матрицы линейного отображения. Изменение матрицы при изменении базисов."
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
### Действующие лица

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

## Напоминание: построение матрицы линейного отображения

- Для определения значения функции нам необходимо только знать значения функции от базисных векторов: $\varphi(x) = \varphi(x_1 v_1 + x_2 v_2) = x_1 \colorbox{red!60}{\ensuremath{\varphi(v_1)}} + x_2 \colorbox{red!60}{\ensuremath{\varphi(v_2)}}$

- Образы базисных векторов возможно разложить по базису в пространстве $\mathbb{W}$:
\begin{align*}
    \varphi(v_{\textcolor{red}{1}}) & = a_{1\textcolor{red}{1}} \omega_{1} + a_{2\textcolor{red}{1}} \omega_{2}, \, [ \varphi(v_{\textcolor{red}{1}}) ]_C = \vtwo{a_{1\textcolor{red}{1}}}{a_{2\textcolor{red}{1}}} \\
    \varphi(v_{\textcolor{red}{2}}) & = a_{1\textcolor{red}{2}} \omega_{1} + a_{2\textcolor{red}{2}} \omega_{2}, \, [ \varphi(v_{\textcolor{red}{2}}) ]_C = \vtwo{a_{1\textcolor{red}{2}}}{a_{2\textcolor{red}{2}}} 
\end{align*}

- В результате получаем разложение $\varphi(x)$ по базису в пространстве $\mathbb{W}$: $\varphi(x) = \gamma_1 \omega_{\textcolor{violet}{1}} + \gamma_2 \omega_{\textcolor{violet}{2}}$, где:
\begin{gather*}
\left[ \varphi(x) \right]_C = \vtwo{\gamma_1}{\gamma_2} =
\begin{pmatrix}
    a_{\textcolor{violet}{1}\textcolor{red}{1}} & a_{\textcolor{violet}{1} \textcolor{red}{2}} \\
    a_{\textcolor{violet}{2}\textcolor{red}{1}} & a_{\textcolor{violet}{2} \textcolor{red}{2}} \\
\end{pmatrix}
    \begin{pmatrix}
        x_{\textcolor{red}{1}}\\
        x_{\textcolor{red}{2}}
    \end{pmatrix} = \colorbox{green!50}{$L_{\varphi, \,(B,C)} \left[x \right]_{B}$}
\end{gather*}

## Устройство матрицы линейного отображения

\begin{itemize}
    \item Если обобщать наш игрушечный пример, то 
    $$
        L_{\varphi, \,(B,C)} = \begin{pmatrix} | & | & \cdots & | \\ [\varphi(v_1)]_C & [\varphi(v_2)]_C & \cdots & [\varphi(v_n)]_C \\ | & | & \cdots & | \end{pmatrix}, \; L_{\varphi, \,(B,C)} \in \mathbb{R}^{m \times n},
    $$

    где $[\varphi(v_i)]_C$ — это координаты образа базисного вектора $v_i$ в базисе $C$.

    \item Базис $B = \{ v_1, \ldots ,v_n \}$ действует в области определения (пространстве аргументов) функции $\mathbb{V}$, базис $C = \{ \omega_1, \ldots , \omega_m \}$ действует в пространстве значений функции $\mathbb{W}$.
\end{itemize}

## Случай стандартных базисов

\begin{center}
\begin{tikzpicture}[scale=0.7]
    % Top notation
    \node[above] at (2.5,2.5) {$\varphi: \mathbb{V} \longrightarrow \mathbb{W}$};
    
    % V set with three elements
    \draw[thick, fill=blue!10] (0,0) circle (1.2);
    \node[above] at (0,1.4) {$\mathbb{V}$};
    \node[below] at (0,-1.5) {Basis $S^v = \{s^v_1, \,s^v_2\}$};
    
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
    \node[below] at (5,-2.2) {Basis $S^w = \{s^w_1, \,s^w_2\}$};
    
    % Elements in W
    \fill[red] (4.5,1.0) circle (2pt);
    \node[right] at (4.5,1.0) {$\varphi(x)$};
    
    \fill[green] (4.8,-1.3) circle (2pt);
    \node[right] at (4.9,-1.3) {$\varphi(s^v_1)$};
    
    \fill[blue] (4.3,0.2) circle (2pt);
    \node[right] at (4.4,0.2) {$\varphi(s^v_2)$};
    
    \fill[brown] (4.2,-0.8) circle (2pt);
    \node[left] at (4.1,-0.8) {$s^w_1$};
    
    \fill[orange] (5.8,-0.8) circle (2pt);
    \node[right] at (5.9,-0.8) {$s^w_2$};
  
    % Arrows connecting elements
    \draw[thick, ->] (-0.1,0.5) .. controls (2.5, 1.0) .. (4.3,1.0);
    \draw[thick, ->] (-0.1,-0.4) .. controls (1.5, -0.8) and (3.0,-1.0) .. (4.6,-1.3);
    \draw[thick, ->] (0.5,0.2) .. controls (2.8, 0.1) .. (4.1,0.2);
\end{tikzpicture}
\end{center}

- В случае стандартных базисов получаем 
$$
    L_{\varphi} = \begin{pmatrix} | & | & \cdots & | \\ [\varphi(s^v_1)] & [\varphi(s^v_2)] & \cdots & [\varphi(s^v_n)] \\ | & | & \cdots & | \end{pmatrix},
$$

где $[\varphi(s^v_i)]$ — это координаты образа базисного вектора $s^v_i$ в стандартном базисе $S^{w}$ в пространстве $\mathbb{W}$.

## Чувствительность матрицы к выбору пары базисов
### Пример

- Построенная матрица линейного преобразования крайне хрупка. По факту она работает только с теми базисами, которые были выбраны при ее построении.

- Пример: $\varphi: \mathbb{R}^2 \longrightarrow \mathbb{R}^2, \; \varphi \vtwo{x_1}{x_2} = \vtwo{x_1 + x_2}{2x_2 - x_1}$


## Изменение матрицы отображения при изменении базисов пространств

\begin{center}
\begin{tikzpicture}[scale=0.7]
    % Top notation
    \node[above] at (2.0,3.5) {$\varphi: \mathbb{V} \longrightarrow \mathbb{W}$};

    % Upper V set (standard basis)
    \draw[thick, fill=blue!10] (-2.0,2) circle (1.2);
    \node[above] at (-2.0,3.5) {$\mathbb{V}$};
    \node[above left] at (-3.2,2.5) {Basis $S^v$};
    
    % Upper W set (standard basis)
    \draw[thick, fill=green!10] (7.5,2) circle (1.2);
    \node[above] at (7.5,3.5) {$\mathbb{W}$};
    \node[above right] at (8.7,2.5) {Basis $S^w$};
    
    % Lower V set (basis B)
    \draw[thick, fill=blue!10] (-2.0,-3.5) circle (1.2);
    \node[left] at (-3.4,-3.5) {$\mathbb{V}$};
    \node[below] at (-2.0,-5.0) {Basis $B = \{v_1, \ldots, v_n\}$};
    
    % Lower W set (basis C)
    \draw[thick, fill=green!10] (7.5,-3.5) circle (1.2);
    \node[right] at (8.9,-3.5) {$\mathbb{W}$};
    \node[below] at (7.5,-5.0) {Basis $C = \{\omega_1, \ldots, \omega_m\}$};
    
    % Arrow from upper V to upper W
    \draw[thick, ->] (-0.8,2) -- (6.3,2);
    \node[above] at (2.75,2.3) {$[\varphi(x)] = L_{\varphi} [x]$};
    
    % Arrow from lower V to lower W
    \draw[thick, ->] (-0.8,-3.5) -- (6.3,-3.5);
    \node[below] at (2.75,-3.7) {$[\varphi(x)]_C = L_{\varphi, \,(B,C)} [x]_B$};
    
    % Curved arrows from upper to lower sets
    \draw[thick, ->] (-2.5,-2.3) .. controls (-3.6,-0.9) .. (-2.5,0.8);
    \node[left] at (-3.3, 0.0) {$[x] = B [x]_B$};
    \draw[thick, ->] (-1.5,0.8) .. controls (-0.4,-0.9) .. (-1.5,-2.3);
    \node[right] at (-0.7,-1.9) {$[x]_B = B^{-1} [x]$};

    \draw[thick, ->] (7.0,-2.3) .. controls (5.9,-0.9) .. (7.0,0.8);
    \node[left] at (6.2,0.0) {$[y] = C [y]_C$};
    \draw[thick, ->] (8.0,0.8) .. controls (9.1,-0.9) .. (8.0,-2.3);
    \node[right] at (8.8,-1.9) {$[y]_C = C^{-1} [y]$};
    
\end{tikzpicture}
\end{center}

## Изменение матрицы отображения при изменении базисов пространств
### Ура, мы добрались!

- Подключаем наши знания о переходах между базисами. Пусть следующие матрицы выполняют переходы из базисов $B$ и $C$ в стандартные:
\begin{equation*}
[x] = P_{B \rightarrow S^v}[x]_B = B[x]_B, \quad [y] = P_{C \rightarrow S^w}[y]_C = C[y]_C
\end{equation*}

- Подставим выражения в известную формулу $[\varphi(x)] = L_{\varphi} [x]$:
$$
    C [\varphi(x)]_C = L_{\varphi} B[x]_B
$$

- Используем трюк с обратной матрицей:
$$
    [\varphi(x)]_C = C^{-1} L_{\varphi} B [x]_B = L_{\varphi, \,(B,C)} [x]_B
$$

- Финально, формула для изменения матрицы линейного отображения при одновременном изменении пары базисов из стандартного:
\begin{equation*}
    \colorbox{green!50}{$L_{\varphi, \,(B,C)} = C^{-1} L_{\varphi} B$}
\end{equation*}

## Примеры

## Слайд для записей
