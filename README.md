# 🧬 Quantum-Inspired Algorithms

> **Benchmarking Quantum-Inspired Evolutionary Algorithm (QIEA) vs Classical Genetic Algorithm (GA) on the 0/1 Knapsack Problem**

This repository implements and compares two metaheuristic optimization approaches — a **Classical Genetic Algorithm** and a **Quantum-Inspired Evolutionary Algorithm** — on the classic Knapsack Problem. We start with an intuitive 5-snack example and scale up to a rigorous statistical comparison on larger instances.

---

## 📁 Repository Structure

```
Quantum_Inspired_Algorithms/
│
├── README.md                          ← You are here
│
├── QIEA/                             ← Algorithm implementations
│   ├── README.md                     ← Overview of both approaches
│   ├── Classical/                    ← Classical Genetic Algorithm
│   │   ├── README.md                 ← Detailed GA explanation
│   │   └── classical_ga.py           ← Standalone GA code
│   └── Quantum_Inspired/            ← Quantum-Inspired EA
│       ├── README.md                 ← Detailed QIEA explanation
│       └── qiea.py                   ← Standalone QIEA code
│   └── QIEA_vs_GA_Analysis/         ← Combined comparison
│       ├── README.md                ← What the notebook implements
│       ├── QIEA_vs_GA_Knapsack.ipynb← Full benchmark notebook
│       ├── convergence_plots.png    ← Convergence curves
│       ├── boxplots.png             ← Final fitness distributions
│       └── gap_chart.png            ← Optimality gap comparison
```

---

## 🎯 The Problem: 0/1 Knapsack

You walk into a movie theatre with **₹500**. Five snacks are available:

| Snack | Price (₹) | Happiness |
|-------|-----------|-----------|
| 🍿 Popcorn | 150 | 8 |
| 🥤 ColdDrink | 100 | 6 |
| 🧀 Nachos | 200 | 9 |
| 🍫 Chocolate | 80 | 5 |
| 🥪 Sandwich | 250 | 10 |

**Goal:** Maximize happiness without exceeding ₹500.

This is the **0/1 Knapsack Problem** — a classic benchmark used worldwide to compare optimization algorithms. Each item is either taken (1) or left (0). For 5 items there are only 2⁵ = 32 combinations. But scale to 100 items and you have 2¹⁰⁰ — more than atoms in the universe. That's why we need smart algorithms.

---

## 🔬 The Two Approaches

### Classical Genetic Algorithm (GA)
Inspired by natural evolution — survival of the fittest. Solutions are binary strings of 0s and 1s. Good solutions survive, bad ones die. Survivors mix (crossover) and occasionally mutate. Over generations, the population gets smarter.

**Limitation:** Solutions are hard 0s and 1s from the start. The algorithm commits early and can get stuck.

→ [Read the full explanation](QIEA/Classical/README.md)

### Quantum-Inspired Evolutionary Algorithm (QIEA)
Borrows the concept of **superposition** from quantum mechanics. Instead of committing to 0 or 1, each gene stays in a probabilistic state — "60% yes, 40% no" — and gradually converges as the algorithm learns. More exploration = better answers.

**Advantage:** Stays uncertain longer, explores more of the solution space, and matches GA's quality with 5× fewer individuals.

→ [Read the full explanation](QIEA/Quantum_Inspired/README.md)

---

## 📊 Key Results (from the Notebook)

Both algorithms were benchmarked rigorously — same instances, same fitness budget, 30 independent trials, statistical significance testing:

| Instance | GA Mean | QIEA Mean | GA Gap | QIEA Gap | p-value |
|----------|---------|-----------|--------|----------|---------|
| n=20 | 827.0 | 826.9 | 0.00% | 0.01% | 0.334 (n.s.) |
| n=50 | 1848.3 | 1848.3 | 0.04% | 0.04% | 0.790 (n.s.) |
| n=100 | 3810.0 | 3810.0 | 0.00% | 0.00% | 1.000 (n.s.) |

**No statistically significant difference** — QIEA matches GA's solution quality using only 10 individuals vs GA's 50.

→ [See full analysis in the Notebook](QIEA/QIEA_vs_GA_Analysis/README.md)

---


## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/Govind-v-kartha/Quantum_Inspired_Algorithms.git
cd Quantum_Inspired_Algorithms

# Run Classical GA
python QIEA/Classical/classical_ga.py

# Run QIEA
python QIEA/Quantum_Inspired/qiea.py

# Open the full comparison notebook
jupyter notebook QIEA/QIEA_vs_GA_Analysis/QIEA_vs_GA_Knapsack.ipynb
```

### Requirements
- Python 3.10+
- NumPy, Matplotlib, Pandas, SciPy, Seaborn, tqdm

```bash
pip install numpy matplotlib pandas scipy seaborn tqdm jupyter
```

---

## 📚 References

1. **Han, K.-H., & Kim, J.-H. (2002).** *Quantum-Inspired Evolutionary Algorithm for a Class of Combinatorial Optimization.* IEEE Trans. Evol. Comput., 6(6), 580-593.
2. **Goldberg, D.E. (1989).** *Genetic Algorithms in Search, Optimization, and Machine Learning.* Addison-Wesley.
3. **Reference implementation:** [mjBM/Quantum-Evolutionary-Algorithm-Knapsack-Python-](https://github.com/mjBM/Quantum-Evolutionary-Algorithm-Knapsack-Python-)

---

## 👤 Author

**Govind V Kartha**

---
