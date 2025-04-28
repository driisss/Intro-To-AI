goal = [[1,2,3],[4,5,6],[7,8,0]]
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota          Dristi Sapkota
def find_zero(p):
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:
                return i, j
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota          Dristi Sapkota
def move(p):
    x, y = find_zero(p)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    next_states = []
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_p = [row[:] for row in p]
            new_p[x][y], new_p[nx][ny] = new_p[nx][ny], new_p[x][y]
            next_states.append(new_p)
    return next_states
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota          Dristi Sapkota         
def dfs(p, visited):
    if p == goal:
        return [p]
    visited.add(str(p))
    for nxt in move(p):
        if str(nxt) not in visited:
            path = dfs(nxt, visited)
            if path:
                return [p] + path
    return None
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota          Dristi Sapkota
start = [[1,2,3],[4,0,6],[7,5,8]]
visited = set()
result = dfs(start, visited)

if result:
    for step in result:
        for row in step:
            print(row)
        print()
else:
    print("No solution.")
#Dristi Sapkota         Dristi Sapkota          Dristi Sapkota          Dristi Sapkota          Dristi Sapkota