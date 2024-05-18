def check(y, x):
    if y > h - 1 or x > w - 1 or x < 0 or y < 0 or maze[y][x] in wall:
        return False
    else:
        return True


def destroy(y, x, d):
    see = direction.index(d)
    while y < h and x < w and y >= 0 and x >= 0:
        if maze[y][x] == '*':
            maze[y][x] = '.'
            break
        if maze[y][x] == '#':
            break
        y += posY[see]
        x += posX[see]


move = ['U', 'D', 'L', 'R']
posY = [-1, 1, 0, 0]
posX = [0, 0, -1, 1]

direction = ['^', 'v', '<', '>']
wall = ['*', '#', '-']

T = int(input())
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    maze = [list(map(str, input())) for _ in range(h)]
    n = int(input())
    order = input()

    curY, curX = 0, 0
    curD = ''
    for i in range(h):
        for k in range(w):
            if maze[i][k] in direction:
                curY, curX = i, k
                curD = maze[i][k]
                break

    for x in order:
        if x in move:
            index = move.index(x)
            tmpY, tmpX = curY + posY[index], curX + posX[index]
            curD = direction[index]
            if check(tmpY, tmpX):
                maze[curY][curX] = '.'
                curY, curX = tmpY, tmpX,
            maze[curY][curX] = curD
        if x == 'S':
            destroy(curY, curX, curD)

    print(f"#{test_case}", end=' ')
    for i in range(h):
        for k in range(w):
            print(maze[i][k], end='')
        print()