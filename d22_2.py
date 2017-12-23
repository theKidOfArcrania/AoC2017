import sys

F = 10000
nodes = [['.' for i in range(F * 2 + 1)] for j in range(F * 2 + 1)]

grid = list(sys.stdin)
top = F - len(grid) // 2
for r in range(len(grid)):
    for c in range(len(grid)):
        nodes[r + top][c + top] = grid[r][c]

moving = {'.': -1, 'W': 0, '#': 1, 'F': -2}
statusChg = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
head = 0
sr = F
sc = F

print('GO!')
infect = 0
for i in range(10000000):
    head = (head + moving[nodes[sr][sc]]) % len(moves)
    nodes[sr][sc] = statusChg[nodes[sr][sc]]
    if nodes[sr][sc] == '#':
        infect += 1
    #print('\n'.join([''.join(x) for x in nodes]))
    #print('')

    sr += moves[head][0]
    sc += moves[head][1]
print(infect)


