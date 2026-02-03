# dfs bfs 탐색
# 정점 여러개 -> 작은것 부터
# n:정점, m:간선, v:시작번호

from collections import deque

def dfs(v, graph, visited):
    visited[v] = True
    answer_dfs.append(v)
    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited)


def bfs(v, graph, visited):
    visited[v] = True
    answer_bfs.append(v)
    q = deque([v])
    while q:
        l = q.popleft()
        for w in graph[l]:
            if not visited[w]:
                visited[w] = True
                answer_bfs.append(w)
                q.append(w)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer_dfs = []
answer_bfs = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

dfs(v, graph, [False] * (n+1))
bfs(v, graph, [False] * (n+1))

print(*answer_dfs)
print(*answer_bfs)