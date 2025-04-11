# 모든 풍선 서로 다른 숫자 n개
# 1개 남을 때까지 계속 터티름
# 인접한 두 풍선 고르고 둘 중 하나 터트림
# 빈공간 생기면 압축
# 두 풍선 중 번호가 더 작은 풍선 터트리기 아이템은 1회
# 나머진 큰 숫자만 펑
def solution(a):
    n = len(a)
    if n <= 2:
        return n

    left_min = [0] * n
    right_min = [0] * n

    # 왼쪽 최소값 구하기
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽 최소값 구하기
    right_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    answer = 0
    for i in range(n):
        # 양쪽에서 최소값 중 하나라도 자신보다 크거나 같으면 살아남음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1

    return answer
