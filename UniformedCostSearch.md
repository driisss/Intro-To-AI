Uniform Cost Search (UCS)
�It is a type of uninformed searching algorithm
• Uniform Cost Search is an uninformed search algorithm that finds the least-cost path from a start node to a
goal node.
It expands nodes based on the cumulative path cost g(n) — the cost from the start node to the current node.
� Key Characteristics:
• Type: Uninformed (Blind) Search
• Strategy: Lowest path cost first (g(n))
• Optimal: ✅ Yes (if all costs ≥ 0) : it means it finds the best solution among all possible solutions
• Complete: ✅ Yes (if goal is reachable): it means it can find the solution if there exist a path to reach solution
• Heuristic used: ❌ No (does not use h(n))
• Data Structure: Priority Queue (min-heap by cost)
