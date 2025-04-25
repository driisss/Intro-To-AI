A* Search Algorithm (Step-by-Step)
1.Initialize:
◦Place the start node in the open list (nodes to be evaluated).
◦Set the g(start) = 0 and f(start) = h(start).
2.Repeat until the open list is empty:
a. Select the node n from the open list with the lowest f(n) = g(n) + h(n).
b. If n is the goal node, reconstruct and return the path.
c. Move n from the open list to the closed list (nodes already evaluated).
d. For each neighbor of n:
◦Calculate tentative g(neighbor) = g(n) + cost(n, neighbor).
◦If the neighbor is in the closed list and the new g is higher, skip it.
◦If the neighbor is not in the open list or the new g is lower:
▪Set came_from[neighbor] = n.
▪Set g(neighbor) = tentative g.
▪Set f(neighbor) = g(neighbor) + h(neighbor).
▪If the neighbor is not in the open list, add it.
3.If the open list is empty, return failure (no path found).