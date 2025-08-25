# Selberg's Conjectures and Artin L-functions
## M. Ram Murty (1994)

### Summary
This influential paper establishes fundamental connections between Selberg's conjectures about a class of Dirichlet series with functional equations and the Artin conjecture concerning nonabelian L-functions. The work demonstrates how Selberg's framework provides a new pathway toward proving major conjectures in algebraic number theory.

## 1. The Selberg Class S

### Definition
Selberg introduced the class S of functions F(s) satisfying:

**(i) Dirichlet series:** For Re(s) > 1, F(s) = Σ_{n=1}^∞ a_n/n^s with a_1 = 1

**(ii) Analytic continuation:** F(s) extends meromorphically so (s-1)^m F(s) is entire of finite order for some m ≥ 0

**(iii) Functional equation:** 
Φ(s) = Q^s ∏_{i=1}^d Γ(α_i s + r_i) F(s)
satisfies Φ(s) = wΦ(1-s) for |w| = 1

**(iv) Euler product:** F(s) = ∏_p F_p(s) where F_p(s) = exp(Σ_{k=1}^∞ b_{pk}/p^{ks}) with b_{pk} = O(p^{kθ}) for θ < 1/2

**(v) Ramanujan hypothesis:** a_n = O(n^ε) for any ε > 0

### Key Properties
- S is multiplicatively closed (forms a monoid)
- All known examples are automorphic L-functions
- Dimension of F defined as dim F = 2α_F where α_F = Σα_i

## 2. Selberg's Conjectures

### Conjecture A (Asymptotic Distribution)
For all F ∈ S, there exists positive integer n_F such that:
Σ_{p≤x} |a_p(F)|²/p = n_F log log x + O(1)

### Conjecture B (Primitive Functions)
**(i)** For any primitive function F, n_F = 1 so:
Σ_{p≤x} |a_p(F)|²/p = log log x + O(1)

**(ii)** For distinct primitive functions F and F':
Σ_{p≤x} a_p(F)a_p(F')/p = O(1)

**Interpretation:** Primitive functions form an orthonormal system in some sense.

### Definition of Primitive Functions
F ∈ S is **primitive** if F = F₁F₂ with F₁, F₂ ∈ S implies F = F₁ or F = F₂.

## 3. Unique Factorization in S

### Fundamental Results

**Proposition 2.3 (Conrey-Ghosh):** Every F ∈ S factors into primitive functions.

**Proposition 2.4:** Conjecture B implies unique factorization into primitives in S.

**Key Insight:** If F = F₁^{e₁} ⋯ F_r^{e_r} is the primitive factorization, then:
- Conjecture B implies n_F = e₁² + ⋯ + e_r²
- F is primitive ⟺ n_F = 1

### Classical Examples
- Riemann zeta function ζ(s) is primitive
- Dirichlet L-functions L(s,χ) for primitive characters χ are primitive

## 4. Connection to Artin L-functions

### Artin L-functions
For Galois extension K/k with group G and irreducible representation ρ:

L(s,ρ,K/k) = ∏_p det(1 - ρ(σ_p)Np^{-s}|V_p)^{-1}

where V_p is the subspace fixed by inertia group I_p.

### Artin's Conjecture
If ρ is irreducible ≠ 1, then L(s,ρ,K/k) extends to an entire function.

## 5. Main Theorem: Selberg ⟹ Artin

### Theorem 3.1
**Conjecture B implies Artin's conjecture.**

**Proof Strategy:**
1. Reduce to case K/Q Galois using normal closure
2. Use Brauer induction: L(s,φ,K/Q) = L(s,χ₁)/L(s,χ₂) where χ₁,χ₂ are products of Hecke L-functions
3. Both numerator and denominator belong to S with unique primitive factorization
4. Write L(s,φ) = ∏F_i(s)^{e_i} where F_i are primitive and e_i ∈ Z
5. Use Chebotarev density theorem to compute:
   Σ_{p≤x} |φ(p)|²/p = log log x + O(1)
6. By Conjecture B orthogonality: Σe_i² = 1
7. Therefore m = 1 and e₁ = ±1, so L(s,φ) = F(s) or 1/F(s)
8. Since L(s,φ) has no poles for irreducible φ ≠ 1, must have L(s,φ) = F(s) primitive and entire

### Corollary 3.2
If K/Q is Galois with irreducible character χ, then Conjecture B implies L(s,χ) is primitive.

## 6. Langlands Reciprocity Conjecture

### Langlands Program Context
The Langlands reciprocity conjecture asserts:
For n-dimensional irreducible representation ρ, there exists cuspidal automorphic representation π of GL_n(A_k) such that L(s,ρ,K/k) = L(s,π).

### Solvable Case Result

**Theorem 4.3:** Assume Conjecture B. Let K be Galois extension of Q with solvable group G, and χ irreducible character of degree n. Then there exists irreducible cuspidal automorphic representation π of GL_n(A_Q) such that L(s,χ) = L(s,π).

**Proof Method:**
1. Use Arthur-Clozel results on base change and automorphic induction for cyclic extensions
2. Factor Dedekind zeta function ζ_K(s) using solvable tower Q = K₀ ⊂ K₁ ⊂ ⋯ ⊂ K_m = K
3. Apply automorphic induction successively to express ζ_K as product of automorphic L-functions over Q
4. Use classical Artin factorization ζ_K(s) = ∏_χ L(s,χ)^{χ(1)}
5. Both factorizations consist of primitive functions (by Selberg conjectures)
6. Unique factorization implies correspondence between Artin and automorphic L-functions

## 7. Mathematical Structure and Implications

### Dimension Theory
- **Bochner's Bound:** If F ∈ S and α_F > 0, then α_F ≥ 1/2
- **Classification:** For dimension 1 functions with rational α_i, complete classification exists:
  - Riemann zeta function ζ(s)
  - Classical Dirichlet L-functions L(s,χ)

### Primitive Function Properties
**From Ramanujan Conjecture:** If π is cuspidal automorphic representation satisfying Ramanujan conjecture, then L(s,π) is primitive.

**Orthogonality:** Distinct primitive functions are "orthogonal" in the sense of Conjecture B(ii).

### Connection to Automorphic Representations
- Selberg conjectures imply L-functions of irreducible cuspidal automorphic representations over Q are primitive
- Open question: Are there elements of S not arising from automorphic representations?

## 8. Technical Tools and Methods

### Chebotarev Density Theorem
Crucial for computing asymptotic behavior:
Σ_{p≤x, σ_p∈C} 1/p = |C|/|G| log log x + O(1)

### Jacquet-Shalika Theory
For distinct cuspidal representations π₁, π₂:
- L^S(s, π₁ ⊗ π₂) analytic and nonvanishing on Re s = 1
- L^S(s, π₁ ⊗ π̃₁) has simple pole at s = 1
This provides the orthogonality relations needed for primitive function theory.

### Arthur-Clozel Results
Base change and automorphic induction maps exist for cyclic extensions, enabling the solvable case proof of Langlands reciprocity.

## 9. Open Problems and Consequences

### Classification Problems
1. **Complete classification** of primitive functions of higher dimension
2. **Existence question:** Are there primitive functions not arising from known automorphic forms?
3. **Rationality:** Are the α_i always rational for functions in S?

### Connections to Other Conjectures
- **Unique factorization** might be provable by other means
- **Non-vanishing:** Conjecture B implies no primitive function (except ζ(s)) vanishes on σ = 1
- **Special values:** Connection to Deligne and Birch-Swinnerton-Dyer conjectures

### Computational Consequences
If F₁,...,F_r are distinct primitive functions, expect existence of complex numbers s₁,...,s_r such that F_i(s_j) = 0 iff i = j, which would imply unique factorization.

## 10. Historical Context and Impact

### Relationship to Major Programs
- **Alternative approach** to Langlands program via analytic methods
- **Unification** of various L-function conjectures under single framework
- **Bridge** between analytic number theory and representation theory

### Methodological Innovation
- **Primitive function concept** provides new organizational principle for L-functions
- **Orthogonality relations** give quantitative version of independence
- **Unique factorization** perspective on multiplicative structure of L-functions

This paper established Selberg's class as a fundamental framework for understanding L-functions and demonstrated deep connections between analytic properties (Selberg conjectures) and arithmetic conjectures (Artin, Langlands). The work shows how the multiplicative structure encoded in Selberg's conjectures can resolve major problems in algebraic number theory, particularly for solvable Galois groups.