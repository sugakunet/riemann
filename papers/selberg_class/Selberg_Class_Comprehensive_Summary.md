# The Selberg Class: Comprehensive Summary of Theory and Results

## Introduction and Historical Context

The Selberg class, introduced by Atle Selberg in 1989 and formalized in 1992, represents one of the most important conceptual advances in the theory of L-functions. It provides an axiomatic framework that captures the essential properties of L-functions arising from number theory and automorphic representation theory, while being general enough to potentially include new, as-yet-undiscovered examples.

The class emerged from Selberg's deep insight that L-functions share certain fundamental properties that can be axiomatized, allowing for a unified treatment of diverse objects including the Riemann zeta function, Dirichlet L-functions, Artin L-functions, and automorphic L-functions.

## Definition of the Selberg Class S

A Dirichlet series F(s) = ∑_{n=1}^∞ a(n)/n^s belongs to the Selberg class S if it satisfies four axioms:

### Axiom 1: Dirichlet Series
F(s) is absolutely convergent for Re(s) > 1.

### Axiom 2: Analytic Continuation
There exists an integer m ≥ 0 such that (s-1)^m F(s) is an entire function of finite order.

### Axiom 3: Functional Equation
F satisfies a functional equation of the form:
Φ(s) = ω Φ̄(1-s̄)

where:
- Φ(s) = Q^s ∏_{j=1}^r Γ(λ_j s + μ_j) F(s)
- Q > 0 (the conductor)
- λ_j > 0
- Re(μ_j) ≥ 0
- |ω| = 1

### Axiom 4: Euler Product
F has an Euler product:
F(s) = ∏_p exp(∑_{k=1}^∞ b(p^k)/p^{ks})

where:
- b(p^k) ≪ p^{kθ} for some θ < 1/2
- b(n) = 0 unless n is a prime power

### Critical Constraint
The condition θ < 1/2 in Axiom 4 is essential. Without it, the class would include functions violating the Riemann Hypothesis.

## The Degree and the Degree Conjecture

### Definition of Degree
The degree of F ∈ S is defined as:
d_F = 2∑_{j=1}^r λ_j

This is a fundamental invariant that measures the "complexity" of the L-function.

### The Degree Conjecture
**Conjecture**: For every F ∈ S, the degree d_F is a non-negative integer.

This conjecture is central to the theory and has profound implications for the structure of S.

### Progress on the Degree Conjecture

The following results have been established:

1. **d = 0**: S_0 = {1} (Conrey-Ghosh, 1993)
   - Only the trivial function has degree 0

2. **0 < d < 1**: S_d = ∅ (Richert 1957, Conrey-Ghosh 1992)
   - No functions exist with fractional degree less than 1

3. **d = 1**: Complete classification (Kaczorowski-Perelli, 1999)
   - S_1 consists exactly of ζ(s) and shifted Dirichlet L-functions L(s+iτ, χ)

4. **1 < d < 2**: S_d = ∅ (Kaczorowski-Perelli, 2002, 2011)
   - No functions exist with degree between 1 and 2

5. **d < 5/3**: Degree conjecture proven (Kaczorowski-Perelli)
   - All functions with degree less than 5/3 have integer degree

## Extended Selberg Class S♯

The extended Selberg class S♯ relaxes the Euler product requirement while maintaining the functional equation. This larger class is technically useful for proving results about S itself.

### Key Properties of S♯:
- Contains S as a subclass
- Closed under multiplication
- Admits unique factorization into primitive functions
- More amenable to analytical techniques

## Classification Results

### Degree 1 Functions
**Theorem** (Kaczorowski-Perelli, 1999): Every F ∈ S with d_F = 1 has the form:
F(s) = L(s + iτ, χ)

where χ is a primitive Dirichlet character and τ ∈ ℝ.

### Degree 2, Conductor 1 Functions
**Theorem** (Kaczorowski-Perelli, 2020): Every F ∈ S♯ with degree 2 and conductor 1 is one of:
1. ζ(s)^2
2. L-function of a holomorphic cusp form
3. L-function of a Maass form

The classification is determined by the eigenweight invariant:
χ_F = ξ_F + H_F(2) + 2/3

where:
- χ_F > 0: holomorphic cusp forms
- χ_F = 0: ζ(s)^2
- χ_F < 0: Maass forms

## Selberg's Conjectures

### Conjecture A (Primitivity)
For F ∈ S primitive, there exists an integer n_F such that:
∑_{p≤x} |a(p)|^2/p = n_F log log x + O(1)

### Conjecture B (Orthogonality)
For F, G ∈ S primitive:
∑_{p≤x} a_F(p)ā_G(p)/p = δ_{F,G} log log x + O(1)

### Implications
- Conjectures A and B imply unique factorization in S
- They imply the Artin conjecture for non-abelian L-functions (Murty, 1994)
- For solvable Galois groups, they imply Langlands reciprocity

## Forbidden Conductors

### Recent Discovery
Not all positive real numbers can be conductors of degree-2 L-functions in S♯.

**Theorem** (Kaczorowski-Perelli-Radziejewski, 2023): A positive integer q > 1 is a forbidden conductor if:
1. All prime divisors p of q satisfy p ≡ 3 (mod 4)
2. The Jacobi symbol (2|q) = -1
3. The continued fraction of √q has period length 1

### Examples of Forbidden Conductors
- 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, ...

This reveals unexpected arithmetic constraints on the Selberg class structure.

## Proof Techniques and Methods

### 1. Mellin Transform Methods
Used extensively for proving non-existence results and establishing functional equations.

### 2. Tauberian Theory
Essential for connecting Dirichlet series coefficients to asymptotic behavior.

### 3. Virtual γ-factors
Hypothetical gamma factors used in classification proofs that may not correspond to actual L-functions.

### 4. Period Functions
Lewis-Zagier period functions applied to constrain structural invariants.

### 5. Nonlinear Twists
Analysis of F(s,β,α) = ∑a(n)e(-βn-α√n)/n^s provides structural information.

### 6. Quadratic Form Theory
Structural invariants lie on universal algebraic varieties, providing geometric constraints.

## Connections to Other Areas

### Random Matrix Theory
- Zero statistics of L-functions in S connected to eigenvalue distributions
- Montgomery-Dyson conjecture relates to pair correlation

### Automorphic Forms
- Conjectured that S consists exactly of automorphic L-functions
- Degree 2, conductor 1 case confirms this for a special case

### Arithmetic Geometry
- Artin L-functions from Galois representations
- Motivic L-functions expected to be in S

### Spectral Theory
- Selberg trace formula connections
- Eigenvalues of Laplacians on arithmetic manifolds

## Universality Results

### Joint Universality
**Theorem** (Using Selberg's orthonormality): Distinct primitive functions in S are jointly universal - they simultaneously approximate arbitrary analytic functions in the critical strip.

### Significance
- Provides functional independence of L-functions
- New approach avoiding difficult mean-square estimates
- Applications to value distribution theory

## Open Problems and Future Directions

### Major Open Questions

1. **Complete Degree Conjecture**: Prove d_F ∈ ℕ for all F ∈ S

2. **Classification for d = 2**: Complete classification of all degree-2 functions

3. **Selberg's Orthogonality**: Prove Conjecture B

4. **Automorphic Characterization**: Prove S consists exactly of automorphic L-functions

5. **Forbidden Conductors**: Extend theory to higher degrees

### Research Directions

1. **Higher Degree Classification**: Extend methods to degree 3 and beyond

2. **Geometric Approach**: Develop geometric interpretation of structural invariants

3. **Computational Methods**: Algorithms for testing membership in S

4. **Connections to Physics**: Explore quantum chaos connections

5. **Categorical Framework**: Develop categorical interpretation of S

## Significance for the Riemann Hypothesis

The Selberg class framework is crucial for RH research because:

### 1. Unified Framework
Provides a single setting for studying RH for all L-functions simultaneously.

### 2. Structural Insights
Classification results reveal deep structural properties constraining zeros.

### 3. New Proof Strategies
- Degree conjecture approach
- Orthogonality-based methods
- Forbidden conductor constraints

### 4. Connections
Links RH to:
- Automorphic forms
- Representation theory
- Arithmetic geometry
- Random matrix theory

### 5. Generalization
Any proof for S would immediately apply to all classical L-functions.

## Key References

### Foundational Papers
1. Selberg, A. (1992). "Old and new conjectures and results about a class of Dirichlet series"
2. Conrey, J.B. & Ghosh, A. (1992). "On the Selberg class of Dirichlet series: small degrees"
3. Murty, M.R. (1994). "Selberg's conjectures and Artin L-functions"

### Classification Results
4. Kaczorowski, J. & Perelli, A. (1999). "On the structure of the Selberg class, I: 0 ≤ d ≤ 1"
5. Kaczorowski, J. & Perelli, A. (2011). "On the structure of the Selberg class, VII: 1 < d < 2"
6. Kaczorowski, J. & Perelli, A. (2020). "Classification of L-functions of degree 2 and conductor 1"

### Recent Developments
7. Kaczorowski, J., Perelli, A. & Radziejewski, M. (2023). "Forbidden conductors of L-functions"
8. Various authors (2015). "Selberg's orthonormality conjecture and joint universality"

## Conclusion

The Selberg class represents a fundamental organizing principle for L-function theory, providing both a conceptual framework and concrete results about the structure of these essential objects in number theory. The degree conjecture and classification results have revealed unexpected constraints and patterns, while forbidden conductors show surprising arithmetic obstructions.

The theory connects diverse areas of mathematics - from automorphic forms to random matrices - and provides multiple potential pathways toward understanding the Riemann Hypothesis. The classification of small degree cases and the discovery of forbidden conductors demonstrate that the Selberg class has rich internal structure still being uncovered.

Future progress will likely require new techniques bridging the analytic, arithmetic, and geometric aspects of L-functions. The Selberg class framework ensures that any such advances will apply broadly to all L-functions of number-theoretic interest, making it an essential tool for modern research in analytic number theory.