import sys

F = 10000 
nodes = [['.' for i in range(F * 2 + 1)] for j in range(F * 2 + 1)]

grid = list(sys.stdin)
top = F - len(grid) // 2
for r in range(len(grid)):
    for c in range(len(grid)):
        nodes[r + top][c + top] = grid[r][c]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
head = 0
sr = F
sc = F

infect = 0
for i in range(F):
    clean = nodes[sr][sc] == '.'
    head = (head + (1, -1)[clean]) % len(moves)
    nodes[sr][sc] = ('.', '#')[clean]
    if clean:
        infect += 1
    #print('\n'.join([''.join(x) for x in nodes]))
    #print('')

    sr += moves[head][0]
    sc += moves[head][1]
print(infect)


