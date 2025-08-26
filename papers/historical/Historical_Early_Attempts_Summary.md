# Historical Perspective and Early Attempts at the Riemann Hypothesis

## Overview
This document summarizes the historical attempts and contributions by early mathematicians to prove or understand the Riemann Hypothesis, with particular focus on the work of Stieltjes, Mertens, Littlewood, Siegel, Lindelöf, Denjoy, and Hardy.

## 1. Thomas Stieltjes (1885)

### The Claim
- In 1885, Dutch mathematician Thomas Stieltjes claimed to have a proof of the Riemann Hypothesis
- Published a note in Comptes Rendus of the Paris Academy of Sciences
- Actually claimed to prove something stronger: the Mertens conjecture, from which RH would follow
- Wrote to Hermite: "My proof is very arduous; I shall try to simplify it further when I resume my research on these questions"

### The Outcome
- The proof was never published
- No proof found in his papers after his death
- The claim is now thoroughly discredited because:
  1. The Mertens conjecture was proven false in 1985 by Odlyzko and te Riele
  2. Therefore, his approach could not possibly have worked
- Despite this, Stieltjes was a respected mathematician (Riemann-Stieltjes integral named after him)

## 2. Franz Mertens and the Mertens Conjecture

### The Conjecture (1897)
- Mertens independently published the conjecture in 1897
- States that |M(x)|/√x < 1 for all x > 1, where M(x) is the Mertens function
- The conjecture would have implied the Riemann Hypothesis
- Verified computationally up to x < 10^9 by von Sterneck in 1912

### The Disproof (1985)
- **Andrew Odlyzko and Herman te Riele** disproved the conjecture in 1985
- Published in: Journal für die reine und angewandte Mathematik, vol. 357, pp. 138-160
- Method: Used the Lenstra-Lenstra-Lovász (LLL) lattice basis reduction algorithm
- Result: Showed that lim sup M(x)/x^(1/2) > 1.06
- Nature: Indirect proof - no explicit counterexample provided
- Bounds: Believed no counterexamples exist for x < 10^20
- Later work reduced explicit upper bound from exp(3.21×10^64) to exp(1.59×10^40)

## 3. J.E. Littlewood (1914)

### The Oscillation Result
- **Major Discovery**: Proved that π(x) - li(x) changes sign infinitely often
- This overturned the long-held belief (by Gauss and Riemann) that π(x) < li(x) always
- All numerical evidence had supported π(x) < li(x)

### Method
- Proof divided into two cases:
  1. RH is false (about half a page of proof)
  2. RH is true (about a dozen pages)
- Showed oscillatory behavior is controlled by zeros of the Riemann zeta function

### The Skewes Number
- Littlewood's proof was non-constructive (didn't give explicit values)
- His student Stanley Skewes later found upper bounds:
  - First Skewes number (1933): e^(e^(e^79)) assuming RH
  - Second Skewes number (1955): 10^(10^(10^963)) without assuming RH
- Modern computations show first sign change occurs around x = 1.39822 × 10^316

### Other Contributions
- 1912: Showed equivalence conditions for the Riemann hypothesis
- Collaborated extensively with Hardy on prime number theory
- Work has been improved by Landau, Titchmarsh, Maier, Montgomery, and Soundararajan

## 4. Carl Ludwig Siegel (1932)

### The Riemann-Siegel Formula Discovery
- **Major Discovery**: Found the Riemann-Siegel formula in Riemann's unpublished manuscripts from the 1850s
- Published his findings in 1932
- The formula is an asymptotic expression for computing the Riemann zeta function

### Historical Significance
- Revealed that Riemann had made detailed numerical calculations of zeros
- Showed Riemann's hypothesis wasn't just intuition but based on computation
- The formula became a fundamental computational tool for studying ζ(s)
- Often used with the Odlyzko-Schönhage algorithm for efficiency

### Connection to Theta Functions
- For real positive t: Z(t) = e^(iθ(t))ζ(1/2+it)
- Where θ(t) is the Riemann-Siegel theta function

## 5. Ernst Leonard Lindelöf (1908)

### The Lindelöf Hypothesis
- Proposed in 1908 by Finnish mathematician Ernst Leonard Lindelöf
- States: For any ε > 0, ζ(1/2 + it) = O(t^ε) as t → ∞
- In other words: The zeta function grows very slowly on the critical line

### Relationship to RH
- The Riemann Hypothesis implies the Lindelöf Hypothesis
- The converse is not necessarily true
- A proof of Lindelöf would be a major breakthrough

### Alternative Formulation (Backlund 1918-1919)
- Equivalent statement about zeros: For every ε > 0, the number of zeros with real part ≥ 1/2 + ε and imaginary part between T and T+1 is o(log(T))

### Current Status
- Despite seeming "only slightly stronger" than proven results, it remains unproven
- The number of zeros with imaginary part between T and T+1 is known to be O(log(T))

## 6. Arnaud Denjoy (1921)

### Quasi-Analytic Functions
- In 1921, gave partial results contributing to the Denjoy-Carleman theorem
- Completed by Torsten Carleman in 1926
- Focused on quasi-analytic classes of functions
- These generalize real analytic functions with uniqueness properties

### Connection to RH
- No direct connection to the classical Riemann Hypothesis found
- Work was primarily in establishing foundations of quasi-analytic function theory
- Applications mainly in analysis and differential equations

### Contemporary Development
- Same year (1921): Emil Artin wrote thesis on RH for function fields
- This led to André Weil's proof in 1948 for the function field case

## 7. G.H. Hardy (1914)

### The Critical Line Result
- **Breakthrough**: First proof that infinitely many zeros lie on the critical line Re(s) = 1/2
- Published: "Sur les zéros de la fonction ζ(s) de Riemann" in Comptes Rendus
- Method: Used transformation formula of the Jacobi theta function

### Significance
- First rigorous proof that at least some zeros must be on the critical line
- Didn't prove all zeros are there (as RH requires), but showed infinitely many are
- Established foundation for future work on zero distribution

### Subsequent Improvements
- Hardy-Littlewood (1921): Proved ≫ T zeros on critical line up to height T
- Selberg (1942): Proved ≫ T log T zeros (a positive proportion)
- Conrey (1989): Proved more than 40% of zeros are on critical line
- Current record (Feng 2012): At least 41.28% of zeros on critical line

### Hardy-Littlewood Conjectures (1922-1923)
- First Hardy-Littlewood conjecture: On asymptotic density of prime k-tuples
- Second Hardy-Littlewood conjecture: About primes in intervals
- Paper: "Some problems of 'Partitio Numerorum' III" (Acta Math. 44, 1922)

## Papers Downloaded

The following papers have been saved to `/papers/historical/`:

1. **physics_RH.pdf** - "Physics of the Riemann Hypothesis" (arXiv:1101.3116)
   - Examines RH's influence in physics and physical approaches to the problem

2. **essay_RH.pdf** - "An essay on the Riemann Hypothesis" (arXiv:1509.05576)
   - General essay on the hypothesis and approaches

3. **ramanujan_robin_RH.pdf** - "Ramanujan, Robin, Highly Composite Numbers, and the Riemann Hypothesis" (arXiv:1211.6944)
   - Historical account of equivalent conditions for RH

4. **skewes_twin_primes.pdf** - "The Skewes number for twin primes" (arXiv:1107.2809)
   - Extension of Skewes number concept to twin primes

5. **littlewood_prime_proof.pdf** - "On Littlewood's proof of the prime number theorem" (arXiv:1906.09906)
   - Analysis of Littlewood's proof methods

## Key Historical Lessons

1. **False Claims**: Even respected mathematicians (Stieltjes) can believe they have proofs that are incorrect

2. **Computational Evidence Can Be Misleading**: 
   - Mertens conjecture verified to 10^9 but still false
   - π(x) < li(x) appears true for all computable values but reverses eventually

3. **Indirect Methods**: Many results (Littlewood's oscillation, Odlyzko-te Riele disproof) are existence proofs without explicit examples

4. **Progress is Incremental**: 
   - 1914: Infinitely many zeros on critical line (Hardy)
   - 1942: Positive proportion on critical line (Selberg)
   - 1989: 40% on critical line (Conrey)
   - 2012: 41.28% on critical line (Feng)

5. **Interdisciplinary Connections**: Modern approaches use:
   - Lattice reduction algorithms (computer science)
   - Random matrix theory (physics)
   - Spectral theory (operator theory)

## References for Further Reading

- Bombieri, E. "Problems of the Millennium: The Riemann Hypothesis" (Clay Mathematics Institute)
- Edwards, H.M. "Riemann's Zeta Function" (1974)
- Titchmarsh, E.C. "The Theory of the Riemann Zeta-Function" (1986)
- Conrey, J.B. "The Riemann Hypothesis" (Notices of the AMS, 2003)
- Odlyzko, A.M. and te Riele, H.J.J. "Disproof of the Mertens Conjecture" (1985)