---
title: "Линейная алгебра"
subtitle: "Линейные отображения и их матричное представление."
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

## Линейные отображения
### Введение и мотивация

\begin{center}
\begin{tikzpicture}
    \draw[thick, fill=blue!10] (0,0) circle (1.0);
    \node[above] at (0,1.2) {$\mathbb{V}$};
    \node at (0,-0.3) {$[x]_B$};
    \fill[red] (0,0) circle (2pt);

    \draw[thick, fill=green!10] (4,0) circle (1.0);
    \node[above] at (4,1.2) {$\mathbb{W}$};
    \node at (3.8,-0.3) {$[\varphi(x)]_C$};
    \fill[red] (4,0) circle (2pt);
  
    \draw[thick, ->] (1.1,0.4) .. controls (2, 0.7) and (2,0.7) .. (2.9,0.4) node[midway, above] {$\varphi$};
\end{tikzpicture}
\end{center}

## Линейные отображения

::: {.callout-note}
## Определение

Пусть $V, W$ — векторные пространства. Отображение $\varphi: V \rightarrow W$ называется \textit{линейным}, если
\begin{enumerate}
    \item $\varphi(\mathbf{u}+\mathbf{v})=\varphi(\mathbf{u})+\varphi(\mathbf{v})$ для всех $\mathbf{u}, \mathbf{v} \in V$

    \item $\varphi(\alpha \mathbf{v})=\alpha \varphi(\mathbf{v})$ для всех $\mathbf{v} \in V$ и всех скаляров $\alpha \in \mathbb{R}$.
\end{enumerate}
Свойства 1 и 2 вместе иногда объединяют в одно:
$$
\varphi(\alpha \mathbf{u}+\beta \mathbf{v})=\alpha \varphi(\mathbf{u})+\beta \varphi(\mathbf{v}), \quad \forall \mathbf{u}, \mathbf{v} \in V, \quad \forall \alpha, \beta \in \mathbb{R}.
$$
:::

## Аналитическое представление отображения

## Матричное представление линейного отображения
### Основные действующие лица

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

## Матричное представление линейного отображения

- На этом этапе мы подключаем аппарат линейной алгебры и предпологаем, что в пространствах $\mathbb{V}$ и $\mathbb{W}$. Предположим, что $\varphi: V \rightarrow W$, набор векторов $B = \{v_1, v_2\}$ образует базис в $\mathbb{V}$, а набор векторов $C = \{\omega_1, \omega_2 \}$ образует базис в $\mathbb{W}$.

Мы хотим исследовать, как $\varphi$ действует на произвольный $x \in \mathbb{V}$. 
По свойствам базиса можем представить $x$ как:
$$
    x = x_1 v_1 + x_2 v_2, \quad [x]_B = \vtwo{x_1}{x_2}
$$
И используем это разложение вместе со свойствами линейного преобразования:
$$
   \varphi(x) = \varphi(x_1 v_1 + x_2 v_2) = x_1 \varphi(v_1) + x_2 \varphi(v_2).
$$

- Вывод: чтобы узнать результат действия функции $\varphi(x)$ достаточно только знать, как функция действует на базисные векторы пространства $\mathbb{V}$ в нашем примере это $\varphi(v_1)$, $\varphi(v_2)$. Помните, что $\varphi(v_1)$, $\varphi(v_2)$ — это тоже \textit{векторы}, \textit{т.е.} абстрактные элементы, жители векторного пространства $W$.

## Матричное представление линейного отображения
Давайте посмотрим на элементы $\varphi(v_1)$, $\varphi(v_2)$ в базисе $C$:

\begin{gather*}
\varphi(v_{\textcolor{red}{1}}) = a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \omega_{\textcolor{violet}{2}}, \\
\varphi(v_{\textcolor{red}{2}}) = a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \omega_{\textcolor{violet}{2}} \\
\end{gather*}

Теперь вернемся к $\varphi(x) = x_{\textcolor{red}{1}} \varphi(v_{\textcolor{red}{1}}) + x_{\textcolor{red}{2}} \varphi(v_{\textcolor{red}{2}})$.

\begin{align*}
\varphi(x) = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \omega_{\textcolor{violet}{2}} \right) & + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \omega_{\textcolor{violet}{2}} \right) =\\
\left(a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} \right) \omega_{\textcolor{violet}{1}} & + \left( a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}} \right) \omega_{\textcolor{violet}{2}} = \\
\gamma_1 \omega_{\textcolor{violet}{1}} & + \gamma_2 \omega_{\textcolor{violet}{2}} 
\end{align*}

- Мы получили разложение элемента $\varphi(x)$ по базису пространства $\mathbb{W}$. Можем записать координаты как:

\begin{equation*}
    \left[ \varphi(x) \right]_C = \vtwo{\gamma_1}{\gamma_2} = \vtwo{a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}}}{a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}}}
\end{equation*}

## Умножение матрицы на вектор... снова...
Наконец:
$$
    \left[ \varphi(x) \right]_{C} = 
    \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}} & a_{\textcolor{violet}{1} \textcolor{red}{2}} \\
        a_{\textcolor{violet}{2}\textcolor{red}{1}} & a_{\textcolor{violet}{2} \textcolor{red}{2}} \\
    \end{pmatrix}
    \begin{pmatrix}
        x_{\textcolor{red}{1}}\\
        x_{\textcolor{red}{2}}
    \end{pmatrix} = A_{\varphi} \left[x \right]_{B}.
$$

Wow!



::: {.callout-tip}
## Матрица линейного преобразования

Для любого линейного преобразования существует его матрица, которая через mat-vec связывает координаты аргумента функции с координатами значения функции в выбранных заранее базисах.

Если у нас есть два базиса $B = \{v_1, v_2, \ldots, v_n\}$ и $C = \{\omega_1, \omega_2, \ldots, \omega_m\}$, то матрица линейного преобразования $L_{\varphi, \,(B,C)}$ строится как:

$$
    L_{\varphi, \,(B,C)} = \begin{pmatrix} | & | & \cdots & | \\ [\varphi(v_1)]_C & [\varphi(v_2)]_C & \cdots & [\varphi(v_n)]_C \\ | & | & \cdots & | \end{pmatrix},
$$

где $[\varphi(v_i)]_C$ — это координаты образа базисного вектора $v_i$ в базисе $C$.
:::

## Матричное представление линейного отображения
### Общий многомерный случай

Предположим, что существует линейное преобразование $\varphi: \mathbb{V} \rightarrow \mathbb{W}$, набор векторов $B = \{v_1,\ldots, v_n\}$ образует базис в $\mathbb{V}$, а набор векторов $C = \{\omega_1, \ldots, \omega_m \}$ образует базис в $\mathbb{W}$.

Мы хотим исследовать, как $\varphi$ действует на произвольный $x \in \mathbb{V}$.

$$
    x = x_1 v_1 + \ldots + x_n v_n,
$$
$$
   \varphi(x) = \varphi(x_1 v_1 + \ldots + x_n v_n) = x_1 \varphi(v_1) + \ldots + x_n \varphi(v_n).
$$

Помните, что $\varphi(v_1), \ldots, \varphi(v_n)$ — это \textit{векторы}, \textit{т.е.} абстрактные элементы векторного пространства $\mathbb{W}$.

## Матричное представление линейного отображения
### Общий многомерный случай

Давайте посмотрим на $\varphi(v_1), \ldots, \varphi(v_n)$ в базисе $C$:

\begin{gather*}
\varphi(v_{\textcolor{red}{1}}) = a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \omega_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \omega_{\textcolor{violet}{m}}, \\
\varphi(v_{\textcolor{red}{2}}) = a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \omega_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \omega_{\textcolor{violet}{m}}, \\
\vdots \\
\varphi(v_{\textcolor{red}{n}}) = a_{\textcolor{violet}{1} \textcolor{red}{n}} \omega_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{n}} \omega_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \omega_{\textcolor{violet}{m}}
\end{gather*}

Теперь вернемся к $\varphi(x) = x_{\textcolor{red}{1}} \varphi(v_{\textcolor{red}{1}}) + \ldots + x_{\textcolor{red}{n}} \varphi(v_{\textcolor{red}{n}})$.

\begin{gather*}
\varphi(x) = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \omega_{\textcolor{violet}{m}} \right) + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \omega_{\textcolor{violet}{m}} \right)\\
+ x_{\textcolor{red}{n}} \left( a_{\textcolor{violet}{1} \textcolor{red}{n}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \omega_{\textcolor{violet}{m}} \right)\\
\end{gather*}

## Матричное представление линейного отображения
### Общий многомерный случай

\begin{gather*}
\varphi(x) = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \omega_{\textcolor{violet}{m}} \right) + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \omega_{\textcolor{violet}{m}} \right)\\
+ x_{\textcolor{red}{n}} \left( a_{\textcolor{violet}{1} \textcolor{red}{n}} \omega_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \omega_{\textcolor{violet}{m}} \right)\\
= \left(a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{1} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \omega_{\textcolor{violet}{1}} + \left( a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{2} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \omega_{\textcolor{violet}{2}}\\
+ \left( a_{\textcolor{violet}{m}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \omega_{\textcolor{violet}{m}}
\end{gather*}

## Умножение матрицы на вектор... снова...
Наконец:
$$
    \left[ \varphi(x) \right]_{C} = 
    \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}} & a_{\textcolor{violet}{1} \textcolor{red}{2}} & \ldots & a_{\textcolor{violet}{1} \textcolor{red}{n}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{1}} & a_{\textcolor{violet}{2} \textcolor{red}{2}} & \ldots & a_{\textcolor{violet}{2} \textcolor{red}{n}}\\
        \vdots & \vdots & \vdots & \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{1}} & a_{\textcolor{violet}{m} \textcolor{red}{2}} & \ldots & a_{\textcolor{violet}{m} \textcolor{red}{n}}
    \end{pmatrix}
    \begin{pmatrix}
        x_{\textcolor{red}{1}}\\
        x_{\textcolor{red}{2}}\\
        \vdots\\
        x_{\textcolor{red}{n}}
    \end{pmatrix} = A_{\varphi} \left[x \right]_{B}.
$$

Wow!

Для построения матрицы $A_{\varphi}$ линейного отображения $\varphi$ нам нужно знать только координаты образов базисных векторов: $\varphi(v_1), \ldots, \varphi(v_n)$, \textit{т.е.} 

$$
    v_1 \overset{\varphi}{\rightarrow} a_{\textcolor{red}{1}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{1}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{1}}
    \end{pmatrix},
    v_2 \overset{\varphi}{\rightarrow} a_{\textcolor{red}{2}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{2}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{2}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{2}}
    \end{pmatrix},\ldots, 
     v_n \overset{\varphi}{\rightarrow} a_{\textcolor{red}{n}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{n}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{n}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{n}}
    \end{pmatrix}
$$
