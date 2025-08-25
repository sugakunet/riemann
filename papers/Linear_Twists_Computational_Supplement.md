# Computational Supplement: Linear Twists and Lindelöf Hypothesis

## Python Implementation Guide for Numerical Experiments

### 1. Basic Implementation of Linear Twists

```python
import numpy as np
from scipy.special import zeta
import matplotlib.pyplot as plt
from mpmath import mp, zetazero

# Set precision for high-accuracy computations
mp.dps = 50

def linear_twist(s, a, N_max=10000):
    """
    Compute the linear twist Z(s,a) = sum_{n=1}^{N_max} e(na)/n^s
    
    Parameters:
    s: complex number (typically 1/2 + it)
    a: real parameter (rational or irrational)
    N_max: truncation point for the sum
    """
    n = np.arange(1, N_max + 1)
    phases = np.exp(2j * np.pi * a * n)
    terms = phases / (n ** s)
    
    # Compute partial sums for convergence analysis
    partial_sums = np.cumsum(terms)
    
    return partial_sums[-1], partial_sums

def compare_growth_rates(t_values, parameters):
    """
    Compare |Z(1/2 + it, a)| for different parameters a
    """
    results = {}
    
    for a_name, a_value in parameters.items():
        z_values = []
        for t in t_values:
            s = 0.5 + 1j * t
            z, _ = linear_twist(s, a_value, N_max=int(10 * t))
            z_values.append(abs(z))
        results[a_name] = np.array(z_values)
    
    return results

# Example parameters to test
test_parameters = {
    'rational_1/2': 0.5,
    'rational_13/89': 13/89,  # Fibonacci ratio approximation
    'sqrt_2': np.sqrt(2),
    'golden_ratio': (1 + np.sqrt(5))/2,
    'e_minus_2': np.e - 2,
    'pi_minus_3': np.pi - 3
}
```

### 2. Moment Calculations

```python
def compute_moments(a, T_max=1000, num_points=500, k_max=3):
    """
    Compute the k-th moments of |Z(1/2 + it, a)|
    """
    t_values = np.linspace(1, T_max, num_points)
    z_values = []
    
    for t in t_values:
        s = 0.5 + 1j * t
        z, _ = linear_twist(s, a, N_max=int(10 * t))
        z_values.append(abs(z))
    
    z_values = np.array(z_values)
    moments = {}
    
    for k in range(1, k_max + 1):
        # Numerical integration using trapezoidal rule
        integrand = z_values ** (2 * k)
        moment = np.trapz(integrand, t_values) / T_max
        moments[k] = moment
        
        # Estimate growth exponent: M_k(T) ~ T * (log T)^alpha_k
        # We fit log(M_k/T) ~ alpha_k * log(log T)
        if T_max > 100:
            log_log_T = np.log(np.log(T_max))
            alpha_k = np.log(moment / T_max) / log_log_T if log_log_T > 0 else 0
            moments[f'alpha_{k}'] = alpha_k
    
    return moments

def moment_growth_analysis(a, T_values=[100, 200, 500, 1000]):
    """
    Analyze how moments grow with T
    """
    growth_data = {k: [] for k in range(1, 4)}
    
    for T in T_values:
        moments = compute_moments(a, T_max=T)
        for k in range(1, 4):
            growth_data[k].append(moments[k])
    
    # Fit growth rates
    for k in range(1, 4):
        y = np.log(growth_data[k])
        x = np.log(T_values)
        
        # Linear regression in log-log space
        coeffs = np.polyfit(x, y, 1)
        print(f"Moment {k}: Growth ~ T^{coeffs[0]:.3f}")
        
        # Check if it matches T(log T)^k or T(log T)^(k^2)
        theoretical_random = 1 + k * np.log(np.log(T_values[-1])) / np.log(T_values[-1])
        theoretical_zeta = 1 + k**2 * np.log(np.log(T_values[-1])) / np.log(T_values[-1])
        
        print(f"  Expected for random phases: T^{theoretical_random:.3f}")
        print(f"  Expected for zeta function: T^{theoretical_zeta:.3f}")
    
    return growth_data
```

### 3. Diophantine Properties Analysis

```python
def continued_fraction(x, max_terms=20):
    """
    Compute continued fraction expansion of x
    """
    cf = []
    for _ in range(max_terms):
        a = int(x)
        cf.append(a)
        x = x - a
        if abs(x) < 1e-10:
            break
        x = 1/x
    return cf

def best_rational_approximations(x, max_denom=1000):
    """
    Find best rational approximations using continued fractions
    """
    cf = continued_fraction(x, 30)
    convergents = []
    
    h_prev, k_prev = 0, 1
    h_curr, k_curr = 1, 0
    
    for a in cf:
        h_next = a * h_curr + h_prev
        k_next = a * k_curr + k_prev
        
        if k_next > max_denom:
            break
            
        convergents.append((h_next, k_next, abs(x - h_next/k_next)))
        h_prev, k_prev = h_curr, k_curr
        h_curr, k_curr = h_next, k_next
    
    return convergents

def irrationality_measure_estimate(x, sample_size=10000):
    """
    Estimate the irrationality measure of x
    """
    approximations = best_rational_approximations(x, sample_size)
    
    mu_estimates = []
    for p, q, error in approximations:
        if error > 0 and q > 1:
            # |x - p/q| ~ 1/q^mu
            mu = -np.log(error) / np.log(q)
            mu_estimates.append(mu)
    
    # Use median to avoid outliers
    if mu_estimates:
        return np.median(mu_estimates)
    return 2.0  # Default for algebraic numbers

def analyze_parameter_quality(a):
    """
    Comprehensive analysis of parameter a
    """
    print(f"\nAnalyzing parameter a = {a:.10f}")
    print("-" * 40)
    
    # Continued fraction
    cf = continued_fraction(a, 10)
    print(f"Continued fraction: {cf}")
    
    # Best approximations
    approx = best_rational_approximations(a, 100)
    print(f"Best approximations (p/q, error):")
    for p, q, err in approx[:5]:
        print(f"  {p}/{q}: error = {err:.2e}")
    
    # Irrationality measure
    mu = irrationality_measure_estimate(a)
    print(f"Estimated irrationality measure: {mu:.3f}")
    
    # Classification
    if mu < 2.1:
        print("Classification: Likely algebraic (quadratic or higher)")
    elif mu < 2.5:
        print("Classification: Typical transcendental")
    else:
        print("Classification: Possible Liouville-like number")
    
    return mu
```

### 4. Experimental Zero Finding

```python
def find_zeros_linear_twist(a, s_range=(0.1, 0.9), t_max=100, resolution=0.01):
    """
    Search for zeros of Z(s,a) in a region
    Note: Zeros won't lie on a line for irrational a
    """
    sigma_values = np.linspace(s_range[0], s_range[1], int((s_range[1]-s_range[0])/resolution))
    t_values = np.linspace(0.1, t_max, int(t_max/resolution))
    
    zeros = []
    
    for sigma in sigma_values:
        for t in t_values:
            s = sigma + 1j * t
            z1, _ = linear_twist(s, a, N_max=1000)
            
            # Check small neighborhood for sign changes
            eps = 0.001
            z2, _ = linear_twist(s + eps, a, N_max=1000)
            z3, _ = linear_twist(s + 1j*eps, a, N_max=1000)
            
            # Simple zero detection (needs refinement)
            if abs(z1) < 0.1 and (np.sign(z1.real) != np.sign(z2.real) or 
                                  np.sign(z1.imag) != np.sign(z3.imag)):
                zeros.append(s)
    
    return zeros

def zero_distribution_analysis(a, num_zeros=100):
    """
    Analyze the distribution of zeros
    """
    zeros = find_zeros_linear_twist(a, t_max=50)
    
    if len(zeros) > 0:
        real_parts = [z.real for z in zeros]
        imag_parts = [z.imag for z in zeros]
        
        print(f"Found {len(zeros)} potential zeros")
        print(f"Mean real part: {np.mean(real_parts):.3f}")
        print(f"Std dev of real parts: {np.std(real_parts):.3f}")
        
        # Check clustering
        if len(zeros) > 10:
            spacings = np.diff(sorted(imag_parts))
            print(f"Mean spacing (imaginary): {np.mean(spacings):.3f}")
            print(f"Spacing variance: {np.var(spacings):.3f}")
    
    return zeros
```

### 5. Comparison with Dirichlet L-functions

```python
def dirichlet_character(n, q, a):
    """
    Simple Dirichlet character mod q
    """
    if np.gcd(n, q) != 1:
        return 0
    # Principal character for simplicity
    return np.exp(2j * np.pi * a * n / q)

def dirichlet_L(s, q, a, N_max=10000):
    """
    Compute Dirichlet L-function with character mod q
    """
    n = np.arange(1, N_max + 1)
    chi = np.array([dirichlet_character(k, q, a) for k in n])
    terms = chi / (n ** s)
    return np.sum(terms)

def compare_linear_vs_dirichlet(t_values):
    """
    Compare linear twist with Dirichlet L-function for same denominator
    """
    q = 89  # Prime for clean comparison
    
    results = {
        'linear_13/89': [],
        'dirichlet_mod_89': [],
        'linear_sqrt2': [],
        'riemann_zeta': []
    }
    
    for t in t_values:
        s = 0.5 + 1j * t
        
        # Linear twist with rational parameter
        z1, _ = linear_twist(s, 13/89, N_max=int(10*t))
        results['linear_13/89'].append(abs(z1))
        
        # Dirichlet L-function
        z2 = dirichlet_L(s, 89, 13, N_max=int(10*t))
        results['dirichlet_mod_89'].append(abs(z2))
        
        # Linear twist with irrational parameter  
        z3, _ = linear_twist(s, np.sqrt(2), N_max=int(10*t))
        results['linear_sqrt2'].append(abs(z3))
        
        # Riemann zeta for reference
        z4 = float(mp.zeta(0.5 + 1j*t))
        results['riemann_zeta'].append(abs(z4))
    
    return results
```

### 6. Visualization Tools

```python
def plot_growth_comparison(results, t_values):
    """
    Visualize growth rates of different twists
    """
    plt.figure(figsize=(12, 8))
    
    for label, values in results.items():
        plt.loglog(t_values, values, label=label, linewidth=2)
    
    # Add reference lines
    plt.loglog(t_values, t_values**0.155, 'k--', 
               label='t^{13/84} (current bound)', alpha=0.5)
    plt.loglog(t_values, t_values**0.25, 'k:', 
               label='t^{1/4} (trivial bound)', alpha=0.5)
    
    plt.xlabel('t', fontsize=12)
    plt.ylabel('|Z(1/2 + it, a)|', fontsize=12)
    plt.title('Growth Rate Comparison: Linear Twists vs L-functions', fontsize=14)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_moment_scaling(moment_data, T_values):
    """
    Visualize moment growth
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for k in range(1, 4):
        ax = axes[k-1]
        
        # Plot actual moments
        ax.loglog(T_values, moment_data[k], 'o-', label=f'M_{k}(T)')
        
        # Plot theoretical predictions
        T_array = np.array(T_values)
        random_theory = T_array * (np.log(T_array))**k
        zeta_theory = T_array * (np.log(T_array))**(k**2)
        
        ax.loglog(T_array, random_theory, '--', 
                  label=f'T(log T)^{k} (random)')
        ax.loglog(T_array, zeta_theory, ':', 
                  label=f'T(log T)^{k**2} (zeta)')
        
        ax.set_xlabel('T')
        ax.set_ylabel(f'M_{k}(T)')
        ax.set_title(f'{k}-th Moment Growth')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

### 7. Main Experimental Framework

```python
def run_comprehensive_experiment():
    """
    Run full experimental analysis
    """
    print("=" * 60)
    print("COMPREHENSIVE LINEAR TWIST ANALYSIS")
    print("=" * 60)
    
    # Define parameters to test
    parameters = {
        'rational_small': 1/3,
        'rational_medium': 13/89,
        'rational_large': 355/113,  # Good approximation to pi
        'sqrt_2': np.sqrt(2),
        'golden_ratio': (1 + np.sqrt(5))/2,
        'e_minus_2': np.e - 2,
        'pi_minus_3': np.pi - 3,
        'liouville_like': sum(10**(-np.math.factorial(k)) for k in range(1, 6))
    }
    
    # 1. Analyze Diophantine properties
    print("\n1. DIOPHANTINE ANALYSIS")
    print("=" * 60)
    mu_values = {}
    for name, value in parameters.items():
        if 'rational' not in name:
            mu = analyze_parameter_quality(value)
            mu_values[name] = mu
    
    # 2. Growth rate comparison
    print("\n2. GROWTH RATE ANALYSIS")
    print("=" * 60)
    t_values = np.logspace(1, 3, 50)  # t from 10 to 1000
    growth_results = compare_growth_rates(t_values, parameters)
    
    # Fit power laws
    for name, values in growth_results.items():
        # Fit log|Z| ~ alpha * log(t)
        coeffs = np.polyfit(np.log(t_values[10:]), np.log(values[10:]), 1)
        print(f"{name}: |Z(1/2+it,a)| ~ t^{coeffs[0]:.4f}")
    
    # 3. Moment analysis
    print("\n3. MOMENT ANALYSIS")
    print("=" * 60)
    for name in ['sqrt_2', 'rational_medium', 'pi_minus_3']:
        print(f"\nParameter: {name}")
        moment_data = moment_growth_analysis(parameters[name])
    
    # 4. Linear vs Dirichlet comparison
    print("\n4. LINEAR VS DIRICHLET COMPARISON")
    print("=" * 60)
    comparison = compare_linear_vs_dirichlet(t_values)
    
    # Calculate average ratio
    for key in comparison:
        if key != 'riemann_zeta':
            ratios = np.array(comparison[key]) / np.array(comparison['riemann_zeta'])
            print(f"{key}: Average ratio to zeta = {np.mean(ratios):.3f}")
    
    # 5. Visualization
    plot_growth_comparison(growth_results, t_values)
    
    # Save results
    import json
    with open('linear_twist_results.json', 'w') as f:
        json.dump({
            'parameters': {k: float(v) for k, v in parameters.items()},
            'mu_values': mu_values,
            'growth_exponents': {k: float(np.polyfit(np.log(t_values[10:]), 
                                                    np.log(v[10:]), 1)[0]) 
                                for k, v in growth_results.items()}
        }, f, indent=2)
    
    print("\nResults saved to linear_twist_results.json")
    
    return growth_results, mu_values

# Run the experiment
if __name__ == "__main__":
    results, mu_values = run_comprehensive_experiment()
```

## Implementation Notes

### Numerical Challenges

1. **Convergence Issues**: Linear twists converge slowly. Use acceleration methods:
   - Euler-Maclaurin summation
   - Shanks transformation
   - Richardson extrapolation

2. **Precision Requirements**: For large $t$, use arbitrary precision libraries:
   ```python
   from mpmath import mp
   mp.dps = 100  # 100 decimal places
   ```

3. **Oscillatory Integrals**: For moment calculations, use specialized methods:
   - Filon quadrature
   - Levin's method
   - Asymptotic expansions

### Optimization Strategies

1. **Vectorization**: Use NumPy arrays for bulk computations
2. **Caching**: Store computed values for reuse
3. **Parallelization**: Use multiprocessing for parameter sweeps:
   ```python
   from multiprocessing import Pool
   
   def parallel_computation(params):
       with Pool() as pool:
           results = pool.map(analyze_parameter, params)
       return results
   ```

### Validation Tests

1. **Rational Parameters**: Verify decomposition into Dirichlet L-functions
2. **Known Values**: Check against tabulated values where available
3. **Symmetries**: Verify expected symmetries and functional relationships
4. **Convergence**: Monitor partial sum convergence

## Expected Results

Based on theoretical predictions:

1. **Growth Exponents**:
   - Quadratic irrationals: $\approx 0$ (Lindelöf satisfied)
   - Rational $p/q$: Increases with $q$
   - Typical transcendentals: $\approx 0$
   - Liouville numbers: Potentially $> 0$

2. **Moment Growth**:
   - Linear twists (irrational): $M_k(T) \sim T(\log T)^k$
   - Dirichlet L-functions: $M_k(T) \sim T(\log T)^{k^2}$

3. **Zero Distribution**:
   - Not on a line for irrational parameters
   - More scattered than Riemann zeros
   - Possible fractal structure

## Future Computational Directions

1. **Machine Learning**: Train models to predict growth from Diophantine properties
2. **GPU Acceleration**: Massive parallel computation of many parameters
3. **Symbolic Computation**: Exact arithmetic for special algebraic values
4. **Distributed Computing**: Large-scale parameter space exploration

This computational framework provides the tools needed to test the conjectures about linear twists and their superior cancellation properties compared to Dirichlet L-functions.