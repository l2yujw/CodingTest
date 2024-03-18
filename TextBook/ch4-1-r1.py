n = int(input())
a = list(input().split())

posX, posY = 1, 1
move = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in a:
    k = move.index(i)
    if posX + dx[k] < 1 or posY + dy[k] < 1:
        continue
    posX += dx[k]
    posY += dy[k]

print(posY, posX)