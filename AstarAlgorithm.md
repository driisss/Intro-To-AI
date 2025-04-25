A star (A*) Algorithm
•Purpose: Finds the shortest path from a start node to a goal node using both actual and
estimated costs.
•Core Formula:
f(n) = g(n) + h(n)
◦g(n): Actual Cost from start to current node
◦h(n): Estimated cost from current node to goal (heuristic)
◦f(n): Total estimated cost of the path through node n