from sys import stdin
import sys
input = stdin.readline

sys.setrecursionlimit(10**7)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

res = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        res += 1

print(res)