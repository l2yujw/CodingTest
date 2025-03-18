# N개의 아파트
# 4G -> 5G
# stations: 기지국 있는 아파트, W:전파 도달 거리

import math

def solution(n, stations, w):
    answer = 0

    dists = []
    for station in stations:
        dists.append([station - w, station + w])
    
    dists.sort(key = lambda x:x[0])
    length = w * 2 + 1
    
    pos = 1
    for dist in dists:
        if pos < dist[0]:
            answer += math.ceil((dist[0] - pos) / length)
        pos = dist[1] + 1

    if pos <= n:
        answer += math.ceil((n - pos + 1) / length)
    return answer