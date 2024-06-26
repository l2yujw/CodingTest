def solution(n, control):
    rule = {"w": 1, "s": -1, "d": 10, "a": -10}
    answer = n
    
    for i in control:
        answer += rule[i]
    
    return answer