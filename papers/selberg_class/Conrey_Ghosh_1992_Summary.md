# Conrey-Ghosh 1992: On the Selberg Class of Dirichlet Series: Small Degrees

**Authors:** J. B. Conrey, A. Ghosh  
**Year:** 1992  
**Focus:** Classification and non-existence results for functions in the Selberg class with small degrees

## 1. The Selberg Class Definition

The **Selberg class S** consists of Dirichlet series F(s) = ∑(a_n/n^s) satisfying:

### Axioms:
1. **Analyticity**: (s-1)^m F(s) is entire of finite order for some non-negative integer m
2. **Ramanujan Hypothesis**: a_n ≪ n^ε for any fixed ε > 0  
3. **Functional Equation**: There exists γ_F(s) = εQ^s ∏Γ(w_i s + μ_i) where |ε| = 1, Q > 0, w_i > 0, ℜ(μ_i) ≥ 0 such that Φ(s) = γ_F(s)F(s) satisfies Φ(s) = Φ(1-s)
4. **Euler Product**: a_1 = 1 and log F(s) = ∑(b_n/n^s) where b_n = 0 unless n is a prime power and b_n ≪ n^θ for some θ < 1/2

### Degree Definition:
The **degree** of F ∈ S is d_F = 2∑w_i, allowing d_F = 0 if no gamma factors are present.

### Key Properties:
- Coefficients a_n are multiplicative
- Has Euler product expansion F(s) = ∏F_p(s) where F_p(s) = ∑(a_{p^k}/p^{ks})
- The condition θ < 1/2 is **crucial** - prevents violation of Riemann hypothesis

## 2. Fundamental Structural Results

### Theorem 2.1 (Uniqueness of Gamma Factors)
If γ^{(1)}(s) and γ^{(2)}(s) are both admissible gamma factors for F, then γ^{(1)}(s) = Cγ^{(2)}(s) for some real constant C.

**Consequence**: The degree d_F is well-defined and independent of the choice of gamma factor.

### Key Lemmas:
- **Lemma 2.1**: If F(s) ∈ S, then F_p(s) has no zeros in σ > 1/2 and F(s) has no zeros in σ > 1
- **Lemma 2.2**: If F ∈ S has a pole/zero at s = 1 + iα, then ∑_{p≤x} a_p/p^{1+iα} is unbounded

## 3. Main Theorem: Non-existence of Small Degrees

### Theorem 3.1 (Central Result)
**If F ∈ S, then F = 1 or d_F ≥ 1.**

This completely eliminates functions of degree 0 < d < 1 from the Selberg class.

### Proof Strategy:
The proof uses complex analysis and the Mellin transform technique:

1. **For d_F < 1**: Consider h(x) = ∑a_n e^{-2πnx} using Mellin inversion
2. **Key observation**: h(x) becomes entire due to degree constraint
3. **Periodicity**: h is periodic with period i, so h is entire everywhere
4. **Growth estimates**: This forces a_n ≪ n^{-2}, making F(s) convergent for σ > -1
5. **Functional equation contradiction**: Using Stirling's formula shows this is impossible for d > 0

### For Degree d = 0:
- F must be a Dirichlet polynomial with F = ∑_{n|Q^2} a_n/n^s
- Functional equation forces specific structure
- If Q^2 > 1, leads to contradiction with θ < 1/2 condition
- Therefore Q = 1 and F(s) = 1

### Bochner's Connection:
**Theorem 3.2 (Bochner)**: The number of linearly independent Dirichlet series with given gamma factors is ≤ 2q∏w_i^{2w_i} where q = Q^2.

## 4. Consequences and Corollaries

### Corollary 3.3 (Factorization)
Any function in S can be factored into a product of primitives.

### Corollary 3.4 (Primitivity)
If F ∈ S and d_F < 2, then F is primitive.

## 5. Selberg's Conjectures and Their Consequences

### The Three Main Conjectures:
1. **Regularity**: ∑_{p≤x} |a_p|^2/p = n_F log log x + O(1)
2. **Orthogonality**: For distinct primitives F, F': ∑_{p≤x} a_p a'_p/p = O(1)  
3. **GL(1) Twists**: Twisted functions preserve primitive factorization

### Proposition 4.1
If F = F_1^{e_1} ⋯ F_k^{e_k} (primitive factors), then n_F = e_1^2 + ⋯ + e_k^2.

### Key Applications:
- **Proposition 4.2**: n_F = 1 ⟹ F is primitive
- **Proposition 4.3**: If F has simple pole at s = 1, then ζ(s) divides F
- **Proposition 4.4**: S has unique factorization
- **Proposition 4.5**: Dedekind's conjecture follows from Selberg's conjectures
- **Proposition 4.6**: F ∈ S ⟹ F has no zeros on σ = 1

## 6. Classification of S*(1)

### The Refined Class S*:
Consider the normalized class S* where gamma factors have the form:
ε^2 Q^s ∏Γ(s/2 + μ_i)F(s) = Q^{1-s} ∏Γ((1-s)/2 + μ̄_i)F(1-s)

### Theorem 5.1 (Complete Classification)
**If F ∈ S*(1), then q is a positive integer and there exists a primitive Dirichlet character χ mod q and real α such that F(s) = L(s + iα, χ).**

### Proof Method:
- Uses Siegel-type proof similar to Hamburger's theorem
- **Crucial role of θ < 1/2**: Without this, false examples like ∑_{n odd} n^{-s} - 2∑_{n≡2(4)} n^{-s} would be included
- Complex analysis of the functional equation structure
- Reduction to known L-functions via character theory

## 7. Functional Equations and GL(2) Theory

### Theorem 6.1 (Converse Theorem)
For Dirichlet series with GL(2)-type functional equations, the functional equation Φ(s) = Φ(1-s) holds if and only if certain transformation properties hold for associated automorphic forms.

### Connection to Modular Forms:
- **Holomorphic case**: Corresponds to weight k cusp forms  
- **Maass forms**: Non-holomorphic automorphic forms
- **Bessel function analysis**: Uses J_ν and K_ν functions for the converse direction

## 8. Key Examples and Applications

### Classical Examples in S:
1. **ζ(s) ∈ S(1)**: The Riemann zeta function
2. **L(s, χ) ∈ S(1)**: Dirichlet L-functions  
3. **Dedekind zeta functions**: ζ_K(s) ∈ S([K:ℚ])
4. **Rankin-Selberg convolutions**: Products of modular forms
5. **Symmetric power L-functions**: Under Langlands conjectures

### Non-Examples:
- **ζ(s + iα)** with α ≠ 0: Violates analyticity
- **Maass forms with exceptional eigenvalues**: Violate ℜ(μ_i) ≥ 0
- **Functions with θ ≥ 1/2**: Would violate Riemann hypothesis

## 9. Mathematical Significance and Impact

### Theoretical Importance:
1. **Eliminates small degrees**: Proves no functions exist with 0 < d < 1
2. **Classification completeness**: Fully characterizes S*(1)
3. **Structural understanding**: Provides factorization and primitivity results
4. **Connection to conjectures**: Links Selberg's conjectures to classical results

### Technical Innovations:
- **Mellin transform methods**: Sophisticated use in degree restriction proofs
- **Functional equation analysis**: Deep structural results
- **Character theory integration**: Connects abstract class to concrete L-functions

### Open Problems Addressed:
- **Admissible degrees**: Shows only integers ≥ 1 are possible
- **Primitive characterization**: Provides concrete criteria
- **Uniqueness of factorization**: Establishes fundamental structural property

## 10. Connections to Broader Theory

### Links to:
- **Automorphic forms**: Via Mellin transforms and functional equations
- **Artin L-functions**: Through holomorphy conjectures  
- **Random matrix theory**: Via zero distribution patterns
- **Analytic number theory**: Through character sums and exponential sums

### Future Directions:
- Extension to higher degrees
- Computational verification of conjectures
- Applications to specific L-function families
- Connections to motivic L-functions

---

## Summary of Main Results

1. **No small degrees exist**: Functions in S have degree 0 (trivial case F = 1) or degree ≥ 1
2. **Complete S*(1) classification**: All degree-1 functions are twisted Dirichlet L-functions
3. **Structural theorems**: Unique factorization, primitivity criteria, and factorization properties
4. **Conjecture implications**: Selberg's conjectures imply classical results like Dedekind's conjecture
5. **Technical methods**: Sophisticated use of complex analysis, Mellin transforms, and functional equations

The paper provides a foundational classification of the Selberg class for small degrees, establishing both impossibility results (no degrees 0 < d < 1) and complete characterizations (degree 1 case), with profound implications for the structure of L-functions and automorphic forms.