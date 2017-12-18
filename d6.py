import sys, re

parent = {}
tree = {}
isroot = {}

indivWeight = {}

for line in sys.stdin:
    line = line[:-1]
    parts = line.split(' -> ')
    parts2 = parts[0].split(' ')
    name = parts2[0]
    weight = int(parts2[1][1:-1])

    indivWeight[name] = weight

    if len(parts) < 2:
        children = []
    else:
        children = parts[1].split(', ')


    subtree = {}
    for c in children:
        isroot[c] = False
        parent[c] = name
        if (c in tree):
            ctree = tree[c]
        else:
            ctree = {}
        subtree[c] = ctree

    if name in parent:
        tree[name] = subtree
        tree[parent[name]][name] = subtree
    else:
        tree[name] = subtree
        isroot[name] = True


for x in isroot.keys():
    if isroot[x]:
        print(x)
        root = x

def weight(node):
    total = indivWeight[node]
    first = -1
    for c in reversed(list(tree[node].keys())):
        if first == -1:
            first = weight(c)
        else:
            w = weight(c)
            if first != w:
                print(c + ': ' + str(first) + ' but is ' + str(w) + '. Weight: '+ \
                        str(indivWeight[c]))
        total += first
    return total

weight(root)
