DFS Algorithm:
1.Initialize an empty stack S
2.Initialize an empty set Visited
3.Push start onto S
4.Add start to Visited
5.While S is not empty, do:
1.Pop a node current from S
2.Process current (e.g., print or store it)
3.For each neighbor n of current in G (in reverse order if needed for consistent
ordering):
▪If n is not in Visited:
▪Push n onto S
▪Add n to Visited