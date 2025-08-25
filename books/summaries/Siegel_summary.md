# Summary: Notes on Siegel Modular Forms
**Author:** Kevin Buzzard  
**Date:** April 26, 2012 (Last modified Oct 2005)  
**Pages:** 15  

## Overview

These notes provide an introduction to Siegel modular forms, focusing on genus 2 forms with full level structure. The document covers fundamental definitions, structural theorems, Hecke operators, and connections to Galois representations and number theory.

## Key Definitions and Concepts

### 1. Siegel Upper Half Space
- **Definition**: $H_n^+$ is the set of $n \times n$ complex matrices $\Omega = X + iY$ where:
  - $\Omega^t = \Omega$ (symmetric)
  - $Y$ is positive definite
- **Dimension**: $n(n+1)/2$
- **Action**: The symplectic group $\text{Sp}(2n, \mathbb{R})$ acts on $H_n^+$ via:
  $$\begin{pmatrix} A & B \\ C & D \end{pmatrix} \Omega = (A\Omega + B)(C\Omega + D)^{-1}$$

### 2. Symplectic Groups
- **GSp(2n, R)**: Invertible $2n \times 2n$ matrices $M$ such that $J[M] = \nu(M)J$ for $\nu(M) \in R^×$
- **Sp(2n, R)**: Kernel of the multiplier map $\nu$
- **Key matrix**: $J = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$

### 3. Siegel Modular Forms
**Definition**: A holomorphic function $f: H_n^+ \to \mathbb{C}$ such that for all $\gamma = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \in \text{Sp}(2n, \mathbb{Z})$:
$$f(\gamma\Omega) = \det(C\Omega + D)^k f(\Omega)$$

**Boundedness conditions**:
- Automatically satisfied for $n \geq 2$
- For $n = 1$: require boundedness on fundamental domain
- Weight $k$ is an integer

## Fourier Expansions

### General Structure
Siegel modular forms admit Fourier expansions:
$$f = \sum c(A) \prod_{i \leq j} q_{i,j}^{a_{i,j}}$$
where:
- $q_{i,j} = e^{2\pi\sqrt{-1}z_{i,j}}$
- $A$ is the symmetric matrix with entries $a_{i,j}$
- $c(A) = 0$ unless $A$ is positive semi-definite (Koecher's theorem for $n \geq 2$)

### Key Properties
- **Periodicity**: $f$ is periodic with period 1 in each variable
- **Transformation law**: $c(A[U]) = \det(U)^k c(A)$ for $U \in \text{GL}_n(\mathbb{Z})$
- **Weight restrictions**: No non-zero forms of odd weight when $n$ is odd

## The Φ Operator

**Definition**: Maps weight $k$ forms of genus $n$ to weight $k$ forms of genus $n-1$ by setting $q_{i,n} = 0$.

**Properties**:
- Always surjective
- **Cusp forms**: Elements in the kernel of Φ
- **Eisenstein series**: Provide one-sided inverse when $k > n+1$ and $k$ even

## Eisenstein Series

For $k > n+1$ even, Eisenstein series exist:
$$E_k(\Omega) = \sum_{\gamma} \det(C\Omega + D)^{-k}$$
where the sum is over appropriate coset representatives.

**Lifts**: If $0 \leq r < n$, $k > n + r + 1$ even, and $f$ is a genus $r$ cusp form, there exists an Eisenstein lift to a genus $n$ non-cusp form.

## Structure Theorem for Genus 2 (Igusa's Result)

### Ring Structure
$$\bigoplus_{k \geq 0, 2|k} M_k = \mathbb{C}[E_4, E_6, E_{10}, E_{12}]$$
where $M_k$ denotes genus 2 modular forms of weight $k$.

### Dimensional Results
- $M_0 = \mathbb{C}$, $M_k = 0$ for $1 \leq k \leq 3$
- $M_4$ is one-dimensional
- General dimension formula: $\text{dim } M_k = O(k^{n(n+1)/2})$

### Fourier Expansion (Genus 2)
For $\Omega = \begin{pmatrix} \tau & z \\ z & \tau' \end{pmatrix}$ with $q = e^{2\pi i\tau}$, $\zeta = e^{2\pi iz}$, $q' = e^{2\pi i\tau'}$:
$$F = \sum_{r,n,m \in \mathbb{Z}} a(n,r,m) q^n \zeta^r (q')^m$$

The coefficient $a(n,r,m)$ vanishes unless $\begin{pmatrix} n & r/2 \\ r/2 & m \end{pmatrix}$ is positive semi-definite.

## Galois Representations and Decomposition (Genus 2)

For even weight $k$, the space $M_k$ decomposes into 4 subspaces:

### 1. "Very" Eisenstein
- **Dimension**: 1 (or 0 if $k = 2$)
- **Galois representation**: $1 \oplus \omega^{k-1} \oplus \omega^{k-2} \oplus \omega^{2k-3}$

### 2. Classical Eisenstein
- **Source**: Classical cusp forms via Eisenstein construction
- **Dimension**: Same as classical weight $k$ cusp forms
- **Galois representation**: $\rho_f \otimes (1 \oplus \omega^{k-2})$
- **Kicks in**: At $k = 12$

### 3. Cuspidal (from Jacobi forms)
- **Source**: Classical cusp forms of weight $2k-2$ via Jacobi forms
- **Galois representation**: $\omega^{k-2} \oplus \omega^{k-1} \oplus \rho_f$
- **Kicks in**: At $k = 10$

### 4. "Interesting" Cuspidal
- **First appearance**: Weight 20 (1-dimensional space)
- **Dimensions**: $k = 20,22,24,26,28$ give $1,1,2,2,3$ respectively
- **Special property**: Rational Fourier expansions at weights 24 and 26

## Hecke Operators (Genus 2)

### Basic Setup
- **Group**: $\Gamma = \text{Sp}_4(\mathbb{Z})$
- **Semigroup**: $\Delta$ consists of $4 \times 4$ integral matrices in $\text{GSp}_4(\mathbb{Q})$ with positive $\nu$
- **Action**: $(f|\delta)(\Omega) = \nu(\delta)^{2k-3} \det(C\Omega + D)^{-k} f(\delta\Omega)$

### Key Operators
- **T(n)**: Sum over double cosets with $\nu(\delta) = n$
- **T(p)**: Corresponds to $\text{diag}(1,1,p,p)$
- **$T_1(p^2)$**: Corresponds to $\text{diag}(1,p,p^2,p)$
- **$S_p$**: Corresponds to $\text{diag}(p,p,p,p)$ (acts as $p^{2k-6}$)

### Satake Parameters
The local Hecke algebra at $p$ maps to $\mathbb{Q}[x_0, x_1, x_2, (x_0x_1x_2)^{-1}]^W$ where $W$ is the Weyl group.

**Key relations**:
- $t = x_0(1 + x_1)(1 + x_2)$ (trace of 4D representation)
- $\rho_0 = x_0^2 x_1 x_2$ (norm of 4D representation)
- $\rho_1 = \rho_0(x_1 + x_1^{-1} + x_2 + x_2^{-1})$

### Explicit Formulas
**T(p) action**: For $F = \sum a(n,r,m) q^n \zeta^r (q')^m$:
$$b(n,r,m) = p^{2k-3} a(n/p, r/p, m/p) + p^{k-2} a(pn, r, m/p) + \text{(additional terms)}$$

## Applications to L-adic Representations

For a Siegel eigenform with eigenvalues $\lambda$ for $T(p)$ and $\mu$ for $T_1(p^2)$ in weight $k$:

**Characteristic polynomial** of Frobenius (4D spinor representation):
$$X^4 - \lambda X^3 + (p\mu + (p^3 + p)p^{2k-6})X^2 - \lambda p^{2k-3} X + p^{4k-6}$$

The eigenvalues are $\{x_0, x_0 x_1, x_0 x_1 x_2, x_0 x_2\}$.

## Key Theorems and Results

### Koecher's Theorem
For $n \geq 2$, Fourier coefficients $c(A) = 0$ unless the symmetric matrix $A$ is positive semi-definite.

### Igusa's Structure Theorem
The ring of even weight genus 2 Siegel modular forms is a polynomial ring in 4 generators.

### Dimension Growth
The dimension of weight $k$ forms grows like $O(k^{n(n+1)/2})$ as $k \to \infty$.

## Connections to Number Theory

### Classical Modular Forms
- Φ operator provides connection to classical theory
- Eisenstein series give explicit lifts from lower genus

### Arithmetic Applications
- Galois representations encode arithmetic information
- L-functions and special values
- Connections to quadratic forms and theta series

### Hecke Theory
- Rich structure of Hecke operators
- Satake parameters encode local information
- Computational methods for eigenvalues

## Notable Features and Limitations

**Advantages over classical case**:
- Richer geometric structure
- Multiple types of automorphic representations
- Connections to higher-dimensional algebraic geometry

**Challenges**:
- No general explicit formulas for Eisenstein series Fourier coefficients (unlike genus 1)
- More complex Hecke operator calculations
- Limited computational tools compared to classical case

**Computational Aspects**:
- Explicit algorithms for genus 2, weight 4 (Skoruppa)
- Automated computations possible for low weights and level 1
- Connection to computing Galois representations

This summary captures the essential mathematical content of Buzzard's notes, providing both the fundamental theory and specific results for genus 2 Siegel modular forms, along with their connections to broader areas of number theory and arithmetic geometry.