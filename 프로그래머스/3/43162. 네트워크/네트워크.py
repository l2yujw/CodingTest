# A->B->C 연결시 같은 레벨 취급
# n(1<=n<=200): 컴퓨터의 개수, computers(0~n-1): 연결정보
# i j연결 => computers[i][j] == 1
# return 네트워크의 개수

def solution(n, computers):
    answer = 0

    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(computers, i, visited)
    
    return answer


def dfs(graph, v, visited):
    visited[v] = True
    
    for i in range(len(graph[v])):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)