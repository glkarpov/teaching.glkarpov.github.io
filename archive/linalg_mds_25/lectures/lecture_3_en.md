---
title: "FCS HSE, MDS, Linear Algebra"
format: beamer
---

# Function

# Functions between vector spaces

\textbf{Definition}. Let $V, W$ be vector spaces. A transformation $T: V \rightarrow W$ is called linear if

1. $T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}) \forall \mathbf{u}, \mathbf{v} \in V$


2. $T(\alpha \mathbf{v})=\alpha T(\mathbf{v})$ for all $\mathbf{v} \in V$ and for all scalars $\alpha \in \mathbb{R}$.

Properties 1 and 2 together are sometimes combined into the following one:
$$
T(\alpha \mathbf{u}+\beta \mathbf{v})=\alpha T(\mathbf{u})+\beta T(\mathbf{v}), \quad \forall \mathbf{u}, \mathbf{v} \in V, \quad \forall \alpha, \beta \in \mathbb{R}.
$$

# We need a way to write a transformation analytically

# Matrix representation of a linear transformation

Let us assume $T: V \rightarrow W$, vectors $e_1, \ldots, e_m$ be a standard basis in $V$, and vectors $\tilde{e}_1, \ldots, \tilde{e}_m$ be a basis in $W$.

We would like to investigate how $T$ acts on any $x \in V$.

$$
    x = x_1 e_1 + \ldots + x_n e_n,
$$
$$
   T(x) = T(x_1 e_1 + \ldots + x_n e_n) = x_1 T(e_1) + \ldots + x_n T(e_n).
$$

Keep in mind, that $T(e_1), \ldots, T(e_n)$ are \textit{vectors}, \textit{i.e.} abstract citizens of the vector space $W$.

# Matrix representation of a linear transformation
Let us look at them from standard basis in $W$:

\begin{gather*}
T(e_{\textcolor{red}{1}}) = a_{\textcolor{violet}{1}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{m}}, \\
T(e_{\textcolor{red}{2}}) = a_{\textcolor{violet}{1} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{m}}, \\
\vdots \\
T(e_{\textcolor{red}{n}}) = a_{\textcolor{violet}{1} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{m}}
\end{gather*}

Then get back to $T(x) = x_{\textcolor{red}{1}} T(e_{\textcolor{red}{1}}) + \ldots + x_{\textcolor{red}{n}} T(e_{\textcolor{red}{n}})$.

\begin{multline*}
T(x) = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{m}} \right) + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{m}} \right)\\
+ x_{\textcolor{red}{n}} \left( a_{\textcolor{violet}{1} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{m}} \right)\\
\end{multline*}

# Matrix representation of a linear transformation

\begin{multline*}
T(x) = x_{\textcolor{red}{1}} \left( a_{\textcolor{violet}{1}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m}\textcolor{red}{1}} \tilde{e}_{\textcolor{violet}{m}} \right) + x_{\textcolor{red}{2}} \left( a_{\textcolor{violet}{1} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{2}} \tilde{e}_{\textcolor{violet}{m}} \right)\\
+ x_{\textcolor{red}{n}} \left( a_{\textcolor{violet}{1} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{1}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} \tilde{e}_{\textcolor{violet}{m}} \right)\\
= \left(a_{\textcolor{violet}{1}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{1} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \tilde{e}_{\textcolor{violet}{1}} + \left( a_{\textcolor{violet}{2}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{2} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{2} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \tilde{e}_{\textcolor{violet}{2}}\\
+ \left( a_{\textcolor{violet}{m}\textcolor{red}{1}} x_{\textcolor{red}{1}} + a_{\textcolor{violet}{1} \textcolor{red}{2}} x_{\textcolor{red}{2}} + \ldots + a_{\textcolor{violet}{m} \textcolor{red}{n}} x_{\textcolor{red}{n}} \right) \tilde{e}_{\textcolor{violet}{m}}
\end{multline*}

# Matvec... again...
Finally:
$$
    \left[ T(x) \right]_{\tilde{e}} = 
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
    \end{pmatrix} = A_{T} \left[x \right]_{e}.
$$

Huh!

If indeed $e$ and $\tilde{e}$ are standard bases then

To construct matrix $A_T$ of a linear transformation $T$ we need just to know images of basis vectors: $T(e_1), \ldots, T(e_n)$, \textit{i.e.} 

$$
    e_1 \overset{T}{\rightarrow} a_{\textcolor{red}{1}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{1}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{1}}
    \end{pmatrix},
    e_2 \overset{T}{\rightarrow} a_{\textcolor{red}{2}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{2}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{2}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{2}}
    \end{pmatrix},\ldots, 
     e_n \overset{T}{\rightarrow} a_{\textcolor{red}{n}} = \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{n}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{n}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{n}}
    \end{pmatrix}
$$


# Matrix representation of a linear transformation

Sweet and easy for any $x \in V$, $x = (x_1, \ldots, x_n)^{\top}$:

$$
    x = x_1 e_1 + \ldots + x_n e_n,
$$
$$
   T(x) = x_1 T(e_1) + \ldots + x_n T(e_n).
$$

Then we want to observe $T(x)$ in standard basis $\tilde{e}$ as well:

\begin{gather*}
    \left[ T(x) \right] = x_1 a_{\textcolor{red}{1}} + \ldots + x_n a_{\textcolor{red}{n}}\\
    = x_1 \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{1}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{1}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{1}}
    \end{pmatrix} + x_2 \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{2}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{2}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{2}}
    \end{pmatrix} + \ldots + x_n \begin{pmatrix}
        a_{\textcolor{violet}{1}\textcolor{red}{n}}\\
        a_{\textcolor{violet}{2}\textcolor{red}{n}}\\
        \vdots\\
        a_{\textcolor{violet}{m}\textcolor{red}{n}}
    \end{pmatrix}.
\end{gather*}

# Matrix form of transformations' composition

# Whar if bases are not standard?

# What if bases are not standard?

# Examples
