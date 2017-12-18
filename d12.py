import sys, os
from functools import reduce

def dfs(adjList, visited = None, val = 0):
    if visited == None:
        visited = [False for x in adjList]
    if visited[val]:
        return 0
    visited[val] = True
    
    adjs = 0
    for x in adjList[val]:
        adjs += dfs(adjList, visited, x)
    return adjs + 1


adjList = []
for l in sys.stdin:
    adjList += [list(map(int, l.split(' <-> ')[1].split(', ')))]

visited = [False for x in adjList]
print(dfs(adjList))

groups = 0
for i in range(len(visited)): 
    if not visited[i]:
        dfs(adjList, visited, i)
        groups += 1
print(groups)
