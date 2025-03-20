def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    
    while left <= right:
        count = 0
        mid = (left + right) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break
        if count < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer