# QIEA: Algorithm Implementations

This directory contains standalone, pure-Python implementations of the two optimization algorithms. These scripts demonstrate the core mechanics of each algorithm on a simple, intuitive 5-item 0/1 Knapsack problem (the "Movie Theatre Snacks" problem).

## 📁 Structure

- **[Classical/](Classical/)**
  Contains `classical_ga.py`, demonstrating a standard Genetic Algorithm using a binary representation, crossover, and mutation.

- **[Quantum_Inspired/](Quantum_Inspired/)**
  Contains `qiea.py`, demonstrating the Quantum-Inspired Evolutionary Algorithm using a Q-bit (probabilistic amplitude) representation and a rotation gate update mechanism.

## 🧠 Why Two Folders?

While both algorithms solve the exact same problem, their approaches to maintaining and exploring the search space are fundamentally different. 

- The **Classical** approach commits to hard 0s and 1s early, exploring via random mutation and crossover.
- The **Quantum-Inspired** approach keeps choices in a state of uncertainty (superposition) for as long as possible, nudging the underlying probabilities toward good solutions over time.

Read the `README.md` inside each subfolder for a detailed, beginner-friendly explanation of how the respective algorithm works!
