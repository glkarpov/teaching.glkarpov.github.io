---
title: "Линейная алгебра"
subtitle: "Нормированные пространства"
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

## Пространства со скалярным произведением (Inner product spaces)

::: {.callout-def}
#### Cкалярное произведение
Пусть $\mathbb{V}$ — векторное пространство. Скалярное произведение на $\mathbb{V}$ — это **функция**, которая каждой паре векторов $\mathbf{x}, \mathbf{y}$ сопоставляет скаляр, обозначаемый как $(\mathbf{x}, \mathbf{y})$ или $\langle \mathbf{x}, \mathbf{y} \rangle$, так что выполняются свойства 1–4 ниже.
:::

\begin{enumerate}
\item Симметричность (сопряжённая): $(\mathbf{x}, \mathbf{y})=(\mathbf{y}, \mathbf{x})$,

\item Линейность: $(\alpha \mathbf{x}+\beta \mathbf{y}, \mathbf{z})=\alpha(\mathbf{x}, \mathbf{z})+\beta(\mathbf{y}, \mathbf{z})$ для любых векторов $\mathbf{x}, \mathbf{y}, \mathbf{z}$ и любых скаляров $\alpha, \beta$,

\item Неотрицательность: $(\mathbf{x}, \mathbf{x}) \geq 0 \quad \forall \mathbf{x}$,

\item Невырожденность: $(\mathbf{x}, \mathbf{x})=0$ тогда и только тогда, когда $\mathbf{x}=\mathbf{0}$.
\end{enumerate}

## Слайд для записей

## Скалярное произведение в координатных пространствах

:::{.callout-definition}
Скалярное произведение двух векторов $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ — это число, вычисляемое по формуле:

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n$$
:::

**Геометрический смысл:**
$$\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| \cdot |\mathbf{v}| \cdot \cos \theta$$

где $\theta$ — угол между векторами $\mathbf{u}$ и $\mathbf{v}$.

## Обозначения скалярного произведения
### Различные способы записи

::: {.columns}

::: {.column width="50%"}
### 1. Через транспонирование
$$\mathbf{u}^T \mathbf{v}$$

**Матричная форма:**
$$\mathbf{u}^T \mathbf{v} = \begin{bmatrix} u_1 & u_2 & \cdots & u_n \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$$

**Результат:**
$$= u_1 v_1 + u_2 v_2 + \cdots + u_n v_n$$
:::

::: {.column width="50%"}
### 2. Через угловые скобки
$$\langle \mathbf{u}, \mathbf{v} \rangle$$

**Альтернативно:**
- $\mathbf{u} \cdot \mathbf{v}$ — точечное произведение

**Обозначения эквивалентны:**
$$\mathbf{u}^T \mathbf{v} = \langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v}$$
:::

:::

## Нормированные пространства

**Свойства нормы**:

1. Однородность: $\|\alpha \mathbf{v}\|=|\alpha| \cdot\|\mathbf{v}\|$ для любых $\mathbf{v}$ и скаляров $\alpha$.

2. Неравенство треугольника: $\|\mathbf{u}+\mathbf{v}\| \leq\|\mathbf{u}\|+\|\mathbf{v}\|$.

3. Неотрицательность: $\|\mathbf{v}\| \geq 0$ для всех векторов $\mathbf{v}$.

4. Невырожденность: $\|\mathbf{v}\|=0$ тогда и только тогда, когда $\mathbf{v}=\mathbf{0}$.

:::: {.callout-def}
#### Определение (норма и нормированное пространство)

Пусть в векторном пространстве $V$ каждой вектору $\mathbf{v}$ сопоставлено число $\|\mathbf{v}\|$ так, что выполняются свойства 1–4 выше. Тогда функция $\mathbf{v} \mapsto\|\mathbf{v}\|$ называется нормой. Векторное пространство $V$, оснащённое нормой, называется нормированным пространством.
::::

## Разные нормированные пространства
Любое пространство со скалярным произведением является нормированным, поскольку норма $\|\mathbf{v}\|= \sqrt{(\mathbf{v}, \mathbf{v})}$ удовлетворяет свойствам 1–4. Однако существуют и другие нормы. Например, для $p, 1 \leq p<\infty$, можно определить норму $\|\cdot\|_p$ на $\mathbb{R}^n$ как
$$
\|\mathbf{x}\|_p=\left(\left|x_1\right|^p+\left|x_2\right|^p+\ldots+\left|x_n\right|^p\right)^{1 / p}=\left(\sum_{k=1}^n\left|x_k\right|^p\right)^{1 / p} .
$$

Также можно определить норму $\|\cdot\|_{\infty}$ (при $p=\infty$) как
$$
\|\mathbf{x}\|_{\infty}=\max \left\{\left|x_k\right|: k=1,2, \ldots, n\right\}
$$


## Ортогональность. Ортогональные и ортонормированные базисы.

::: {.callout-def}
#### Определение

Два вектора $\mathbf{u}$ и $\mathbf{v}$ называются ортогональными (перпендикулярными), если $(\mathbf{u}, \mathbf{v})=0$. Запись $\mathbf{u} \perp \mathbf{v}$ обозначает ортогональность векторов.
:::

Для ортогональных векторов $\mathbf{u}$ и $\mathbf{v}$ верно тождество Пифагора:
$$
\|\mathbf{u}+\mathbf{v}\|^2=\|\mathbf{u}\|^2+\|\mathbf{v}\|^2 \quad \text { if } \mathbf{u} \perp \mathbf{v}
$$

Доказательство:
$$
\begin{aligned}
\|\mathbf{u}+\mathbf{v}\|^2= & (\mathbf{u}+\mathbf{v}, \mathbf{u}+\mathbf{v})=(\mathbf{u}, \mathbf{u})+(\mathbf{v}, \mathbf{v})+(\mathbf{u}, \mathbf{v})+(\mathbf{v}, \mathbf{u}) \\ = & \|\mathbf{u}\|^2+\|\mathbf{v}\|^2 \\
& ((\mathbf{u}, \mathbf{v})=(\mathbf{v}, \mathbf{u})=0 \text { because of orthogonality }) .
\end{aligned}
$$
