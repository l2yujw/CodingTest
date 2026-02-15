import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

zeros = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zeros.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(tmp):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    count = 0
    for i in range(N):
        count += tmp[i].count(0)
    return count

answer = 0

for walls in combinations(zeros, 3):
    tmp = copy.deepcopy(lab)
    for x, y in walls:
        tmp[x][y] = 1

    answer = max(answer, bfs(tmp))

print(answer)