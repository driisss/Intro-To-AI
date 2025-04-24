Depth First Search (uninformed)
• Always expands the deepest node
in the current fringe of the search
tree
• The search proceeds immediately
to the deepest level of the search
tree, where the nodes have no
successors (dead end)
• When a dead end is reached, the
search backup to the next
shallowest node that still has
unexplored successors
• This strategy can be implemented
by tree search with a last-in-firstout (LIFO), known as
stack.
Note by: Er. Suman
• Note: We can also use BFS and DFS in graph. (Like path finding
between cities. But this path might not be the shortest one)
Note: we need to make a set / list of already visited nodes, in order to
Prevent it from visiting same node again and again (avoiding cycle)