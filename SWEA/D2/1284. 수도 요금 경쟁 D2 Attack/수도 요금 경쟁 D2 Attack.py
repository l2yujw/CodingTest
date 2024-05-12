T = int(input())
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())

    a = p * w
    b = q if w <= r else q + (s * (w - r))

    print("#%d %d" % (test_case, min(a, b)))