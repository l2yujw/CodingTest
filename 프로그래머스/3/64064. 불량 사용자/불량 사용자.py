from itertools import permutations

def is_match(user, ban):
    if len(user) != len(ban):
        return False
    return all(b == '*' or u == b for u, b in zip(user, ban))

def solution(user_id, banned_id):

    n = len(banned_id)
    results = set()

    for perm in permutations(user_id, n):
        if all(is_match(u, b) for u, b in zip(perm, banned_id)):
            results.add(frozenset(perm))

    return len(results)