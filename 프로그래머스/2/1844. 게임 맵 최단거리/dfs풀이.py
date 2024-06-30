answer = 100 * 100
def solution(maps):
    global answer
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for y in range(0, len(maps)):
        for x in range(0, len(maps[0])):
            if maps[y][x] == 0:
                visited[y][x] = True
    dfs(maps, visited, 0, 0, 1)
    if answer == 100*100:
        return -1
    else:
        return answer


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(maps, visited, y, x, cost):
    global answer
    if y == len(maps) - 1 and x == len(maps[0]) - 1:
        answer = min(answer, cost)
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
            dfs(maps, visited, ny, nx, cost + 1)
    visited[y][x] = False


# print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
