# 아이디 일부 * 필터
# 제재 아이디 목록의 경우의수
# abc adc => a*c, 2가지 가능

def is_match(user, ban):
    if len(user) != len(ban):
        return False
    
    return all(b == '*' or u == b for u, b in zip(user, ban))


def dfs(idx, user_id, banned_id, visited, results):
    if idx == len(banned_id):
        results.add(frozenset(visited))
        return

    for i in range(len(user_id)):
        if i not in visited and is_match(user_id[i], banned_id[idx]):
            visited.add(i)
            dfs(idx + 1, user_id, banned_id, visited, results)
            visited.remove(i)

def solution(user_id, banned_id):
    results = set()
    dfs(0, user_id, banned_id, set(), results)
    return len(results)