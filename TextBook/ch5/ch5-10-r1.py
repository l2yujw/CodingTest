n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(y, x):
    if y <= -1 or y >= n or x <= -1 or x >= m:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        if dfs(i, j) == True:
            count += 1

print(count)




