# n명 입국심사
# 한 심사대에 한명, 가장 앞에 서 있는 사람 비어있는 심사대
# 모든 사람이 심사를 받는데 걸리는 시간 최소

def solution(n, times):
    answer = 0
    
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        p = 0
        for time in times:
            p += mid // time
            if p >= n:
                break
        
        if p >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer