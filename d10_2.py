from functools import reduce

size = 256
def m(x):
    return x % size

line = list(range(size))

pos = 0
skip = 0
data = list(map(ord, input())) + [17,31,73,47,23]

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
print(('%02x'*len(xor)) % tuple(xor))
