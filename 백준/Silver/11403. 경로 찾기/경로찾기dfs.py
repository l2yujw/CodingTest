n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if map[i][k] == 1 and map[k][j] == 1:
                map[i][j] = 1

for i in map:
    print(*i)