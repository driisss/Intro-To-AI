Greedy Best First Search (GBFS)
It is a type of informed searching algorithm
Greedy Best-First Search is an informed search algorithm that expands the node which appears to be
closest to the goal, using a heuristic function h(n) (estimated cost from current node to goal).
� Key Characteristics:
• Type: Informed (Heuristic) Search
• Strategy: Select node with lowest heuristic value h(n)
• Optimal: ❌ No: It means the solution it find might not be the best possible solution
• Complete: ✅ Yes (in finite spaces with no cycles)
• Heuristic used: ✅ Yes
• Data Structure: Priority Queue (min-heap by h(n))