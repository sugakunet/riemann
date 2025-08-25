# Do Dirichlet L-Functions Satisfy the Three Properties Simultaneously?

## The Three Properties

Examining whether Dirichlet L-functions L(s,χ) satisfy:
1. **Order 1 globally**
2. **Polynomial growth on vertical lines**
3. **Bounded strictly to the right of Re(s) = 1, unbounded to the left of Re(s) = 1**

## Analysis by Character Type

### I. Non-Principal Characters (χ ≠ χ₀)

**Property 1: Order 1 globally** ✓
- L(s,χ) is entire of order 1
- Growth: log|L(s,χ)| ~ |s|log|s|

**Property 2: Polynomial growth on vertical lines** ✓
- On Re(s) = σ: |L(σ+it,χ)| ≪ |t|^((1-σ)/2+ε) for 0 ≤ σ ≤ 1
- Polynomial in t for each fixed σ

**Property 3: Bounded right of 1, unbounded left of 1** ✗
- For Re(s) > 1: **BOUNDED** ✓ (from Euler product convergence)
- For Re(s) < 1: **NOT necessarily unbounded** ✗

**The Problem**: Since L(s,χ) is **entire** (no poles), it doesn't have the forced unboundedness that ζ(s) has from its pole at s = 1.

**Specific Behavior**:
- L(s,χ) is bounded in any vertical strip
- At s = 0: L(0,χ) is finite (often = 0 for odd characters)
- No pole means no forced blow-up

**CONCLUSION**: Non-principal L-functions satisfy 2 out of 3 properties. They fail property 3 because they remain bounded everywhere.

### II. Principal Character (χ = χ₀)

**Property 1: Order 1 globally** ✓
- L(s,χ₀) is meromorphic of order 1

**Property 2: Polynomial growth on vertical lines** ✓
- Same polynomial growth as non-principal characters

**Property 3: Bounded right of 1, unbounded left of 1** ✓
- For Re(s) > 1: **BOUNDED** (Euler product)
- For Re(s) < 1: **UNBOUNDED** near s = 1 due to the pole

**The Relationship**: L(s,χ₀) = ζ(s)∏_{p|q}(1-1/p^s)

Since the product ∏_{p|q}(1-1/p^s) is bounded and non-zero for Re(s) > 0, L(s,χ₀) inherits the boundedness/unboundedness pattern of ζ(s).

**CONCLUSION**: The principal character L-function **DOES** satisfy all three properties simultaneously.

## III. Comparison Table

| Function | Order 1? | Polynomial on verticals? | Bounded right/unbounded left of 1? | All 3? |
|----------|----------|---------------------------|-------------------------------------|--------|
| ζ(s) | ✓ | ✓ | ✓ | **YES** |
| L(s,χ₀) | ✓ | ✓ | ✓ | **YES** |
| L(s,χ), χ≠χ₀ | ✓ | ✓ | ✗ (bounded everywhere) | **NO** |

## IV. The Critical Distinction

The key difference is the **pole at s = 1**:

### Functions WITH pole at s = 1:
- ζ(s)
- L(s,χ₀) for principal character
- These satisfy all three properties

### Functions WITHOUT poles (entire):
- L(s,χ) for non-principal characters
- These are bounded everywhere, violating property 3

## V. Why This Matters

### The Pole is Essential

The pole at s = 1 is not a defect but a **necessary feature** for satisfying all three properties:
1. It forces unboundedness to the left
2. It encodes the Prime Number Theorem (or its analog)
3. It creates the boundary between convergent/divergent regions

### For Non-Principal L-functions

The absence of a pole means:
- L(s,χ) can be bounded on the entire critical strip
- The function is "too well-behaved" to match ζ's pattern
- Growth is controlled everywhere, not just to the right

## VI. Modified Question

If we modify property 3 to match non-principal L-functions:

**Property 3'**: "Bounded for Re(s) > 1, bounded but non-zero for Re(s) < 1"

Then non-principal L(s,χ) would satisfy:
1. Order 1 globally ✓
2. Polynomial growth on verticals ✓
3. Modified boundedness property ✓

## VII. Other Functions with All Three Original Properties

Functions satisfying all three original properties must:
- Be meromorphic (not entire)
- Have at least one pole creating unboundedness
- Have that pole positioned to create the right boundary (around Re(s) = 1)

Examples:
1. **ζ(s)** - prototype
2. **L(s,χ₀)** - principal character L-functions
3. **Dedekind zeta functions ζ_K(s)** for number fields K (pole at s = 1)
4. **Certain Artin L-functions** (when they have poles)

## VIII. Conclusion

**Answer**: Among Dirichlet L-functions:
- **Principal character L(s,χ₀)**: YES, satisfies all three properties
- **Non-principal characters L(s,χ)**: NO, satisfies only properties 1 and 2

The distinction is entirely due to the presence or absence of the pole at s = 1. This pole is intimately connected to:
- The residue class character summing to 0 or not
- The divergence of Σχ(n)/n
- The arithmetic content of the character

This analysis reinforces that the three properties you identified are quite special and essentially characterize **meromorphic functions with a simple pole at s = 1** rather than general L-functions.