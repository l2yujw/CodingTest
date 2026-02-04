def solution(s):
    answer = 0
    
    for i in s:
        if answer < 0:
            break
        answer = answer + 1 if i == '(' else answer -1
        
    return answer == 0