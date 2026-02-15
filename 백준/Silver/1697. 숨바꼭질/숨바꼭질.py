from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
limit = 100000
visited = [0] * (limit + 1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= limit and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)


bfs()