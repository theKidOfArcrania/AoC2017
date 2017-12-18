size = int(input())
def m(x):
    return x % size

line = list(range(size))

pos = 0
skip = 0
for l in map(int, input().split(',')):
    for off in range(l // 2):
        a = m(off + pos)
        b = m((l - off - 1) + pos)
        tmp = line[a]
        line[a] = line[b]
        line[b] = tmp
    pos = m(pos + skip + l) 
    skip += 1

print(line)
print(line[0] * line[1])
