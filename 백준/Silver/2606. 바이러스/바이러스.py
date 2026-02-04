def dfs(v):
    visited[v] = True
    cnt = 1
    for w in graph[v]:
        if not visited[w]:
            cnt += dfs(w)

    return cnt


c = int(input())
n = int(input())
graph = [[] for _ in range(c + 1)]
visited = [False] * (c + 1)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1) - 1)