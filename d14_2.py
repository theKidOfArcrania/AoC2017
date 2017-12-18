from functools import reduce

def hash(data):
    size = 256
    def m(x):
        return x % size

    line = list(range(size))

    pos = 0
    skip = 0
    data = list(map(ord, data)) + [17,31,73,47,23]

    for r in range(64):
        for l in data:
            for off in range(l // 2):
                a = m(off + pos)
                b = m((l - off - 1) + pos)
                tmp = line[a]
                line[a] = line[b]
                line[b] = tmp
            pos = m(pos + skip + l) 
            skip += 1

    xor = [reduce(lambda x,y: x^y, line[r*16:(r+1)*16]) for r in range(16)]
    return xor

def hamming(h):
    return sum([bin(x).count('1') for x in h])

bitmap = [[False for i in range(128)] for j in range(128)]
visited = [[False for i in range(128)] for j in range(128)]

used = 0
start = input()
for i in range(128):
    h = hash(start + '-' + str(i))
    for x in range(len(h)):
        for xx in range(8):
            bitmap[i][x * 8 + xx] = ((h[x] >> (7 - xx)) & 1) == 1

def dfs(x, y):
    if x < 0 or x >= 128 or y < 0 or y >= 128:
        return
    if visited[x][y]:
        return
    if not bitmap[x][y]:
        return
    visited[x][y] = True
    dfs(x+1, y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
lands = 0
for xx in range(128):
    for yy in range(128):
        if not visited[xx][yy] and bitmap[xx][yy]:
            lands += 1
            dfs(xx, yy)

print(lands)
