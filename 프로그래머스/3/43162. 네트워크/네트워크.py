# A->B->C 연결시 같은 레벨 취급
# n(1<=n<=200): 컴퓨터의 개수, computers(0~n-1): 연결정보
# i j연결 => computers[i][j] == 1
# return 네트워크의 개수

def solution(n, computers):
    answer = 0

    graph = [[] * _ for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    visited = [False] * n
    
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(graph, i, visited)
    
    return answer


def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)