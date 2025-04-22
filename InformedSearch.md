Informed Search (Heuristic Search)
 Definition:
• Informed search algorithms use problem-specific knowledge (heuristics) to guess which path
is more likely to lead to the goal. They try to be "smart" about which paths to explore first.
 Examples:
• Greedy Best-First Search – picks the path that seems closest to the goal.
• A* Search – considers both the cost so far and an estimate to the goal:
f(n) = g(n) + h(n)
where:
g(n) = cost so far
h(n) = heuristic estimate to goal