# 총단지수, 각 단지내 집 수 오름차순
from collections import deque

def bfs(y, x):
    n = len(matrix)
    q = deque([(y, x)])
    matrix[y][x] = 0
    cnt = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == 1:
                matrix[ny][nx] = 0
                q.append((ny, nx))
                cnt += 1

    return cnt


N = int(input())

matrix = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    matrix.append(list(map(int, input().rstrip())))

cnt = []

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 1:
            cnt.append(bfs(y, x))

cnt.sort()
print(len(cnt))
print(*cnt)