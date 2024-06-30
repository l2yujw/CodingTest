# 자카드 유사도
# 두 집합 A, B 사이의 자카드 유사도 J(A,B) = 두집합의 교집합 크기 / 두집합의 합집합 크기
# ex) 1,2,3  2,3,4 -> 교 2 3 / 합 1 2 3 4 -> J(A,B) = 2/0.5
# 집합 A와 B가 모두 공집합 -> 1

# 1이3개 1이5개 -> 교 3 합 5
# 1,1,2,2,3  1,2,2,4,5 -> 교 1 2 2 / 합 1 1 2 2 3 4 5 -> J(A, B) = 3/7=0.42

# 문자열 활용
# FRANCE FRENCH -> 두글자씩 끊기 ->  {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH} -> 교 {FR, NC}/합  {FR, RA, AN, NC, CE, RE, EN, CH}
# J("FRANCE", "FRENCH") = 2/8 = 0.25

# 특수문자는 버림
# 대소문자 무시
# 최종 결과에 65536 곱 후 int형
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    left = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    right = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    gyo = set(left)
    print(gyo)
    print(set(left) & set(right))

    if len(left) == 0 and len(right) == 0:
        return 1 * 65536

    tot = len(left) + len(right)
    cross = 0
    if len(left) > len(right):
        for v in right:
            if v in left:
                left.remove(v)
                cross += 1
    else:
        for v in right:
            if v in left:
                left.remove(v)
                cross += 1
    tot -= cross

    J = int((cross / tot) * 65536)

    return J



# print(solution(	"handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))