# 삼각형 꼭대기 -> 바닥 경로, 거쳐간 숫자의 합이 가장 큰
# 대각하단 좌우 가능
# list [7] [10 15] [max(18), max(11, 16)]
def solution(triangle):
    for i in range(1, len(triangle)):
        for k in range(i + 1):
            if k == 0:
                triangle[i][k] += triangle[i - 1][k]
            elif k == i:
                triangle[i][k] += triangle[i - 1][k - 1]
            else:
                triangle[i][k] += max(triangle[i - 1][k - 1], triangle[i - 1][k])
    return max(triangle[len(triangle) - 1])