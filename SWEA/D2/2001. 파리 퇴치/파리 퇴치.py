def find_fly(m, table):
    arr = []
    for x in table:
        tmp = []
        for k in range(len(x) - m + 1):
            s = 0
            for t in range(m):
                s += x[k + t]
            tmp.append(s)
        arr.append(tmp)

    res = []
    for x in range(len(arr) - m + 1):
        tmp = []
        for k in range(len(arr[0])):
            s = 0
            for t in range(m):
                s += arr[x + t][k]
            tmp.append(s)
        res.append(tmp)

    return res

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = find_fly(m, arr)

    maxNum = 0
    for res in result:
        maxNum = max(maxNum, max(res))

    print("#%d %d" % (test_case, maxNum))