T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    if n < m:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    else:
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))

    total = 0
    for i in range(len(b) - len(a) + 1):
        tmp = 0
        for k in range(len(a)):
            tmp += a[k] * b[k + i]
        total = max(total, tmp)

    print("#%d %d" % (test_case, total))