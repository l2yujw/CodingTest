N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
print(board[0][0:8])