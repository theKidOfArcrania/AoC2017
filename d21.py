import os, sys

def find(bl):
    for rfl in range(2):
        for rot in range(4):
            xx = '/'.join([''.join(x) for x in bl])
            if xx in mappings:
                return mappings[xx]
            
            top = bl[0][::]
            for i in range(len(bl) - 1):
                bl[0][i] = bl[len(bl) - 1 - i][0]
                bl[len(bl) - 1 - i][0] = bl[len(bl) - 1][len(bl) - 1 - i]
                bl[len(bl) - 1][len(bl) - 1 - i] = bl[i][len(bl) - 1]
                bl[i][len(bl) - 1] = top[i]
        top = bl[0][::]
        for i in range(len(bl)):
            bl[0][i] = bl[len(bl) - 1][i]
            bl[len(bl) - 1][i] = top[i]
    raise ValueError()

def onCount(pat):
    return sum([sum([(0, 1)[x == '#'] for x in row]) for row in pat])

size = 3
pat = [list(x) for x in ['.#.', '..#', '###']]

mappings = {}
for li in sys.stdin:
    parts = li[0:-1].split(' => ')
    mappings[parts[0]] = parts[1].split('/')


for i in range(18):
    if size % 2 == 0:
        newsize = size // 2 * 3
        for r in range(0, newsize, 3):
            pat.insert(r + 2, ['.'] * size)
            for c in range(0, newsize, 3):
                bl = find([pat[r + i][c:c+2] for i in range(2)])
                for x in range(3):
                    pat[r + x][c:c+2] = bl[x]
    else:
        newsize = size // 3 * 4
        for r in range(0, newsize, 4):
            pat.insert(r + 3, ['.'] * size)
            for c in range(0, newsize, 4):
                bl = find([pat[r + i][c:c+3] for i in range(3)])
                for x in range(4):
                    pat[r + x][c:c+3] = bl[x]
    size = newsize

#    print('\n'.join([''.join(x) for x in pat]))
#    print('')
#    if i + 1 == 5 or i + 1 == 18:
    print(onCount(pat))

