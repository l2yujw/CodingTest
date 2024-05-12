T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    v, d = 0, 0
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for x in arr:
        if x[0] == 1:
            v += x[1]
        elif x[0] == 2:
            v -= x[1]
            if v < 0:
                v = 0
        d += v
    print("#%d %d" % (test_case, d))