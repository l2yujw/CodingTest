for test_case in range(1, 11):
    d = int(input())
    h = list(map(int, input().split()))
    for _ in range(d):
        if max(h) == min(h):
            break
        else:
            ma = h.index(max(h))
            mi = h.index(min(h))
            h[ma] -= 1
            h[mi] += 1

    print(f"#{test_case} {max(h) - min(h)}")