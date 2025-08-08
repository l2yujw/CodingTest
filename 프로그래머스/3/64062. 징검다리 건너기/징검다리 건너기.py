# 디딤돌 밟으면 -1
# 0되면 무시
# stones: 디딤돌 숫자, k: 점프력
# return 최대 몇명
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