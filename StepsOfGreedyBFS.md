Steps of GBFS algorithm
1.Initialize a priority queue with the start node.
2.Use h(n) to prioritize nodes — lower h(n) = higher priority.
3.Repeat until the queue is empty:
◦Remove the node with the lowest h(n).
◦If it’s the goal node, return the path.
◦Otherwise, expand the node and:
▪Add its unvisited children to the queue with their h(n) values.
4.If the queue is empty and the goal hasn’t been found, return failure.