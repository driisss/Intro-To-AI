#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota
import heapq

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

def a_star(start, goal):
    heap = [(hamming(start, goal), 0, start, [start])]
    visited = set()
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota
    while heap:
        _, g, curr, path = heapq.heappop(heap)
        if curr == goal:
            return path
        if curr in visited:
            continue
        visited.add(curr)
        for i in range(len(curr)):
            flipped = curr[:i] + ('1' if curr[i] == '0' else '0') + curr[i+1:]
            if flipped not in visited:
                heapq.heappush(heap, (g + 1 + hamming(flipped, goal), g + 1, flipped, path + [flipped]))
    return None
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota

start = "10110101"
goal = "01100011"
result = a_star(start, goal)

if result:
    print("Steps:", len(result) - 1)
    for r in result: print(r)
else:
    print("No solution.")
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota