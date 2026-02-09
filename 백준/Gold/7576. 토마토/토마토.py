from collections import deque
from sys import stdin

input = stdin.readline

def sol():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append([i, j])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < n and 0 <= tx < m and box[ty][tx] == 0:
                box[ty][tx] = box[y][x] + 1
                queue.append((ty, tx))


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
res = 0

sol()

for i in box:
    if 0 in i:
        print(-1)
        exit()
    res = max(res, max(i))

print(res - 1)