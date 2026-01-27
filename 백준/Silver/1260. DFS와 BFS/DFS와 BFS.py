from collections import deque

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for x in graph[v]:
        if not visited[x]:
            dfs(x, graph, visited)

def bfs(v, graph, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        l = q.popleft()
        print(l, end=' ')
        for x in graph[l]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


def solution(start, graph, type):
    visited = [False] * len(graph)
    if type == 'dfs':
        dfs(start, graph, visited)
    if type == 'bfs':
        bfs(start, graph, visited)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

solution(v, graph, "dfs")
print()
solution(v, graph, "bfs")