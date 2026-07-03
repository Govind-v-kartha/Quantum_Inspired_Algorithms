# Classical Genetic Algorithm

## 2.1 What is a Genetic Algorithm?
Remember our cheetah story? Thousands of years ago cheetahs weren't as fast as they are today. Some were born slightly faster by random chance. Slow ones couldn't catch food and died. Fast ones survived, had babies, passed their speed genes forward. After thousands of generations — cheetahs became the fastest land animal on earth. Nobody planned it. It just happened through random variation, selection, and inheritance.

Genetic Algorithm does the exact same thing — but instead of cheetahs, we have solutions to a problem. Bad solutions die. Good solutions survive and produce better children. Over many generations the population gets smarter until we find a great answer.

## 2.2 Why Genetic Algorithm?
Because brute force is impossible in real life.
For our 5 snack problem we had 2⁵ = 32 possible combinations — small enough to check manually. But scale that up to 100 items and you have 2¹⁰⁰ combinations — more than atoms in the universe. You simply cannot check them all.

GA doesn't check everything. It learns from good solutions and builds better ones — like a student who learns from mistakes each exam instead of memorising every possible question. Smart guessing beats exhaustive searching every time.

## 2.3 Understanding the Snack Example
We walked into a movie theatre with ₹500 in our pocket. Five snacks available — each with a price and a happiness score. Goal was simple: maximum happiness without crossing ₹500.

This is the classic Knapsack Problem — the exact same problem researchers worldwide use to benchmark and compare optimization algorithms. By solving it with both GA and QIEA, we are doing exactly what papers do — implementing and comparing on a standard benchmark.

## 2.4 Binary Representation
Every solution in GA is written as a string of 0s and 1s:
```
[Popcorn, ColdDrink, Nachos, Chocolate, Sandwich]
[  1    ,     0    ,   1   ,     0    ,    1    ]
```
→ buy Popcorn, Nachos, Sandwich
→ skip ColdDrink, Chocolate

1 = buy, 0 = don't buy. This binary encoding is what makes the whole algorithm possible — you can't mix and flip words, but you can mix and flip bits cleanly. Every solution, no matter how complex, becomes a simple row of 0s and 1s.

## 2.5 Fitness Function
This is the scoring system — the judge that tells the algorithm how good each solution is:
- if total price <= ₹500 → fitness = total happiness   ✅
- if total price >  ₹500 → fitness = 0  (invalid)      ❌

Think of it like a teacher grading exam papers. Every solution gets a score. Higher score = better solution = more likely to survive. Without a fitness function the algorithm has no direction — it wouldn't know what "better" even means.

## 2.6 Population Initialization
Before evolution begins, we need a starting population — a random first batch of solutions:
- Solution 1  → `[1, 0, 1, 0, 0]`  → ₹350, 😊17
- Solution 2  → `[0, 1, 0, 1, 1]`  → ₹430, 😊21
- Solution 3  → `[1, 1, 1, 0, 0]`  → ₹450, 😊23
- ...
- Solution 10 → `[1, 0, 0, 1, 1]`  → ₹480, 😊23

All completely random — nobody is good yet. This is Generation 1. Just like the first batch of cheetahs — some fast, some slow, all starting from scratch.

## 2.7 Selection
After scoring every solution, we keep the best ones and discard the weak ones:
- Solution 3  → 😊23  ← SURVIVES 🏆
- Solution 10 → 😊23  ← SURVIVES 🏆
- Solution 2  → 😊21  ← SURVIVES
- Solution 1  → 😊17  ← dies ❌
- ...

Only the top 50% survive and get to reproduce. Exactly like nature — stronger individuals pass their genes forward, weaker ones don't. This is where "survival of the fittest" happens in the code.

## 2.8 Crossover
Now the surviving solutions mix together to produce children — like parents passing traits to their babies:
```
Parent 1 → [1, 0, 1, | 0, 0]
Parent 2 → [0, 1, 0, | 1, 1]
                     ↕
Cut at position 3 and swap:

Child 1  → [1, 0, 1,   1, 1]  ← left of P1 + right of P2
Child 2  → [0, 1, 0,   0, 0]  ← left of P2 + right of P1
```
The cut point is chosen randomly each time. Sometimes children are better than both parents — sometimes worse. That randomness is what keeps the search alive and exploring new territory.

## 2.9 Mutation
After crossover, occasionally one gene randomly flips — like a copying error in DNA:
```
Before mutation → [1, 0, 1, 1, 1]  → ₹700 ❌ over budget
                           ↕
Random flip at position 4:
After mutation  → [1, 0, 1, 1, 0]  → ₹450 ✅ valid!
```
Mutation rate is kept small — typically 10% — so it doesn't destroy good solutions but still introduces enough variety to escape local optima. Too much mutation = pure randomness. Too little = gets stuck. Balance is key.

## 2.10 Building the Classical Genetic Algorithm
We built it in clean blocks, each doing one job:
- Block 1 → Problem definition    (snacks, prices, budget)
- Block 2 → GA settings           (population size, generations, mutation rate)
- Block 3 → Fitness function      (score each solution)
- Block 4 → Crossover function    (mix two parents)
- Block 5 → Mutation function     (random flip)
- Block 6 → Main loop             (evolve for 100 generations)
- Block 7 → Results               (print top 3 diverse solutions)

Each block independent and readable — exactly how professional research code should be structured.

## 2.11 Running the Program
When we ran the code, each generation printed its best fitness score. We watched the score climb from random low values toward the optimal answer — exactly like watching cheetahs get faster over generations:
```
Generation  10 | Best fitness: 19
Generation  20 | Best fitness: 21
Generation  30 | Best fitness: 23
Generation  50 | Best fitness: 24
...
🥇 Option 1 → Popcorn, ColdDrink, Sandwich | ₹500 | Happiness: 24
```

## 2.12 Summary
Genetic Algorithm in one picture:

1. Random population
2. Evaluate fitness (score everyone)
3. Selection (keep the best)
4. Crossover (mix survivors)
5. Mutation (random small change)
6. Repeat → Repeat → Repeat
7. Best solution found 🏆

Classical GA works well. But it has one weakness — solutions are hard 0s and 1s from the start. It commits too early and can miss better answers by getting stuck. That's exactly the problem QIEA was designed to fix.
