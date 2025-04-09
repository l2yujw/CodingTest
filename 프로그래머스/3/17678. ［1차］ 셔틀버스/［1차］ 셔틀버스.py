# 셔틀 m인승 09:00 총 n회 t분 간격 역에 도착
# 시간 딱코까진 태워줌
# 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각 구해라
# 같은 시각에 도착하면 제일 뒤에 섬
# 모든 크루는 23:59에 집에 돌아감
# HH:MM 형식

# n: 셔틀 운영 횟수, t: 운행 간격, m: 인승, timetable: 크루 대기열 도착 시각

# timetable sort
# for _ in range(n) current_time += t
# 현재시각 -t < timetable <= 현재시각
# m명 배열 제거
# 막차 남은자리 = m, if timetable ~m 마지막값 - 1
# 남은자리 > m, 출발시간
# 남은자리 < m, 마지막에 탄사람 시각 -1
def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def to_HHMM(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    crew = sorted([to_minutes(time) for time in timetable])
    bus_time = 540
    i = 0

    for round in range(n):
        onboard = []
        while i < len(crew) and crew[i] <= bus_time and len(onboard) < m:
            onboard.append(crew[i])
            i += 1

        if round == n - 1:
            if len(onboard) < m:
                return to_HHMM(bus_time)
            else:
                return to_HHMM(onboard[-1] - 1)

        bus_time += t