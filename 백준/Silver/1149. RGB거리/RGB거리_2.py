# RGB 중 하나로 칠함
# 1번집은 2번집과 다름
# N번집은 N-1번집의 색과 다름
# I번 집의 색은 I-1번 I+1번집의 색과 같지 않아야함

from sys import stdin
input = stdin.readline

def dfs(v, tot, pos):
    global res
    if v == n:
        res = min(res, tot)
        return
    for i in range(3):
        if i == pos:
            continue
        num = graph[v][i]
        tot += num
        dfs(v + 1, tot, i)
        tot -= num


n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
res = 1e9

dfs(0, 0, -1)
print(res)
#그니까 각 열마다 안겹치게 골라서 만든 합이 최소