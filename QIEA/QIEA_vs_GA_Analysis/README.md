# 🔬 Statistical Benchmark: QIEA vs GA on 0/1 Knapsack

This folder contains a comprehensive, statistical benchmark comparing the **Quantum-Inspired Evolutionary Algorithm (QIEA)** with the **Classical Genetic Algorithm (GA)** on the classic 0/1 Knapsack Problem.

While the standalone scripts in the parent directories demonstrate these algorithms on a simple 5-item problem, this notebook scales up the complexity to rigorously test their exploration and exploitation capabilities.

---

## 📓 The Jupyter Notebook
The main file is `QIEA_vs_GA_Knapsack.ipynb`. It is a fully self-contained Jupyter notebook that provides:
1. **From-scratch implementations** of both QIEA and GA.
2. **Dynamic Programming (DP) exact solver** to calculate the absolute ground-truth optimal solutions for all generated knapsack problems.
3. **Rigorous experiment harness** that evaluates both algorithms under identical conditions.
4. **Data analysis and statistical testing** (Mann-Whitney U tests) to compare the algorithms mathematically rather than just visually.

---

## 🧩 The Problem Space

We tested the algorithms on synthetic instances of the 0/1 Knapsack problem with varying sizes: **n = 20, 50, and 100 items**. 
- Item weights and values were drawn uniformly from `[1, 100]`.
- Knapsack capacity was set to exactly **50% of the total sum of all item weights**.
- This creates a dense, constrained search space where greedy heuristics alone cannot guarantee the optimal solution.

---

## 🛠️ Algorithm Configurations

To ensure a fair comparison of computational effort, both algorithms were given the **exact same fitness evaluation budget** (e.g., max 10,000 evaluations).

### Classical GA Setup
- **Population:** 50 individuals
- **Selection:** Tournament selection (k=3)
- **Crossover:** 2-point crossover (rate = 0.8)
- **Mutation:** Bit-flip mutation (rate = 1/n)
- **Elitism:** Top 1 individual preserved

### QIEA Setup
- **Population:** 10 individuals (Q-bit vectors)
- **Initialization:** All qubits at equal superposition ($\theta = \pi/4$)
- **Rotation Gate:** Han & Kim (2002) formulation with $\Delta\theta = 0.05\pi$
- **H-Gate:** Clamping applied to prevent total qubit collapse ($\epsilon = 0.01$)
- **Migration:** Periodic sharing of the best-found solutions (local every 30 generations, global every 70 generations)

### The Repair Mechanism
Since crossover, mutation, and quantum observation often produce invalid (over-weight) solutions, both algorithms use a shared **greedy repair function**:
1. **Drop phase:** Items with the worst value-to-weight ratio are dropped until the knapsack is under capacity.
2. **Add-back phase:** Unselected items with the best value-to-weight ratio are greedily added back if they fit.

---

## 🐛 The Reference Bug & Rotation Gate Sensitivity

During the validation of our QIEA implementation against a widely cited [Python port](https://github.com/mjBM/Quantum-Evolutionary-Algorithm-Knapsack-Python-) of Han & Kim's original MATLAB code, we discovered a **critical bug in the reference repository's rotation gate**.

The rotation gate dictates how probabilities are updated. The correct MATLAB formulation uses:
```matlab
% Correct MATLAB formulation
sign_factor = 2 * (sin(theta) * cos(theta) > 0) - 1
```
This evaluates to `{+1, -1}`, ensuring qubits are always rotated either towards or away from the target state.

However, the Python port mistakenly placed the multiplier inside the comparison:
```python
# Buggy Python port
sign_factor = (2 * sin(theta) * cos(theta) > 0) - 1
```
Because Booleans evaluate to `1` or `0`, this buggy formula yields `{0, -1}`. As a result, **no rotation occurs at all** when qubits are in the first quadrant (where they are all initialized). 

When we ran the buggy version, QIEA performed significantly worse than GA. After discovering and fixing this operator precedence bug to match the MATLAB original, the performance of QIEA shifted dramatically, perfectly matching GA. This highlights the extreme sensitivity of Quantum-Inspired algorithms to the specific mechanics of the rotation gate.

---

## 📊 Key Findings & Results

The experiment ran **30 independent trials** (different random seeds) for each algorithm at each instance size.

| Instance | Algorithm | Mean Fitness | Best Found | Worst Found | Gap to DP Optimal | Mann-Whitney p-value |
|----------|-----------|--------------|------------|-------------|-------------------|----------------------|
| **n=20** | GA | 827.0 | 827 | 827 | 0.00% | 0.334 (Not Sig.) |
| | QIEA | 826.9 | 827 | 825 | 0.01% | |
| **n=50** | GA | 1848.3 | 1849 | 1848 | 0.04% | 0.790 (Not Sig.) |
| | QIEA | 1848.3 | 1849 | 1848 | 0.04% | |
| **n=100**| GA | 3810.0 | 3810 | 3810 | 0.00% | 1.000 (Not Sig.) |
| | QIEA | 3810.0 | 3810 | 3810 | 0.00% | |

### Conclusions
1. **Statistical Parity:** There is no statistically significant difference in the final solution quality between QIEA and GA. Both achieve near-perfect optimality (< 0.05% gap).
2. **Population Efficiency:** QIEA achieves these results using **5× fewer individuals** (10 vs 50). The probabilistic nature of the Q-bit superposition provides massive implicit diversity, allowing a very small population to explore the search space as effectively as a large classical population.

---

## 🖼️ Understanding the Visualizations

### 1. Convergence Plots (`convergence_plots.png`)
These line charts show how the "best fitness found so far" evolves over the total number of fitness evaluations. 
- You will see QIEA and GA tracking each other nearly identically.
- The dashed green line represents the absolute DP optimal limit.

### 2. Final Fitness Boxplots (`boxplots.png`)
These plots show the distribution of the final fitness values found across all 30 independent trials. 
- A tight box indicates the algorithm consistently finds the exact same quality of solution every time it is run, regardless of the initial random seed.

### 3. Optimality Gap (`gap_chart.png`)
This bar chart shows the percentage difference between the algorithm's average result and the true mathematical optimum. Lower is better.

---

## 🚀 Running the Notebook

To re-run the experiments or tweak the parameters yourself:

```bash
# Ensure dependencies are installed
pip install numpy pandas matplotlib seaborn scipy jupyter

# Launch Jupyter
jupyter notebook QIEA_vs_GA_Knapsack.ipynb
```

**Note:** Depending on your machine, executing all 180 runs (30 trials × 3 sizes × 2 algorithms) takes about 45 to 60 seconds.

---

## 📚 References

1. **Han, K.-H., & Kim, J.-H. (2002).** *Quantum-Inspired Evolutionary Algorithm for a Class of Combinatorial Optimization.* IEEE Transactions on Evolutionary Computation, 6(6), 580-593. [DOI: 10.1109/TEVC.2002.804320]
2. **Reference Bug Discovery:** Validated against the implementation found at [mjBM/Quantum-Evolutionary-Algorithm-Knapsack-Python-](https://github.com/mjBM/Quantum-Evolutionary-Algorithm-Knapsack-Python-)
3. **Goldberg, D.E. (1989).** *Genetic Algorithms in Search, Optimization, and Machine Learning.* Addison-Wesley.
