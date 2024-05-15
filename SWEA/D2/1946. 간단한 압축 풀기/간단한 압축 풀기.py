T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        a, n = map(str, input().split())
        arr.append([a, n])

    len = 0
    print(f"#{test_case}")
    for i in arr:
        for _ in range(int(i[1])):
            if len == 10:
                len = 0
                print()
                print(i[0], end="")
            else:
                print(i[0], end="")
            len += 1
    print()