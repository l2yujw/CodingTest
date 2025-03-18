# 모든 차량이 단속용 카메라를 한번은 만나도록
# routes: 차량 경로, 위 상황을 위한 최소 카메라
# (진입, 진출)
# -15 -13 -5 -3
# -20 -18 -14 -5

def solution(routes):
    routes.sort(key = lambda x: x[1])

    answer = 0
    key = -30001
    for route in routes:
        if route[0] > key:
            answer += 1
            key = route[1]
    return answer