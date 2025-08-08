# m * n = 가로 * 세로
# 우, 하 이동가능
def solution(m, n, puddles):
    puddles = [[q, p] for p, q in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if y == 1 and x == 1:
                continue
            elif [y, x] in puddles:
                dp[y][x] = 0
            else:
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
                
    return dp[n][m] % 1000000007