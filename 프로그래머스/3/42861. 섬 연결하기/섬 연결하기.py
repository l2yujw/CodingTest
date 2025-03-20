# n개의 섬, costs: n개의 섬사이에 다리 건설 비용
# 최소 비용 모든 섬 통행 가능하도록
# return 최소비용
# 각각 출발
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connect = set([costs[0][0]])
    
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
    
