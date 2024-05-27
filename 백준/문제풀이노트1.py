from sys import stdin
from collections import deque
input = stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, y, x):
    n = len(graph)
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    count = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                count += 1
    return count


n = int(input().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))
cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])