# Proven Analytic Properties of the Riemann Zeta Function

## Table of Contents
1. [Definition and Basic Convergence](#1-definition-and-basic-convergence)
2. [Analytic Continuation](#2-analytic-continuation)
3. [Functional Equation](#3-functional-equation)
4. [Growth Rates and Vertical Line Estimates](#4-growth-rates-and-vertical-line-estimates)
5. [Zero-Free Regions](#5-zero-free-regions)
6. [Distribution of Zeros](#6-distribution-of-zeros)
7. [Moment Estimates](#7-moment-estimates)
8. [Universality Properties](#8-universality-properties)
9. [Special Values and Residues](#9-special-values-and-residues)
10. [Convexity and Subconvexity](#10-convexity-and-subconvexity)

---

## 1. Definition and Basic Convergence

### Original Definition
For $\Re(s) > 1$:
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$

### Euler Product (1737)
For $\Re(s) > 1$:
$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1-p^{-s}}$$

**Proof**: Absolutely convergent for $\sigma = \Re(s) > 1$, allows arbitrary rearrangement.

### Convergence Properties
- **Absolute convergence**: $\sigma > 1$
- **Conditional convergence**: None for the original series
- **Divergence**: $\sigma \leq 1$ (for the Dirichlet series)
- At $s = 1$: Diverges like $\log(N)$ where $N$ is partial sum limit

---

## 2. Analytic Continuation

### Riemann's Continuation (1859)
The function extends to a **meromorphic function** on $\mathbb{C}$ with:
- **Single simple pole** at $s = 1$ with residue 1
- **Holomorphic** everywhere else

### Methods of Continuation

#### Method 1: Eta Function (Dirichlet)
$$\eta(s) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} = (1-2^{1-s})\zeta(s)$$
- $\eta(s)$ converges for $\Re(s) > 0$
- Provides continuation to $\Re(s) > 0$ except at zeros of $(1-2^{1-s})$

#### Method 2: Integral Representation
For $\Re(s) > 1$:
$$\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{t^{s-1}}{e^t - 1} dt$$

#### Method 3: Hermite's Formula
$$\zeta(s) = \frac{1}{1-s} + 1 - s \int_1^{\infty} (\{x\} - \frac{1}{2}) x^{-s-1} dx$$
Valid for $\Re(s) > 0$, $s \neq 1$

---

## 3. Functional Equation

### Riemann's Functional Equation
$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

### Symmetric Form
Define $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$

Then: **$\xi(s) = \xi(1-s)$**

### Completed Zeta Function
$$Z(s) = \pi^{-s/2} \Gamma(s/2) \zeta(s)$$
Satisfies: $Z(s) = Z(1-s)$ (up to simple factors)

---

## 4. Growth Rates and Vertical Line Estimates

### On the Line $\sigma = \Re(s)$

#### Classical Bounds

**For $\sigma > 1$**: 
$$|\zeta(\sigma + it)| \leq \zeta(\sigma)$$

**For $\sigma = 1$** (not at pole):
$$\zeta(1 + it) = O(\log |t|)$$
More precisely: $|\zeta(1 + it)| \leq c \log(|t| + 2)$

**For $\sigma = 1/2$ (Critical Line)**:
- **Hardy-Littlewood (1924)**: $\zeta(1/2 + it) = O(t^{1/4})$
- **Weyl (1921)**: $\zeta(1/2 + it) = O(t^{1/6} \log t)$
- **Current best**: $\zeta(1/2 + it) = O(t^{32/205})$ (Huxley, 2005)
- **Lindelöf Hypothesis**: $\zeta(1/2 + it) = O(t^{\epsilon})$ for any $\epsilon > 0$

**For $0 < \sigma < 1$ (Critical Strip)**:
$$|\zeta(\sigma + it)| = O(|t|^{(1-\sigma)/2} \log |t|)$$
This is the **convexity bound**.

#### Phragmén-Lindelöf Principle
The maximum of $|\zeta(s)|$ on any vertical strip is attained on the boundaries.

### Mean Value Theorems

**Second Moment on Critical Line**:
$$\int_0^T |\zeta(1/2 + it)|^2 dt = T \log(T/2\pi) + (2\gamma - 1)T + O(T^{1/2})$$
where $\gamma$ is Euler's constant.

**Fourth Moment** (Ingham, 1926):
$$\int_0^T |\zeta(1/2 + it)|^4 dt \sim \frac{T}{2\pi^2} (\log T)^4$$

---

## 5. Zero-Free Regions

### Classical Zero-Free Region (de la Vallée Poussin, 1896)
There exists $c > 0$ such that $\zeta(s) \neq 0$ for:
$$\sigma > 1 - \frac{c}{\log(|t| + 2)}$$

### Improvements
**Korobov-Vinogradov (1958)**: Zero-free for
$$\sigma > 1 - \frac{c}{(\log |t|)^{2/3}(\log \log |t|)^{1/3}}$$

### On Special Lines
- **$\sigma = 1$**: No zeros (crucial for Prime Number Theorem)
- **$\sigma > 1$**: No zeros (from Euler product)
- **$\sigma < 0$**: Only "trivial zeros" at $s = -2, -4, -6, ...$
- **$\sigma = 0$**: No zeros except trivial ones

---

## 6. Distribution of Zeros

### Riemann-von Mangoldt Formula
Let $N(T)$ = number of zeros with $0 < \Im(\rho) \leq T$ in critical strip.

$$N(T) = \frac{T}{2\pi} \log \frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T)$$

### Density Results

**Zero Density Estimates**: For $\sigma \geq 1/2$, let $N(\sigma, T)$ be the number of zeros with $\Re(\rho) \geq \sigma$ and $0 < \Im(\rho) \leq T$.

- **Ingham**: $N(\sigma, T) = O(T^{3(1-\sigma)/(2-\sigma)} \log^5 T)$ for $1/2 \leq \sigma < 1$
- **Density Hypothesis**: $N(\sigma, T) = O(T^{2(1-\sigma)+\epsilon})$ for any $\epsilon > 0$

### Zeros on Critical Line

**Hardy's Theorem (1914)**: Infinitely many zeros lie on $\Re(s) = 1/2$.

**Selberg (1942)**: A positive proportion of zeros lie on the critical line.

**Conrey (1989)**: At least 40% of zeros lie on the critical line.

### Pair Correlation
**Montgomery (1973)**: Introduced pair correlation conjecture about spacing of zeros.

---

## 7. Moment Estimates

### On the Critical Line $\sigma = 1/2$

For $k \in \mathbb{N}$:
$$\int_0^T |\zeta(1/2 + it)|^{2k} dt$$

**Known Results**:
- $k = 1$: $\sim cT \log T$
- $k = 2$: $\sim \frac{T}{2\pi^2}(\log T)^4$
- $k = 3$: Upper bound $O(T(\log T)^9)$
- General $k$: Conjectured $\sim c_k T(\log T)^{k^2}$

### Moments in the Critical Strip
For $1/2 < \sigma < 1$:
$$\int_0^T |\zeta(\sigma + it)|^2 dt \sim \frac{\zeta(2\sigma)T}{2\pi}$$

---

## 8. Universality Properties

### Voronin's Universality Theorem (1975)

Let $K$ be a compact subset of the strip $\{s : 1/2 < \Re(s) < 1\}$ with connected complement. Let $f$ be a non-vanishing continuous function on $K$, holomorphic in the interior of $K$.

Then for any $\epsilon > 0$:
$$\liminf_{T \to \infty} \frac{1}{T} \text{meas}\{t \in [0,T] : \max_{s \in K}|\zeta(s+it) - f(s)| < \epsilon\} > 0$$

**Interpretation**: $\zeta(s)$ approximates any reasonable holomorphic function through vertical translations.

### Effective Universality
**Bagchi (1981)**: The lower density is at least $\exp(-c/\epsilon^2)$ for some constant $c$.

---

## 9. Special Values and Residues

### At Integers

**Positive Even Integers**:
$$\zeta(2n) = \frac{(-1)^{n+1}(2\pi)^{2n}B_{2n}}{2(2n)!}$$
where $B_{2n}$ are Bernoulli numbers.

Examples:
- $\zeta(2) = \pi^2/6$
- $\zeta(4) = \pi^4/90$
- $\zeta(6) = \pi^6/945$

**Negative Integers**:
$$\zeta(-n) = -\frac{B_{n+1}}{n+1}$$

**At $s = 0$**: $\zeta(0) = -1/2$

**At $s = 1$**: Simple pole with residue 1

### Laurent Expansion at $s = 1$
$$\zeta(s) = \frac{1}{s-1} + \gamma + \gamma_1(s-1) + \gamma_2(s-1)^2 + ...$$
where $\gamma = 0.5772...$ is Euler's constant.

### Values at Odd Positive Integers
- **Apéry's Theorem (1979)**: $\zeta(3)$ is irrational
- $\zeta(3) = 1.202056...$
- Irrationality of $\zeta(2n+1)$ for $n > 1$ mostly unknown

---

## 10. Convexity and Subconvexity

### Phragmén-Lindelöf Convexity Bound
For $0 \leq \sigma \leq 1$:
$$|\zeta(\sigma + it)| \ll |t|^{(1-\sigma)/2 + \epsilon}$$

This follows from the functional equation and convexity principle.

### Subconvexity Problem
Any improvement over the convexity bound is called **subconvexity**.

**Weyl's Bound**: First subconvexity result
$$\zeta(1/2 + it) = O(t^{1/6 + \epsilon})$$

### Burgess Bound
For Dirichlet L-functions (generalizing $\zeta$):
$$L(1/2 + it, \chi) \ll q^{3/16 + \epsilon}$$
where $q$ is the conductor.

### Applications of Subconvexity
- Quantum unique ergodicity
- Bounds on Fourier coefficients of modular forms
- Equidistribution problems

---

## Summary of Key Unproven Conjectures

### Riemann Hypothesis (RH)
All non-trivial zeros have $\Re(s) = 1/2$.

### Generalized Riemann Hypothesis (GRH)
Same for all Dirichlet L-functions.

### Lindelöf Hypothesis
$$\zeta(1/2 + it) = O(t^{\epsilon})$$ for any $\epsilon > 0$.

### Density Hypothesis
$$N(\sigma, T) = O(T^{2(1-\sigma) + \epsilon})$$ for any $\epsilon > 0$.

### Montgomery's Pair Correlation Conjecture
The pair correlation of zeros follows random matrix theory (GUE) statistics.

### Moments Conjecture
$$\int_0^T |\zeta(1/2 + it)|^{2k} dt \sim c_k T(\log T)^{k^2}$$

---

## Key Techniques and Methods

### Complex Analysis Tools
1. **Maximum modulus principle**
2. **Phragmén-Lindelöf principle**
3. **Jensen's formula**
4. **Hadamard factorization**
5. **Contour integration**

### Number-Theoretic Methods
1. **Euler-Maclaurin formula**
2. **Poisson summation**
3. **Exponential sums**
4. **Sieve methods**
5. **Multiplicative functions**

### Analytic Methods
1. **Mellin transforms**
2. **Functional equations**
3. **Approximate functional equations**
4. **Stationary phase**
5. **Saddle point method**

---

## References and Further Reading

### Classical Sources
- Riemann, B. (1859) "Über die Anzahl der Primzahlen unter einer gegebenen Grösse"
- Hadamard, J. (1896) "Sur la distribution des zéros de la fonction ζ(s)"
- de la Vallée Poussin (1896) "Recherches analytiques sur la théorie des nombres"

### Modern Treatments
- Titchmarsh, E.C. "The Theory of the Riemann Zeta-Function"
- Edwards, H.M. "Riemann's Zeta Function"
- Ivić, A. "The Riemann Zeta-Function"
- Karatsuba, A.A. & Voronin, S.M. "The Riemann Zeta-Function"

### Recent Advances
- Conrey, J.B. (2003) "The Riemann Hypothesis"
- Soundararajan, K. (2009) "Moments of the Riemann zeta function"
- Young, M. (2017) "The fourth moment of Dirichlet L-functions"

---

*This document compiles proven results as of 2024. The field remains highly active with ongoing research in all areas mentioned.*