# n개 중복 집합 permutation
# {a, b} a+b=S, a*b := max => |a - b| := min
# {a, b, c} a+b+c=S, a*b*c := max => 차가 최소
def solution(n, s):
    if s < n:
        return [-1]
    
    base = s // n
    answer = list(base for _ in range(n))
    
    rest = s % n
    for i in range(0, rest):
        answer[i] += 1
        
    return sorted(answer)