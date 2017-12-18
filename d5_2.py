table = []
while True:
    try:
        table += [int(input())]
    except:
        break

steps = 0
i = 0

while i >= 0 and i < len(table):
    t = table[i]
    if table[i] >= 3:
        table[i] -= 1
    else:
        table[i] += 1
    i += t
    steps += 1
print(steps)
