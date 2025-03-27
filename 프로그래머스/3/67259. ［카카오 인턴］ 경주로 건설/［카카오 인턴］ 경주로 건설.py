# N*N 경주로
# 0:빈칸 1:벽
# (0,0) 시작, 도착(N-1,N-1)
# 상하좌우 벽 불가
# 직선 100원, 코너 500원
# 최소비용 구해라
from collections import deque
def solution(board):
    answer = min(bfs(0, 0, 0, 1, board), bfs(0, 0, 0, 3, board))
    return answer


def bfs(y, x, cost, dir, b):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    l = len(b)
    
    visited = [[ [float('inf')] * 4 for _ in range(l)] for _ in range(l)]
    for d in range(4):
        visited[y][x][d] = 0
    
    q = deque()
    q.append((y, x, cost, dir))
    while q:
        y, x, cost, dir = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and b[ny][nx] == 0:
                if i == dir:
                    ncost = cost + 100
                else:
                    ncost = cost + 600
                
                if visited[ny][nx][i] > ncost:
                    visited[ny][nx][i] = ncost
                    q.append((ny, nx, ncost, i))
    return min(visited[-1][-1])