# [번호, 요청 시각, 소요 시간]
# 우선순위 소요시간 -> 요청시각 -> 번호
# 

import heapq

def solution(jobs):
    answer = 0
    j = 0
    now = 0
    start = -1
    q = []
    
    while j < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
            
        if q:
            cur = heapq.heappop(q)
            start = now
            now += cur[0]
            answer += now - cur[1]
            j += 1
        else:
            now += 1
            
    return answer // len(jobs)
            