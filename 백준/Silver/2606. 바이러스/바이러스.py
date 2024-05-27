from sys import stdin
input = stdin.readline

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


c = int(input().rstrip())

net = int(input().rstrip())
graph = [[] for _ in range(c + 1)]

for i in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (c + 1)
dfs(1)
print(visited.count(True) - 1)