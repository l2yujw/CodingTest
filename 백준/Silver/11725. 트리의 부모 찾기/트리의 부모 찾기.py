import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

dfs(1)
for i in range(2, n + 1):
    print(visited[i])