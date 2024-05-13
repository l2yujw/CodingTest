T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    row, col, box = [], [], []
    pat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for y in range(9):
        row.append(arr[y])
        tmp = []
        for x in range(9):
            tmp.append(arr[x][y])
        col.append(tmp)

    for x in range(0, 9, 3):
        tmp = []
        for y in range(9):
            tmp += arr[y][x: x + 3]
            if y % 3 == 2:
                box.append(tmp)
                tmp = []

    for y in range(9):
        if sorted(row[y]) != pat or sorted(col[y]) != pat or sorted(box[y]) != pat:
            result = 0
            break

    print("#%d %d" % (test_case, result))