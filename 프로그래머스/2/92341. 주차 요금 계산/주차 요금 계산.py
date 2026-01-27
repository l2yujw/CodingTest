import math

def solution(fees, records):
    parking_cars = {}   # 현재 주차중인 차량: car -> 입차시간
    parking_time = {}   # 누적 주차 시간: car -> minutes
    parking_fee = {}    # 최종 요금: car -> fee

    # 입출차 기록 처리
    for record in records:
        time, car, action = record.split()

        if action == "IN":
            parking_cars[car] = time
        else:  # OUT
            in_h, in_m = map(int, parking_cars[car].split(":"))
            out_h, out_m = map(int, time.split(":"))
            minutes = (out_h - in_h) * 60 + (out_m - in_m)

            parking_time[car] = parking_time.get(car, 0) + minutes
            parking_cars.pop(car)

    # 출차 안 한 차량 (23:59 처리)
    for car, time in parking_cars.items():
        in_h, in_m = map(int, time.split(":"))
        minutes = (23 - in_h) * 60 + (59 - in_m)
        parking_time[car] = parking_time.get(car, 0) + minutes

    # 요금 계산
    base_time, base_fee, unit_time, unit_fee = fees

    for car, total_time in parking_time.items():
        if total_time <= base_time:
            parking_fee[car] = base_fee
        else:
            parking_fee[car] = base_fee + math.ceil(
                (total_time - base_time) / unit_time
            ) * unit_fee

    # 차량 번호 순 정렬 후 결과 반환
    return [parking_fee[car] for car in sorted(parking_fee)]