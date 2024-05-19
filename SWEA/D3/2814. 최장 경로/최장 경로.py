def dfs(v, count):
    global length
    visited[v] = True
    for x in graph[v]:
        if not visited[x]:
            dfs(x, count + 1)
    visited[v] = False
    length = max(length, count)


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    count, length = 0, 0
    for i in range(1, n + 1):
        dfs(i, 1)

    print(f"#{test_case}", end=' ')
    print(length)