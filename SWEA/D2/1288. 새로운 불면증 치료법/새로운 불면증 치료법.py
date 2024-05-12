T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    visited = [False] * 10

    num = N
    while True:
        for i in str(num):
            if not visited[int(i)]:
                visited[int(i)] = True

        if False not in visited:
            break
        else:
            num += N

    print("#%d %d" % (test_case, num))
