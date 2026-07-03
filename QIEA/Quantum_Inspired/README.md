# Quantum-Inspired Evolutionary Algorithm

## 3.1 Why Quantum-Inspired Evolutionary Algorithm?
Classical GA commits too early. Once a solution is `[1, 0, 1, 0, 1]` — it's fixed. No flexibility, no uncertainty. This causes premature convergence — the algorithm thinks it found the best answer but actually got stuck in a locally good but globally bad solution.

QIEA fixes this by borrowing one powerful idea from quantum mechanics — uncertainty. Instead of committing to 0 or 1 immediately, each gene stays uncertain for as long as needed, exploring more of the solution space before deciding. More exploration = better final answers.

## 3.2 From Bits to Q-bits
In Classical GA each gene is a hard bit:
- **Bit** → either 0 or 1. Decided. Fixed. No flexibility.

In QIEA each gene is a qubit — a pair of probability amplitudes (α, β):
- **Qubit** → `[α, β]` where `α² + β² = 1`
- `α²` = probability of being 0
- `β²` = probability of being 1

Start → `α = β = 1/√2 = 0.707`
→ `α² = 0.5 = 50% chance of 0`
→ `β² = 0.5 = 50% chance of 1`
→ perfectly uncertain at the start

Think of it like your friend asking "coming to the trip?" and instead of yes or no immediately — you say "I'm 60% yes, 40% no, let me see." You haven't committed yet. That flexibility is the whole point.

## 3.3 Superposition
This uncertain state — where a qubit is neither fully 0 nor fully 1 — is called superposition. You've seen this in Qiskit:
`|+⟩ = 1/√2 (|0⟩ + |1⟩)`  ← equal superposition, 50/50

QIEA starts every gene in equal superposition:
`Generation 1 → [0.50, 0.50, 0.50, 0.50, 0.50]`
→ completely uncertain about every item
→ maximum exploration possible

Over generations, superposition gradually collapses as the algorithm learns which choices are better — just like measuring a qubit collapses it to 0 or 1.

## 3.4 Observation (Measurement)
Since probabilities aren't actual solutions, QIEA needs to measure them to get a testable 0/1 string — exactly like measuring a qubit in Qiskit:

Current probabilities → `[0.65, 0.40, 0.75, 0.30, 0.70]`

Roll dice for each item:
- Popcorn    → 65% chance of 1 → dice → 1 ✅
- ColdDrink  → 40% chance of 1 → dice → 0 ❌
- Nachos     → 75% chance of 1 → dice → 1 ✅
- Chocolate  → 30% chance of 1 → dice → 0 ❌
- Sandwich   → 70% chance of 1 → dice → 1 ✅

Observed solution → `[1, 0, 1, 0, 1]` → test this!

The randomness here is intentional — it allows exploration even at late stages. A 49% probability can still produce a 1 occasionally, which is how the algorithm escapes local optima.

## 3.5 Rotation Gate
This is the heart of QIEA — the update mechanism that nudges probabilities toward better solutions each generation:
```
[ α_new ]   =   [ cos(Δθ)   -sin(Δθ) ]   ×   [ α_old ]
[ β_new ]       [ sin(Δθ)    cos(Δθ) ]       [ β_old ]
```
Why a matrix and not just addition? Because `α² + β²` must always equal 1 — the rotation matrix guarantees this automatically. Adding directly would break this rule.

Direction of rotation is decided by comparing current solution to best solution:
- Best says 1, current going toward 0 → rotate + (push toward 1)
- Best says 0, current going toward 1 → rotate - (push toward 0)
- Both already agree                   → no rotation needed

Small nudge every generation. After 50 generations of nudges — fully converged.

## 3.6 Building the Quantum-Inspired Evolutionary Algorithm
We built it block by block, just like GA:
- Block 1 → Problem definition     (same snack problem)
- Block 2 → QIEA settings          (individuals, generations, theta)
- Block 3 → Qubit initialization   (all start at 1/√2)
- Block 4 → Fitness function       (identical to GA)
- Block 5 → Observe function       (roll dice using β²)
- Block 6 → Rotation gate update   (nudge toward best)
- Block 7 → Top 3 diverse results  (your idea! 🏆)
- Block 8 → Main loop              (evolve for 100 generations)

## 3.7 Running the Program
We watched the probabilities evolve live — something GA can't show because its solutions are always hard 0s and 1s:
```
Generation 10 | Probs: [1.  0.98  0.02  0.  1. ]  ← almost decided
Generation 20 | Probs: [1.  1.    0.    0.  1. ]  ← fully converged

========== TOP 3 RESULTS ==========
🥇 Option 1 → Popcorn, ColdDrink, Sandwich  | ₹500 | Happiness: 24
🥈 Option 2 → Popcorn, Nachos, Chocolate    | ₹430 | Happiness: 22
🥉 Option 3 → Nachos, Sandwich              | ₹450 | Happiness: 19
```
Key observation — QIEA converged by generation 10. GA typically needs more generations to reach the same quality answer because it commits too early and sometimes needs to recover from bad decisions.

## 3.8 Summary
QIEA in one picture:

1. All qubits at 50/50 superposition
2. Observe → roll dice → get 0/1 solution
3. Evaluate fitness
4. Update qubits via rotation gate (nudge toward best solution found)
5. Repeat → Repeat → Repeat
6. Probabilities converge to 0 or 1
7. Best solution found 🏆
8. Top 3 diverse options shown to user

The key difference from GA — QIEA stays uncertain longer, explores more, and finds better answers with fewer wasted generations. That's the entire reason quantum-inspired algorithms exist.
