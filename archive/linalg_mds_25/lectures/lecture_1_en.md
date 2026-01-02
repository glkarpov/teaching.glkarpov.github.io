---
title: "Linear Algebra"
subtitle: "Matrices and Vectors. First Introduction, Basic Operations."
institute: "MDS FCS HSE"
author: "Gleb Karpov"
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
## Matrix

- :::{.callout-definition}
A **matrix** is an ordered array of numbers arranged in $n$ rows and $m$ columns. 
$$
A_{n \times m} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1m} \\
a_{21} & a_{22} & \cdots & a_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nm}
\end{bmatrix}
$$
:::

- We usually denote it as $A_{n \times m}$ or, to emphasize the nature of numbers in the matrix, we write $A \in \mathbb{R}^{n \times m}$.

- If $n = m$, the matrix is called *square*; if $n \neq m$, it's called *rectangular*

## Basic operations: transpose

:::{.callout-definition}
**Transpose** of a matrix is an operation where rows and columns are swapped.
If $A \in \mathbb{R}^{n \times m}$, then $B = A^T \in \mathbb{R}^{m \times n}$, where $b_{ij} = a_{ji}$
:::


\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Original matrix A
    \draw[thick] (-2.2, 1.6) -- (-2.4, 1.6) -- (-2.4, -0.6) -- (-2.2, -0.6);
    \draw[thick] (0.6, 1.6) -- (0.8, 1.6) -- (0.8, -0.6) -- (0.6, -0.6);
    
    % Matrix A elements with colors (increased spacing)
    \node[fill=red!20, minimum width=0.6cm, minimum height=0.4cm] at (-1.8, 1.2) {$a_{11}$};
    \node[fill=blue!20, minimum width=0.6cm, minimum height=0.4cm] at (-1.1, 1.2) {$a_{12}$};
    \node[fill=green!20, minimum width=0.6cm, minimum height=0.4cm] at (-0.4, 1.2) {$a_{13}$};
    
    \node[fill=red!40, minimum width=0.6cm, minimum height=0.4cm] at (-1.8, 0.4) {$a_{21}$};
    \node[fill=blue!40, minimum width=0.6cm, minimum height=0.4cm] at (-1.1, 0.4) {$a_{22}$};
    \node[fill=green!40, minimum width=0.6cm, minimum height=0.4cm] at (-0.4, 0.4) {$a_{23}$};
    
    \node at (-1.1, -1.1) {$A_{2 \times 3}$};
    
    % Arrow
    \draw[->, thick] (1.3, 0.5) -- (2.3, 0.5);
    \node[above] at (1.8, 0.8) {$A^T$};
    
    % Transposed matrix A^T (fixed brackets and spacing)
    \draw[thick] (2.7, 1.9) -- (2.5, 1.9) -- (2.5, -0.9) -- (2.7, -0.9);
    \draw[thick] (4.3, 1.9) -- (4.5, 1.9) -- (4.5, -0.9) -- (4.3, -0.9);
    
    % Matrix A^T elements with matching colors (increased spacing)
    \node[fill=red!20, minimum width=0.6cm, minimum height=0.4cm] at (3.1, 1.5) {$a_{11}$};
    \node[fill=red!40, minimum width=0.6cm, minimum height=0.4cm] at (3.9, 1.5) {$a_{21}$};
    
    \node[fill=blue!20, minimum width=0.6cm, minimum height=0.4cm] at (3.1, 0.7) {$a_{12}$};
    \node[fill=blue!40, minimum width=0.6cm, minimum height=0.4cm] at (3.9, 0.7) {$a_{22}$};
    
    \node[fill=green!20, minimum width=0.6cm, minimum height=0.4cm] at (3.1, -0.1) {$a_{13}$};
    \node[fill=green!40, minimum width=0.6cm, minimum height=0.4cm] at (3.9, -0.1) {$a_{23}$};
    
    \node at (3.5, -1.3) {$B_{3 \times 2} = A^T$};
    
\end{tikzpicture}
\end{center}

## Basic operations: matrix addition

- :::{.callout-definition}
**Matrix addition** is only possible for matrices of the same size. The result is obtained by adding corresponding elements.
If $A, B \in \mathbb{R}^{n \times m}$, then $C = A + B$, where $c_{ij} = a_{ij} + b_{ij}$
:::

**Example:**
$$\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} + \begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix} = \begin{bmatrix}
1+5 & 2+6 \\
3+7 & 4+8
\end{bmatrix} = \begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}$$

## Basic operations: scalar multiplication

- :::{.callout-definition}
**Scalar multiplication** - each element of the matrix is multiplied by the given number.
If $A \in \mathbb{R}^{n \times m}$ and $\alpha \in \mathbb{R}$, then $C = \alpha A$, where $c_{ij} = \alpha \cdot a_{ij}$
:::

**Example:**
$$3 \cdot \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} = \begin{bmatrix}
3 \cdot 1 & 3 \cdot 2 \\
3 \cdot 3 & 3 \cdot 4
\end{bmatrix} = \begin{bmatrix}
3 & 6 \\
9 & 12
\end{bmatrix}$$

**Another example - Linear combination:**
$$2 \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} + 3 \begin{bmatrix}
1 & 1 \\
1 & 1
\end{bmatrix} = \begin{bmatrix}
2 & 0 \\
0 & 2
\end{bmatrix} + \begin{bmatrix}
3 & 3 \\
3 & 3
\end{bmatrix} = \begin{bmatrix}
5 & 3 \\
3 & 5
\end{bmatrix}$$


## Vector

In the simplest representation, we treat a **vector** as a special case of a matrix:

::: {.columns}

::: {.column width="50%"}
### Column vector
$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{R}^{n \times 1}$$

**Dimension:** $n \times 1$ (matrix with one column)
:::

::: {.column width="50%"}
### Row vector
$$\mathbf{y}^T = \begin{bmatrix} y_1 & y_2 & \cdots & y_m \end{bmatrix} \in \mathbb{R}^{1 \times m}$$

**Dimension:** $1 \times m$ (matrix with one row)
:::

:::

### Notation

- **Vectors:** usually denoted by lowercase letters $x, v$ or $\mathbf{u}$
- **Matrices:** usually denoted by uppercase letters $A, B, C$
- **By default:** vector is considered a **column vector**
- **Transpose:** $\mathbf{x}^{\top}$ converts column to row 

## Matrix-by-vector multiplication (matvec)
### Standard approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for specific positions
    \definecolor{col1}{RGB}{255,102,102}  % Red - first element
    \definecolor{col2}{RGB}{102,178,255}  % Blue - second element
    \definecolor{col3}{RGB}{102,255,178}  % Green - pre-last element
    \definecolor{col4}{RGB}{255,178,102}  % Orange - last element
    
    % Matrix A (n x m)
    
    % Draw matrix brackets
    \draw[thick] (-2.5, 2.5) -- (-2.7, 2.5) -- (-2.7, -2.5) -- (-2.5, -2.5);
    \draw[thick] (2.3, 2.5) -- (2.5, 2.5) -- (2.5, -2.5) -- (2.3, -2.5);
    
    % First row with colors (only this row participates in multiplication)
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.8, 2) {$a_{11}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-1, 2) {$a_{12}$};
    \node at (-0.2, 2) {$\cdots$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.6, 2) {$a_{1,m-1}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.8, 2) {$a_{1m}$};
    
    % Second row (no colors)
    \node[minimum width=0.8cm, minimum height=0.6cm] at (-1.8, 1.2) {$a_{21}$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (-1, 1.2) {$a_{22}$};
    \node at (-0.2, 1.2) {$\cdots$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (0.6, 1.2) {$a_{2,m-1}$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (1.8, 1.2) {$a_{2m}$};
    
    % Vertical dots
    \node at (-1.8, 0.4) {$\vdots$};
    \node at (-1, 0.4) {$\vdots$};
    \node at (-0.2, 0.4) {$\ddots$};
    \node at (0.6, 0.4) {$\vdots$};
    \node at (1.8, 0.4) {$\vdots$};
    
    % Last row (no colors)
    \node[minimum width=0.8cm, minimum height=0.6cm] at (-1.8, -1.5) {$a_{n1}$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (-1, -1.5) {$a_{n2}$};
    \node at (-0.2, -1.5) {$\cdots$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (0.6, -1.5) {$a_{n,m-1}$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (1.8, -1.5) {$a_{nm}$};
    
    % Matrix A label
    \node at (0, -3) {$A$};
    
    % Vector x
    
    % Draw vector brackets (fitting actual vector size)
    \draw[thick] (3.5, 2.3) -- (3.3, 2.3) -- (3.3, -1.8) -- (3.5, -1.8);
    \draw[thick] (5.3, 2.3) -- (5.5, 2.3) -- (5.5, -1.8) -- (5.3, -1.8);
    
    % Vector elements with matching colors
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (4.4, 2) {$x_1$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (4.4, 1.2) {$x_2$};
    \node at (4.4, 0.4) {$\vdots$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (4.4, -0.7) {$x_{m-1}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (4.4, -1.5) {$x_m$};
    
    % Vector x label
    \node at (4.4, -3) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2.5) -- (7.3, 2.5) -- (7.3, -2.5) -- (7.5, -2.5);
    \draw[thick] (9.3, 2.5) -- (9.5, 2.5) -- (9.5, -2.5) -- (9.3, -2.5);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.4, 2) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.4, 1.2) {$y_2$};
    \node at (8.4, 0.4) {$\vdots$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.4, -1.5) {$y_n$};
    
    % Result vector y label
    \node at (8.4, -3) {$\mathbf{y}$};
    
    % explanation for first row multiplication
    \node at (4.4, -4) {\small $y_1 = \textcolor{col1}{a_{11}x_1} + \textcolor{col2}{a_{12}x_2} + \cdots + \textcolor{col3}{a_{1,m-1}x_{m-1}} + \textcolor{col4}{a_{1m}x_m}$};
    
    % General formula in a box
    \node at (4.4, -5.5) {\boxed{\textcolor{blue}{y_j = \sum_{k=1}^{m} a_{jk} x_k}}};
        
\end{tikzpicture}
\end{center}


## Matrix-by-vector multiplication (matvec)
### Computational complexity and a brief look at parallel computing

**Recall the general formula:**
$$\boxed{y_j = \sum_{k=1}^{m} a_{jk} x_k, \quad j = 1, 2, \ldots, n}$$

**Operations analysis:**
\begin{itemize}
    \item For computing one element $y_j$: $m$ multiplications (each $a_{jk} \cdot x_k$), $m-1$ additions (summing $m$ products)

    \item For the entire vector $\mathbf{y}$ (n elements): $n \cdot (2m-1)$ total operations.
\end{itemize}

**Time complexity:**
\begin{itemize}
    \item For square matrix $n \times n$: $\mathcal{O}(2n^2 - n) = \mathcal{O}(n^2)$
    \item For rectangular matrix $n \times m$: $\mathcal{O}(nm)$
\end{itemize}

::: {.callout-tip}
## Natural parallelism
Computing each element $y_j$ is **independent** of other elements!
:::

- **Row-wise parallelization:** each processor computes its own $y_j$

## Matrix-by-vector multiplication (matvec)
### Guru approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for each column
    \definecolor{col1}{RGB}{255,102,102}  % Red
    \definecolor{col2}{RGB}{102,178,255}  % Blue  
    \definecolor{col3}{RGB}{102,255,178}  % Green
    \definecolor{col4}{RGB}{255,178,102}  % Orange
    
    % Matrix A (3x4)
    
    % Draw matrix brackets
    \draw[thick] (-2, 2) -- (-2.2, 2) -- (-2.2, -1) -- (-2, -1);
    \draw[thick] (1.8, 2) -- (2, 2) -- (2, -1) -- (1.8, -1);
    
    % Matrix elements with colors
    % First column (red)
    \node at (-1.2, 1.5) {$a_{11}$};
    \node at (-1.2, 0.5) {$a_{21}$};
    \node at (-1.2, -0.5) {$a_{31}$};
    
    % Second column (blue)
    \node at (-0.4, 1.5) {$a_{12}$};
    \node at (-0.4, 0.5) {$a_{22}$};
    \node at (-0.4, -0.5) {$a_{32}$};
    
    % Third column (green)
    \node at (0.4, 1.5) {$a_{13}$};
    \node at (0.4, 0.5) {$a_{23}$};
    \node at (0.4, -0.5) {$a_{33}$};
    
    % Fourth column (orange)
    \node at (1.2, 1.5) {$a_{14}$};
    \node at (1.2, 0.5) {$a_{24}$};
    \node at (1.2, -0.5) {$a_{34}$};
    
    % Matrix A label
    \node at (0, -1.7) {$A$};
    
    % Vector x
    
    % Draw vector brackets
    \draw[thick] (3.5, 2) -- (3.3, 2) -- (3.3, -2) -- (3.5, -2);
    \draw[thick] (5.3, 2) -- (5.5, 2) -- (5.5, -2) -- (5.3, -2);
    
    % Vector elements with matching colors
    \node at (4.5, 1.5) {$x_1$};
    \node at (4.5, 0.5) {$x_2$};
    \node at (4.5, -0.5) {$x_3$};
    \node at (4.5, -1.5) {$x_4$};
    \node at (4.5, -2.7) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0.5) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2) -- (7.3, 2) -- (7.3, -1) -- (7.5, -1);
    \draw[thick] (9.3, 2) -- (9.5, 2) -- (9.5, -1) -- (9.3, -1);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 1.5) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 0.5) {$y_2$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, -0.5) {$y_3$};
    \node at (8.5, -1.7) {$\mathbf{y}$};
    
\end{tikzpicture}
\end{center}

## Matrix-by-vector multiplication (matvec)
### Guru approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for each column
    \definecolor{col1}{RGB}{255,102,102}  % Red
    \definecolor{col2}{RGB}{102,178,255}  % Blue  
    \definecolor{col3}{RGB}{102,255,178}  % Green
    \definecolor{col4}{RGB}{255,178,102}  % Orange
    
    % Matrix A (3x4)
    
    % Draw matrix brackets
    \draw[thick] (-2, 2) -- (-2.2, 2) -- (-2.2, -1) -- (-2, -1);
    \draw[thick] (1.8, 2) -- (2, 2) -- (2, -1) -- (1.8, -1);
    
    % Matrix elements with colors
    % First column (red)
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 1.5) {$a_{11}$};
    \node at (-1.2, 0.5) {$a_{21}$};
    \node at (-1.2, -0.5) {$a_{31}$};
    
    % Second column (blue)
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 1.5) {$a_{12}$};
    \node at (-0.4, 0.5) {$a_{22}$};
    \node at (-0.4, -0.5) {$a_{32}$};
    
    % Third column (green)
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 1.5) {$a_{13}$};
    \node at (0.4, 0.5) {$a_{23}$};
    \node at (0.4, -0.5) {$a_{33}$};
    
    % Fourth column (orange)
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 1.5) {$a_{14}$};
    \node at (1.2, 0.5) {$a_{24}$};
    \node at (1.2, -0.5) {$a_{34}$};
    
    % Matrix A label
    \node at (0, -1.7) {$A$};
    
    % Vector x
    
    % Draw vector brackets
    \draw[thick] (3.5, 2) -- (3.3, 2) -- (3.3, -2) -- (3.5, -2);
    \draw[thick] (5.3, 2) -- (5.5, 2) -- (5.5, -2) -- (5.3, -2);
    
    % Vector elements with matching colors
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 1.5) {$x_1$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 0.5) {$x_2$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -0.5) {$x_3$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -1.5) {$x_4$};
    
    % Vector x label
    \node at (4.5, -2.7) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0.5) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2) -- (7.3, 2) -- (7.3, -1) -- (7.5, -1);
    \draw[thick] (9.3, 2) -- (9.5, 2) -- (9.5, -1) -- (9.3, -1);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 1.5) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 0.5) {$y_2$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, -0.5) {$y_3$};
    
    % Result vector y label
    \node at (8.5, -1.7) {$\mathbf{y}$};
    
\end{tikzpicture}
\end{center}

\begin{center}
$y_1 = \textcolor{red}{a_{11}x_1} + \textcolor{blue}{a_{12}x_2} + \textcolor{green}{a_{13}x_{3}} + \textcolor{orange}{a_{14}x_{4}}$
\end{center}

## Matrix-by-vector multiplication (matvec)
### Guru approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for each column
    \definecolor{col1}{RGB}{255,102,102}  % Red
    \definecolor{col2}{RGB}{102,178,255}  % Blue  
    \definecolor{col3}{RGB}{102,255,178}  % Green
    \definecolor{col4}{RGB}{255,178,102}  % Orange
    
    % Matrix A (3x4)
    
    % Draw matrix brackets
    \draw[thick] (-2, 2) -- (-2.2, 2) -- (-2.2, -1) -- (-2, -1);
    \draw[thick] (1.8, 2) -- (2, 2) -- (2, -1) -- (1.8, -1);
    
    % Matrix elements with colors
    % First column (red)
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 1.5) {$a_{11}$};
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 0.5) {$a_{21}$};
    \node at (-1.2, -0.5) {$a_{31}$};
    
    % Second column (blue)
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 1.5) {$a_{12}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 0.5) {$a_{22}$};
    \node at (-0.4, -0.5) {$a_{32}$};
    
    % Third column (green)
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 1.5) {$a_{13}$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 0.5) {$a_{23}$};
    \node at (0.4, -0.5) {$a_{33}$};
    
    % Fourth column (orange)
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 1.5) {$a_{14}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 0.5) {$a_{24}$};
    \node at (1.2, -0.5) {$a_{34}$};
    
    % Matrix A label
    \node at (0, -1.7) {$A$};
    
    % Vector x
    
    % Draw vector brackets
    \draw[thick] (3.5, 2) -- (3.3, 2) -- (3.3, -2) -- (3.5, -2);
    \draw[thick] (5.3, 2) -- (5.5, 2) -- (5.5, -2) -- (5.3, -2);
    
    % Vector elements with matching colors
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 1.5) {$x_1$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 0.5) {$x_2$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -0.5) {$x_3$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -1.5) {$x_4$};
    
    % Vector x label
    \node at (4.5, -2.7) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0.5) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2) -- (7.3, 2) -- (7.3, -1) -- (7.5, -1);
    \draw[thick] (9.3, 2) -- (9.5, 2) -- (9.5, -1) -- (9.3, -1);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 1.5) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 0.5) {$y_2$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, -0.5) {$y_3$};
    \node at (8.5, -1.7) {$\mathbf{y}$};    
\end{tikzpicture}
\end{center}

\begin{center}
\begin{gather*}
y_1 = \textcolor{red}{a_{11}x_1} + \textcolor{blue}{a_{12}x_2} + \textcolor{green}{a_{13}x_{3}} + \textcolor{orange}{a_{14}x_{4}} \\
y_2 = \textcolor{red}{a_{21}x_1} + \textcolor{blue}{a_{22}x_2} + \textcolor{green}{a_{23}x_{3}} + \textcolor{orange}{a_{24}x_{4}} \\ 
\end{gather*}
\end{center}


## Matrix-by-vector multiplication (matvec)
### Guru approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for each column
    \definecolor{col1}{RGB}{255,102,102}  % Red
    \definecolor{col2}{RGB}{102,178,255}  % Blue  
    \definecolor{col3}{RGB}{102,255,178}  % Green
    \definecolor{col4}{RGB}{255,178,102}  % Orange
    
    % Matrix A (3x4)
    
    % Draw matrix brackets
    \draw[thick] (-2, 2) -- (-2.2, 2) -- (-2.2, -1) -- (-2, -1);
    \draw[thick] (1.8, 2) -- (2, 2) -- (2, -1) -- (1.8, -1);
    
    % Matrix elements with colors
    % First column (red)
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 1.5) {$a_{11}$};
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 0.5) {$a_{21}$};
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, -0.5) {$a_{31}$};
    
    % Second column (blue)
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 1.5) {$a_{12}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 0.5) {$a_{22}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, -0.5) {$a_{32}$};
    
    % Third column (green)
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 1.5) {$a_{13}$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 0.5) {$a_{23}$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, -0.5) {$a_{33}$};
    
    % Fourth column (orange)
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 1.5) {$a_{14}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 0.5) {$a_{24}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, -0.5) {$a_{34}$};
    
    % Matrix A label
    \node at (0, -1.7) {$A$};
    
    % Vector x
    
    % Draw vector brackets
    \draw[thick] (3.5, 2) -- (3.3, 2) -- (3.3, -2) -- (3.5, -2);
    \draw[thick] (5.3, 2) -- (5.5, 2) -- (5.5, -2) -- (5.3, -2);
    
    % Vector elements with matching colors
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 1.5) {$x_1$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 0.5) {$x_2$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -0.5) {$x_3$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -1.5) {$x_4$};
    
    % Vector x label
    \node at (4.5, -2.7) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0.5) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2) -- (7.3, 2) -- (7.3, -1) -- (7.5, -1);
    \draw[thick] (9.3, 2) -- (9.5, 2) -- (9.5, -1) -- (9.3, -1);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 1.5) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 0.5) {$y_2$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, -0.5) {$y_3$};
    
    % Result vector y label
    \node at (8.5, -1.7) {$\mathbf{y}$};
\end{tikzpicture}
\end{center}

\begin{center}
\begin{gather*}
y_1 = \textcolor{red}{a_{11}x_1} + \textcolor{blue}{a_{12}x_2} + \textcolor{green}{a_{13}x_{3}} + \textcolor{orange}{a_{14}x_{4}} \\
y_2 = \textcolor{red}{a_{21}x_1} + \textcolor{blue}{a_{22}x_2} + \textcolor{green}{a_{23}x_{3}} + \textcolor{orange}{a_{24}x_{4}} \\
y_3 = \textcolor{red}{a_{31}x_1} + \textcolor{blue}{a_{32}x_2} + \textcolor{green}{a_{33}x_{3}} + \textcolor{orange}{a_{34}x_{4}}
\end{gather*}
\end{center}


## Matrix-by-vector multiplication (matvec)
### Guru approach

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors for each column
    \definecolor{col1}{RGB}{255,102,102}  % Red
    \definecolor{col2}{RGB}{102,178,255}  % Blue  
    \definecolor{col3}{RGB}{102,255,178}  % Green
    \definecolor{col4}{RGB}{255,178,102}  % Orange
    
    % Matrix A (3x4)
    
    % Draw matrix brackets
    \draw[thick] (-2, 2) -- (-2.2, 2) -- (-2.2, -1) -- (-2, -1);
    \draw[thick] (1.8, 2) -- (2, 2) -- (2, -1) -- (1.8, -1);
    
    % Matrix elements with colors
    % First column (red)
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 1.5) {$a_{11}$};
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, 0.5) {$a_{21}$};
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (-1.2, -0.5) {$a_{31}$};
    
    % Second column (blue)
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 1.5) {$a_{12}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, 0.5) {$a_{22}$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (-0.4, -0.5) {$a_{32}$};
    
    % Third column (green)
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 1.5) {$a_{13}$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, 0.5) {$a_{23}$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (0.4, -0.5) {$a_{33}$};
    
    % Fourth column (orange)
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 1.5) {$a_{14}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, 0.5) {$a_{24}$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (1.2, -0.5) {$a_{34}$};
    
    % Matrix A label
    \node at (0, -1.7) {$A$};
    
    % Vector x
    
    % Draw vector brackets
    \draw[thick] (3.5, 2) -- (3.3, 2) -- (3.3, -2) -- (3.5, -2);
    \draw[thick] (5.3, 2) -- (5.5, 2) -- (5.5, -2) -- (5.3, -2);
    
    % Vector elements with matching colors
    \node[fill=col1!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 1.5) {$x_1$};
    \node[fill=col2!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, 0.5) {$x_2$};
    \node[fill=col3!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -0.5) {$x_3$};
    \node[fill=col4!30, minimum width=0.8cm, minimum height=0.6cm] at (4.5, -1.5) {$x_4$};
    
    % Vector x label
    \node at (4.5, -2.7) {$\mathbf{x}$};
    
    % Equals sign
    \node at (6.2, 0.5) {$=$};
    
    % Result vector y
    
    % Draw result vector brackets
    \draw[thick] (7.5, 2) -- (7.3, 2) -- (7.3, -1) -- (7.5, -1);
    \draw[thick] (9.3, 2) -- (9.5, 2) -- (9.5, -1) -- (9.3, -1);
    
    % Result vector elements
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 1.5) {$y_1$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, 0.5) {$y_2$};
    \node[minimum width=0.8cm, minimum height=0.6cm] at (8.5, -0.5) {$y_3$};
    
    % Result vector y label
    \node at (8.5, -1.7) {$\mathbf{y}$};
        
    % Color the column vectors in the explanation
    \node at (-1., -4.5) {$\mathbf{y} = $};
    \node[fill=col1!20, rounded corners=2pt] at (0.5, -4.5) {$x_1 \begin{bmatrix} a_{11} \\ a_{21} \\ a_{31} \end{bmatrix}$};
    \node at (1.5, -4.5) {$+$};
    \node[fill=col2!20, rounded corners=2pt] at (2.5, -4.5) {$x_2 \begin{bmatrix} a_{12} \\ a_{22} \\ a_{32} \end{bmatrix}$};
    \node at (3.5, -4.5) {$+$};
    \node[fill=col3!20, rounded corners=2pt] at (4.5, -4.5) {$x_3 \begin{bmatrix} a_{13} \\ a_{23} \\ a_{33} \end{bmatrix}$};
    \node at (5.5, -4.5) {$+$};
    \node[fill=col4!20, rounded corners=2pt] at (6.5, -4.5) {$x_4 \begin{bmatrix} a_{14} \\ a_{24} \\ a_{34} \end{bmatrix}$};
    
\end{tikzpicture}
\end{center}

## Matrix-by-vector product
### Visual comparison

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Define colors
    \definecolor{col1}{RGB}{255,102,102}  % Red for first column
    \definecolor{col2}{RGB}{102,178,255}  % Blue for second column
    \definecolor{result}{RGB}{102,255,102}  % Green for result
    
    % Matrix A emphasizing columns
    \draw[thick] (-1.5, 2.5) -- (-1.7, 2.5) -- (-1.7, 1) -- (-1.5, 1);
    \draw[thick] (0.1, 2.5) -- (0.3, 2.5) -- (0.3, 1) -- (0.1, 1);
    
    \node[fill=col1!40, minimum width=0.6cm, minimum height=0.5cm] at (-1, 2.2) {$3$};
    \node[fill=col2!40, minimum width=0.6cm, minimum height=0.5cm] at (-0.4, 2.2) {$1$};
    \node[fill=col1!40, minimum width=0.6cm, minimum height=0.5cm] at (-1, 1.3) {$2$};
    \node[fill=col2!40, minimum width=0.6cm, minimum height=0.5cm] at (-0.4, 1.3) {$4$};
    
    \node[below] at (-0.7, 0.8) {$A$};
    
    % Vector x
    \draw[thick] (1.5, 2.5) -- (1.3, 2.5) -- (1.3, 1) -- (1.5, 1);
    \draw[thick] (2.5, 2.5) -- (2.7, 2.5) -- (2.7, 1) -- (2.5, 1);
    
    \node[fill=col1!40, minimum width=0.6cm, minimum height=0.5cm] at (2, 2.2) {$2$};
    \node[fill=col2!40, minimum width=0.6cm, minimum height=0.5cm] at (2, 1.3) {$1$};
    
    \node[below] at (2, 0.8) {$\mathbf{x}$};
    
    % Equals
    \node at (3.3, 1.75) {$=$};
    
    % Result vector
    \draw[thick] (3.8, 2.5) -- (3.6, 2.5) -- (3.6, 1) -- (3.8, 1);
    \draw[thick] (4.8, 2.5) -- (5, 2.5) -- (5, 1) -- (4.8, 1);
    
    \node[fill=result!20, minimum width=0.6cm, minimum height=0.5cm] at (4.3, 2.2) {$7$};
    \node[fill=result!20, minimum width=0.6cm, minimum height=0.5cm] at (4.3, 1.3) {$8$};
    
    \node[below] at (4.3, 0.8) {$\mathbf{y}$};
    
\end{tikzpicture}
\end{center}

::: {.columns}

::: {.column width="50%"}
### Traditional View: Row-wise

**Calculations:**
\begin{itemize}
\item $y_1 = 3 \cdot 2 + 1 \cdot 1 = 7$

\item $y_2 = 2 \cdot 2 + 4 \cdot 1 = 8$
\end{itemize}
:::

::: {.column width="50%"}
### Guru View: Column Linear Combination



**Linear combination:**

\begin{tikzpicture}[scale=0.8]
    % Define colors
    \definecolor{col1}{RGB}{255,102,102}  % Red for first column
    \definecolor{col2}{RGB}{102,178,255}  % Blue for second column
    \definecolor{result}{RGB}{102,255,102}  % Green for result
    
    % Grid first (so it's behind everything)
    \draw[gray!30] (0, -3.5) grid[step=0.5] (4, 1);
    
    % Coordinate system (drawn after grid)
    \draw[->, thick] (-0.5, -2) -- (4.5, -2) node[right] {$x$};
    \draw[->, thick] (2, -3.8) -- (2, 1.3) node[above] {$y$};
    
    % First column vector: [3, 2] scaled by 2 = [6, 4]
    \draw[very thick, col1, ->] (2, -2) -- (3.5, 0) node[midway, above left] {\small $2 \cdot \mathbf{a_1}$};
    \node[col1, below right] at (3.5, 0) {\small $\begin{bmatrix} 6 \\ 4 \end{bmatrix}$};
    
    % Second column vector: [1, 4] scaled by 1, starting from end of first vector
    \draw[very thick, col2, ->] (3.5, 0) -- (4, 2) node[midway, above right] {\small $1 \cdot \mathbf{a_2}$};
    \node[col2, above right] at (4, 2) {\small $\begin{bmatrix} 1 \\ 4 \end{bmatrix}$};
    
    % Result vector (from origin to final point)
    \draw[very thick, result, ->] (2, -2) -- (4, 2) node[midway, below right] {\small $\mathbf{y}$};
    \node[result, above left] at (4, 2) {\small $\begin{bmatrix} 7 \\ 8 \end{bmatrix}$};
    
    % Origin
    \node[below left] at (2, -2) {$O$};
    
    % Dashed line showing the parallelogram construction
    \draw[dashed, gray] (3.5, 0) -- (4, 0) -- (4, 2);
    
    % Labels for column vectors (moved further left and separated)
    \node[col1, align=left] at (-1, 0.5) {\small First column: \\ $\mathbf{a_1} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$};
    \node[col2, align=left] at (-1, -1.5) {\small Second column: \\ $\mathbf{a_2} = \begin{bmatrix} 1 \\ 4 \end{bmatrix}$};
    
\end{tikzpicture}

:::

:::

## Matrix-by-matrix multiplication (matmul, General Matrix Multiplication - GEMM)
### Standard approach

\begin{center}
\begin{tikzpicture}[scale=0.7]
    % Define colors for specific positions
    \definecolor{rowcolor}{RGB}{255,102,102}  % Red - i-th row
    \definecolor{colcolor}{RGB}{102,178,255}  % Blue - j-th column
    \definecolor{resultcolor}{RGB}{102,255,102}  % Green - result element
    
    % Matrix A (n x k)
    
    % Draw matrix A brackets
    \draw[thick] (-3.5, 3) -- (-3.7, 3) -- (-3.7, -2) -- (-3.5, -2);
    \draw[thick] (0.3, 3) -- (0.5, 3) -- (0.5, -2) -- (0.3, -2);
    
    % i-th row label (on the left)
    \node[rowcolor, left] at (-4, 0.5) {\small $i$-th row};
    \draw[rowcolor, ->] (-3.8, 0.5) -- (-3.5, 0.5);
    
    % Matrix A elements - highlight i-th row
    % First row (normal)
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2.8, 2.5) {$a_{11}$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2, 2.5) {$a_{12}$};
    \node at (-1.2, 2.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-0.4, 2.5) {$a_{1k}$};
    
    % Dots above i-th row
    \node at (-2.8, 1.7) {$\vdots$};
    \node at (-2, 1.7) {$\vdots$};
    \node at (-1.2, 1.7) {$\ddots$};
    \node at (-0.4, 1.7) {$\vdots$};
    
    % i-th row (highlighted)
    \node[fill=rowcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (-2.8, 0.5) {$a_{i1}$};
    \node[fill=rowcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (-2, 0.5) {$a_{i2}$};
    \node at (-1.2, 0.5) {$\cdots$};
    \node[fill=rowcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (-0.4, 0.5) {$a_{ik}$};
    
    % Dots below i-th row
    \node at (-2.8, -0.3) {$\vdots$};
    \node at (-2, -0.3) {$\vdots$};
    \node at (-1.2, -0.3) {$\ddots$};
    \node at (-0.4, -0.3) {$\vdots$};
    
    % Last row (normal)
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2.8, -1.5) {$a_{n1}$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2, -1.5) {$a_{n2}$};
    \node at (-1.2, -1.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-0.4, -1.5) {$a_{nk}$};
    
    % Matrix A label
    \node at (-1.6, -2.7) {$A$};
    
    % Matrix B (k x m)
    
    % Draw matrix B brackets
    \draw[thick] (2.1, 2.8) -- (1.9, 2.8) -- (1.9, -0.2) -- (2.1, -0.2);
    \draw[thick] (6.1, 2.8) -- (6.3, 2.8) -- (6.3, -0.2) -- (6.1, -0.2);
    
    % j-th column label (on the top)
    \node[colcolor, above] at (4.1, 3.2) {\small $j$-th column};
    \draw[colcolor, ->] (4.1, 3) -- (4.1, 2.7);
    
    % Matrix B elements - highlight j-th column
    % First row
    \node[minimum width=0.7cm, minimum height=0.5cm] at (2.6, 2.5) {$b_{11}$};
    \node at (3.4, 2.5) {$\cdots$};
    \node[fill=colcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (4.1, 2.5) {$b_{1j}$};
    \node at (4.8, 2.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (5.6, 2.5) {$b_{1m}$};
    
    % Second row
    \node[minimum width=0.7cm, minimum height=0.5cm] at (2.6, 1.7) {$b_{21}$};
    \node at (3.4, 1.7) {$\cdots$};
    \node[fill=colcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (4.1, 1.7) {$b_{2j}$};
    \node at (4.8, 1.7) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (5.6, 1.7) {$b_{2m}$};
    
    % Vertical dots
    \node at (2.6, 0.9) {$\vdots$};
    \node at (3.4, 0.9) {$\ddots$};
    \node[fill=colcolor!30] at (4.1, 0.9) {$\vdots$};
    \node at (4.8, 0.9) {$\ddots$};
    \node at (5.6, 0.9) {$\vdots$};
    
    % Last row
    \node[minimum width=0.7cm, minimum height=0.5cm] at (2.6, 0.1) {$b_{k1}$};
    \node at (3.4, 0.1) {$\cdots$};
    \node[fill=colcolor!30, minimum width=0.7cm, minimum height=0.5cm] at (4.1, 0.1) {$b_{kj}$};
    \node at (4.8, 0.1) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (5.6, 0.1) {$b_{km}$};
    
    % Matrix B label
    \node at (4.1, -0.9) {$B$};
    
    % Equals sign
    \node at (7.1, 0.75) {$=$};
    
    % Result matrix C (n x m)
    
    % Draw result matrix brackets
    \draw[thick] (8.1, 3) -- (7.9, 3) -- (7.9, -2) -- (8.1, -2);
    \draw[thick] (12.1, 3) -- (12.3, 3) -- (12.3, -2) -- (12.1, -2);
    
    % Result matrix elements - highlight c_ij
    % First row
    \node[minimum width=0.7cm, minimum height=0.5cm] at (8.8, 2.5) {$c_{11}$};
    \node at (9.6, 2.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (10.3, 2.5) {$c_{1j}$};
    \node at (11, 2.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (11.8, 2.5) {$c_{1m}$};
    
    % Dots above i-th row
    \node at (8.8, 1.7) {$\vdots$};
    \node at (9.6, 1.7) {$\ddots$};
    \node at (10.3, 1.7) {$\vdots$};
    \node at (11, 1.7) {$\ddots$};
    \node at (11.8, 1.7) {$\vdots$};
    
    % i-th row with highlighted c_ij
    \node[minimum width=0.7cm, minimum height=0.5cm] at (8.8, 0.5) {$c_{i1}$};
    \node at (9.6, 0.5) {$\cdots$};
    \node[fill=resultcolor!50, minimum width=0.7cm, minimum height=0.5cm] at (10.3, 0.5) {$c_{ij}$};
    \node at (11, 0.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (11.8, 0.5) {$c_{im}$};
    
    % Dots below i-th row
    \node at (8.8, -0.3) {$\vdots$};
    \node at (9.6, -0.3) {$\ddots$};
    \node at (10.3, -0.3) {$\vdots$};
    \node at (11, -0.3) {$\ddots$};
    \node at (11.8, -0.3) {$\vdots$};
    
    % Last row
    \node[minimum width=0.7cm, minimum height=0.5cm] at (8.8, -1.5) {$c_{n1}$};
    \node at (9.6, -1.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (10.3, -1.5) {$c_{nj}$};
    \node at (11, -1.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (11.8, -1.5) {$c_{nm}$};
    
    % Matrix C label
    \node at (10.1, -2.7) {$C$};
    
    % explanation for c_ij computation
    \node at (4.1, -3.5) {\small $c_{ij} = \textcolor{red}{a_{i1}} \cdot \textcolor{blue}{b_{1j}} + \textcolor{red}{a_{i2}} \cdot \textcolor{blue}{b_{2j}} + \cdots + \textcolor{red}{a_{ik}} \cdot \textcolor{blue}{b_{kj}}$};
    
    % General formula in a box
    \node at (4.1, -4.8) {\boxed{\textcolor{purple}{c_{ij} = \sum_{l=1}^{k} a_{il} b_{lj}}}};
        
\end{tikzpicture}
\end{center}

## Matrix multiplication (matmul, General Matrix Multiplication - GEMM)
### Column-wise approach

\begin{center}
\begin{tikzpicture}[scale=0.7]
    % Define colors for different columns
    \definecolor{col1}{RGB}{255,102,102}  % Red - first column
    \definecolor{col2}{RGB}{102,178,255}  % Blue - second column  
    \definecolor{col3}{RGB}{102,255,178}  % Green - third column
    \definecolor{col4}{RGB}{255,178,102}  % Orange - fourth column
    \definecolor{rowcolor}{RGB}{255,102,102}  % Red - for i-th row highlighting
    
    % Matrix A (n x k) - copied from above diagram
    
    % Draw matrix A brackets
    \draw[thick] (-3.5, 3) -- (-3.7, 3) -- (-3.7, -2) -- (-3.5, -2);
    \draw[thick] (0.3, 3) -- (0.5, 3) -- (0.5, -2) -- (0.3, -2);
    
    % Matrix A elements - highlight i-th row
    % First row (normal)
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2.8, 2.5) {$a_{11}$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2, 2.5) {$a_{12}$};
    \node at (-1.2, 2.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-0.4, 2.5) {$a_{1k}$};
    
    % Dots above i-th row
    \node at (-2.8, 1.7) {$\vdots$};
    \node at (-2, 1.7) {$\vdots$};
    \node at (-1.2, 1.7) {$\ddots$};
    \node at (-0.4, 1.7) {$\vdots$};
    
    % i-th row (no highlighting)
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2.8, 0.5) {$a_{i1}$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2, 0.5) {$a_{i2}$};
    \node at (-1.2, 0.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-0.4, 0.5) {$a_{ik}$};
    
    % Dots below i-th row
    \node at (-2.8, -0.3) {$\vdots$};
    \node at (-2, -0.3) {$\vdots$};
    \node at (-1.2, -0.3) {$\ddots$};
    \node at (-0.4, -0.3) {$\vdots$};
    
    % Last row (normal)
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2.8, -1.5) {$a_{n1}$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-2, -1.5) {$a_{n2}$};
    \node at (-1.2, -1.5) {$\cdots$};
    \node[minimum width=0.7cm, minimum height=0.5cm] at (-0.4, -1.5) {$a_{nk}$};
    
    % Matrix A label
    \node at (-1.6, -2.7) {$A$};
    
    % Matrix B (k x m) - colorize columns
    
    % Draw matrix B brackets
    \draw[thick] (2.1, 2.8) -- (1.9, 2.8) -- (1.9, -0.2) -- (2.1, -0.2);
    \draw[thick] (7.1, 2.8) -- (7.3, 2.8) -- (7.3, -0.2) -- (7.1, -0.2);
    
    % Matrix B elements with colored columns
    % First row
    \node[fill=col1!40, minimum width=0.7cm, minimum height=0.5cm] at (2.6, 2.5) {$b_{11}$};
    \node[fill=col2!40, minimum width=0.7cm, minimum height=0.5cm] at (3.6, 2.5) {$b_{12}$};
    \node[fill=col3!40, minimum width=0.7cm, minimum height=0.5cm] at (4.6, 2.5) {$b_{13}$};
    \node at (5.6, 2.5) {$\cdots$};
    \node[fill=col4!40, minimum width=0.7cm, minimum height=0.5cm] at (6.6, 2.5) {$b_{1m}$};
    
    % Second row
    \node[fill=col1!40, minimum width=0.7cm, minimum height=0.5cm] at (2.6, 1.7) {$b_{21}$};
    \node[fill=col2!40, minimum width=0.7cm, minimum height=0.5cm] at (3.6, 1.7) {$b_{22}$};
    \node[fill=col3!40, minimum width=0.7cm, minimum height=0.5cm] at (4.6, 1.7) {$b_{23}$};
    \node at (5.6, 1.7) {$\cdots$};
    \node[fill=col4!40, minimum width=0.7cm, minimum height=0.5cm] at (6.6, 1.7) {$b_{2m}$};
    
    % Vertical dots
    \node[fill=col1!40] at (2.6, 0.9) {$\vdots$};
    \node[fill=col2!40] at (3.6, 0.9) {$\vdots$};
    \node[fill=col3!40] at (4.6, 0.9) {$\vdots$};
    \node at (5.6, 0.9) {$\ddots$};
    \node[fill=col4!40] at (6.6, 0.9) {$\vdots$};
    
    % Last row
    \node[fill=col1!40, minimum width=0.7cm, minimum height=0.5cm] at (2.6, 0.1) {$b_{k1}$};
    \node[fill=col2!40, minimum width=0.7cm, minimum height=0.5cm] at (3.6, 0.1) {$b_{k2}$};
    \node[fill=col3!40, minimum width=0.7cm, minimum height=0.5cm] at (4.6, 0.1) {$b_{k3}$};
    \node at (5.6, 0.1) {$\cdots$};
    \node[fill=col4!40, minimum width=0.7cm, minimum height=0.5cm] at (6.6, 0.1) {$b_{km}$};
    
    % Matrix B label
    \node at (4.6, -0.9) {$B$};
    
    % Equals sign
    \node at (8.1, 0.75) {$=$};
    
    % Result matrix C (n x m) - same colors but more transparent
    
    % Draw result matrix brackets
    \draw[thick] (9.1, 3) -- (8.9, 3) -- (8.9, -2) -- (9.1, -2);
    \draw[thick] (14.2, 3) -- (14.4, 3) -- (14.4, -2) -- (14.2, -2);
    
    % Result matrix elements with matching colors (more transparent)
    % First row
    \node[fill=col1!15, minimum width=0.7cm, minimum height=0.5cm] at (9.8, 2.5) {$c_{11}$};
    \node[fill=col2!15, minimum width=0.7cm, minimum height=0.5cm] at (10.8, 2.5) {$c_{12}$};
    \node[fill=col3!15, minimum width=0.7cm, minimum height=0.5cm] at (11.8, 2.5) {$c_{13}$};
    \node at (12.8, 2.5) {$\cdots$};
    \node[fill=col4!15, minimum width=0.7cm, minimum height=0.5cm] at (13.8, 2.5) {$c_{1m}$};
    
    % Dots above i-th row
    \node[fill=col1!15] at (9.8, 1.7) {$\vdots$};
    \node[fill=col2!15] at (10.8, 1.7) {$\vdots$};
    \node[fill=col3!15] at (11.8, 1.7) {$\vdots$};
    \node at (12.8, 1.7) {$\ddots$};
    \node[fill=col4!15] at (13.8, 1.7) {$\vdots$};
    
    % i-th row with highlighted c_ij
    \node[fill=col1!15, minimum width=0.7cm, minimum height=0.5cm] at (9.8, 0.5) {$c_{i1}$};
    \node[fill=col2!15, minimum width=0.7cm, minimum height=0.5cm] at (10.8, 0.5) {$c_{i2}$};
    \node[fill=col3!15, minimum width=0.7cm, minimum height=0.5cm] at (11.8, 0.5) {$c_{i3}$};
    \node at (12.8, 0.5) {$\cdots$};
    \node[fill=col4!15, minimum width=0.7cm, minimum height=0.5cm] at (13.8, 0.5) {$c_{im}$};
    
    % Dots below i-th row
    \node[fill=col1!15] at (9.8, -0.3) {$\vdots$};
    \node[fill=col2!15] at (10.8, -0.3) {$\vdots$};
    \node[fill=col3!15] at (11.8, -0.3) {$\vdots$};
    \node at (12.8, -0.3) {$\ddots$};
    \node[fill=col4!15] at (13.8, -0.3) {$\vdots$};
    
    % Last row
    \node[fill=col1!15, minimum width=0.7cm, minimum height=0.5cm] at (9.8, -1.5) {$c_{n1}$};
    \node[fill=col2!15, minimum width=0.7cm, minimum height=0.5cm] at (10.8, -1.5) {$c_{n2}$};
    \node[fill=col3!15, minimum width=0.7cm, minimum height=0.5cm] at (11.8, -1.5) {$c_{n3}$};
    \node at (12.8, -1.5) {$\cdots$};
    \node[fill=col4!15, minimum width=0.7cm, minimum height=0.5cm] at (13.8, -1.5) {$c_{nm}$};
    
    % Matrix C label
    \node at (11.1, -2.7) {$C$};
    
    % Explanation showing column-wise computation
    \node at (5.6, -3.5) {\small Each column of $C$ = $A \times$ corresponding column of $B$};
    
    % General formula in a box
    \node at (5.6, -4.8) {\boxed{\textcolor{purple}{\mathbf{C_j} = A \mathbf{B_j}, \quad j = 1, 2, \ldots, m}}};
        
\end{tikzpicture}
\end{center}

## Matrix multiplication (matmul, General Matrix Multiplication - GEMM)
### Properties of matrix multiplication

1. **Associativity:**
   $$(AB)C = A(BC)$$
   
2. **Distributivity:**
   $$A(B + C) = AB + AC$$
   $$(A + B)C = AC + BC$$

3. **Scalar multiplication:**
   $$\alpha(AB) = (\alpha A)B = A(\alpha B)$$

## Matrix multiplication (matmul, General Matrix Multiplication - GEMM)
### Important limitations

4. **Non-commutativity:**
   $$AB \neq BA \quad \text{(in general)}$$
   
   **Example:** For $2 \times 2$ matrices:
   $$\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix}$$
   
   $$\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix}$$

5. **Transpose of product:**
   $$(AB)^T = B^T A^T$$
   
   ::: {.callout-note}
   Note the **reversed order** of matrices when transposing!
   :::

## Matrix multiplication (matmul, General Matrix Multiplication - GEMM)
### Computational complexity and parallelization

**Recall the general formula:**
$$\boxed{c_{ij} = \sum_{l=1}^{k} a_{il} b_{lj}, \quad i = 1, 2, \ldots, n, \quad j = 1, 2, \ldots, m}$$

**Operations analysis for matrices $A_{n \times k}$ and $B_{k \times m}$:**
\begin{itemize}
    \item For computing one element $c_{ij}$: $k$ multiplications, $k-1$ additions
    \item Total number of operations: $n \times m \times (2k-1)$
\end{itemize}

**Time complexity:**
\begin{itemize}
    \item For square matrices $n \times n$: $\mathcal{O}(2n^3 - n^2) = \mathcal{O}(n^3)$
    \item For rectangular matrices: $\mathcal{O}(nmk)$
\end{itemize}

::: {.callout-tip}
## Natural parallelism
- **By elements:** each $c_{ij}$ is computed independently
- **By rows:** each processor handles its rows of matrix $A$
- **By columns:** each processor handles its columns of matrix $B$
- **Block approach:** dividing matrices into blocks for efficient cache usage
:::

## Example. Simple but important idea about matrix computations.

Suppose you have the following expression

$$
b = A_1 A_2 A_3 x,
$$

where $A_1, A_2, A_3 \in \mathbb{R}^{3 \times 3}$ are random square dense (fully filled with numbers) matrices, and $x \in \mathbb{R}^3$ is a vector. You need to compute $b$.

Which approach is best to use?
\begin{enumerate}
    \item $A_1 A_2 A_3 x$ (left to right)
    \item $\left(A_1 \left(A_2 \left(A_3 x\right)\right)\right)$ (right to left)
    \item It doesn't matter
    \item The results of the first two options will not be the same.
\end{enumerate}

Check the attached .ipynb file in the repository.
