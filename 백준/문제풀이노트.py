N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

count = 0
minCount = 64
def change(check):
    global count
    count += 1
    if check == 'B':
        return 'W'
    else:
        return 'B'

def arrSort(arr):
    for y in range(8):
        if y > 0 and arr[y][0] == arr[y-1][0]:
            arr[y][0] = change(arr[y][0])
        for x in range(1, 8):
            if arr[y][x] == arr[y][x-1]:
                arr[y][x] = change(arr[y][x])

def arrSort2(arr):
    global count
    Sort1 = count
    count = 0
    arr[0][0] = change(arr[0][0])
    for y in range(8):
        if y > 0 and arr[y][0] == arr[y-1][0]:
            arr[y][0] = change(arr[y][0])
        for x in range(1, 8):
            if arr[y][x] == arr[y][x-1]:
                arr[y][x] = change(arr[y][x])
    count = min(count, Sort1)

def createArr(y ,x):
    arr = []
    for Y in range(8):
        arr.append(board[Y + y][x:x+8])
    return arr

for y in range(N - 7):
    for x in range(M - 7):
        tmp = createArr(y, x)
        tmp2 = createArr(y, x)
        arrSort(tmp)
        arrSort2(tmp2)
        minCount = min(minCount, count)
        count = 0

print(minCount)