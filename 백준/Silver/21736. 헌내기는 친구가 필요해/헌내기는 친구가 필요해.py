from collections import deque
from sys import stdin

input = stdin.readline

def bfs(y, x):
    global count
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 'X':
                if arr[ny][nx] == 'P':
                    count += 1
                arr[ny][nx] = 'X'
                q.append([ny, nx])


count = 0
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            arr[i][j] = 'X'
            bfs(i, j)
            break

if count == 0:
    print('TT')
else:
    print(count)
