# 거스름돈 n원
# 5원 거슬러줘야 할때 (1, 2, 5) 존재면
# 1원 5개, 1원 3개 2원 1개, 1원 1개, 2원 2개, 5원 1개

# n: 거스름돈, money: 돈의 종류
# dfs로 가장 큰 금액부터 시작
# if 마지막 화폐면:
#     if rest % 현재화폐 == 0: result += 1
#     return
# for i in range(rest // 현재 화폐 + 1):
#    dfs(rest - i * 현재화폐, 다음 화폐)
# return
# def solution(n, coins):
#     coins.sort(reverse=True)

#     def dfs(rest, idx):
#         coin = coins[idx]
#         if idx == len(coins) - 1:
#             return 1 if rest % coin == 0 else 0

#         count = 0
#         for i in range(rest // coin + 1):
#             count += dfs(rest - i * coin, idx + 1)
#         return count

#     return dfs(n, 0)

def solution(n, coins):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]
