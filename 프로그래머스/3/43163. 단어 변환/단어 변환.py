# words[[begin, target]]
# 한 번에 한개의 알파벳만 변경 가능
# words에 있는 단어로만 변환 가능

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    return dfs(begin, target, words, visited, 0)

def dfs(current, target, words, visited, count):
    if current == target:
        return count
    
    min_count = float('inf')
    
    for i in range(len(words)):
        if not visited[i] and is_one_matched(current, words[i]):
            visited[i] = True
            result = dfs(words[i], target, words, visited, count + 1)
            if result:
                min_count = min(result, min_count)
            visited[i] = False
            
    return min_count if min_count != float('inf') else 0
            
def is_one_matched(word1, word2):
    diff_count = sum([word1[i] != word2[i] for i in range(len(word1))])
    return diff_count == 1
