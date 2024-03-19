n, m = map(int, input().split())
posY, posX, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[posY][posX] = 1
# 0 1 2 3 북 동 남 서

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 북 -> 서 -> 남 -> 동
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 1
turnTime = 0
while True:
    turnLeft()
    ny = posY + dy[direction]
    nx = posX + dx[direction]
    if arr[ny][nx] == 0 and d[ny][nx] == 0:
        d[ny][nx] = 1
        posY = ny
        posX = nx
        count += 1
        turnTime = 0
    else:
        turnTime += 1

    if turnTime == 4:
        ny = posY - dy[direction]
        nx = posX - dx[direction]
        if arr[nx][ny] == 0:
            posY = ny
            posX = nx
        else:
            break
        turnTime = 0


print(count)