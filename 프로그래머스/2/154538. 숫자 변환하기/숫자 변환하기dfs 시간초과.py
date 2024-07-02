# x를 y로 변환
# x + n / x * 2 / x * 3
answer = 1e6
def solution(x, y, n):
    global answer
    dfs(x, y, n, 0)
    if answer == 1e6:
        return -1
    else:
        return answer


def dfs(x, y, n, cost):
    global answer
    if x == y:
        answer = min(answer, cost)
        return

    if x > y:
        return

    dfs(x * 3, y, n, cost + 1)
    dfs(x * 2, y, n, cost + 1)
    dfs(x + n, y, n, cost + 1)

print(solution(10, 40, 5))