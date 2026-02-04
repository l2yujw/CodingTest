# N개의 아파트
# 4G -> 5G
# stations: 기지국 있는 아파트, W:전파 도달 거리

# (5G 없는 각 범위 / 전파 범위) 올림 => 필요 기지국 갯수
import math

def solution(n, stations, w):
    answer = 0
    length = w * 2 + 1
    pos = 1
    for station in stations:
        if pos < station - w:
            answer += math.ceil((station - w - pos) / length)
        pos = station + w + 1

    if pos <= n:
        answer += math.ceil((n - pos + 1) / length)
    return answer