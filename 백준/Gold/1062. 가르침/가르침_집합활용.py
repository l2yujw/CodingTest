from itertools import combinations
from sys import stdin

input = stdin.readline

def solution():
    n, k = map(int, input().split())
    if k < 5:
        return 0
    k -= 5

    learned = set('antic')
    unlearned = set()
    cant_read_words = []
    can_read_cnt = 0

    for _ in range(n):
        word = set(input().rstrip()) - learned
        if word:
            unlearned.update(word)
            cant_read_words.append(word)
        else:
            can_read_cnt += 1

    if len(unlearned) <= k:
        return n

    answer = 0
    for comb in combinations(unlearned, k):
        comb = set(comb)
        cnt = 0
        for word in cant_read_words:
            if comb >= word:
                cnt += 1
        answer = max(answer, cnt)

    answer += can_read_cnt
    return answer


print(solution())