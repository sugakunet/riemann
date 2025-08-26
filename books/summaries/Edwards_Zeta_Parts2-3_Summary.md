# Edwards' "Riemann's Zeta Function" - Parts 2-3 Analysis (Pages 36-105)

## Overview

This analysis covers pages 36-105 of Edwards' exposition, which details the mathematical developments following Riemann's 1859 paper, particularly focusing on:
- The rigorous proof of the product formula for ξ(s)
- Von Mangoldt's proof of Riemann's main formula 
- The prime number theorem and its proof
- De la Vallée Poussin's error estimates

## Chapter 2: The Product Formula for ξ(s) (Pages 39-47)

### Historical Context
Edwards explains that Riemann's sketch of the product formula proof was "so abbreviated as to make it virtually useless in constructing a proof." The first rigorous proof came from **Hadamard in 1893**, which von Mangoldt called "the first real progress in the field in 34 years."

### Key Mathematical Development: Jensen's Theorem (1899)
Edwards emphasizes how Jensen's theorem revolutionized the proof technique:

**Jensen's Theorem**: For f(z) analytic in |z| ≤ R with zeros z₁, z₂, ..., zₙ and f(0) ≠ 0:
```
log|f(0)| · R/z₁ · R/z₂ · ... · R/zₙ = (1/2π) ∫₀²π log|f(Re^(iθ))| dθ
```

This theorem provided the crucial estimate that **n(R) ≤ 2R log R** for the number of zeros of ξ(s) in |s - 1/2| ≤ R, which was sufficient to prove convergence of the infinite product.

### The Product Formula
Edwards shows how the rigorous proof establishes:
```
ξ(s) = ξ(0) ∏ₚ (1 - s/p)
```
where the product is over all non-trivial zeros ρ, with terms paired as ρ and 1-ρ.

## Chapter 3: Riemann's Main Formula (Pages 48-67)

### Von Mangoldt's Achievement (1895)
Edwards details how **von Mangoldt provided the first rigorous proof** of Riemann's main formula, using methods that were "closer to Riemann's outline than to Hadamard's proof."

### The Explicit Formula
Von Mangoldt established:
```
J(x) = Li(x) - Σₚ Li(x^ρ) - log 2 + ∫ₓ^∞ dt/[t(t²-1)log t]
```

Edwards emphasizes the **fundamental connection** this reveals:
- **Li(x)**: The smooth approximation from integration
- **Σₚ Li(x^ρ)**: The "periodic" terms from zeros  
- **Integral term**: Contribution from the pole at s = 1
- **Constant**: Normalization from ξ(0)

### Von Mangoldt's Innovation: The ψ(x) Formula
Edwards shows how von Mangoldt reformulated Riemann's result in terms of the **Chebyshev function ψ(x)**:
```
ψ(x) = x - Σₚ x^ρ/ρ + Σₙ x^(-2n)/(2n) - ζ'(0)/ζ(0)
```

This form became "virtually the standard" because:
1. **More natural**: ψ(x) counts weighted prime powers directly
2. **Easier to prove**: Avoids some of Riemann's convergence issues
3. **Better for applications**: More amenable to error estimates

### Fourier Analysis Connection
Edwards emphasizes Riemann's use of **Fourier inversion**:
```
J(x) = (1/2πi) ∫_{a-i∞}^{a+i∞} log ζ(s)x^s ds/s
```

This technique, which Edwards notes "preceded Mellin's work by 40 years," transforms the problem of understanding J(x) into analyzing the analytic properties of log ζ(s).

### Technical Innovation: Termwise Integration
Edwards details the sophisticated estimates von Mangoldt developed to justify **termwise integration of infinite series**. This was a major technical advance, requiring:
- **Uniform convergence estimates** on finite intervals
- **Careful analysis of the density of zeros** ρ
- **Integration by parts** to handle divergent integrals

## Chapter 4: The Prime Number Theorem (Pages 68-77)

### The Central Obstacle: Zeros on Re s = 1
Edwards shows how the prime number theorem reduced to proving **ζ(s) ≠ 0 for Re s = 1**. This was the "substantial step beyond von Mangoldt's work."

### Hadamard's Breakthrough (1896)
Edwards presents **Hadamard's elegant proof** that Re ρ < 1:

**Key Inequality**: For Re s > 1:
```
Re{3ζ'(σ)/ζ(σ) + 4ζ'(σ+it)/ζ(σ+it) + ζ'(σ+2it)/ζ(σ+2it)} ≥ 0
```

This uses the **fundamental identity**:
```
3 + 4cos θ + cos 2θ = 2(1 + cos θ)² ≥ 0
```

The proof shows that if ζ(1 + it) = 0, then the inequality would be violated, creating a contradiction.

### Prime Number Theorem Proof Structure
Edwards outlines the **two-step process**:

1. **ψ(x) ~ x**: Using Hadamard's zero-free region
2. **π(x) ~ Li(x)**: Using the relationship between π(x) and ψ(x)

The connection uses **partial summation** and the key estimate:
```
θ(x) = ψ(x) + O(x^(1/2) log x)
```

## Chapter 5: De la Vallée Poussin's Theorem (Pages 78-90)

### Error Rate Estimates (1899)
Edwards shows how **de la Vallée Poussin improved** the zero-free region to:
```
β < 1 - c/log γ  (for |γ| ≥ K)
```

This **quantitative improvement** yielded the error bound:
```
|π(x) - Li(x)|/Li(x) < exp(-(c√(log x)))
```

### Technical Innovation: The 3+4cos θ+cos 2θ Method
Edwards details how **Mertens' inequality** was strengthened:
```
∫₀^∞ x^(-σ)[3 + 4cos(t log x) + cos(2t log x)] dψ(x) ≥ 0
```

This technique became fundamental for **all subsequent work** on zero-free regions.

### Riemann Hypothesis Equivalence
Edwards presents the remarkable result:
> **The Riemann Hypothesis is equivalent to**: π(x) - Li(x) = O(x^(1/2+ε)) for all ε > 0.

This shows the **deep connection** between the distribution of zeros and prime counting error.

## Computational Aspects and Verification

### Early Numerical Work
Edwards describes how Riemann's ideas were **computationally verified**:

1. **Riemann himself** computed the first few zeros
2. **Gram (1903)** verified the first 15 zeros lie on Re s = 1/2  
3. **Early calculations** confirmed the prime number theorem predictions

### The Logarithmic Integral Advantage
Edwards shows **empirical superiority** of Li(x) over other approximations:

| x           | π(x) error with Li(x) | π(x) error with x/log x |
|-------------|----------------------|-------------------------|
| 10⁶        | 30                   | 130                     |
| 10⁷        | 88                   | 339                     |

This **stunning accuracy** validated Riemann's approach.

## Historical Impact and Development

### Mathematical Technique Evolution
Edwards traces how **methods evolved**:

1. **Riemann (1859)**: Brilliant insights, incomplete proofs
2. **Hadamard (1893)**: Product formula via complex function theory  
3. **Von Mangoldt (1895)**: Explicit formulas via Fourier analysis
4. **Hadamard & de la Vallée Poussin (1896)**: Prime number theorem
5. **De la Vallée Poussin (1899)**: Quantitative error estimates

### Key Conceptual Advances
Edwards emphasizes several **paradigm shifts**:

1. **From elementary to analytic**: Moving beyond elementary number theory
2. **From local to global**: Understanding global distribution via complex analysis  
3. **From existence to quantitative**: Getting explicit error bounds
4. **From special to general**: Techniques applicable to L-functions

## Connection Between Zeros and Primes

### The Fundamental Relationship
Edwards shows how the **explicit formulas** reveal:
- **Each zero ρ contributes** a term Li(x^ρ) to the prime counting function
- **The real parts Re ρ** determine the **growth rates** of these contributions  
- **The imaginary parts Im ρ** create **oscillatory behavior** in prime distribution

### Von Mangoldt's Explicit Formula
The **crown jewel** is the precise relationship:
```
ψ(x) = x - Σₚ (x^ρ/ρ) + O(log x)
```

This shows:
- **Main term x**: The "expected" density of primes
- **Oscillatory terms**: Deviations caused by each zero
- **Error term**: Contributions from trivial zeros and poles

## Computational Methods Discussed

### Riemann's Approach
Edwards describes Riemann's computational method:
1. **Functional equation** to relate ζ(s) and ζ(1-s)
2. **Theta function expansion** for efficient computation
3. **Saddle point approximation** for large arguments

### Von Mangoldt's Verification
The **termwise integration** required:
- **Uniform convergence estimates** 
- **Density bounds** on zeros ρ
- **Careful treatment** of conditionally convergent series

## Significance and Legacy

### Foundational Impact
Edwards emphasizes that this work:
1. **Established analytic number theory** as a field
2. **Created the template** for studying L-functions  
3. **Demonstrated the power** of complex analysis in number theory
4. **Revealed deep connections** between analysis and arithmetic

### Modern Relevance  
The techniques developed here became **fundamental tools**:
- **Explicit formulas** for all L-functions
- **Zero-free regions** for error estimates  
- **Fourier analysis** in number theory
- **Complex function theory** applications

## Conclusion

Edwards' exposition reveals how Riemann's visionary 1859 paper required **nearly 40 years of intensive development** to be made rigorous. The key achievements were:

1. **Hadamard (1893)**: Rigorous product formula proof
2. **Von Mangoldt (1895)**: Explicit formulas with full justification  
3. **Hadamard & de la Vallée Poussin (1896)**: Prime number theorem
4. **De la Vallée Poussin (1899)**: Quantitative error estimates

These developments **transformed number theory** and established the **analytical approach** that dominates the field today. Edwards shows how each mathematician built upon Riemann's insights while developing the **sophisticated techniques** needed to make the theory rigorous and applicable.

The work reveals the **profound connection** between the zeros of the zeta function and the distribution of prime numbers, establishing a **paradigm** that continues to drive research in analytic number theory to this day.