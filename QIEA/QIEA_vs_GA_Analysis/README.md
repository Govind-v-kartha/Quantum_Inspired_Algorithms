# 🔬 Knapsack Benchmarks: QIEA vs GA

This folder contains a comprehensive, statistical benchmark comparing the Quantum-Inspired Evolutionary Algorithm (QIEA) with the Classical Genetic Algorithm (GA) on larger instances of the 0/1 Knapsack Problem.

## 📓 The Notebook
The main file is `QIEA_vs_GA_Knapsack.ipynb`. It is a self-contained Jupyter notebook that provides:
1. **Implementation from scratch** of both QIEA and GA.
2. **Dynamic Programming (DP) solver** to calculate the absolute ground-truth optimal solutions for the generated knapsack problems.
3. **Rigorous experiment harness** that runs both algorithms over multiple independent trials to collect statistically valid results.
4. **Data analysis and visualization** of the results, including convergence plots, boxplots of fitness distributions, and gap-to-optimal charts.

## 📊 What We Implemented & Tested

We scaled up the knapsack problem from a simple 5-item "movie snacks" problem to 20, 50, and 100-item synthetic instances. We evaluated both algorithms giving them the **same fitness evaluation budget** (to ensure a fair comparison of computational effort).

- **Instance Sizes:** n=20, n=50, n=100 items
- **GA Configuration:** Population of 50, tournament selection, 2-point crossover, bit-flip mutation.
- **QIEA Configuration:** Population of 10, Q-bit representation, Han & Kim rotation gate update, local/global migration, H-gate clamping.
- **Experiment Scale:** 30 independent trials per algorithm, per instance.

### Repair Mechanism
Both algorithms use a shared **greedy repair function** to handle invalid solutions (over-budget). If a solution exceeds the knapsack capacity, items with the worst value-to-weight ratio are dropped, and then items that fit are greedily added back. This ensures all evaluated solutions are valid and comparable.

## 📈 Key Findings

As detailed in the notebook's Discussion section, after validating our QIEA implementation against the published reference code (Han & Kim, 2002):

- **Both algorithms achieve excellent results**, finding solutions within 0.05% of the true DP-optimal across all instance sizes.
- **Statistical Parity:** With our corrected rotation gate implementation, QIEA matches GA's solution quality perfectly, showing no statistically significant difference in final fitness outcomes (Mann-Whitney U tests yielded p-values > 0.3 across all instances).
- **Efficiency:** QIEA achieves these results using **5× fewer individuals** (10 vs 50) by leveraging the implicit diversity of the Q-bit superposition state, demonstrating the power of quantum-inspired representations to explore effectively with small populations.

## 🖼️ Included Visualizations
- `convergence_plots.png`: Shows how quickly the algorithms hone in on the optimal solution over the course of the fitness evaluations.
- `boxplots.png`: Displays the variance and consistency of the final fitness values found across the 30 trials.
- `gap_chart.png`: A bar chart visualizing how close each algorithm gets to the 100% optimal DP solution.
