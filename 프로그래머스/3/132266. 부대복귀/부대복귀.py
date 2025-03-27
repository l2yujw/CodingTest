# 지역간 통과 시간 1
# 최단시간 부대 복귀
# 적군의 방해로 경로가 없어져 복귀 불가 부대원 존재가능
# n: 총지역의 수, roads: 두 지역 왕복 가능 길 [a,b] => 서로 왕복 가능
# sources: 각 부대원이 위치한 서로 다른 지역
# destinations: 강철부대 지역
# sources의 원소 순서대로 복귀할 수 있는 최단시간 return
# 복귀 불가능 -1

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    
    for s, d in roads:
        graph[s].append(d)
        graph[d].append(s)
        
    dist = bfs(n, graph, destination)
    
    for s in sources:
        answer.append(dist[s])

    return answer


from collections import deque
def bfs(n, graph, destination):
    dist = [-1] * (n + 1)
    q = deque([destination])
    dist[destination] = 0
    
    while q:
        cur = q.popleft()
        for g in graph[cur]:
            if dist[g] == -1:
                dist[g] = dist[cur] + 1
                q.append(g)
                
    return dist
    