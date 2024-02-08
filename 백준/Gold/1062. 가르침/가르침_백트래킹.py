# anta tica
# antic
#
# 5개가 default고
# 이후에 +된 알파벳 정하는데
# 입력된 단어들을 최대로 읽을 수 있게하는 +된 알파벳들을 세팅해서 최대를 찾는거

from sys import stdin

input = stdin.readline
N, K = map(int, input().split())

ANTA = "anta"
TICA = "tica"
ANTATICA = ["a", "n", "t", "i", "c"]
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']


sentences = [list(input().replace(ANTA, "").replace(TICA, "").strip()) for i in range(N)]

def choose_alpha(n, start):
    global result
    if n == 0:
        result = max(result, check())
        return
    for i in range(start, len(alpha_list)):
        ANTATICA.append(alpha_list[i])
        choose_alpha(n-1, i+1)
        ANTATICA.pop()

def check():
    result = 0
    for words in sentences:
        isRead = True
        for i in range(len(words)):
            if words[i] not in ANTATICA:
                isRead = False
                break
        if isRead:
            result += 1
    return result

result = 0
if K < 5:
    print(result)
else:
    choose_alpha(K-5, 0)
    print(result)