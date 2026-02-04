# 2*N명 A:N B:N
# 모든 사원 무작위 자연수 하나씩
# 각각 한번 경기
# 양팀 한명씩 나와서 서로의 수 공개 => 큰쪽 우승
# B가 최종승점 최대로 이기는법

def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    return answer