# n개의 노드
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수
# 최단 경로로 이동했을때 간선의 개수가 가장 많은 노드
# vertex: 간선에 대한 정보, n: 노드의 개수 2<=n<=20000
from heapq import heappush, heappop

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    distance = [20001] * (n + 1)

    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    dijkstra(1, graph, distance)
    max_distance = max(distance[1:])
    for i in range(1, n + 1):
        if distance[i] == max_distance:
            answer += 1
    return answer


def dijkstra(start, graph, distance):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heappush(q, (cost, i))