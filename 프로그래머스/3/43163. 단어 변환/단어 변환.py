# 한 번에 한 개의 알파벳 변경
# words에 있어야 함
from collections import deque

def solution(begin, target, words):
    return solve_bfs(begin, target, words)


def solve_dfs(begin, target, words):
    if target not in words:
        return 0
    
    answer = [int(1e9)]
    
    words = [begin] + words
    visited = [False] * len(words)
    graph = [[] for _ in range(len(words))]
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_changable(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)

    dfs(graph, visited, words, target, 0, 0, answer)
    
    return answer[0] if answer[0] != int(1e9) else 0

def is_changable(word, target):
    count = sum(word[i] != target[i] for i in range(len(word)))
    return count == 1
    
    
def dfs(graph, visited, words, target, v, count, answer):
    if words[v] == target:
        answer[0] = min(answer[0], count)
        return
    
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, words, target, i, count + 1, answer)
    visited[v] = False
    
def solve_bfs(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))

    while q:
        word, count = q.popleft()
        if word == target:
            return count

        for next_word in words:
            if is_changable(word, next_word):
                q.append((next_word, count + 1))

    return 0

