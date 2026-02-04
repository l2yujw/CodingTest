# tickets: 항공권 정보
# ICN 출발
# 가능 경로가 2개 이상이면 알파벳 순서

def solution(tickets):
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    tickets.sort(key = lambda x: x[1], reverse = True)
    for start, end in tickets:
        graph[start].append(end)
    
    route = []
    
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)
    
    dfs("ICN")
    return route[::-1]
