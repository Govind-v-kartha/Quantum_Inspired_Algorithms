import numpy as np

# ── PROBLEM DEFINITION ──────────────────────────────
# Same movie theatre snack problem as Classical GA
weights = [150, 100, 200, 80, 250]
values  = [8,   6,   9,   5,  10]
budget  = 500
n_items = len(weights)
names   = ["Popcorn", "ColdDrink", "Nachos", "Chocolate", "Sandwich"]

# ── QIEA SETTINGS ───────────────────────────────────
n_individuals = 10
n_generations = 100
delta_theta   = 0.05 * np.pi    # rotation angle

# ── QUBIT INITIALIZATION ────────────────────────────
# Each individual is a vector of angles θ, where:
#   α = cos(θ),  β = sin(θ)
#   P(0) = α² = cos²(θ),  P(1) = β² = sin²(θ)
# Start at θ = π/4 → α = β = 1/√2 → 50/50 superposition
Q = np.full((n_individuals, n_items), np.pi / 4)

# ── FITNESS ─────────────────────────────────────────
def fitness(solution):
    total_weight = np.dot(solution, weights)
    total_value  = np.dot(solution, values)
    return total_value if total_weight <= budget else 0

# ── OBSERVE (MEASUREMENT) ───────────────────────────
def observe(q_individual):
    """Collapse qubit probabilities to a binary solution.
    P(1) = sin²(θ) — roll dice for each item."""
    probs = np.sin(q_individual) ** 2
    return (np.random.random(n_items) < probs).astype(int)

# ── ROTATION GATE UPDATE ────────────────────────────
def update_qubits(q_individual, observed, best_solution, obs_fit, best_fit):
    """Rotate each qubit toward the better solution.

    Uses the Han & Kim (2002) rotation gate:
      sign = [2·(sin(θ)·cos(θ) > 0) - 1] × (2·target - 1)
      θ_new = θ + sign × Δθ

    If this observation improved on personal best → rotate toward observed.
    Otherwise → rotate toward best known solution.
    """
    if obs_fit > best_fit:
        target = observed
    else:
        target = best_solution

    alpha = np.cos(q_individual)
    beta  = np.sin(q_individual)
    ab    = alpha * beta

    # Correct Han & Kim formula: 2*(condition) - 1 gives {+1, -1}
    sign_factor   = 2.0 * (ab > 0).astype(float) - 1.0
    target_factor = 2.0 * target.astype(float) - 1.0

    rotation = sign_factor * target_factor * delta_theta
    q_individual += rotation

    return q_individual

# ── MAIN LOOP ───────────────────────────────────────
best_solution = np.zeros(n_items, dtype=int)
best_fitness  = 0
personal_best_sol = [np.zeros(n_items, dtype=int) for _ in range(n_individuals)]
personal_best_fit = [0] * n_individuals
top3 = []

print("Starting Quantum-Inspired EA...\n")

for generation in range(n_generations):

    for i in range(n_individuals):
        # STEP 1: Observe — collapse qubits to binary
        observed = observe(Q[i])

        # STEP 2: Evaluate fitness
        fit = fitness(observed)

        # STEP 3: Update qubits via rotation gate
        Q[i] = update_qubits(Q[i], observed,
                             personal_best_sol[i], fit, personal_best_fit[i])

        # STEP 4: Update personal best
        if fit > personal_best_fit[i]:
            personal_best_fit[i] = fit
            personal_best_sol[i] = observed.copy()

        # STEP 5: Update global best
        if fit > best_fitness:
            best_fitness  = fit
            best_solution = observed.copy()

        # Track top 3 diverse solutions
        if fit > 0:
            candidate = (observed.copy(), fit)
            if all(np.sum(observed != s) >= 2 for s, f in top3):
                top3.append(candidate)
                top3 = sorted(top3, key=lambda x: x[1], reverse=True)[:3]

    # Print progress — show probabilities evolving
    if (generation + 1) % 10 == 0:
        probs = np.sin(Q[0]) ** 2   # show first individual's P(1) values
        prob_str = ", ".join(f"{p:.2f}" for p in probs)
        print(f"Generation {generation+1:3d} | "
              f"Best fitness: {best_fitness} | "
              f"Probs: [{prob_str}]")

# ── RESULTS ─────────────────────────────────────────
print("\n========== TOP 3 RESULTS ==========")
medals = ["🥇", "🥈", "🥉"]

for rank, (sol, fit) in enumerate(top3):
    chosen = [names[i] for i in range(n_items) if sol[i] == 1]
    spent  = int(np.dot(sol, weights))
    print(f"{medals[rank]} Option {rank+1} → "
          f"{', '.join(chosen):40s} | "
          f"₹{spent} | Happiness: {fit}")

print(f"\nBest answer → happiness {best_fitness} "
      f"within ₹{budget} budget")
