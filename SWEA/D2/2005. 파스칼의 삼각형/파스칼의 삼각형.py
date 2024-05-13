T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[1] for _ in range(n)]
    for i in range(1, n):
        tmp = []
        for k in range(i):
            if k == (i - 1):
                res = 1
            else:
                res = arr[i - 1][k] + arr[i - 1][k + 1]
            tmp.append(res)
        arr[i] += tmp

    print(f"#{test_case}")
    for i in range(n):
        print(*arr[i])
