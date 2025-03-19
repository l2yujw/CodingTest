# 특정 범위 다 가져옴
# 모든 종류의 보석을 적어도 1개 이상 포함하는 짧은 구간
from collections import defaultdict

def solution(gems):
    gem_types = set(gems)
    gem_count = defaultdict(int)
    left, right = 0, 0
    min_length = float('inf')
    answer = [0, len(gems)]
    
    while right < len(gems):
        gem_count[gems[right]] += 1
        right += 1

        while len(gem_count) == len(gem_types):
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right]

            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]
            left += 1

    return answer
