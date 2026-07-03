import numpy as np

# ── PROBLEM DEFINITION ──────────────────────────────
weights = [150, 100, 200, 80, 250]
values  = [8,   6,   9,   5,  10]
budget  = 500
n_items = len(weights)

# ── GA SETTINGS ─────────────────────────────────────
pop_size      = 10
n_generations = 100
mutation_rate = 0.1

# ── FITNESS ─────────────────────────────────────────
def fitness(solution):
    total_weight = np.dot(solution, weights)
    total_value  = np.dot(solution, values)
    return total_value if total_weight <= budget else 0

# ── CROSSOVER ───────────────────────────────────────
def crossover(parent1, parent2):
    point = np.random.randint(1, n_items)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return child1, child2

# ── MUTATION ────────────────────────────────────────
def mutate(solution):
    for i in range(n_items):
        if np.random.random() < mutation_rate:
            solution[i] = 1 - solution[i]
    return solution

# ── MAIN LOOP ───────────────────────────────────────
# create random population
population = np.random.randint(0, 2, (pop_size, n_items))

best_solution = None
best_fitness  = 0
top3          = []

print("Starting Classical GA...\n")

for generation in range(n_generations):

    # evaluate all
    scores = [fitness(ind) for ind in population]

    # track best
    for i, score in enumerate(scores):
        if score > best_fitness:
            best_fitness  = score
            best_solution = population[i].copy()

        # update top3
        if score > 0:
            candidate = (population[i].copy(), score)
            if all(np.sum(population[i] != s) >= 2
                   for s, f in top3):
                top3.append(candidate)
                top3 = sorted(top3,
                       key=lambda x: x[1],
                       reverse=True)[:3]

    # selection → top half survives
    sorted_idx  = np.argsort(scores)[::-1]
    survivors   = [population[i] for i in sorted_idx[:pop_size//2]]

    # crossover → fill population back up
    new_pop = list(survivors)
    while len(new_pop) < pop_size:
        p1, p2 = survivors[np.random.randint(len(survivors))], \
                 survivors[np.random.randint(len(survivors))]
        c1, c2 = crossover(p1, p2)
        new_pop.extend([mutate(c1), mutate(c2)])

    population = np.array(new_pop[:pop_size])

    if (generation + 1) % 10 == 0:
        print(f"Generation {generation+1:3d} | "
              f"Best fitness: {best_fitness}")

# ── RESULTS ─────────────────────────────────────────
print("\n========== TOP 3 RESULTS ==========")
names  = ["Popcorn", "ColdDrink", "Nachos", "Chocolate", "Sandwich"]
medals = ["🥇", "🥈", "🥉"]

for rank, (sol, fit) in enumerate(top3):
    chosen = [names[i] for i in range(n_items) if sol[i] == 1]
    spent  = int(np.dot(sol, weights))
    print(f"{medals[rank]} Option {rank+1} → "
          f"{', '.join(chosen):40s} | "
          f"₹{spent} | Happiness: {fit}")

print(f"\nBest answer → happiness {top3[0][1]} "
      f"within ₹{budget} budget")