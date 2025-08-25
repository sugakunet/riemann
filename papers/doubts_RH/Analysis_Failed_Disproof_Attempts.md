# Analysis of Two Failed Riemann Hypothesis Disproof Attempts

## Executive Summary

This document analyzes two claimed disproof attempts of the Riemann Hypothesis:
1. **Wolf (2009)**: A computational approach using the Báez-Duarte criterion that found a 10^-996 discrepancy
2. **Liu (2024)**: A theoretical approach claiming "quadruplet-zeros outside the critical line"

Both attempts fail for different reasons: Wolf's due to insufficient computational precision, and Liu's due to fundamental mathematical errors in logic and contradictory assumptions.

---

## 1. Wolf's 2009 Computational Approach

### 1.1 Mathematical Framework

**Core Method**: Wolf used the Báez-Duarte criterion for RH, which states that RH is equivalent to:
```
c_k = O(k^(-3/4+ε)) for all ε > 0
```

where the Báez-Duarte sequence is defined as:
```
c_k = Σ(j=0 to k) (-1)^j (k choose j) 1/ζ(2j+2)
```

**Two-Formula Approach**: Wolf calculated c_100000 using:
1. **Generic formula (14)**: Direct computation from the definition above
2. **Explicit formula**: Using known zeros of ζ(s) and the decomposition c_k = c̄_k + c̃_k

### 1.2 Computational Method Details

**Generic Formula Calculation**:
- Used PARI/GP with 100,000 decimal precision
- Calculated c^g_100000 by summing 100,001 terms
- Partial sums peaked at ~10^30100 before dropping to final value ~1.609 × 10^-9
- Required ~14-20 hours on AMD Opteron 2.6 GHz

**Explicit Formula Calculation**:
- Used Mathematica's `ZetaZero[m]` and numerical differentiation `ND[...]`
- Calculated first 2600 nontrivial zeros with 1000-digit precision
- Applied formulas (18) and (27) for trend and oscillating parts
- Used PARI's `sumalt` procedure for infinite alternating series

### 1.3 The 10^-996 Discrepancy

**Progressive Accuracy Improvements**:
- Initial attempt: Agreement only to 87 decimal places (10^-87)
- With improved ζ'(ρ_l) calculation: 105 places (10^-105)
- Using PARI's `sumalt`: 625 places (10^-625)
- Final result with 2000-digit precision: **996 places (10^-996)**

**Final Comparison**:
```
c^g_100000 = 1.60975799...←980 digits→...291369630140 × 10^-9
c^e_100000 = 1.60975799...←980 digits→...291369629833 × 10^-9
```

### 1.4 Why Wolf's Approach Failed

**1. Insufficient Theoretical Foundation**: 
- Wolf estimated that detecting off-critical-line zeros would require k values astronomically larger than 100,000
- The required K satisfies: K^(δ_l/2) e^(-γ^(o)_l) > C, leading to K > 10^(10^...)

**2. Computational Precision Limitations**:
- Even 1000-digit precision insufficient for the scale required
- The 10^-996 discrepancy likely represents numerical noise, not mathematical truth

**3. Theoretical Contradiction**:
- Wolf's own analysis (Section 3) shows why his computational approach cannot work
- As Maślanka noted: disproving RH this way is "far beyond any numerical capabilities"

**4. Misinterpretation of Results**:
- The high precision agreement actually supports RH rather than refuting it
- Similar to Borwein brothers' "high precision fraud" examples

---

## 2. Liu's 2024 Theoretical Approach

### 2.1 Mathematical Framework

**Core Claim**: Liu argues that "at least one set of quadruplet-zeros exists outside the critical line" by:
1. Expanding the infinite product of the Riemann ξ function
2. Assuming no zeros outside Re(s) = 1/2 leads to contradictions
3. Deriving bounds that allegedly prove zeros must exist off the critical line

**Key Definitions**:
- Ω₁: zeros on critical line {ρ_m | ρ_m = 1/2 + iβ_m}
- Ω₂: zeros off critical line {ρ_k | ρ_k = 1/2 + δ_k + iβ_k, δ_k > 0}
- Claims Ω₂ cannot be empty

### 2.2 Liu's Argument Structure

**Theorem 4.1** (Liu's main claim): "At least one set of quadruplet-zeros exists outside the critical line"

**Proof Strategy**:
1. Assume RH is true (Ω₂ = ∅)
2. Derive equation (4.1): log(2ξ(s)) = Σ log(1 + λ_m(s² - s))
3. Through complex manipulations involving Taylor series expansions
4. Arrive at contradictory inequalities (4.25) and (4.26)
5. Conclude RH must be false

### 2.3 Critical Mathematical Errors in Liu's Approach

**1. Circular Reasoning**:
Liu's proof assumes the existence of parameters μ_k, ν_k associated with zeros in Ω₂, then uses properties of these parameters to prove Ω₂ is non-empty. This is logically circular.

**2. Invalid Use of Euler-Mascheroni Constant**:
Equation (2.11) states λ + μ = 1 + γ/2 - (1/2)log(4π), but Liu sets μ = 0 when assuming RH, leading to inconsistencies in his constraint system.

**3. Flawed Taylor Series Analysis**:
Liu's manipulations in equations (4.5)-(4.11) involve questionable convergence assumptions and inappropriate term-by-term operations on conditionally convergent series.

**4. Contradictory Numerical Substitutions**:
- Liu uses z = 1.0×10^-10 and z = -z in equations (4.20)-(4.23)
- These lead to the contradictory bounds (4.25) and (4.26)
- The contradiction arises from computational errors, not mathematical truth

**5. Misapplication of Hadamard Factorization**:
Liu's expansion of ξ(s) in equation (3.1) contains errors in handling the infinite product convergence and zero multiplicities.

### 2.4 Specific Mathematical Flaws

**Equation (4.24)**: Liu writes λ = 1 + γ/2 - (1/2)log(4π) ≈ 0.0228
But from Theorem 2.4, this should include the μ term, which Liu incorrectly sets to zero.

**Equations (4.25) vs (4.26)**:
```
Liu claims: Σ λ²_m < 3.710063643739287e-05  [from 4.25]
But also:   Σ λ²_m > 3.710063643755369e-05  [from 4.26]
```
This "contradiction" arises from:
- Inappropriate numerical precision claims
- Invalid manipulations of conditionally convergent series
- Computational errors in complex function evaluations

### 2.5 Why Liu's Approach Fails

**1. Fundamental Logical Error**:
Liu assumes the existence of the very objects (off-critical zeros) he's trying to prove exist. The entire framework depends on properties of Ω₂ being non-empty.

**2. Computational Inconsistencies**:
The claimed numerical contradictions result from:
- Inappropriate precision claims in symbolic computation
- Errors in complex function evaluation
- Invalid series manipulations

**3. Violation of Known Results**:
Liu's approach contradicts well-established results about:
- The distribution of zeta function zeros
- Properties of the Euler-Mascheroni constant
- Convergence of series related to zeta zeros

**4. Lack of Verification**:
Unlike Wolf's self-aware analysis of limitations, Liu provides no critical examination of his method's validity or comparison with established results.

---

## 3. Comparative Analysis

### 3.1 Methodological Differences

| Aspect | Wolf (2009) | Liu (2024) |
|--------|-------------|------------|
| **Approach** | Computational verification | Theoretical proof by contradiction |
| **Self-awareness** | Acknowledges limitations | Claims definitive proof |
| **Rigor** | High computational precision | Flawed mathematical logic |
| **Verifiability** | Results can be reproduced | Contains fundamental errors |

### 3.2 Common Failure Modes

**1. Scale Misunderstanding**:
Both approaches underestimate the mathematical difficulty of disproving RH. The problem requires techniques beyond current computational or elementary analytical methods.

**2. Precision vs. Truth**:
Wolf achieves remarkable computational precision (10^-996) but this doesn't constitute mathematical proof. Liu claims mathematical certainty but makes computational errors.

**3. Missing Key Insights**:
Neither approach engages with the deep structural reasons why RH is difficult - the connections to random matrix theory, L-functions, and modular forms.

---

## 4. Valid Insights Despite Failures

### 4.1 From Wolf's Work

**Computational Techniques**:
- Demonstrates sophisticated use of PARI/GP and Mathematica
- Shows importance of high-precision arithmetic in number theory
- Validates the Báez-Duarte criterion computationally

**Theoretical Analysis**:
- Provides realistic estimates of computational requirements
- Correctly identifies fundamental obstacles to computational disproof
- Contributes to understanding of ζ-function zero computations

### 4.2 From Liu's Work

**Mathematical Formalism**:
Despite errors, Liu's work demonstrates:
- Systematic approach to infinite product expansions
- Use of Hadamard factorization techniques
- Application of complex analysis to RH

**Cautionary Value**:
Liu's errors serve as examples of:
- How circular reasoning can hide in complex proofs
- Why numerical precision claims need careful verification
- The importance of independent verification

---

## 5. Why These Attempts Were Not Accepted

### 5.1 Wolf's Rejection

**Scientific Honesty**: Wolf himself explains why his approach fails:
- "The refutation of the RH by computer methods seems to be as difficult as the analytical proof of its validity"
- Cites Borwein brothers' work on "high precision fraud"
- Acknowledges that 996-digit agreement means "nothing about the validity of the RH"

**Peer Review Recognition**: The mathematical community recognized:
- Computational approach insufficient for RH resolution
- High precision agreement more likely supports RH than refutes it
- Theoretical estimates show computational disproof is impossible with current technology

### 5.2 Liu's Rejection

**Mathematical Errors**: The paper contains:
- Circular reasoning in core argument
- Computational errors presented as rigorous proof
- Misapplication of standard theorems
- Contradictory assumptions about constants

**Lack of Verification**: Unlike legitimate mathematical work:
- No independent verification of key claims
- No engagement with established RH literature
- No acknowledgment of potential limitations
- Claims certainty where skepticism is warranted

---

## 6. Lessons for Future Attempts

### 6.1 Computational Approaches

**Requirements for Validity**:
1. **Scale Recognition**: Must acknowledge the astronomical computational requirements
2. **Precision vs. Proof**: High precision agreement supports rather than refutes RH
3. **Theoretical Foundation**: Need deep understanding of why computational disproof is likely impossible

**Wolf's Legacy**: Demonstrates that even sophisticated computational approaches with extreme precision cannot resolve RH through brute force.

### 6.2 Theoretical Approaches

**Critical Requirements**:
1. **Logical Consistency**: Must avoid circular reasoning
2. **Established Results**: Cannot contradict well-known theorems
3. **Independent Verification**: Claims must be verifiable by others
4. **Limitation Recognition**: Must acknowledge potential errors

**Liu's Cautionary Tale**: Shows how complex mathematical formalism can obscure fundamental logical errors.

---

## 7. Conclusion

Both Wolf (2009) and Liu (2024) attempted to disprove the Riemann Hypothesis but failed for different reasons:

**Wolf's Computational Failure**:
- Achieved remarkable 10^-996 computational precision
- Correctly identified why his approach must fail
- Provided valuable computational techniques and realistic difficulty estimates
- Failed because computational disproof requires impossible precision levels

**Liu's Theoretical Failure**:
- Made fundamental logical errors (circular reasoning)
- Presented computational mistakes as rigorous proof
- Failed to engage with established mathematical literature
- Created apparent contradictions through invalid mathematical manipulations

**Overall Assessment**:
These failures illustrate why RH remains unsolved after 165+ years. The problem requires:
- Mathematical insights beyond current computational capability
- Theoretical advances connecting diverse areas of mathematics
- Recognition that elementary approaches are likely insufficient

The mathematical community's rejection of these attempts demonstrates:
- Rigorous standards for accepting RH-related claims
- Ability to identify both computational and theoretical limitations
- Appreciation for the profound difficulty of the problem

Wolf's honest self-assessment contrasts sharply with Liu's overconfident claims, highlighting the importance of intellectual humility when tackling millennium problems.