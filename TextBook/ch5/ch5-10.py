n, m = map(int(input()))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)