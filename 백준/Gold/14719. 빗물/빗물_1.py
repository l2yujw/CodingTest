from sys import stdin

input = stdin.readline

H, W= map(int, input().split())
num = list(map(int, input().split()))

frame = [[0]*W for _ in range(H)]
posX = 0
for i in num:
    posY = H - 1
    for _ in range(i):
        frame[posY][posX] = 1
        posY -= 1
    posX += 1

total = 0
for i in range(H):
    wall = 0
    water = 0
    for x in range(W):
        if frame[i][x] == 1:
            wall += 1
            if wall == 2:
                total += water
                water = 0
                wall -= 1
        elif frame[i][x] == 0:
            if wall == 0:
                continue
            else:
                water += 1

print(total)