# n명 입국 심사
# 한 심사대 동시에 한명
# 가장 앞 사람 비어 있는 곳으로 가서 심사
# 더 빨리 끝나는 심사대가 있으면 그곳으로 가서 심사

# n: 사람, times: 각 심사관 한명 심사 걸리는 시간
# return 모든 사람 심사 소요 시간 최솟값

def solution(n, times):
    
    answer = 0
    
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        p = sum(mid // time for time in times)
        
        if p >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer