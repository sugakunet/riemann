# Growth Order of Dirichlet L-Functions

## Executive Summary

Dirichlet L-functions have the **same growth order as the Riemann zeta function**: they are functions of **order 1** with **finite exponential type**. The key distinction is that L(s,χ) is **entire** for non-principal characters but **meromorphic** (with a simple pole at s=1) for the principal character.

## I. Definition and Basic Properties

### Dirichlet L-Function
For a Dirichlet character χ modulo q:

```
L(s,χ) = Σ(n=1 to ∞) χ(n)/n^s     (Re(s) > 1)
```

### Euler Product
For Re(s) > 1:
```
L(s,χ) = ∏(p prime) (1 - χ(p)/p^s)^(-1)
```

## II. Analytic Classification

### 1. Principal Character χ₀

**L(s,χ₀) is meromorphic** with:
- **Simple pole at s = 1** with residue φ(q)/q
- Relationship to ζ(s): L(s,χ₀) = ζ(s)∏(p|q)(1 - 1/p^s)
- **Order**: 1 (same as ζ)
- **Type**: Finite exponential type

### 2. Non-Principal Characters χ ≠ χ₀

**L(s,χ) is entire** (holomorphic everywhere):
- **No poles** in the complex plane
- **Order**: 1
- **Type**: Finite exponential type ~ q^(1/2)

## III. Growth Order Analysis

### 1. Definition of Order

For an entire/meromorphic function f, the **order ρ** is:
```
ρ = lim sup(r→∞) [log log M(r)] / [log r]
```
where M(r) = max(|z|=r) |f(z)|

### 2. Order of L-Functions

**Theorem**: All Dirichlet L-functions have **order ρ = 1**.

**Proof sketch**:
- The completed L-function Λ(s,χ) = (q/π)^(s/2)Γ((s+a)/2)L(s,χ) is entire (for χ ≠ χ₀)
- Stirling's formula: |Γ(s/2)| ~ |s|^(Re(s)/2-1/4)e^(-π|Im(s)|/4)
- This gives log |Λ(s,χ)| ~ |s|log|s|, hence order 1

### 3. Exponential Type

For primitive character χ modulo q:
- **Type τ ≈ √q** (more precisely, related to the conductor)
- Growth: |L(s,χ)| ≤ exp(C|s|) for some constant C depending on q

## IV. Growth on Vertical Lines

### 1. Convexity Bound

On the line Re(s) = σ:
```
|L(σ+it,χ)| ≪ {
    q^(1/2)|t|^((1-σ)/2+ε)     if 0 ≤ σ ≤ 1
    q^ε                         if σ ≥ 1
    q^(1/2)|t|^(σ/2+ε)         if σ ≤ 0
}
```

### 2. On the Critical Line (σ = 1/2)

Under the Generalized Riemann Hypothesis (GRH):
```
log|L(1/2+it,χ)| ≪ log(q|t|)/log log(q|t|)
```

This is the **same growth** as ζ(1/2+it) under RH.

### 3. Comparison Table

| Property | ζ(s) | L(s,χ₀) | L(s,χ), χ≠χ₀ |
|----------|------|---------|---------------|
| **Type** | Meromorphic | Meromorphic | Entire |
| **Poles** | Simple at s=1 | Simple at s=1 | None |
| **Order** | 1 | 1 | 1 |
| **Exp. Type** | π | ~√q | ~√q |
| **Growth on Re(s)=1/2** | exp(O(log t/log log t)) | exp(O(log qt/log log qt)) | exp(O(log qt/log log qt)) |

## V. Functional Equation

### For Primitive Character χ mod q

The functional equation connects L(s,χ) and L(1-s,χ̄):

```
Λ(s,χ) = ε(χ)Λ(1-s,χ̄)
```

where:
- Λ(s,χ) = (q/π)^(s/2)Γ((s+a)/2)L(s,χ) is the completed L-function
- ε(χ) is the root number with |ε(χ)| = 1
- a = 0 if χ(-1) = 1 (even), a = 1 if χ(-1) = -1 (odd)

This functional equation is **analogous to ζ's** but with conductor q appearing.

## VI. Key Differences from ζ(s)

### 1. Entire vs Meromorphic
- **ζ(s)**: Always meromorphic (pole at s=1)
- **L(s,χ)**: Entire for χ ≠ χ₀, meromorphic for χ = χ₀

### 2. Growth Rate Dependence
- **ζ(s)**: Growth independent of parameters
- **L(s,χ)**: Growth depends on conductor q

### 3. Zeros
- **ζ(s)**: Trivial zeros at -2,-4,-6,... and non-trivial zeros
- **L(s,χ)**: Similar structure but zeros depend on character parity

## VII. Implications for Growth Classification

### 1. Universality Class

All Dirichlet L-functions belong to the **Selberg class** S with:
- Dirichlet series convergent for Re(s) > 1
- Analytic continuation (entire or meromorphic)
- Functional equation of standard type
- Euler product for Re(s) > 1
- **Order 1** growth

### 2. Phragmén-Lindelöf Consequences

The order 1 classification implies:
- Polynomial growth on vertical lines
- Subexponential growth globally
- Convexity principle applies in vertical strips

### 3. Connection to RH

The Generalized Riemann Hypothesis (GRH) states:
- All non-trivial zeros of L(s,χ) lie on Re(s) = 1/2

GRH would imply **optimal growth bounds**:
```
|L(σ+it,χ)| ≪ (q|t|)^ε for σ ≥ 1/2+ε
```

## VIII. Conclusion

Dirichlet L-functions share the fundamental growth characteristics of the Riemann zeta function:
- **Order 1** (neither polynomial nor exponential growth)
- **Finite exponential type** (controlled by conductor q)
- **Polynomial growth on vertical lines**
- **Functional equation** creating symmetry about Re(s) = 1/2

The main distinctions are:
1. **Analyticity**: L(s,χ) is entire for non-principal characters
2. **Conductor dependence**: Growth rates scale with q
3. **Character variety**: Different L-functions for each character mod q

This classification places all Dirichlet L-functions in the same fundamental class as ζ(s), supporting the expectation that they satisfy similar distribution properties for their zeros (GRH) and exhibit similar extremal behavior in the sense of Beurling-Selberg theory.