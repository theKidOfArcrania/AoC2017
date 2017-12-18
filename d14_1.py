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

used = 0
start = input()
for i in range(128):
    used += hamming(hash(start + '-' + str(i)))

print(used)
