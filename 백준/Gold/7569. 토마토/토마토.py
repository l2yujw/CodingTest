from sys import stdin
from collections import deque
input = stdin.readline

queue = deque()
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for t in range(6):
            nz, ny, nx = z + dz[t], y + dy[t], x + dx[t]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append([nz, ny, nx])


m, n, h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dx = [0, 0, -1, 1, 0, 0]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append([i, j, k])

bfs()
flag = True
day = 0
for i in box:
    for j in i:
        if 0 in j:
            flag = False
        day = max(day, max(j))


if flag:
    print(day - 1)
else:
    print(-1)