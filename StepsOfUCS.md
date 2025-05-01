Steps of UCS Algorithm
1.Initialize a priority queue (open list) with the start node at cost 0.
2.Repeat until the queue is empty:
◦Remove the node with the lowest cumulative cost.
◦If it’s the goal node, terminate and return the path.
◦Otherwise, expand the node and:
▪For each child, calculate the new path cost.
▪Add it to the queue if not visited or found with lower cost.
▪Update the cost if a cheaper path is found.
3.If the goal is not found and the queue is empty, return failure.