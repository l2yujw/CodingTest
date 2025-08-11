# N*N 경주로
# 0:빈칸 1:벽
# (0,0) 시작, 도착(N-1,N-1)
# 상하좌우 벽 불가
# 직선 100원, 코너 500원
# 최소비용 구해라 = bfs why? 내가 다음 간 길이 무조건 최소

from collections import deque

def solution(board):
    return min(bfs(0, 0, 0, 1, board), bfs(0, 0, 0, 3, board))


def bfs(y, x, cost, dir, b):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    l = len(b)
    
    INF = int(1e9)
    
    visited = [[INF] * l for _ in range(l)]
    
    q = deque()
    q.append((y, x, cost, dir))
    
    while q:
        y, x, cost, dir = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < l and 0 <= nx < l and b[ny][nx] == 0:
                ncost = cost + (100 if i == dir else 600)
                if ncost < visited[ny][nx]:
                    visited[ny][nx] = ncost
                    q.append((ny, nx, ncost, i))
                    
    return visited[-1][-1]