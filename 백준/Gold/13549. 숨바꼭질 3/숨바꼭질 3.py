from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

def bfs():
    visited = [-1] * 100001
    visited[n] = 0
    q = deque([n])

    while q:
        cur = q.popleft()

        if cur == k:
            return visited[cur]

        for v in (cur * 2, cur - 1, cur + 1):
            if 0 <= v < 100001 and visited[v] == -1:
                if v == cur * 2:
                    visited[v] = visited[cur]
                else:
                    visited[v] = visited[cur] + 1
                q.append(v)


print(bfs())