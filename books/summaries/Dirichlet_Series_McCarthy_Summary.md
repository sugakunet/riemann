# Comprehensive Summary: Dirichlet Series by McCarthy

## Overview
This comprehensive text on Dirichlet series provides a thorough treatment from basic foundations through advanced topics in Hilbert spaces, ergodic theory, and interpolation problems. The work bridges classical analytic number theory with modern functional analysis.

## Part I: Foundations (Chapters 1-2)

### Chapter 1: Introduction and Basic Properties

#### Fundamental Definition
A **Dirichlet series** is a series of the form:
$$\sum_{n=1}^{\infty} \frac{a_n}{n^s} = f(s), \quad s \in \mathbb{C}$$
where $s = \sigma + it$ with $\sigma = \Re(s)$ and $t = \Im(s)$.

#### Key Example: Riemann Zeta Function
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$
- Converges absolutely for $\sigma > 1$
- Diverges for $\sigma \leq 0$ or $0 < s \leq 1$
- Can be analytically continued to $\mathbb{C} \setminus \{1\}$

#### Euler Product Formula (Theorem 1.5)
For $\sigma > 1$:
$$\prod_{p \in \mathbb{P}} \left(1 - \frac{1}{p^s}\right)^{-1} = \zeta(s) = \sum_{n=1}^{\infty} n^{-s}$$

This establishes the fundamental connection between Dirichlet series and prime numbers.

#### Important Arithmetic Functions
- **Möbius Function**: $\frac{1}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s}$
- **Divisor Function**: $\zeta^2(s) = \sum_{k=1}^{\infty} \frac{d(k)}{k^s}$
- **Euler Totient**: $\frac{\zeta(s-1)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\phi(n)}{n^s}$ for $\sigma > 2$

### Chapter 2: Prime Number Theorem

#### Critical Result (Theorem 2.19)
The Riemann zeta function has no zeros on the line $\{\Re(s) = 1\}$.

#### Prime Number Theorem (Theorem 2.2)
$$\pi(x) \sim \frac{x}{\log x}$$
This is equivalent to $\Theta(x) \sim x$ where $\Theta(x) = \sum_{p \leq x} \log p$.

## Part II: Convergence Theory (Chapters 3-5)

### Chapter 3: Convergence of Dirichlet Series

#### Fundamental Abscissae
- **Abscissa of convergence** ($\sigma_c$): Boundary of convergence region
- **Abscissa of absolute convergence** ($\sigma_a$): Where series converges absolutely
- **Abscissa of uniform convergence** ($\sigma_u$): Where uniform convergence occurs
- **Abscissa of bounded convergence** ($\sigma_b$): Where series converges to bounded function

#### Key Inequality (Proposition 3.10)
For any Dirichlet series: $\sigma_c \leq \sigma_a \leq \sigma_c + 1$

#### Convergence in Sectors (Theorem 3.1)
If the series converges at $s_0$, it converges uniformly in sectors:
$$\{s : -\pi/2 + \delta < \arg(s - s_0) < \pi/2 - \delta\}$$

### Chapter 4: Perron's and Schnee's Formulae

#### Perron's Formula (Theorem 4.5)
For $f(s) = \sum a_n n^{-s}$, the summatory function $F(x) = \sum_{n \leq x} a_n$ satisfies:
$$F(x) = \frac{1}{2\pi i} \lim_{T \to \infty} \int_{\sigma-iT}^{\sigma+iT} \frac{f(w)}{w} x^w dw$$
for $\sigma > \max(0, \sigma_c)$.

#### Schnee's Formula (Theorem 4.11)
Allows extraction of individual coefficients:
$$\lim_{T \to \infty} \frac{1}{2T} \int_{-T}^T f(\sigma + it)e^{i\lambda t} dt = \begin{cases} a_n n^{-\sigma} & \text{if } \lambda = \log n \\ 0 & \text{otherwise} \end{cases}$$

### Chapter 5: Uniform and Bounded Convergence

#### Bohr's Theorem (Theorem 5.4)
If a Dirichlet series extends to a bounded function in $\Omega_\rho$, it converges uniformly in $\Omega_{\rho+\delta}$ for all $\delta > 0$.

#### Bohnenblust-Hille Theorem (Theorem 5.26)
The sharp bound: $\sigma_a - \sigma_u \leq 1/2$

## Part III: Hilbert Spaces and Functional Analysis (Chapter 6)

### Hilbert Space of Dirichlet Series
$$H^2 = \left\{ \sum_{n=1}^{\infty} a_n n^{-s} : \sum_{n=1}^{\infty} |a_n|^2 < \infty \right\}$$

For any $f \in H^2$, the abscissa of absolute convergence $\sigma_a \leq 1/2$.

### Beurling's Problem
For odd 2-periodic function $\psi$, the system $\{\psi(nx)\}_{n \in \mathbb{N}^+}$ forms a Riesz basis for $L^2([0,1])$ if and only if both $g$ and $1/g$ are multipliers of $H^2$, where $g(s) = \sum c_n n^{-s}$ is the associated Dirichlet series.

### Multiplier Algebras
**Definition**: $\text{Mult}(X) = \{\phi : \phi f \in X \text{ for all } f \in X\}$

**Key Result (Theorem 6.42)**: Hedenmalm-Lindqvist-Seip
$$\text{Mult}(H^2_w) \cong H^{\infty}(\Omega_0) \cap \mathcal{D}$$

### Weighted Hilbert Spaces
$$H^2_w = \left\{ \sum a_n n^{-s} : \sum |a_n|^2 w_n < \infty \right\}$$

Example weights: $w_n = (\log n)^\alpha$ for $\alpha < 0$.

## Part IV: Advanced Topics

### Chapter 7: Ergodic Theory and Characters

#### Kronecker Flows
The Kronecker flow on $\mathbb{T}^{\infty}$ is ergodic if and only if $\{\alpha_n\}$ are linearly independent over $\mathbb{Q}$.

#### Helson's Theorem (Theorem 7.15)
For $f \in H^2$ and almost every character $\chi$, the function $f_\chi(s) = \sum a_n \chi(n) n^{-s}$ extends to $H^2_i(\Omega_0)$ and:
$$\lim_{T \to \infty} \frac{1}{2T} \int_{-T}^T |f_\chi(it)|^2 dt = \sum |a_n|^2$$

#### Dirichlet's Theorem on Primes (Theorem 7.21)
For $\gcd(l,q) = 1$:
$$\sum_{p \equiv l \pmod{q}} \frac{1}{p} = \infty$$

### Characters and L-functions

#### Dirichlet L-function
For a Dirichlet character $\chi$ modulo $q$:
$$L(s,\chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$$

These functions are crucial for:
- Proving infinitude of primes in arithmetic progressions
- Understanding distribution of primes
- Connections to class field theory

### Interpolation Theory

#### Carleson's Interpolation Theorem
A sequence is interpolating for $H^{\infty}(\Omega_0)$ if and only if it satisfies:
1. Weak separation condition
2. Strong separation condition
3. Carleson measure condition

### Applications and Connections

#### Number Theory
- Prime distribution via Euler products
- Arithmetic functions as Dirichlet series coefficients
- L-functions and class field theory

#### Harmonic Analysis
- Almost periodic functions (Besicovitch's theorem)
- Kronecker flows and ergodic theory
- Character theory on infinite-dimensional tori

#### Complex Analysis
- Hardy spaces $H^p(\Omega_0)$
- Zero distribution of analytic functions
- Interpolation problems

#### Functional Analysis
- Reproducing kernel Hilbert spaces
- Multiplier algebras
- Composition operators

## Key Insights and Themes

1. **Analytic-Arithmetic Duality**: The analytic properties of Dirichlet series (zeros, poles, growth) encode arithmetic information about their coefficients.

2. **Convergence Hierarchy**: The relationships between different types of convergence ($\sigma_c \leq \sigma_b = \sigma_u \leq \sigma_a \leq \sigma_c + 1$) reveal the subtle structure of these series.

3. **Functional Analytic Framework**: Modern theory places Dirichlet series in the context of Hilbert spaces, multiplier algebras, and operator theory.

4. **Probabilistic Methods**: Characters and ergodic theory provide probabilistic tools for deterministic results about primes and arithmetic functions.

5. **Interdisciplinary Connections**: The theory connects number theory, harmonic analysis, complex analysis, functional analysis, and ergodic theory in profound ways.

## Notable Open Problems Mentioned

1. **Lindelöf Hypothesis**: Growth estimates for $|\zeta^k(\sigma + it)|^2$
2. **Optimal interpolation conditions** for various function spaces
3. **Complete characterization** of zero sets for weighted Dirichlet series spaces

This comprehensive work demonstrates that Dirichlet series serve as a fundamental bridge between diverse areas of mathematics, with applications ranging from the distribution of prime numbers to modern operator theory.