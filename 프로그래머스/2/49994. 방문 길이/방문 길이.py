def solution(dirs):
    answer = 0

    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    inst = {'U':0, 'D':1, 'L':2, 'R':3}

    way = set()

    y, x = 0, 0
    for i in dirs:
        num = inst[i]
        ny, nx = y + dy[num], x + dx[num],
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            way.add(((y, x), (ny, nx)))
            way.add(((ny, nx), (y, x)))
            y, x = ny, nx

    return len(way) // 2