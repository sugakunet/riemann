# Jonathan Bober's Computational Work on the Riemann Zeta Function and L-functions

## Overview

Jonathan Bober's research represents groundbreaking computational achievements in understanding the Riemann zeta function and L-functions at unprecedented scales. His work combines theoretical innovation with practical implementation, pushing computational boundaries to reveal new insights about zeta behavior at extreme heights.

## Key Papers Analyzed

1. **New Computations of the Riemann Zeta Function on the Critical Line** (with Ghaith Hiary, 2016)
2. **The Highest Lowest Zero of General L-functions** (with Conrey, Farmer, et al., 2012)
3. **A Conjectural Extension of Hecke's Converse Theorem** (with Bettin, Booker, Conrey, et al., 2017)
4. **Computing Classical Modular Forms** (with Best, Booker, Costa, Cremona, et al., 2022)

## 1. Extreme Value Computations of ζ(1/2 + it)

### Revolutionary Achievement: Computing at t ≈ 10^32

Bober and Hiary implemented the first practical O(t^(1/3)) algorithm for computing ζ(1/2 + it) at unprecedented heights, reaching values around the **10^36-th zero** of the Riemann zeta function.

### Key Computational Breakthroughs

#### The O(t^(1/3)) Algorithm Implementation
- **Core innovation**: Transforms Riemann-Siegel main sum into quadratic exponential sums
- **Subdivision strategy**: Main sum M(t) = Σ_{n=1}^N e^(it log n)/√n divided into R+1 blocks
- **Fast evaluation**: Uses Poisson summation to reduce sum lengths iteratively
- **Complexity reduction**: Each iteration reduces sum length by factor ~2, total ~log K iterations

#### Multi-evaluation Method
- Enables efficient computation of ζ at multiple nearby points t₀ + δj
- Factors out oscillation: e^(i(t₀+δj) log v)/√v = (e^(it₀ log v)/√v) × e^(iδj log v)
- Cost: Little more than single-point evaluation for small ranges

### Record-Breaking Discoveries

#### Largest |Z(t)| Values Found
- **Absolute record**: |Z(t)| ≈ **16,244.865** at t ≈ 3.92 × 10^28
- Previous computational records were orders of magnitude smaller
- Found 12 values above 10,000 (see Table 1 in paper)

#### Extreme S(t) Values
Where S(t) = (1/π) arg ζ(1/2 + it) measures irregularity in zero distribution:
- **Maximum**: S(t) ≈ 3.3455 at t ≈ 7.76 × 10^27
- **Range discovered**: -3.27 to +3.27
- **Significance**: Previous record was only S(t) ≈ -2.9076
- Found 11 values with |S(t)| > 3.1

### Insights About Zeta Behavior at Large Heights

#### Zero Distribution Patterns
- When |ζ(1/2 + it)| is very large, nearby zeros are "pushed away"
- S(t) becomes large and positive before the peak
- S(t) becomes large and negative after the peak
- This creates compensating irregularities in zero distribution

#### Computational Verification
- Computed >50,000 zeros in >200 intervals up to 10^36-th zero
- All zeros found on critical line (consistent with RH)
- Used Turing's method to verify completeness of zero lists

### Computational Resources and Feasibility
- Used "Riemann machine" cluster: 16 nodes, 8 cores each at 2.27GHz
- Largest computation: ~22.5 cpu-core-years
- **Future potential**: Estimated feasible up to 10^40-th zero with current methods

## 2. L-functions with Exceptional Properties

### The Highest Lowest Zero Discovery

Bober and collaborators found a degree-4 L-function whose first zero at t ≈ **14.496** exceeds the Riemann zeta function's first zero at t ≈ 14.134, disproving a conjecture by Stephen D. Miller.

#### Computational Methods
- High-precision computation of spectral parameters: μ₁ = 4.72095103638565339773i
- Verification using Z-function for zero detection
- Consistency tests to validate numerical L-function

#### Theoretical Implications
- Shows Riemann zeta does not have universally highest lowest zero
- Reveals "Strombergsson effect": trivial zeros suppress nearby critical zeros
- Establishes universal bound: all L-functions have zeros in (-22.661, 22.661)

## 3. Revolutionary Approach to Modular Forms

### Linearization via Ramanujan Sums

The conjectural extension of Hecke's converse theorem replaces nonlinear Euler product requirements with linear constraints using Ramanujan sum twists.

#### Key Innovation
Instead of requiring:
- Euler product (nonlinear)
- Character twist functional equations

The conjecture requires only:
- Functional equations for Ramanujan sum twists Λf(s, cq)
- These are **purely linear constraints**

#### Computational Verification
- Conjecture verified for N ≤ 9 and N ∈ {11, 15, 17, 23}
- Uses minimal generating sets for Γ₀(N) computed with Sage
- Provides explicit algorithms for verification

## 4. Large-Scale Modular Forms Computation

### LMFDB Database Achievement
Bober contributed to computing:
- **281,219 newform orbits** across 62,142 newspaces
- **14,398,359 embedded newforms** with complex coefficients
- Complete L-function data with rigorous verification

### Algorithmic Innovations

#### LLL-Optimized Coefficient Storage
- Revolutionary technique reducing storage by orders of magnitude
- Uses LLL-reduced basis for coefficient ring
- Example: Degree-20 field coefficients reduced to small integer combinations

#### Comparative Algorithm Analysis
| Method | Full trace form O(q^r) | Basis to O(q^r) |
|--------|------------------------|------------------|
| Modular Symbols | Õ(dr²) | Õ(dr²) |
| Trace Formula | Õ(r^(3/2)) | Õ(d^(3/2)r^(3/2)) |

## 5. Implications for Understanding the Riemann Hypothesis

### Direct RH Verification
- No counterexamples found up to height 10^32
- Verified GRH for 14+ million L-functions in LMFDB
- All computed zeros lie on critical line

### Behavioral Insights at Extreme Heights

#### Growth Bounds Context
Current theoretical bounds:
- **Conditional upper**: |ζ(1/2 + it)| ≪ exp[(log 2/2)(log t)/(log log t)]
- **Unconditional lower**: |ζ(1/2 + it)| > exp[(1/√2)√((log t log log log t)/(log log t))]
- Bober's value of 16,244 at t ≈ 10^28 provides crucial data points

#### Irregularity Persistence
- Large values occur sporadically with no apparent pattern
- Correlation between large |ζ| and large zero gaps confirmed
- S(t) compensation mechanism revealed

### Computational Methodology Impact

#### Feasibility Demonstrations
- First practical sub-polynomial algorithm implementation
- Opens systematic exploration of previously inaccessible regions
- Enables statistical analysis of extreme value distributions

#### Cross-Validation Architecture
- Multiple independent implementations (Magma, Pari/GP, custom C++)
- Rigorous interval arithmetic using Arb library
- Total computational investment: >100 CPU-years

## 6. Software Tools and Resources

### zetacalc Repository
- GitHub: https://github.com/jwbober/zetacalc
- C++ implementation of O(t^(1/3)) algorithm
- Computes quadratic exponential sums and ζ(1/2 + it)

### Data Resources
- Extreme value data: https://people.maths.bris.ac.uk/~jb12407/data/zeta/
- Includes visualizations, plots of Z(t) and S(t)
- Some entries include videos of partial sum evolution

## 7. Connection to Your Research on RH

### Relevance to Complex Analytic Approaches

1. **Extreme Value Distribution**: Bober's discoveries of |ζ| ≈ 16,244 provide crucial empirical data for:
   - Testing growth conjectures
   - Understanding zero repulsion mechanisms
   - Calibrating probabilistic models

2. **S(t) Irregularities**: The discovery of S(t) values exceeding ±3.2 reveals:
   - Persistent irregularity at all scales
   - Compensation mechanisms in zero distribution
   - Potential connections to random matrix theory predictions

3. **Computational Verification Methods**: The O(t^(1/3)) algorithm enables:
   - Testing conjectures at unprecedented heights
   - Statistical analysis of zero distributions
   - Verification of spectral interpretations

### Integration with de Branges Theory
Bober's computational evidence at extreme heights could:
- Test predictions from de Branges spaces
- Verify growth estimates required for operator-theoretic approaches
- Provide data for calibrating functional models

### Connections to Modular Forms Approach
The linearization via Ramanujan sums:
- Eliminates nonlinear Euler product constraints
- Makes modular form spaces explicitly computable
- Could enable new computational attacks on RH via L-functions

## 8. Future Directions Suggested by Bober's Work

### Computational Frontiers
1. **Push to 10^40-th zero**: Feasible with current algorithms
2. **Statistical analysis**: Large-scale study of extreme value distributions
3. **Pattern detection**: Machine learning on zero distribution irregularities

### Theoretical Applications
1. **Growth conjecture testing**: Calibrate theoretical bounds with empirical data
2. **Zero gap analysis**: Understand correlation with large values
3. **S(t) theory**: Develop models for extreme argument behavior

### Algorithmic Development
1. **Further complexity reduction**: Below O(t^(1/3)) if possible
2. **Parallel architectures**: Optimize for modern GPU/TPU systems
3. **Multi-evaluation extensions**: Compute ζ over larger ranges efficiently

## Conclusion

Jonathan Bober's computational work represents a quantum leap in our ability to explore the Riemann zeta function at extreme heights. His discoveries of unprecedented large values, implementation of sub-polynomial algorithms, and innovative approaches to modular forms computation provide both crucial empirical data and powerful computational tools for attacking the Riemann Hypothesis.

The key insights from his work:
- **Empirical evidence**: RH holds up to extraordinary heights (10^32)
- **Behavioral patterns**: Large values correlate with zero distribution irregularities
- **Computational feasibility**: Modern algorithms make previously impossible computations routine
- **Theoretical connections**: Links between modular forms, L-functions, and zeta behavior

For researchers working on RH, Bober's contributions provide:
- Concrete data for testing theoretical predictions
- Computational tools for verification
- New perspectives on the interplay between different approaches
- Evidence for the deep structural properties underlying the hypothesis

His work exemplifies how computational mathematics can drive theoretical understanding, revealing phenomena invisible to pure analysis while providing rigorous verification of conjectures at unprecedented scales.