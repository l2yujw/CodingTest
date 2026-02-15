from sys import stdin
import sys
input = stdin.readline

sys.setrecursionlimit(10**7)
def dfs(v):
    visited[v] = True
    for x in graph[v]:
        if not visited[x]:
            dfs(x)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
