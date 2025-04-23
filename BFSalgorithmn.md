BFS Algorithm:
1.Initialize an empty queue Q
2.Initialize an empty set Visited
3.Enqueue start into Q
4.Add start to Visited
5.While Q is not empty, do:
1.Dequeue a node current from Q
2.Process current (e.g., print or store it)
3.For each neighbor n of current in G:
▪If n is not in Visited:
▪ Enqueue n into Q
▪ Add n to Visited