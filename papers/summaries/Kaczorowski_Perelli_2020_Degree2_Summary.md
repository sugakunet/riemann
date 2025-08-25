# Classification of L-functions of Degree 2 and Conductor 1
## Kaczorowski & Perelli (2020) - Detailed Mathematical Summary

### Paper Overview
**Authors:** J. Kaczorowski, A. Perelli  
**Title:** Classification of L-functions of Degree 2 and Conductor 1  
**Year:** 2020  
**arXiv:** 2009.12329v2  

This paper provides a complete classification of functions F of degree 2 and conductor 1 in the extended Selberg class S♯ using a new numerical invariant χ_F (the "eigenweight").

### Key Innovation: The Eigenweight χ_F

**Definition:** For normalized F ∈ S♯ with degree 2 and conductor 1:
```
χ_F = ξ_F + H_F(2) + 2/3
```
where:
- ξ_F is the ξ-invariant 
- H_F(2) is the second H-invariant
- Both are easily computed from the functional equation data

**Key Examples:**
- If χ_F = 0 ⟹ F(s) = ζ(s)²
- If χ_F = 121/2 ⟹ F(s) = L(s + 11/2, Δ) (Ramanujan L-function)

### Main Classification Theorem

**Theorem 1.1:** Let F ∈ S♯ of degree 2 and conductor 1 be normalized. Then χ_F ∈ ℝ and:

**(i) Holomorphic Case (χ_F > 0):**
- There exists a holomorphic cusp form f of level 1 and even integral weight k = 1 + √(2χ_F)
- F(s) = L(s + (k-1)/2, f)

**(ii) Trivial Case (χ_F = 0):**
- F(s) = ζ(s)²

**(iii) Maass Case (χ_F < 0):**
- There exists a Maass form u of level 1, weight 0, with eigenvalue 1/4 + κ² = (1-2χ_F)/4
- F(s) = L(s, u)
- Parity ε = (1-ω_F)/2 where ω_F is the root number

### Normalization Process

**Definition:** F ∈ S♯ is normalized if:
1. Internal shift θ_F = 0
2. First nonvanishing Dirichlet coefficient equals 1

**Key Properties of Normalized Functions (Lemma 4.1):**
- Dirichlet coefficients are real
- ξ_F is an even integer  
- ω_F = -e^(iπξ_F/2)
- All H-invariants are real
- γ-factor satisfies γ(s) = γ̄(s)

### Mathematical Framework

#### Extended Selberg Class S♯
Functions F(s) = Σ a(n)/n^s with:
- Absolute convergence for σ > 1
- (s-1)^m F(s) entire of finite order for some m ≥ 0
- Functional equation: F(s)γ(s) = ωγ(1-s)F(1-s)
- γ-factor: γ(s) = Q^s ∏ᵣⱼ₌₁ Γ(λⱼs + μⱼ)

#### Invariants and Parameters
**Degree and Conductor:**
- d = 2Σλⱼ = 2 (degree 2 case)
- q = (2π)^d Q² ∏λⱼ^(2λⱼ) = 1 (conductor 1 case)

**H-invariants:** H_F(n) = 2Σᵣⱼ₌₁ Bₙ(μⱼ)/λⱼ^(n-1)
- H_F(0) = d = 2
- H_F(1) = ξ_F  
- H_F(2) = 2Σᵣⱼ₌₁ (μⱼ² - μⱼ + 1/6)/λⱼ

### Proof Strategy and Key Innovations

#### 1. Structural Invariants d_ℓ(F)
The proof relies on analyzing structural invariants d_ℓ(F) that appear in the asymptotic expansion:
```
h_F(s) ≈ (ω_F/√(2π)) * (q^(1/d)/(2πd))^((1/2-s)) * Σ d_ℓ(F)Γ_d(s*_ℓ - s)
```

**Key Result (Proposition 4.1):** For every N ≥ 2, the invariants d₀(F),...,d_N(F) lie on universal algebraic varieties defined by quadratic forms Q_N independent of F.

#### 2. Virtual γ-factors
**Definition:** The paper introduces "virtual γ-factors":
- **Hecke type:** γ(s) = (2π)^(-s)Γ(s + μ) with μ > 0
- **Maass type:** γ(s) = π^(-s)Γ((s+ε+iκ)/2)Γ((s+ε-iκ)/2) with ε ∈ {0,1}, κ ≥ 0

**Eigenweight for virtual γ-factors:**
```
χ_γ = { 2μ² (Hecke type)
       {-2κ² (Maass type)
```

#### 3. Transformation Formula for Nonlinear Twists
**Lemma 4.2:** For α ∈ Spec(F) and integer M ≥ 0:
```
F(s; f) = Σᴹₘ₌₀ Wₘ(s,α)F(s + m/2, α) + H_M(s,α)
```
where f(n,α) = n + α√n and Wₘ(s,α) are explicit polynomials in the structural invariants.

### Period Functions and Final Proof

#### Definition of Period Functions
For F as in Theorem 1.1 and z ∈ upper half-plane:
```
f(z) = Σ a(n)n^λ e(nz)
```
where λ = μ (if χ_F > 0) or λ = iκ (if χ_F ≤ 0).

The period function is:
```
ψ(z) = f(z) - z^(-2λ-1) f(-1/z)
```

#### Key Propositions
**Proposition 6.1 (Hecke case, χ_F > 0):**
ψ(z) = Q_H(z) + P_H(z) + L(z)
where Q_H(z), P_H(z) are holomorphic for |arg(z)| < π.

**Proposition 6.2 (Maass case, χ_F ≤ 0):**
ψ(z) = Q_M(z) + P_M(z) + L(z)
where Q_M(z) is holomorphic for |arg(z)| < π.

#### Contradiction Argument
The proof concludes by showing that if R(s) = S_F(s)/S_γ(s) is not constant, then f(z) would have analytic continuation to an angular region below the real axis, contradicting Lemma 6.1 (f cannot be entire due to growth properties of Dirichlet coefficients).

### Applications and Corollaries

**Corollary 1.1:** Every F ∈ S♯ of degree 2 and conductor 1 belongs, modulo normalization, to one of the three families in Theorem 1.1.

**Corollary 1.2:** Every F ∈ S of degree 2 and conductor 1 is an automorphic L-function.

This confirms the conjecture that functions in the Selberg class are automorphic L-functions, at least for the case of degree 2 and conductor 1.

### Connections to Classical Results

#### Converse Theorems
The result provides a sharp form of classical converse theorems of:
- **Hecke:** For holomorphic modular forms
- **Maass:** For non-holomorphic modular forms

The eigenweight χ_F precisely determines which type of L-function F represents, making the classification algorithmic.

#### Relationship to Riemann Hypothesis
The paper works within the framework of the Selberg class, which assumes a generalized Riemann hypothesis. The classification helps understand the structure of degree 2 L-functions, which are central to many problems in analytic number theory.

### Technical Innovations

1. **Universal Algebraic Varieties:** The structural invariants lie on algebraic varieties independent of the specific L-function.

2. **Mittag-Leffler Functions:** The proof uses special functions E_{β}(w) = E_{1,β}(-w) to analyze period integrals.

3. **Three-term Functional Equation:** The period function ψ(z) satisfies:
   ```
   ψ(z) = ψ(z+1) + (z+1)^(-2μ-1) ψ(z/(z+1))
   ```

### Mathematical Significance

This paper represents a major advance in understanding the Selberg class by:

1. **Providing Complete Classification:** The first complete classification for any non-trivial case in the Selberg class.

2. **Algorithmic Nature:** The eigenweight χ_F provides a computable invariant that determines the nature of the L-function.

3. **Bridge to Automorphic Theory:** Confirms the automorphic nature conjecture for degree 2, conductor 1 case.

4. **Technical Methods:** Introduces powerful techniques (virtual γ-factors, period functions, structural invariants) that may apply to other cases.

The work opens new avenues for attacking the general Selberg class conjecture and provides a template for understanding higher degree cases.