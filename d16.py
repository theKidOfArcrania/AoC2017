import sys, os

def iterate(pos, moves):
    for mv in moves.split(','):
        if mv[0] == 's':
            x = int(mv[1:]) % len(pos)
            pos = pos[len(pos)-x:] + pos[:len(pos)-x]
        elif mv[0] == 'x':
            pt = mv[1:].split('/')
            a = int(pt[0])
            b = int(pt[1])

            tmp = pos[a]
            pos[a] = pos[b]
            pos[b] = tmp
        else:
            pt = mv[1:].split('/')
            a = pt[0]
            b = pt[1]
            times = 0
            for i in range(len(pos)):
                if pos[i] == a:
                    pos[i] = b
                    times += 1
                elif pos[i] == b:
                    pos[i] = a
                    times += 1
            assert times == 2
    return pos 


pos = [chr(i + 97) for i in range(16)]
moves = input()

maps = {}
ctr = {}
trunc = False

dd = 0
end = 1000000000
while dd < end:
    # Print for part 1
    if dd == 1:
        print(''.join(pos))
    bef = tuple(pos)
    if bef in maps: 
        if not trunc:
            # We found a cycle
            pos = list(maps[bef])
            cycleLen = dd - ctr[bef]
            dd += ((end - dd) // cycleLen) * cycleLen + 1
            trunc = True
        else:
            # Use precomputed table
            pos = maps[bef]
            dd += 1
        continue
    
    pos = iterate(pos, moves)
    ctr[bef] = dd
    maps[bef] = tuple(pos)
    dd += 1

# Print for part 2
print(''.join(pos)) 

