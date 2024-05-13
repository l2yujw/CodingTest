T = int(input())
for tc in range(1, T + 1):
    arr = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        arr[i] = list(map(int, input().split()))
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    flag = 1
    for i in range(9):
        for j in range(9):
            num = arr[i][j]
            idx = (i // 3) * 3 + (j // 3)

            if num in rows[i] or num in cols[j] or num in boxes[idx]:
                flag = 0
            rows[i].add(num)
            cols[j].add(num)
            boxes[idx].add(num)
    print(f'#{tc} {flag}')