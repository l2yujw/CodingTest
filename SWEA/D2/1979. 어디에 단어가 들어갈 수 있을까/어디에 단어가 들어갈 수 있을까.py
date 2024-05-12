T = int(input())
for test_case in range(1, T + 1):
    n , k =map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    block = 0
    for i in range(n):
        for x in range(n + 1):
            if x == n or board[i][x] == 0:
                if block == k:
                    result += 1
                block = 0
            else:
                block += 1
        block = 0

        for x in range(n + 1):
            if x == n or board[x][i] == 0:
                if block == k:
                    result += 1
                block = 0
            else:
                block += 1
        block = 0

    print("#%d %d" %(test_case, result))