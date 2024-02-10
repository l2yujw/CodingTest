from collections import deque
import sys
input = sys.stdin.readline

def bfs(x1, y1, x2, y2):
  queue = deque()
  queue.append((x1, y1))
  graph[x1][y1] = 0

  while queue:
    x, y = queue.popleft()
    if(x == x2 and y == y2):
      return graph[x2][y2]
    for i in range(4):
      for j in range(1, k + 1):
        nx = x + dx[i] * j
        ny = y + dy[i] * j
        if(nx < 0 or nx >= n or ny < 0 or ny >= m): break
        if(graph[nx][ny] == '#'): break
        if(graph[nx][ny] == '.'): 
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
        elif (graph[nx][ny] > graph[x][y]): continue
        else: break
  return -1

n, m, k = map(int, input().split()) 
graph = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split()) 
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(x1-1, y1-1, x2-1, y2-1))