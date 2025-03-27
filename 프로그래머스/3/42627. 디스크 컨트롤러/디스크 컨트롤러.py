import heapq
def solution(jobs):
    answer = 0
    
    j = 0
    now = 0
    start = -1
    heap = []
    while j < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))
        
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            j += 1
        else:
            now += 1
    
            
    return answer // len(jobs)